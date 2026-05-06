### Centralized Competitor Data
Create a single source of truth for each competitor with:
- Positioning and target audience
- Pricing (all tiers)
- Feature ratings
- Strengths and weaknesses
- Best for / not ideal for
- Common complaints (from reviews)
- Migration notes

**For data structure and examples**: See [templates.md](templates.md)

---

## Data Consumption

- Use the central data to populate all pages consistently
- Update in one place; propagate to all pages
- Version history to track changes over time

---

## Data Model (Example)
```yaml
competitor: AcmeX
positioning: 'Leading solution for small teams'
pricing:
  free: true
  tiers:
    - name: Starter
      price: 9
      features:
        - feature-a
        - feature-b
    - name: Pro
      price: 29
      features:
        - feature-a
        - feature-b
        - feature-c
strengths:
- Easy onboarding
- Flexible pricing
weaknesses:
- Limited enterprise integrations
migration_notes: 'Migration steps documented in Migration Guide'
```

---

## Templates

- Use templates for each page section to ensure consistency across pages
- Keep data-driven sections up to date
