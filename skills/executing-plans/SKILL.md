# Executing Plans

**Use when:** You have a written implementation plan to execute — step-by-step tasks with clear instructions.

**Core principle:** Load plan, review critically, execute all tasks, report when complete. Stop when blocked.

---

## When to Use

**Use when:**
- User provides a plan or spec with numbered steps
- You need to implement something with multiple tasks
- There's a checklist or TODO list to work through

**Don't use when:**
- No plan exists — use brainstorming first
- Tasks are tightly coupled — use subagent-driven-development instead
- It's a one-off question or simple task

## The Process

### Step 1: Load and Review Plan

1. Read the plan file or instructions
2. Review critically — identify any questions or concerns
3. If concerns: Raise them before starting
4. If no concerns: Proceed to execution

**Questions to ask during review:**
- Are all steps clear? Any ambiguous instructions?
- Are dependencies properly ordered?
- Are there verification steps for each task?
- Any missing information or resources?

### Step 2: Execute Tasks

For each task in order:

1. **Announce:** "Executing Task N: [description]"
2. **Follow each step exactly** — plan has bite-sized steps
3. **Run verifications** as specified
4. **Mark complete** and move to next

### Step 3: Complete Development

After all tasks complete and verified:

1. Run full test suite
2. Verify no regressions
3. Report completion with summary

## When to Stop and Ask for Help

**STOP executing immediately when:**
- Hit a blocker (missing dependency, test fails, instruction unclear)
- Plan has critical gaps preventing starting
- You don't understand an instruction
- Verification fails repeatedly
- Something feels wrong — trust that instinct

**Ask for clarification rather than guessing.**

## When to Revisit Earlier Steps

**Return to Review (Step 1) when:**
- User updates the plan based on your feedback
- Fundamental approach needs rethinking
- New information changes the context

**Don't force through blockers** — stop and ask.

## Integration with Other Skills

This skill works best with:

- **writing-plans** — Creates the plan this skill executes
- **verification-before-completion** — Use before claiming tasks are done
- **systematic-debugging** — Use when hitting blockers

## Remember

- Review plan critically first
- Follow plan steps exactly
- Don't skip verifications
- Stop when blocked, don't guess
- Report progress as you go

## Red Flags

- **Starting without reviewing** — "I'll just follow the steps"
- **Skipping verification** — "This looks right, moving on"
- **Forcing through blockers** — "I'll figure it out"
- **Skipping tasks** — "This one isn't needed"
- **Making assumptions** — "I think they meant X"