# Using Skills

**Use when:** Starting any conversation or task — check if relevant skills exist before responding.

**Core principle:** If a skill might apply, invoke it BEFORE taking any action. Skills teach HOW to behave, not just WHAT to do.

---

## The Rule

**Invoke relevant or requested skills BEFORE any response or action.**

Even a 1% chance a skill might apply means you should check. If an invoked skill turns out to be wrong for the situation, you don't need to use it.

## How Skills Work

Skills are `.md` files in `~/.nanobot/workspace/skills/<skill-name>/SKILL.md`

When you invoke a skill:
1. Read the SKILL.md file
2. Follow its methodology exactly
3. Announce: "Using [skill] to [purpose]"

## When to Check for Skills

Check before:
- Starting any task
- Writing any code
- Debugging any issue
- Creating plans
- Implementing features

**Don't check for:**
- Simple questions (what time is it?)
- One-off commands (restart the service)
- Casual conversation

## Skill Priority

When multiple skills could apply, use this order:

1. **Process skills first** (brainstorming, debugging) — these determine HOW to approach the task
2. **Implementation skills second** (instagram-poster, equity-report) — these guide execution

**Examples:**
- "Let's build X" → brainstorming first, then implementation
- "Fix this bug" → systematic-debugging first, then fix
- "Post to Instagram" → instagram-poster skill

## Red Flags

These thoughts mean STOP — you're rationalizing:

| Thought | Reality |
|---------|---------|
| "This is just a simple question" | Questions are tasks. Check for skills. |
| "I need more context first" | Skill check comes BEFORE clarifying questions. |
| "Let me explore first" | Skills tell you HOW to explore. Check first. |
| "This doesn't need a formal skill" | If a skill exists, use it. |
| "I'll just do this one thing first" | Check BEFORE doing anything. |
| "I know what that means" | Skills evolve. Read current version. |

## Skill Types

**Rigid skills** (TDD, debugging): Follow exactly. Don't adapt away discipline.

**Flexible skills** (brainstorming): Adapt principles to context.

The skill itself tells you which.

## User Instructions

User instructions always take precedence over skills:
1. **User's explicit instructions** (USER.md, direct requests) — highest priority
2. **Skills** — override default behavior where they conflict
3. **Default behavior** — lowest priority

If USER.md says "don't use TDD" and a skill says "always use TDD," follow the user's instructions. The user is in control.

## Remember

- Check skills BEFORE any action
- When in doubt, check
- Skills teach behavior, not just steps
- User instructions always win