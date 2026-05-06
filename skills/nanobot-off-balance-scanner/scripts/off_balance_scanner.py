#!/usr/bin/env python3
"""off_balance_scanner.py — Detect off-balance sheet items and adjust leverage ratios."""
import argparse
import json
import sys


def scan_operating_leases(notes):
    """Detect operating lease obligations from notes."""
    leases = []
    notes_lower = notes.lower()
    
    if 'operating lease' in notes_lower or 'right-of-use' in notes_lower:
        leases.append({
            'type': 'operating_lease',
            'description': 'Operating lease obligations (post-IFRS16/ASC842)',
            'estimated_value': None,
            'note_reference': 'Note 12 (typical)'
        })
    
    return leases


def scan_special_entities(notes):
    """Detect SPE/VIE exposures from notes."""
    entities = []
    notes_lower = notes.lower()
    
    if 'special purpose entity' in notes_lower or 'variable interest entity' in notes_lower or 'vie' in notes_lower:
        entities.append({
            'type': 'spe_vie',
            'description': 'Special Purpose Entity / Variable Interest Entity exposure',
            'estimated_value': None,
            'note_reference': 'Note 15 (typical)'
        })
    
    return entities


def scan_guarantees(notes):
    """Detect guarantees and contingent liabilities."""
    guarantees = []
    notes_lower = notes.lower()
    
    if 'guarantee' in notes_lower or 'contingent liability' in notes_lower:
        guarantees.append({
            'type': 'guarantee',
            'description': 'Guarantees or contingent liabilities',
            'estimated_value': None,
            'note_reference': 'Note 18 (typical)'
        })
    
    return guarantees


def calculate_total_off_balance(off_balance_items):
    """Sum estimated values of off-balance items."""
    total = 0
    for item in off_balance_items:
        if item.get('estimated_value'):
            total += item['estimated_value']
    return total


def adjust_leverage_ratios(financial_data, total_off_balance_debt):
    """Recalculate leverage ratios including off-balance debt."""
    balance = financial_data.get('balance_sheet', {})
    total_debt = abs(balance.get('total_debt', 0))
    total_assets = abs(balance.get('total_assets', 0))
    total_equity = abs(balance.get('total_equity', total_assets - total_debt))
    
    adjusted_total_debt = total_debt + total_off_balance_debt
    
    adjusted_debt_to_assets = adjusted_total_debt / total_assets if total_assets > 0 else 0
    adjusted_debt_to_equity = adjusted_total_debt / total_equity if total_equity > 0 else 0
    
    return {
        'original_debt_to_assets': total_debt / total_assets if total_assets > 0 else 0,
        'adjusted_debt_to_assets': round(adjusted_debt_to_assets, 4),
        'original_debt_to_equity': total_debt / total_equity if total_equity > 0 else 0,
        'adjusted_debt_to_equity': round(adjusted_debt_to_equity, 4),
        'total_off_balance_debt': total_off_balance_debt
    }


def assess_risk(off_balance_items, total_assets, total_off_balance_debt):
    """Assess risk of off-balance sheet exposure."""
    if not off_balance_items:
        return 'low'
    
    if total_assets > 0 and total_off_balance_debt / total_assets > 0.15:
        return 'high'
    
    if total_off_balance_debt > 0:
        return 'medium'
    
    return 'low'


def main():
    parser = argparse.ArgumentParser(description='Detect off-balance sheet items and adjust leverage ratios.')
    parser.add_argument('input_json', help='Path to input JSON file with financial_data and notes')
    parser.add_argument('--output', dest='output', default=None, help='Output JSON file (default: stdout)')
    args = parser.parse_args()

    try:
        with open(args.input_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {args.input_json}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)

    financial_data = data.get('financial_data', {})
    notes = data.get('notes', '')

    off_balance_items = []
    off_balance_items.extend(scan_operating_leases(notes))
    off_balance_items.extend(scan_special_entities(notes))
    off_balance_items.extend(scan_guarantees(notes))

    total_off_balance_debt = calculate_total_off_balance(off_balance_items)
    
    balance = financial_data.get('balance_sheet', {})
    total_assets = abs(balance.get('total_assets', 0))
    
    adjusted_ratios = adjust_leverage_ratios(financial_data, total_off_balance_debt)
    risk_score = assess_risk(off_balance_items, total_assets, total_off_balance_debt)

    recommendations = []
    if risk_score == 'high':
        recommendations.append('Immediate disclosure of off-balance items in MD&A')
    if any(item['type'] == 'spe_vie' for item in off_balance_items):
        recommendations.append('Review SPE/VIE structures for consolidation requirements')
    if any(item['type'] == 'operating_lease' for item in off_balance_items):
        recommendations.append('Ensure right-of-use assets are properly capitalized per IFRS16/ASC842')

    result = {
        'off_balance_items': off_balance_items,
        'total_off_balance_debt': total_off_balance_debt,
        'adjusted_ratios': adjusted_ratios,
        'risk_score': risk_score,
        'recommendations': recommendations
    }

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, default=str)
        print(f"Saved: {args.output}")
    else:
        print(json.dumps(result, indent=2, default=str))


if __name__ == '__main__':
    main()
