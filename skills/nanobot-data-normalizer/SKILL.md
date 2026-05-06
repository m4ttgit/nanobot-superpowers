# Data Normalizer#

## Use when
- User provides financial data in a non-standard format (XBRL, proprietary chart of accounts, or inconsistent naming)
- Need to map diverse account names to a unified schema
- Building a pipeline that ingests multiple companies' data#

## Core principle
- **Standardization enables comparison** — All companies must use the same field names for meaningful analysis
- **Map, don't rename** — Preserve original data in `_original` fields
- **Infer missing fields** — Use heuristics (e.g., "Cost of Sales" → COGS)#

## The Process#

### Step 1: Detect Input Format
Check the input JSON structure:
- **XBRL format:** Has `xbrl_context`, `xbrl_units`, `xbrl_facts`
- **Proprietary CoA:** Has `chart_of_accounts` with custom account names
- **Standard:** Already uses `income_statement`, `balance_sheet`, `cash_flow` — pass through#

### Step 2: Run the Normalizer
```bash
python scripts/data_normalizer.py <input.json> --output normalized.json [--format xbrl|proprietary|standard] [--company-name "Acme Corp"]
```

Input examples:

**XBRL Format:**
```json
{
  "xbrl_context": {"entity": "ACME", "period": "FY2024"},
  "xbrl_facts": [
    {"concept": "Revenue", "value": 10000000, "unit": "USD"},
    {"concept": "CostOfGoodsSold", "value": 5500000},
    {"concept": "NetIncomeLoss", "value": 1500000}
  ]
}
```

**Proprietary CoA:**
```json
{
  "company_name": "Acme Corp",
  "chart_of_accounts": [
    {"account": "1000 - Sales Revenue", "value": 10000000},
    {"account": "5000 - Cost of Sales", "value": 5500000},
    {"account": "9000 - Net Earnings", "value": 1500000}
  ]
}
```

### Step 3: Mapping Logic
The script applies mapping rules:

**XBRL → Standard:**
- `Revenue` / `SalesRevenueNet` → `income_statement.revenue`
- `CostOfGoodsSold` / `CostOfSales` → `income_statement.cogs`
- `NetIncomeLoss` → `income_statement.net_income`

**Proprietary → Standard (heuristics):**
- Account starts with "1" or contains "Asset" → Balance Sheet
- Account starts with "2" or contains "Liability" → Balance Sheet  
- Account starts with "3" or contains "Revenue/Sales" → Income Statement
- Account starts with "4" or contains "Expense/Cost" → Income Statement
- Account contains "Inventory" → Balance Sheet (inventory field)
- Account contains "Receivable" → Balance Sheet (accounts_receivable)
- Account contains "Payable" → Balance Sheet (accounts_payable)#

### Step 4: Verify Output
The normalized JSON must have:
```json
{
  "company_name": "Acme Corp",
  "fiscal_year": "FY2024",
  "currency": "USD",
  "income_statement": {
    "revenue": 10000000,
    "cogs": 5500000,
    "_original_revenue_field": "1000 - Sales Revenue"
  },
  "balance_sheet": {
    "cash": 1500000,
    "accounts_receivable": 1425000,
    "inventory": 800000,
    "total_assets": 7725000,
    "total_equity": 4425000
  }
}
```

### Step 5: Report to User
- Confirm normalization completed
- List fields that were mapped vs. inferred
- Flag any required fields still missing after normalization#

## Red Flags#

- **Cannot map 3+ required fields** — Input format not recognized, ask user for standard format
- **All account names are numeric** — Proprietary CoA with no hints, use industry heuristics
- **Negative values in Revenue/Assets** — Data error, flag for user review
- **XBRL has no context** — Cannot determine fiscal period, flag as limitation#

## Script Dependencies
- **None** — Uses Python standard library only (`json`, `sys`, `re`, `argparse`)
- Heuristic-based mapping (no ML required)#

## Reference
- `references/account-mapping.md` — Complete mapping rules for XBRL, proprietary CoA, and edge cases#

## Asset
- `assets/sample_xbrl_input.json` — XBRL example
- `assets/sample_proprietary_coa.json` — Proprietary chart of accounts example