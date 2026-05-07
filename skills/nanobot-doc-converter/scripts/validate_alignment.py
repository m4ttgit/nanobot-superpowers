#!/usr/bin/env python3
"""
validate_alignment.py - Validate that alignments are preserved between original and converted documents.

Usage:
    python3 validate_alignment.py original.md converted.md
    python3 validate_alignment.py original.md --pdf converted.pdf
    python3 validate_alignment.py original.md converted.md --report report.html

Validates:
- Table column alignments (left, right, center markers)
- Code block indentation (leading spaces/tabs)
- Heading hierarchy (count # markers)
- List nesting (leading spaces/bullet levels)
- Image reference preservation
"""

import argparse
import re
import sys
import os
import tempfile
import subprocess

def check_pandoc():
    """Check if pandoc is available for PDF conversion."""
    try:
        subprocess.run(['pandoc', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def extract_md_from_pdf(pdf_file):
    """Extract Markdown from PDF using Pandoc (for comparison)."""
    if not check_pandoc():
        return None
    
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            temp_md = f.name
        
        cmd = ['pandoc', pdf_file, '--from', 'pdf', '--to', 'markdown', '--output', temp_md]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            with open(temp_md, 'r', encoding='utf-8') as f:
                content = f.read()
            os.unlink(temp_md)
            return content
        else:
            if os.path.exists(temp_md):
                os.unlink(temp_md)
            return None
    except Exception:
        return None

def parse_table_alignments(md_content):
    """Parse table alignment markers from Markdown."""
    alignments = []
    
    # Match pipe tables: |---|, |---:|, |:---:|, |---:|
    pattern = r'^[ \t]*\|(.+)\|[ \t]*$'
    lines = md_content.split('\n')
    
    for i, line in enumerate(lines):
        if re.match(r'^[ \t]*\|?[\-:| ]+\|[ \t]*$', line.strip()):
            # This is a separator line
            cells = [c.strip() for c in line.split('|') if c.strip()]
            for j, cell in enumerate(cells):
                if cell.startswith(':') and cell.endswith(':'):
                    alignments.append(('center', i, j))
                elif cell.startswith(':'):
                    alignments.append(('left', i, j))
                elif cell.endswith(':'):
                    alignments.append(('right', i, j))
                else:
                    alignments.append(('default', i, j))
    
    return alignments

def parse_code_indentation(md_content):
    """Parse code block indentation."""
    indentations = []
    in_code_block = False
    code_fence = None
    
    lines = md_content.split('\n')
    for i, line in enumerate(lines):
        # Detect code fence
        fence_match = re.match(r'^(`{3,})', line)
        if fence_match:
            if not in_code_block:
                in_code_block = True
                code_fence = fence_match.group(1)
                continue
            elif line.strip() == code_fence:
                in_code_block = False
                code_fence = None
                continue
        
        if in_code_block:
            # Count leading spaces/tabs
            leading = len(line) - len(line.lstrip())
            if line.strip():  # Non-empty line
                indentations.append((leading, i, line.rstrip()))
    
    return indentations

def parse_heading_levels(md_content):
    """Parse heading levels."""
    headings = []
    lines = md_content.split('\n')
    
    for i, line in enumerate(lines):
        match = re.match(r'^(#+)\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            text = match.group(2)
            headings.append((level, i, text))
    
    return headings

def parse_list_nesting(md_content):
    """Parse list nesting levels."""
    lists = []
    lines = md_content.split('\n')
    
    for i, line in enumerate(lines):
        # Match ordered/unordered list items
        match = re.match(r'^(\s*)([-*+]|\d+\.)\s+(.+)$', line)
        if match:
            indent = len(match.group(1))
            marker = match.group(2)
            text = match.group(3)
            lists.append((indent // 2, i, marker, text))  # Approximate nesting level
    
    return lists

def parse_image_references(md_content):
    """Parse image references."""
    images = []
    
    # Markdown images: ![alt](url)
    for match in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', md_content):
        alt_text = match.group(1)
        url = match.group(2)
        images.append(('markdown', alt_text, url))
    
    # HTML images: <img src="...">
    for match in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', md_content):
        url = match.group(1)
        images.append(('html', '', url))
    
    return images

def compare_alignments(align1, align2):
    """Compare table alignments between two documents."""
    issues = []
    
    if len(align1) != len(align2):
        issues.append(f"Table alignment count mismatch: {len(align1)} vs {len(align2)}")
        return issues
    
    for i, (a1, line1, col1) in enumerate(align1):
        a2, line2, col2 = align2[i]
        if a1 != a2:
            issues.append(f"Table alignment mismatch at line {line1}: '{a1}' vs '{a2}' (col {col1})")
    
    return issues

def compare_indentations(ind1, ind2):
    """Compare code block indentations."""
    issues = []
    
    if len(ind1) != len(ind2):
        issues.append(f"Code block line count mismatch: {len(ind1)} vs {len(ind2)}")
        return issues
    
    for i, (indent1, line1, text1) in enumerate(ind1):
        indent2, line2, text2 = ind2[i]
        if indent1 != indent2:
            issues.append(f"Indentation mismatch at line {line1}: {indent1} spaces vs {indent2} spaces")
    
    return issues

def compare_headings(head1, head2):
    """Compare heading levels."""
    issues = []
    
    if len(head1) != len(head2):
        issues.append(f"Heading count mismatch: {len(head1)} vs {len(head2)}")
        return issues
    
    for i, (level1, line1, text1) in enumerate(head1):
        level2, line2, text2 = head2[i]
        if level1 != level2:
            issues.append(f"Heading level mismatch: H{level1} vs H{level2} at line {line1}: '{text1}'")
    
    return issues

def compare_lists(list1, list2):
    """Compare list nesting."""
    issues = []
    
    if len(list1) != len(list2):
        issues.append(f"List item count mismatch: {len(list1)} vs {len(list2)}")
        return issues
    
    for i, (nest1, line1, marker1, text1) in enumerate(list1):
        nest2, line2, marker2, text2 = list2[i]
        if nest1 != nest2:
            issues.append(f"List nesting mismatch at line {line1}: level {nest1} vs {nest2}")
    
    return issues

def compare_images(img1, img2):
    """Compare image references."""
    issues = []
    
    urls1 = [url for _, _, url in img1]
    urls2 = [url for _, _, url in img2]
    
    for url in urls1:
        if url not in urls2:
            issues.append(f"Image missing in converted document: {url}")
    
    return issues

def validate_alignment(original_file, converted_file, is_pdf=False, report_file=None, strict=False, ignore_whitespace=False, tolerance=5):
    """Main validation function."""
    # Read original
    try:
        with open(original_file, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"Error reading original file: {e}")
        return False
    
    # Read or extract converted
    if is_pdf:
        if not check_pandoc():
            print("Error: Pandoc needed for PDF comparison.")
            return False
        converted_content = extract_md_from_pdf(converted_file)
        if not converted_content:
            print("Error: Could not extract Markdown from PDF.")
            return False
    else:
        try:
            with open(converted_file, 'r', encoding='utf-8') as f:
                converted_content = f.read()
        except Exception as e:
            print(f"Error reading converted file: {e}")
            return False
    
    # Parse both
    orig_align = parse_table_alignments(original_content)
    conv_align = parse_table_alignments(converted_content)
    
    orig_indent = parse_code_indentation(original_content)
    conv_indent = parse_code_indentation(converted_content)
    
    orig_head = parse_heading_levels(original_content)
    conv_head = parse_heading_levels(converted_content)
    
    orig_lists = parse_list_nesting(original_content)
    conv_lists = parse_list_nesting(converted_content)
    
    orig_imgs = parse_image_references(original_content)
    conv_imgs = parse_image_references(converted_content)
    
    # Compare
    all_issues = []
    
    all_issues.extend([(f"TABLE ALIGNMENT: {issue}") for issue in compare_alignments(orig_align, conv_align)])
    all_issues.extend([(f"CODE INDENTATION: {issue}") for issue in compare_indentations(orig_indent, conv_indent)])
    all_issues.extend([(f"HEADING: {issue}") for issue in compare_headings(orig_head, conv_head)])
    all_issues.extend([(f"LIST NESTING: {issue}") for issue in compare_lists(orig_lists, conv_lists)])
    all_issues.extend([(f"IMAGE REFERENCE: {issue}") for issue in compare_images(orig_imgs, conv_imgs)])
    
    # Output results
    if report_file:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("<html><head><title>Alignment Validation Report</title></head><body>\n")
            f.write(f"<h1>Alignment Validation Report</h1>\n")
            f.write(f"<p>Original: {original_file}<br>Converted: {converted_file}</p>\n")
            f.write(f"<h2>Summary</h2>\n")
            f.write(f"<p>Total issues found: {len(all_issues)}</p>\n")
            f.write(f"<h2>Details</h2>\n<ul>\n")
            for issue in all_issues:
                f.write(f"<li>{issue}</li>\n")
            f.write("</ul></body></html>")
        print(f"Report written to {report_file}")
    else:
        print(f"\n=== ALIGNMENT VALIDATION ===")
        print(f"Original: {original_file}")
        print(f"Converted: {converted_file}")
        print(f"\nTotal issues found: {len(all_issues)}")
        
        if all_issues:
            print("\nIssues:")
            for issue in all_issues:
                print(f"  - {issue}")
        else:
            print("\n✅ All alignments preserved!")
    
    if strict and all_issues:
        print("\n❌ Validation FAILED (strict mode)")
        return False
    elif all_issues:
        print("\n⚠ Validation completed with issues.")
        return True
    else:
        print("\n✅ Validation PASSED!")
        return True

def main():
    parser = argparse.ArgumentParser(
        description='Validate alignment preservation between original and converted documents.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Compare two MD files:
    python3 validate_alignment.py original.md converted.md
  
  Compare MD with PDF (extracts MD from PDF first):
    python3 validate_alignment.py original.md --pdf converted.pdf
  
  Generate HTML report:
    python3 validate_alignment.py original.md converted.md --report report.html
"""
    )
    parser.add_argument('original', help='Original Markdown file')
    parser.add_argument('converted', help='Converted file (MD or PDF)')
    parser.add_argument('--pdf', action='store_true',
                        help='Second file is a PDF (requires Pandoc)')
    parser.add_argument('--report', '-r', help='Generate HTML report file')
    parser.add_argument('--strict', action='store_true',
                        help='Exit with error if any issues found')
    parser.add_argument('--ignore-whitespace', action='store_true',
                        help='Ignore whitespace differences')
    parser.add_argument('--tolerance', type=int, default=5,
                        help='Pixel tolerance for alignment (default: 5px)')
    
    args = parser.parse_args()
    
    success = validate_alignment(args.original, args.converted, args.pdf,
                                 args.report, args.strict, args.ignore_whitespace,
                                 args.tolerance)
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
