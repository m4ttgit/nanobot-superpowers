# PDF Table Extractor

## Use when
- You need to extract structured financial tables from PDF financial statements and export them as JSON, and optionally as Excel. This skill is especially useful for Income Statements, Balance Sheets, and Cash Flow Statements that appear across multiple pages or with merged headers.

## Core principle
- Rely on pdfplumber for robust table extraction of financial layouts, with a safe fallback to tabula-py if pdfplumber is unavailable. Infer the statement type from layout/text cues and normalize values to a structured JSON schema. Output JSON by default; provide a simple Excel-compatible export when requested.

## The Process
- Identify the PDF source pages and scan for potential financial tables per page.
- Detect the statement type (income statement, balance sheet, cash flow) from page text and the layout.
- Extract tabular data, treating the first non-empty row as headers and the first column as the label column.
- Normalize numeric values (remove currency symbols, commas; handle negative values in parentheses).
- Capture page number and a best-effort period/date from headers (e.g., FY2024).
- Build the JSON structure described in the Data Schema and write to disk. If requested, also produce a simple Excel-friendly file.
- Validate basic integrity checks (e.g., at least 3-5 rows per table, not all values are missing).

## Red Flags
- PDF is image-based (OCR needed) or contains heavy merged cells (>30%).
- Detected number of rows is suspiciously low (<5 rows).
- Currency symbols appear in inconsistent positions.
- Negative numbers use non-standard formatting beyond parentheses (e.g., - (100)).

## Reference Doc Content
- pdf-extraction-guide.md — guidance on tricky layouts, common PDF issues, financial statement patterns, and how to identify IS vs BS vs CF from layout alone.

## Asset File
- assets/sample_output.json — a realistic example of extracted income statement data used for validation and testing.

## How to Identify Statement Types
- Look for headers like "Income Statement", "Balance Sheet", or "Cash Flows" in the page text or in large bold headers near the top of a page.
- If multiple statements appear on a single page, segment by detected header blocks and assign to separate statement entries.

## How to Handle Multi-Page Extractions
- Accumulate tables per page but carry forward a consistent period hint when available. If a statement spans pages, the script will create multiple statement entries for each page with the same type/period when feasible.

## How to Merge Tables Spanning Pages
- If a header row is detected at the top of page X and the next page starts with more rows continuing that table, merge by using the label column matching and concatenating numeric rows where the page break occurs.

## How to Handle Tables with Merged Headers
- Treat the top-most row as header if it appears consistently and aligns to all columns; if not, fall back to a best-effort labeling:
- First column is treated as the row label; remaining columns as values, with headers used as column names if present.

## Currency Formatting Handling
- Strip currency symbols like "$" or localized symbols and remove thousands separators (commas). Interpret parentheses as negative values where applicable.

## Period/Date Identification
- Search within page text for patterns like FY2024, FY2023, or Year End 2024 to populate the period field.
- Fall back to the last 4-digit year found on the page if no explicit fiscal year is detected.

## When to Skip a Table
- If a table has fewer than 3 meaningful numeric rows or if the header is ambiguous, skip the table to avoid malformed output.
- If the table contains more than 30% merged cells, skip and mark in notes.

## Validation Rules
- Basic sanity checks: total of value columns should be finite numbers; non-numeric placeholders should be nulls.
- Optional: perform simple row-sums sanity checks for consistency where feasible.
