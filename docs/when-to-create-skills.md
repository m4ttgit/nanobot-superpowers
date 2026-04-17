# When to Create a Skill

This guide helps you decide whether to create a new skill or handle a task directly.

## The Core Question

> Will creating a skill save time and improve consistency across multiple sessions?

If yes → Create a skill. If no → Just do the task.

---

## ✅ Create a Skill When:

### 1. Repeated Process
You follow the same steps repeatedly across different tasks.

**Examples:**
- Always debugging with the same methodology
- Starting every feature with a design phase
- Verifying work the same way every time

**Why:** Skills enforce discipline. Without them, steps get skipped under time pressure.

### 2. Complex Workflow
Multiple steps that must happen in a specific order with decision points.

**Examples:**
- TDD cycle (write test → watch fail → write code → verify pass)
- Brainstorming gate (explore → design → get approval → implement)
- Code review process (verify → evaluate → respond → implement)

**Why:** Complex workflows are hard to remember. A skill provides a checklist.

### 3. Preventing Failure Modes
You've seen the same mistake happen multiple times.

**Examples:**
- Jumping to solutions without understanding the problem
- Claiming "done" without running tests
- Skipping the design phase for "simple" features

**Why:** Skills create friction that prevents habitual mistakes.

### 4. Teaching Behavior
You want nanobot to behave a certain way, not just complete a task.

**Examples:**
- "Question assumptions before implementing"
- "Verify before claiming completion"
- "Explore before coding"

**Why:** Skills teach methodology, not just steps.

### 5. High-Cost Failures
The cost of getting it wrong is high.

**Examples:**
- Security vulnerabilities
- Data loss
- Breaking production

**Why:** Skills add verification gates for critical paths.

---

## ❌ Don't Create a Skill When:

### 1. One-off Tasks
The task will only happen once.

**Examples:**
- "Migrate this specific database"
- "Fix this one bug"
- "Generate this one report"

**Why:** The overhead of creating a skill outweighs the benefit.

### 2. Rapidly Changing
The process or technology will change frequently.

**Examples:**
- Technology-specific commands that will be obsolete
- Workflows tied to a specific project's current state
- Steps that depend on external APIs

**Why:** Skills become stale and misleading.

### 3. Simple Commands
The task is just "do X" with no methodology.

**Examples:**
- "Restart the service"
- "Check the logs"
- "Deploy to production"

**Why:** No process to encode. Just execute.

### 4. Over-Engineering
Creating a skill for the sake of it.

**Signs:**
- The "skill" is just "do the task"
- No real decision-making or steps
- No failure mode being prevented

**Why:** Adds complexity without value.

---

## The Decision Matrix

| Factor | Create Skill | Don't Create |
|--------|-------------|--------------|
| Frequency | Multiple times | One-off |
| Complexity | Multi-step with decisions | Single action |
| Failure cost | High | Low |
| Consistency needed | Yes | No |
| Methodology matters | Yes | No |

**Create a skill if you answer "yes" to 3+ of these.**

---

## Signs You Need a Skill (But Don't Have One)

Watch for these patterns:

1. **Same mistake twice** — "I keep forgetting to verify before claiming done"
2. **Inconsistent outcomes** — "Sometimes I brainstorm, sometimes I just code"
3. **Skipped steps** — "I know I should do X, but I skip it when busy"
4. **Reinventing the wheel** — "I figure out the same approach each time"
5. **Quality variance** — "My debugging is thorough sometimes, sloppy others"

---

## When Existing Skills Aren't Enough

Sometimes existing skills don't cover your use case:

1. **Gap in coverage** — No skill for a specific workflow you use
2. **Domain-specific adaptation** — A skill exists but needs tailoring to your context
3. **New methodology** — You've developed a process that works well for you

**Before creating:** Check if the gap can be filled by:
- Combining existing skills
- Adapting an existing skill slightly
- Extending a skill with additional steps

**If not:** Create a new skill following the [writing-skills](../skills/writing-skills/SKILL.md) guide.

---

## Summary

**Create a skill when:**
- The process will be used repeatedly
- Multiple steps with decision points
- Failure would be costly
- Consistency matters
- You're teaching behavior, not just tasks

**Don't create when:**
- One-off task
- Simple command
- Rapidly changing
- No real methodology to encode

**The test:** Would creating this skill save time and improve outcomes across multiple sessions? If yes, create it.