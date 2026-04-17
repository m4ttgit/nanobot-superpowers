# nanobot-superpowers

A collection of **process skills** for [nanobot](https://github.com/nanobot-dev/nanobot) — the AI assistant that runs on your server.

These skills are adapted from [superpowers](https://github.com/obra/superpowers) by [obra](https://github.com/obra) (originally for OpenCode) and ported to work with nanobot's skill system.

## What Are Skills?

Skills are `.md` files that teach nanobot how to behave in specific situations. When you install a skill, nanobot reads it and follows its guidance automatically.

## Included Skills (13 total)

| Skill | Ported | Why |
|-------|--------|-----|
| **brainstorming** | ✅ Yes | Core creative process — essential for any new work |
| **systematic-debugging** | ✅ Yes | Core quality process — essential for any bug fix |
| **verification-before-completion** | ✅ Yes | Core discipline — prevents false "done" claims |
| **test-driven-development** | ✅ Yes | Core implementation process — ensures correctness |
| **writing-plans** | ✅ Yes | Core planning process — enables structured execution |
| **writing-skills** | ✅ Yes | Meta-skill — enables creating new skills |
| **executing-plans** | ✅ Yes | Complements writing-plans — executes what was planned |
| **finishing-a-development-branch** | ✅ Yes | Completes the workflow — verifies and presents options |
| **using-superpowers** | ✅ Yes | Meta-skill — ensures skills are invoked correctly |
| **receiving-code-review** | ✅ Yes | Quality gate — handles feedback rigorously |
| **requesting-code-review** | ✅ Yes | Quality gate — requests review before completion |
| **instagram-poster** | ✅ Yes | Utility skill — posts images to Instagram |
| **equity-report** | ✅ Yes | Utility skill — generates equity research reports |

### Not Ported (3 skills)

| Skill | Reason Not Ported |
|-------|-------------------|
| **dispatching-parallel-agents** | Requires subagent support that nanobot doesn't have. The `spawn` tool exists but parallel dispatch with isolated context isn't the same pattern. |
| **subagent-driven-development** | Requires sophisticated subagent orchestration with two-stage review loops. Too tightly coupled to OpenCode's Task system. |
| **using-git-worktrees** | Git worktrees are a specific git workflow. Porting would require adapting to nanobot's execution model, and the core principle (isolated workspace) is already covered by executing-plans. |

## Skill Triggers

Skills activate in two ways:

### Explicit Invocation (Complex Process Skills)
Invoke explicitly — these require reading the full skill:

| Trigger | Skill |
|---------|-------|
| "Use brainstorming" / "Design this" | brainstorming |
| "Use TDD" / "Write tests first" | test-driven-development |
| "Write a plan" / "Create a plan" | writing-plans |
| "Execute the plan" | executing-plans |
| "Finish up" / "Ready to merge" | finishing-a-development-branch |
| "Create a skill" / "Port a skill" | writing-skills |
| "Request review" | requesting-code-review |
| "Received feedback" | receiving-code-review |

### Auto-Trigger (Utility Skills)
These activate on domain keywords automatically:

| Keywords | Skill |
|----------|-------|
| instagram, post to IG, IG, carousel | instagram-poster |
| equity report, analyze stock, [symbol] | equity-report |
| debug, fix this bug, error, not working | systematic-debugging |
| verify, test it, is it working | verification-before-completion |

See [skills/TRIGGERS.md](skills/TRIGGERS.md) for full trigger list.

## Quick Start

### Option 1: Copy Individual Skills

```bash
# Copy a skill to your nanobot skills directory
cp -r skills/brainstorming ~/.nanobot/workspace/skills/

# Restart nanobot or wait for it to reload
```

### Option 2: Clone Into Skills Directory

```bash
git clone https://github.com/m4ttgit/nanobot-superpowers.git \
  ~/.nanobot/workspace/skills/superpowers
```

### Option 3: Sync from Google Drive

If you use rclone with Google Drive:
```bash
rclone copy your_remote:nanobot_backup/skills/ \
  ~/.nanobot/workspace/skills/
```

## Skill Descriptions

### brainstorming
**Use when:** Starting any creative work — new features, designs, components, or behavior changes.

**Core principle:** Explore before implementing. Always understand what you're building before touching code.

The hard gate: Do NOT write code or take implementation actions until you have presented a design and the user has approved it.

### systematic-debugging
**Use when:** Encountering any bug, test failure, or unexpected behavior — before proposing fixes.

**Core principle:** Always find root cause before attempting fixes. Symptom fixes are failure.

Four-phase process: Root Cause Investigation → Pattern Analysis → Hypothesis & Testing → Implementation.

### verification-before-completion
**Use when:** About to claim work is complete, fixed, or passing — before committing or reporting success.

**Core principle:** Evidence before claims, always.

The iron law: No completion claims without fresh verification evidence. Run the command. Read the output. THEN claim the result.

### test-driven-development
**Use when:** Implementing any feature or bugfix — before writing implementation code.

**Core principle:** Write the test first. Watch it fail. Write minimal code to pass.

Red-Green-Refactor cycle: RED (write failing test) → GREEN (minimal code) → REFACTOR (clean up) → repeat.

### writing-plans
**Use when:** You have a spec or requirements for a multi-step task — before touching code.

**Core principle:** Write comprehensive plans assuming the engineer has zero context. Document everything they need to know.

Bite-sized tasks: Each step is one action (2-5 minutes). No placeholders. Exact file paths, complete code, exact commands.

### writing-skills
**Use when:** Creating a new skill for nanobot — either from scratch or porting from another framework.

**Core principle:** Skills should be scannable in 30 seconds, actionable in detail, and teach nanobot HOW to behave, not just WHAT to do.

### executing-plans
**Use when:** You have a written implementation plan to execute — step-by-step tasks with clear instructions.

**Core principle:** Load plan, review critically, execute all tasks, report when complete. Stop when blocked.

### finishing-a-development-branch
**Use when:** Completing feature work — all tasks done, ready to finalize before merge or delivery.

**Core principle:** Verify everything works, present options, let the user choose. Never merge without explicit consent.

### using-superpowers
**Use when:** Starting any conversation or task — check if relevant skills exist before responding.

**Core principle:** If a skill might apply, invoke it BEFORE taking any action. Skills teach HOW to behave, not just WHAT to do.

### receiving-code-review
**Use when:** Receiving code review feedback — before implementing suggestions, especially if feedback seems unclear or questionable.

**Core principle:** Verify before implementing. Ask before assuming. Technical correctness over social performance.

### requesting-code-review
**Use when:** Completing tasks, implementing major features, or before delivery to verify work meets requirements.

**Core principle:** Review early, review often. Catch issues before they cascade.

## Project Structure

```
nanobot-superpowers/
├── README.md
├── INSTALL.md
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
├── docs/
│   └── adapting-skills.md
├── examples/
│   ├── brainstorming-example.md
│   ├── debugging-example.md
│   └── tdd-example.md
└── skills/
    ├── brainstorming/SKILL.md
    ├── systematic-debugging/SKILL.md
    ├── verification-before-completion/SKILL.md
    ├── test-driven-development/SKILL.md
    ├── writing-plans/SKILL.md
    ├── writing-skills/SKILL.md
    ├── executing-plans/SKILL.md
    ├── finishing-a-development-branch/SKILL.md
    ├── using-superpowers/SKILL.md
    ├── receiving-code-review/SKILL.md
    ├── requesting-code-review/SKILL.md
    ├── instagram-poster/SKILL.md
    ├── instagram-poster/post.py
    └── equity-report/SKILL.md
```

## Documentation

- [When to Create a Skill](docs/when-to-create-skills.md) — Decide if a skill is the right solution
- [Skill Activation Models](docs/skill-activation-models.md) — Choose how to activate skills (tiered hybrid, explicit, always-on)
- [Adapting Skills for Nanobot](docs/adapting-skills.md) — Port skills from other frameworks

## Adapting Skills for Nanobot

Nanobot skills are simpler than OpenCode plugins. Key differences:

1. **Format:** Plain Markdown (`.md`) files, no YAML frontmatter required
2. **Location:** `~/.nanobot/workspace/skills/<skill-name>/SKILL.md`
3. **No plugin system:** Just copy files into the skills directory
4. **Scripts optional:** Skills can be pure documentation, or include executable scripts

See [docs/adapting-skills.md](docs/adapting-skills.md) for full guidance on porting skills.

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE)

## Credits

- Original **superpowers** by [obra](https://github.com/obra/superpowers) (OpenCode)
- Ported to nanobot by [m4ttgit](https://github.com/m4ttgit)