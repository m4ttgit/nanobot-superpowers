# Financial Research Report Generator#

## Use when
- User requests a "financial research report", "investment analysis", or "should I buy/hold/sell [stock]?"
- You have financial statement data and need to produce a professional research report
- Due diligence is required before making investment decisions
- User wants all financial ratios analyzed in one comprehensive document

## Core principle
- A proper research report combines quantitative analysis (ratios) with qualitative assessment (risks, outlook)
- The report must be audit-ready: clear methodology, cited benchmarks, logical conclusions
- Investment recommendations must be backed by data, not opinions

## The Process

### Step 1: Validate Input Data
Before generating, confirm the JSON contains:
- `company_name`, `currency`, `fiscal_year`
- `income_statement`: Revenue, COGS, Operating Expenses, EBIT, Net Income
- `balance_sheet`: Current Assets, Current Liabilities, Total Assets, Total Equity, Debt
- `cash_flow`: Operating Cash Flow, Free Cash Flow
- `assumptions` (if projection-based report)

If any section is missing, report what's missing before proceeding.

### Step 2: Calculate All Financial Ratios
The script calculates 5 categories of ratios:

**Profitability Ratios:**
- Gross Margin % = Gross Profit ÷ Revenue
- Operating Margin % = EBIT ÷ Revenue  
- Net Margin % = Net Income ÷ Revenue
- Return on Assets (ROA) = Net Income ÷ Total Assets
- Return on Equity (ROE) = Net Income ÷ Total Equity
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

**Valuation Ratios:**
- P/E Ratio = Market Cap ÷ Net Income (if provided)
- P/B Ratio = Market Cap ÷ Total Equity (if provided)
- EV/EBITDA = Enterprise Value ÷ EBITDA (if provided)
- PEG Ratio = P/E ÷ Earnings Growth Rate (if provided)

### Step 3: Run the Report Generator
```bash
python scripts/financial_report_generator.py <input.json> --output <report.docx> --company-name "Acme Corp" --recommendation buy
```

**Input JSON Schema:**
```json
{
  "company_name": "Acme Corp",
  "currency": "USD",
  "fiscal_year": "FY2024",
  "income_statement": {
    "revenue": 10000000,
    "cogs": 5500000,
    "operating_expenses": 2500000,
    "ebit": 2000000,
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
  "cash_flow": {
    "operating_cash_flow": 1655000,
    "free_cash_flow": 1155000
  }
}
```

### Step 4: Verify the Report
After generation, verify the Word document contains:
- **Executive Summary** with investment recommendation
- **Profitability Analysis** with margin trends
- **Liquidity Analysis** with current/quick ratios
- **Leverage Analysis** with debt ratios
- **Efficiency Analysis** with turnover metrics
- **Valuation Analysis** (if market data provided)
- **Risk Assessment** with red/yellow flags
- **Appendix** with complete ratio tables

### Step 5: Present to User
Report the full path to the generated Word document. If Excel models were also built (via `nanobot-excel-projection-builder`), reference them in the report and link the files.

## Report Structure

### 1. Executive Summary
- Company overview and fiscal year
- Key financial highlights (Revenue, EBITDA, Net Income)
- Investment recommendation (Buy/Hold/Sell) with target price
- Summary of key risks and opportunities

### 2. Profitability Analysis
- Revenue growth analysis (YoY)
- Margin analysis (Gross, Operating, Net)
- ROA and ROE trends
- EBITDA performance
- **Flags:** Declining margins, negative ROE, contracting EBITDA

### 3. Liquidity Analysis
- Current Ratio and Quick Ratio trends
- Working capital changes
- Cash position and burn rate
- **Flags:** Current Ratio < 1.2, Quick Ratio < 1.0, Negative Working Capital

### 4. Leverage Analysis
- Debt-to-Equity and Debt-to-Assets
- Interest coverage ratio
- Financial leverage trends
- **Flags:** D/E > 2.0, Interest Coverage < 2.5, Over-leveraged

### 5. Efficiency Analysis
- Asset, Inventory, and Receivables Turnover
- Days Sales Outstanding (DSO)
- Cash Conversion Cycle
- **Flags:** DS0 > 60 days, DIO > 90 days, Low turnover ratios

### 6. Valuation Analysis (if market data)
- P/E, P/B, EV/EBITDA ratios
- Comparison to industry peers
- PEG ratio (growth-adjusted)
- **Flags:** Overvalued (P/E > 30), Undervalued (P/E < 10)

### 7. Risk Assessment
- Red Flags (critical issues requiring immediate attention)
- Yellow Flags (areas for improvement)
- Mitigating factors
- Scenario analysis (base/bull/bear cases)

### 8. Investment Recommendation
- Clear Buy/Hold/Sell with target price
- Time horizon (short/medium/long-term)
- Key catalysts and risk factors
- Confidence level (High/Medium/Low)

## Red Flags

- **Insufficient data** — Cannot calculate 3+ ratio categories, ask user for complete statements
- **Negative Net Income** — Company is unprofitable, flag for turnaround risk
- **Current Ratio < 1.0** — Liquidity crisis imminent, flag as Red
- **D/E > 3.0** — Over-leveraged, financial distress risk
- **DS0 > 90 days** — Collections broken, cash flow will suffer
- **Revenue declining > 15% YoY** — Business model under pressure
- **Negative Working Capital** — Cannot meet short-term obligations

## Script Dependencies
- **python-docx** — for Word document generation
  - Install: `pip install python-docx`
  - If not installed, script exits with clear error message
- **No pandas/openpyxl required** — pure stdlib + python-docx

## Reference
- `references/financial-reporting-standards.md` — professional report format, disclaimer templates, common ratios
- `references/ratio-interpretation.md` — benchmark values, industry-specific norms

## Asset
- `assets/sample_report_input.json` — complete input with all financial statement data
- `assets/sample_report_output.json` — example output structure with all calculated ratios