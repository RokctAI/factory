#!/usr/bin/env python3
"""Mojibake guard: fail when UTF-8-decoded-as-cp1252 artifacts appear in job
cards or lesson content.

Signatures (the visible residue of UTF-8 bytes read as cp1252/latin-1):
  U+00E2 U+20AC (a-circumflex + euro sign) — the E2 80 xx punctuation family
  (em-dash, curly quotes, ellipsis); U+00C2 (stray C2 prefix, typically
  before NBSP); U+00C3 (C3 prefix, accented letters double-decoded).
  Spelled as escapes below so this file never trips its own check.

Corrupted cards must never advance a pipeline level and corrupted lesson
files must never reach a release, so this check runs in TWO layers:
  - locally (fail fast before a push):  python lessons/scripts/check_mojibake.py <files>
    or a full-tree scan:                python lessons/scripts/check_mojibake.py --all
  - in CI (the enforcement layer):      .github/workflows/mojibake_check.yml
    runs it against every pushed change under .rokct/agent/jobs/ and lessons/.

Known writer pitfall this guards against: Windows PowerShell 5.1 Get-Content
reads BOM-less UTF-8 as cp1252 — read with an explicit encoding
([IO.File]::ReadAllText($f, [Text.Encoding]::UTF8)) before writing back.

Exit 0 = clean; exit 1 = mojibake found (file, line number and the offending
line are printed for every hit).
"""
import sys
from pathlib import Path

SIGNATURES = ("â€", "Â", "Ã")
SCAN_GLOBS = (".rokct/agent/jobs/**/*.md", "lessons/**/*")
# Binary/asset formats that legitimately contain arbitrary bytes.
SKIP_SUFFIXES = {".pdf", ".mp3", ".wav", ".png", ".jpg", ".jpeg", ".zip", ".pyc"}


def check_file(path):
    """Return [(line_number, line_text), ...] mojibake hits for one file."""
    p = Path(path)
    if not p.is_file() or p.suffix.lower() in SKIP_SUFFIXES:
        return []
    if p.name == "check_mojibake.py":
        return []  # this file necessarily contains the signature strings
    try:
        text = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # Not valid UTF-8 at all — that is its own corruption failure.
        return [(0, "<file is not valid UTF-8>")]
    hits = []
    for n, line in enumerate(text.splitlines(), 1):
        if any(sig in line for sig in SIGNATURES):
            hits.append((n, line.strip()))
    return hits


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args == ["--all"]:
        files = []
        for pattern in SCAN_GLOBS:
            files.extend(str(f) for f in Path(".").glob(pattern) if f.is_file())
    else:
        files = args

    failed = False
    checked = 0
    for f in files:
        hits = check_file(f)
        checked += 1
        for n, line in hits:
            failed = True
            print(f"MOJIBAKE {f}:{n}: {line[:160]}")
    if failed:
        print("\nFAIL: mojibake artifacts found — the file was written with a "
              "wrong encoding (UTF-8 decoded as cp1252). Fix the content and "
              "the writer that produced it. Corrupted cards must not advance.")
        return 1
    print(f"mojibake check clean ({checked} file(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
