# Working Capital Analyst

## Use when
- User provides financial statement data and wants working capital ratios calculated
- You need to compute Debtor Days (DSO), Creditor Days (DPO), Inventory Days (DIO), Cash Conversion Cycle
- User asks "What is our cash conversion cycle?" or "How fast are we collecting receivables?"
- Company financial health check focusing on liquidity and working capital efficiency

## Core principle
- Working capital ratios reveal how efficiently a company manages its short-term liquidity — slow collections or bloated inventory tie up cash that could be reinvested
- Each ratio has an industry benchmark — flag values that are significantly outside norms

## The Process

### Step 1: Gather Required Data
From the most recent financial statements (or projection JSON):
- **Revenue** (Income Statement) — used for Debtor Days
- **COGS** (Income Statement) — used for Creditor Days and Inventory Days
- **Accounts Receivable** (Balance Sheet) — end-of-period value
- **Inventory** (Balance Sheet) — end-of-period value (if applicable)
- **Accounts Payable** (Balance Sheet) — end-of-period value
- **Cash** (Balance Sheet) — optional, for cash-based working capital

### Step 2: Run the Calculator
```bash
python scripts/working_capital_calculator.py <input.json> [--output output.json] [--benchmark retail|manufacturing|saas|services]
```

Input JSON schema:
```json
{
  "revenue": 10000000,
  "cogs": 5500000,
  "accounts_receivable": 1425000,
  "inventory": 800000,
  "accounts_payable": 900000,
  "cash": 1500000
}
```

### Step 3: Interpret Results
After running the script, you'll receive:
- **Working Capital** = Current Assets - Current Liabilities
- **Working Capital Ratio** = Current Assets / Current Liabilities (benchmark: >1.2)
- **Debtor Days (DSO)** = (AR / Revenue) × 365 (benchmark: 30-45 days)
- **Creditor Days (DPO)** = (AP / COGS) × 365 (benchmark: 30-60 days)
- **Inventory Days (DIO)** = (Inventory / COGS) × 365 (benchmark: 30-60 days for retail/manufacturing)
- **Cash Conversion Cycle** = DS0 + DIO - DP0 (benchmark: <60 days)

### Step 4: Flag Concerns
Present results with flags:
- 🔴 **Red Flag:** DS0 > 60 days (slow collections)
- 🟡 **Yellow Flag:** DP0 > 90 days (stretching payables dangerously)
- 🔴 **Red Flag:** Cash Conversion Cycle > 90 days (cash trap)
- 🟡 **Yellow Flag:** Working Capital Ratio < 1.0 (liquidity concern)

### Step 5: Report to User
Provide a concise summary:
```
Working Capital Analysis for [Company]:
- Working Capital: $2.5M (Ratio: 1.4x — healthy)
- Debtor Days: 45 days (benchmark: 30-45) — acceptable
- Creditor Days: 60 days (benchmark: 30-60) — acceptable
- Inventory Days: 53 days (benchmark: 30-60) — slightly high, investigate slow-moving stock
- Cash Conversion Cycle: 38 days — excellent (benchmark: <60)
```

## Red Flags

- **Negative Working Capital** — Company may face short-term liquidity crisis (flag for user review)
- **DS0 > 90 days** — Collections process is broken, cash flow will suffer
- **DP0 > 120 days** — Supplier relationships at risk, may lose credit terms
- **DIO not applicable but Inventory > 0** — possible data error for service/SaaS companies
- **Revenue = 0 or COGS = 0** — cannot calculate ratios, ask user for valid data
- **Inventory > 20% of Current Assets** for a SaaS company — unusual, flag for review

## Script Dependencies
- **None** — uses Python standard library only (`json`, `sys`, `argparse`)
- Works anywhere Python runs

## Reference
- `references/working-capital-benchmarks.md` — industry benchmarks, interpretation guide, common pitfalls

## Asset
- `assets/sample_financials.json` — example input with realistic values for a $10M revenue company