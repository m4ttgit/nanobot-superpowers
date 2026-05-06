# PDF Extraction Guide for Financial Statements

This guide provides practical strategies for extracting structured data from PDF financial statements. It complements the PDF Table Extractor skill by detailing layout heuristics, common pitfalls, and validation techniques.

## Common PDF Layouts
- Financial statements often follow a recurring pattern: a header with the company name and report period, followed by sections for Income Statement, Balance Sheet, and Cash Flow Statement.
- Tables may appear across multiple pages with repeating headers, merged cells, and inconsistent decimal placements.
- Some PDFs embed text in columns, while others use image-based regions; OCR may be required for the latter.

## Distinguishing IS, BS, CF by Layout
- Income Statement: typically lists revenue, expenses, and earnings with an operating performance focus.
- Balance Sheet: lists assets, liabilities, and equity; headers often include assets and liabilities sections with subtotals.
- Cash Flow: tracks cash movements, often categorized into operating, investing, and financing activities.

## Handling Multi-Page Tables
- If a table header repeats on subsequent pages, accumulate rows under the same logical table until a new header is detected.
- When a single logical table breaks across pages, aim to align rows by the first column (labels) and append value rows from the continuing page.

## Merged Headers and Cells
- Merged headers can appear as two rows, with the top row describing the category and the second row listing specific line items. When detected, flatten into a single header per column where possible.
- If headers are not parseable, fall back to using the first column as the label and treat remaining columns as values labeled by their index (Col1, Col2, ...).

## Currency and Number Formatting
- Remove currency symbols ($, €, ¥, etc.) and thousands separators. Interpret numbers in parentheses as negatives.
- Ensure decimals are preserved when present; coerce to float where possible.

## Period and Date Extraction
- Look for patterns like FY2024, FY2023, or Year End 2024 in the header text to populate the period field.
- If no year is found, default to an empty period and document the limitation in notes.

## Validation Rules
- Check that at least 3-5 rows contain numeric data to avoid spurious headers.
- Validate basic arithmetic relationships where applicable (e.g., totals should not be negative unless expected).
- Log suspicious results into a notes array for manual review.

## Data Schema Reference
- The JSON schema used by the skill (see assets/sample_output.json) mirrors the following structure:
- source_file, extracted_at, statements[].type, page, title, period, headers, rows[].label/values[], notes[]

## Troubleshooting
- If pdfplumber is not installed, install it with: pip install pdfplumber
- If pdfplumber fails to parse a layout, you can install tabula-py as a fallback: pip install tabula-py
- Ensure Java is installed for tabula-py usage.
