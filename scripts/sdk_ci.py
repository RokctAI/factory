#!/usr/bin/env python3
"""PR and repo housekeeping for PRIVATE SDK repos, run from factory.

The SDK repos used to call 11 shared-workflows wrappers themselves, which
billed private Actions minutes. Each SDK repo now only notifies factory
(notify_factory_ci.yml); factory/.github/workflows/sdk_ci.yml calls this
script against the NOTIFYING repo, never against factory.

Commands (all take --repo owner/name; the token comes from GH_TOKEN):
  status   --sha S --context C --state success|failure|error|pending [--description D]
  size     --pr N        label size/xs..size/xl from additions+deletions
  semantic --pr N        conventional-commit title check -> commit status
  assign   --pr N        least-loaded assignee (same candidates as before)
  welcome  --pr N | --issue N   first-contribution comment
  labeler  --issue N     version label from the issue body checkboxes
  merge    --pr N        arm auto-merge (allowed authors, not draft, no workflow files)
  sweep                  re-evaluate every open PR for auto-merge
  stale                  label/close inactive issues and PRs (60 + 7 days)
  todo     --before B --after A   open issues for TODO/FIXME lines added in a push

Values are never printed beyond repo names, numbers and file paths.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request

API = "https://api.github.com"
ALLOWED_AUTHORS = {"rendanisinyage", "rendani sinyage", "rokctbot", "rokctbot[bot]"}
ASSIGN_CANDIDATES = ["RendaniSinyage", "RokctBOT"]
SEMANTIC_TYPES = ["feat", "fix", "docs", "style", "refactor", "perf", "test",
                  "build", "ci", "chore", "revert"]
SIZES = [("size/xs", 10), ("size/s", 100), ("size/m", 500), ("size/l", 1000)]
STALE_DAYS, CLOSE_DAYS = 60, 7
STALE_EXEMPT = {"security", "critical", "pinned"}
TODO_RE = re.compile(r"\b(TODO|FIXME)\b[:\s]+(.{3,120})")


def gh(method: str, path: str, body: dict | None = None, ok404: bool = False):
    token = os.environ.get("GH_TOKEN", "")
    if not token:
        sys.exit("GH_TOKEN is not set.")
    req = urllib.request.Request(
        API + path, method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {token}",
                 "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        if ok404 and e.code == 404:
            return None
        sys.exit(f"GitHub API {method} {path} failed: HTTP {e.code}")


def paged(path: str):
    page = 1
    sep = "&" if "?" in path else "?"
    while True:
        items = gh("GET", f"{path}{sep}per_page=100&page={page}")
        if not items:
            return
        yield from items
        if len(items) < 100:
            return
        page += 1


def run_url() -> str:
    s, r, i = (os.environ.get(k, "") for k in
               ("GITHUB_SERVER_URL", "GITHUB_REPOSITORY", "GITHUB_RUN_ID"))
    return f"{s}/{r}/actions/runs/{i}" if i else ""


def set_status(repo, sha, context, state, description=""):
    gh("POST", f"/repos/{repo}/statuses/{sha}", {
        "state": state, "context": f"factory/{context}",
        "description": description[:140], "target_url": run_url()})
    print(f"{repo}@{sha[:7]} factory/{context}: {state}")


def add_labels(repo, number, labels):
    gh("POST", f"/repos/{repo}/issues/{number}/labels", {"labels": labels})


def cmd_size(a):
    pr = gh("GET", f"/repos/{a.repo}/pulls/{a.pr}")
    n = pr["additions"] + pr["deletions"]
    label = next((lbl for lbl, mx in SIZES if n <= mx), "size/xl")
    for lb in gh("GET", f"/repos/{a.repo}/issues/{a.pr}/labels"):
        if lb["name"].startswith("size/") and lb["name"] != label:
            gh("DELETE", f"/repos/{a.repo}/issues/{a.pr}/labels/{lb['name']}", ok404=True)
    add_labels(a.repo, a.pr, [label])
    print(f"PR #{a.pr}: {n} changed lines -> {label}")


def cmd_semantic(a):
    pr = gh("GET", f"/repos/{a.repo}/pulls/{a.pr}")
    title = pr["title"]
    ok = re.match(rf"^({'|'.join(SEMANTIC_TYPES)})(\([^)]+\))?!?: \S", title) is not None
    set_status(a.repo, pr["head"]["sha"], "semantic", "success" if ok else "failure",
               "PR title follows type(scope): subject" if ok
               else "PR title must start with feat:, fix:, docs:, chore: ...")


def cmd_assign(a):
    pr = gh("GET", f"/repos/{a.repo}/pulls/{a.pr}")
    if pr.get("assignees"):
        print(f"PR #{a.pr}: already assigned")
        return
    best, low = None, 10 ** 9
    for user in ASSIGN_CANDIDATES:
        res = gh("GET", f"/search/issues?q=assignee:{user}+is:open")
        count = res.get("total_count", 0)
        if count < low:
            best, low = user, count
    gh("POST", f"/repos/{a.repo}/issues/{a.pr}/assignees", {"assignees": [best]})
    print(f"PR #{a.pr}: assigned {best}")


def cmd_welcome(a):
    number = a.pr or a.issue
    item = gh("GET", f"/repos/{a.repo}/issues/{number}")
    author = item["user"]["login"]
    kind = "pr" if a.pr else "issue"
    q = f"repo:{a.repo}+author:{author}+is:{kind}"
    if gh("GET", f"/search/issues?q={q}").get("total_count", 0) > 1:
        print(f"#{number}: {author} is not new here")
        return
    msg = ("Thanks for your first Pull Request! Please ensure you have added a "
           "comprehensive description." if a.pr else
           "Thanks for opening your first issue! Please review CONTRIBUTING.md.")
    gh("POST", f"/repos/{a.repo}/issues/{number}/comments", {"body": msg})
    print(f"#{number}: welcomed first-time {kind} author")


def cmd_labeler(a):
    body = gh("GET", f"/repos/{a.repo}/issues/{a.issue}").get("body") or ""
    m = re.search(r"- \[x\] (v\d+\.\d+\.\d+)", body, re.I)
    if m:
        version = m.group(1)
    elif re.search(r"- \[x\] main", body, re.I):
        version = "main"
    else:
        m = re.search(r"- \[x\] Other.*?:\s*(v?\d+\.\d+\.\d+)", body, re.I)
        version = (m.group(1) if m.group(1).startswith("v") else "v" + m.group(1)) if m else None
    if not version:
        print(f"Issue #{a.issue}: no version ticked")
        return
    add_labels(a.repo, a.issue, [f"version: {version}"])
    print(f"Issue #{a.issue}: labelled version: {version}")


def _merge_one(repo, pr) -> str:
    if pr.get("draft"):
        return "draft"
    if pr.get("auto_merge"):
        return "auto-merge already armed"
    if pr["user"]["login"].lower() not in ALLOWED_AUTHORS:
        return f"author {pr['user']['login']} not allowed"
    files = [f["filename"] for f in paged(f"/repos/{repo}/pulls/{pr['number']}/files")]
    if any(f.startswith(".github/workflows/") for f in files):
        return "touches .github/workflows/"
    q = """mutation($id:ID!){enablePullRequestAutoMerge(input:{pullRequestId:$id,mergeMethod:SQUASH}){clientMutationId}}"""
    token = os.environ["GH_TOKEN"]
    req = urllib.request.Request(
        API + "/graphql", method="POST",
        data=json.dumps({"query": q, "variables": {"id": pr["node_id"]}}).encode(),
        headers={"Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            res = json.loads(r.read())
    except urllib.error.HTTPError as e:
        return f"enabling auto-merge failed (HTTP {e.code}), retry next sweep"
    if res.get("errors"):
        return "enabling auto-merge refused, retry next sweep"
    return "auto-merge armed"


def cmd_merge(a):
    pr = gh("GET", f"/repos/{a.repo}/pulls/{a.pr}")
    print(f"PR #{a.pr}: {_merge_one(a.repo, pr)}")


def cmd_sweep(a):
    for pr in paged(f"/repos/{a.repo}/pulls?state=open"):
        print(f"PR #{pr['number']}: {_merge_one(a.repo, pr)}")


def cmd_stale(a):
    now = dt.datetime.now(dt.timezone.utc)
    for it in paged(f"/repos/{a.repo}/issues?state=open"):
        labels = {lb["name"] for lb in it.get("labels", [])}
        if labels & STALE_EXEMPT:
            continue
        is_pr = "pull_request" in it
        stale_label = "no-pr-activity" if is_pr else "no-issue-activity"
        idle = now - dt.datetime.fromisoformat(it["updated_at"].replace("Z", "+00:00"))
        n = it["number"]
        if stale_label in labels and idle.days >= CLOSE_DAYS:
            gh("PATCH", f"/repos/{a.repo}/issues/{n}", {"state": "closed"})
            print(f"#{n}: closed after {CLOSE_DAYS} more idle days")
        elif stale_label not in labels and idle.days >= STALE_DAYS:
            kind = "PR" if is_pr else "issue"
            add_labels(a.repo, n, [stale_label])
            gh("POST", f"/repos/{a.repo}/issues/{n}/comments", {
                "body": f"This {kind} is stale because it has been open {STALE_DAYS} days with no activity."})
            print(f"#{n}: marked stale")


def cmd_todo(a):
    if not a.before or set(a.before) == {"0"}:
        print("No base commit (new branch): nothing to compare.")
        return
    cmp = gh("GET", f"/repos/{a.repo}/compare/{a.before}...{a.after}")
    existing = {i["title"] for i in paged(f"/repos/{a.repo}/issues?state=all&labels=todo")}
    for f in cmp.get("files", []):
        if f["filename"].startswith((".rokct/", "node_modules/")):
            continue
        for line in (f.get("patch") or "").splitlines():
            if not line.startswith("+") or line.startswith("+++"):
                continue
            m = TODO_RE.search(line)
            if not m:
                continue
            title = f"{m.group(1)}: {m.group(2).strip()}"[:120]
            if title in existing:
                continue
            gh("POST", f"/repos/{a.repo}/issues", {
                "title": title, "labels": ["todo"],
                "body": f"Added in `{f['filename']}` at {a.after[:7]}."})
            existing.add(title)
            print(f"Opened TODO issue from {f['filename']}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("cmd")
    p.add_argument("--repo", required=True)
    p.add_argument("--pr", type=int)
    p.add_argument("--issue", type=int)
    p.add_argument("--sha")
    p.add_argument("--context")
    p.add_argument("--state")
    p.add_argument("--description", default="")
    p.add_argument("--before")
    p.add_argument("--after")
    a = p.parse_args()
    if not re.fullmatch(r"RokctAI/[A-Za-z0-9_.-]+", a.repo):
        sys.exit("Bad repo name.")
    if a.cmd == "status":
        set_status(a.repo, a.sha, a.context, a.state, a.description)
        return
    fn = globals().get(f"cmd_{a.cmd}")
    if not fn:
        sys.exit(f"Unknown command {a.cmd}")
    fn(a)


if __name__ == "__main__":
    main()
