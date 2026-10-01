"""Model-free tests for the Grades R-3 voice batch. Run: python -m pytest voice_batch/tests

Set AGENT_ROOT to a RokctAI/agent checkout to also check the keys and the
default praise against the app's Dart source (r3_session_engine.dart and
lms_{en,af}_translations.dart); skipped otherwise.
"""
import collections
import json
import os
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import batch  # noqa: E402
import merge_manifest  # noqa: E402
import r3_lines as R  # noqa: E402
from qc import f0_range, pick, pyin_bounds  # noqa: E402
from textnorm import norm_words  # noqa: E402

FACTORY = HERE.parent
sys.path.insert(0, str(FACTORY / "lessons" / "scripts" / "CAPS"))
import r3_pack_check  # noqa: E402

AGENT_ROOT = os.environ.get("AGENT_ROOT")
PROBE = FACTORY / "voice_batches" / "examples" / "r3_phonics_probe.json"
EN = "english_home_language."
GOOD = {"kind": "r3", "voice": "voice_x", "ref_path": "lms/team/voice_refs/voice_x_ref.wav",
        "ref_sha256": "0" * 64, "agent_branch": "rokct/r3-test"}
NO_RESP = {"by_key": {}, "by_text": {}}


def load(d):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(d, f)
    return batch.load_batch(f.name)


def template_of(where: str) -> str:
    return re.sub(r"^rounds_\d+_", "rounds_{i}_", where)


def dart_where_templates(src: str) -> set:
    """The <where> templates R3SessionEngine.lines passes to l(...)."""
    body = src[src.index("List<R3Line> get lines"):src.index("String get parentLine")]
    out = set()
    for lit in re.findall(r"\bl\(\s*'([^']+)'", body):
        out.add(lit.replace("${at}", "rounds_{i}"))
    return out


