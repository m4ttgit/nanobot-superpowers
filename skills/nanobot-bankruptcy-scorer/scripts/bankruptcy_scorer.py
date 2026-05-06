#!/usr/bin/env python3
"""bankruptcy_scorer.py — Altman Z-Score + Beneish M-Score."""
import argparse
import json
import sys


def calculate_z_score(data):
    """Calculate Altman Z-Score for bankruptcy prediction."""
    balance = data.get('balance_sheet', {})
    income = data.get('income_statement', {})

    working_capital = abs(balance.get('current_assets', 0)) - abs(balance.get('current_liabilities', 0))
    total_assets = abs(balance.get('total_assets', 0))
    retained_earnings = abs(balance.get('retained_earnings', 0))
    ebit = abs(income.get('ebit', 0))
    market_value_equity = abs(data.get('market_value_equity', total_assets))
    sales = abs(income.get('revenue', 0))
    total_liabilities = abs(balance.get('total_liabilities', 0))

    if total_assets == 0:
        return None, 'Cannot calculate — Total Assets = 0'

    # Altman Z-Score formula (original, for public manufacturers)
    # Z = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E
    A = working_capital / total_assets
    B = retained_earnings / total_assets
    C = ebit / total_assets
    D = market_value_equity / total_liabilities if total_liabilities > 0 else 0
    E = sales / total_assets

    z = 1.2 * A + 1.4 * B + 3.3 * C + 0.6 * D + 1.0 * E

    # Interpretation
    if z > 2.99:
        zone = 'Safe'
        flag = None
    elif z > 1.81:
        zone = 'Grey'
        flag = '🟡 Grey Zone — monitor closely (Z between 1.81-2.99)'
    else:
        zone = 'Distress'
        flag = '🔴 Distress Zone — HIGH bankruptcy risk (Z < 1.81)'

    return {
        'z_score': round(z, 2),
        'zone': zone,
        'components': {
            'A_working_capital_ratio': round(A, 4),
            'B_retained_earnings_ratio': round(B, 4),
            'C_ebit_ratio': round(C, 4),
            'D_equity_leverage': round(D, 4),
            'E_turnover_ratio': round(E, 4),
        },
        'flag': flag,
    }


