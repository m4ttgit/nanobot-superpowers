# Skill Activation Models

This guide explains different ways to activate skills and helps you choose the best approach for your use case.

## Overview

Skills are only useful if they're invoked. This document covers three activation models with different tradeoffs:

| Model | Token Cost | Cognitive Load | Best For |
|-------|------------|----------------|----------|
| **Tiered Hybrid** | Low | Low | Most users |
| **Explicit Only** | Minimal | Medium | Power users |
| **Always Loaded** | High | Low | Simple, few skills |

---

## Model 1: Tiered Hybrid (Recommended)

**Philosophy:** Load skills only when relevant. Use system prompts for lightweight awareness, explicit triggers for complex skills, auto-triggers for utility skills.

### How It Works

**System Level (~10 tokens/message):**
Add to SOUL.md or AGENTS.md:
```
Before responding, briefly consider: could a skill help here? If yes, invoke it.
```

**Explicit Invocation (Complex Process Skills):**
Invoke when you explicitly ask:
- "Use brainstorming for this feature"
- "Apply TDD to this task"
- "Write a plan for this migration"

**Auto-Trigger (Utility Skills):**
Automatically activate on keywords:
- "instagram" → instagram-poster
- "debug" → systematic-debugging
- "equity report" → equity-report

### Token Cost
- System reminder: ~10 tokens/message
- Skill loaded only when invoked: ~200-500 tokens (one-time)

### Pros
- ✅ Low ongoing token cost
- ✅ Complex skills only load when needed
- ✅ Utility skills auto-activate for convenience
- ✅ System reminder creates awareness without overhead

### Cons
- ❌ Requires knowing when to invoke explicitly
- ❌ Some skills won't auto-trigger (need documentation)

### Setup

1. Add to SOUL.md:
```markdown
Before responding, briefly consider: could a skill help here? If yes, invoke it by reading the relevant SKILL.md from ~/.nanobot/workspace/skills/<skill-name>/.
```

2. Install skills:
```bash
git clone https://github.com/m4ttgit/nanobot-superpowers.git \
  ~/.nanobot/workspace/skills/superpowers
```

3. Reference [TRIGGERS.md](../skills/TRIGGERS.md) for invocation phrases.

### Best For
- Most users
- Multi-skill installations
- Token-conscious usage
- Balanced approach

---

## Model 2: Explicit Only

**Philosophy:** Only load skills when explicitly invoked. No auto-triggers, no system reminders.

### How It Works

You must explicitly invoke every skill:
- "Use the brainstorming skill"
- "Apply systematic-debugging to this issue"
- "Follow the TDD process"

### Token Cost
- ~0 tokens/message (until invoked)
- Skill loaded on invocation: ~200-500 tokens

### Pros
- ✅ Minimal token overhead
- ✅ Full control over when skills activate
- ✅ No unexpected behavior
- ✅ Simple to understand

### Cons
- ❌ Requires remembering to invoke skills
- ❌ Easy to forget for "simple" tasks
- ❌ No lightweight awareness prompting

### Setup

1. Install skills (same as above)
2. Always invoke explicitly when you want a skill used
3. No system prompt changes needed

### Best For
- Power users who know the skills well
- Single-skill usage
- Maximum token efficiency
- When you want full control

---

## Model 3: Always Loaded

**Philosophy:** Load all skills at session start. Always available, always active.

### How It Works

All skills are loaded into context at the start of every session.

### Token Cost
- **High:** ~500-2000 tokens per message (all skills loaded)
- Scales poorly with number of skills

### Pros
- ✅ Skills always available
- ✅ No need to remember to invoke
- ✅ Consistent behavior

### Cons
- ❌ High token cost per message
- ❌ Context window pressure
- ❌ Skills may conflict or confuse
- ❌ Wastes tokens on irrelevant skills

### Setup

1. Install skills
2. Add to SOUL.md:
```markdown
Load all skills from ~/.nanobot/workspace/skills/ at session start.
```

### Best For
- Very few skills (1-3)
- Simple, complementary skills
- When token cost is not a concern
- Standalone utility skills only

---

## Comparison Summary

| Aspect | Tiered Hybrid | Explicit Only | Always Loaded |
|--------|--------------|---------------|---------------|
| **Token efficiency** | Good | Best | Poor |
| **Ease of use** | Good | Medium | Best |
| **Consistency** | Good | Depends on user | Best |
| **Scalability** | Good | Good | Poor |
| **Setup complexity** | Low | Lowest | Low |
| **Skill count support** | Many | Many | Few (1-3) |

---

## Making Your Choice

### Choose Tiered Hybrid if:
- You have 5+ skills
- You want convenience without high token cost
- You're comfortable with explicit invocation for complex skills

### Choose Explicit Only if:
- You have few skills or use them rarely
- You want maximum token efficiency
- You don't mind remembering to invoke skills

### Choose Always Loaded if:
- You have 1-3 simple utility skills
- Token cost is not a concern
- You want zero friction for skill availability

---

## Hybrid Model Deep Dive

The recommended tiered hybrid model works in three tiers:

### Tier 1: System Reminder
```
Before responding, briefly consider: could a skill help here?
```
**Purpose:** Lightweight awareness. ~10 tokens. Creates the habit without overhead.

### Tier 2: Explicit Invocation
For complex process skills that require reading full methodology:
- brainstorming
- systematic-debugging
- test-driven-development
- writing-plans
- executing-plans
- finishing-a-development-branch
- writing-skills
- receiving-code-review
- requesting-code-review

**Invoke with:** "Use [skill name]" or "Apply [skill] to this"

### Tier 3: Auto-Trigger
For utility skills with clear domain keywords:
- instagram-poster → "instagram", "post to IG"
- equity-report → "equity report", "analyze [stock]"
- systematic-debugging → "debug", "fix this bug"

**Activate:** Automatically when keywords detected.

---

## Customizing the Hybrid Model

### Adjusting Triggers

Edit `skills/TRIGGERS.md` to add or modify triggers:

```markdown
## Auto-Trigger (Utility Skills)

| Keywords | Skill |
|----------|-------|
| mytool, run my custom script | my-custom-skill |
```

### Adding System Reminders

Edit SOUL.md to customize the reminder:

```markdown
Before responding, briefly consider: could a skill help here? If yes, invoke it.
```

### Disabling Auto-Triggers

If you prefer explicit-only, remove auto-trigger keywords from TRIGGERS.md and rely on explicit invocation only.

---

## Summary

| Your Situation | Recommended Model |
|----------------|-------------------|
| 5+ skills, balanced usage | Tiered Hybrid |
| Few skills, rare usage | Explicit Only |
| 1-3 utility skills only | Always Loaded |
| New to skills | Tiered Hybrid |
| Maximum token efficiency | Explicit Only |
| Maximum convenience | Always Loaded |

**Start with Tiered Hybrid.** It's the best balance for most users and can be simplified or extended based on your needs.