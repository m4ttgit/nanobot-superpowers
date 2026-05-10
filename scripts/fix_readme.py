import os

tree_path = r"D:\Projects\nanobot-superpowers\README.md"
base = r"D:\Projects\nanobot-superpowers\skills"

with open(tree_path, "r", encoding="utf-8") as f:
    content = f.read()

orig_dirs = sorted([
    "brainstorming/", "systematic-debugging/",
    "verification-before-completion/", "test-driven-development/",
    "writing-plans/", "writing-skills/",
    "executing-plans/", "finishing-a-development-branch/",
    "using-superpowers/", "receiving-code-review/",
    "requesting-code-review/", "instagram-poster/", "equity-report/"
])

tree_lines = [
    "## Project Structure",
    "",
    "```",
    "nanobot-superpowers/",
    "    README.md",
    "    INSTALL.md",
    "    CONTRIBUTING.md",
    "    LICENSE",
    "    progress.md",
    "    REMAINING_SKILLS.md",
    "    .gitignore",
    "    docs/",
    "        adapting-skills.md",
    "    examples/",
    "        brainstorming-example.md",
    "        debugging-example.md",
    "        tdd-example.md",
    "    skills/",
]

for d in orig_dirs:
    tree_lines.append("        " + d)

tree_lines.append("        Nanobot Skills (130+ adapted + 13 new):")

dirs = sorted([d.name for d in os.scandir(base) if d.is_dir() and d.name.startswith("nanobot-")])
for d in dirs:
    tree_lines.append(f"            {d}/")

tree_lines.append("```")
tree_lines.append("")

# Find the old section and replace
start = content.find("## Project Structure")
if start == -1:
    print("ERROR: Could not find section")
    exit(1)

# Find end of old section's code block (look for the closing ``` then next ##)
after_start = start + len("## Project Structure")
# Find the closing ``` of the project structure code block
next_section = content.find("\n## ", after_start + 1)
if next_section == -1:
    next_section = len(content)

old_section = content[start:next_section]
new_section = "\n".join(tree_lines)

new_content = content.replace(old_section, new_section)

with open(tree_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"README updated. Replaced section of {len(old_section)} chars with {len(new_section)} chars")