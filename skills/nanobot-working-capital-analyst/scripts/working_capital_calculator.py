#!/usr/bin/env python3
"""working_capital_calculator.py — Calculate working capital ratios and cash conversion cycle."""
import argparse
import json
import sys


def calculate_ratios(data):
    """Calculate all working capital ratios from input data."""
    revenue = data.get('revenue', 0)
    cogs = abs(data.get('cogs', 0))
    accounts_receivable = abs(data.get('accounts_receivable', 0))
    inventory = abs(data.get('inventory', 0))
    accounts_payable = abs(data.get('accounts_payable', 0))
    cash = data.get('cash', 0)

    results = {
        'input_summary': {
            'revenue': revenue,
            'cogs': cogs,
            'accounts_receivable': accounts_receivable,
            'inventory': inventory,
            'accounts_payable': accounts_payable,
            'cash': cash,
        },
        'ratios': {},
        'flags': [],
    }

    debtor_days = None
    creditor_days = None
    inventory_days = None
    ccc = None

    working_capital = cash + accounts_receivable + inventory - accounts_payable
    results['ratios']['working_capital'] = working_capital
    results['ratios']['working_capital_ratio'] = None

    current_assets = cash + accounts_receivable + inventory
    current_liabilities = accounts_payable
    if current_liabilities > 0:
        results['ratios']['working_capital_ratio'] = current_assets / current_liabilities

    if working_capital < 0:
        results['flags'].append({
            'level': 'red',
            'metric': 'working_capital',
            'message': f'Negative working capital (${working_capital:,.0f}) — liquidity risk'
        })

    if revenue > 0 and accounts_receivable > 0:
        debtor_days = (accounts_receivable / revenue) * 365
    results['ratios']['debtor_days'] = debtor_days

    if debtor_days is not None:
        if debtor_days > 60:
            results['flags'].append({
                'level': 'red',
                'metric': 'debtor_days',
                'message': f'Debtor Days {debtor_days:.1f} — collections process needs improvement'
            })
        elif debtor_days > 45:
            results['flags'].append({
                'level': 'yellow',
                'metric': 'debtor_days',
                'message': f'Debtor Days {debtor_days:.1f} — above benchmark (30-45 days)'
            })

    if cogs > 0 and accounts_payable > 0:
        creditor_days = (accounts_payable / cogs) * 365
    results['ratios']['creditor_days'] = creditor_days

    if creditor_days is not None:
        if creditor_days > 90:
            results['flags'].append({
                'level': 'red',
                'metric': 'creditor_days',
                'message': f'Creditor Days {creditor_days:.1f} — supplier relationships at risk'
            })
        elif creditor_days > 60:
            results['flags'].append({
                'level': 'yellow',
                'metric': 'creditor_days',
                'message': f'Creditor Days {creditor_days:.1f} — above benchmark (30-60 days)'
            })

    if cogs > 0 and inventory > 0:
        inventory_days = (inventory / cogs) * 365
    results['ratios']['inventory_days'] = inventory_days

    if inventory_days is not None:
        if inventory_days > 60:
            results['flags'].append({
                'level': 'red',
                'metric': 'inventory_days',
                'message': f'Inventory Days {inventory_days:.1f} — excess stock tying up cash'
            })
        elif inventory_days > 45:
            results['flags'].append({
                'level': 'yellow',
                'metric': 'inventory_days',
                'message': f'Inventory Days {inventory_days:.1f} — above benchmark (30-45 days)'
            })

    if debtor_days is not None and inventory_days is not None and creditor_days is not None:
        ccc = debtor_days + inventory_days - creditor_days
    results['ratios']['cash_conversion_cycle'] = ccc

    if ccc is not None:
        if ccc > 90:
            results['flags'].append({
                'level': 'red',
                'metric': 'cash_conversion_cycle',
                'message': f'Cash Conversion Cycle {ccc:.1f} days — cash trap, too much capital tied up'
            })
        elif ccc > 60:
            results['flags'].append({
                'level': 'yellow',
                'metric': 'cash_conversion_cycle',
                'message': f'Cash Conversion Cycle {ccc:.1f} days — above benchmark (<60 days)'
            })

    return results


def format_report(results, currency='USD'):
    """Format results as a human-readable report."""
    lines = []
    lines.append('=' * 50)
    lines.append('WORKING CAPITAL ANALYSIS')
    lines.append('=' * 50)
    lines.append('')

    inputs = results['input_summary']
    lines.append('Input Summary:')
    for k, v in inputs.items():
        if v is not None:
            lines.append(f'  {k.replace("_", " ").title():<25} ${v:,.0f}')
    lines.append('')

    ratios = results['ratios']
    lines.append('Ratios:')
    lines.append('-' * 50)

    def fmt_days(val, benchmark):
        if val is None:
            return '  N/A (insufficient data)'
        return f'  {val:.1f} days (benchmark: {benchmark})'

    lines.append(f'  Working Capital:          ${ratios.get("working_capital", 0):,.0f}')
    wc_ratio = ratios.get('working_capital_ratio')
    if wc_ratio is not None:
        lines.append(f'  Working Capital Ratio:      {wc_ratio:.2f}x (benchmark: >1.2x)')
    else:
        lines.append('  Working Capital Ratio:      N/A (no current liabilities)')

    lines.append(fmt_days(ratios.get('debtor_days'), '30-45 days'))
    lines.append(fmt_days(ratios.get('inventory_days'), '30-60 days'))
    lines.append(fmt_days(ratios.get('creditor_days'), '30-60 days'))
    lines.append(fmt_days(ratios.get('cash_conversion_cycle'), '<60 days'))

    if results['flags']:
        lines.append('')
        lines.append('Flags:')
        lines.append('-' * 50)
        for flag in results['flags']:
            icon = '🔴' if flag['level'] == 'red' else '🟡'
            lines.append(f'{icon} {flag["metric"].replace("_", " ").upper()}: {flag["message"]}')

    lines.append('')
    lines.append('=' * 50)
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Calculate working capital ratios from financial data.')
    parser.add_argument('input_json', help='Path to input JSON file with financial data')
    parser.add_argument('--output', dest='output', default=None,
                        help='Output JSON file (default: stdout)')
    parser.add_argument('--format', dest='fmt', choices=['json', 'text'], default='text',
                        help='Output format: json or text (default: text)')
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

    results = calculate_ratios(data)

    if args.fmt == 'json':
        output = json.dumps(results, indent=2, default=str)
    else:
        output = format_report(results)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Saved: {args.output}")
    else:
        print(output)

    if results['flags']:
        sys.exit(0 if all(f['level'] == 'yellow' for f in results['flags']) else 1)


if __name__ == '__main__':
    main()
