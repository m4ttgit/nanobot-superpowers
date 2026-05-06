#!/usr/bin/env python3
"""data_normalizer.py — Map XBRL/proprietary Chart of Accounts to unified schema."""
import argparse
import json
import sys


def normalize_xbrl(data):
    """Normalize XBRL format to unified schema."""
    result = {
        'company_name': data.get('xbrl_context', {}).get('entity', 'Unknown'),
        'fiscal_year': data.get('xbrl_context', {}).get('period', 'Unknown'),
        'currency': 'USD',
        'income_statement': {},
        'balance_sheet': {},
        'cash_flow': {},
    }

    facts = data.get('xbrl_facts', [])
    
    for fact in facts:
        concept = fact.get('concept', '')
        value = abs(fact.get('value', 0))
        
        # Map to income statement
        if concept in ['Revenue', 'SalesRevenueNet']:
            result['income_statement']['revenue'] = value
        elif concept in ['CostOfGoodsSold', 'CostOfSales']:
            result['income_statement']['cogs'] = value
        elif concept == 'GrossProfit':
            result['income_statement']['gross_profit'] = value
        elif concept in ['OperatingIncome', 'EBIT']:
            result['income_statement']['ebit'] = value
        elif concept == 'EBITDA':
            result['income_statement']['ebitda'] = value
        elif concept == 'InterestExpense':
            result['income_statement']['interest'] = value
        elif concept == 'NetIncomeLoss':
            result['income_statement']['net_income'] = value
        # Map to balance sheet
        elif concept == 'AssetsCurrent':
            result['balance_sheet']['current_assets'] = value
        elif concept == 'Assets':
            result['balance_sheet']['total_assets'] = value
        elif concept == 'InventoryNet':
            result['balance_sheet']['inventory'] = value
        elif concept == 'ReceivablesNet':
            result['balance_sheet']['accounts_receivable'] = value
        elif concept == 'CashAndCashEquivalents':
            result['balance_sheet']['cash'] = value
        elif concept == 'LiabilitiesCurrent':
            result['balance_sheet']['current_liabilities'] = value
        elif concept == 'Liabilities':
            result['balance_sheet']['total_liabilities'] = value
        elif concept == 'StockholdersEquity':
            result['balance_sheet']['total_equity'] = value
        elif concept == 'LongTermDebt':
            result['balance_sheet']['total_debt'] = value

    return result


def normalize_proprietary(data):
    """Normalize proprietary Chart of Accounts to unified schema."""
    result = {
        'company_name': data.get('company_name', 'Unknown'),
        'fiscal_year': data.get('fiscal_year', 'Unknown'),
        'currency': data.get('currency', 'USD'),
        'income_statement': {},
        'balance_sheet': {},
        'cash_flow': {},
        '_original_fields': {},
    }

    coa = data.get('chart_of_accounts', [])
    
    def infer_category(account_name):
        """Infer if account belongs to Income Statement or Balance Sheet."""
        name = account_name.lower()
        if any(k in name for k in ['revenue', 'sales', 'income']):
            return 'income'
        if any(k in name for k in ['cost', 'cogs', 'expense', 'operating']):
            return 'income'
        if any(k in name for k in ['asset', 'inventory', 'receivable', 'cash']):
            return 'balance'
        if any(k in name for k in ['liability', 'debt', 'payable']):
            return 'balance'
        if any(k in name for k in ['equity', 'retained', 'capital']):
            return 'balance'
        return None

    def map_field(account_name, value):
        """Map proprietary field to unified name."""
        name = account_name.lower()
        # Revenue
        if any(k in name for k in ['1', 'revenue', 'sales']):
            return 'revenue', value
        # COGS
        if any(k in name for k in ['cogs', 'cost of goods', 'cost of sales']):
            return 'cogs', value
        # EBIT/EBITDA
        if 'ebitda' in name or 'earnings before' in name:
            return 'ebitda', value
        if 'ebit' in name or 'operating income' in name:
            return 'ebit', value
        # Net Income
        if 'net income' in name or 'net earnings' in name:
            return 'net_income', value
        # Balance Sheet
        if 'inventory' in name:
            return 'inventory', value
        if 'receivable' in name:
            return 'accounts_receivable', value
        if 'cash' in name and 'flow' not in name:
            return 'cash', value
        if 'payable' in name:
            return 'accounts_payable', value
        if 'asset' in name and 'total' in name:
            return 'total_assets', value
        if 'liability' in name and 'total' in name:
            return 'total_liabilities', value
        if 'equity' in name or 'stockholder' in name:
            return 'total_equity', value
        return None, None

    for account in coa:
        name = account.get('account', '')
        value = abs(account.get('value', 0))
        result['_original_fields'][name] = value
        
        unified_name, val = map_field(name, value)
        if unified_name:
            category = infer_category(name)
            if category == 'income':
                result['income_statement'][unified_name] = val
            elif category == 'balance':
                result['balance_sheet'][unified_name] = val

    return result


def main():
    parser = argparse.ArgumentParser(description='Normalize financial data to unified schema.')
    parser.add_argument('input_json', help='Path to financial data JSON file')
    parser.add_argument('--output', dest='output', default=None,
                        help='Output JSON file (default: stdout)')
    parser.add_argument('--format', dest='fmt', choices=['xbrl', 'proprietary', 'standard'],
                        default='standard', help='Input format (default: standard/auto-detect)')
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

    # Auto-detect format
    fmt = args.fmt
    if fmt == 'standard' and 'xbrl_context' in data:
        fmt = 'xbrl'
    elif fmt == 'standard' and 'chart_of_accounts' in data:
        fmt = 'proprietary'

    if fmt == 'xbrl':
        result = normalize_xbrl(data)
    elif fmt == 'proprietary':
        result = normalize_proprietary(data)
    else:
        result = data  # Already in standard format

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, default=str)
        print(f"Saved: {args.output}")
    else:
        print(json.dumps(result, indent=2, default=str))


if __name__ == '__main__':
    main()
