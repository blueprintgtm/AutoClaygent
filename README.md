# AutoClaygent

Build production-quality Claygent prompts with AI-guided methodology.

**Part of Blueprint GTM by Jordan Crawford**

---

## Quick Start (3 Steps)

### Step 1: Add Your License Key

1. Find `license.txt` in the AutoClaygent folder
2. Double-click to open it
3. Replace the placeholder with your license key (starts with `CMB-`)
4. Save (Cmd+S on Mac, Ctrl+S on Windows)

> **No license?** Purchase at [autoclaygent.blueprintgtm.com](https://autoclaygent.blueprintgtm.com)

---

### Step 2: Install Claude Code

**What is Terminal?** It's a text-based way to control your computer. You only need to copy-paste commands.

**Open Terminal:**
- **Mac:** Press `Cmd + Space`, type `Terminal`, press Enter
- **Windows:** Press `Windows` key, type `PowerShell`, press Enter

**Install Claude Code:**

Mac/Linux:
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows (in PowerShell):
```powershell
irm https://claude.ai/install.ps1 | iex
```

> Already have Node.js? You can use: `npm install -g @anthropic-ai/claude-code`

---

### Step 3: Start AutoClaygent

#### Option A: Drag and Drop (Recommended)

This works on any system and doesn't require knowing where your folder is:

1. **Open Terminal** (see Step 2 for how)
2. **Type** `cd ` (that's the letters "cd" followed by a space - don't press Enter yet!)
3. **Find your AutoClaygent folder** in Finder (Mac) or File Explorer (Windows)
4. **Drag the folder** into the Terminal window - the path will appear automatically
5. **Press Enter**
6. **Type** `claude` and press Enter

**What it looks like:**
```
$ cd /Users/yourname/Downloads/AutoClaygent
$ claude
```

#### Option B: Auto-Find Command (Mac Only)

This command automatically finds AutoClaygent wherever you put it:

```bash
cd "$(mdfind -name webhook_server.py -onlyin ~ 2>/dev/null | xargs -I{} dirname {} | head -1)" && claude
```

Copy the whole thing, paste into Terminal, and press Enter.

---

## Wrong Folder? No Problem!

If you accidentally start Claude Code in the wrong place:

1. **AutoClaygent will detect this automatically**
2. **It will search your computer** for the AutoClaygent folder
3. **It will tell you exactly what command to run**

Just follow the instructions it shows you.

---

## What's Included

| File | What It Does |
|------|--------------|
| `CLAUDE.md` | AutoClaygent instructions (loaded automatically) |
| `license.txt` | Your license key goes here |
| `webhook_server.py` | Server for Clay callbacks |
| `references/` | Templates and documentation |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "command not found: claude" | Go back to Step 2 - Claude Code isn't installed yet |
| "I can't find the folder" | Use the drag-and-drop method in Step 3 |
| License key doesn't work | Check for extra spaces. Key should start with `CMB-` |
| "Wrong directory" message | Follow the instructions shown - it will help you find the right folder |

---

## Getting Updates

**If you cloned from GitHub:**
```bash
cd /path/to/AutoClaygent && git pull
```

**If you downloaded the ZIP:**
Re-download from [autoclaygent.blueprintgtm.com](https://autoclaygent.blueprintgtm.com)

---

## Support

- **Website:** [autoclaygent.blueprintgtm.com](https://autoclaygent.blueprintgtm.com)
- **Email:** support@blueprintgtm.com
- **Lessons:** [autoclaygent.blueprintgtm.com/lessons](https://autoclaygent.blueprintgtm.com/lessons/claude-code-setup)
