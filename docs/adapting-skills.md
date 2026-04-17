# Adapting Skills for Nanobot

This guide explains how to port skills from other agent frameworks (like OpenCode) to nanobot's format.

## Key Differences

| Aspect | OpenCode | Nanobot |
|--------|----------|---------|
| Format | YAML frontmatter + Markdown | Plain Markdown |
| Location | `~/.opencode/plugins/` | `~/.nanobot/workspace/skills/` |
| Installation | `opencode plugin install` | Copy files manually |
| Scripts | Optional | Optional |
| Naming | `skill-name/SKILL.md` | `skill-name/SKILL.md` |

## Porting Steps

### 1. Create the Skill Directory

```bash
mkdir -p ~/.nanobot/workspace/skills/<skill-name>
```

### 2. Create SKILL.md

Nanobot skills are plain Markdown. The minimum viable skill:

```markdown
# Skill Name

**Use when:** [When to trigger this skill]

**Core principle:** [One sentence philosophy]

---

## The Process

[Your methodology here]

## Examples

[Good vs bad examples]

## Red Flags

[Anti-patterns to watch for]
```

### 3. Optional: Add Supporting Files

If your skill has scripts:

```
skills/
└── my-skill/
    ├── SKILL.md
    ├── script.py      # Optional helper script
    └── config.json    # Optional config
```

### 4. Test It

Send a message to nanobot that triggers the skill. Verify it follows the methodology.

## Common Pitfalls

- **YAML frontmatter:** Nanobot ignores it, but it's fine to keep for compatibility
- **Code examples:** Adapt to Python/shell (nanobot's environment) rather than TypeScript/Node
- **File paths:** Update any path examples to nanobot's workspace structure
- **Trigger phrases:** Make sure "Use when" covers natural language triggers

## Skill Quality Checklist

- [ ] "Use when" header at top
- [ ] Core principle stated
- [ ] Actionable steps (not just theory)
- [ ] Good/bad examples where helpful
- [ ] Red flags section
- [ ] No placeholder text (TODO, TBD, etc.)
- [ ] Tested with nanobot