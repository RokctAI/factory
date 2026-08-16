#!/usr/bin/env bash
# Install the Rokct agent protocol into this repo. Run once, before the first
# commit. The protocol is fetched rather than vendored so a spawned repo never
# ships a stale copy; .workspace_config.json is already seeded, so initiate.py
# will not stop to ask which workspace this belongs to.
set -euo pipefail

curl -sSL https://raw.githubusercontent.com/RokctAI/The-Rokct-Protocol/main/profiles/local/initiate.py \
  -o .rokct/initiate.py
python .rokct/initiate.py
