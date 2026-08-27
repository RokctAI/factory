#!/usr/bin/env python3
# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Mojibake guard: fail when UTF-8-decoded-as-cp1252 artifacts appear in job
cards or lesson content.

Signatures (the visible residue of UTF-8 bytes read as cp1252/latin-1):
  a mangled lead byte — U+00E2 (from E2, the punctuation/euro family),
  U+00C2 (stray C2) or U+00C3 (C3, double-decoded accented letters) — but
  ONLY when immediately followed by the cp1252 or latin-1 rendering of a
  UTF-8 continuation byte (0x80-0xBF), because that pairing is what an
  actual mangled multi-byte sequence produces (e.g. E2 80 94 -> a-circumflex
  + euro + right-double-quote for an em-dash; C2 A0 -> A-circumflex + NBSP;
  C3 A9 -> A-tilde + copyright sign for e-acute; under a latin-1 mis-read
  the 0x80-0x9F bytes surface as C1 controls instead).  A bare U+00C2 followed
  by ordinary ASCII is NOT mojibake: DBE maths papers legitimately write
  angle notation with a precomposed A-circumflex (U+00C2 then "1", as in
  "angle A1 = 40 deg", or between plain capitals as in "K^AC"), and blunt
  substring matching false-positived on every such line.
  Spelled as escapes below so this file never trips its own check.

Corrupted cards must never advance a pipeline level and corrupted lesson
files must never reach a release, so this check runs in TWO layers:
  - locally (fail fast before a push):  python lessons/scripts/CAPS/check_mojibake.py <files>
    or a full-tree scan:                python lessons/scripts/CAPS/check_mojibake.py --all
  - in CI (the enforcement layer):      .github/workflows/mojibake_check.yml
    runs it against every pushed change under .rokct/agent/jobs/ and lessons/.

Known writer pitfall this guards against: Windows PowerShell 5.1 Get-Content
reads BOM-less UTF-8 as cp1252 — read with an explicit encoding
([IO.File]::ReadAllText($f, [Text.Encoding]::UTF8)) before writing back.

Exit 0 = clean; exit 1 = mojibake found (file, line number and the offending
line are printed for every hit).
"""
import re
import sys
from pathlib import Path


def _continuation_residue():
    """Characters a UTF-8 continuation byte (0x80-0xBF) can turn into when
    the file is mis-read.  Two renderings exist in the wild and both are
    covered: the cp1252 one (Windows readers; the five bytes cp1252 leaves
    undefined — 81, 8D, 8F, 90, 9D — pass through as C1 controls), and the
    latin-1 one, where every 0x80-0x9F byte lands on the C1 control of the
    same value.  For 0xA0-0xBF the two encodings agree, so the set is the
    64 cp1252 characters plus the 27 remaining C1 controls (91 total).
    C1 controls never occur in legitimate lesson text, so widening the set
    with them costs no false positives."""
    chars = set()
    for b in range(0x80, 0xC0):
        try:
            chars.add(bytes([b]).decode("cp1252"))
        except UnicodeDecodeError:
            pass
        chars.add(chr(b))  # latin-1 rendering; C1 control for 0x80-0x9F
    return "".join(sorted(chars))


# A mangled lead byte (U+00E2 from E2, U+00C2 from C2, U+00C3 from C3) is
# only mojibake when the very next character is the cp1252 or latin-1
# rendering of a continuation byte.  This covers the whole E2 80 xx
# punctuation family and the E2 82 AC euro sign (U+20AC, byte 0x80, is
# itself in the residue set) under both mis-decodes, while a precomposed
# A-circumflex followed by plain ASCII — legitimate DBE angle notation —
# passes.
MOJIBAKE_RE = re.compile(
    "[\u00e2\u00c2\u00c3][{}]".format(re.escape(_continuation_residue()))
)
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
        if MOJIBAKE_RE.search(line):
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
