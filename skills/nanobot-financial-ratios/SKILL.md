# Financial Ratios#

## Use when
- User provides financial statement data and wants ALL 5 categories of ratios calculated
- Need a single script that calculates everything (Profitability, Liquidity, Leverage, Efficiency, Valuation)
- Building a comprehensive financial analysis#

## Core principle
- Calculate ALL ratios in one pass — no need to run multiple scripts
- Each ratio has a benchmark — flag outliers immediately
- Return structured JSON — ready for report generation#

## The Process#

### Step 1: Gather Required Data
From the financial statements (or projection JSON):
- **Income Statement:** Revenue, COGS, Gross Profit, EBIT, EBITDA, Net Income, Interest Expense
- **Balance Sheet:** Cash, Accounts Receivable, Inventory, Current Assets, Total Assets, Accounts Payable, Current Liabilities, Total Debt, Total Equity
- **Market Data (optional):** Market Cap, Enterprise Value, Earnings Growth Rate#

### Step 2: Run the Calculator
```bash
python scripts/financial_ratios.py <input.json> [--output output.json] [--market-cap 300M] [--enterprise-value 320M] [--growth-rate 0.15]
```

Input JSON schema:
```json
{
  "income_statement": {
    "revenue": 10000000,
    "cogs": 5500000,
    "gross_profit": 4500000,
    "ebit": 2000000,
    "ebitda": 2200000,
    "interest": 160000,
    "net_income": 1500000
  },
  "balance_sheet": {
    "cash": 1500000,
    "accounts_receivable": 1425000,
    "inventory": 800000,
    "current_assets": 3725000,
    "total_assets": 7725000,
    "accounts_payable": 900000,
    "current_liabilities": 1300000,
    "total_debt": 2000000,
    "total_equity": 4425000
  },
  "market_cap": 30000000,
  "enterprise_value": 32000000,
  "growth_rate": 0.15
  "auditor_opinion": "Unqualified"
}
```

### Step 3: Interpret Results
The script returns ALL 5 categories:

**Profitability Ratios:**
- Gross Margin % = Gross Profit ÷ Revenue
- Operating Margin % = EBIT ÷ Revenue  
- Net Margin % = Net Income ÷ Revenue
- ROA = Net Income ÷ Total Assets
- ROE = Net Income ÷ Total Equity
- EBITDA Margin = EBITDA ÷ Revenue

**Liquidity Ratios:**
- Current Ratio = Current Assets ÷ Current Liabilities
- Quick Ratio = (Current Assets - Inventory) ÷ Current Liabilities
- Working Capital = Current Assets - Current Liabilities
- Cash Ratio = Cash ÷ Current Liabilities

**Leverage Ratios:**
- Debt-to-Equity = Total Debt ÷ Total Equity
- Debt-to-Assets = Total Debt ÷ Total Assets
- Interest Coverage = EBIT ÷ Interest Expense
- Financial Leverage = Total Assets ÷ Total Equity

**Efficiency Ratios:**
- Asset Turnover = Revenue ÷ Total Assets
- Inventory Turnover = COGS ÷ Inventory (if applicable)
- Receivables Turnover = Revenue ÷ Accounts Receivable
- Days Sales Outstanding (DSO) = (AR ÷ Revenue) × 365
- Days Payable Outstanding (DPO) = (AP ÷ COGS) × 365
- Cash Conversion Cycle = DS0 + DIO - DP0

**Valuation Ratios (if market data):**
- P/E Ratio = Market Cap ÷ Net Income
- P/B Ratio = Market Cap ÷ Total Equity
- EV/EBITDA = Enterprise Value ÷ EBITDA
- PEG Ratio = P/E ÷ Earnings Growth Rate#

### Step 4: Flag Concerns
The script automatically flags:
- 🔴 **Red Flag:** Current Ratio < 1.0, DS0 > 60, P/E > 30, ROE < 0
- 🟡 **Yellow Flag:** Current Ratio 1.0-1.2, DS0 45-60, P/E 20-30#

### Step 5: Report to User
Provide a structured summary with all ratios organized by category, flags highlighted, and benchmark comparisons.#

## Red Flags#

- **Negative Working Capital** — Company may face short-term liquidity crisis
- **DS0 > 90 days** — Collections process is broken
- **DP0 > 120 days** — Supplier relationships at risk
- **DIO not applicable but Inventory > 0** — Data error for service/SaaS
- **P/E > 30** — Potentially overvalued
- **Interest Coverage < 2.5** — Debt servicing risk#

## Script Dependencies
- **None** — Uses Python standard library only (`json`, `sys`, `argparse`)
- Works anywhere Python runs#

## Reference
- `references/ratio-interpretation.md` — Benchmark values, industry-specific norms, flag thresholds#

## Asset
- `assets/sample_ratios_input.json` — Example with all financial statement data