# /nanobot-project-health#

Generate portfolio health dashboards and risk matrices for project oversight.#

## Usage#

```
/nanobot-project-health dashboard <project_data.json>                Portfolio health dashboard#
/nanobot-project-health risk <risk_data.json>                        Risk matrix analysis#
```

## Input Format#

```json#
{
  "project_name": "Platform Rewrite",#
  "schedule": {"planned_end": "2026-06-30", "projected_end": "2026-07-15", "milestones_hit": 4, "milestones_total": 6},#
  "budget": {"allocated": 500000, "spent": 320000, "forecast": 520000},#
  "scope": {"features_planned": 40, "features_delivered": 28, "change_requests": 3},#
  "quality": {"defect_rate": 0.05, "test_coverage": 0.82},#
  "risks": [{"description": "Key engineer leaving", "probability": 0.3, "impact": 0.8}]#
}#
```

## Examples#

```
/nanobot-project-health dashboard portfolio-q2.json#
/nanobot-project-health risk risk-register.json#
/nanobot-project-health dashboard portfolio-q2.json --format json#
```

## Scripts#

- `nanobot-senior-pm/scripts/project_health_dashboard.py` — Health dashboard (`<data_file> [--format text|json]`)#
- `nanobot-senior-pm/scripts/risk_matrix_analyzer.py` — Risk matrix analyzer (`<data_file> [--format text|json]`)#

## Skill Reference#

> `nanobot-senior-pm/SKILL.md`#
