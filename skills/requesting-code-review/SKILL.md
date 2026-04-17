# Requesting Code Review

**Use when:** Completing tasks, implementing major features, or before delivery to verify work meets requirements.

**Core principle:** Review early, review often. Catch issues before they cascade.

---

## When to Request Review

**Mandatory:**
- After completing major feature
- Before delivery to user
- Before merge (if using git)

**Optional but valuable:**
- When stuck (fresh perspective)
- Before refactoring (baseline check)
- After fixing complex bug

## How to Request Review

### 1. Prepare the Work

Ensure:
- All tests passing
- Code is clean (no debug code, TODOs resolved)
- Changes are committed

### 2. Summarize for Reviewer

Provide:
- **What was implemented:** Brief description
- **What it should do:** Requirements or acceptance criteria
- **Key files changed:** List of files
- **How to test:** Steps to verify it works

### 3. Present for Review

```
Ready for review. Summary:

**Implemented:** [What was built]
**Should do:** [What it should accomplish]
**Files:** [List of changed files]
**Test:** [How to verify]

Please review for:
- Correctness (does it work as specified?)
- Code quality (is it clean, maintainable?)
- Edge cases (what's missing?)
```

## What to Look For (as reviewer)

When reviewing your own work or requesting review:

### Correctness
- Does it do what it's supposed to?
- Are there edge cases not handled?
- Does it break existing functionality?

### Quality
- Is the code clean and readable?
- Are there obvious simplifications?
- Is there repeated code that could be extracted?

### Completeness
- Are all requirements met?
- Are error cases handled?
- Is documentation updated?

## Acting on Feedback

- **Critical issues:** Fix immediately
- **Important issues:** Fix before proceeding
- **Minor issues:** Note for later
- **Reviewer wrong:** Push back with reasoning

## Integration with Other Skills

This skill pairs with:

- **verification-before-completion** — Verify before requesting review
- **receiving-code-review** — How to handle feedback
- **finishing-a-development-branch** — Finalize after review

## Remember

- Review early, not just at the end
- Be specific about what to review
- Accept feedback gracefully
- Push back when reviewer is wrong

## Red Flags

**Never:**
- Skip review because "it's simple"
- Ignore critical issues
- Proceed with unfixed important issues
- Argue with valid technical feedback

**If reviewer is wrong:**
- Push back with technical reasoning
- Show code/tests that prove it works
- Request clarification