#!/usr/bin/env bash
# Pick the agent ref a voice batch job checks out (render), or tell the
# merge job the branch is still missing (nothing was rendered).
#
#   AGENT_PAT=... resolve_agent_ref.sh [--create] BRANCH [AGENT_URL]
#
# Writes ref=<ref> and create=<true|false> to $GITHUB_OUTPUT (stdout when
# unset). BRANCH on the agent repo: ref=BRANCH, create=false. No such branch
# (never created, or its agent PR was merged and the branch auto-deleted
# before this run): ref=main, create=true, and the job creates BRANCH locally
# from main so push_agent.sh's push creates it. With --create (the plan job,
# once, before the matrix starts) a missing BRANCH is created on the remote
# at main's tip instead, so parallel render jobs all check out an existing
# branch and none of them has to create it: ref=BRANCH, create=false. If
# another run creates it first, that is fine too. Also writes empty=true when
# BRANCH exists but still points at main's tip (created, nothing pushed yet),
# else empty=false. Only rokct/ branches. The
# token goes in an HTTP header scoped to the agent host (git -c), masked,
# never echoed and never written to a git config; xtrace is off.
set +x
set -euo pipefail

create_remote=false
if [ "${1:-}" = "--create" ]; then create_remote=true; shift; fi
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
# -c is inherited by child processes, so this also covers fetch's helpers.
agit() { git -c "http.${host}.extraheader=" -c "http.${host}.extraheader=$auth" "$@"; }
has_branch() { printf '%s\n' "$1" | awk -v r="refs/heads/$branch" '$2 == r { f = 1 } END { exit !f }'; }
if ! heads="$(agit ls-remote --heads "$url" "refs/heads/$branch" refs/heads/main)"; then
  echo "::error::could not list the agent repo's branches"; exit 1
fi
out="${GITHUB_OUTPUT:-/dev/stdout}"
if ! has_branch "$heads" && [ "$create_remote" = true ]; then
  # Point the new ref at main's current tip. The remote already has that
  # commit, so the push sends no objects: a depth-1, blob-less fetch of main
  # into a throwaway bare repo is all it needs.
  tmp="$(mktemp -d "${RUNNER_TEMP:-${TMPDIR:-/tmp}}/agent-branch.XXXXXX")"
  trap 'rm -rf "$tmp"' EXIT
  git init --quiet --bare "$tmp"
  agit -C "$tmp" fetch --quiet --depth=1 --filter=blob:none "$url" refs/heads/main
  if agit -C "$tmp" push --quiet "$url" "FETCH_HEAD:refs/heads/$branch"; then
    echo "agent branch $branch created from main ($(git -C "$tmp" rev-parse --short FETCH_HEAD))"
  else
    # Lost a race with another creator: fine as long as it exists now.
    heads="$(agit ls-remote --heads "$url" "refs/heads/$branch")" || true
    if ! has_branch "$heads"; then
      echo "::error::could not create agent branch $branch"; exit 1
    fi
  fi
  { echo "ref=$branch"; echo "create=false"; echo "empty=true"; } >> "$out"
  exit 0
fi
if has_branch "$heads"; then
  sha_of() { printf '%s\n' "$heads" | awk -v r="refs/heads/$1" '$2 == r { print $1 }'; }
  empty=false
  if [ "$(sha_of "$branch")" = "$(sha_of main)" ]; then empty=true; fi
  echo "agent branch $branch exists; checking it out"
  { echo "ref=$branch"; echo "create=false"; echo "empty=$empty"; } >> "$out"
else
  echo "::notice::agent branch $branch does not exist; starting it from main"
  { echo "ref=main"; echo "create=true"; echo "empty=false"; } >> "$out"
fi
