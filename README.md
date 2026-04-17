# nanobot-superpowers

A collection of **process skills** for [nanobot](https://github.com/nanobot-dev/nanobot) — the AI assistant that runs on your server.

These skills are adapted from [superpowers](https://github.com/obra/superpowers) by [obra](https://github.com/obra) (originally for OpenCode) and ported to work with nanobot's skill system.

## What Are Skills?

Skills are `.md` files that teach nanobot how to behave in specific situations. When you install a skill, nanobot reads it and follows its guidance automatically.

## Included Skills

| Skill | When to Use |
|-------|-------------|
| **brainstorming** | Starting any creative work — explore before implementing |
| **systematic-debugging** | Any bug or unexpected behavior — find root cause first |
| **verification-before-completion** | Before claiming work is done — verify with evidence |
| **test-driven-development** | Before writing code — test first, then implement |
| **writing-plans** | Before starting implementation — write the plan first |
| **instagram-poster** | Post images to Instagram via the Graph API |
| **equity-report** | Generate professional equity research reports |

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
    ├── instagram-poster/SKILL.md
    ├── instagram-poster/post.py
    └── equity-report/SKILL.md
```

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