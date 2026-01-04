#!/bin/bash
# AutoClaygent Launcher
# Double-click this file to start AutoClaygent in Claude Code

# Get the directory where this script is located
cd "$(dirname "$0")"

echo ""
echo "================================"
echo "   Starting AutoClaygent..."
echo "================================"
echo ""

# Check if Claude Code is installed
if ! command -v claude &> /dev/null; then
    echo "ERROR: Claude Code is not installed."
    echo ""
    echo "Please install Claude Code first:"
    echo "  npm install -g @anthropic-ai/claude-code"
    echo ""
    echo "Then run this script again."
    echo ""
    read -p "Press Enter to close..."
    exit 1
fi

# Check if license.key exists and has content
if [ ! -f "license.key" ]; then
    echo "ERROR: license.key file not found."
    echo ""
    echo "Please create a license.key file with your key."
    echo ""
    read -p "Press Enter to close..."
    exit 1
fi

LICENSE=$(cat license.key | tr -d '[:space:]')
if [ -z "$LICENSE" ] || [ "$LICENSE" = "PASTE_YOUR_LICENSE_KEY_HERE" ]; then
    echo "ERROR: No valid license key found."
    echo ""
    echo "Please open license.key and paste your license key."
    echo "Your key starts with CMB- and is in your purchase receipt."
    echo ""
    read -p "Press Enter to close..."
    exit 1
fi

echo "License key found. Launching Claude Code..."
echo ""

# Launch Claude Code in this directory
claude

