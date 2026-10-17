#!/usr/bin/env python3
"""One-off: copy every voice file from an agent checkout into a lessons
checkout, at the voice_paths.py layout (phase 2 of the repo split).

    python voice_batch/ci/migrate_voices_to_lessons.py --agent ../agent --lessons ../lessons --check
    python voice_batch/ci/migrate_voices_to_lessons.py --agent ../agent --lessons ../lessons

Path map (voice_batch/voice_paths.py, VOICE_ROOT=voices):

  lms/team/voice_refs/<x>.wav                     -> voices/refs/<x>.wav
  lms/dart/templates/assets/r3_packs/audio/<f>    -> voices/r3/<f>
  lms/team/{tutors,assistants}/CAPS/<id>/<audio>  -> voices/team/{tutors,assistants}/CAPS/<id>/<audio>
      (<audio>: *.m4a, *.mp3, *.wav, *.timings.json, <voice>_manifest[.<cat>].json,
       qc_failed.json; persona JSON, scripts and images stay in agent)
  lms/team/voices/samples/<f>                     -> voices/samples/<f>

Files are copied byte for byte and verified by sha256. A copied JSON file
(manifests, audition.json, qc_failed logs) has every string value that is an
old agent path in the map ("file", "file_not_committed", "reference.path",
"settings.output.dir", ...) rewritten to its new path; JSON with nothing to
rewrite is copied unchanged. Script paths ("script": lms/team/.../NN.md) stay
as they are: the scripts stay in agent.

Nothing is ever deleted or changed in the agent checkout (removing the old
files there is a later, separate step). A destination that already exists
with the expected bytes is left alone (re-runs are idempotent); one with
other bytes is a conflict, reported and not overwritten unless --overwrite.

--check only reports what a run would do (and checks the existing copies).
Output: counts and MB per area, then conflicts and failures by path. Paths
and counts only, never file contents. Exit 1 on a conflict or a failed
verification, else 0. Does not commit or push: review and commit the lessons
checkout yourself.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import voice_paths as vp  # noqa: E402

AREAS = (
    ("refs", vp.AGENT_REFS),
    ("r3", vp.AGENT_R3),
    ("team", f"{vp.AGENT_TEAM}/tutors/CAPS"),
    ("team", f"{vp.AGENT_TEAM}/assistants/CAPS"),
    ("samples", vp.AGENT_SAMPLES),
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sources(agent: Path) -> list[tuple[str, str]]:
    """(area, agent-relative path) of every file in the path map, sorted.
    Symlinks are skipped (never followed out of the checkout)."""
    out: set[tuple[str, str]] = set()
    for area, base in AREAS:
        root = agent / base
        if not root.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = sorted(d for d in dirnames if not (Path(dirpath) / d).is_symlink() and d != ".git")
            for f in filenames:
                p = Path(dirpath) / f
                if p.is_symlink() or not p.is_file():
                    continue
                rel = p.relative_to(agent).as_posix()
                if vp.map_agent_path(rel) is not None:
                    out.add((area, rel))
    return sorted(out, key=lambda x: x[1])


def rewrite_paths(obj, root: str):
    """obj with every string that is an old agent voice path mapped to its
    new path; (new obj, number of strings rewritten)."""
    if isinstance(obj, str):
        new = vp.map_agent_path(obj, root) if obj.startswith("lms/") else None
        return (new, 1) if new is not None and new != obj else (obj, 0)
    if isinstance(obj, list):
        items = [rewrite_paths(x, root) for x in obj]
        return [x for x, _ in items], sum(n for _, n in items)
    if isinstance(obj, dict):
        items = {k: rewrite_paths(v, root) for k, v in obj.items()}
        return {k: v for k, (v, _) in items.items()}, sum(n for _, n in items.values())
    return obj, 0


def json_style(text: str) -> dict:
    """Keep the source file's indent, its ASCII escaping and trailing newline."""
    indent = None
    for line in text.splitlines()[1:]:
        stripped = line.lstrip(" ")
        if stripped and len(stripped) < len(line):
            indent = len(line) - len(stripped)
            break
    return {"indent": indent, "ensure_ascii": not any(ord(c) > 127 for c in text), "newline": text.endswith("\n")}


