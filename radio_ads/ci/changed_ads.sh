#!/usr/bin/env bash
# Print the ad JSONs a CI run should render, one repo-relative path per line.
#
#   changed_ads.sh EVENT BEFORE AFTER [INPUT_PATH] [DEFAULT_BRANCH]
#
# push:              JSONs under radio_ads/inbox/ added or modified between
#                    BEFORE and AFTER (deleted files are skipped). On a new
#                    branch (BEFORE is all zeros) the base is the merge-base
#                    with origin/DEFAULT_BRANCH.
# workflow_dispatch: INPUT_PATH if given (must be a .json under radio_ads/),
#                    otherwise every JSON committed under radio_ads/inbox/.
# Needs the full history (actions/checkout fetch-depth: 0).
set -euo pipefail

event="${1:?usage: changed_ads.sh EVENT BEFORE AFTER [INPUT_PATH] [DEFAULT_BRANCH]}"
before="${2:-}"
after="${3:-HEAD}"
input="${4:-}"
default_branch="${5:-main}"
inbox_re='^radio_ads/inbox/.+\.json$'

list_inbox() {
  git -c core.quotePath=false ls-files -- radio_ads/inbox | grep -E "$inbox_re" || true
}

if [ "$event" = "workflow_dispatch" ]; then
  if [ -n "$input" ]; then
    case "$input" in
      *..*) echo "::error::ad_path must not contain '..': $input" >&2; exit 1 ;;
      radio_ads/*.json) ;;
      *) echo "::error::ad_path must be a .json file under radio_ads/, e.g. radio_ads/inbox/my_ad.json (got: $input)" >&2; exit 1 ;;
    esac
    if [ ! -f "$input" ]; then
      echo "::error::ad_path not found in this commit: $input" >&2; exit 1
    fi
    printf '%s\n' "$input"
  else
    list_inbox
  fi
  exit 0
fi

zero="0000000000000000000000000000000000000000"
if [ -z "$before" ] || [ "$before" = "$zero" ] || ! git cat-file -e "${before}^{commit}" 2>/dev/null; then
  base="$(git merge-base "$after" "origin/$default_branch" 2>/dev/null || true)"
  if [ -z "$base" ]; then
    list_inbox
    exit 0
  fi
  before="$base"
fi

git -c core.quotePath=false diff --name-only --diff-filter=AMR "$before" "$after" -- radio_ads/inbox \
  | grep -E "$inbox_re" || true
