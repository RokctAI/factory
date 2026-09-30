#!/usr/bin/env bash
# Commit one category's passing audio + its manifest to the agent branch.
#
#   AGENT_PAT=... push_agent.sh AGENT_DIR BRANCH TUTOR VOICE CATEGORY
#
# Only claude/ branches. Stages only the tutor's .wav files and
# <voice>_manifest[.<category>].json (never the reference, never anything else), then
# pushes with the token passed as an HTTP header (git -c, scoped to the origin
# host) on every network-capable git command. The token is masked, never
# echoed, never written to .git/config; xtrace is off.
# Idempotent: re-running over identical files commits nothing. Parallel
# category jobs touch disjoint files, so a rejected push is resolved by
# rebasing onto the remote branch and retrying (up to 5 times).
# The checkout is a sparse, blob-less partial clone, so the rebase lazily
# fetches missing blobs from the promisor remote: it must carry the header too,
# or that fetch fails with "could not read Username".
set +x
set -euo pipefail

dir="${1:?agent dir}"; branch="${2:?branch}"; tutor="${3:?tutor}"; voice="${4:?voice}"; category="${5:?category}"
: "${AGENT_PAT:?AGENT_PAT must be set}"
case "$branch" in
  claude/*) ;;
  *) echo "::error::refusing to push to non-claude/ branch"; exit 1 ;;
esac
tdir="lms/team/tutors/CAPS/$tutor"
cd "$dir"

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

for m in "$tdir/${voice}"_manifest*.json; do
  if [ -e "$m" ]; then git add -- "$m"; fi
done
{ git ls-files --others --exclude-standard -- "$tdir"; git ls-files --modified -- "$tdir"; } \
  | { grep -E '\.wav$' || true; } | sort -u | while IFS= read -r f; do git add -- "$f"; done
if git diff --cached --quiet; then
  echo "category $category: nothing new to commit"
  exit 0
fi
echo "Staged:"
git diff --cached --name-only | sed 's/^/  /'
if git diff --cached --name-only | grep -v -E "^$tdir/(.+\.wav|${voice}_manifest(\.[a-z]+)?\.json)$"; then
  echo "::error::unexpected staged path; refusing to commit"; exit 1
fi
n_wav=$(git diff --cached --name-only | grep -c '\.wav$' || true)
git commit --quiet -m "$tutor $voice: $category audio ($n_wav file(s)) from factory voice batch CI" \
  -m "Rendered and gated by RokctAI/factory voice_batch (run ${GITHUB_RUN_ID:-local}). Per-line seeds, scores and hashes are in $tdir/${voice}_manifest.json."

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
  echo "push rejected (attempt $i); rebasing on the remote branch"
  agit fetch --quiet --depth=50 origin "$branch"
  agit rebase --quiet FETCH_HEAD || { git rebase --abort || true; echo "::error::rebase onto the agent branch failed"; exit 1; }
  sleep $((RANDOM % 5 + 2))
done
echo "::error::could not push to the agent branch"
exit 1
