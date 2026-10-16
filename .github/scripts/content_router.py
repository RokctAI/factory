#!/usr/bin/env python3
"""Dispatch engine workflows when content repos change.

The content repos are private and carry no workflows, so a push to them
can't fire anything. Every quarter hour this compares each content repo's
main against the commit it saw last time, collects the paths changed by the
commits a workflow would have fired on, and dispatches every workflow whose
former push filter matches them (`.github/content_router.json`, written by
split/split.py from the factory's push filters).

A commit is skipped, as GitHub would have skipped its push:
  * its message carries [skip ci] (or [ci skip], [no ci], [skip actions],
    [actions skip]);
  * github-actions[bot] wrote it. Factory workflows pushed with
    GITHUB_TOKEN, which never starts a run; now they push with
    MONOREPO_PAT, so the router filters them instead.

Each dispatch passes `router_before` (the last commit seen) so the workflow
can diff the pushed range as its push run did.

Nothing private reaches the log: it prints repo names, commit counts and
workflow names, never paths or messages.

State: {"RokctAI/lessons": "<sha>", ...} in cursors.json on the engine's
router-state branch. The first run for a repo only records its head.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

API = "https://api.github.com"
SKIP_RE = re.compile(r"\[(skip ci|ci skip|no ci|skip actions|actions skip)\]", re.I)
BOT_LOGINS = {"github-actions[bot]"}
BOT_EMAILS = {"github-actions[bot]@users.noreply.github.com",
              "41898282+github-actions[bot]@users.noreply.github.com"}
MAX_FILES = 3000  # GitHub lists at most this many files for one commit


def glob_re(pattern):
    """GitHub Actions path-filter glob as a regex."""
    out, i = "", 0
    while i < len(pattern):
        c = pattern[i]
        if pattern.startswith("**", i):
            out += ".*"
            i += 2
        elif c == "*":
            out += "[^/]*"
            i += 1
        elif c == "?":
            out += "[^/]"
            i += 1
        else:
            out += re.escape(c)
            i += 1
    return re.compile(out + r"\Z")


def path_matches(path, patterns):
    """True when the last pattern matching path is not a negation."""
    hit = False
    for p in patterns:
        neg = p.startswith("!")
        if glob_re(p[1:] if neg else p).match(path):
            hit = not neg
    return hit


def skipped(commit):
    msg = commit.get("commit", {}).get("message", "")
    if SKIP_RE.search(msg):
        return True
    login = (commit.get("author") or {}).get("login", "")
    email = commit.get("commit", {}).get("author", {}).get("email", "")
    return login in BOT_LOGINS or email in BOT_EMAILS


def workflows_for(paths, routes, everything=False):
    hit = []
    for r in routes:
        if everything or any(path_matches(p, r["paths"]) for p in paths):
            if r["workflow"] not in hit:
                hit.append(r["workflow"])
    return hit


class GitHub:
    def __init__(self, token):
        self.token = token

    def call(self, method, url, body=None):
        if not url.startswith("http"):
            url = API + url
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, data=data, method=method, headers={
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        })
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read()
            return json.loads(raw) if raw else None

    def head(self, repo, branch="main"):
        return self.call("GET", f"/repos/{repo}/commits/{branch}")["sha"]

    def compare(self, repo, base, head):
        """(status, [commits]) for base...head, all pages."""
        commits, page, status = [], 1, None
        while True:
            r = self.call("GET", f"/repos/{repo}/compare/{base}...{head}?per_page=100&page={page}")
            status = r["status"]
            commits += r.get("commits", [])
            if len(commits) >= r.get("total_commits", 0) or not r.get("commits"):
                return status, commits
            page += 1

    def commit_files(self, repo, sha):
        files, page = [], 1
        while True:
            r = self.call("GET", f"/repos/{repo}/commits/{sha}?per_page=300&page={page}")
            batch = [f["filename"] for f in r.get("files", [])]
            batch += [f["previous_filename"] for f in r.get("files", []) if f.get("previous_filename")]
            files += batch
            if len(r.get("files", [])) < 300:
                return files
            page += 1

    def dispatch(self, engine, workflow, inputs):
        self.call("POST", f"/repos/{engine}/actions/workflows/{workflow}/dispatches",
                  {"ref": "main", "inputs": inputs})


def route_repo(gh, repo, routes, cursor, engine, dry_run=False):
    """Dispatch for one repo; return (new_cursor, dispatched workflows)."""
    head = gh.head(repo)
    if cursor is None:
        print(f"{repo}: first run, recording head")
        return head, []
    if cursor == head:
        print(f"{repo}: no new commits")
        return head, []
    status, commits = gh.compare(repo, cursor, head)
    if status not in ("ahead", "identical"):
        print(f"::warning::{repo}: main is {status} of the last commit seen (history rewritten?); "
              "resetting the cursor without dispatching. Run the affected workflows by hand.")
        return head, []
    live = [c for c in commits if not skipped(c)]
    print(f"{repo}: {len(commits)} new commit(s), {len(live)} that would have fired workflows")
    paths, everything = set(), False
    for c in live:
        files = gh.commit_files(repo, c["sha"])
        if len(files) >= MAX_FILES:
            everything = True
        paths.update(files)
    hit = workflows_for(sorted(paths), routes, everything)
    for wf in hit:
        print(f"{repo}: dispatching {wf}" + (" (dry run)" if dry_run else ""))
        if not dry_run:
            gh.dispatch(engine, wf, {"router_before": cursor})
    return head, hit


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--routes", default=".github/content_router.json")
    ap.add_argument("--state", required=True, help="cursors.json (read and rewritten)")
    ap.add_argument("--engine", default=os.environ.get("GITHUB_REPOSITORY", "RokctAI/factory"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    token = os.environ.get("GH_TOKEN")
    if not token:
        print("::error::GH_TOKEN (MONOREPO_PAT) is not set")
        return 1
    with open(args.routes) as f:
        table = json.load(f)["push"]  # pull_request routes: not handled yet (README)
    try:
        with open(args.state) as f:
            state = json.load(f)
    except FileNotFoundError:
        state = {}
    gh, failed = GitHub(token), False
    for repo, routes in table.items():
        try:
            state[repo], _ = route_repo(gh, repo, routes, state.get(repo), args.engine, args.dry_run)
        except urllib.error.HTTPError as e:
            # Keep the old cursor so the next run retries this range.
            print(f"::error::{repo}: GitHub API {e.code}; will retry next run")
            failed = True
    with open(args.state, "w") as f:
        json.dump(state, f, indent=2, sort_keys=True)
        f.write("\n")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
