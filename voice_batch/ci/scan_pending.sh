#!/usr/bin/env bash
# The scheduled voice batch run: print the first batch in voice_batches/inbox/
# (sorted by path) that still has a line to render, or nothing.
#
#   AGENT_PAT=... scan_pending.sh AGENT_DIR
#
# AGENT_DIR is a sparse, blob-less checkout of agent main without audio
# (scripts, voice specs, R-3 app sources, manifests). For each valid batch
# whose rokct/ agent branch exists, the branch's manifests (only the
# *manifest*.json files directly in the batch's team or R-3 audio folder) are
# fetched blob-less at depth 1 and exported to a temp dir; pending.py then
# counts lines done on the branch or on main (a passed entry for the same
# text and reference, or one that failed every seed round) and picks the
# first batch with any left. Run from the factory checkout root.
#
# Logs batch paths and counts only. Only rokct/ branches are read. The token
# goes in an HTTP header scoped to the agent host on every git command (agit;
# blob-less, so `git show` lazily fetches the manifest blob and needs it too),
# masked, never echoed and never written to a git config; xtrace is off.
set +x
set -euo pipefail

agent="${1:?agent checkout dir}"
: "${AGENT_PAT:?AGENT_PAT must be set}"
here="$(cd "$(dirname "$0")/.." && pwd)"
r3_dir="lms/dart/templates/assets/r3_packs/audio"

b64="$(printf 'x-access-token:%s' "$AGENT_PAT" | base64 -w0)"
echo "::add-mask::$b64" >&2
auth="AUTHORIZATION: basic $b64"
host="$(git -C "$agent" remote get-url origin | sed -E 's#^([a-z]+://[^/]+/).*#\1#')"
# The empty value first resets any header inherited from a persisted
# checkout credential for the same host (see resolve_agent_ref.sh).
agit() { git -C "$agent" -c "http.${host}.extraheader=" -c "http.${host}.extraheader=$auth" "$@"; }

tmp="$(mktemp -d "${RUNNER_TEMP:-${TMPDIR:-/tmp}}/voice-scan.XXXXXX")"
trap 'rm -rf "$tmp"' EXIT
list="$tmp/list.tsv"
: > "$list"

n=0
while IFS= read -r f; do
  n=$((n + 1))
  if ! out="$(python3 "$here/batch.py" "$f" 2>/dev/null)"; then
    echo "::warning::scan: $f is not a valid batch; skipped" >&2
    continue
  fi
  field() { printf '%s\n' "$out" | sed -n "s/^$1=//p" | head -n1; }
  branch="$(field agent_branch)"
  case "$branch" in rokct/*) ;; *) echo "::warning::scan: $f: not a rokct/ branch; skipped" >&2; continue ;; esac
  if [ "$(field kind)" = r3 ]; then dir="$r3_dir"; else dir="$(field team_dir)"; fi
  overlay=""
  rc=0; agit ls-remote --exit-code --heads origin "refs/heads/$branch" > /dev/null || rc=$?
  if [ "$rc" = 0 ]; then
    overlay="$tmp/b$n"
    agit fetch --quiet --depth=1 --filter=blob:none origin "+refs/heads/$branch:refs/scan/b$n"
    agit ls-tree --name-only "refs/scan/b$n" -- "$dir/" | { grep -E '/[^/]*manifest[^/]*\.json$' || true; } \
      | while IFS= read -r p; do
          mkdir -p "$overlay/$(dirname "$p")"
          agit show "refs/scan/b$n:$p" > "$overlay/$p"
        done
    agit update-ref -d "refs/scan/b$n"
  elif [ "$rc" != 2 ]; then
    echo "::error::scan: could not reach the agent repo (ls-remote exit $rc)" >&2
    exit 1
  fi
  printf '%s\t%s\n' "$f" "$overlay" >> "$list"
done < <(git -c core.quotePath=false ls-files -- voice_batches/inbox | grep -E '^voice_batches/inbox/.+\.json$' | LC_ALL=C sort)

python3 "$here/pending.py" --agent-root "$agent" --scan "$list"
