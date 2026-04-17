# Installation Guide

## Prerequisites

- [nanobot](https://github.com/nanobot-dev/nanobot) installed and running
- Access to your nanobot workspace (typically `~/.nanobot/workspace/`)

## Method 1: Git Clone (Recommended)

```bash
# Clone into your skills directory
git clone https://github.com/m4tthias/nanobot-superpowers.git \
  ~/.nanobot/workspace/skills/superpowers

# Or clone anywhere and symlink
git clone https://github.com/m4tthias/nanobot-superpowers.git /tmp/nanobot-superpowers
ln -s /tmp/nanobot-superpowers/skills/* \
  ~/.nanobot/workspace/skills/
```

## Method 2: Copy Individual Skills

```bash
# Copy specific skills you want
cp -r skills/brainstorming ~/.nanobot/workspace/skills/
cp -r skills/systematic-debugging ~/.nanobot/workspace/skills/
cp -r skills/verification-before-completion ~/.nanobot/workspace/skills/
cp -r skills/test-driven-development ~/.nanobot/workspace/skills/
cp -r skills/writing-plans ~/.nanobot/workspace/skills/
```

## Method 3: From Google Drive (If You Use rclone)

```bash
# If you have your skills backed up to Google Drive
rclone copy your_remote:nanobot_backup/skills/ \
  ~/.nanobot/workspace/skills/
```

## Method 4: Download ZIP

```bash
# Download and extract latest release
curl -L https://github.com/m4tthias/nanobot-superpowers/archive/refs/heads/main.zip \
  -o superpowers.zip
unzip superpowers.zip
cp -r nanobot-superpowers-main/skills/* \
  ~/.nanobot/workspace/skills/
rm -rf superpowers.zip nanobot-superpowers-main
```

## After Installation

1. **Verify skills are installed:**
   ```bash
   ls ~/.nanobot/workspace/skills/
   ```

2. **Nanobot will automatically load skills** on next message or restart

3. **Test a skill** by triggering it:
   - "Let's brainstorm a new feature"
   - "Debug why this is broken"
   - "equity report Tesla"

## Updating

```bash
cd ~/.nanobot/workspace/skills/superpowers
git pull
```

## Uninstalling

Remove the skill directories you don't want:
```bash
rm -rf ~/.nanobot/workspace/skills/brainstorming
rm -rf ~/.nanobot/workspace/skills/systematic-debugging
# etc.
```

## Troubleshooting

**Skill not loading?**
- Check the skill directory is named correctly (e.g., `brainstorming/`, not `brainstorming.md`)
- Ensure `SKILL.md` exists inside the skill directory
- Restart nanobot

**Skill not triggering?**
- Skills are read automatically when relevant context is detected
- You can also explicitly invoke: "Use the brainstorming skill"

## Skill Dependencies

Some skills reference others. For full functionality, install all skills:
```bash
cp -r skills/* ~/.nanobot/workspace/skills/
```