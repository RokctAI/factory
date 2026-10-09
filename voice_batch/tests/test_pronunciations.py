"""Pronunciations: the global word list, inline {{word|respelling}}, the
ambiguous-word gate and the ASR wildcard. Model-free; own fixtures only
(the shipped pronunciations.json has no words on purpose).
Run: python -m pytest voice_batch/tests
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import batch  # noqa: E402
import pronunciations as P  # noqa: E402
import r3_lines as R  # noqa: E402
from lines import build_lines  # noqa: E402

PRON = P.validate({
    "words": {"Mahikeng": "mah-hee-KENG", "Nkosi": "n-KOH-see"},
    "ambiguous": {"Thendo": ["TEN-doh", "TEN-dooh"]},
})


class ShippedFile(unittest.TestCase):
    def test_empty_and_valid(self):
        raw = json.loads(P.PRONUNCIATIONS.read_text(encoding="utf-8"))
        self.assertEqual((raw["words"], raw["ambiguous"]), ({}, {}))
        self.assertIn("{{", raw["_comment"])
        self.assertEqual(P.load(), {**P.empty(), "names": raw.get("names", [])})


class Names(unittest.TestCase):
    def test_validate(self):
        self.assertEqual(P.validate({"names": ["Supacharge", "van Zyl"]})["names"], ["Supacharge", "van Zyl"])
        for bad in ({"names": "Supacharge"}, {"names": [""]}, {"names": ["a.b"]}, {"names": [3]}):
            with self.assertRaises(P.PronunciationError, msg=str(bad)):
                P.validate(bad)

    def test_name_wild_longest_first_whole_words(self):
        self.assertEqual(P.name_wild("Over to you, John Petersen. Johnny's here.", ["John", "John Petersen"]),
                         [["John Petersen", "John Petersen"]])
        self.assertEqual(P.name_wild("I'm kavitha.", ["Kavitha"]), [["kavitha", "kavitha"]])

    def test_a_name_the_asr_misspells_still_matches(self):
        wild = P.name_wild("Welcome back, I'm Kavitha.", ["Kavitha"])
        self.assertEqual(P.word_errors_wild("Welcome back, I'm Kavitha.", "Welcome back, I'm Kavita.", wild), 0)
        self.assertEqual(P.word_errors_wild("Welcome back, I'm Kavitha.", "Welcome back, I'm Kavita.", []), 1)
        self.assertEqual(P.word_errors_wild("Welcome back, I'm Kavitha.", "Welcome back, Kavita.", wild), 1)


class Validate(unittest.TestCase):
    def test_rejects(self):
        for bad in ({"words": {"x": ""}}, {"words": {"x": "a.b"}}, {"words": {"x": "a|b"}},
                    {"words": {"1x": "y"}}, {"words": []}, {"ambiguous": {"Thendo": ["TEN-doh"]}},
                    {"ambiguous": {"Thendo": "TEN-doh"}}, {"other": {}},
                    {"words": {"Thendo": "x"}, "ambiguous": {"thendo": ["a", "b"]}}):
            with self.assertRaises(P.PronunciationError, msg=str(bad)):
                P.validate(bad)

    def test_multiword_and_comment(self):
        p = P.validate({"_comment": "x", "words": {"Mr Zulu": "mister ZOO-loo"}})
        self.assertEqual(P.apply("Hi, Mr Zulu.", p)[1], "Hi, mister ZOO-loo.")


class Inline(unittest.TestCase):
    def test_with_punctuation(self):
        d, t, w = P.apply("Well done, {{Thendo|TEN-doh}}!")
        self.assertEqual((d, t, w), ("Well done, Thendo!", "Well done, TEN-doh!", [["Thendo", "TEN-doh"]]))
        d, t, _ = P.apply("({{Thendo|TEN-dooh}}'s turn.)")
        self.assertEqual((d, t), ("(Thendo's turn.)", "(TEN-dooh's turn.)"))

    def test_several_per_line(self):
        d, t, w = P.apply("{{Thendo|TEN-doh}} and {{Thendo|TEN-dooh}} met {{Lerato|leh-RAH-toh}}.")
        self.assertEqual(d, "Thendo and Thendo met Lerato.")
        self.assertEqual(t, "TEN-doh and TEN-dooh met leh-RAH-toh.")
        self.assertEqual([x[1] for x in w], ["TEN-doh", "TEN-dooh", "leh-RAH-toh"])

    def test_malformed_rejected(self):
        for bad in ("Hi {{Thendo}}.", "Hi {{Thendo|}}.", "Hi {{|TEN-doh}}.", "Hi {{Thendo|TEN-doh}.",
                    "Hi {Thendo|TEN-doh}}.", "Hi {{Thendo|TEN|doh}}.", "Hi }} there."):
            with self.assertRaises(P.PronunciationError, msg=bad):
                P.apply(bad, PRON)

    def test_any_respelling_allowed_inline(self):
        self.assertEqual(P.apply("{{Thendo|TEHN-doh}}", PRON)[1], "TEHN-doh")
        self.assertEqual(P.ambiguous_uses("{{Thendo|TEHN-doh}}", PRON), [])

    def test_inline_wins_over_global(self):
        d, t, w = P.apply("From {{Mahikeng|MAH-ee-keng}} to Mahikeng.", PRON)
        self.assertEqual(d, "From Mahikeng to Mahikeng.")
        self.assertEqual(t, "From MAH-ee-keng to mah-hee-KENG.")
        self.assertEqual(w, [["Mahikeng", "MAH-ee-keng"], ["Mahikeng", "mah-hee-KENG"]])


class Global(unittest.TestCase):
    def test_whole_words_any_case(self):
        d, t, w = P.apply("Nkosi's class, nkosi, Nkosinathi.", PRON)
        self.assertEqual(d, "Nkosi's class, nkosi, Nkosinathi.")
        self.assertEqual(t, "n-KOH-see's class, n-KOH-see, Nkosinathi.")
        self.assertEqual(len(w), 2)

    def test_never_touches_ambiguous(self):
        self.assertEqual(P.apply("Thendo.", PRON)[1], "Thendo.")


class Ambiguous(unittest.TestCase):
    def test_error_names_line_and_variants(self):
        items = [{"id": "tutor_009/greetings/01", "text": "Hi Thendo.", "source_text": "Hi Thendo."},
                 {"id": "ok", "text": "Hi Thendo.", "source_text": "Hi {{Thendo|TEN-doh}}."}]
        self.assertEqual(P.check_ambiguous(items, PRON), [
            "line tutor_009/greetings/01 uses 'Thendo': write {{Thendo|TEN-doh}} or {{Thendo|TEN-dooh}}"])

    def test_case_and_possessive(self):
        self.assertEqual(P.ambiguous_uses("THENDO's book, {{Thendo|x}}", PRON), ["Thendo"])
        self.assertEqual(P.ambiguous_uses("Thendos", PRON), [])

    def _tutor(self, d, text):
        t = Path(d, "lms/team/tutors/CAPS/tutor_009/greetings")
        t.mkdir(parents=True)
        (t / "01.md").write_text(text)
        b = {"tutor": "tutor_009", "voice": "voice_a", "ref_path": "lms/team/voice_refs/voice_a_ref.wav",
             "ref_sha256": "0" * 64, "agent_branch": "rokct/x", "categories": ["greetings"]}
        p = Path(d, "b.json")
        p.write_text(json.dumps(b))
        return p

    def test_tutor_batch_fails_with_agent_root(self):
        with tempfile.TemporaryDirectory() as d:
            p = self._tutor(d, "Hello Thendo.\n")
            b = batch.load_batch(p)  # no agent checkout: tutor lines not visible yet
            errs = batch.pronunciation_errors(b, d, pron=PRON)
            self.assertEqual(len(errs), 1)
            self.assertIn("line tutor_009/greetings/01 uses 'Thendo'", errs[0])
            self.assertIn("{{Thendo|TEN-dooh}}", errs[0])

    def test_tutor_malformed_names_line(self):
        with tempfile.TemporaryDirectory() as d:
            p = self._tutor(d, "Hello {{Thendo}}.\n")
            errs = batch.pronunciation_errors(batch.load_batch(p), d, pron=PRON)
            self.assertEqual(len(errs), 1)
            self.assertTrue(errs[0].startswith("line tutor_009/greetings/01: malformed"), errs[0])
            self.assertNotIn("Hello", errs[0])  # errors reach public logs: never the line text

    def test_r3_items_checked(self):
        it = R.item("x.show", "Hi Thendo.", "en", "t", {"by_key": {}, "by_text": {}}, PRON)
        self.assertEqual(len(P.check_ambiguous([it], PRON)), 1)


class Items(unittest.TestCase):
    def test_tutor_item(self):
        with tempfile.TemporaryDirectory() as d:
            t = Path(d, "lms/team/tutors/CAPS/tutor_009/greetings")
            t.mkdir(parents=True)
            (t / "01.md").write_text("Hi {{Thendo|TEN-doh}}. Welcome to Mahikeng.\n")
            (t / "02.md").write_text("Plain line.\n")
            a, b = build_lines(d, "tutor_009", ["greetings"], PRON)
            self.assertEqual(a["text"], "Hi Thendo. Welcome to Mahikeng.")
            self.assertEqual(a["sentences"], ["Hi Thendo.", "Welcome to Mahikeng."])
            self.assertEqual(a["render_text"], ["Hi TEN-doh.", "Welcome to mah-hee-KENG."])
            self.assertEqual(a["sentence_wild"], [[["Thendo", "TEN-doh"]], [["Mahikeng", "mah-hee-KENG"]]])
            self.assertEqual(a["tts_text"], "Hi TEN-doh. Welcome to mah-hee-KENG.")
            self.assertEqual(a["pronounced"], ["Thendo", "Mahikeng"])
            plain = build_lines(d, "tutor_009", ["greetings"], P.empty())[1]
            self.assertEqual(b, plain)
            self.assertNotIn("tts_text", b)
            self.assertEqual(b["asr_wild"], [])

    def test_r3_item_after_respelling(self):
        resp = {"by_key": {"x.show": "Ah, as in ant, Nkosi."}, "by_text": {}}
        it = R.item("x.show", "a as in ant, Nkosi.", "en", "t", resp, PRON)
        self.assertEqual(it["text"], "a as in ant, Nkosi.")
        self.assertEqual(it["asr_text"], "Ah, as in ant, Nkosi.")
        self.assertEqual(it["tts_text"], "Ah, as in ant, n-KOH-see.")
        self.assertTrue(it["needs_listen"])
        it = R.item("y.show", "Go {{Thendo|TEN-doh}}!", "en", "t", {"by_key": {}, "by_text": {}}, PRON)
        self.assertEqual((it["text"], it["tts_text"], it["needs_listen"]), ("Go Thendo!", "Go TEN-doh!", True))
        self.assertNotIn("{", it["file"])


class Wildcard(unittest.TestCase):
    def test_respelled_word_matches_one_to_n(self):
        w = [["Thendo", "TEN-doh"]]
        for hyp in ("Hi Thendo.", "Hi Tendo.", "Hi, ten doe.", "Hi ten though so."):
            self.assertEqual(P.word_errors_wild("Hi Thendo.", hyp, w), 0, hyp)
        self.assertEqual(P.word_errors_wild("Hi Thendo.", "Hi.", w), 1)
        self.assertEqual(P.word_errors_wild("Hi Thendo.", "Hi ten doe so much.", w), 1)

    def test_other_words_stay_exact(self):
        w = [["Thendo", "TEN-doh"]]
        self.assertEqual(P.word_errors_wild("Well done Thendo.", "Well gone Tendo.", w), 1)
        self.assertEqual(P.word_errors_wild("Thendo said two.", "Tendo said 2.", w), 0)

    def test_no_wild_is_word_errors(self):
        from textnorm import word_errors
        for ref, hyp in (("Let us start.", "Let's start."), ("Done.", ""), ("a b c", "a x c")):
            self.assertEqual(P.word_errors_wild(ref, hyp, []), word_errors(ref, hyp))
            self.assertEqual(P.word_errors_wild(ref, hyp, None), word_errors(ref, hyp))


if __name__ == "__main__":
    unittest.main()
