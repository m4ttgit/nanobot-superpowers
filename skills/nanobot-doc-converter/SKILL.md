# Doc Converter

Convert between Markdown and PDF formats while preserving document structure, table alignments, code block formatting, heading hierarchy, and list indentation.

**Tier:** POWERFUL  
**Category:** Engineering  
**Domain:** Document Processing & Conversion

---

## Overview

A document conversion skill that preserves formatting alignments during Markdown ↔ PDF conversion. Uses Pandoc as the primary engine with fallback strategies for environments without Pandoc. Handles tables with column alignment, code blocks with indentation, heading hierarchy, nested lists, and image references.

## Core Capabilities

- **MD → PDF**: Convert Markdown to PDF preserving all formatting
- **PDF → MD**: Extract Markdown from PDF with structure preservation
- **Alignment Validation**: Verify table columns, code blocks, and lists remain aligned
- **Batch Conversion**: Process multiple files with consistent settings
- **Template Support**: Custom LaTeX templates for PDF generation
- **Image Preservation**: Maintain image references and alignment during conversion

---

## When to Use

- Convert documentation from MD to PDF for distribution
- Extract content from PDF into Markdown for editing
- Ensure table alignments survive format conversion
- Batch convert multiple documents with consistent styling
- Validate that converted documents preserve original structure

---

## Quick Start

### Prerequisites

- **Pandoc** (recommended): `https://pandoc.org/installing.html`
- **PDF Engine** (for MD→PDF): `wkhtmltopdf` or `xelatex`
- **Python 3.7+** with packages: `pdfminer.six`, `beautifulsoup4`, `markdown`

### Installation

```bash
# Install Pandoc (macOS)
brew install pandoc

# Install Pandoc (Ubuntu)
sudo apt-get install pandoc

# Install Python dependencies
pip install pdfminer.six beautifulsoup4 markdown
```

### Basic Conversion

```bash
# MD to PDF (preserves alignments)
python3 scripts/md_to_pdf.py input.md --output document.pdf

# PDF to MD (preserves structure)
python3 scripts/pdf_to_md.py input.pdf --output document.md

# Validate alignments after conversion
python3 scripts/validate_alignment.py original.md converted.md
```

---

## Script Interfaces

### 1. md_to_pdf.py

Converts Markdown to PDF while preserving all alignments.

**Features:**
- Table column alignment (left, right, center via Pandoc pipe tables)
- Code block indentation and syntax highlighting
- Heading hierarchy (H1-H6) preservation
- List nesting and numbering
- Image embedding and positioning
- Custom CSS/LaTeX templates

**Usage:**

```bash
# Basic conversion
python3 scripts/md_to_pdf.py input.md --output output.pdf

# With custom template
python3 scripts/md_to_pdf.py input.md --template template.latex --output output.pdf

# With CSS styling (HTML-based PDF)
python3 scripts/md_to_pdf.py input.md --css style.css --output output.pdf

# Batch conversion
python3 scripts/md_to_pdf.py *.md --batch --output-dir ./pdfs/
```

**CLI Options:**
- `--input`: Input Markdown file (or stdin with `--stdin`)
- `--output`: Output PDF file path
- `--template`: LaTeX template for PDF generation
- `--css`: CSS file for HTML-based conversion
- `--toc`: Include table of contents
- `--highlight-style`: Syntax highlighting style (pygments, katex, etc.)
- `--pdf-engine`: PDF engine (`wkhtmltopdf`, `xelatex`, `pdflatex`)

### 2. pdf_to_md.py

Extracts Markdown from PDF while preserving document structure.

**Features:**
- Heading detection and hierarchy reconstruction
- Table extraction with alignment preservation
- List and numbering recovery
- Code block identification
- Image extraction and linking
- Pandoc-based conversion with fallback to pdfminer

**Usage:**

```bash
# Basic extraction
python3 scripts/pdf_to_md.py input.pdf --output output.md

# With structure analysis
python3 scripts/pdf_to_md.py input.pdf --analyze-structure --output output.md

# Batch conversion
python3 scripts/pdf_to_md.py *.pdf --batch --output-dir ./md/
```

**CLI Options:**
- `--input`: Input PDF file
- `--output`: Output Markdown file path
- `--analyze-structure`: Print document structure before conversion
- `--extract-images`: Extract images to separate files
- `--preserve-links`: Keep hyperlinks in output
- `--pandoc-fallback`: Force Pandoc usage (if available)

