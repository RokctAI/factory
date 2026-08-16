#!/usr/bin/env bash
# Install the Rokct agent protocol into this repo. Run once, before the first
# commit. The protocol is fetched rather than vendored so a spawned repo never
# ships a stale copy of it.
#
# Why .workspace_config.json is committed empty rather than absent:
# profiles/local/initiate.py auto-routes RokctAI/* repos to the org workspace,
# and for every other origin it falls through to an interactive input() asking
# for a parent repo. That prompt has no CI guard, so in a spawned repo — owned
# by a person, not the org — an unattended run dies with EOFError. The script
# only reaches the prompt when .rokct/.workspace_config.json is missing, so the
# scaffold ships one with an empty parent_repo. Both places the protocol reads
# that key treat empty as standalone (initiate.py's `not
# config_data.get("parent_repo")` branch, and sync_workspace.py's `if not
# parent_repo: return`), so the repo bootstraps as its own workspace and syncs
# nowhere. See docs/app-factory.md in the factory for the upstream fix.
set -euo pipefail

mkdir -p .rokct
curl -sSL https://raw.githubusercontent.com/RokctAI/The-Rokct-Protocol/main/profiles/local/initiate.py \
  -o .rokct/initiate.py
python3 .rokct/initiate.py
