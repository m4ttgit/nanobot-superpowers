# Excel Projection Builder

## Use when
- User provides a financial projection JSON (from nanobot-financial-analyst or manual input) and wants it formatted as a professional Excel workbook
- You need to generate a multi-year financial projection workbook with Income Statement, Balance Sheet, Cash Flow, and Summary tabs
- The output Excel will be linked or referenced in a written report

## Core principle
- Output must be audit-ready: bold totals, proper accounting number format, frozen headers, color-coded section headers
- The workbook is a deliverable the user will share or present — formatting quality reflects on the analysis quality

## The Process

### Step 1: Validate input JSON
Before generation, confirm the JSON contains:
- `company_name`, `currency`, `assumptions`
- `projections.years` (list of year labels)
- `projections.income_statement` (array of line items)
- `projections.balance_sheet` (array of line items)
- `projections.cash_flow` (array of line items)

Each line item must have `line_item` (label), `values` (array, one per year), and optionally `is_total: true`.

If any section is missing, report what is missing to the user before generating partial output.

### Step 2: Run the script
```bash
python scripts/excel_projection_builder.py <path_to_projection.json> --output <output.xlsx> --company-name "Acme Corp"
```

If no `--output` is given, save as `{company_name}_projection.xlsx` in the current directory.

### Step 3: Verify the workbook
After generation, verify:
- All year columns are present and populated
- Totals (Gross Profit, EBIT, Net Income, Total Assets, etc.) are bolded
- The Assumptions tab lists all input assumptions
- The Summary tab shows key metrics (Revenue, EBITDA, Net Income)

### Step 4: Report to user
Report the full path to the generated Excel file. If the workbook will be embedded in a Word/document report, note the file path clearly so it can be linked.

## Workbook Structure

### Summary Tab
- Key metrics per year: Revenue, EBITDA, Net Income
- YoY growth rates for Revenue and Net Income
- Company name and currency in header

### Income Statement Tab
Sections (each separated by a bold subtotal row):
- Revenue
- COGS → Gross Profit (bold, calculated: Revenue + COGS)
- Operating Expenses → EBIT (bold, calculated)
- Interest, Taxes → Net Income (bold, calculated)

Each line: label | FY2025 | FY2026 | FY2027...

### Balance Sheet Tab
Sections:
- Assets: Current Assets, Non-Current Assets → Total Assets (bold)
- Liabilities: Current Liabilities, Long-Term Debt → Total Liabilities (bold)
- Equity → Total Equity (bold)
- Check: Total Liabilities + Equity = Total Assets (flag if not)

### Cash Flow Tab
Sections:
- Operating Activities → Operating Cash Flow (bold)
- Investing Activities → Investing Cash Flow (bold)
- Financing Activities → Financing Cash Flow (bold)
- Net Change in Cash (bold)
- Beginning Cash, Ending Cash (calculated)

### Assumptions Tab
Table of all input assumptions:
| Assumption | Value |
|---|---|
| Revenue Growth Rate | 15% |
| COGS % of Revenue | 55% |
| ... | ... |

## Red Flags
- Missing required fields in input JSON — do not proceed, list what's missing
- `values` arrays have different lengths across line items — flag before generation
- No year columns detected — cannot build workbook without year labels
- Net Income is positive but cash flow from operations is negative — flag this inconsistency for user review
- Total Assets does not equal Total Liabilities + Equity — add a validation note

## Script Dependencies
- Requires `openpyxl` — if not installed, script will exit with: `pip install openpyxl`

## Reference
- `references/excel-formatting-guide.md` — openpyxl styling reference, accounting format codes, common formatting mistakes