#!/usr/bin/env bash
# Copy the persona reference voices from a checkout of RokctAI/agent into
# radio_ads/voices/ (git-ignored), then delete the checkout.
#
#   install_voices.sh AGENT_CHECKOUT_DIR
#
# Prints counts only, never file contents. The voices are used for rendering
# and must not end up in commits or artifacts (the workflow uploads only
# radio_ads/out/<id>/).
set -euo pipefail

src="${1:?usage: install_voices.sh AGENT_CHECKOUT_DIR}"
voices="$src/lms/team/voices"
dest="$(cd "$(dirname "$0")/.." && pwd)/voices"

if [ ! -d "$voices/samples" ]; then
  echo "::error::$voices/samples not found in RokctAI/agent at this ref. The voices are expected under lms/team/voices/samples on RokctAI/agent main (PR #319); if VOICES_REF is set, check that it points at a ref that has them (radio_ads/README.md, 'Render in CI')." >&2
  exit 1
fi

shopt -s nullglob
wavs=("$voices"/samples/*.wav)
specs=("$voices"/*.voice.json)
if [ "${#wavs[@]}" -eq 0 ]; then
  echo "::error::no reference WAVs in lms/team/voices/samples/ at this ref" >&2
  exit 1
fi
mkdir -p "$dest"
cp "${wavs[@]}" "$dest/"
if [ "${#specs[@]}" -gt 0 ]; then cp "${specs[@]}" "$dest/"; fi
rm -rf "$src"
echo "Installed ${#wavs[@]} reference voices (+${#specs[@]} .voice.json) into radio_ads/voices/"
