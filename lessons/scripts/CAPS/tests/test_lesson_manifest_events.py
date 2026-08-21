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

Follow-up coverage: the opening's five minutes are flagged as an ESTIMATE
rather than emitted as a measured `duration_seconds` (and become measured
once the clips carry audio), the handover states that it follows the opening,
the host's standing lines are assigned deterministic variants like the
tutor's, and a clips-table `script` that names no file fails
lesson_compliance R6.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -v
"""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import lesson_compliance  # noqa: E402
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
        # The five minutes are a BUDGET for audio nobody has recorded, so
        # they go out flagged as an estimate and never as a bare
        # `duration_seconds` a consumer would read as measured.
        self.assertEqual(evs[0]["estimated_duration_seconds"],
                         lesson_manifest.ASSISTANT_OPENING_ESTIMATE_SECONDS)
        self.assertEqual(evs[0]["duration_source"], "estimate")
        self.assertNotIn("duration_seconds", evs[0])
        # Both intro variants are offered; the APP picks new vs returning
        # (it knows the attendance history — decision #39).
        self.assertEqual(evs[0]["clips"],
                         {"new": "assistant_003/intro/new",
                          "returning": "assistant_003/intro/returning"})
        self.assertEqual(evs[1]["type"], "handover")
        self.assertEqual(evs[1]["from"], "assistant_003")
        self.assertEqual(evs[1]["to"], "tutor_001")

    def test_handover_states_that_it_follows_the_opening(self):
        # Sharing time 0 with a 300-second opening left the ordering to be
        # inferred; `after` says it outright.
        evs = tracks()
        (hand,) = by_type(evs, "handover")
        self.assertEqual(hand["after"], "assistant_opening")
        self.assertEqual(hand["time"], 0)
        self.assertLess(evs.index(by_type(evs, "assistant_opening")[0]),
                        evs.index(hand))

    def test_no_event_carries_an_unflagged_placeholder_duration(self):
        # Every duration in the track is either measured (derived from the
        # real audio) or explicitly flagged as an estimate.
        for ev in tracks():
            if "estimated_duration_seconds" in ev:
                self.assertEqual(ev["duration_source"], "estimate")
                self.assertNotIn("duration_seconds", ev)

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


class MeasuredDurationTests(unittest.TestCase):
    """An estimate becomes a real duration the moment the clips it names
    carry recorded audio — the upgrade path that makes the estimate flag
    temporary rather than permanent."""

    def _opening(self, evs):
        return by_type(evs, "assistant_opening")[0]

    def test_estimate_survives_an_unrecorded_clip_table(self):
        evs = tracks()
        table = lesson_manifest.collect_clip_table(evs)
        lesson_manifest.apply_measured_clip_durations(evs, table)
        opening = self._opening(evs)
        self.assertEqual(opening["duration_source"], "estimate")
        self.assertNotIn("duration_seconds", opening)

    def test_recorded_clips_replace_the_estimate_with_the_real_length(self):
        evs = tracks()
        table = lesson_manifest.collect_clip_table(evs)
        for ref in self._opening(evs)["clips"].values():
            table[ref]["audio"] = f"{ref}.mp3"
        table["assistant_003/intro/new"]["duration_seconds"] = 41.5
        table["assistant_003/intro/returning"]["duration_seconds"] = 28.25
        lesson_manifest.apply_measured_clip_durations(evs, table)
        opening = self._opening(evs)
        # The app plays exactly one of the two alternatives, so the longer
        # one is the block's real length.
        self.assertEqual(opening["duration_seconds"], 41.5)
        self.assertEqual(opening["duration_source"], "measured")
        self.assertNotIn("estimated_duration_seconds", opening)

    def test_a_partly_recorded_pair_stays_an_estimate(self):
        evs = tracks()
        table = lesson_manifest.collect_clip_table(evs)
        table["assistant_003/intro/new"]["audio"] = "x.mp3"
        table["assistant_003/intro/new"]["duration_seconds"] = 41.5
        lesson_manifest.apply_measured_clip_durations(evs, table)
        opening = self._opening(evs)
        self.assertEqual(opening["duration_source"], "estimate")
        self.assertNotIn("duration_seconds", opening)


class AssistantVariantTests(unittest.TestCase):
    """The host's standing lines vary per lesson the way the tutor's already
    do (assign_ack_variant's "never becomes a tic"), through
    lesson_pipeline's own picker."""

    LINES = ("intro/new", "intro/returning", "timekeeping/five_min_warning",
             "timekeeping/halfway", "timekeeping/wrap_up",
             "handover/into_break", "handover/out_of_break",
             "signoff/session_end", "signoff/recording_stopped")

    def _seed(self, root, n=4):
        for line in self.LINES:
            d = root / "assistant_003" / line
            d.mkdir(parents=True)
            for i in range(1, n + 1):
                (d / f"{i:02d}.md").write_text("Standing line.",
                                               encoding="utf-8")

    def _plan(self, key):
        return lesson_manifest.resolve_standing_clips(
            key, FIRST, SECOND, 12,
            greeting_ref="tutor_001/greetings/01.md",
            signoff_ref="tutor_001/signoffs/01.md", ack_ref="")

    def test_variants_assigned_deterministically_and_vary_by_lesson(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._seed(root)
            saved = lesson_pipeline.ASSISTANTS_DIR
            lesson_pipeline.ASSISTANTS_DIR = root
            try:
                plans = [self._plan(f"session_{i}") for i in range(12)]
                again = self._plan("session_0")
            finally:
                lesson_pipeline.ASSISTANTS_DIR = saved
        self.assertEqual(plans[0], again)  # re-runs never reshuffle
        for plan in plans:
            clips = plan["assistant_clips"]
            self.assertRegex(clips["wrap_up"],
                             r"^assistant_003/timekeeping/wrap_up/\d+$")
            # Two calls of the SAME line in one lesson get different
            # variants — the repeat is what made it a tic.
            self.assertNotEqual(clips["five_min_warning"][0],
                                clips["five_min_warning"][1])
        # Across lessons the line is not always the same recording.
        self.assertGreater(len({p["assistant_clips"]["wrap_up"]
                                for p in plans}), 1)

    def test_no_authored_variants_keeps_the_single_fixed_ref(self):
        with tempfile.TemporaryDirectory() as tmp:
            saved = lesson_pipeline.ASSISTANTS_DIR
            lesson_pipeline.ASSISTANTS_DIR = Path(tmp)
            try:
                plan = self._plan("session_0")
            finally:
                lesson_pipeline.ASSISTANTS_DIR = saved
        self.assertEqual(plan["assistant_clips"]["wrap_up"],
                         "assistant_003/timekeeping/wrap_up")
        self.assertEqual(plan["assistant_clips"]["five_min_warning"],
                         ["assistant_003/timekeeping/five_min_warning"] * 2)

    def test_build_tracks_emits_the_assigned_variants(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._seed(root)
            saved = lesson_pipeline.ASSISTANTS_DIR
            lesson_pipeline.ASSISTANTS_DIR = root
            try:
                plan = self._plan("session_7")
            finally:
                lesson_pipeline.ASSISTANTS_DIR = saved
        evs = tracks(plan=plan)
        warns = [e for e in by_type(evs, "assistant_interjection")
                 if e["kind"] == "five_min_warning"]
        self.assertEqual([w["clip"] for w in warns],
                         plan["assistant_clips"]["five_min_warning"])
        self.assertEqual(by_type(evs, "assistant_signoff")[0]["clip"],
                         plan["assistant_clips"]["session_end"])
        (brk,) = by_type(evs, "break_start")
        self.assertEqual(brk["clips"]["into_break"],
                         plan["assistant_clips"]["into_break"])
        (opening,) = by_type(evs, "assistant_opening")
        self.assertEqual(opening["clips"]["new"],
                         plan["assistant_clips"]["intro_new"])

    def test_a_plan_without_assignments_still_builds(self):
        # PLAN (the card-shaped fixture) carries no `assistant_clips`; the
        # emitter falls back to each line's single fixed ref.
        (wrap,) = [e for e in by_type(tracks(), "assistant_interjection")
                   if e["kind"] == "wrap_up"]
        self.assertEqual(wrap["clip"], "assistant_003/timekeeping/wrap_up")


class ClipScriptResolutionTests(unittest.TestCase):
    """A clips-table `script` is a claim about a file, and the claim is
    checked."""

    def _team(self, tmp):
        root = Path(tmp) / "team"
        (root / "assistants" / "CAPS").mkdir(parents=True)
        (root / "tutors" / "CAPS").mkdir(parents=True)
        return root

    def test_missing_script_is_reported(self):
        table = lesson_manifest.collect_clip_table(tracks())
        with tempfile.TemporaryDirectory() as tmp:
            root = self._team(tmp)
            saved = os.environ.get("TEAM_ROOT")
            os.environ["TEAM_ROOT"] = str(root)
            try:
                missing = lesson_manifest.unresolved_clip_scripts(table)
            finally:
                if saved is None:
                    del os.environ["TEAM_ROOT"]
                else:
                    os.environ["TEAM_ROOT"] = saved
        self.assertEqual({ref for ref, _ in missing}, set(table))

    def test_authored_script_resolves(self):
        table = lesson_manifest.collect_clip_table(tracks())
        with tempfile.TemporaryDirectory() as tmp:
            root = self._team(tmp)
            for entry in table.values():
                path = root / entry["script"]
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("Standing line.", encoding="utf-8")
            saved = os.environ.get("TEAM_ROOT")
            os.environ["TEAM_ROOT"] = str(root)
            try:
                missing = lesson_manifest.unresolved_clip_scripts(table)
            finally:
                if saved is None:
                    del os.environ["TEAM_ROOT"]
                else:
                    os.environ["TEAM_ROOT"] = saved
        self.assertEqual(missing, [])

    def test_no_team_layout_is_unverifiable_not_a_violation(self):
        # Nothing to check against: report nothing rather than flag every
        # ref (the graceful degrade the persona checks already use).
        with tempfile.TemporaryDirectory() as tmp:
            saved_cwd = os.getcwd()
            saved = os.environ.pop("TEAM_ROOT", None)
            os.chdir(tmp)
            try:
                table = lesson_manifest.collect_clip_table(tracks())
                self.assertEqual(
                    lesson_manifest.unresolved_clip_scripts(table), [])
                path, checkable = lesson_manifest.resolve_clip_script(
                    "tutors/CAPS/tutor_001/greetings/02.md")
                self.assertFalse(checkable)
                self.assertIsNone(path)
            finally:
                os.chdir(saved_cwd)
                if saved is not None:
                    os.environ["TEAM_ROOT"] = saved

    def test_legacy_layout_drops_the_caps_segment(self):
        with tempfile.TemporaryDirectory() as tmp:
            saved_cwd = os.getcwd()
            saved = os.environ.pop("TEAM_ROOT", None)
            os.chdir(tmp)
            try:
                Path("lessons/tutors/tutor_001/greetings").mkdir(parents=True)
                Path("lessons/tutors/tutor_001/greetings/02.md").write_text(
                    "Hi.", encoding="utf-8")
                path, checkable = lesson_manifest.resolve_clip_script(
                    "tutors/CAPS/tutor_001/greetings/02.md")
                self.assertTrue(checkable)
                self.assertEqual(
                    path, Path("lessons/tutors/tutor_001/greetings/02.md"))
                self.assertTrue(path.is_file())
            finally:
                os.chdir(saved_cwd)
                if saved is not None:
                    os.environ["TEAM_ROOT"] = saved


class ComplianceClipTableTests(unittest.TestCase):
    """R6: lesson_compliance stops passing a manifest whose clip scripts do
    not resolve."""

    def _manifest(self, tmp, table):
        path = Path(tmp) / "manifest.json"
        path.write_text(json.dumps({"version": "1", "tracks": [],
                                    "clips": table}), encoding="utf-8")
        return path

    def _run(self, table, author):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "team"
            root.mkdir()
            if author:
                for entry in table.values():
                    p = root / entry["script"]
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text("Standing line.", encoding="utf-8")
            else:
                (root / "assistants").mkdir()
            path = self._manifest(tmp, table)
            saved = os.environ.get("TEAM_ROOT")
            os.environ["TEAM_ROOT"] = str(root)
            try:
                return lesson_compliance.check_manifest(path)
            finally:
                if saved is None:
                    del os.environ["TEAM_ROOT"]
                else:
                    os.environ["TEAM_ROOT"] = saved

    def test_dangling_clip_script_is_a_violation(self):
        table = lesson_manifest.collect_clip_table(tracks())
        out = self._run(table, author=False)
        self.assertTrue(out)
        self.assertEqual({rule for rule, _ in out}, {"R6"})
        self.assertEqual(len(out), len(table))

    def test_authored_clip_scripts_pass(self):
        table = lesson_manifest.collect_clip_table(tracks())
        self.assertEqual(self._run(table, author=True), [])

    def test_entry_without_a_script_path_is_a_violation(self):
        out = self._run({"assistant_003/intro/new": {"speaker":
                                                     "assistant_003"}},
                        author=False)
        self.assertEqual([rule for rule, _ in out], ["R6"])

    def test_manifest_without_a_clips_table_is_unaffected(self):
        self.assertEqual(self._run({}, author=False), [])

    def test_r6_is_reported_as_a_failing_rule(self):
        self.assertIn("R6", lesson_compliance.RULE_TITLES)


class PlanHygieneTests(unittest.TestCase):
    def test_repeated_calls_do_not_grow_sys_path(self):
        # The module-level import guard owns sys.path; a per-call insert
        # made the list grow without bound across a batch run.
        lesson_manifest.resolve_standing_clips(
            "warmup", FIRST, SECOND, 12, greeting_ref="tutor_001/greetings/01.md",
            signoff_ref="tutor_001/signoffs/01.md", ack_ref="")
        before = len(sys.path)
        for i in range(25):
            lesson_manifest.resolve_standing_clips(
                f"sess_{i}", FIRST, SECOND, 12,
                greeting_ref="tutor_001/greetings/01.md",
                signoff_ref="tutor_001/signoffs/01.md", ack_ref="")
        self.assertEqual(len(sys.path), before)

    def test_card_refs_with_derived_ack_resolve(self):
        # greeting/signoff from the card, ack derived: the branch that
        # reaches assign_ack_variant from outside the derivation block.
        plan = lesson_manifest.resolve_standing_clips(
            "sess", FIRST, SECOND, 12,
            greeting_ref="tutor_001/greetings/03.md",
            signoff_ref="tutor_001/signoffs/02.md", ack_ref=None)
        self.assertEqual(plan["greeting"], "tutor_001/greetings/03")
        self.assertFalse(plan["ack_first"] and plan["ack_second"])


if __name__ == "__main__":
    unittest.main()
