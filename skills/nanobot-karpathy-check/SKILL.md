# /nanobot-karpathy-check

Review your staged changes (or last commit) against Karpathy's 4 coding principles.

## Usage

```
/nanobot-karpathy-check                 # review staged changes
/nanobot-karpathy-check --last-commit   # review the most recent commit
```

## What it runs

1. **Principle #2 (Simplicity):** `scripts/complexity_checker.py` on all changed files — detects over-engineering, premature abstractions, deep nesting, long functions
2. **Principle #3 (Surgical):** `scripts/diff_surgeon.py` on the diff — detects comment-only changes, whitespace noise, style drift, drive-by refactors
3. **Principles #1 + #4 (Think + Goals):** The `nanobot-karpathy-reviewer` agent reads the diff and applies human-judgment checks — hidden assumptions, missing verification

## Output

A structured report with per-principle verdicts and specific line-level fix recommendations.

## When to run

- Before committing (catches noise and overcomplication early)
- After completing a feature (sanity check before PR)
- When you suspect the LLM overcoded something

## Sub-agent

Dispatches the `nanobot-karpathy-reviewer` agent. See `nanobot-karpathy-coder/SKILL.md`.

## Scripts

- `nanobot-karpathy-coder/scripts/complexity_checker.py`
- `nanobot-karpathy-coder/scripts/diff_surgeon.py`
- `nanobot-karpathy-coder/scripts/assumption_linter.py`
- `nanobot-karpathy-coder/scripts/goal_verifier.py`

## Skill Reference

→ `nanobot-karpathy-coder/SKILL.md`
