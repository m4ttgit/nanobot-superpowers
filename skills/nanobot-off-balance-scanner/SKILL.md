## Use when
- User asks to detect off-balance sheet items
- Analyzing notes to financial statements for hidden liabilities
- Assessing lease obligations (operating leases post-IFRS 16/ASC 842)
- Identifying special purpose entities (SPEs) or variable interest entities (VIEs)
- Evaluating joint venture disclosures
- Checking for unconsolidated subsidiaries

## Core principle
Off-balance sheet items distort leverage ratios. Always re-calculate leverage metrics including these obligations.

## The Process
1. **Read Input**: Normalized financial data + notes to financial statements
2. **Scan for Off-Balance Items**:
   - Operating lease obligations (post-IFRS16/ASC842: right-of-use assets/lease liabilities)
   - Finance leases (capital leases)
   - Guarantees and contingent liabilities
   - SPE/VIE interests
   - Joint venture commitments
   - Pension/future employee benefit obligations
   - Legal settlements not yet accrued
3. **Quantify Impact**: Estimate debt-equivalent value of each item
4. **Recalculate Ratios**: Adjust leverage ratios (Debt/Equity, Debt/Assets) to include off-balance items
5. **Risk Assessment**: Flag if off-balance items >15% of total assets or >50% of reported debt

## Red Flags
- Operating lease expenses >10% of EBIT
- Unconsolidated subsidiaries with revenue >5% of group revenue
- Guarantees >10% of total assets
- Pension deficits >20% of total equity
- SPE/VIE exposures with no clear business purpose

## Output Format
```json
{
  "off_balance_items": [
    {"type": "operating_lease", "value": 500000, "note_reference": "Note 12"}
  ],
  "total_off_balance_debt": 1200000,
  "adjusted_debt_ratio": 0.45,  // Debt + off-balance / Total Assets
  "risk_score": "low|medium|high",
  "recommendations": ["..."]
}
```

## Dependencies
- Requires normalized data from nanobot-data-normalizer
- Notes to financial statements from nanobot-pdf-table-extractor
- Feeds into nanobot-financial-ratios for adjusted ratio calculation
