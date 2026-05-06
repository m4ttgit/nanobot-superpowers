#!/usr/bin/env python3
"""financial_orchestrator.py — Decision Engine for financial analysis."""
import argparse
import json
import sys


def check_auditor_opinion(data):
    """Parse auditor opinion from input or audit report text."""
    opinion = data.get('auditor_opinion', '').strip().lower()
    if 'adverse' in opinion:
        return 'Adverse'
    if 'disclaimer' in opinion or 'cannot' in opinion:
        return 'Disclaimer'
    if 'qualif' in opinion:
        return 'Qualifed'
    if 'unqualified' in opinion or 'clean' in opinion:
        return 'Unqualified'
    return None


def determine_routing(data):
    """Determine which modules to fire based on data quality and auditor opinion."""
    routing = {
        'modules': [],
        'skip': [],
        'survival_mode': False,
        'red_flags': [],
        'yellow_flags': [],
    }

    # Always fire core modules
    routing['modules'].extend([
        'nanobot-financial-ratios',
        'nanobot-working-capital-analyst',
    ])

    # Check auditor opinion (gatekeeper)
    opinion = check_auditor_opinion(data)
    if opinion:
        routing['auditor_opinion'] = opinion
        if opinion == 'Adverse':
            routing['survival_mode'] = True
            routing['skip'] = ['valuation_analysis', 'growth_projections']
            routing['modules'].extend([
                'nanobot-bankruptcy-scorer',
                'nanobot-off-balance-scanner',
            ])
            routing['red_flags'].append('Adverse auditor opinion — company in financial distress')
            return routing
        elif opinion == 'Disclaimer':
            routing['modules'].extend([
                'nanobot-audit-interpreter',
                'nanobot-bankruptcy-scorer',
                'nanobot-off-balance-scanner',
            ])
            routing['yellow_flags'].append('Disclaimer opinion — limited audit assurance')
        elif opinion == 'Qualifed':
            routing['yellow_flags'].append('Qualifed opinion — issues noted but not fatal')

    # Conditionally fire based on data
    if data.get('market_cap') and data.get('enterprise_value'):
        routing['modules'].append('nanobot-valuation-engine')

    if data.get('balance_sheet', {}).get('current_assets'):
        routing['modules'].append('nanobot-working-capital-analyst')

    # Check for red flag escalation after initial modules
    routing['escalate_if'] = {
        'negative_working_capital': ['nanobot-cash-flow-quality'],
        'debtor_days > 60': ['nanobot-collection-efficiency'],
        'current_ratio < 1.0': ['nanobot-off-balance-scanner'],
    }

    return routing


def validate_input(data):
    """Validate that required sections exist."""
    missing = []
    if 'income_statement' not in data:
        missing.append('income_statement')
    if 'balance_sheet' not in data:
        missing.append('balance_sheet')
    if 'cash_flow' not in data:
        missing.append('cash_flow')
    return missing


def main():
    parser = argparse.ArgumentParser(description='Financial Orchestrator — Decision Engine.')
    parser.add_argument('input_json', help='Path to financial data JSON file')
    parser.add_argument('--output', dest='output', default=None,
                        help='Output JSON file (default: stdout)')
    parser.add_argument('--format', dest='fmt', choices=['json', 'text'],
                        default='json', help='Output format (default: json)')
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

    missing = validate_input(data)
    if missing:
        result = {'error': f"Missing required sections: {', '.join(missing)}"}
    else:
        result = determine_routing(data)

    if args.fmt == 'json':
        output = json.dumps(result, indent=2, default=str)
    else:
        lines = []
        lines.append('Financial Orchestrator Routing Decision')
        lines.append('=' * 50)
        if 'error' in result:
            lines.append(f"ERROR: {result['error']}")
        else:
            lines.append(f"Auditor Opinion: {result.get('auditor_opinion', 'Not provided')}")
            lines.append(f"Survival Mode: {result['survival_mode']}")
            lines.append('')
            lines.append('Modules to Fire:')
            for m in result['modules']:
                lines.append(f"  - {m}")
            if result['skip']:
                lines.append('')
                lines.append('Skipped (Survival Mode):')
                for s in result['skip']:
                    lines.append(f"  - {s}")
            if result['red_flags']:
                lines.append('')
                lines.append('Red Flags:')
                for f in result['red_flags']:
                    lines.append(f"  🔴 {f}")
            if result['yellow_flags']:
                lines.append('')
                lines.append('Yellow Flags:')
                for f in result['yellow_flags']:
                    lines.append(f"  🟡 {f}")
        output = '\n'.join(lines)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Saved: {args.output}")
    else:
        print(output)

    sys.exit(0 if not missing else 1)


if __name__ == '__main__':
    main()
