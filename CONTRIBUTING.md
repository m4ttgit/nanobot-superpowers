# Contributing to nanobot-superpowers

Thank you for your interest in contributing!

## How to Contribute

### 1. Port a Skill

Found a useful OpenCode (or similar) skill? Port it to nanobot format:

1. Fork the repo
2. Create a new skill directory: `skills/<skill-name>/`
3. Create `SKILL.md` inside it
4. Test it works with nanobot
5. Submit a PR

**Porting guidelines:**
- Convert YAML frontmatter to plain Markdown (optional — nanobot doesn't require it)
- Keep the core methodology intact
- Adapt examples to nanobot's context (Python/shell instead of TypeScript/Node if appropriate)
- Add a "When to Use" header at the top
- Keep it concise — nanobot skills should be scannable

### 2. Improve Existing Skills

- Fix typos or unclear explanations
- Add better examples
- Adapt to new nanobot features
- Improve cross-references between skills

### 3. Add New Skills

Have an idea for a new skill? Open an issue first to discuss.

## Skill Format

Nanobot skills are simple Markdown files:

```markdown
# Skill Name

**Use when:** [One sentence describing when to trigger]

**Core principle:** [One sentence core philosophy]

---

## The Process

[Detailed steps...]

## Key Patterns

[Examples with good/bad comparisons]

## Red Flags

- [Things that mean STOP]
```

**Requirements:**
- `SKILL.md` filename (case-sensitive)
- Clear "Use when" header
- Core principle stated upfront
- Actionable steps, not just theory
- Good/bad examples where helpful
- Red flags section for anti-patterns

**Optional:**
- YAML frontmatter (nanobot ignores it but it's fine to keep)
- Executable scripts in subdirectory

## Development

```bash
# Clone the repo
git clone https://github.com/m4tthias/nanobot-superpowers.git
cd nanobot-superpowers

# Install test dependencies
pip install markdownlint-cli2  # or your preferred Markdown linter

# Validate all skills
make validate

# Or validate a single skill
markdownlint skills/brainstorming/SKILL.md
```

## Pull Request Checklist

- [ ] Skill directory named correctly (`kebab-case`)
- [ ] `SKILL.md` exists inside
- [ ] "Use when" header at top
- [ ] Core principle stated
- [ ] No placeholder text (TODO, TBD, etc.)
- [ ] Examples are realistic
- [ ] Red flags section included
- [ ] Tested with nanobot

## Reporting Issues

Found a bug or have a suggestion? Open an issue with:
- Skill name
- What you expected vs what happened
- Example conversation or context

## License

By contributing, you agree that your contributions will be licensed under the MIT License.