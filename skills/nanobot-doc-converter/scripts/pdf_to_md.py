#!/usr/bin/env python3
"""
pdf_to_md.py - Convert PDF to Markdown with structure preservation.

Usage:
    python3 pdf_to_md.py input.pdf --output output.md
    python3 pdf_to_md.py input.pdf --analyze-structure
    python3 pdf_to_md.py *.pdf --batch --output-dir ./md/

Preserves:
- Heading hierarchy (converted to # H1, ## H2, etc.)
- Table structure (where detectable)
- List numbering and nesting
- Code block identification (where possible)
- Image references (extracted or linked)
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

def check_pdfminer():
    try:
        import pdfminer
        return True
    except ImportError:
        return False

def convert_pdf_to_md_pdfminer(pdf_file, md_file):
    try:
        from pdfminer.high_level import extract_text
        from pdfminer.layout import LAParams
        
        text = extract_text(pdf_file, laparams=LAParams())
        
        lines = text.split('\n')
        md_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                md_lines.append('')
                continue
            
            if len(line) < 80 and line[0].isupper() and not line.endswith('.'):
                md_lines.append(f"# {line}")
            else:
                md_lines.append(line)
        
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(md_lines))
        
        print(f"Success (basic): '{pdf_file}' -> '{md_file}'")
        print("Note: Basic structure only. Install Pandoc for better results.")
        return True
    except ImportError:
        print("Error: pdfminer.six not installed. Install: pip install pdfminer.six")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_pdf_to_md_pandoc(pdf_file, md_file, analyze=False):
    """Convert PDF to MD using Pandoc (best quality)."""
    if not check_pandoc():
        return False
    
    cmd = ['pandoc', pdf_file, '--to', 'markdown+pipe_tables+grid_tables']
    
    if analyze:
        # Just print structure analysis
        cmd.append('--to', 'json')
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("Document structure analysis:")
            print(result.stdout)
            return True
        else:
            print(f"Error analyzing '{pdf_file}'")
            print(result.stderr)
            return False
    else:
        cmd.extend(['--output', md_file])
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Success: '{pdf_file}' -> '{md_file}'")
                return True
            else:
                print(f"Error converting '{pdf_file}'")
                print(result.stderr)
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False

def convert_pdf_to_md(pdf_file, md_file, analyze=False, use_fallback=True):
    """Try Pandoc first, fallback to pdfminer."""
    if check_pandoc():
        return convert_pdf_to_md_pandoc(pdf_file, md_file, analyze)
    elif use_fallback and check_pdfminer():
        print("Pandoc not found, using pdfminer fallback...")
        return convert_pdf_to_md_pdfminer(pdf_file, md_file)
    else:
        print("Error: Neither Pandoc nor pdfminer available.")
        print("Install Pandoc: brew install pandoc (macOS) or apt-get install pandoc (Ubuntu)")
        print("  or: pip install pdfminer.six")
        return False

def batch_convert(file_list, output_dir, **kwargs):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    success = 0
    total = len(file_list)
    
    for f in file_list:
        if not f.endswith('.pdf'):
            continue
        basename = os.path.splitext(os.path.basename(f))[0]
        output = os.path.join(output_dir, f"{basename}.md")
        if convert_pdf_to_md(f, output, **kwargs):
            success += 1
    
    print(f"\nBatch conversion complete: {success}/{total} files converted successfully.")
    return success

def main():
    parser = argparse.ArgumentParser(
        description='Convert PDF to Markdown with structure preservation.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Single file:
    python3 pdf_to_md.py document.pdf --output document.md
  
  Analyze structure:
    python3 pdf_to_md.py document.pdf --analyze-structure
  
  Batch conversion:
    python3 pdf_to_md.py *.pdf --batch --output-dir ./md/
"""
    )
    parser.add_argument('input', nargs='*', help='Input PDF file(s)')
    parser.add_argument('--input', '-i', help='Input file (alternative)')
    parser.add_argument('--output', '-o', help='Output Markdown file path')
    parser.add_argument('--analyze-structure', action='store_true',
                        help='Print document structure instead of converting')
    parser.add_argument('--no-links', action='store_false', dest='preserve_links',
                        help='Do not preserve links')
    parser.add_argument('--batch', action='store_true',
                        help='Batch mode: convert all inputs to output-dir')
    parser.add_argument('--output-dir', default='./md',
                        help='Output directory for batch mode')
    parser.add_argument('--fallback', action='store_true',
                        help='Use pdfminer fallback if Pandoc not available')
    
    args = parser.parse_args()
    
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
                              analyze=args.analyze_structure,
                              preserve_links=args.preserve_links)
        sys.exit(0 if success > 0 else 1)
    
    # Single file mode
    if len(expanded_files) > 1 and not args.output:
        print("Error: Multiple input files require --batch or --output.")
        sys.exit(1)
    
    input_file = expanded_files[0]
    output_file = args.output or os.path.splitext(input_file)[0] + '.md'
    
    success = convert_pdf_to_md(input_file, output_file, args.analyze_structure,
                             args.fallback)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
