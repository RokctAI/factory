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

"""Unit tests for the standing-clip event emitters in
lessons/scripts/CAPS/lesson_manifest.py (stdlib unittest).

Covers the framing-as-events contract (decisions #7/#9/#38/#39/#40): the
assistant_opening / handover pair at session start, clip refs on
profile/signoff/break_start, the timekeeping assistant_interjection set
(five_min_warning per tutor block, halfway on single-voice lessons only,
wrap_up at lesson end), the assistant_signoff + recording_stopped close, the
manifest-level clips table, and the never-both-tutors acknowledgement rule.
Also pins that a call WITHOUT a standing-clip plan still emits exactly the
legacy seven-type vocabulary, so pre-plan callers are unaffected.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -v
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import lesson_manifest  # noqa: E402
import lesson_pipeline  # noqa: E402

FIRST = {"id": "tutor_001", "display_name": "Test Expert"}
SECOND = {"id": "tutor_002", "display_name": "Test Simplifier"}

SUBTOPICS = {"subtopics": [
    {"ref": "subtopic_1", "title": "One", "start_seconds": 0, "end_seconds": 300},
    {"ref": "subtopic_2", "title": "Two", "start_seconds": 300, "end_seconds": 600},
    {"ref": "subtopic_3", "title": "Three", "start_seconds": 600, "end_seconds": 900},
    {"ref": "subtopic_4", "title": "Four", "start_seconds": 900, "end_seconds": 1200},
]}

LEGACY_TYPES = {"topic_display", "profile", "subtopic_start", "subtopic_end",
                "break_start", "comprehension_check", "signoff"}

PLAN = {"assistant": "assistant_003",
        "greeting": "tutor_001/greetings/02",
        "signoff": "tutor_001/signoffs/01",
        "ack_first": "tutor_001/acknowledgements/01",
        "ack_second": ""}


def tracks(second=SECOND, split_ref="subtopic_3", plan=PLAN, audio=1200.0):
    return lesson_manifest.build_tracks(
        SUBTOPICS, {}, {}, FIRST, second, 1.0, audio, "Topic", 4.0,
        split_ref=split_ref, grade=12, standing_clips=plan)


def by_type(evs, t):
    return [e for e in evs if e["type"] == t]


class OpeningTests(unittest.TestCase):
    def test_assistant_opening_then_handover_lead_the_track(self):
        evs = tracks()
        self.assertEqual(evs[0]["type"], "assistant_opening")
        self.assertEqual(evs[0]["time"], 0)
        self.assertEqual(evs[0]["assistant"], "assistant_003")
        self.assertEqual(evs[0]["duration_seconds"],
                         lesson_manifest.ASSISTANT_OPENING_SECONDS)
        # Both intro variants are offered; the APP picks new vs returning
        # (it knows the attendance history — decision #39).
        self.assertEqual(evs[0]["clips"],
                         {"new": "assistant_003/intro/new",
                          "returning": "assistant_003/intro/returning"})
        self.assertEqual(evs[1]["type"], "handover")
        self.assertEqual(evs[1]["from"], "assistant_003")
        self.assertEqual(evs[1]["to"], "tutor_001")

    def test_profile_carries_clip_and_keeps_audio(self):
        (profile,) = by_type(tracks(), "profile")
        self.assertEqual(profile["clip"], "tutor_001/greetings/02")
        self.assertEqual(profile["audio"], "audio.mp3")  # deployed field kept

    def test_signoff_carries_clip_and_keeps_audio(self):
        (signoff,) = by_type(tracks(), "signoff")
        self.assertEqual(signoff["clip"], "tutor_001/signoffs/01")
        self.assertEqual(signoff["audio"], "audio.mp3")


class InterjectionTests(unittest.TestCase):
    def test_five_min_warning_per_block_two_part(self):
        warns = [e for e in by_type(tracks(), "assistant_interjection")
                 if e["kind"] == "five_min_warning"]
        self.assertEqual(len(warns), 2)
        # Blocks end at the break (600, the boundary before subtopic_3
        # where the second tutor takes over) and at lesson end (1200); the
        # warning lands five minutes before each.
        self.assertEqual([w["time"] for w in warns], [300.0, 900.0])
        for w in warns:
            self.assertEqual(w["clip"],
                             "assistant_003/timekeeping/five_min_warning")

    def test_ack_on_first_block_only_never_both(self):
        warns = [e for e in by_type(tracks(), "assistant_interjection")
                 if e["kind"] == "five_min_warning"]
        self.assertEqual(warns[0].get("ack_clip"),
                         "tutor_001/acknowledgements/01")
        self.assertEqual(warns[0].get("ack_tutor"), "tutor_001")
        self.assertNotIn("ack_clip", warns[1])

    def test_halfway_only_on_single_voice(self):
        two_part = by_type(tracks(), "assistant_interjection")
        self.assertEqual([e for e in two_part if e["kind"] == "halfway"], [])
        single = by_type(tracks(second=None, split_ref=None),
                         "assistant_interjection")
        halfway = [e for e in single if e["kind"] == "halfway"]
        self.assertEqual(len(halfway), 1)
        self.assertEqual(halfway[0]["time"], 600.0)
        self.assertEqual(halfway[0]["clip"],
                         "assistant_003/timekeeping/halfway")

    def test_wrap_up_at_lesson_end_before_signoff(self):
        evs = tracks()
        wrap = [e for e in by_type(evs, "assistant_interjection")
                if e["kind"] == "wrap_up"]
        self.assertEqual(len(wrap), 1)
        self.assertEqual(wrap[0]["time"], 1200.0)
        self.assertLess(evs.index(wrap[0]),
                        evs.index(by_type(evs, "signoff")[0]))


class CloseTests(unittest.TestCase):
    def test_host_closes_then_marks_the_recording_cut(self):
        evs = tracks()
        self.assertEqual(evs[-2]["type"], "assistant_signoff")
        self.assertEqual(evs[-2]["clip"], "assistant_003/signoff/session_end")
        self.assertEqual(evs[-1]["type"], "recording_stopped")
        self.assertEqual(evs[-1]["clip"],
                         "assistant_003/signoff/recording_stopped")
        self.assertEqual(evs[-1]["time"], 1200.0)

    def test_break_start_carries_handover_clips(self):
        (brk,) = by_type(tracks(), "break_start")
        self.assertEqual(brk["clips"],
                         {"into_break": "assistant_003/handover/into_break",
                          "out_of_break": "assistant_003/handover/out_of_break"})


class LegacyShapeTests(unittest.TestCase):
    def test_no_plan_emits_exactly_the_legacy_vocabulary(self):
        evs = lesson_manifest.build_tracks(
            SUBTOPICS, {}, {}, FIRST, SECOND, 1.0, 1200.0, "Topic", 4.0,
            split_ref="subtopic_3", grade=12)
        self.assertTrue({e["type"] for e in evs} <= LEGACY_TYPES)
        for e in evs:
            self.assertNotIn("clip", e)
            self.assertNotIn("clips", e)

    def test_no_host_suppresses_assistant_events_keeps_tutor_clips(self):
        plan = dict(PLAN, assistant=None)
        evs = tracks(plan=plan)
        self.assertTrue({e["type"] for e in evs} <= LEGACY_TYPES)
        (profile,) = by_type(evs, "profile")
        self.assertEqual(profile["clip"], "tutor_001/greetings/02")


class ClipTableTests(unittest.TestCase):
    def test_table_resolves_team_layout_and_dedupes(self):
        table = lesson_manifest.collect_clip_table(tracks())
        self.assertEqual(table["tutor_001/greetings/02"],
                         {"speaker": "tutor_001",
                          "script": "tutors/CAPS/tutor_001/greetings/02.md"})
        self.assertEqual(table["assistant_003/intro/new"],
                         {"speaker": "assistant_003",
                          "script": "assistants/CAPS/assistant_003/intro/new.md"})
        # Every clip the tracks name is in the table, exactly once.
        named = set()
        for ev in tracks():
            for ref in [ev.get("clip"), ev.get("ack_clip"),
                        *(ev.get("clips") or {}).values()]:
                if ref:
                    named.add(ref)
        self.assertEqual(set(table), named)

    def test_empty_without_clips(self):
        evs = lesson_manifest.build_tracks(
            SUBTOPICS, {}, {}, FIRST, None, 1.0, 1200.0, "Topic", 4.0)
        self.assertEqual(lesson_manifest.collect_clip_table(evs), {})


class ResolvePlanTests(unittest.TestCase):
    def _seed_tutor_assets(self, root):
        for tid in ("tutor_001", "tutor_002"):
            for kind, n in (("greetings", 6), ("signoffs", 3),
                            ("acknowledgements", 2)):
                d = root / tid / kind
                d.mkdir(parents=True)
                for i in range(1, n + 1):
                    (d / f"{i:02d}.md").write_text("Standing line.",
                                                   encoding="utf-8")

    def test_card_refs_pass_through_extensionless(self):
        plan = lesson_manifest.resolve_standing_clips(
            "sess", FIRST, SECOND, 12,
            greeting_ref="tutor_001/greetings/03.md",
            signoff_ref="tutor_001/signoffs/02.md",
            ack_ref="tutor_001/acknowledgements/01.md")
        self.assertEqual(plan["assistant"], "assistant_003")
        self.assertEqual(plan["greeting"], "tutor_001/greetings/03")
        self.assertEqual(plan["signoff"], "tutor_001/signoffs/02")
        self.assertEqual(plan["ack_first"], "tutor_001/acknowledgements/01")
        self.assertEqual(plan["ack_second"], "")

    def test_empty_card_ack_means_silent_not_derived(self):
        plan = lesson_manifest.resolve_standing_clips(
            "sess", FIRST, SECOND, 12,
            greeting_ref="tutor_001/greetings/03.md",
            signoff_ref="tutor_001/signoffs/02.md", ack_ref="")
        self.assertEqual(plan["ack_first"], "")
        self.assertEqual(plan["ack_second"], "")

    def test_derivation_is_deterministic_and_never_both_acks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._seed_tutor_assets(root)
            saved = lesson_pipeline.TUTORS_DIR
            lesson_pipeline.TUTORS_DIR = root
            try:
                plans = [lesson_manifest.resolve_standing_clips(
                    f"session_{i}", FIRST, SECOND, 12) for i in range(24)]
                again = lesson_manifest.resolve_standing_clips(
                    "session_0", FIRST, SECOND, 12)
            finally:
                lesson_pipeline.TUTORS_DIR = saved
        self.assertEqual(plans[0], again)  # re-runs never reshuffle
        for plan in plans:
            self.assertTrue(plan["greeting"].startswith("tutor_001/greetings/"))
            self.assertTrue(plan["signoff"].startswith("tutor_001/signoffs/"))
            # RARE and never both tutors of one lesson (decision #38).
            self.assertFalse(plan["ack_first"] and plan["ack_second"])
        acked = sum(1 for p in plans if p["ack_first"] or p["ack_second"])
        self.assertLess(acked, len(plans))  # about 1 in ACK_ONE_IN, not all

    def test_gradeless_lesson_has_no_host(self):
        plan = lesson_manifest.resolve_standing_clips(
            "sess", FIRST, None, 0,
            greeting_ref="tutor_001/greetings/01.md",
            signoff_ref="tutor_001/signoffs/01.md", ack_ref="")
        self.assertIsNone(plan["assistant"])


if __name__ == "__main__":
    unittest.main()