### 3. validate_alignment.py

Validates that alignments are preserved between original and converted documents.

**Features:**
- Table column alignment comparison
- Code block indentation checking
- Heading hierarchy validation
- List nesting verification
- Image reference preservation
- Report generation with diff details

**Usage:**

```bash
# Compare original MD with converted MD
python3 scripts/validate_alignment.py original.md converted.md

# Compare MD with PDF (extract PDF to temp MD first)
python3 scripts/validate_alignment.py original.md --pdf converted.pdf

# Generate HTML report
python3 scripts/validate_alignment.py original.md converted.md --report report.html
```

**CLI Options:**
- `--pdf`: Compare with PDF (requires pdfminer)
- `--report`: Generate HTML report instead of text output
- `--strict`: Fail on any alignment mismatch
- `--ignore-whitespace`: Ignore whitespace differences
- `--tolerance`: Set pixel tolerance for alignment (default: 5px)

---

## Key Workflows

### 1. Simple MD → PDF

```bash
# Convert single file with default settings
python3 scripts/md_to_pdf.py README.md --output README.pdf
```

### 2. PDF → MD with Validation

```bash
# Extract MD from PDF
python3 scripts/pdf_to_md.py document.pdf --output document.md

# Validate alignments preserved
python3 scripts/validate_alignment.py original.md document.md
```

### 3. Batch Conversion with Consistent Styling

```bash
# Convert all MD files in directory
for f in *.md; do
  python3 scripts/md_to_pdf.py "$f" --output "pdfs/${f%.md}.pdf"
done

# Validate all converted files
for f in *.md; do
  python3 scripts/validate_alignment.py "$f" "pdfs/${f%.md}.pdf" || echo "Alignment issue in $f"
done
```

### 4. Template-Based PDF Generation

```bash
# Use custom LaTeX template for professional PDFs
python3 scripts/md_to_pdf.py report.md \
  --template templates/professional.latex \
  --toc \
  --highlight-style pygments \
  --output report.pdf
```

---

## Alignment Preservation Details

### Table Alignments

| Alignment Type | Markdown Syntax | PDF Result |
|---------------|----------------|-------------|
| Left | `|:---|` | Left-aligned column |
| Right | `|---:|` | Right-aligned column |
| Center | `|:---:|` | Center-aligned column |
| Default | `|---|` | Default (usually left) |

The conversion ensures that Pandoc's pipe tables preserve these alignments in PDF output.

### Code Block Indentation

```markdown
# This code block indentation is preserved
def example():
    # 4 spaces indentation
    nested = True
    return nested
```

Converted to PDF with monospace font and identical indentation.

### Heading Hierarchy

```markdown
# H1 - Top Level
## H2 - Section
### H3 - Subsection
#### H4 - Detail
```

PDF output maintains heading levels via LaTeX sectioning or HTML heading tags.

### List Nesting

```markdown
1. First item
   - Nested bullet (3 spaces)
   - Another nested (3 spaces)
2. Second item
   - Nested (3 spaces)
```

Preserved as numbered lists with proper bullet indentation.

---

## Best Practices

1. **Use Pandoc when available** — it handles alignments best
2. **Validate after conversion** — always run validation script
3. **Test with sample content** — verify tables, code, lists before batch
4. **Keep templates versioned** — store LaTeX/CSS templates in repo
5. **Check image paths** — ensure relative paths work in both formats
6. **Use consistent heading style** — ATX style (`# H1`) works best
7. **Batch convert with scripts** — automate repetitive conversions

---

## Common Pitfalls

| Pitfall | Solution |
|----------|-----------|
| Tables lose alignment in PDF | Use Pandoc pipe tables format |
| Code blocks not monospace | Specify `--highlight-style` for PDF |
| Images not appearing | Check paths are relative, not absolute |
| Headings merge in PDF | Use proper ATX heading syntax |
| Lists flatten after conversion | Verify Pandoc list parsing enabled |
| PDF extraction messy | Use `--pandoc-fallback` if available |

---

## Installation & Dependencies

### Required (Minimum)

```bash
pip install pdfminer.six beautifulsoup4 markdown
```