class PackLines(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packs = R.load_packs()
        cls.items = R.build_r3_lines(respellings=NO_RESP)

    def test_counts(self):
        # Derived from the pack tree (Grades R-3 land one grade at a time), so
        # a new grade's packs never need this number changed by hand.
        paths = r3_pack_check.pack_paths()
        self.assertGreaterEqual(len(paths), 74)  # Grade R Terms 1-4, maths + English HL
        self.assertEqual(len(self.packs), len(paths))
        pack_items = [i for i in self.items if not i["key"].startswith("r3.")]
        want = sum(1 for p in self.packs for _, t in r3_pack_check._spoken_lines(p) if t.strip())
        self.assertEqual(len(pack_items), want)
        self.assertEqual(len(self.items), want + 4)  # + the 4 default praise lines
        self.assertEqual(len({i["key"] for i in self.items}), len(self.items))

    def test_mirrors_checker(self):
        """Same lines as r3_pack_check._spoken_lines (the packs all pass the
        checker, so no round is skipped and every pack has 2 hints)."""
        self.assertEqual(r3_pack_check.run(r3_pack_check.pack_paths()), [])
        for p in self.packs:
            want = collections.Counter(t for _, t in r3_pack_check._spoken_lines(p) if t.strip())
            got = collections.Counter(t for _, t in R.pack_lines(p))
            self.assertEqual(got, want, p["id"])
            # checker address -> app key, one to one
            conv = {re.sub(r"\[(\d+)\]", r"_\1", w).replace(".", "_").replace("show_line", "show"): t
                    for w, t in r3_pack_check._spoken_lines(p)}
            self.assertEqual({f"{p['id']}.{k}": t for k, t in conv.items()}, dict(R.pack_lines(p)))

    def test_key_scheme(self):
        for i in self.items:
            if i["key"].startswith("r3."):
                self.assertRegex(i["key"], r"^r3\.r3_praise_[a-z]+$")
                continue
            pid, where = i["key"].rsplit(".", 1)
            self.assertRegex(pid, r"^(maths|english_home_language)\.grade[R123]\.term[1-4]\.w\d\d_[a-z0-9_]+$")
            self.assertIn(template_of(where), R.WHERE_TEMPLATES, i["key"])
            self.assertEqual(i["file"], f"{R.AUDIO_DIR}/{i['key']}.mp3")

    def test_dart_parsing_rules(self):
        pack = {"id": "s.gradeR.term1.x", "show": {"line": "Hi."}, "hints": ["h0", "h1", "h2"],
                "rounds": [{"type": "nope", "prompt": "skip me"},
                           {"type": "say_it", "prompt": "p0", "accept": ["x"], "praise": "  "},
                           {"type": "say_it", "prompt": "p1"},  # missing accept: skipped
                           {"type": "story_tap", "prompt": "p2", "story": "s", "options": ["a", "b"],
                            "answer": "a", "praise": "yay"},
                           {"type": "trace", "prompt": "p3", "glyph": "a", "story": "not spoken"}],
                "beat_the_tutor": {"setup": "su", "tutor_try": "tt", "win_line": "", "gentle_line": "gl"}}
        self.assertEqual([k.split(".", 4)[-1] for k, _ in R.pack_lines(pack)], [
            "show", "hints_0", "hints_1", "rounds_0_prompt", "rounds_1_prompt", "rounds_1_story",
            "rounds_1_praise", "rounds_2_prompt", "beat_the_tutor_setup", "beat_the_tutor_tutor_try",
            "beat_the_tutor_gentle_line"])

    def test_praise_fallback(self):
        en, src = R.default_praise("en")
        self.assertEqual(src, "fallback")
        self.assertEqual([k for k, _ in en], ["r3.r3_praise_yes", "r3.r3_praise_great",
                                              "r3.r3_praise_clever", "r3.r3_praise_right"])
        af = R.build_r3_lines(locale="af", respellings=NO_RESP)
        self.assertEqual([i["id"] for i in af], [f"{k}.af" for k, _ in en])
        self.assertTrue(all(i["file"].endswith(".af.mp3") for i in af))
        with self.assertRaises(R.R3Error):
            R.default_praise("zu")

    def test_dart_translation_parser(self):
        src = "const m = {\n  'r3_praise_right': 'That\\'s right!',\n  'x_y': \"Q\",\n};\n"
        self.assertEqual(R.dart_translations(src), {"r3_praise_right": "That's right!", "x_y": "Q"})

    def test_packs_filter_drops_praise(self):
        items = R.build_r3_lines(packs=["maths.*"], respellings=NO_RESP)
        self.assertTrue(items)
        self.assertTrue(all(i["key"].startswith("maths.") for i in items))

    def test_shards(self):
        n = R.shard_count(len(self.items), batch.R3_LINES_PER_SHARD, batch.R3_MAX_SHARDS)
        self.assertEqual(n, 8)  # capped at R3_MAX_SHARDS, so each shard is about 155 lines
        parts = [R.shard(self.items, k, n) for k in range(1, n + 1)]
        self.assertEqual(sum(parts, []), self.items)
        per_shard = -(-len(self.items) // n)
        self.assertTrue(all(0 < len(p) <= per_shard for p in parts))
        self.assertEqual(R.shard_count(6), 1)
        self.assertEqual(R.shard_count(10_000), 8)


@unittest.skipUnless(AGENT_ROOT, "AGENT_ROOT not set")
class AgainstDart(unittest.TestCase):
    def test_where_templates_match_engine(self):
        src = (Path(AGENT_ROOT) / R.ENGINE_DART).read_text(encoding="utf-8")
        self.assertEqual(dart_where_templates(src), set(R.WHERE_TEMPLATES))
        self.assertIn("R3Line('${pack.id}.$where', text)", src)
        self.assertIn("R3Line('r3.$key', translate(key, text))", src)
        self.assertIn("r is R3StoryTap", src)  # story lines only for story_tap rounds

    def test_praise_from_app(self):
        for loc in R.LOCALES:
            got, src = R.default_praise(loc, AGENT_ROOT)
            self.assertEqual(src, "agent")
            fb, _ = R.default_praise(loc)
            self.assertEqual(got, fb, f"fallback table drifted from the app ({loc})")

    def test_every_key_is_one_the_engine_can_build(self):
        src = (Path(AGENT_ROOT) / R.ENGINE_DART).read_text(encoding="utf-8")
        templates = dart_where_templates(src)
        keys = set(R.dart_praise_keys(src))
        for i in R.build_r3_lines(agent_root=AGENT_ROOT, respellings=NO_RESP):
            if i["key"].startswith("r3."):
                self.assertIn(i["key"][3:], keys)
            else:
                self.assertIn(template_of(i["key"].rsplit(".", 1)[1]), templates)


class Respellings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.resp = R.load_respellings()
        cls.plain = {i["key"]: i for i in R.build_r3_lines(respellings=NO_RESP)}
        cls.items = {i["key"]: i for i in R.build_r3_lines()}

    def test_keys_exist_and_are_english(self):
        self.assertTrue(self.resp["by_key"])
        for k in self.resp["by_key"]:
            self.assertIn(k, self.plain)
            self.assertTrue(k.startswith(EN), k)
        for t in self.resp["by_text"]:
            self.assertIn(t, {i["text"] for i in self.plain.values()})

    def test_only_letter_tokens_change(self):
        for k, tts in self.resp["by_key"].items():
            a, b = norm_words(self.plain[k]["text"]), norm_words(tts)
            self.assertEqual(len(a), len(b), k)
            for x, y in zip(a, b):
                if x != y:
                    self.assertTrue(len(x) == 1 or x == "vvv", (k, x, y))

    def test_no_letter_names_left(self):
        """A respelled line never keeps a bare letter (bar the article a and
        the pronoun I), so the voice cannot fall back to a letter name."""
        for k, tts in self.resp["by_key"].items():
            bare = [t for t in re.findall(r"(?<!['’])\b[A-Za-z]\b(?!['’])", tts) if t not in ("a", "A", "I")]
            self.assertEqual(bare, [], k)

    def test_every_phonics_line_is_covered(self):
        for k, it in self.plain.items():
            if k.startswith(EN) and re.search(r"(?<!['’])\b([b-hj-zB-HJ-Z]|i)\b(?!['’])", it["text"]):
                self.assertIn(k, self.resp["by_key"], k)

    def test_display_text_unchanged_render_and_asr_use_tts(self):
        for k, tts in self.resp["by_key"].items():
            it = self.items[k]
            self.assertEqual(it["text"], self.plain[k]["text"])
            self.assertEqual(it["text_sha256"], self.plain[k]["text_sha256"])
            self.assertEqual(it["tts_text"], tts)
            self.assertEqual(it["asr_text"], tts)
            self.assertEqual(" ".join(it["sentences"]), " ".join(tts.split()))
            self.assertTrue(it["needs_listen"])
            self.assertNotEqual(it["render_sha256"], self.plain[k]["render_sha256"])
        for k, it in self.items.items():
            if k not in self.resp["by_key"]:
                self.assertFalse(it["needs_listen"])
                self.assertNotIn("tts_text", it)

    def test_by_text(self):
        it = R.item("x.show", "a as in ant.", "en", "t", {"by_key": {}, "by_text": {"a as in ant.": "Ah, as in ant."}})
        self.assertEqual((it["asr_text"], it["text"], it["needs_listen"]), ("Ah, as in ant.", "a as in ant.", True))


class R3Batch(unittest.TestCase):
    def test_all_lines(self):
        b = load(GOOD)
        self.assertEqual((b["kind"], b["locale"]), ("r3", "en"))
        self.assertEqual(b["line_count"], len(R.build_r3_lines()))
        self.assertEqual(len(b["matrix"]), 8)
        self.assertEqual((b["f0_target_hz"], b["f0_tolerance_hz"]), (102.0, 8.0))

    def test_filters(self):
        b = load(dict(GOOD, packs="english_home_language.gradeR.term1.w01_*"))
        self.assertEqual(b["line_count"], 28)
        self.assertEqual(len(b["matrix"]), 1)
        key = "maths.gradeR.term1.w01_circle.show"
        self.assertEqual(load(dict(GOOD, lines=[key, "r3.r3_praise_yes"]))["lines"], sorted([key, "r3.r3_praise_yes"]))
        self.assertEqual(load(dict(GOOD, locale="af"))["line_count"], 4)

    def test_rejects(self):
        for bad in ({"agent_branch": "main"}, {"agent_branch": "rokct/../x"}, {"agent_branch": "claude/r3-test"}, {"packs": "nothing.*"},
                    {"packs": ["a b"]}, {"lines": ["maths.gradeR.term1.w01_circle.nope"]}, {"lines": []},
                    {"locale": "zu"}, {"locale": "af", "packs": "maths.*"}, {"kind": "other"},
                    {"tutor": "tutor_001"}, {"categories": ["teaching"]}, {"f0_target_hz": 5},
                    {"f0_tolerance_hz": "8"}, {"voice": "Voice A"}):
            with self.assertRaises(batch.BatchError, msg=str(bad)):
                load(dict(GOOD, **bad))

    def test_custom_f0(self):
        b = load(dict(GOOD, f0_target_hz=210, f0_tolerance_hz=25))
        self.assertEqual((b["f0_target_hz"], b["f0_tolerance_hz"]), (210.0, 25.0))
        self.assertIn("f0_target_hz=210", batch.outputs(b))

    def test_outputs_carry_no_text(self):
        b = load(GOOD)
        out = "\n".join(batch.outputs(b))
        for i in R.build_r3_lines()[:50]:
            self.assertNotIn(i["text"], out)
        self.assertIn("sparse<<SPARSE_EOF\nlms/dart/templates/assets/r3_packs/audio\n", out)
        self.assertIn('matrix_json=[{"category": "r3", "shard": "1/8"}', out)

    def test_probe_example(self):
        self.assertFalse(str(PROBE).startswith(str(FACTORY / "voice_batches" / "inbox")))
        b = batch.load_batch(PROBE)
        self.assertEqual((b["voice"], b["agent_branch"], b["line_count"]), ("voice_a", "rokct/r3-phonics-probe", 6))
        self.assertEqual(b["ref_sha256"], "de4a86bdea53fa5722cb8d08edd699098207019a8a2611bf569491a4e6993d5f")
        items = R.build_r3_lines(only=b["lines"])
        self.assertEqual(len(items), 6)
        self.assertTrue(all(i["needs_listen"] for i in items))


class F0Gate(unittest.TestCase):
    def test_tutor_defaults_unchanged(self):
        good = {"tutor": "tutor_001", "voice": "voice_a", "ref_path": "lms/team/voice_refs/voice_a_ref.wav",
                "ref_sha256": "0" * 64, "agent_branch": "rokct/x-y", "categories": ["teaching"]}
        b = load(good)
        self.assertEqual((b["kind"], b["f0_target_hz"], b["f0_tolerance_hz"]), ("tutor", 102.0, 8.0))
        self.assertEqual(f0_range(b["f0_target_hz"], b["f0_tolerance_hz"]), (94.0, 110.0))
        self.assertEqual(pyin_bounds(), (50.0, 300.0))
        self.assertEqual(b["matrix"], [{"category": "teaching", "shard": ""}])
        b = load(dict(good, f0_target_hz=120, f0_tolerance_hz=10))
        self.assertEqual(f0_range(b["f0_target_hz"], b["f0_tolerance_hz"]), (110.0, 130.0))

    def test_pick_with_target(self):
        t = lambda f0: {"err": 0, "f0": f0, "swings": 0, "res": 0.9}  # noqa: E731
        low, high = t(100), t(215)
        self.assertIs(pick([low, high])[0], low)
        self.assertEqual(pick([high])[1], 2)
        self.assertEqual(pick([high], 210, 20), (high, 1))
        self.assertEqual(pick([low], 210, 20)[1], 2)
        self.assertEqual(pyin_bounds(210, 20), (50.0, 460.0))


class Mp3(unittest.TestCase):
    def test_encode(self):
        try:
            import lameenc  # noqa: F401
        except ImportError:
            if not shutil.which("ffmpeg"):
                self.skipTest("no lameenc or ffmpeg")
        import numpy as np
        import soundfile as sf
        import mp3
        with tempfile.TemporaryDirectory() as d:
            sr = 24000
            x = 0.3 * np.sin(np.arange(sr) * 2 * np.pi * 220 / sr)
            sf.write(f"{d}/a.wav", x, sr, subtype="PCM_16")
            mp3.encode(f"{d}/a.wav", f"{d}/out/a.mp3")
            mp3.encode(f"{d}/a.wav", f"{d}/out/b.mp3")
            a, b = Path(d, "out/a.mp3").read_bytes(), Path(d, "out/b.mp3").read_bytes()
            self.assertEqual(a, b)  # deterministic -> idempotent re-runs
            self.assertTrue(a[:3] == b"ID3" or (a[0] == 0xFF and a[1] & 0xE0 == 0xE0))
            self.assertLess(len(a), 64_000 / 8 * 1.3)  # ~64 kbps for 1 s
            self.assertFalse(list(Path(d, "out").glob("*.part")))
            try:
                y, ysr = sf.read(f"{d}/out/a.mp3")
            except Exception:  # libsndfile without MP3 support
                return
            self.assertEqual(ysr, sr)
            self.assertEqual(y.ndim, 1)


class MergeR3(unittest.TestCase):
    def test_parts_fold_and_are_removed(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            e = lambda i, **kw: {"id": i, **kw}  # noqa: E731
            (d / "r3_manifest.v.json").write_text(json.dumps({"lines": [e("k1", sha256="old"), e("k2")]}))
            (d / "r3_manifest.v.part01.json").write_text(json.dumps({
                "kind": "r3", "voice": "v", "updated_at": "2026-01-01T00:00:00Z",
                "lines": [e("k1", sha256="new", needs_listen=True)], "failed": [e("k3")]}))
            (d / "r3_manifest.v.part02.json").write_text(json.dumps({
                "kind": "r3", "voice": "v", "updated_at": "2026-01-02T00:00:00Z",
                "lines": [e("k3")], "failed": [e("k2"), e("k4")]}))
            (d / "r3_manifest.w.part01.json").write_text("{}")
            merge_manifest.main_r3(d, "v")
            m = json.loads((d / "r3_manifest.v.json").read_text())
            self.assertEqual([x["id"] for x in m["lines"]], ["k1", "k2", "k3"])
            self.assertEqual(m["lines"][0]["sha256"], "new")
            self.assertEqual([x["id"] for x in m["failed"]], ["k4"])  # a failed re-render never hides a pass
            self.assertEqual(m["needs_listen"], 1)
            self.assertEqual(sorted(p.name for p in d.iterdir()), ["r3_manifest.v.json", "r3_manifest.w.part01.json"])
            merge_manifest.main_r3(d, "v")  # idempotent
            self.assertEqual(json.loads((d / "r3_manifest.v.json").read_text()), m)


if __name__ == "__main__":
    unittest.main()


class RunR3Install(unittest.TestCase):
    """run.py's r3 path end to end with the render/QC rounds stubbed out."""

    def test_install_manifest_and_skip(self):
        try:
            import lameenc  # noqa: F401
        except ImportError:
            if not shutil.which("ffmpeg"):
                self.skipTest("no lameenc or ffmpeg")
        import argparse
        import hashlib
        import numpy as np
        import soundfile as sf
        import run
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            agent = d / "agent"
            (agent / "lms/team/voice_refs").mkdir(parents=True)
            ref = agent / "lms/team/voice_refs/voice_a_ref.wav"
            ref.write_bytes(b"ref")
            sha = hashlib.sha256(b"ref").hexdigest()
            wav = d / "take.wav"
            sf.write(str(wav), 0.2 * np.sin(np.arange(12000) / 10), 24000, subtype="PCM_16")
            calls = []

            def fake_rounds(items, work, ref_, scripts, args, label):
                calls.append([it["id"] for it in items])
                out = []
                for n, it in enumerate(items):
                    r = {"id": it["id"], "seeds_tried": [11], "lacking": []}
                    if n == 0:
                        r.update(status="fail", duration_s=0.5, median_f0_hz=150.0, similarity=0.7,
                                 similarity_threshold=0.83, asr_match=False, gate={"f0": False})
                    else:
                        r.update(status="pass", final_path=str(wav), duration_s=0.5, median_f0_hz=101.0,
                                 upward_swings=0, similarity=0.9, similarity_threshold=0.83, asr_match=True,
                                 rms_dbfs=-20.0, peak=0.3, pauses_ms=[], sha256="w", seeds=[11],
                                 takes=[{"sentence": k, "seed": 11} for k in range(1, len(it["sentences"]) + 1)])
                    out.append(r)
                return out

            args = argparse.Namespace(batch=str(PROBE), shard="1/1", factory_root=str(FACTORY), voice="voice_a",
                                      ref_sha256=sha, model_path="m", work=str(d / "work"), asr_model="small.en",
                                      language="en", f0_target=102.0, f0_tolerance=8.0)
            orig, run.render_rounds = run.render_rounds, fake_rounds
            try:
                b = json.loads(PROBE.read_text())
                b["ref_sha256"] = sha
                PROBE_TMP = d / "probe.json"
                PROBE_TMP.write_text(json.dumps(b))
                args.batch = str(PROBE_TMP)
                self.assertEqual(run.run_r3(args, agent, ref, agent / "lms/team/scripts"), 0)
                audio = agent / R.AUDIO_DIR
                part = json.loads((audio / "r3_manifest.voice_a.part01.json").read_text())
                self.assertEqual((len(part["lines"]), len(part["failed"])), (5, 1))
                e = part["lines"][0]
                self.assertTrue(e["needs_listen"])
                self.assertIn("tts_text", e)
                self.assertNotEqual(e["tts_text"], e["text"])
                self.assertTrue((agent / e["file"]).is_file())
                self.assertEqual(part["settings"]["gate"]["median_f0_hz"], [94.0, 110.0])
                self.assertEqual(part["settings"]["output"]["bitrate_kbps"], 64)
                self.assertFalse(list(audio.glob("*.wav")))
                # Second run: the 5 installed lines are skipped, only the failed one re-renders.
                self.assertEqual(run.run_r3(args, agent, ref, agent / "lms/team/scripts"), 0)
                self.assertEqual(len(calls[1]), 1)
                self.assertEqual(calls[1][0], calls[0][0])
            finally:
                run.render_rounds = orig
