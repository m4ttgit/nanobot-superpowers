# Bankruptcy Scorer#

## Use when
- User asks "Will [company] go bankrupt?" or "What's the bankruptcy risk?"
- You have financial statement data and need statistical bankruptcy prediction
- Due diligence requires assessing corporate failure probability#
## Core principle
- **Two proven models** — Altman Z-Score (general manufacturing) + Beneish M-Score (earnings manipulation detection)
- **Statistical rigor** — These models have 80-95% accuracy in predicting bankruptcy within 2 years
- **Red flag immediately** — Z-Score < 1.8 or M-Score > -1.78 means high risk#

## The Process#

### Step 1: Gather Required Data
From the financial statements:
- **Working Capital** = Current Assets - Current Liabilities
- **Retained Earnings** = Total Equity - Paid-in Capital (or use RE from statements)
- **EBIT** = Operating Income  
- **Market Value of Equity** (or Book Value if market data unavailable)
- **Sales/Revenue** = Total Revenue#
- **Total Assets** = From Balance Sheet#
- **Beneish-specific:**  
  - **Net Income** = From Income Statement
  - **Cash Flow from Operations** = From Cash Flow Statement
  - **Total Debt** = Current Liabilities + Long-term Debt
  - **Cumulative Depreciation** = Accumulated Depreciation#

### Step 2: Run the Scorer#
```bash
python scripts/bankruptcy_scorer.py <input.json> [--output output.json] [--market-value 300M]
```

**Input JSON schema:**
```json
{
  "income_statement": {
    "revenue": 10000000,
    "ebit": 2000000,
    "net_income": 1500000
  },
  "balance_sheet": {
    "current_assets": 3725000,
    "current_liabilities": 1300000,
    "total_assets": 7725000,
    "total_equity": 4425000,
    "reteined_earnings": 1500000
  },
  "cash_flow": {
    "operating_cash_flow": 1655000
  },
  "total_debt": 2000000,
  "market_value_equity": 30000000,
  "cumulative_depreciation": 500000
}
```

### Step 3: Interpret Results
The script returns:

**Altman Z-Score (for public manufacturers):**
```
Z-Score = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E
Where:
  A = Working Capital / Total Assets
  B = Retained Earnings / Total Assets  
  C = EBIT / Total Assets
  D = Market Value of Equity / Total Liabilities
  E = Sales / Total Assets#

Z-Score Interpretation:
- Z > 2.99 → Safe Zone (bankruptcy unlikely)
- 1.81 < Z < 2.99 → Grey Zone (caution)
- Z < 1.81 → Distress Zone (high bankruptcy risk)
```

**Beneish M-Score (earnings manipulation):**
```
M-Score = -4.84 + 0.92DSR + 0.528GMI + 0.404GMI + 0.892ACCRUAL + 0.32LEVI + 0.66SGI + 0.047DEP + 0.65SGAI
Where:
  DSR = (Net Income_t / Cash Flow_t) / (Net Income_t-1 / Cash Flow_t-1)
  GMI = (Sales_t / Total Assets_t) / (Sales_t-1 / Total Assets_t-1)
  ACRRUAL = (Net Income - Cash Flow) / Total Assets#
  LEVI = (Total Debt / Total Assets) / (Total Debt_t-1 / Total Assets_t-1)
  SGI = Sales_t / Sales_t-1
  DEP = Depreciation_t / (Depreciation_t + PP&E_t)
  SGAI = (SG&A_t / Sales_t) / (SG&A_t-1 / Sales_t-1)#
M-Score Interpretation:
- M > -1.78 → High probability of earnings manipulation
- M < -2.22 → Low probability of manipulation
```

### Step 4: Flag Concerns
Present results with flags:
```
Bankruptcy Risk Analysis for [Company]:
- Altman Z-Score: 1.45 (Distress Zone — 🔴 HIGH bankruptcy risk)
- Beneish M-Score: -1.2 (🟡 Moderate manipulation risk — review accruals)
```

### Step 5: Report to User
Provide clear assessment:
- **Safe (Z > 2.99 + M < -2.22)** → Low bankruptcy risk#
- **Caution (1.81 < Z < 2.99)** → Monitor closely#
- **Distress (Z < 1.81)** → 🔴 HIGH risk — recommend Sell#
- **Manipulation likely (M > -1.78)** → 🔴 Flag for forensic accounting review#

## Red Flags#

- **Z-Score < 1.81** — Company in distress zone, bankruptcy likely within 2 years#
- **M-Score > -1.78** — Earnings likely manipulated, investigate accruals#
- **Cannot calculate Z-Score** — Missing Total Assets or Market Value#
- **Cannot calculate M-Score** — Missing Cash Flow or prior-year data#
- **Z-Score < 0** — Company already in severe financial distress#

## Script Dependencies
- **None** — Uses Python standard library only (`json`, `sys`, `argparse`, `math`)#
## Reference
- `references/bankruptcy-models.md` — Altman Z-Score formulas, Beneish M-Score variables, industry adjustments#

## Asset
- `assets/sample_input.json` — Example with realistic values for a $10M revenue company