def payload(src: Path, root: str) -> tuple[bytes, int]:
    """The bytes the destination should hold, and how many paths were rewritten."""
    data = src.read_bytes()
    if src.suffix != ".json":
        return data, 0
    try:
        text = data.decode("utf-8")
        obj = json.loads(text)
    except (UnicodeDecodeError, ValueError):
        return data, 0                      # not JSON we can read: copy as is
    new, n = rewrite_paths(obj, root)
    if not n:
        return data, 0
    st = json_style(text)
    out = json.dumps(new, indent=st["indent"], ensure_ascii=st["ensure_ascii"]) + ("\n" if st["newline"] else "")
    return out.encode("utf-8"), n


def migrate(agent: Path, lessons: Path, root: str = vp.DEFAULT_ROOT, check: bool = False,
            overwrite: bool = False) -> dict:
    """Copy (or, with check, only plan) every mapped file. Returns the report."""
    if not root:
        raise ValueError("the voice root must not be empty (that is the agent layout itself)")
    rep = {"areas": {}, "copied": 0, "same": 0, "conflicts": [], "failed": [], "rewritten_json": 0,
           "rewritten_paths": 0, "bytes": 0, "check": check}
    for area, rel in sources(agent):
        a = rep["areas"].setdefault(area, {"files": 0, "bytes": 0})
        src = agent / rel
        dst_rel = vp.map_agent_path(rel, root)
        dst = lessons / dst_rel
        data, n = payload(src, root)
        a["files"] += 1
        a["bytes"] += len(data)
        rep["bytes"] += len(data)
        if n:
            rep["rewritten_json"] += 1
            rep["rewritten_paths"] += n
        want = sha256(data)
        if dst.exists():
            if dst.is_file() and sha256(dst.read_bytes()) == want:
                rep["same"] += 1
                continue
            if not overwrite:
                rep["conflicts"].append(dst_rel)
                continue
        if check:
            rep["copied"] += 1              # would copy
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        tmp = dst.with_name(dst.name + ".migrate-tmp")
        tmp.write_bytes(data)
        os.replace(tmp, dst)
        if sha256(dst.read_bytes()) != want or (not n and sha256(src.read_bytes()) != want):
            rep["failed"].append(dst_rel)
        else:
            rep["copied"] += 1
    return rep


def mb(n: int) -> str:
    return f"{n / 1_000_000:.1f} MB"


def summary(rep: dict) -> str:
    verb = "would copy" if rep["check"] else "copied"
    lines = [f"voice migration {'(check only, nothing written)' if rep['check'] else ''}".rstrip()]
    for area in ("refs", "r3", "team", "samples"):
        a = rep["areas"].get(area, {"files": 0, "bytes": 0})
        lines.append(f"  {area:8s} {a['files']:6d} file(s)  {mb(a['bytes'])}")
    total = sum(a["files"] for a in rep["areas"].values())
    lines.append(f"  total    {total:6d} file(s)  {mb(rep['bytes'])}")
    lines.append(f"{verb}: {rep['copied']}, already there: {rep['same']}, conflicts: {len(rep['conflicts'])}, "
                 f"failed verification: {len(rep['failed'])}")
    lines.append(f"JSON with paths rewritten: {rep['rewritten_json']} file(s), {rep['rewritten_paths']} path(s)")
    for p in rep["conflicts"]:
        lines.append(f"conflict (exists with other bytes, not overwritten): {p}")
    for p in rep["failed"]:
        lines.append(f"::error::sha256 verification failed: {p}")
    lines.append("nothing was deleted from the agent checkout")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--agent", required=True, help="RokctAI/agent checkout (read only)")
    ap.add_argument("--lessons", required=True, help="RokctAI/lessons checkout (written unless --check)")
    ap.add_argument("--root", default=vp.DEFAULT_ROOT, help="folder in lessons (default: voices)")
    ap.add_argument("--check", action="store_true", help="only report; write nothing")
    ap.add_argument("--overwrite", action="store_true", help="replace a destination that has other bytes")
    a = ap.parse_args(argv)
    agent, lessons = Path(a.agent).resolve(), Path(a.lessons).resolve()
    for p, name in ((agent, "--agent"), (lessons, "--lessons")):
        if not p.is_dir():
            print(f"::error::{name} {p} is not a directory", file=sys.stderr)
            return 2
    if agent == lessons or agent in lessons.parents or lessons in agent.parents:
        print("::error::--agent and --lessons must be separate checkouts", file=sys.stderr)
        return 2
    try:
        rep = migrate(agent, lessons, a.root.strip("/"), a.check, a.overwrite)
    except ValueError as exc:
        print(f"::error::{exc}", file=sys.stderr)
        return 2
    print(summary(rep))
    return 1 if rep["conflicts"] or rep["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
