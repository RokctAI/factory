#!/usr/bin/env python3
# Licensed under the MIT License.
# Copyright 2026 RokctAI
"""Unit tests for lessons/scripts/regen_denied.py (stdlib unittest).

Covers the post-junior-tree-retirement data shape (2026-08): the pipeline
requeue branch is gone — lessons/review_index.json lists session packages
only, and a denied lesson is regenerated via a session brief in
lessons/reviews/regen/. A stray index entry claiming source "pipeline" is
warned about and skipped, never queued.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/tests -v
"""

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import regen_denied  # noqa: E402

PATCHED_GLOBALS = (
    "REPO_ROOT",
    "REVIEWS_DIR",
    "REGEN_DIR",
    "STATE_PATH",
    "INDEX_PATH",
)

SESSION_ID = "session_maths_g11_t1_quadratic-equations_factoring-method"

SESSION_ENTRY = {
    "id": SESSION_ID,
    "source": "session",
    "subject": "maths",
    "grade": 11,
    "term": 1,
    "topic": "Quadratic equations",
    "subtopic": "Factoring method",
    "package_path": (
        "lessons/curriculum/CAPS/maths/session/grade11/term1/"
        "quadratic-equations/factoring-method"
    ),
    "produced": False,
    "assets": None,
    "review": {"status": "pending", "reason": None, "reviewed_at": None},
}


class RegenDeniedTests(unittest.TestCase):
    def setUp(self):
        self._saved = {
            name: getattr(regen_denied, name) for name in PATCHED_GLOBALS
        }
        self.addCleanup(self._restore_globals)
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        regen_denied.REPO_ROOT = root
        regen_denied.REVIEWS_DIR = root / "lessons" / "reviews"
        regen_denied.REGEN_DIR = regen_denied.REVIEWS_DIR / "regen"
        regen_denied.STATE_PATH = regen_denied.REVIEWS_DIR / "regen_state.json"
        regen_denied.INDEX_PATH = root / "lessons" / "review_index.json"
        regen_denied.REVIEWS_DIR.mkdir(parents=True)
        self.write_index([SESSION_ENTRY])

    def _restore_globals(self):
        for name, value in self._saved.items():
            setattr(regen_denied, name, value)

    # --- fixtures -----------------------------------------------------------

    def write_index(self, lessons):
        regen_denied.INDEX_PATH.write_text(
            json.dumps(
                {
                    "version": 1,
                    "generated_at": "2026-08-14T00:00:00Z",
                    "lessons": lessons,
                }
            )
            + "\n",
            encoding="utf-8",
        )

    def write_review(self, lesson_id, status, reason=None,
                     reviewed_at="2026-08-14T08:00:00Z"):
        (regen_denied.REVIEWS_DIR / f"{lesson_id}.json").write_text(
            json.dumps(
                {
                    "lesson_id": lesson_id,
                    "status": status,
                    "reason": reason,
                    "reviewed_by": "RendaniSinyage",
                    "reviewed_at": reviewed_at,
                }
            )
            + "\n",
            encoding="utf-8",
        )

    def run_main(self):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = regen_denied.main()
        self.assertEqual(code, 0)
        return out.getvalue(), err.getvalue()

    def read_state(self):
        return json.loads(
            regen_denied.STATE_PATH.read_text(encoding="utf-8")
        )["lessons"]

    # --- session lessons: brief-queue behaviour -----------------------------

    def test_denied_session_lesson_writes_brief(self):
        self.write_review(SESSION_ID, "denied", reason="Intro too abstract")
        out, err = self.run_main()
        brief_path = regen_denied.REGEN_DIR / f"{SESSION_ID}.md"
        self.assertTrue(brief_path.is_file())
        brief = brief_path.read_text(encoding="utf-8")
        self.assertIn("Intro too abstract", brief)
        self.assertIn(SESSION_ENTRY["package_path"], brief)
        self.assertIn(f"queued session regen: {SESSION_ID}", out)
        self.assertNotIn("warning", err)
        self.assertEqual(self.read_state()[SESSION_ID]["attempts"], 1)

    def test_approved_review_clears_state_and_brief(self):
        self.write_review(SESSION_ID, "denied", reason="Fix the MCQ key",
                          reviewed_at="2026-08-14T08:00:00Z")
        self.run_main()
        self.write_review(SESSION_ID, "approved",
                          reviewed_at="2026-08-14T09:00:00Z")
        self.run_main()
        self.assertNotIn(SESSION_ID, self.read_state())
        self.assertFalse(
            (regen_denied.REGEN_DIR / f"{SESSION_ID}.md").is_file()
        )

    def test_repeat_denials_bound_attempts_then_park(self):
        self.write_review(SESSION_ID, "denied", reason="First denial",
                          reviewed_at="2026-08-14T08:00:00Z")
        self.run_main()
        self.write_review(SESSION_ID, "denied", reason="Second denial",
                          reviewed_at="2026-08-14T09:00:00Z")
        self.run_main()
        self.assertEqual(self.read_state()[SESSION_ID]["attempts"], 2)

        # Third denial exceeds MAX_ATTEMPTS: parked, brief removed, nothing
        # queued.
        self.write_review(SESSION_ID, "denied", reason="Third denial",
                          reviewed_at="2026-08-14T10:00:00Z")
        out, _ = self.run_main()
        self.assertIn("parked", out)
        self.assertTrue(self.read_state()[SESSION_ID]["parked"])
        self.assertFalse(
            (regen_denied.REGEN_DIR / f"{SESSION_ID}.md").is_file()
        )

    def test_rerun_on_same_denial_is_noop(self):
        self.write_review(SESSION_ID, "denied", reason="Needs rework")
        self.run_main()
        state_before = self.read_state()
        out, _ = self.run_main()
        self.assertIn("regen_state.json unchanged", out)
        self.assertEqual(self.read_state(), state_before)

    # --- retired pipeline path: warn and skip, never queue ------------------

    def test_pipeline_source_entry_warns_and_skips(self):
        pipeline_id = "maths_g11_quadratic_equations_factoring_method_31d165"
        self.write_index([
            SESSION_ENTRY,
            {**SESSION_ENTRY, "id": pipeline_id, "source": "pipeline"},
        ])
        self.write_review(pipeline_id, "denied", reason="Denied")
        out, err = self.run_main()
        self.assertIn("source 'pipeline'", err)
        self.assertIn("retired", err)
        self.assertIn("regen_state.json unchanged", out)
        self.assertFalse(
            (regen_denied.REGEN_DIR / f"{pipeline_id}.md").is_file()
        )

    # --- unknown lessons: warn, queue nothing, keep state retryable ---------

    def test_denied_lesson_without_index_entry_not_queued(self):
        self.write_review("ghost_lesson_000000", "denied", reason="Denied")
        out, err = self.run_main()
        self.assertIn("not in review_index.json", err)
        self.assertIn("regen_state.json unchanged", out)
        self.assertFalse(regen_denied.STATE_PATH.is_file() and
                         self.read_state())


if __name__ == "__main__":
    unittest.main()
