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

"""Unit tests for lessons/scripts/IEB/release_on_complete.py (stdlib unittest).

The point under test is release identity: IEB mirror packages reuse the SAME
lesson_id values as their CAPS twins by design, so the IEB release script
must prefix its release identity with `ieb_` (tag `lesson-ieb_<lesson_id>`)
or every IEB release would collide with the CAPS tag and be idempotently
skipped. On-disk package lesson_ids stay untouched — only the release
tooling discriminates.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/IEB/tests -v
"""

import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import release_on_complete as roc  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[4]

REL_PACKAGE = ("maths/session/grade11/term1/"
               "quadratic-equations/factoring-method")
CAPS_TWIN_LESSON_ID = "maths_g11_quadratic-equations_factoring-method"


class ReleaseIdentityTests(unittest.TestCase):
    """The ieb_ prefix on derived release identity."""

    def make_package_path(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        folder = root / REL_PACKAGE
        folder.mkdir(parents=True)
        return folder, root

    def test_release_identity_carries_ieb_prefix(self):
        folder, root = self.make_package_path()
        ident = roc.lesson_identity(folder, root)
        self.assertEqual(ident["id"], f"ieb_{CAPS_TWIN_LESSON_ID}")
        self.assertEqual(ident["tag"], f"lesson-ieb_{CAPS_TWIN_LESSON_ID}")
        self.assertTrue(ident["tag"].startswith("lesson-ieb_"))

    def test_non_identity_fields_carry_unchanged(self):
        # Only the release identity is prefixed; the path-derived metadata
        # (including the #52 knowledge-bite join key) stays CAPS-identical.
        folder, root = self.make_package_path()
        ident = roc.lesson_identity(folder, root)
        self.assertEqual(ident["subject_key"], "maths")
        self.assertEqual(ident["grade"], 11)
        self.assertEqual(ident["lesson_slug"], "factoring-method")
        self.assertEqual(ident["topic"], "Quadratic Equations")

    def test_caps_twin_lesson_id_does_not_collide(self):
        # The same package path (IEB mirrors reuse CAPS lesson_ids
        # byte-identically) must yield a DIFFERENT tag than the CAPS
        # machinery derives, or the idempotent skip would drop the release.
        folder, root = self.make_package_path()
        caps_ident = roc._caps_lesson_identity(folder, root)
        ieb_ident = roc.lesson_identity(folder, root)
        self.assertEqual(caps_ident["id"], CAPS_TWIN_LESSON_ID)
        self.assertNotEqual(ieb_ident["tag"], caps_ident["tag"])
        self.assertEqual(ieb_ident["id"], "ieb_" + caps_ident["id"])
        self.assertEqual(ieb_ident["tag"], "lesson-ieb_" + caps_ident["id"])


class SessionRootTests(unittest.TestCase):
    """The script targets the IEB session tree, not the CAPS one."""

    def test_session_root_is_ieb_tree(self):
        self.assertEqual(roc.SESSION_ROOT, Path("lessons/curriculum/IEB"))

    def test_caps_module_root_differs(self):
        # The imported CAPS implementation keeps its own default until
        # main() parameterizes a run — and it is not the IEB root.
        self.assertNotEqual(roc.SESSION_ROOT,
                            Path("lessons/curriculum/CAPS"))


class MainScanTests(unittest.TestCase):
    """main() end-to-end in --dry-run: IEB root default, ieb_ tags."""

    def setUp(self):
        # main() parameterizes the shared CAPS module in place; restore it
        # so these tests leave the imported module pristine.
        self._saved = {
            "SESSION_ROOT": roc.caps.SESSION_ROOT,
            "lesson_identity": roc.caps.lesson_identity,
        }
        self.addCleanup(self._restore)
        # Keep dry-run offline: no gh CLI means no release-existence calls.
        self._which = roc.caps.shutil.which
        roc.caps.shutil.which = lambda _name: None
        self.addCleanup(self._restore_which)

    def _restore(self):
        for name, value in self._saved.items():
            setattr(roc.caps, name, value)

    def _restore_which(self):
        roc.caps.shutil.which = self._which

    def run_main(self, argv):
        saved_argv = sys.argv
        sys.argv = ["release_on_complete.py"] + argv
        out = io.StringIO()
        try:
            with redirect_stdout(out), redirect_stderr(out):
                code = roc.main()
        finally:
            sys.argv = saved_argv
        return code, out.getvalue()

    def test_default_root_scans_ieb_session_tree(self):
        saved_cwd = os.getcwd()
        self.addCleanup(os.chdir, saved_cwd)
        os.chdir(REPO_ROOT)
        code, out = self.run_main(["--dry-run"])
        self.assertEqual(code, 0)
        self.assertIn(f"under {Path('lessons/curriculum/IEB')}", out)
        self.assertNotIn("curriculum/CAPS", out)

    def test_dry_run_derives_ieb_tags(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        folder = root / REL_PACKAGE
        folder.mkdir(parents=True)
        for name in roc.caps.REQUIRED_FILES + (roc.caps.AUDIO_FILE,):
            (folder / name).write_text("", encoding="utf-8")
        code, out = self.run_main(["--dry-run", "--root", str(root)])
        self.assertEqual(code, 0)
        self.assertIn(f"lesson-ieb_{CAPS_TWIN_LESSON_ID}", out)
        # The unprefixed CAPS tag must never appear for an IEB package.
        self.assertNotIn(f"lesson-{CAPS_TWIN_LESSON_ID}",
                         out.replace(f"lesson-ieb_{CAPS_TWIN_LESSON_ID}", ""))


if __name__ == "__main__":
    unittest.main()
