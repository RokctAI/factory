#!/usr/bin/env bash
# Copy the persona reference voices into radio_ads/voices/ (git-ignored),
# then delete the checkouts. Since phase 2 of the repo split the reference
# WAVs live in the private voice repo (vars.VOICE_REPO, default
# RokctAI/lessons) under voices/samples/ (voice_batch/voice_paths.py), and
# the persona specs (*.voice.json) stay in RokctAI/agent lms/team/voices/.
#
#   install_voices.sh VOICE_REPO_CHECKOUT_DIR [AGENT_CHECKOUT_DIR]
#
# Without AGENT_CHECKOUT_DIR no .voice.json is copied (the specs are optional
# metadata). Prints counts only, never file contents. The voices are used for
# rendering and must not end up in commits or artifacts (the workflow uploads
# only radio_ads/out/<id>/).
set -euo pipefail

src="${1:?usage: install_voices.sh VOICE_REPO_CHECKOUT_DIR [AGENT_CHECKOUT_DIR]}"
agent="${2:-}"
here="$(cd "$(dirname "$0")/.." && pwd)"
rel="$(python3 "$here/../voice_batch/voice_paths.py" samples)"
samples="$src/$rel"
dest="$here/voices"

if [ ! -d "$samples" ]; then
  echo "::error::$rel not found in the voice repo at this ref. The reference voices are expected under $rel on its main; if VOICES_REF is set, check that it points at a ref that has them (radio_ads/README.md, 'Render in CI')." >&2
  exit 1
fi

shopt -s nullglob
wavs=("$samples"/*.wav)
specs=()
if [ -n "$agent" ]; then specs=("$agent"/lms/team/voices/*.voice.json); fi
if [ "${#wavs[@]}" -eq 0 ]; then
  echo "::error::no reference WAVs in $rel/ at this ref" >&2
  exit 1
fi
mkdir -p "$dest"
cp "${wavs[@]}" "$dest/"
if [ "${#specs[@]}" -gt 0 ]; then cp "${specs[@]}" "$dest/"; fi
rm -rf "$src"
if [ -n "$agent" ]; then rm -rf "$agent"; fi
echo "Installed ${#wavs[@]} reference voices (+${#specs[@]} .voice.json) into radio_ads/voices/"
