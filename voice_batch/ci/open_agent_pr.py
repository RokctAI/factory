#!/usr/bin/env python3
"""Open a PR in the agent repo from a batch's rokct/ branch into main, or,
when one is already open, leave one short comment with this run's counts.

    AGENT_PAT=... python voice_batch/ci/open_agent_pr.py --repo RokctAI/agent \\
        --head rokct/<branch> --target <tutor_NNN|r3> --voice <voice> \\
        --manifest <merged manifest> [--run-id ID --run-url URL]

Idempotent: the PR is only created when none is open for head -> base, and
a run's comment carries a hidden marker so re-running the step never posts
it twice. The PR is opened ready for review (never draft). Bodies and
comments carry counts, the run URL and a "Failed QC" table (line ids,
attempts and failing gates, never line text) of the final-failed lines. The
token goes in a header, is never printed and never written to disk.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from qc_failed import last_failing  # noqa: E402

ATTRIBUTION = "<!-- ccr-projects-attribution -->\n_Requested by **Ray** via a Claude Code Project_"
FOOTER = ("🤖 Generated with [Claude Code](https://claude.com/claude-code)\n\n"
          "https://claude.ai/code/session_01WVrZ3ZtDLBuD78jnGwzGHF")


class Api:
    def __init__(self, base: str, token: str):
        self.base, self.token = base.rstrip("/"), token

    def call(self, method: str, path: str, body: dict | None = None):
        req = urllib.request.Request(
            self.base + path, method=method,
            data=None if body is None else json.dumps(body).encode(),
            headers={"Authorization": f"Bearer {self.token}", "Accept": "application/vnd.github+json",
                     "X-GitHub-Api-Version": "2022-11-28", "Content-Type": "application/json",
                     "User-Agent": "factory-voice-batch"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status, json.loads(r.read() or b"null")
        except urllib.error.HTTPError as e:
            try:
                return e.code, json.loads(e.read() or b"null")
            except ValueError:
                return e.code, None


def counts(manifest: dict, run_id: str | None) -> dict:
    """This run's pass/fail/needs-listen counts (entries tagged with the run
    id); the manifest totals when no run id is given."""
    mine = (lambda e: e.get("ci_run_id") == run_id) if run_id else (lambda e: True)
    lines = [e for e in manifest.get("lines", []) if mine(e)]
    failed = [e for e in manifest.get("failed", []) if mine(e)]
    return {"passed": len(lines), "failed": len(failed),
            "needs_listen": sum(bool(e.get("needs_listen")) for e in lines),
            "total_passed": len(manifest.get("lines", [])), "total_failed": len(manifest.get("failed", []))}


def counts_line(c: dict) -> str:
    s = f"This run: {c['passed']} passed, {c['failed']} failed"
    if c["needs_listen"]:
        s += f", {c['needs_listen']} respelled for phonics (need a listen before merging)"
    return s + f". Branch manifest total: {c['total_passed']} passed, {c['total_failed']} failed."


FAILED_ROWS = 50


def failed_table(manifest: dict) -> list[str]:
    """'Failed QC' section: the lines that failed every seed round (ids,
    attempts and the gates that failed last). Empty when none. The full
    per-round log is qc_failed.json beside the clips on this branch."""
    failed = manifest.get("failed", [])
    if not failed:
        return []
    out = ["## Failed QC", "",
           f"{len(failed)} line(s) failed every seed round; their audio is not committed. "
           "Per-round gates and values: `qc_failed.json` beside the clips.", "",
           "| line | category | attempts | failing gates (last round) |", "|---|---|---|---|"]
    for e in failed[:FAILED_ROWS]:
        out.append(f"| `{e['id']}` | {e.get('category', '')} | {e.get('attempts', len(e.get('seeds_tried') or []))} "
                   f"| {last_failing(e)} |")
    if len(failed) > FAILED_ROWS:
        out.append(f"| ... | {len(failed) - FAILED_ROWS} more | | |")
    return out + [""]


def title(target: str, voice: str) -> str:
    return f"{target} {voice}: rendered audio (voice batch)"


def pr_body(target: str, voice: str, c: dict, run_url: str, manifest: dict | None = None) -> str:
    what = "Grades R-3 activity-pack lines" if target == "r3" else "the tutor's standing lines"
    where = ("lms/dart/templates/assets/r3_packs/audio/ (MP3s plus r3_manifest)" if target == "r3"
             else "the tutor's team folder (WAVs beside their scripts plus the voice manifest)")
    return "\n".join([
        ATTRIBUTION, "",
        "## Before / After", "",
        f"**Before:** main has none of this batch's rendered audio for {what} in `{voice}`.", "",
        f"**After:** the factory voice batch CI rendered and gated the audio and committed it to {where} "
        "on this branch. **Merging this PR ships the audio into the app bundle.**", "",
        "## Run", "",
        f"- {run_url or 'run URL not available'}",
        f"- {counts_line(c)}", "",
        "Per-line scores, seeds and hashes are in the manifest on this branch.", "",
        *failed_table(manifest or {}),
        FOOTER,
    ])


def comment_body(c: dict, run_url: str, marker: str, manifest: dict | None = None) -> str:
    table = failed_table(manifest or {})
    return f"{marker}\nVoice batch run {run_url or '(local)'}: {counts_line(c)}" + ("\n\n" + "\n".join(table) if table else "")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--head", required=True)
    ap.add_argument("--base", default="main")
    ap.add_argument("--target", required=True)
    ap.add_argument("--voice", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--run-id", default=os.environ.get("GITHUB_RUN_ID", ""))
    ap.add_argument("--run-url", default="")
    args = ap.parse_args(argv)
    token = os.environ.get("AGENT_PAT", "")
    if not token:
        print("::error::AGENT_PAT must be set")
        return 1
    if not re.fullmatch(r"rokct/[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*", args.head) or ".." in args.head:
        print("::error::refusing: head must be a rokct/ branch")
        return 1
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repo):
        print("::error::bad repo")
        return 1
    if not (args.target == "r3" or re.fullmatch(r"(tutor|assistant)_\d{3}", args.target)) \
            or not re.fullmatch(r"[a-z][a-z0-9_]{0,31}", args.voice):
        print("::error::bad target or voice")
        return 1
    mp = Path(args.manifest)
    manifest = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
    c = counts(manifest, args.run_id or None)
    api = Api(os.environ.get("GITHUB_API_URL", "https://api.github.com"), token)
    owner = args.repo.split("/")[0]

    st, pulls = api.call("GET", f"/repos/{args.repo}/pulls?state=open&base={args.base}&head={owner}:{args.head}")
    if st != 200:
        print(f"::error::listing pull requests failed (HTTP {st})")
        return 1
    if pulls:
        num = pulls[0]["number"]
        marker = f"<!-- voice-batch-run:{args.run_id or 'local'} -->"
        st, comments = api.call("GET", f"/repos/{args.repo}/issues/{num}/comments?per_page=100")
        if st == 200 and any(marker in (x.get("body") or "") for x in comments or []):
            print(f"PR #{num} already open and already noted for this run; nothing to do")
            return 0
        st, _ = api.call("POST", f"/repos/{args.repo}/issues/{num}/comments",
                         {"body": comment_body(c, args.run_url, marker, manifest)})
        print(f"PR #{num} already open; {'commented with this run' if st == 201 else f'comment failed (HTTP {st})'}")
        return 0 if st == 201 else 1

    st, pr = api.call("POST", f"/repos/{args.repo}/pulls", {
        "title": title(args.target, args.voice), "head": args.head, "base": args.base,
        "body": pr_body(args.target, args.voice, c, args.run_url, manifest), "draft": False})
    if st == 201:
        print(f"opened PR #{pr['number']} (ready for review)")
        return 0
    if st == 422:
        # e.g. nothing to merge yet (no commits beyond base) or the branch is gone.
        print("no PR opened: GitHub declined (HTTP 422, likely no difference from the base branch)")
        return 0
    print(f"::error::opening the pull request failed (HTTP {st})")
    return 1


if __name__ == "__main__":
    sys.exit(main())
