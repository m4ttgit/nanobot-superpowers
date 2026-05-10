# /nanobot-persona#

Generate structured user personas with demographics, goals, pain points, and behavioral patterns.#

## Usage#

```
/nanobot-persona generate                                            Generate persona (interactive)#
/nanobot-persona generate json                                       Generate persona as JSON#
```

## Input Format#

Interactive mode prompts for product context. Alternatively, provide context inline:#

```
/nanobot-persona generate#
> Product: B2B project management tool#
> Target: Engineering managers at mid-size companies#
> Key problem: Cross-team visibility#
```

## Examples#

```
/nanobot-persona generate#
/nanobot-persona generate json#
/nanobot-persona generate json > persona-eng-manager.json#
```

## Scripts#

- `nanobot-ux-researcher-designer/scripts/persona_generator.py` — Persona generator (positional `json` arg for JSON output)#

## Skill Reference#

> `nanobot-ux-researcher-designer/SKILL.md`#