def calculate_m_score(data):
    """Calculate Beneish M-Score for earnings manipulation detection."""
    income = data.get('income_statement', {})
    balance = data.get('balance_sheet', {})
    cash_flow = data.get('cash_flow', {})
    net_income = abs(income.get('net_income', 0))

    # Need prior year data for Beneish (year-over-year changes)
    prior = data.get('prior_year', {})
    if not prior:
        return None, 'Cannot calculate — prior year data required for Beneish M-Score'

    # Variables
    # DSRI = Days Sales Receivable Index = (AR_t / Sales_t) / (AR_t-1 / Sales_t-1)
    ar_t = abs(balance.get('accounts_receivable', 0))
    ar_t1 = abs(prior.get('accounts_receivable', 0))
    sales_t = abs(income.get('revenue', 0))
    sales_t1 = abs(prior.get('revenue', 0))
    
    dsri = (ar_t / sales_t) / (ar_t1 / sales_t1) if sales_t > 0 and sales_t1 > 0 and ar_t1 > 0 else 1.0

    # GMI = Gross Margin Index = (Sales_t-1 - COGS_t-1) / (Sales_t - COGS_t)
    cogs_t = abs(income.get('cogs', 0))
    cogs_t1 = abs(prior.get('cogs', 0))
    gmi = ((sales_t1 - cogs_t1) / (sales_t - cogs_t)) if sales_t > cogs_t and sales_t1 > cogs_t1 else 1.0

    # AQI = Asset Quality Index = (AR_t + Inventory_t) / Total_Assets_t
    inventory_t = abs(balance.get('inventory', 0))
    total_assets_t = abs(balance.get('total_assets', 0))
    aqi = (ar_t + inventory_t) / total_assets_t if total_assets_t > 0 else 1.0

    # SGI = Sales Growth Index = Sales_t / Sales_t-1
    sgi = sales_t / sales_t1 if sales_t1 > 0 else 1.0

    # DEPI = Depreciation Index = (Depreciation_t / (Depreciation_t + PP&E_t)) / (Depreciation_t-1 / (Depreciation_t-1 + PP&E_t-1))
    depr_t = abs(income.get('depreciation', 0))
    depr_t1 = abs(prior.get('depreciation', 0))
    ppe_t = abs(balance.get('ppe_net', 0))
    ppe_t1 = abs(prior.get('ppe_net', 0))
    
    depi_num = depr_t / (depr_t + ppe_t) if (depr_t + ppe_t) > 0 else 1.0
    depi_den = depr_t1 / (depr_t1 + ppe_t1) if (depr_t1 + ppe_t1) > 0 else 1.0
    depi = depi_num / depi_den if depi_den > 0 else 1.0

    # SGAI = SG&A Index = (SG&A_t / Sales_t) / (SG&A_t-1 / Sales_t-1)
    sga_t = abs(income.get('sga', 0))
    sga_t1 = abs(prior.get('sga', 0))
    sgai = (sga_t / sales_t) / (sga_t1 / sales_t1) if sales_t > 0 and sales_t1 > 0 else 1.0

    # LVGI = Leverage Index = Total Debt_t / Total Assets_t
    total_debt_t = abs(balance.get('total_debt', 0))
    total_debt_t1 = abs(prior.get('total_debt', 0))
    lvgi = (total_debt_t / total_assets_t) / (total_debt_t1 / abs(prior.get('total_assets', 0))) if total_assets_t > 0 else 1.0

    # TATA = Total Accruals to Total Assets
    cfo = abs(cash_flow.get('operating_cash_flow', 0))
    tata = (net_income - cfo) / total_assets_t if total_assets_t > 0 else 0

    # Beneish M-Score formula
    # M = -4.84 + 0.92DSRI + 0.528GMI + 0.404AQI + 0.892SGI + 0.115DEPI + 0.172SGAI + 4.679TATA + 0.327LVGI
    m = -4.84 + 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi + 0.115 * depi + 0.172 * sgai + 4.679 * tata + 0.327 * lvgi

    # Interpretation
    if m < -2.22:
        assessment = 'Low probability of earnings manipulation'
        flag = None
    elif m < -1.78:
        assessment = 'Moderate probability'
        flag = '🟡 Moderate manipulation risk — review accruals'
    else:
        assessment = 'High probability of earnings manipulation'
        flag = '🔴 HIGH manipulation risk — forensic accounting review recommended'

    return {
        'm_score': round(m, 2),
        'assessment': assessment,
        'variables': {
            'DSRI': round(dsri, 2),
            'GMI': round(gmi, 2),
            'AQI': round(aqi, 2),
            'SGI': round(sgi, 2),
            'DEPI': round(depi, 2),
            'SGAI': round(sgai, 2),
            'TATA': round(tata, 4),
            'LVGI': round(lvgi, 2),
        },
        'flag': flag,
    }


def main():
    parser = argparse.ArgumentParser(description='Calculate bankruptcy risk (Altman Z + Beneish M).')
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

    result = {'models': {}}

    # Altman Z-Score
    z_result, z_error = calculate_z_score(data)
    if z_result:
        result['models']['altman_z_score'] = z_result
    else:
        result['models']['altman_z_score'] = {'error': z_error}

    # Beneish M-Score
    m_result, m_error = calculate_m_score(data)
    if m_result:
        result['models']['beneish_m_score'] = m_result
    else:
        result['models']['beneish_m_score'] = {'error': m_error}

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, default=str)
        print(f"Saved: {args.output}")
    else:
        print(json.dumps(result, indent=2, default=str))


if __name__ == '__main__':
    main()
