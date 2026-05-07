# /nanobot-user-story

Generate structured user stories with acceptance criteria, story points, and sprint capacity planning.

## Usage

```
/nanobot-user-story generate                                         Generate user stories (interactive)
/nanobot-user-story sprint <capacity>                                Plan sprint with story point capacity
```

## Input Format

Interactive mode prompts for feature context. For sprint planning, provide capacity as story points:

```
/nanobot-user-story generate
> Feature: User authentication
> Persona: Engineering manager
> Epic: Platform Security

/nanobot-user-story sprint 21
> Stories are ranked by priority and fit within 21-point capacity
```

## Examples

```
/nanobot-user-story generate
/nanobot-user-story sprint 34
/nanobot-user-story sprint 21
```

## Scripts

- `nanobot-agile-product-owner/scripts/user_story_generator.py` — User story generator (positional args: `sprint <capacity>`)

## Skill Reference

> `nanobot-agile-product-owner/SKILL.md`
