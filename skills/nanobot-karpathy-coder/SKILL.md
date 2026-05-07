# Karpathy Coder — Active Coding Discipline

Derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls. This is **not just guidelines** — it ships Python tools that detect violations, a review agent, a slash command, and a pre-commit hook.

> "The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should."
> "They really like to overcomplicate code and APIs, bloat abstractions, don't clean up dead code... implement a bloated construction over 1000 lines when 100 would do."
> "LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go."
> — Andrej Karpathy

## The four principles

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

- State assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

**The test:** Would a senior engineer say this is overcomplicated? If yes, simplify.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

- No drive-by refactors of unrelated code.
- No style changes outside changed lines.
- No "while I'm here" scope creep.
- If a function wasn't changed, don't rename its variables.
- Diff should be minimal and purposeful.

**The test:** Could someone guess the change from the diff alone? If no, scope-creep likely happened.

### 4. Goal-Driven Execution

**Define success before coding. Verify it happened.**

- State what "done" looks like before writing code.
- Define concrete success criteria, not "should work."
- After coding, verify each criterion explicitly.
- If you can't verify it, the criterion is vague — rewrite it.
- Loop until ALL criteria pass, not "most of them."

**The test:** Can you demonstrate success with a command? If no, the goals are too vague.

## Quick start

```bash
# Install as Nanobot plugin
/plugin marketplace add nanobot-superpowers
/plugin install karpathy-coder@nanobot-superpowers

# Run before committing
/nanobot-karpathy-check

# Or use individual tools from the shell
python scripts/complexity_checker.py src/ --threshold strict
python scripts/diff_surgeon.py --diff HEAD~1..HEAD
echo "I'll just export all user data" | python scripts/assumption_linter.py -
python scripts/goal_verifier.py plan.md
```

## What's in the box

| Piece | Count | Detail |
|---|---|---|
| SKILL.md | 1 | The 4 principles with `context: fork` for skill chaining |
| Python tools | 4 | `complexity_checker`, `diff_surgeon`, `assumption_linter`, `goal_verifier` — all stdlib-only |
| Sub-agent | 1 | `karpathy-reviewer` — runs all 4 principles against a diff |
| Slash command | 1 | `/nanobot-karpathy-check` — one-command pre-commit review |
| Pre-commit hook | 1 | `karpathy-gate.sh` — non-blocking awareness gate |
| Reference docs | 3 | Full Karpathy context, 10+ anti-pattern examples, 4-level enforcement guide |

## The tools

### complexity_checker.py (Principle #2)

Detects over-engineering: cyclomatic complexity, class density, nesting depth, function length, premature ABC/Protocol usage, import coupling.

```bash
python scripts/complexity_checker.py src/auth/ --threshold strict --json
# → score 72/100, 3 findings: nesting depth 6, function 'validate' 62 lines, 2 classes in 80 lines
```

Three threshold levels: `strict` (new code), `medium` (default), `relaxed` (legacy).

### diff_surgeon.py (Principle #3)

Analyzes a git diff and flags lines that don't trace to the stated goal: comment-only changes, whitespace noise, style drift (quote swaps), drive-by refactors, docstring additions to unchanged functions.

```bash
python scripts/diff_surgeon.py                    # staged changes
python scripts/diff_surgeon.py --diff HEAD~3..HEAD # last 3 commits
# → Noise ratio: 23% (NOISY), 7 comment-only changes, 2 quote-style swaps
```

### assumption_linter.py (Principle #1)

Reads a plan or proposal and flags hidden assumptions: "just" (hides complexity), "obviously" (unstated assumption), "should work" (hopeful, not verified), vague action verbs, unscoped user references, missing format specifications.

```bash
echo "I'll just add a function to export all user data" | python scripts/assumption_linter.py -
# → 3 findings: assumption-just, missing-format, scope-absolute
```

### goal_verifier.py (Principle #4)

Scores each step of a plan for verification quality (0-3 per step). Flags vague criteria ("should work"), checks for final end-to-end verification, and recommends concrete checks.

```bash
python scripts/goal_verifier.py implementation-plan.md --json
# → 6 steps, 8/18 (44%), WEAK — 3 steps have no verification
```

## Enforcement levels

1. **Passive** — install plugin, principles load as context (~60% compliance)
2. **Active review** — run `/nanobot-karpathy-check` before commits (~85%)
3. **Pre-commit hook** — wire `karpathy-gate.sh` via Husky (~95%)
4. **CI gate** — add tools to GitHub Actions PR checks (~99%)

See `references/enforcement-patterns.md` for setup instructions at each level.

## Cross-tool compatibility

The tools are pure Python stdlib. The principles work in any AGENTS.md-aware CLI (Codex, Cursor, Antigravity, OpenCode, Gemini CLI).

## Attribution

Derived from [Andrej Karpathy's X post](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls. The principles are Karpathy's observations; the tooling, enforcement patterns, and anti-pattern gallery are original.

## License

MIT.
