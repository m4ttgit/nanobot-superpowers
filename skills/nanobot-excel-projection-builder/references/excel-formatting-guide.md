# Excel Formatting Guide

Guide for building professional financial reporting Excel workbooks using `openpyxl`.

## Number Formats

### Currency Format
```python
CURR_FMT = '#,##0;(#,##0);"-"'          # values < 1M
CURR_FMT_LARGE = '#,##0,;(#,##0,);"-"'  # values >= 1M
```
- Positive: `1,234,567`
- Negative: `(1,234,567)` (parentheses, no minus sign)
- Zero: `-`

### Percentage Format
```python
PCT_FMT = '0.0%;0.0%;"-"'
```
- 0.15 → `15.0%`
- -0.25 → `(25.0%)`

## Header Styling

```python
HEADER_FILL = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
HEADER_FONT = Font(color="FFFFFF", bold=True, size=10)
# Dark blue background, white bold text — professional financial reporting standard
```

## Section Headers

```python
SECTION_FILL = PatternFill(start_color="2E75B6", end_color="2E75B6", fill_type="solid")
SECTION_FONT = Font(color="FFFFFF", bold=True, size=10)
# Medium blue — distinct from column headers, used for section labels within the sheet
```

## Total Rows

```python
TOTAL_FILL = PatternFill(start_color="BDD7EE", end_color="BDD7EE", fill_type="solid")
TOTAL_FONT = Font(bold=True, size=10)
# Light blue — clearly differentiated from data rows but not as bold as section headers
```

## Row Shading

Alternate row shading (every other row with a subtle tint) improves readability in dense tables:
```python
ALT_FILL = PatternFill(start_color="DEEAF1", end_color="DEEAF1", fill_type="solid")
if row_index % 2 == 0:
    for c in range(1, num_cols + 2):
        ws.cell(row=row_index, column=c).fill = ALT_FILL
```

## Borders

Apply to all cells with data — never leave cells unbordered in a financial table:
```python
thin = Side(style='thin')
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
for cell in row.cells:
    cell.border = BORDER
```

## Column Widths

Auto-fit based on content, with a max cap:
```python
for col_cells in ws.columns:
    length = max(len(str(cell.value)) if cell.value else 0 for cell in col_cells)
    ws.column_dimensions[get_column_letter(col_cells[0].column)].width = min(length + 3, 30)
```

## Freezing Panes

Always freeze the header row so it stays visible when scrolling:
```python
ws.freeze_panes = 'B5'  # freeze rows 1-4 and column A
```

## Tab Colors

Use consistent tab colors for related sheets:
```python
ws.sheet_properties.tabColor = "1F4E79"  # dark blue for financial statements
```

## Common Mistakes

1. **Using wrong number format** — `0.15` displayed as `0.15` instead of `15.0%`
2. **Missing borders** — makes tables hard to read when printed
3. **Frozen panes on wrong row** — must freeze below all header rows
4. **No distinction between total and detail rows** — auditors/readers need instant visual differentiation
5. **Over-merging cells** — merged title cells can break sorting/filtering
6. **Using hard-coded column letters** — use `get_column_letter()` for maintainability