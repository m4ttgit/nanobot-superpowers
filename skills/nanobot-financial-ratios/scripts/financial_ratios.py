#!/usr/bin/env python3
"""financial_ratios.py — Calculate all 5 categories of financial ratios."""
import argparse
import json
import sys


def calculate_all_ratios(data):
    """Calculate all 5 categories of financial ratios."""
    income = data.get('income_statement', {})
    balance = data.get('balance_sheet', {})

    revenue = abs(income.get('revenue', 0))
    cogs = abs(income.get('cogs', 0))
    gross_profit = abs(income.get('gross_profit', 0))
    ebit = abs(income.get('ebit', 0))
    ebitda = abs(income.get('ebitda', 0))
    net_income = abs(income.get('net_income', 0))
    interest = abs(income.get('interest', 0))

    current_assets = abs(balance.get('current_assets', 0))
    total_assets = abs(balance.get('total_assets', 0))
    inventory = abs(balance.get('inventory', 0))
    ar = abs(balance.get('accounts_receivable', 0))
    cash = abs(balance.get('cash', 0))
    current_liabilities = abs(balance.get('current_liabilities', 0))
    total_liabilities = abs(balance.get('total_liabilities', 0))
    total_equity = abs(balance.get('total_equity', 0))
    total_debt = abs(balance.get('total_debt', total_liabilities))

    result = {'profitability': {}, 'liquidity': {}, 'leverage': {}, 'efficiency': {}, 'valuation': {}}

    # Profitability
    if revenue > 0:
        result['profitability']['gross_margin'] = gross_profit / revenue
        result['profitability']['operating_margin'] = ebit / revenue
        result['profitability']['net_margin'] = net_income / revenue
    if total_assets > 0:
        result['profitability']['roa'] = net_income / total_assets
    if total_equity > 0:
        result['profitability']['roe'] = net_income / total_equity
    if revenue > 0:
        result['profitability']['ebitda_margin'] = ebitda / revenue

    # Liquidity
    if current_liabilities > 0:
        result['liquidity']['current_ratio'] = current_assets / current_liabilities
        result['liquidity']['quick_ratio'] = (current_assets - inventory) / current_liabilities
        result['liquidity']['working_capital'] = current_assets - current_liabilities
    if cash > 0 and current_liabilities > 0:
        result['liquidity']['cash_ratio'] = cash / current_liabilities

    # Leverage
    if total_equity > 0:
        result['leverage']['debt_to_equity'] = total_debt / total_equity
    if total_assets > 0:
        result['leverage']['debt_to_assets'] = total_debt / total_assets
    if ebit > 0:
        result['leverage']['interest_coverage'] = ebit / interest if interest > 0 else None
    if total_assets > 0 and total_equity > 0:
        result['leverage']['financial_leverage'] = total_assets / total_equity

    # Efficiency
    if total_assets > 0 and revenue > 0:
        result['efficiency']['asset_turnover'] = revenue / total_assets
    if cogs > 0 and inventory > 0:
        result['efficiency']['inventory_turnover'] = cogs / inventory
        result['efficiency']['inventory_days'] = (inventory / cogs) * 365
    if revenue > 0 and ar > 0:
        result['efficiency']['receivables_turnover'] = revenue / ar
        result['efficiency']['debtor_days'] = (ar / revenue) * 365
    if cogs > 0 and current_liabilities > 0:
        ap = abs(balance.get('accounts_payable', 0))
        result['efficiency']['creditor_days'] = (ap / cogs) * 365
    if all(v is not None for v in [result['efficiency'].get('debtor_days'), result['efficiency'].get('inventory_days'), result['efficiency'].get('creditor_days')]):
        result['efficiency']['cash_conversion_cycle'] = (
            result['efficiency']['debtor_days'] +
            result['efficiency']['inventory_days'] -
            result['efficiency']['creditor_days']
        )

    # Valuation (if market data provided)
    market_cap = data.get('market_cap')
    enterprise_value = data.get('enterprise_value')
    if market_cap and net_income > 0:
        result['valuation']['pe_ratio'] = market_cap / net_income
    if market_cap and total_equity > 0:
        result['valuation']['pb_ratio'] = market_cap / total_equity
    if enterprise_value and ebitda > 0:
        result['valuation']['ev_to_ebitda'] = enterprise_value / ebitda
    growth_rate = data.get('growth_rate')
    if market_cap and growth_rate:
        pe = result['valuation'].get('pe_ratio')
        if pe:
            result['valuation']['peg_ratio'] = pe / growth_rate

    return result


def main():
    parser = argparse.ArgumentParser(description='Calculate all financial ratios.')
    parser.add_argument('input_json', help='Path to financial data JSON file')
    parser.add_argument('--output', dest='output', default=None,
                        help='Output JSON file (default: stdout)')
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

    result = calculate_all_ratios(data)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, default=str)
        print(f"Saved: {args.output}")
    else:
        print(json.dumps(result, indent=2, default=str))


if __name__ == '__main__':
    main()
