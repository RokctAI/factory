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
# The cloned voices' references, pinned: a reference whose bytes differ is
# never used (same values as the voice batches that rendered these voices).
declare -A ref_sha256=(
  [voice_a_ref.wav]=de4a86bdea53fa5722cb8d08edd699098207019a8a2611bf569491a4e6993d5f
  [voice_b_ref.wav]=30c7ab70671dcd2c7239337d8de2dd2e6c9b468a11c0e7028646cc244ab6564d
)
mkdir -p "$dest"
# install_one SRC NAME: copy SRC to voices/NAME, refusing to replace a voice that
# is already there (two sources with one name would silently swap a voice).
install_one() {
  if [ -e "$dest/$2" ]; then
    echo "::error::radio_ads/voices/$2 already exists; refusing to overwrite it" >&2
    exit 1
  fi
  cp "$1" "$dest/$2"
}
for w in "${wavs[@]}"; do install_one "$w" "$(basename "$w")"; done
for s in "${specs[@]}"; do install_one "$s" "$(basename "$s")"; done
# Cloned voices (lms/team/voice_refs/voice_a_ref.wav and the like) install as
# voices/voice_a.wav, so an ad casts them as "voice": "voice_a".
refs=("$src"/lms/team/voice_refs/*_ref.wav)
cloned=0
for r in "${refs[@]}"; do
  base="$(basename "$r")"
  want="${ref_sha256[$base]:-}"
  if [ -z "$want" ]; then
    echo "::notice::skipping lms/team/voice_refs/$base: no pinned sha256 in radio_ads/ci/install_voices.sh"
    continue
  fi
  got="$(sha256sum "$r" | cut -d' ' -f1)"
  if [ "$got" != "$want" ]; then
    echo "::error::lms/team/voice_refs/$base sha256 does not match the pinned value; refusing to use it" >&2
    exit 1
  fi
  install_one "$r" "$(basename "$r" _ref.wav).wav"
  cloned=$((cloned + 1))
done
rm -rf "$src"
echo "Installed ${#wavs[@]} reference voices, $cloned cloned voices (sha256 verified) (+${#specs[@]} .voice.json) into radio_ads/voices/"
