#!/usr/bin/env bash
# Pick the agent ref a voice batch job checks out (render), or tell the
# merge job the branch is still missing (nothing was rendered).
#
#   AGENT_PAT=... resolve_agent_ref.sh BRANCH [AGENT_URL]
#
# Writes ref=<ref> and create=<true|false> to $GITHUB_OUTPUT (stdout when
# unset). BRANCH on the agent repo: ref=BRANCH, create=false. No such branch
# (never created, or its agent PR was merged and the branch auto-deleted
# before this run): ref=main, create=true, and the job creates BRANCH locally
# from main so push_agent.sh's push creates it. Only rokct/ branches. The
# token goes in an HTTP header scoped to the agent host (git -c), masked,
# never echoed and never written to a git config; xtrace is off.
set +x
set -euo pipefail

branch="${1:?branch}"; url="${2:-https://github.com/RokctAI/agent.git}"
: "${AGENT_PAT:?AGENT_PAT must be set}"
case "$branch" in
  rokct/*) ;;
  *) echo "::error::refusing to use non-rokct/ branch"; exit 1 ;;
esac

b64="$(printf 'x-access-token:%s' "$AGENT_PAT" | base64 -w0)"
echo "::add-mask::$b64"
auth="AUTHORIZATION: basic $b64"
host="$(printf '%s' "$url" | sed -E 's#^([a-z]+://[^/]+/).*#\1#')"
# CI runs this in the factory checkout, where actions/checkout persisted its
# own GITHUB_TOKEN as an extraheader for the same host; git would send that
# Authorization header first and GitHub would answer "not found" for the
# private agent repo. The empty value resets the inherited headers, so only
# ours is sent (push_agent.sh runs in .agent, checked out without them).
if ! heads="$(git -c "http.${host}.extraheader=" -c "http.${host}.extraheader=$auth" ls-remote --heads "$url" "refs/heads/$branch")"; then
  echo "::error::could not list the agent repo's branches"; exit 1
fi
out="${GITHUB_OUTPUT:-/dev/stdout}"
if printf '%s\n' "$heads" | awk -v r="refs/heads/$branch" '$2 == r { f = 1 } END { exit !f }'; then
  echo "agent branch $branch exists; checking it out"
  { echo "ref=$branch"; echo "create=false"; } >> "$out"
else
  echo "::notice::agent branch $branch does not exist; starting it from main"
  { echo "ref=main"; echo "create=true"; } >> "$out"
fi
