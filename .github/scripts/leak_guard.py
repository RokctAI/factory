#!/usr/bin/env python3
"""Fail when the public engine could leak private content or voices.

This repository is public: anyone can read its files, run logs, job
summaries and artifacts, and a fork PR's run can restore its caches. The
content repos it works on are private. Checks:

  1. No audio files tracked anywhere (cloned voices, rendered lines, ads).
  2. No content-repo folders tracked (school/, books/, bible/, film/,
     StartupOS/, and radio_ads/out/).
  3. No `actions/upload-artifact` step.
  4. No `actions/cache` path outside public model weights and tool caches.
  5. No `pull_request_target` trigger (it hands secrets to fork code).

A line may opt out with a trailing `# leak-guard: allow <reason>`; the
reason is required, so the exception is reviewed in the diff.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

AUDIO_EXT = {".wav", ".mp3", ".flac", ".ogg", ".m4a", ".aac", ".opus", ".webm"}
CONTENT_PREFIXES = ("school/", "lessons/", "books/", "bible/", "film/", "StartupOS/",
                    "radio_ads/out/", "radio_ads/samples/")
# Cache paths that only ever hold public downloads.
SAFE_CACHE_RE = re.compile(r"(HF_HOME|huggingface|ASR_DOWNLOAD_ROOT|\.cache/pip|~/\.npm|node_modules)")
ALLOW_RE = re.compile(r"#\s*leak-guard:\s*allow\s+\S")


def tracked_files(root):
    out = subprocess.run(["git", "-C", str(root), "ls-files", "-z"], check=True,
                         capture_output=True).stdout.decode()
    return [p for p in out.split("\0") if p]


def check_files(paths):
    errors = []
    for p in paths:
        if Path(p).suffix.lower() in AUDIO_EXT:
            errors.append(f"{p}: audio file tracked in the public engine")
        elif p.startswith(CONTENT_PREFIXES):
            errors.append(f"{p}: content belongs in a private content repo")
    return errors


def check_workflow(name, text):
    errors = []
    lines = text.split("\n")
    for k, ln in enumerate(lines):
        code = ln.split("#", 1)[0] if not ln.lstrip().startswith("#") else ""
        if not code.strip() or ALLOW_RE.search(ln):
            continue
        where = f"{name}:{k + 1}"
        if re.search(r"uses:\s*actions/upload-artifact@", code):
            errors.append(f"{where}: upload-artifact publishes files to anyone")
        if re.search(r"\bpull_request_target\b", code):
            errors.append(f"{where}: pull_request_target gives fork code the secrets")
        if re.search(r"uses:\s*actions/cache(/restore|/save)?@", code):
            # Look at this step's path: lines.
            j, paths = k + 1, []
            indent = len(ln) - len(ln.lstrip())
            if ln.lstrip().startswith("- "):
                indent += 2  # `- uses:` opens the step; its keys sit 2 deeper

            def in_step(s):
                d = len(s) - len(s.lstrip())
                return (not s.strip() or s.lstrip().startswith("#") or d > indent
                        or (d == indent and not s.lstrip().startswith("-")))
            while j < len(lines) and in_step(lines[j]):
                s = lines[j].strip()
                if s.startswith("path:"):
                    v = s[5:].strip()
                    if v in ("|", ">"):
                        key = len(lines[j]) - len(lines[j].lstrip())
                        j += 1
                        while j < len(lines) and len(lines[j]) - len(lines[j].lstrip()) > key:
                            paths.append(lines[j].strip())
                            j += 1
                        continue
                    paths.append(v)
                j += 1
            if not paths:
                errors.append(f"{where}: cache step without a readable path")
            for p in paths:
                if not SAFE_CACHE_RE.search(p):
                    errors.append(f"{where}: cache path {p!r} is not a public download; fork PR runs can restore it")
    return errors


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    root = Path(args.root)
    errors = check_files(tracked_files(root))
    for wf in sorted((root / ".github" / "workflows").glob("*.y*ml")):
        errors += check_workflow(f".github/workflows/{wf.name}", wf.read_text(encoding="utf-8"))
    for e in errors:
        print(f"::error::{e}")
    print(f"leak_guard: {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
