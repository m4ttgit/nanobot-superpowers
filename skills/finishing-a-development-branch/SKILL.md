# Finishing a Development Branch

**Use when:** Completing feature work — all tasks done, ready to finalize before merge or delivery.

**Core principle:** Verify everything works, present options, let the user choose. Never merge without explicit consent.

---

## When to Use

**Use when:**
- All implementation tasks are complete
- Tests are passing
- Ready to finalize work for review/merge
- About to report "done" to the user

**Don't use when:**
- Work is still in progress
- Tests are failing
- Unresolved blockers exist

## The Process

### Phase 1: Verification

Before anything else, verify the work is actually complete:

1. **Run full test suite** — All tests passing?
2. **Check for lint/style issues** — Code is clean?
3. **Verify no debug code** — No console.log, print statements, TODO comments left behind?
4. **Check for unintended changes** — git status shows only expected files?

### Phase 2: Present Options

Present the user with choices for how to finalize:

**Option A: Clean Commit**
```
Ready to commit. Summary of changes:
- [List of changes]
Shall I commit with this message?
```

**Option B: Pull Request**
```
Ready to create PR. Options:
1. Squash and merge (clean history)
2. Merge commit (preserves all commits)
3. Rebase and merge (linear history)
Which do you prefer?
```

**Option C: Direct Delivery**
```
All done! Here's what was implemented:
- [Summary]
Ready for your review.
```

### Phase 3: Execute Choice

After user selects:
1. Execute the chosen action
2. Report the result
3. Confirm completion

## Integration with Other Skills

This skill is the natural endpoint for:

- **executing-plans** — After all tasks complete
- **subagent-driven-development** — After all subagent tasks done
- **test-driven-development** — After implementation is verified

## Remember

- Verify before presenting options
- Never assume — present choices
- User controls the final decision
- Report clearly what was done

## Red Flags

- **Claiming "done" without running tests** — Always verify
- **Skipping review** — Let user see what changed
- **Auto-merging** — Never merge without explicit consent
- **Leaving debug code** — Clean before finalizing
- **Unresolved TODOs** — Either fix or document them