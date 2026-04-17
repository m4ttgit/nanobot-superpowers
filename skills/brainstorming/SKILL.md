# Brainstorming

**Use when:** Starting any creative work — new features, designs, components, or behavior changes.

**Core principle:** Explore before implementing. Always understand what you're building before touching code.

---

## The Hard Gate

```
DO NOT write code, scaffold projects, or take implementation actions
until you have presented a design and the user has approved it.
```

This applies to EVERY project regardless of perceived simplicity.

---

## The Process

### 1. Explore Context
Check existing files, docs, recent changes. Understand the current state.

### 2. Ask Clarifying Questions
One at a time. Understand:
- **Purpose** — What problem does this solve?
- **Constraints** — What's fixed vs. flexible?
- **Success criteria** — How do we know it's done?

### 3. Propose 2-3 Approaches
With trade-offs. Lead with your recommendation and explain why.

### 4. Present Design
Scale sections to complexity. Get approval after each section before moving on.

### 5. Write Design Doc
Save to `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md` (or user-preferred location).

### 6. Spec Self-Review
Check for:
- Placeholders ("TBD", "TODO", incomplete sections)
- Internal contradictions
- Scope creep or ambiguity

Fix inline. No re-review needed — just fix and move on.

### 7. User Reviews Spec
> "Spec written. Please review and let me know if you want changes before we start the implementation plan."

Wait for approval. If changes requested, make them and re-run.

### 8. Transition to Implementation
Invoke the **writing-plans** skill to create the implementation plan.

---

## Key Principles

- **One question at a time** — Don't overwhelm
- **Multiple choice preferred** — Easier to answer than open-ended
- **YAGNI ruthlessly** — Remove unnecessary features
- **Explore alternatives** — Always propose 2-3 approaches
- **Incremental validation** — Get approval before moving on
- **Be flexible** — Go back and clarify when something doesn't make sense

---

## Anti-Pattern: "This Is Too Simple"

Every project goes through this process. A todo list, a single utility, a config change — all of them. "Simple" projects are where unexamined assumptions cause the most wasted work.

The design can be short (a few sentences for truly simple projects), but you MUST present it and get approval.

---

## Design for Isolation

Break the system into smaller units that each have one clear purpose. For each unit, you should be able to answer:
- What does it do?
- How do you use it?
- What does it depend on?

Can someone understand what a unit does without reading its internals? Can you change the internals without breaking consumers? If not, the boundaries need work.