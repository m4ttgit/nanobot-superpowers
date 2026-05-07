#!/usr/bin/env python3
"""
md_to_pdf.py - Convert Markdown to PDF with alignment preservation.

Usage:
    python3 md_to_pdf.py input.md --output output.pdf
    python3 md_to_pdf.py input.md --css style.css
    python3 md_to_pdf.py *.md --batch --output-dir ./pdfs/

Preserves:
- Table column alignments (left, right, center) via HTML table attributes
- Code block indentation and syntax highlighting
- Heading hierarchy (H1-H6)
- List nesting and numbering
- Image references and positioning
"""

import argparse
import os
import sys
import glob
import subprocess
import tempfile

def check_pandoc():
    """Check if pandoc is available."""
    try:
        subprocess.run(['pandoc', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_weasyprint():
    """Check if weasyprint is available."""
    try:
        subprocess.run(['weasyprint', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def convert_md_to_html(md_file, html_file, css_file=None):
    """Convert MD to HTML (preserving alignments)."""
    try:
        from markdown import markdown
        from markdown.extensions import tables, toc, fenced_code
        
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        extensions = [
            'tables',
            'fenced_code',
            'toc',
            'nl2br',
        ]
        
        try:
            from markdown.extensions.codehilite import CodeHiliteExtension
            extensions.append('codehilite')
        except ImportError:
            pass
        
        html = markdown(md_content, extensions=extensions)
        
        css_style = ''
        if css_file and os.path.isfile(css_file):
            with open(css_file, 'r') as f:
                css_style = f"<style>{f.read()}</style>"
        
        full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    {css_style}
    <style>
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; }}
        th {{ background-color: #f2f2f2; text-align: left; }}
        .align-left {{ text-align: left; }}
        .align-center {{ text-align: center; }}
        .align-right {{ text-align: right; }}
        pre {{ background: #f5f5f5; padding: 10px; overflow: auto; }}
        code {{ background: #f5f5f5; padding: 2px 4px; }}
    </style>
</head>
<body>
{html}
</body>
</html>"""
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        return True
    except ImportError:
        if check_pandoc():
            cmd = ['pandoc', md_file, '--to', 'html', '--output', html_file]
            if css_file:
                cmd.extend(['--css', css_file])
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.returncode == 0
    except Exception as e:
        print(f"Error converting to HTML: {e}")
        return False

def convert_html_to_pdf(html_file, pdf_file):
    try:
        import weasyprint
        weasyprint.HTML(filename=html_file).write_pdf(pdf_file)
        return True
    except ImportError:
        pass
    except Exception as e:
        print(f"weasyprint failed: {e}")
    
    try:
        cmd = ['wkhtmltopdf', html_file, pdf_file]
        result = subprocess.run(cmd, capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    
    if check_pandoc():
        try:
            cmd = ['pandoc', html_file, '--to', 'pdf', '--output', pdf_file]
            result = subprocess.run(cmd, capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            pass
    
    print("Error: No PDF conversion method available.")
    print("Install: pip install weasyprint")
    print("  or: apt-get install wkhtmltopdf")
    return False

def convert_md_to_pdf(input_file, output_file, css=None, toc=False):
    """Convert a single MD file to PDF."""
    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return False
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
        html_file = f.name
    
    try:
        if not convert_md_to_html(input_file, html_file, css):
            print(f"Error converting '{input_file}' to HTML")
            return False
        
        if not convert_html_to_pdf(html_file, output_file):
            print(f"Error converting HTML to PDF")
            return False
        
        print(f"Success: '{input_file}' -> '{output_file}'")
        return True
    finally:
        if os.path.exists(html_file):
            os.unlink(html_file)

def batch_convert(file_list, output_dir, **kwargs):
    """Convert multiple files to PDF."""
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    success = 0
    total = len(file_list)
    
    for f in file_list:
        if not f.endswith('.md'):
            continue
        basename = os.path.splitext(os.path.basename(f))[0]
        output = os.path.join(output_dir, f"{basename}.pdf")
        if convert_md_to_pdf(f, output, **kwargs):
            success += 1
    
    print(f"\nBatch conversion complete: {success}/{total} files converted successfully.")
    return success

def main():
    parser = argparse.ArgumentParser(
        description='Convert Markdown to PDF with alignment preservation.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Single file:
    python3 md_to_pdf.py README.md --output README.pdf
  
  With CSS styling:
    python3 md_to_pdf.py report.md --css style.css
  
  Batch conversion:
    python3 md_to_pdf.py *.md --batch --output-dir ./pdfs/
"""
    )
    parser.add_argument('input', nargs='*', help='Input Markdown file(s)')
    parser.add_argument('--input', '-i', help='Input file (alternative)')
    parser.add_argument('--output', '-o', help='Output PDF file path')
    parser.add_argument('--css', '-c', help='CSS file for styling')
    parser.add_argument('--toc', action='store_true', help='Include table of contents')
    parser.add_argument('--batch', action='store_true',
                        help='Batch mode: convert all inputs to output-dir')
    parser.add_argument('--output-dir', default='./pdfs',
                        help='Output directory for batch mode')
    
    args = parser.parse_args()
    
    # Check dependencies
    try:
        from markdown import markdown
    except ImportError:
        print("Warning: markdown module not installed. Install: pip install markdown")
        if not check_pandoc():
            print("Error: Neither markdown nor pandoc available.")
            sys.exit(1)
    
    input_files = args.input
    if args.input:
        input_files.append(args.input)
    
    if not input_files:
        parser.print_help()
        sys.exit(1)
    
    # Expand globs
    expanded_files = []
    for pattern in input_files:
        expanded_files.extend(glob.glob(pattern))
    
    if not expanded_files:
        print("Error: No input files found.")
        sys.exit(1)
    
    # Batch mode
    if args.batch:
        success = batch_convert(expanded_files, args.output_dir,
                              css=args.css, toc=args.toc)
        sys.exit(0 if success > 0 else 1)
    
    # Single file mode
    if len(expanded_files) > 1 and not args.output:
        print("Error: Multiple input files require --batch or --output.")
        sys.exit(1)
    
    input_file = expanded_files[0]
    output_file = args.output or os.path.splitext(input_file)[0] + '.pdf'
    
    success = convert_md_to_pdf(input_file, output_file, args.css, args.toc)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
