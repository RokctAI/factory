"""Lesson audio (lesson_lines.py, lesson_audio.py, ci/lesson_stems.py).
Model-free; the end-to-end part needs ffmpeg and is skipped without it.

    python -m unittest voice_batch/tests/test_lessons.py

With LESSONS_ROOT (a lessons checkout) and TEAM_ROOT (agent lms/team) set,
the roles of real Grade 9 packages are checked too.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "ci"))
import lesson_audio  # noqa: E402
import lesson_lines as L  # noqa: E402
import lesson_stems  # noqa: E402
from textnorm import TAIL_PAD  # noqa: E402

REL = "maths/session/grade9/term1/algebraic-expressions/like-terms"
ROLES = {"rel": REL, "lesson_id": "maths_g9_algebraic-expressions_like-terms", "grade": 9,
         "first": "tutor_001", "second": "tutor_002", "host": "assistant_005", "split": 2}


class Parsing(unittest.TestCase):
    def test_split_thousands_are_spoken_and_checked_as_one_number(self):
        from textnorm import speak_text, word_errors
        self.assertEqual(speak_text("A deposit of R1 200 at 1 753 m."), "A deposit of R1200 at 1753 m.")
        self.assertEqual(word_errors("a deposit of R1 200", "a deposit of R1,200"), 0)
        self.assertEqual(word_errors("12 metres", "12 meters"), 0)
        self.assertGreater(word_errors("a deposit of R1 200", "a deposit of R"), 0)

    def test_asr_check_folds_spelling_percent_and_compounds(self):
        # Heard on lesson takes that sounded right (2026-10-22 failures).
        from textnorm import word_errors
        self.assertEqual(word_errors("organising and summarising data", "organizing and summarizing data"), 0)
        self.assertEqual(word_errors("the mark-up is 50 percent", "the markup is 50%"), 0)
        self.assertEqual(word_errors("Cross-cast: sales", "Crosscast sales"), 0)
        self.assertEqual(word_errors("a sister-in-charge", "a sister in charge"), 0)
        # A real miss still counts.
        self.assertEqual(word_errors("finally, guard against bias", "finally, god against bias"), 1)

    def test_qa_turns_labels_and_continuations(self):
        md = ("**Assistant:** First question?\n\n**Tutor:** An answer\nthat runs on.\n\n***\n\n"
              "**Thandi:** Second **bold** one?\n\n**Tutor:** Second answer.\n")
        self.assertEqual(L.qa_turns(md), [("assistant", "First question?"),
                                          ("tutor", "An answer that runs on."),
                                          ("thandi", "Second bold one?"), ("tutor", "Second answer.")])

    def test_voices_file_is_well_formed(self):
        for persona, v in L.load_voices().items():
            self.assertRegex(persona, r"^(tutor|assistant)_\d{3}$")
            self.assertRegex(v["ref_sha256"], r"^[0-9a-f]{64}$")
            self.assertTrue(v["ref_path"].startswith("voices/refs/"))
            self.assertGreater(v["f0_tolerance_hz"], 0)
            self.assertIsInstance(v.get("ddpm_steps", 10), int)

    def test_ddpm_steps_default_and_per_voice(self):
        import run as R
        self.assertEqual(R.ddpm_steps(types.SimpleNamespace()), 10)
        self.assertEqual(R.ddpm_steps(types.SimpleNamespace(ddpm_steps=0)), 10)
        self.assertEqual(R.ddpm_steps(types.SimpleNamespace(ddpm_steps=20)), 20)


class Planning(unittest.TestCase):
    def item(self, key, sha="r1"):
        return {"id": f"{REL}#tutor_001/{key}", "key": key, "render_sha256": sha}

    def test_pending_skips_done_and_final_failed_but_not_rejected(self):
        items = [self.item("intro"), self.item("seg00"), self.item("seg01"), self.item("seg02", "new")]
        manifest = {"lines": [{"id": items[0]["id"], "render_sha256": "r1", "ref_sha256": "R", "tail_pad": TAIL_PAD,
                               "sha256": "mp3a"},
                              {"id": items[1]["id"], "render_sha256": "r1", "ref_sha256": "R", "tail_pad": TAIL_PAD,
                               "sha256": "mp3b"},
                              {"id": items[3]["id"], "render_sha256": "old", "ref_sha256": "R", "tail_pad": TAIL_PAD,
                               "sha256": "mp3d"}],
                    "failed": [{"id": items[2]["id"], "render_sha256": "r1", "ref_sha256": "R", "tail_pad": TAIL_PAD}]}
        redo = [{"key": "seg00", "sha256": "mp3b"}]
        got = [it["key"] for it in L.pending_items(items, manifest, "R", redo)]
        self.assertEqual(got, ["seg00", "seg02"])  # rejected take, changed text
        self.assertEqual([it["key"] for it in L.pending_items(items, manifest, "OTHER")],
                         ["intro", "seg00", "seg01", "seg02"])  # a new reference redoes all
        self.assertEqual(L.redo_shift(redo + [{"key": "seg00", "sha256": "x"}], "seg00"), 200)

    def test_asr_only_failures_under_an_older_qc_retry_once(self):
        items = [self.item("intro"), self.item("seg00"), self.item("seg01")]
        base = {"render_sha256": "r1", "ref_sha256": "R", "tail_pad": TAIL_PAD}
        asr = {"rounds": [{"round": 5, "failing": {"asr": {"sentences_without_word_exact_take": 1}}}]}
        sim = {"rounds": [{"round": 5, "failing": {"similarity": 0.8}}]}
        manifest = {"failed": [{"id": items[0]["id"], **base, **asr},           # old QC, ASR only: retry
                               {"id": items[1]["id"], **base, **sim},           # voice match: settled
                               {"id": items[2]["id"], **base, **asr, "qc": L.LESSON_QC}]}  # failed under this QC
        self.assertEqual([it["key"] for it in L.pending_items(items, manifest, "R")], ["intro"])

    def test_pack_one_persona_per_job_round_robin(self):
        todo = ([{"persona": "assistant_005", "lesson": f"a{i}", "words": 300} for i in range(5)]
                + [{"persona": "tutor_001", "lesson": f"t{i}", "words": 2500} for i in range(3)])
        jobs = lesson_audio.L.pack(todo, max_jobs=3, job_words=1000)
        self.assertEqual([(j["persona"], j["lessons"]) for j in jobs],
                         [("assistant_005", "a0,a1,a2"), ("tutor_001", "t0"), ("assistant_005", "a3,a4")])

    def test_blocked_same_family_and_r3(self):
        agent = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, agent)
        vdir = agent / "lms/team/voices"
        vdir.mkdir(parents=True)
        for p, fam in (("tutor_001", "voice_a"), ("tutor_004", "voice_a"), ("assistant_005", "voice_b")):
            (vdir / f"{p}.voice.json").write_text(json.dumps({"voice_family": fam}))
        r = dict(ROLES)
        self.assertIsNone(L.blocked(agent, r, "tutor_001"))
        self.assertIn("same voice family", L.blocked(agent, dict(r, second="tutor_004"), "tutor_001"))
        self.assertIn("R-3", L.blocked(agent, dict(r, grade=2), "tutor_001"))
        self.assertIsNone(L.blocked(agent, dict(r, grade=2), "assistant_005"))


class Stems(unittest.TestCase):
    def test_release_tag_and_asset_names(self):
        self.assertEqual(lesson_stems.release_tag(REL), "stems-maths-grade9-term1")
        self.assertEqual(lesson_stems.asset_name(REL, "tutor_001", "seg03"),
                         "algebraic-expressions--like-terms--tutor_001--seg03.mp3")
        long = f"maths/session/grade9/term1/{'t' * 120}/{'l' * 120}"
        name = lesson_stems.asset_name(long, "tutor_001", "seg03")
        self.assertLessEqual(len(name), lesson_stems.NAME_MAX)
        self.assertNotEqual(name, lesson_stems.asset_name(long + "x", "tutor_001", "seg03"))

    def test_only_records_may_be_committed(self):
        ok = [f"school/curriculum/CAPS/{REL}/voice/tutor_001/manifest.json",
              f"school/curriculum/CAPS/{REL}/voice/assistant_005/qc_failed.json",
              f"school/curriculum/CAPS/{REL}/animations.export.json"]
        bad = [f"school/curriculum/CAPS/{REL}/voice/tutor_001/seg00.mp3",
               f"school/curriculum/CAPS/{REL}/voice/tutor_001/redo.json",
               f"school/curriculum/CAPS/{REL}/script.md", "school/scripts/CAPS/x.py"]
        self.assertTrue(all(lesson_stems.ALLOWED.match(p) for p in ok))
        self.assertFalse(any(lesson_stems.ALLOWED.match(p) for p in bad))


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "needs ffmpeg")
class EndToEnd(unittest.TestCase):
    """render_lesson with the TTS/QC rounds faked: what it records and where
    the MP3s go; then assemble joins the tutors' segments in play order."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        self.stems, self.records = self.tmp / "stems", self.tmp / "records"

    def wav(self, seconds: float) -> str:
        p = self.tmp / f"tone{seconds}.wav"
        subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-f", "lavfi", "-i",
                        f"sine=frequency=220:duration={seconds}", "-ac", "1", "-ar", "24000", "-c:a", "pcm_s16le",
                        str(p)], check=True)
        return str(p)

    def built(self, persona, keys):
        r = ROLES
        return [{"id": f"{REL}#{persona}/{k}", "key": k, "category": "lesson", "file": L.stem_rel(r, persona, k),
                 "script": f"{REL}/script.md", "text": "x", "text_sha256": "t", "render_sha256": f"r-{k}",
                 "render_text": ["One two three."], "sentences": ["One two three."], "pronounced": []}
                for k in keys]

    def args(self, persona):
        return types.SimpleNamespace(persona=persona, voice="voice_a", ref_sha256="R", ref_path="r.wav", model_path="/m",
                                     asr_model="small.en", language="en", f0_target=102.0, f0_tolerance=8.0,
                                     pace_wpm=135.0, pace_tolerance=15.0, work=str(self.tmp / "work"),
                                     budget=None, checkpoint=None, chunk_lines=2)

    def fake_drive(self, seconds, fail=()):
        def drive(items, work, ref, scripts, args, label, install, write):
            res = []
            for it in items:
                if it["key"] in fail:
                    res.append({"id": it["id"], "status": "fail", "seeds_tried": [11], "gate": {"asr": False}})
                else:
                    res.append({"id": it["id"], "status": "pass", "final_path": self.wav(seconds[it["key"]]),
                                "sha256": "w", "duration_s": 1, "seeds": [11], "median_f0_hz": 100,
                                "similarity": 0.9, "asr_match": True, "similarity_threshold": 0.88,
                                "upward_swings": 0, "rms_dbfs": -20, "peak": 0.5, "pauses_ms": [],
                                "tail_db": -40, "seeds_tried": [11]})
            install(res)
            write([])
            return []
        return drive

    def test_render_records_then_assemble(self):
        secs = {"intro": 0.5, "seg00": 1.0, "seg01": 2.0, "qa01_answer": 0.5, "seg02": 1.5}
        t1 = self.built("tutor_001", ["intro", "seg00", "seg01", "qa01_answer"])
        t2 = self.built("tutor_002", ["seg02"])
        with mock.patch("run.drive", self.fake_drive(secs, fail=("qa01_answer",))), \
                mock.patch("run.versions", lambda: {}):
            left = lesson_audio.render_lesson(self.args("tutor_001"), ROLES, t1, self.stems, self.records,
                                              Path("/ref.wav"), Path("/s"), Path("/agent"))
        self.assertEqual(left, 0)
        m = json.loads(L.manifest_path(self.records, ROLES, "tutor_001").read_text())
        self.assertEqual([e["key"] for e in m["lines"]], ["intro", "seg00", "seg01"])
        self.assertEqual([e["key"] for e in m["failed"]], ["qa01_answer"])
        self.assertFalse(m["complete"])
        self.assertEqual(m["roles"]["split"], 2)
        self.assertTrue((self.stems / L.stem_rel(ROLES, "tutor_001", "seg01")).is_file())
        self.assertFalse(any(self.records.rglob("*.mp3")), "MP3s never land in the records tree")
        qc = json.loads((L.manifest_path(self.records, ROLES, "tutor_001").with_name("qc_failed.json")).read_text())
        self.assertEqual([e["id"].rsplit("/", 1)[1] for e in qc["failed"]], ["qa01_answer"])

        # assemble: segments in play order, first tutor then second.
        with mock.patch("run.drive", self.fake_drive(secs)), mock.patch("run.versions", lambda: {}):
            lesson_audio.render_lesson(self.args("tutor_002"), ROLES, t2, self.stems, self.records,
                                       Path("/ref.wav"), Path("/s"), Path("/agent"))
        with mock.patch.object(lesson_audio, "tutor_keys",
                               lambda root, r: [("tutor_001", "seg00"), ("tutor_001", "seg01"), ("tutor_002", "seg02")]), \
                mock.patch.object(L, "roles", lambda root, folder: ROLES):
            out = self.tmp / "out"
            rc = lesson_audio.main(["assemble", "--lessons-root", str(self.tmp), "--stems-root", str(self.stems),
                                    "--lesson", REL, "--out", str(out)])
        self.assertEqual(rc, 0)
        bounds = json.loads((out / "timings.json").read_text())
        self.assertEqual(len(bounds), 3)
        self.assertAlmostEqual(bounds[1]["start"], bounds[0]["end"])
        # MP3 framing pads each stem a little; the bounds are measured on the
        # stems themselves, so they still add up to the joined file.
        total = lesson_audio.probe_seconds(out / "audio.mp3")
        self.assertAlmostEqual(total, 4.5, delta=0.4)
        self.assertAlmostEqual(bounds[-1]["end"], total, delta=0.1)

    def test_checkpoint_asset_survives_a_later_write(self):
        t1 = self.built("tutor_001", ["seg00", "seg01"])
        secs = {"seg00": 0.5, "seg01": 0.5}
        mpath = L.manifest_path(self.records, ROLES, "tutor_001")

        def drive(items, work, ref, scripts, args, label, install, write):
            self.fake_drive(secs)([items[0]], work, ref, scripts, args, label, install, write)
            m = json.loads(mpath.read_text())  # the checkpoint push records the upload
            m["lines"][0]["asset"] = {"tag": "t", "name": "n", "sha256": m["lines"][0]["sha256"]}
            mpath.write_text(json.dumps(m))
            return self.fake_drive(secs)([items[1]], work, ref, scripts, args, label, install, write)

        with mock.patch("run.drive", drive), mock.patch("run.versions", lambda: {}):
            lesson_audio.render_lesson(self.args("tutor_001"), ROLES, t1, self.stems, self.records,
                                       Path("/ref.wav"), Path("/s"), Path("/agent"))
        m = json.loads(mpath.read_text())
        self.assertEqual(m["lines"][0]["asset"]["name"], "n")
        self.assertTrue(m["complete"])


