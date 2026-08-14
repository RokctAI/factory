#!/usr/bin/env python3
# Licensed under the MIT License.
# Copyright 2026 RokctAI
"""Unit tests for lessons/scripts/regen_denied.py (stdlib unittest).

Covers the post-PR-#86 data shape: lessons/review_index.json lists session
packages only, so a denied pipeline lesson is recognised by its job card in
.rokct/agent/jobs/ (its review file is named after the job-card id), not by
a "source": "pipeline" index entry.

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
    "JOBS_ROOT",
)

PIPELINE_ID = "maths_g11_quadratic_equations_factoring_method_31d165"
SESSION_ID = "session_maths_g11_t1_quadratic-equations_factoring-method"

CARD_TEMPLATE = """\
---
id: {lesson_id}
theme: Maths Grade 11: Quadratic equations - Factoring method
type: lesson.maths
subject: Maths
grade: 11
term: 1
topic: Quadratic equations
subtopic: Factoring method
status: done
concept_status: approved
created: 2026-07-27
last_updated: 2026-07-27
attempts: 0
---
"""

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
        regen_denied.JOBS_ROOT = root / ".rokct" / "agent" / "jobs"
        regen_denied.REVIEWS_DIR.mkdir(parents=True)
        for queue in regen_denied.JOB_QUEUES:
            (regen_denied.JOBS_ROOT / queue).mkdir(parents=True)
        self.write_index([])  # post-#86 default: no pipeline entries

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

    def write_card(self, queue, lesson_id):
        path = regen_denied.JOBS_ROOT / queue / f"{lesson_id[:-7]}_card.md"
        path.write_text(
            CARD_TEMPLATE.format(lesson_id=lesson_id), encoding="utf-8"
        )
        return path

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

    # --- pipeline lessons (post-#86: identified by job card, not index) -----

    def test_denied_pipeline_lesson_requeues_card(self):
        card_path = self.write_card("done", PIPELINE_ID)
        self.write_review(PIPELINE_ID, "denied", reason="Part 2 too shallow")
        out, err = self.run_main()

        self.assertFalse(card_path.is_file())  # moved out of done/
        pending = regen_denied.JOBS_ROOT / "pending" / card_path.name
        self.assertTrue(pending.is_file())
        card = pending.read_text(encoding="utf-8")
        self.assertEqual(
            regen_denied.get_field(card, "status"), regen_denied.REENTRY_STATUS
        )
        self.assertEqual(regen_denied.get_field(card, "concept_status"), "pending")
        self.assertIn("review_feedback: |", card)
        self.assertIn("Part 2 too shallow", card)
        self.assertIn("attempt 1 of 2", card)
        self.assertIn(f"queued pipeline regen: {PIPELINE_ID}", out)
        self.assertNotIn("warning", err)
        state = self.read_state()
        self.assertEqual(state[PIPELINE_ID]["attempts"], 1)
        self.assertFalse(state[PIPELINE_ID]["parked"])

    def test_denied_pipeline_card_already_pending_stays_pending(self):
        card_path = self.write_card("pending", PIPELINE_ID)
        self.write_review(PIPELINE_ID, "denied", reason="Wrong worked example")
        self.run_main()
        card = card_path.read_text(encoding="utf-8")
        self.assertEqual(
            regen_denied.get_field(card, "status"), regen_denied.REENTRY_STATUS
        )
        self.assertIn("Wrong worked example", card)

    def test_repeat_denials_bound_attempts_then_park(self):
        card_path = self.write_card("done", PIPELINE_ID)
        self.write_review(PIPELINE_ID, "denied", reason="First denial",
                          reviewed_at="2026-08-14T08:00:00Z")
        self.run_main()
        self.write_review(PIPELINE_ID, "denied", reason="Second denial",
                          reviewed_at="2026-08-14T09:00:00Z")
        self.run_main()
        self.assertEqual(self.read_state()[PIPELINE_ID]["attempts"], 2)

        # Third denial exceeds MAX_ATTEMPTS: parked, card left untouched.
        pending = regen_denied.JOBS_ROOT / "pending" / card_path.name
        before = pending.read_text(encoding="utf-8")
        self.write_review(PIPELINE_ID, "denied", reason="Third denial",
                          reviewed_at="2026-08-14T10:00:00Z")
        out, _ = self.run_main()
        self.assertIn("parked", out)
        self.assertTrue(self.read_state()[PIPELINE_ID]["parked"])
        self.assertEqual(pending.read_text(encoding="utf-8"), before)

    def test_rerun_on_same_denial_is_noop(self):
        self.write_card("done", PIPELINE_ID)
        self.write_review(PIPELINE_ID, "denied", reason="Needs rework")
        self.run_main()
        state_before = self.read_state()
        out, _ = self.run_main()
        self.assertIn("regen_state.json unchanged", out)
        self.assertEqual(self.read_state(), state_before)

    # --- session lessons (indexed) keep their brief-queue behaviour ---------

    def test_denied_session_lesson_writes_brief(self):
        self.write_index([SESSION_ENTRY])
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
        self.write_index([SESSION_ENTRY])
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

    # --- unknown lessons: warn, queue nothing, keep state retryable ---------

    def test_denied_lesson_without_card_or_index_entry_not_queued(self):
        self.write_review("ghost_lesson_000000", "denied", reason="Denied")
        out, err = self.run_main()
        self.assertIn("no job card or session index entry", err)
        self.assertIn("regen_state.json unchanged", out)
        self.assertFalse(regen_denied.STATE_PATH.is_file() and
                         self.read_state())


if __name__ == "__main__":
    unittest.main()
