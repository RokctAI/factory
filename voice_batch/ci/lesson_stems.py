#!/usr/bin/env python3
"""Lesson audio stems on the private lessons repo: MP3s as pre-release
assets, records committed in the lesson folder.

    LESSONS_PAT=... lesson_stems.py push  --lessons-root _lessons --stems-root DIR \
        --persona tutor_001 --lessons <rel>,<rel> [--repo RokctAI/lessons]
    LESSONS_PAT=... lesson_stems.py fetch --lessons-root _lessons --stems-root DIR --lesson <rel>

push: every passed line whose MP3 is not on the pre-release yet (or changed)
is uploaded to the pre-release for its subject, grade and term
(stems-<subject>-<grade>-<term>, created on first use), its asset (tag,
name, url, api_url) is written into the lesson's
voice/<persona>/manifest.json, and the manifest, qc_failed.json and
nothing else is committed to the lessons repo's main with [skip ci] (the
content router skips it). A rejected push rebases and retries.

Assets are never in git, so the repo stays small however much audio there
is; the lesson release (release_on_complete.py) and the backend find each
stem through the manifest. Run as run.py's checkpoint command and once more
at the end of the job. Logs lesson paths, keys and counts only. The token
is masked and passed as a header, never written to .git/config.

fetch: download the stems a lesson's audio.mp3 is made of (the tutors'
script segments) into DIR/<lesson rel>/voice/<persona>/<key>.mp3.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import lesson_lines as L  # noqa: E402

REPO = "RokctAI/lessons"
NAME_MAX = 180


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def token() -> str:
    t = os.environ.get("LESSONS_PAT", "")
    if not t:
        sys.exit("::error::LESSONS_PAT must be set")
    return t


def gh(*args: str, check: bool = True, capture: bool = True) -> subprocess.CompletedProcess:
    env = dict(os.environ, GH_TOKEN=token())
    return subprocess.run(["gh", *args], env=env, check=check, capture_output=capture, text=True)


def release_tag(rel: str) -> str:
    subject, _s, grade, term, _topic, _lesson = rel.split("/")
    return f"stems-{subject.replace('_', '-')}-{grade}-{term}"


def asset_name(rel: str, persona: str, key: str) -> str:
    _subject, _s, _g, _t, topic, lesson = rel.split("/")
    name = f"{topic}--{lesson}--{persona}--{key}.mp3"
    if len(name) > NAME_MAX:
        h = hashlib.sha1(f"{topic}/{lesson}".encode()).hexdigest()[:10]
        name = f"{topic[:60]}--{lesson[:60]}-{h}--{persona}--{key}.mp3"
    return name


def ensure_release(repo: str, tag: str, known: set[str]) -> None:
    if tag in known:
        return
    if gh("release", "view", tag, "--repo", repo, "--json", "tagName", check=False).returncode != 0:
        subject_grade_term = tag[len("stems-"):]
        r = gh("release", "create", tag, "--repo", repo, "--prerelease", "--target", "main",
               "--title", f"Lesson audio stems: {subject_grade_term}",
               "--notes", "Work in progress: per-voice lesson audio, rendered part by part as each voice is "
                          "approved. Each lesson folder's voice/<persona>/manifest.json lists its stems here. "
                          "The lesson release copies them once every part is in.", check=False)
        if r.returncode != 0 and gh("release", "view", tag, "--repo", repo, "--json", "tagName",
                                    check=False).returncode != 0:
            raise SystemExit(f"::error::could not create pre-release {tag}")
    known.add(tag)


def asset_index(repo: str, tag: str) -> dict:
    r = gh("release", "view", tag, "--repo", repo, "--json", "assets")
    return {a["name"]: a for a in json.loads(r.stdout).get("assets", [])}


def upload(repo: str, lessons_root: Path, stems: Path, persona: str, rels: list[str]) -> list[Path]:
    """Upload new/changed stems; returns the manifests it changed."""
    caps = L.curriculum_root(lessons_root)
    known: set[str] = set()
    changed: list[Path] = []
    for rel in rels:
        mpath = caps / rel / L.STEM_DIR / persona / L.MANIFEST
        if not mpath.is_file():
            continue
        m = json.loads(mpath.read_text(encoding="utf-8"))
        tag = release_tag(rel)
        todo = []
        for e in m.get("lines", []):
            a = e.get("asset") or {}
            if a.get("sha256") == e.get("sha256") and a.get("tag") == tag:
                continue
            src = stems / rel / L.STEM_DIR / persona / e["file"]
            if src.is_file() and sha256(src) == e.get("sha256"):
                todo.append((e, src))
        if not todo:
            continue
        ensure_release(repo, tag, known)
        with tempfile.TemporaryDirectory() as tmp:
            files = []
            for e, src in todo:
                dst = Path(tmp) / asset_name(rel, persona, e["key"])
                shutil.copyfile(src, dst)
                files.append(str(dst))
            for i in range(0, len(files), 20):
                for attempt in range(4):
                    if gh("release", "upload", tag, *files[i:i + 20], "--repo", repo, "--clobber",
                          check=False).returncode == 0:
                        break
                    time.sleep(2 ** (attempt + 1))
                else:
                    raise SystemExit(f"::error::upload to {tag} failed")
        idx = asset_index(repo, tag)
        for e, _src in todo:
            name = asset_name(rel, persona, e["key"])
            a = idx.get(name)
            if a:
                e["asset"] = {"tag": tag, "name": name, "sha256": e["sha256"], "url": a.get("url"),
                              "api_url": a.get("apiUrl")}
        mpath.write_text(json.dumps(m, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        changed.append(mpath)
        print(f"{rel} {persona}: uploaded {len(todo)} stem(s) to {tag}")
    return changed


class Git:
    def __init__(self, root: Path):
        self.root = root
        b64 = base64.b64encode(f"x-access-token:{token()}".encode()).decode()
        print(f"::add-mask::{b64}")
        url = subprocess.run(["git", "-C", str(root), "remote", "get-url", "origin"], check=True,
                             capture_output=True, text=True).stdout.strip()
        host = re.sub(r"^([a-z]+://[^/]+/).*", r"\1", url)
        self.header = ["-c", f"http.{host}.extraheader=AUTHORIZATION: basic {b64}"]

    def __call__(self, *args: str, check: bool = True) -> subprocess.CompletedProcess:
        return subprocess.run(["git", *self.header, "-C", str(self.root), *args], check=check,
                              capture_output=True, text=True)


ALLOWED = re.compile(r"^school/curriculum/CAPS/[a-z_]+/session/[^/]+/[^/]+/[^/]+/[^/]+/"
                     r"(voice/(tutor|assistant)_\d{3}/(manifest|qc_failed)\.json|animations\.export\.json)$")


def commit_push(lessons_root: Path, paths: list[str], message: str) -> bool:
    """Commit exactly `paths` (allow-listed records) to main and push, rebasing
    on a rejected push. Returns False when there was nothing to commit."""
    git = Git(lessons_root)
    git("config", "user.name", "github-actions[bot]")
    git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    for p in paths:
        if not ALLOWED.match(p):
            raise SystemExit(f"::error::refusing to commit {p}")
        git("add", "-A", "--", p)
    if git("diff", "--cached", "--quiet", check=False).returncode == 0:
        return False
    staged = git("diff", "--cached", "--name-only").stdout.split()
    bad = [p for p in staged if not ALLOWED.match(p)]
    if bad:
        raise SystemExit(f"::error::unexpected staged path {bad[0]}")
    git("commit", "--quiet", "-m", f"{message} [skip ci]",
        "-m", f"Written by RokctAI/factory lesson audio CI (run {os.environ.get('GITHUB_RUN_ID', 'local')}).")
    # This commit sits alone on top of base (the checkout is shallow), so a
    # rebase replays exactly base..HEAD onto the fetched main.
    base = git("rev-parse", "HEAD~1").stdout.strip()
    for attempt in range(10):
        if git("push", "--quiet", "origin", "HEAD:refs/heads/main", check=False).returncode == 0:
            print(f"pushed {git('rev-parse', '--short', 'HEAD').stdout.strip()} to main ({len(staged)} file(s))")
            return True
        if git("fetch", "--quiet", "--depth=1", "origin", "main", check=False).returncode == 0:
            if git("rebase", "--quiet", "--onto", "FETCH_HEAD", base, check=False).returncode != 0:
                git("rebase", "--abort", check=False)
                raise SystemExit("::error::rebase onto lessons main failed")
            base = git("rev-parse", "FETCH_HEAD").stdout.strip()
        time.sleep(random.randint(2, 8))
    raise SystemExit("::error::could not push to lessons main")


def cmd_push(args) -> int:
    lessons_root = Path(args.lessons_root).resolve()
    rels = [x for x in args.lessons.split(",") if x]
    upload(args.repo, lessons_root, Path(args.stems_root).resolve(), args.persona, rels)
    caps_rel = Path("school/curriculum/CAPS")
    paths = []
    for rel in rels:
        d = lessons_root / caps_rel / rel / L.STEM_DIR / args.persona
        for n in (L.MANIFEST, "qc_failed.json"):
            if (d / n).exists() or n == "qc_failed.json":
                paths.append(str(caps_rel / rel / L.STEM_DIR / args.persona / n))
    tracked_or_present = [p for p in paths if (lessons_root / p).exists() or
                          Git(lessons_root)("ls-files", "--error-unmatch", p, check=False).returncode == 0]
    if not tracked_or_present:
        return 0
    if not commit_push(lessons_root, tracked_or_present, f"Lesson audio: {args.persona} ({len(rels)} lesson(s))"):
        print("nothing new to commit")
    return 0


def cmd_fetch(args) -> int:
    lessons_root = Path(args.lessons_root).resolve()
    stems = Path(args.stems_root).resolve()
    caps = L.curriculum_root(lessons_root)
    r = L.roles(lessons_root, caps / args.lesson)
    import lesson_audio as LA
    want = LA.tutor_keys(lessons_root, r)
    for persona in dict.fromkeys(p for p, _k in want):
        mpath = L.manifest_path(caps, r, persona)
        m = json.loads(mpath.read_text(encoding="utf-8")) if mpath.is_file() else {}
        by_key = {e["key"]: e for e in m.get("lines", [])}
        for p, key in want:
            if p != persona or key not in by_key or not by_key[key].get("asset"):
                continue
            a = by_key[key]["asset"]
            dst = stems / L.stem_rel(r, persona, key)
            dst.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory() as tmp:
                gh("release", "download", a["tag"], "--repo", args.repo, "--pattern", a["name"], "--dir", tmp)
                got = Path(tmp) / a["name"]
                if sha256(got) != a["sha256"]:
                    raise SystemExit(f"::error::{args.lesson} {persona}/{key}: asset hash differs from the manifest")
                shutil.move(str(got), dst)
    miss = LA.missing_segments(lessons_root, stems, r)
    print(f"{args.lesson}: {len(want) - len(miss)} of {len(want)} segment stem(s) fetched")
    return 0 if not miss else 3


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("push", "fetch"):
        p = sub.add_parser(name)
        p.add_argument("--lessons-root", required=True)
        p.add_argument("--stems-root", required=True)
        p.add_argument("--repo", default=REPO)
        if name == "push":
            p.add_argument("--persona", required=True)
            p.add_argument("--lessons", required=True)
        else:
            p.add_argument("--lesson", required=True)
    args = ap.parse_args(argv)
    return {"push": cmd_push, "fetch": cmd_fetch}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
