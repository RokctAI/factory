"""Pronunciation audition planning: changed keys, manual word lists,
slugging and the pinned voice references. Model-free, own fixtures.
Run: python -m pytest voice_batch/tests
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import audition as A  # noqa: E402
import pronunciations as P  # noqa: E402

OLD = P.validate({"words": {"Mahikeng": "mah-hee-KENG", "Nkosi": "n-KOH-see"},
                  "ambiguous": {"Thendo": ["TEN-doh", "TEN-dooh"]}})


class Slug(unittest.TestCase):
    def test_slug(self):
        self.assertEqual(A.slug("Thendo"), "thendo")
        self.assertEqual(A.slug("TEN-doh"), "ten-doh")
        self.assertEqual(A.slug("Nkosi’s  place!"), "nkosis-place")
        self.assertEqual(A.slug("Gqeberha (PE)"), "gqeberha-pe")
        self.assertEqual(A.slug("Ngũgĩ"), "ngugi")
        self.assertEqual(A.slug("--"), "x")
        self.assertLessEqual(len(A.slug("a" * 100)), 48)

    def test_clip_names_are_distinct_per_variant_and_safe(self):
        names = [A.clip_name("Thendo", v) for v in OLD["ambiguous"]["Thendo"]]
        self.assertEqual(names, ["thendo--ten-doh", "thendo--ten-dooh"])
        import re
        for n in names:
            self.assertRegex(n + ".mp3", r"^[a-z0-9][a-z0-9-]*\.mp3$")  # push_agent.sh's allow-list
        self.assertIsNone(re.search(r"[/.\s]", A.clip_name("../x y", "a.b")))

    def test_carrier(self):
        self.assertEqual(A.carrier("TEN-doh"), "TEN-doh. TEN-doh.")


class Changed(unittest.TestCase):
    def words(self, rows):
        return [(r["word"], r["respelling"], r["kind"]) for r in rows]

    def test_no_change(self):
        self.assertEqual(A.changed(OLD, OLD), [])

    def test_added_and_changed_words_only(self):
        new = P.validate({"words": {"Mahikeng": "mah-HEE-keng", "Nkosi": "n-KOH-see", "Gqeberha": "gkeh-BEH-ha"},
                          "ambiguous": OLD["ambiguous"]})
        self.assertEqual(self.words(A.changed(OLD, new)),
                         [("Mahikeng", "mah-HEE-keng", "word"), ("Gqeberha", "gkeh-BEH-ha", "word")])

    def test_removed_renders_nothing(self):
        new = P.validate({"words": {"Nkosi": "n-KOH-see"}, "ambiguous": OLD["ambiguous"]})
        self.assertEqual(A.changed(OLD, new), [])

    def test_ambiguous_every_variant(self):
        new = P.validate({"words": OLD["words"], "ambiguous": {"Thendo": ["TEN-doh", "TEN-dooh", "THEN-doh"]}})
        self.assertEqual(self.words(A.changed(OLD, new)), [("Thendo", "TEN-doh", "ambiguous"),
                                                           ("Thendo", "TEN-dooh", "ambiguous"),
                                                           ("Thendo", "THEN-doh", "ambiguous")])
        self.assertEqual(len(A.changed(P.empty(), OLD)), 4)

    def test_requested(self):
        self.assertEqual(self.words(A.requested(OLD, ["thendo", " Mahikeng "])),
                         [("Thendo", "TEN-doh", "ambiguous"), ("Thendo", "TEN-dooh", "ambiguous"),
                          ("Mahikeng", "mah-hee-KENG", "word")])
        with self.assertRaises(A.AuditionError):
            A.requested(OLD, ["Nowhere"])
        self.assertEqual(A.parse_words(" a, ,b ,"), ["a", "b"])


class PlanFromGit(unittest.TestCase):
    def git(self, *a):
        env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
               "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@x", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@x"}
        return subprocess.run(["git", *a], cwd=self.d, env=env, capture_output=True, text=True, check=True).stdout.strip()

    def commit(self, data):
        p = Path(self.d, A.PRON_REL)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(data))
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "x")
        return self.git("rev-parse", "HEAD")

    def test_diff_against_previous_commit(self):
        with tempfile.TemporaryDirectory() as self.d:
            self.git("init", "-q")
            first = self.commit({"words": {"Mahikeng": "mah-hee-KENG"}, "ambiguous": {}})
            second = self.commit({"words": {"Mahikeng": "mah-hee-KENG", "Nkosi": "n-KOH-see"},
                                  "ambiguous": {"Thendo": ["TEN-doh", "TEN-dooh"]}})
            got = [(r["word"], r["respelling"]) for r in A.plan(first, second, "", cwd=self.d)]
            self.assertEqual(got, [("Nkosi", "n-KOH-see"), ("Thendo", "TEN-doh"), ("Thendo", "TEN-dooh")])
            # No usable "before" (new branch, or a manual run): the previous commit.
            self.assertEqual(A.plan("0" * 40, second, "", cwd=self.d), A.plan(first, second, "", cwd=self.d))
            self.assertEqual(A.plan("", "HEAD", "", cwd=self.d), A.plan(first, second, "", cwd=self.d))
            # The first commit of the file: everything is new.
            self.assertEqual([r["word"] for r in A.plan(first + "^", first, "", cwd=self.d)], ["Mahikeng"])
            # A manual word list wins over the diff.
            self.assertEqual([r["word"] for r in A.plan("", "HEAD", "mahikeng", cwd=self.d)], ["Mahikeng"])

    def test_too_many(self):
        with tempfile.TemporaryDirectory() as self.d:
            self.git("init", "-q")
            self.commit({"words": {}, "ambiguous": {}})
            self.commit({"words": {f"Word{chr(97 + i // 26)}{chr(97 + i % 26)}": "x" for i in range(A.MAX_CLIPS + 1)},
                         "ambiguous": {}})
            with self.assertRaises(A.AuditionError):
                A.plan("", "HEAD", "", cwd=self.d)


class Voices(unittest.TestCase):
    def test_real_inbox_pins_one_ref_per_voice(self):
        vs = {v["voice"]: v for v in A.voices()}
        self.assertEqual(set(vs), {"voice_a", "voice_b"})
        self.assertEqual(vs["voice_a"]["ref_path"], "lms/team/voice_refs/voice_a_ref.wav")
        self.assertEqual(vs["voice_b"]["ref_path"], "lms/team/voice_refs/voice_b_ref.wav")

    def test_conflicting_or_missing_ref_fails(self):
        with tempfile.TemporaryDirectory() as d:
            for n, sha in (("a", "1" * 64), ("b", "2" * 64)):
                Path(d, f"{n}.json").write_text(json.dumps(
                    {"voice": "voice_a", "ref_path": "lms/team/voice_refs/voice_a_ref.wav", "ref_sha256": sha}))
            with self.assertRaises(A.AuditionError):
                A.voices(Path(d), ("voice_a",))
            with self.assertRaises(A.AuditionError):
                A.voices(Path(d), ("voice_b",))


if __name__ == "__main__":
    unittest.main()
