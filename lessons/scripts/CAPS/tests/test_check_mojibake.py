#!/usr/bin/env python3
# Copyright (c) 2026 RokctAI
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

# Licensed under the MIT License.
# Copyright 2026 RokctAI
"""Unit tests for lessons/scripts/CAPS/check_mojibake.py (stdlib unittest).

Two directions are proven:
  1. Legitimate DBE (South African curriculum) angle notation — a
     precomposed A-circumflex (U+00C2) followed by plain ASCII, as it
     appears verbatim in the grade 11/12 geometry knowledge bites and the
     2024/2025 paper2.json past papers — must NOT be flagged.
  2. Real mojibake (UTF-8 bytes mis-decoded as cp1252) — including samples
     that the old blunt substring signatures matched — MUST still be
     flagged.  Every mojibake sample is generated mechanically by
     round-tripping clean UTF-8 through the cp1252 mis-decode, so the tests
     encode the corruption mechanism rather than hand-picked strings.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -v
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check_mojibake  # noqa: E402


def mangle(clean: str) -> str:
    """Reproduce the guarded-against corruption: UTF-8 bytes read as cp1252.

    The five bytes strict cp1252 leaves undefined (81, 8D, 8F, 90, 9D) are
    passed through as C1 controls, matching how real-world cp1252 readers
    (and the checker's residue table) treat them.
    """
    out = []
    for b in clean.encode("utf-8"):
        try:
            out.append(bytes([b]).decode("cp1252"))
        except UnicodeDecodeError:
            out.append(chr(b))
    return "".join(out)


def mangle_latin1(clean: str) -> str:
    """The other mis-decode seen in the wild: UTF-8 bytes read as latin-1.

    Unlike cp1252, latin-1 maps every 0x80-0x9F byte to the C1 control of
    the same value, so e.g. an em-dash (E2 80 94) becomes a-circumflex +
    U+0080 + U+0094 with no euro sign in sight.  The checker must catch
    this rendering too.
    """
    return clean.encode("utf-8").decode("latin-1")


# Verbatim lines (or their load-bearing fragments) from the ten curriculum
# files that the old bare-substring signatures false-positived on.
LEGIT_DBE_LINES = [
    # knowledge_bites .../dbe-maths-g12-p2-2024-nov-q9-1/question.md
    "Â1 = 40°",
    "Exterior angle of a cyclic quadrilateral: DĈE = Â (whole) = 86°; "
    "so Â1 = 86° - 46° = 40°.",
    # .../dbe-maths-g12-p2-2024-nov-q9-2/question.md
    "Â1 = ½B̂, Â2 = 46°, Ĉ1 = 86°; from Q9.1, Â1 = 40°",
    "B̂ = 80° [Â1 = ½B̂]; Ĉ2 = Â1 = 40°; AD = DC",
    # .../dbe-maths-g12-p2-2025-nov-q8-4/question.md and 2025/paper2.json
    "If AB = BK, calculate the size of KÂC.",
    "KÂC = 80,60°",
    "cosine rule: KC^2 = AK^2 + AC^2 - 2.AK.AC cos KÂC",
    # .../dbe-maths-g12-p2-2024-nov-q11-1/question.md and 2024/paper2.json
    "D̂1 = EÂG = x [tan-chord theorem]; AF̂G = EÂG = x",
    "Â3 = Â2 [sum of angles in triangle]; therefore ΔAGF ||| ΔABC [AAA]",
    "ΔACD ||| ΔAGF — common Â3, AF̂G = D̂1 = x",
    # 2025/paper2.json memo_note (q4-8 area)
    "tan MÂB = 4/3 -> MÂB = 53,13°, AM̂D = 36,87°, "
    "MÂC = 90° (tangent ⊥ radius)",
]

# Clean strings whose cp1252 mis-decode must be caught.  This test file is
# itself inside the scanner's lessons/** glob, so the corrupted forms are
# produced at runtime by mangle() and never written literally; the residue
# byte pairs are named in hex only: the E2 80 xx punctuation family, C3 A9
# (e-acute), C2 A0 (the NBSP in "hard\u00a0space"), C2 B0 (degree sign),
# C2 BD (one-half) and E2 82 AC (euro sign).
MOJIBAKE_SOURCES = [
    "em—dash and ‘curly’ “quotes”…",
    "café résumé",
    "hard space",
    "temperature 25°C",
    "½ of the angle",
    "São Paulo über Öl",
    "price €99",
]


class SignatureTests(unittest.TestCase):
    """Direction checks on the compiled signature regex."""

    def test_legit_dbe_notation_passes(self):
        for line in LEGIT_DBE_LINES:
            with self.subTest(line=line):
                self.assertIsNone(
                    check_mojibake.MOJIBAKE_RE.search(line),
                    f"false positive on legitimate DBE notation: {line!r}",
                )

    def test_real_mojibake_still_fails(self):
        for clean in MOJIBAKE_SOURCES:
            mangled = mangle(clean)
            with self.subTest(mangled=mangled):
                self.assertNotEqual(clean, mangled)
                self.assertIsNotNone(
                    check_mojibake.MOJIBAKE_RE.search(mangled),
                    f"missed real mojibake: {mangled!r}",
                )

    def test_latin1_mangled_mojibake_still_fails(self):
        # A latin-1 mis-read renders 0x80-0x9F continuation bytes as C1
        # controls rather than cp1252 punctuation; both renderings must trip
        # the checker.  "École" is the sharpest case: latin-1 gives A-tilde
        # + U+0089, which the old bare-substring signatures caught and a
        # cp1252-only residue table would miss.
        for clean in MOJIBAKE_SOURCES + ["École", "em—dash", "CO₂"]:
            mangled = mangle_latin1(clean)
            with self.subTest(mangled=mangled):
                self.assertNotEqual(clean, mangled)
                self.assertIsNotNone(
                    check_mojibake.MOJIBAKE_RE.search(mangled),
                    f"missed latin-1-rendered mojibake: {mangled!r}",
                )

    def test_mangled_dbe_notation_still_fails(self):
        # Even the DBE lines themselves, if corrupted, must be caught.
        for line in LEGIT_DBE_LINES:
            mangled = mangle(line)
            with self.subTest(mangled=mangled):
                self.assertIsNotNone(
                    check_mojibake.MOJIBAKE_RE.search(mangled),
                    f"missed mangled DBE line: {mangled!r}",
                )


class CheckFileTests(unittest.TestCase):
    """End-to-end behaviour of check_file on real temp files."""

    def _write(self, tmp, name, text):
        p = Path(tmp) / name
        p.write_text(text, encoding="utf-8")
        return p

    def test_clean_dbe_file_has_no_hits(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = self._write(tmp, "question.md", "\n".join(LEGIT_DBE_LINES) + "\n")
            self.assertEqual(check_mojibake.check_file(p), [])

    def test_mojibake_file_reports_line_numbers(self):
        with tempfile.TemporaryDirectory() as tmp:
            body = "clean line one\n" + mangle(MOJIBAKE_SOURCES[0]) + "\nclean line three\n"
            p = self._write(tmp, "question.md", body)
            hits = check_mojibake.check_file(p)
            self.assertEqual([n for n, _ in hits], [2])

    def test_invalid_utf8_file_still_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "bad.md"
            p.write_bytes(b"lone continuation byte \xa0\n")
            self.assertEqual(check_mojibake.check_file(p), [(0, "<file is not valid UTF-8>")])

    def test_repo_curriculum_files_previously_flagged_now_pass(self):
        repo_root = Path(__file__).resolve().parents[4]
        previously_flagged = [
            "lessons/curriculum/CAPS/maths/knowledge_bites/grade11/"
            "cyclic-quadrilaterals-and-tangents/dbe-maths-g12-p2-2024-nov-q9-1/question.md",
            "lessons/curriculum/CAPS/maths/knowledge_bites/grade11/"
            "the-cosine-rule-and-2d-problems/dbe-maths-g12-p2-2025-nov-q8-4/question.md",
            "lessons/curriculum/CAPS/past_papers/maths/grade12/2024/paper2.json",
            "lessons/curriculum/CAPS/past_papers/maths/grade12/2025/paper2.json",
        ]
        for rel in previously_flagged:
            p = repo_root / rel
            if not p.is_file():
                continue  # tolerate curriculum reshuffles; direction 1 is covered above
            with self.subTest(file=rel):
                self.assertEqual(check_mojibake.check_file(p), [])


if __name__ == "__main__":
    unittest.main()
