# Writing Skills

**Use when:** Creating a new skill for nanobot — either from scratch or porting from another framework.

**Core principle:** Skills should be scannable in 30 seconds, actionable in detail, and teach nanobot HOW to behave, not just WHAT to do.

---

## When to Create a Skill

Create a skill when:
- You find yourself following the same process repeatedly
- A methodology keeps getting ignored or forgotten
- A complex workflow needs consistent execution
- You want to teach nanobot a new capability

**Don't create a skill for:**
- One-off tasks
- Simple commands (just do it)
- Things that change frequently

## Skill Structure

Every nanobot skill needs:

```markdown
# Skill Name

**Use when:** [One sentence — when does this skill trigger?]

**Core principle:** [One sentence — the core philosophy]

---

## The Process

[Detailed steps...]

## Key Patterns

[Examples with good/bad comparisons]

## Red Flags

- [Anti-patterns that mean STOP]
```

## Required Elements

### 1. "Use when" Header
At the very top. This is how nanobot decides whether to use the skill.

**Good:** "Use when: Starting any creative work — new features, designs, or behavior changes."
**Bad:** "Use when: Working on things" (too vague)

### 2. Core Principle
One sentence that captures the essence. This is what nanobot should remember when the skill isn't loaded.

### 3. Actionable Steps
Not theory — concrete actions. Each step should be something nanobot can DO.

**Good:**
1. Read the plan file
2. Review critically — identify any concerns
3. If concerns: raise them before starting

**Bad:**
1. Be thorough
2. Think carefully
3. Do a good job

### 4. Red Flags Section
What should make nanobot STOP? This prevents the skill from being followed blindly.

## Optional Elements

### YAML Frontmatter
Nanobot ignores it, but it's fine to keep for compatibility:
```yaml
---
name: skill-name
description: Use when...
---
```

### Supporting Files
```
skills/
└── my-skill/
    ├── SKILL.md
    ├── script.py      # Optional helper
    └── config.json    # Optional config
```

### Examples
Real examples showing the skill in action. Include both good and bad responses.

### Flowcharts
Mermaid diagrams showing decision trees (optional but helpful).

## Porting from Other Frameworks

When porting from OpenCode/superpowers:

| OpenCode | Nanobot |
|----------|---------|
| YAML frontmatter | Optional (ignored) |
| `Skill` tool | Built-in skill loading |
| CLAUDE.md rules | USER.md / AGENTS.md |
| Subagent dispatch | Spawn tool |

### Porting Steps

1. **Extract core methodology** — What does this skill teach?
2. **Identify "Use when"** — When should it trigger?
3. **Adapt examples** — Python/shell instead of TypeScript/Node
4. **Remove framework-specific** — Tool names, subagent patterns
5. **Keep the discipline** — Don't water down the methodology

### Common Pitfalls

- **Watering down:** Removing the "annoying" parts that make the skill effective
- **Too verbose:** Skills should be scannable — put deep detail in docs/
- **Missing red flags:** Without them, skills get followed blindly
- **No examples:** Abstract principles are hard to apply

## Quality Checklist

Before finishing a skill:

- [ ] "Use when" header at top
- [ ] Core principle stated
- [ ] Actionable steps (not just theory)
- [ ] Good/bad examples where helpful
- [ ] Red flags section
- [ ] No placeholder text (TODO, TBD, etc.)
- [ ] Tested with nanobot

## Example: Good vs Bad

**Bad skill:**
```markdown
# Debugging

When you find a bug, be thorough and fix it properly.

1. Look at the error
2. Figure out what went wrong
3. Fix it
4. Test the fix
```

**Good skill:**
```markdown
# Systematic Debugging

**Use when:** Encountering any bug, test failure, or unexpected behavior.

**Core principle:** Always find root cause before attempting fixes. Symptom fixes are failure.

---

## The Process

### Phase 1: Root Cause Investigation
1. **Reproduce** — Can you make it happen again?
2. **Isolate** — What specifically causes it?
3. **Hypothesize** — What's the underlying issue?

### Phase 2: Pattern Analysis
- Is this a one-off or systemic?
- Does it affect other parts?

### Phase 3: Hypothesis & Testing
1. Propose root cause
2. Test the hypothesis
3. Verify fix works

### Phase 4: Implementation
- Fix the root cause (not just symptoms)
- Add regression test

## Red Flags

- **Jumping to solutions** — "Let me try X" without understanding why
- **Fixing symptoms** — Patching the error without finding why it happened
- **Assuming cause** — "It's probably X" without evidence
```

## Testing Your Skill

1. **Trigger test:** Send a message that should activate the skill
2. **Follow test:** Verify nanobot follows the methodology
3. **Edge case test:** Try situations where the skill might not apply
4. **Red flag test:** Verify nanobot stops when it should

## Skill Location

Skills go in: `~/.nanobot/workspace/skills/<skill-name>/SKILL.md`

For this repo: `skills/<skill-name>/SKILL.md`