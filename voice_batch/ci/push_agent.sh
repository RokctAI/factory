#!/usr/bin/env bash
# Commit one job's passing audio + its manifest to the agent branch.
#
#   AGENT_PAT=... push_agent.sh AGENT_DIR BRANCH TUTOR VOICE CATEGORY
#   AGENT_PAT=... push_agent.sh AGENT_DIR BRANCH r3 VOICE LABEL
#
# Only rokct/ branches. A tutor job stages only the tutor's .wav files and
# <voice>_manifest[.<category>].json; an r3 job stages only
# lms/dart/templates/assets/r3_packs/audio/<key>.mp3 and
# r3_manifest.<voice>[.partNN].json directly in that folder (additions,
# changes, and the merge job's removal of folded part manifests). Never the
# reference, never anything else. Then it
# pushes with the token passed as an HTTP header (git -c, scoped to the origin
# host) on every network-capable git command. The token is masked, never
# echoed, never written to .git/config; xtrace is off.
# Idempotent: re-running over identical files commits nothing. Parallel
# category jobs touch disjoint files, so a rejected push is resolved by
# rebasing this job's one commit onto the remote branch and retrying (up to 5
# times). The branch may not exist yet (the job started it from main after
# the old one was merged and deleted): the first push creates it, and a
# sibling that loses that race finds it on the remote and rebases onto it.
# The checkout is a sparse, blob-less partial clone, so the rebase lazily
# fetches missing blobs from the promisor remote: it must carry the header too,
# or that fetch fails with "could not read Username".
set +x
set -euo pipefail

dir="${1:?agent dir}"; branch="${2:?branch}"; tutor="${3:?tutor or r3}"; voice="${4:?voice}"; category="${5:?category}"
: "${AGENT_PAT:?AGENT_PAT must be set}"
case "$branch" in
  rokct/*) ;;
  *) echo "::error::refusing to push to non-rokct/ branch"; exit 1 ;;
esac
if ! printf '%s' "$voice" | grep -qE '^[a-z][a-z0-9_]{0,31}$'; then
  echo "::error::bad voice name"; exit 1
fi
if [ "$tutor" = "r3" ]; then
  tdir="lms/dart/templates/assets/r3_packs/audio"
  allowed="^$tdir/([A-Za-z0-9_][A-Za-z0-9_.-]*\.mp3|r3_manifest\.${voice}(\.part[0-9]{2})?\.json)$"
  ext="mp3"; manifest="$tdir/r3_manifest.${voice}.json"
elif printf '%s' "$tutor" | grep -qE '^tutor_[0-9]{3}$'; then
  tdir="lms/team/tutors/CAPS/$tutor"
  allowed="^$tdir/(.+\.wav|${voice}_manifest(\.[a-z]+)?\.json)$"
  ext="wav"; manifest="$tdir/${voice}_manifest.json"
else
  echo "::error::target must be tutor_NNN or r3"; exit 1
fi
cd "$dir"

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

if [ "$tutor" = "r3" ]; then
  # Only files directly in the audio folder that match the allow-list:
  # new, modified, or deleted (the merge job removes folded part manifests).
  { git ls-files --others --exclude-standard -- "$tdir"; git ls-files --modified -- "$tdir"; git ls-files --deleted -- "$tdir"; } \
    | { grep -E "$allowed" || true; } | sort -u | while IFS= read -r f; do git add -A -- "$f"; done
else
  for m in "$tdir/${voice}"_manifest*.json; do
    if [ -e "$m" ]; then git add -- "$m"; fi
  done
  { git ls-files --others --exclude-standard -- "$tdir"; git ls-files --modified -- "$tdir"; } \
    | { grep -E '\.wav$' || true; } | sort -u | while IFS= read -r f; do git add -- "$f"; done
fi
if git diff --cached --quiet; then
  echo "category $category: nothing new to commit"
  exit 0
fi
echo "Staged:"
git diff --cached --name-only | sed 's/^/  /'
if git diff --cached --name-only | grep -v -E "$allowed"; then
  echo "::error::unexpected staged path; refusing to commit"; exit 1
fi
n_audio=$(git diff --cached --name-only --diff-filter=AM | grep -c "\.$ext\$" || true)
git commit --quiet -m "$tutor $voice: $category audio ($n_audio file(s)) from factory voice batch CI" \
  -m "Rendered and gated by RokctAI/factory voice_batch (run ${GITHUB_RUN_ID:-local}). Per-line seeds, scores and hashes are in $manifest."
# This job's commit sits alone on top of base; rebases replay only base..HEAD.
base="$(git rev-parse HEAD~1)"

b64="$(printf 'x-access-token:%s' "$AGENT_PAT" | base64 -w0)"
echo "::add-mask::$b64"
auth="AUTHORIZATION: basic $b64"
# Scope the header to origin's scheme://host/ (https://github.com/ in CI).
host="$(git remote get-url origin | sed -E 's#^([a-z]+://[^/]+/).*#\1#')"
# -c is inherited by git's child processes (GIT_CONFIG_PARAMETERS), which
# covers the promisor lazy fetches that rebase triggers.
agit() { git -c "http.${host}.extraheader=$auth" "$@"; }
for i in 1 2 3 4 5; do
  if agit push --quiet origin "HEAD:refs/heads/$branch"; then
    echo "category $category: pushed $(git rev-parse --short HEAD) to $branch"
    exit 0
  fi
  # 2 = the branch is not on the remote (yet): nothing to rebase onto, retry
  # the push that creates it. Anything else non-zero is a real failure.
  rc=0; agit ls-remote --exit-code --heads origin "refs/heads/$branch" > /dev/null || rc=$?
  if [ "$rc" = 2 ]; then
    echo "push failed (attempt $i); $branch is not on the remote yet, retrying"
  elif [ "$rc" != 0 ]; then
    echo "::error::could not reach the agent repo"; exit 1
  else
    echo "push rejected (attempt $i); rebasing on the remote branch"
    agit fetch --quiet --depth=50 origin "$branch"
    agit rebase --quiet --onto FETCH_HEAD "$base" || { git rebase --abort || true; echo "::error::rebase onto the agent branch failed"; exit 1; }
    base="$(git rev-parse FETCH_HEAD)"
  fi
  sleep $((RANDOM % 5 + 2))
done
echo "::error::could not push to the agent branch"
exit 1
