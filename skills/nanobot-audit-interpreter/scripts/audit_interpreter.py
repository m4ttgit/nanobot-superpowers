#!/usr/bin/env python3
"""audit_interpreter.py — Interpret audit reports and identify discrepancies."""
import argparse
import json
import sys


def parse_audit_opinion(audit_text):
    """Extract audit opinion from report text."""
    audit_text_lower = audit_text.lower()
    
    if 'adverse' in audit_text_lower:
        return 'adverse'
    if 'disclaimer' in audit_text_lower or 'unable to express' in audit_text_lower:
        return 'disclaimer'
    if 'qualified' in audit_text_lower or 'except for' in audit_text_lower:
        return 'qualified'
    if 'unqualified' in audit_text_lower or 'clean' in audit_text_lower or 'fair presentation' in audit_text_lower:
        return 'unqualified'
    
    return 'unknown'


def identify_findings(audit_text):
    """Identify key findings and red flags in audit text."""
    findings = []
    audit_text_lower = audit_text.lower()
    
    if 'material weakness' in audit_text_lower:
        findings.append({
            'type': 'internal_control',
            'description': 'Material weakness in internal controls identified',
            'severity': 'high'
        })
    
    if 'going concern' in audit_text_lower or 'substantial doubt' in audit_text_lower:
        findings.append({
            'type': 'going_concern',
            'description': 'Going concern flag raised by auditors',
            'severity': 'high'
        })
    
    if 'related party' in audit_text_lower:
        findings.append({
            'type': 'related_party',
            'description': 'Related party transactions disclosed',
            'severity': 'medium'
        })
    
    if 'contingent liability' in audit_text_lower or 'litigation' in audit_text_lower:
        findings.append({
            'type': 'contingent_liability',
            'description': 'Contingent liabilities disclosed',
            'severity': 'medium'
        })
    
    return findings


def assess_risk(opinion, findings):
    """Assess overall audit risk based on opinion and findings."""
    if opinion == 'adverse' or opinion == 'disclaimer':
        return 'high'
    if opinion == 'qualified':
        return 'medium'
    if any(f['severity'] == 'high' for f in findings):
        return 'high'
    if any(f['severity'] == 'medium' for f in findings):
        return 'medium'
    return 'low'


def main():
    parser = argparse.ArgumentParser(description='Interpret audit reports and identify discrepancies.')
    parser.add_argument('input_json', help='Path to input JSON file with audit_text and financial_data')
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

    audit_text = data.get('audit_text', '')

    opinion = parse_audit_opinion(audit_text)

    findings = identify_findings(audit_text)

    risk_score = assess_risk(opinion, findings)

    recommendations = []
    if opinion in ['adverse', 'disclaimer']:
        recommendations.append('Immediate management action required — consult external advisors')
    if any(f['type'] == 'internal_control' for f in findings):
        recommendations.append('Remediate material weaknesses in internal controls per SOX 404')
    if any(f['type'] == 'going_concern' for f in findings):
        recommendations.append('Develop going concern mitigation plan and disclose to stakeholders')

    result = {
        'audit_opinion': opinion,
        'key_findings': findings,
        'financial_discrepancies': [],
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
