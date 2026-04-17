# Systematic Debugging

**Use when:** Encountering any bug, test failure, or unexpected behavior — before proposing fixes.

**Core principle:** Always find root cause before attempting fixes. Symptom fixes are failure.

---

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1, you cannot propose fixes.

---

## When to Use

Use for ANY technical issue:
- Test failures
- Bugs in production
- Unexpected behavior
- Performance problems
- Build failures
- Integration issues

**Use this ESPECIALLY when:**
- Under time pressure (emergencies make guessing tempting)
- "Just one quick fix" seems obvious
- You've already tried multiple fixes
- Previous fix didn't work
- You don't fully understand the issue

**Don't skip when:**
- Issue seems simple (simple bugs have root causes too)
- You're in a hurry (rushing guarantees rework)
- Manager wants it fixed NOW (systematic is faster than thrashing)

---

## The Four Phases

### Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. **Read Error Messages Carefully** — Don't skip past errors. They often contain the exact solution. Read stack traces completely. Note line numbers, file paths, error codes.

2. **Reproduce Consistently** — Can you trigger it reliably? What are the exact steps? Does it happen every time? If not reproducible → gather more data, don't guess.

3. **Check Recent Changes** — What changed that could cause this? Git diff, recent commits, new dependencies, config changes, environmental differences.

4. **Trace Data Flow** — Where does bad value originate? What called this with bad value? Keep tracing up until you find the source. Fix at source, not at symptom.

5. **Gather Evidence in Multi-Component Systems** — For each component boundary: log what enters, log what exits, verify environment/config propagation, check state at each layer. Run once to gather evidence showing WHERE it breaks. THEN analyze evidence to identify failing component.

### Phase 2: Pattern Analysis

**Find the pattern before fixing:**

1. **Find Working Examples** — Locate similar working code. What works that's similar to what's broken?

2. **Compare Against References** — If implementing a pattern, read reference implementation COMPLETELY. Don't skim — read every line.

3. **Identify Differences** — What's different between working and broken? List every difference, however small. Don't assume "that can't matter."

4. **Understand Dependencies** — What other components does this need? What settings, config, environment?

### Phase 3: Hypothesis and Testing

**Scientific method:**

1. **Form Single Hypothesis** — State clearly: "I think X is the root cause because Y." Write it down. Be specific, not vague.

2. **Test Minimally** — Make the SMALLEST possible change to test hypothesis. One variable at a time. Don't fix multiple things at once.

3. **Verify Before Continuing** — Did it work? Yes → Phase 4. Didn't work? Form NEW hypothesis. DON'T add more fixes on top.

4. **When You Don't Know** — Say "I don't understand X." Don't pretend to know. Ask for help. Research more.

### Phase 4: Implementation

**Fix the root cause, not the symptom:**

1. **Create Failing Test Case** — Simplest possible reproduction. Automated test if possible. One-off test script if no framework. MUST have before fixing.

2. **Implement Single Fix** — Address the root cause identified. ONE change at a time. No "while I'm here" improvements. No bundled refactoring.

3. **Verify Fix** — Test passes now? No other tests broken? Issue actually resolved?

4. **If Fix Doesn't Work** — STOP. Count: How many fixes have you tried?
   - If < 3: Return to Phase 1, re-analyze with new information
   - **If ≥ 3: STOP and question the architecture**

5. **If 3+ Fixes Failed: Question Architecture** — Pattern indicating architectural problem: each fix reveals new shared state/coupling in different place, fixes require "massive refactoring," each fix creates new symptoms elsewhere. STOP and question fundamentals. Discuss with your human partner before attempting more fixes.

---

## Red Flags — STOP and Follow Process

If you catch yourself thinking:
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "Add multiple changes, run tests"
- "Skip the test, I'll manually verify"
- "It's probably X, let me fix that"
- "I don't fully understand but this might work"
- **"One more fix attempt" (when already tried 2+)**
- **Each fix reveals new problem in different place**

**ALL of these mean: STOP. Return to Phase 1.**

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Issue is simple, don't need process" | Simple issues have root causes too. Process is fast for simple bugs. |
| "Emergency, no time for process" | Systematic debugging is FASTER than guess-and-check thrashing. |
| "Just try this first, then investigate" | First fix sets the pattern. Do it right from the start. |
| "I'll write test after confirming fix works" | Untested fixes don't stick. Test first proves it. |
| "Multiple fixes at once saves time" | Can't isolate what worked. Causes new bugs. |
| "Reference too long, I'll adapt the pattern" | Partial understanding guarantees bugs. Read it completely. |
| "I see the problem, let me fix it" | Seeing symptoms ≠ understanding root cause. |
| "One more fix attempt" (after 2+ failures) | 3+ failures = architectural problem. Question pattern, don't fix again. |

---

## Quick Reference

| Phase | Key Activities | Success Criteria |
|-------|---------------|------------------|
| **1. Root Cause** | Read errors, reproduce, check changes, gather evidence | Understand WHAT and WHY |
| **2. Pattern** | Find working examples, compare | Identify differences |
| **3. Hypothesis** | Form theory, test minimally | Confirmed or new hypothesis |
| **4. Implementation** | Create test, fix, verify | Bug resolved, tests pass |

---

## When Process Reveals "No Root Cause"

If systematic investigation reveals issue is truly environmental, timing-dependent, or external:
1. You've completed the process
2. Document what you investigated
3. Implement appropriate handling (retry, timeout, error message)
4. Add monitoring/logging for future investigation

**But:** 95% of "no root cause" cases are incomplete investigation.