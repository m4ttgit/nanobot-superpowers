# Working Capital Benchmarks

Industry benchmarks for working capital ratios. Use these to flag outliers in company analysis.

## Working Capital Ratio
**Formula:** Current Assets ÷ Current Liabilities
**Benchmark:** > 1.2x (healthy liquidity)
**Red Flag:** < 1.0x (liquidity crisis risk)
**Yellow Flag:** 1.0x - 1.2x (tight but manageable)

| Industry | Typical Range |
|---|---|
| SaaS / Software | 1.5x - 3.0x (low inventory) |
| Retail | 1.2x - 1.8x |
| Manufacturing | 1.1x - 1.5x |
| Services | 1.8x - 3.5x (minimal working capital) |

## Debtor Days (DSO)
**Formula:** (Accounts Receivable ÷ Revenue) × 365
**Benchmark:** 30-45 days
**Red Flag:** > 60 days (slow collections)
**Yellow Flag:** 45-60 days (needs improvement)

| Industry | Typical Range |
|---|---|
| SaaS / Software | 20-35 days (upfront/retainer) |
| Retail | 5-15 days (POS systems) |
| Manufacturing | 45-60 days (net-60 terms) |
| Services | 30-45 days (net-30/45 terms) |

## Creditor Days (DPO)
**Formula:** (Accounts Payable ÷ COGS) × 365
**Benchmark:** 30-60 days
**Red Flag:** > 90 days (supplier relationships at risk)
**Yellow Flag:** 60-90 days (stretching payables dangerously)

| Industry | Typical Range |
|---|---|
| SaaS / Software | 15-30 days (cloud costs upfront) |
| Retail | 45-60 days (inventory financing) |
| Manufacturing | 60-90 days (supply chain terms) |
| Services | 20-40 days (contractor payments) |

## Inventory Days (DIO)
**Formula:** (Inventory ÷ COGS) × 365
**Benchmark:** 30-60 days
**Red Flag:** > 90 days (excess/obsolete stock)
**Yellow Flag:** 60-90 days (slow-moving inventory)

| Industry | Typical Range |
|---|---|
| SaaS / Software | N/A (no inventory) |
| Retail | 45-75 days (fast fashion ~30, electronics ~60) |
| Manufacturing | 60-120 days (depends on complexity) |
| Services | N/A (no inventory) |

**Note:** For SaaS/Software companies, inventory should be $0. If inventory > 0, flag for user review.

## Cash Conversion Cycle
**Formula:** Debtor Days + Inventory Days - Creditor Days
**Benchmark:** < 60 days (efficient)
**Red Flag:** > 90 days (cash trap - too much capital tied up)
**Yellow Flag:** 60-90 days (room for improvement)

| Industry | Typical Range |
|---|---|
| SaaS / Software | 20-45 days (low capital tied up) |
| Retail | 30-60 days |
| Manufacturing | 45-90 days |
| Services | 10-30 days (minimal working capital) |

## Common Pitfalls

1. **Using Revenue instead of COGS for Creditor Days** — AP is a % of COGS, not Revenue
2. **Using ending AR instead of average AR** — For more accuracy, use (beginning AR + ending AR) ÷ 2
3. **Forgetting Inventory for SaaS** — SaaS companies should have $0 inventory; if not, investigate
4. **Not adjusting for seasonality** — Retail/Manufacturing may have 2x inventory days in Q4 vs Q1
5. **Mixing calendar vs working days** — Some analysts use 360 or 250 days instead of 365; be consistent