@unittest.skipUnless(os.environ.get("LESSONS_ROOT") and os.environ.get("TEAM_ROOT"), "needs real checkouts")
class RealPackages(unittest.TestCase):
    def test_grade9_parts(self):
        root = Path(os.environ["LESSONS_ROOT"])
        agent = Path(os.environ["TEAM_ROOT"]).parents[1]
        folders = [f for f in L.discover(root) if "/maths/session/grade9/" in str(f)][:3]
        self.assertTrue(folders)
        for f in folders:
            r = L.roles(root, f)
            self.assertEqual((r["first"], r["second"], r["host"]), ("tutor_001", "tutor_002", "assistant_005"))
            host = [k for k, _s, _t in L.part_texts(root, f, r, "assistant_005")]
            self.assertTrue(host and host[-1] == "nervous" and all(k.endswith("_ask") for k in host[:-1]))
            first = [k for k, _s, _t in L.part_texts(root, f, r, "tutor_001")]
            second = [k for k, _s, _t in L.part_texts(root, f, r, "tutor_002")]
            self.assertEqual(first[0], "intro")
            segs = sorted(k for k in first + second if k.startswith("seg"))
            self.assertEqual(len(segs), len(set(segs)), "every segment has exactly one speaker")
            items = L.build_items(root, f, r, "tutor_001", {}, L.persona_names(agent))
        self.assertTrue(items)
        # qc.py writes the gated WAV at final_wav (soundfile picks the
        # format from the extension); the MP3 is encoded from it.
        self.assertTrue(all(it["final_wav"].endswith(".wav") and it["file"].endswith(".mp3") for it in items))


if __name__ == "__main__":
    unittest.main()
