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
        self.assertEqual(batch.sparse_paths(b), [f"lms/team/assistants/CAPS/{AID}", "lms/team/voices",
                                                 "lms/team/voice_refs", "lms/team/scripts"])
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
            make_agent(d, {"agreement_in_place": False})
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
