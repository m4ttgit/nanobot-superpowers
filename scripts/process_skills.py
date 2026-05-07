import os
import re

# Map source files to destination files
skill_map = [
    ("D:\\Projects\\claude-skills\\.codex\\skills\\ci-cd-pipeline-builder\\SKILL.md", "D:\\Projects\\nanobot-superpowers\\skills\\nanobot-ci-cd-pipeline-builder\\SKILL.md"),
    ("D:\\Projects\\claude-skills\\.codex\\skills\\mcp-server-builder\\SKILL.md", "D:\\Projects\\nanobot-superpowers\\skills\\nanobot-mcp-server-builder\\SKILL.md"),
    ("D:\\Projects\\claude-skills\\.codex\\skills\\database-designer\\SKILL.md", "D:\\Projects\\nanobot-superpowers\\skills\\nanobot-database-designer\\SKILL.md"),
    ("D:\\Projects\\claude-skills\\.codex\\skills\\rag-architect\\SKILL.md", "D:\\Projects\\nanobot-superpowers\\skills\\nanobot-rag-architect\\SKILL.md"),
    ("D:\\Projects\\claude-skills\\.codex\\skills\\observability-designer\\SKILL.md", "D:\\Projects\\nanobot-superpowers\\skills\\nanobot-observability-designer\\SKILL.md"),
    ("D:\\Projects\\claude-skills\\.codex\\skills\\performance-profiler\\SKILL.md", "D:\\Projects\\nanobot-superpowers\\skills\\nanobot-performance-profiler\\SKILL.md"),
    ("D:\\Projects\\claude-skills\\.codex\\skills\\monorepo-navigator\\SKILL.md", "D:\\Projects\\nanobot-superpowers\\skills\\nanobot-monorepo-navigator\\SKILL.md"),
    ("D:\\Projects\\claude-skills\\.codex\\skills\\release-manager\\SKILL.md", "D:\\Projects\\nanobot-superpowers\\skills\\nanobot-release-manager\\SKILL.md"),
    ("D:\\Projects\\claude-skills\\.codex\\skills\\runbook-generator\\SKILL.md", "D:\\Projects\\nanobot-superpowers\\skills\\nanobot-runbook-generator\\SKILL.md"),
    ("D:\\Projects\\claude-skills\\.codex\\skills\\git-worktree-manager\\SKILL.md", "D:\\Projects\\nanobot-superpowers\\skills\\nanobot-git-worktree-manager\\SKILL.md"),
    ("D:\\Projects\\claude-skills\\.codex\\skills\\env-secrets-manager\\SKILL.md", "D:\\Projects\\nanobot-superpowers\\skills\\nanobot-env-secrets-manager\\SKILL.md"),
    ("D:\\Projects\\claude-skills\\.codex\\skills\\codebase-onboarding\\SKILL.md", "D:\\Projects\\nanobot-superpowers\\skills\\nanobot-codebase-onboarding\\SKILL.md")
]

for src, dst in skill_map:
    print(f"Processing {src}...")
    try:
        with open(src, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the closing --- of YAML frontmatter
        # YAML starts with --- and ends with ---
        # Split into lines and find the closing ---
        lines = content.split('\n')
        yaml_end = -1
        for i, line in enumerate(lines):
            if line.strip() == '---':
                yaml_end = i
                break
        
        # Content after YAML (skip the closing --- line)
        if yaml_end != -1 and yaml_end + 1 < len(lines):
            processed = '\n'.join(lines[yaml_end + 1:])
        else:
            processed = content  # No YAML found, use as-is
        
        # Write to destination
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(processed)
        print(f"  -> Written to {dst}")
    except Exception as e:
        print(f"  ERROR: {e}")

print("Done processing all 12 engineering skills.")
