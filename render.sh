#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
CHROME="/home/hatch/workspace/.browser-cache/chrome-linux64/chrome"
PROFILE_DIR="$(mktemp -d /tmp/chrome-prof.XXXXXX)"
trap 'rm -rf -- "$PROFILE_DIR"' EXIT
"$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars --force-device-scale-factor=1 --window-size=1024,1024 --user-data-dir="$PROFILE_DIR" --screenshot="$SCRIPT_DIR/entry.png" "file://$SCRIPT_DIR/page.html"