### Recommended (Full Functionality)

```bash
# Install Pandoc (system package)
# macOS: brew install pandoc
# Ubuntu: sudo apt-get install pandoc

# Install PDF engine (one of)
# wkhtmltopdf: npm install -g wkhtmltopdf
# or xelatex: sudo apt-get install texlive

# Python packages
pip install pdfminer.six beautifulsoup4 markdown weasyprint
```

---

## File Structure

```
nanobot-doc-converter/
├── SKILL.md                          # This file
├── scripts/
│   ├── md_to_pdf.py                # MD → PDF conversion
│   ├── pdf_to_md.py                # PDF → MD extraction
│   └── validate_alignment.py       # Alignment validation
├── templates/
│   ├── default.latex             # Basic LaTeX template
│   ├── professional.latex         # Professional report template
│   └── style.css                  # CSS for HTML-based PDF
└── references/
    ├── pandoc-guide.md            # Pandoc usage and options
    ├── alignment-patterns.md       # Table/code/list alignment details
    └── template-examples.md       # Sample LaTeX/CSS templates
```

---

## References

- [pandoc-guide.md](references/pandoc-guide.md) — Complete Pandoc usage for format conversion
- [alignment-patterns.md](references/alignment-patterns.md) — Detailed alignment preservation techniques
- [template-examples.md](references/template-examples.md) — Sample templates for PDF generation

---

## Troubleshooting

### "Pandoc not found"

```bash
# Check if pandoc is installed
which pandoc

# Install if missing (macOS)
brew install pandoc

# Install if missing (Ubuntu)
sudo apt-get install pandoc
```

### "PDF generation failed"

```bash
# Check PDF engine
which wkhtmltopdf
which xelatex

# Try simpler conversion (HTML-based)
python3 scripts/md_to_pdf.py input.md --pdf-engine wkhtmltopdf
```

### "Table alignments lost"

```bash
# Ensure Markdown uses Pandoc pipe table format
# Good:
| Left | Center | Right |
|:-----|:------:|------:|
| L    | C       | R     |

# Bad (standard markdown tables may lose alignment):
| Left | Center | Right |
| --- | --- | --- |
| L | C | R |
```

### "Validation reports mismatches"

```bash
# Run with tolerance
python3 scripts/validate_alignment.py orig.md conv.md --tolerance 10

# Ignore whitespace
python3 scripts/validate_alignment.py orig.md conv.md --ignore-whitespace
```

---

## Examples

### Convert README.md to PDF

```bash
python3 scripts/md_to_pdf.py README.md \
  --toc \
  --highlight-style pygments \
  --output README.pdf
```

### Extract PDF to Markdown

```bash
python3 scripts/pdf_to_md.py whitepaper.pdf \
  --extract-images \
  --preserve-links \
  --output whitepaper.md
```

### Validate After Conversion

```bash
# Convert
python3 scripts/md_to_pdf.py document.md --output document.pdf

# Validate (PDF → temporary MD → compare with original)
python3 scripts/validate_alignment.py document.md --pdf document.pdf
```

---

## Integration with CI/CD

```yaml
# .github/workflows/docs.yml
name: Documentation Conversion
on:
  push:
    paths: ['docs/**.md']

jobs:
  convert:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y pandoc wkhtmltopdf
        pip install pdfminer.six beautifulsoup4 markdown
        
    - name: Convert MD to PDF
      run: |
        for f in docs/*.md; do
          python3 scripts/md_to_pdf.py "$f" --output "pdfs/$(basename $f .md).pdf"
        done
        
    - name: Validate alignments
      run: |
        for f in docs/*.md; do
          python3 scripts/validate_alignment.py "$f" "pdfs/$(basename $f .md).pdf" || exit 1
        done
```

---

## Success Metrics

- **Alignment Preservation Rate**: >95% tables/code/lists maintain alignment
- **Conversion Success**: 0 errors during MD→PDF or PDF→MD
- **Validation Pass**: All automated checks pass
- **Image Preservation**: 100% of images referenced correctly

---

## Notes

- This skill focuses on **alignment preservation** as requested
- Pandoc is the recommended engine for best results
- For environments without Pandoc, fallback Python libraries are used (with reduced alignment fidelity)
- Always validate critical documents after conversion
- Store templates and CSS in version control for consistency
