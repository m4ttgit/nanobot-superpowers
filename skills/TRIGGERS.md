# Skill Triggers

Quick reference for when skills activate. Use explicit invocation for complex process skills. Utility skills auto-trigger on domain keywords.

## Explicit Invocation (Complex Process Skills)

Invoke explicitly — these require reading the full skill:

| Trigger Phrase | Skill |
|----------------|-------|
| "Use brainstorming" / "Let's brainstorm" / "Design this" | brainstorming |
| "Use TDD" / "Test-driven" / "Write tests first" | test-driven-development |
| "Write a plan" / "Create a plan" / "Plan this" | writing-plans |
| "Execute the plan" / "Follow the plan" | executing-plans |
| "Finish up" / "Ready to merge" / "Complete this branch" | finishing-a-development-branch |
| "Create a skill" / "Port a skill" / "Write a skill" | writing-skills |
| "Request review" / "Ready for review" | requesting-code-review |
| "Received feedback" / "Review feedback" | receiving-code-review |

## Auto-Trigger (Utility Skills)

These activate on domain keywords — no explicit invocation needed:

| Keywords | Skill |
|----------|-------|
| instagram, post to IG, IG, carousel | instagram-poster |
| equity report, analyze stock, financial analysis, [stock symbol] | equity-report |
| debug, fix this bug, it's broken, error, not working | systematic-debugging |
| verify, test it, is it working, check if done | verification-before-completion |

## Skill Priority

When multiple skills could apply:

1. **Process skills first** (brainstorming, debugging) — determine HOW to approach
2. **Utility skills second** (instagram, equity-report) — guide specific execution

## Examples

**Explicit invocation:**
- "Use brainstorming to design a new dashboard"
- "Apply TDD to implement the login function"
- "Write a plan for migrating the database"

**Auto-trigger:**
- "Post this image to Instagram" → instagram-poster activates
- "Debug why the login is failing" → systematic-debugging activates
- "Tesla equity report" → equity-report activates

## Adding New Triggers

When creating a new skill, add it to this file with:
1. Trigger phrase (explicit) or keywords (auto)
2. Skill name
3. Brief description