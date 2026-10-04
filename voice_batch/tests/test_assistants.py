"""Model-free tests for the assistant kind. Run: python -m pytest voice_batch/tests"""
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import batch  # noqa: E402
import lines  # noqa: E402

AID = "assistant_005"
SCRIPTS = {
    "intro": ("new", "returning"), "handover": ("into_break", "out_of_break"),
    "signoff": ("session_end", "recording_stopped"),
    "timekeeping": ("halfway", "five_min_warning", "wrap_up"),
}
INBOX = HERE.parent / "voice_batches/inbox/assistant_005_voice_b_sister_batch1.json"


def make_agent(root: Path, spec: dict | None = None) -> None:
    adir = root / lines.team_rel(AID)
    for cat, stems in SCRIPTS.items():
        (adir / cat).mkdir(parents=True)
        for s in stems:
            (adir / cat / f"{s}.md").write_text(f"# {s}\n\nRight, {s.replace('_', ' ')} now.\n", encoding="utf-8")
    (root / "lms/team/voices").mkdir(parents=True)
    (root / "lms/team/voices" / f"{AID}.voice.json").write_text(json.dumps(spec or {}), encoding="utf-8")


class AssistantBatch(unittest.TestCase):
    def test_inbox_batch(self):
        b = batch.load_batch(INBOX)
        self.assertEqual(b["kind"], "assistant")
        self.assertEqual(b["tutor"], AID)
        self.assertEqual(b["categories"], ["intro", "handover", "signoff", "timekeeping"])
        self.assertEqual((b["f0_target_hz"], b["f0_tolerance_hz"]), (241.0, 25.0))
        sp = batch.sparse_paths(b)
        for p in (f"/lms/team/assistants/CAPS/{AID}/", "/lms/team/assistants/CAPS/roster.json",
                  "/lms/team/tutors/CAPS/roster.json", "/lms/team/tutors/CAPS/*/tutor.md"):
            self.assertIn(p, sp)
        out = batch.outputs(b)
        self.assertIn(f"team_dir=lms/team/assistants/CAPS/{AID}", out)
        self.assertIn("f0_target_hz=241", out)

    def _write(self, d: Path, **kw) -> Path:
        raw = json.loads(INBOX.read_text())
        raw.update(kw)
        for k in [k for k, v in kw.items() if v is None]:
            raw.pop(k)
        p = d / "b.json"
        p.write_text(json.dumps(raw))
        return p

    def test_f0_from_spec(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            make_agent(d, {"f0_target_hz": 241, "f0_tolerance_hz": 25, "agreement_in_place": False})
            b = batch.load_batch(self._write(d, f0_target_hz=None, f0_tolerance_hz=None), agent_root=d)
            self.assertEqual((b["f0_target_hz"], b["f0_tolerance_hz"]), (241.0, 25.0))
            b = batch.load_batch(self._write(d, f0_target_hz=None, f0_tolerance_hz=None))
            self.assertEqual(b["f0_target_hz"], batch.F0_TARGET_HZ)   # no spec: Voice A default

    def test_rejects(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            for kw in ({"assistant": "tutor_005"}, {"categories": ["greetings"]},
                       {"lines": [f"{AID}/intro/../x"]}, {"tutor": "tutor_001"}):
                with self.assertRaises(batch.BatchError, msg=kw):
                    batch.load_batch(self._write(d, **kw))

    def test_lines_filter(self):
        with tempfile.TemporaryDirectory() as d:
            b = batch.load_batch(self._write(Path(d), lines=[f"{AID}/signoff/session_end"]))
            self.assertEqual(b["categories"], ["signoff"])
            self.assertEqual(b["matrix"], [{"category": "signoff", "shard": ""}])


class AssistantLines(unittest.TestCase):
    def test_discovery(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            make_agent(d, {"sample_line": "Hello,  I keep time."})
            items = lines.build_lines(d, AID, list(lines.ASSISTANT_CATEGORIES), {}, kind="assistant")
            ids = [it["id"] for it in items]
            self.assertEqual(len([i for i in ids if "/" in i]), 9)
            self.assertIn(f"{AID}/intro/new", ids)
            self.assertIn(f"{AID}/timekeeping/five_min_warning", ids)
            self.assertIn(f"{AID}_sample_line", ids)
            it = next(x for x in items if x["id"] == f"{AID}/handover/into_break")
            self.assertEqual(it["file"], f"lms/team/assistants/CAPS/{AID}/handover/into_break.wav")
            self.assertEqual(it["script"], f"lms/team/assistants/CAPS/{AID}/handover/into_break.md")
            self.assertEqual(it["text"], "Right, into break now.")

    def test_sample_line_optional(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            make_agent(d)
            items = lines.build_lines(d, AID, ["intro"], {}, kind="assistant")
            self.assertEqual([it["id"] for it in items], [f"{AID}/intro/new", f"{AID}/intro/returning"])

    def test_team_rel(self):
        self.assertEqual(lines.team_rel("tutor_001"), "lms/team/tutors/CAPS/tutor_001")
        with self.assertRaises(ValueError):
            lines.team_rel("../x")


class AssistantRun(unittest.TestCase):
    """run_tutor with the render rounds mocked: wavs land beside the scripts
    and the manifest in the assistant folder, with the agreement flag."""

    def test_output_paths(self):
        import importlib.util
        heavy = {m: types.ModuleType(m) for m in ("numpy", "librosa", "soundfile", "faster_whisper", "resemblyzer")
                 if importlib.util.find_spec(m) is None}
        with mock.patch.dict(sys.modules, heavy):
            import run
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            make_agent(d, {"agreement_in_place": False, "pace": {"wpm": 132, "tolerance_wpm": 12}})
            ref = d / "ref.wav"
            ref.write_bytes(b"ref")
            take = d / "take.wav"
            take.write_bytes(b"audio")

            def fake_rounds(items, *a, **k):
                return [{"id": it["id"], "status": "pass", "final_path": str(take), "sha256": "0" * 64,
                         "duration_s": 1.0, "seeds": [11], "median_f0_hz": 240.0, "similarity": 0.9,
                         "asr_match": True, "similarity_threshold": 0.83, "upward_swings": 0, "rms_dbfs": -20,
                         "peak": 0.5, "pauses_ms": [], "tail_db": -60, "seeds_tried": [11],
                         "takes": [{"seed": 11} for _ in it["sentences"]]} for it in items]

            args = types.SimpleNamespace(kind="assistant", tutor=AID, category="handover", lines="", voice="voice_b_sister",
                                         ref_sha256="ab" * 32, model_path="/m", work=str(d / "w"), asr_model="small.en",
                                         language="en", f0_target=241.0, f0_tolerance=25.0)
            # persona = the assistant id: pace comes from lms/team/voices/<AID>.voice.json
            args.pace_wpm, args.pace_tolerance = run.voice_pace(d, AID)
            self.assertEqual((args.pace_wpm, args.pace_tolerance), (132, 12))
            with mock.patch.object(run, "render_rounds", fake_rounds), mock.patch.object(run, "versions", lambda: {}), \
                    mock.patch.object(run.pronunciations, "load", lambda: {}):
                self.assertEqual(run.run_tutor(args, d, ref, d / "lms/team/scripts"), 0)
            adir = d / lines.team_rel(AID)
            self.assertEqual((adir / "handover/into_break.wav").read_bytes(), b"audio")
            self.assertTrue((adir / "handover/out_of_break.wav").exists())
            m = json.loads((adir / "voice_b_sister_manifest.handover.json").read_text())
            self.assertEqual((m["kind"], m["assistant"], m["agreement_in_place"]), ("assistant", AID, False))
            self.assertEqual(m["settings"]["gate"]["median_f0_hz"], [216.0, 266.0])
            self.assertEqual([e["id"] for e in m["lines"]], [f"{AID}/handover/into_break", f"{AID}/handover/out_of_break"])
            self.assertFalse((d / "lms/team/tutors").exists())


if __name__ == "__main__":
    unittest.main()


def make_rosters(root: Path, by_grade: dict, extra_phase: dict | None = None) -> None:
    (root / "lms/team/assistants/CAPS").mkdir(parents=True, exist_ok=True)
    (root / lines.ASSISTANT_ROSTER).write_text(json.dumps({"by_grade": by_grade}))
    t = {"fet_grades": [10, 11, 12], "subjects": {"maths": {"expert": "tutor_001", "simplifier": "tutor_002"}},
         "senior_phase": {"grades": [8, 9], "subjects": {
             "maths": {"expert": "tutor_001", "simplifier": "tutor_002"},
             "ns": {"expert": "tutor_003", "simplifier": "tutor_004"},
             "ems": {"grade_duos": {"8": {"expert": "tutor_007", "simplifier": "tutor_008"},
                                    "9": {"expert": "tutor_005", "simplifier": "tutor_006"}}},
             "tech": {"grade_duos": {"9": {"expert": "tutor_005", "simplifier": "tutor_006"}}}}}}
    t.update(extra_phase or {})
    (root / "lms/team/tutors/CAPS").mkdir(parents=True, exist_ok=True)
    (root / lines.TUTOR_ROSTER).write_text(json.dumps(t))
    for n in range(1, 9):
        td = root / f"lms/team/tutors/CAPS/tutor_{n:03d}"
        td.mkdir(parents=True, exist_ok=True)
        (td / "tutor.md").write_text(f"# Tutor\n\nid: tutor_{n:03d}\ndisplay_name: Name {n}\n")


class HostPlaceholders(unittest.TestCase):
    def _agent(self, d: Path, by_grade: dict) -> None:
        make_agent(d)
        (d / lines.team_rel(AID) / "intro/returning.md").write_text("Welcome back. {first_tutor} takes over.\n")
        (d / lines.team_rel(AID) / "handover/out_of_break.md").write_text(
            "Over to you, {second_tutor}. Say {{Ngubane|ngoo-BAH-neh}}.\n")
        make_rosters(d, by_grade)

    def test_one_variant_per_duo_of_the_hosted_grade(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            self._agent(d, {"9": AID, "10": "assistant_001"})
            self.assertEqual(lines.host_duos(d, AID), [("tutor_001", "tutor_002"), ("tutor_003", "tutor_004"),
                                                       ("tutor_005", "tutor_006")])
            items = {it["id"]: it for it in lines.build_lines(d, AID, ["intro", "handover"], {}, kind="assistant")}
            self.assertIn(f"{AID}/intro/new", items)  # no placeholder: one plain line
            self.assertNotIn(f"{AID}/intro/returning", items)
            it = items[f"{AID}/intro/returning@tutor_001+tutor_002"]
            self.assertEqual(it["text"], "Welcome back. Name 1 takes over.")
            self.assertEqual(it["file"], f"{lines.team_rel(AID)}/intro/returning@tutor_001+tutor_002.wav")
            self.assertEqual(items[f"{AID}/handover/out_of_break@tutor_003+tutor_004"]["text"],
                             "Over to you, Name 4. Say Ngubane.")
            self.assertEqual(sum(k.startswith(f"{AID}/intro/returning@") for k in items), 3)
            self.assertEqual(batch.assistant_category_of(f"{AID}/intro/returning@tutor_005+tutor_006", AID), "intro")

    def test_no_live_grade_skips_placeholder_lines(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            self._agent(d, {"10": "assistant_001"})
            with mock.patch("sys.stderr") as err:
                ids = [it["id"] for it in lines.build_lines(d, AID, ["intro"], {}, kind="assistant")]
            self.assertEqual(ids, [f"{AID}/intro/new"])
            self.assertIn("hosts no grade", "".join(str(c) for c in err.write.call_args_list))

    def test_unknown_placeholder_is_an_error(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            self._agent(d, {"9": AID})
            (d / lines.team_rel(AID) / "intro/new.md").write_text("Hi {student_name}.\n")
            with self.assertRaisesRegex(ValueError, "student_name"):
                lines.build_lines(d, AID, ["intro"], {}, kind="assistant")

    def test_display_name_prefers_roster_then_still(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            make_rosters(d, {})
            self.assertEqual(lines.tutor_display_name(d, "tutor_001"), "Name 1")
            app = d / "lms/team/tutors/CAPS/tutor_001/appearance"
            app.mkdir()
            (app / "still.json").write_text(json.dumps({"display_name": "Still Name"}))
            self.assertEqual(lines.tutor_display_name(d, "tutor_001"), "Still Name")
