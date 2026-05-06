## Use when
- User asks to interpret an audit report
- Analyzing auditor opinions (unqualified, qualified, adverse, disclaimer)
- Comparing audit findings with financial statements
- Identifying accounting discrepancies or red flags
- Assessing internal control weaknesses mentioned in audit reports
- Preparing management responses to audit findings

## Core principle
Audit interpretation requires matching auditor language to financial reality. Always cross-reference audit findings with the normalized financial data from nanobot-data-normalizer.

## The Process
1. **Read Input**: Accept audit report (PDF/text) + normalized financial data (from nanobot-data-normalizer)
2. **Parse Audit Opinion**: Extract opinion type (unqualified/clean, qualified, adverse, disclaimer)
3. **Identify Key Findings**:
   - Material weaknesses in internal controls
   - Adjustments proposed by auditors
   - Contingent liabilities disclosed
   - Related party transactions
   - Going concern flags
4. **Cross-Reference Financials**: Match audit findings to balance sheet/income statement/cash flow
5. **Risk Assessment**: Score audit risks (low/medium/high) based on findings
6. **Generate Report**: Structured output with opinion, findings, risks, recommendations

## Red Flags
- Adverse or disclaimer opinions
- Going concern qualifications
- Multiple material weaknesses in internal controls
- Large auditor adjustments to revenue/earnings
- Related party transactions >5% of revenue
- Contingent liabilities >10% of total assets

## Output Format
```json
{
  "audit_opinion": "unqualified|qualified|adverse|disclaimer",
  "key_findings": [
    {"type": "internal_control", "description": "...", "severity": "high|medium|low"}
  ],
  "financial_discrepancies": [
    {"account": "revenue", "audit_adjustment": 1000000, "explanation": "..."}
  ],
  "risk_score": "low|medium|high",
  "recommendations": ["..."]
}
```

## Dependencies
- Uses normalized financial data from nanobot-data-normalizer
- Can feed findings to nanobot-financial-orchestrator for holistic analysis
- Works with nanobot-pdf-table-extractor to parse audit PDFs
