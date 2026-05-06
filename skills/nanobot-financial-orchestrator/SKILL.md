# Financial Orchestrator#

## Use when
- User requests "evaluate [company]" or "should I invest in [company]?"
- Financial data is available (Income Statement, Balance Sheet, Cash Flow)
- Need to coordinate multiple analysis modules
- Must make a final investment recommendation

## Core principle
- **Judge, not just calculator** — The orchestrator weighs all factors and makes a recommendation
- **Survival first** — If Adverse opinion or negative working capital, skip growth/valuation modules
- **Escalate dynamically** — Red flags trigger additional module firings

## The Process#

### Step 1: Validate Input
Before any analysis:
- Check `income_statement`, `balance_sheet`, `cash_flow` exist
- If any missing, report to user and stop
- If `auditor_opinion` provided, parse it immediately#

### Step 2: Determine Survival Mode
```
if auditor_opinion == "Adverse":
    fire: solvency_analysis, liquidity_analysis, bankruptcy_scoring
    skip: growth_analysis, valuation_analysis
    return "DO NOT INVEST — Company in financial distress"
    
elif auditor_opinion == "Disclaimer":
    fire: ALL risk modules with heightened scrutiny
    
elif auditor_opinion == "Qualified":
    fire: all modules, flag all outputs for caution
    
else:  # Unqualified (Clean)
    proceed to normal analysis
```

### Step 3: Fire Core Modules
Always fire (unless in Survival Mode):
- `nanobot-financial-ratios` — All 5 categories
- `nanobot-working-capital-analyst` — Working capital focus
- `nanobot-cash-flow-quality` — Net Income vs OCF reconciliation#

### Step 4: Dynamic Escalation
After core modules return results:
```
if red_flags contains "negative_working_capital":
    fire: nanobot-cash-flow-quality (if not already fired)
    add_to_report: "CRITICAL: Negative working capital — company cannot meet short-term obligations"

if red_flags contains "debtor_days > 60":
    fire: nanobot-collection-efficiency
    add_to_report: "Collections process failing — cash flow impact"

if red_flags contains "pe_ratio > 30":
    add_to_report: "Potentially overvalued — verify growth assumptions"

if red_flags contains "current_ratio < 1.0":
    fire: nanobot-off-balance-scanner
    add_to_report: "Liquidity crisis imminent — scan for hidden liabilities"
```

### Step 5: Generate Final Report
- Use `nanobot-financial-research-report` with all gathered data
- Include all red/yellow flags with explanations
- Provide clear **Buy/Hold/Sell** with target price
- Confidence level: High/Medium/Low based on data completeness#

## Red Flags#

- **No auditor opinion provided** — Cannot assess going concern risk, flag for user
- **Missing 2+ financial statement sections** — Cannot make recommendation, ask user for complete data
- **3+ Red Flags in core modules** — Recommend Sell regardless of valuation
- **Adverse auditor opinion** — Auto-recommend Sell, skip valuation#

## Script Dependencies
- **None** — This is a meta-skill (orchestration logic only)
- Delegates to other `nanobot-*` skills
- Uses `nanobot-financial-research-report` for final output#

## Reference
- `references/orchestration-logic.md` — Complete decision tree, module dependency graph#

## Asset
- `assets/sample_orchestration_input.json` — Example with all required fields