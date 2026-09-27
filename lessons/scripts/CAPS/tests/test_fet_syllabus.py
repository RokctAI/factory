#!/usr/bin/env python3
# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""FET (Grades 10-12) sources and syllabi: manifest integrity, held from the
pipeline, and the same `pathway` block as the Grades R-9 files."""
import hashlib
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import lesson_pipeline as lp  # noqa: E402
from fet_pathways import SUBJECT_NAMES  # noqa: E402

CAPS_DIR = Path(__file__).resolve().parents[3] / "curriculum" / "CAPS"
MANIFEST = CAPS_DIR / "fet_sources.json"
REPO = CAPS_DIR.parents[2]


def _manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def _fet_syllabi():
    for folder in sorted(SUBJECT_NAMES):
        for grade in (10, 11, 12):
            path = CAPS_DIR / folder / "syllabus" / f"grade{grade}.json"
            if path.exists():
                yield folder, grade, path


class FetSourcesTest(unittest.TestCase):
    def test_manifest_files_exist_and_match_hash(self):
        man = _manifest()
        self.assertEqual(man["gaps"], [])
        for entry in man["files"]:
            with self.subTest(path=entry["path"]):
                data = (CAPS_DIR / entry["path"]).read_bytes()
                self.assertTrue(data.startswith(b"%PDF"))
                self.assertEqual(len(data), entry["bytes"])
                self.assertEqual(hashlib.sha256(data).hexdigest(), entry["sha256"])
                self.assertTrue(entry["source_url"].startswith("https://www.education.gov.za/"))

    def test_every_subject_has_caps_and_three_atps(self):
        by_subject = {}
        for entry in _manifest()["files"]:
            by_subject.setdefault(entry["subject"], []).append(entry)
        self.assertEqual(set(by_subject), set(SUBJECT_NAMES))
        for folder, entries in by_subject.items():
            with self.subTest(subject=folder):
                self.assertEqual(sum(e["kind"] == "caps" for e in entries), 1)
                self.assertEqual(sorted(e["grade"] for e in entries if e["kind"] == "atp"),
                                 [10, 11, 12])


class FetSyllabusTest(unittest.TestCase):
    def test_syllabi_are_held_and_carry_pathway(self):
        files = list(_fet_syllabi())
        # every FET subject with sources on file has Grades 10, 11 and 12
        self.assertEqual({(f, g) for f, g, _ in files},
                         {(f, g) for f in SUBJECT_NAMES for g in (10, 11, 12)})
        for folder, grade, path in files:
            with self.subTest(path=str(path.relative_to(CAPS_DIR))):
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(data["grade"], grade)
                self.assertEqual(data["curriculum"], "CAPS")
                self.assertEqual(data["phase"], "FET")
                self.assertIs(data["pipeline_enabled"], False)
                self.assertEqual(set(data["pathway"]), {"comes_from", "leads_to", "fet_subjects"})
                self.assertEqual(data["pathway"]["fet_subjects"], [SUBJECT_NAMES[folder]])
                for src in data["source_path"]:
                    self.assertTrue((REPO / src).exists(), src)
                self.assertTrue(data["terms"])
                for term in data["terms"]:
                    self.assertIn(term["term"], (1, 2, 3, 4))
                    self.assertTrue(term["topics"], f"term {term['term']} has no topics")
                    for topic in term["topics"]:
                        self.assertTrue(topic["name"].strip())

    def test_fet_folders_stay_out_of_the_pipeline(self):
        new = set(SUBJECT_NAMES) - {"english_home_language", "english_first_additional_language",
                                    "life_orientation"}
        self.assertFalse(new & set(lp.CAPS_TYPE_BY_FOLDER))


try:
    import extract_fet_syllabus as fet  # needs pdfplumber
except ImportError:  # pragma: no cover
    fet = None


@unittest.skipIf(fet is None, "pdfplumber not installed")
class FetExtractorTest(unittest.TestCase):
    def test_duration_lines_in_each_language(self):
        cases = {
            "Dihora tse 2": 2, "Ixesha: 2 iiyure": 2, "Ura e le nngwe": 1,
            "Diura di le tharo": 3, "Nako: Diiri tše 4": 4, "Nkarhi: Awara ya 1 na hafu": 1.5,
            "Isikhathi: Ama-iri ama-2 nesiquntu.": 2.5, "Tshifhinga: Awara 2": 2,
        }
        for text, hours in cases.items():
            with self.subTest(text=text):
                self.assertEqual(fet.duration_line(text), hours)
        self.assertIsNone(fet.duration_line("Poko"))

    def test_split_informal_assessment_label_is_ignored(self):
        self.assertEqual(fet.label_role("TLHATLHOBO E E SA TLHOMAMANG"), "ignore")
        self.assertEqual(fet.label_role("SBA TLHATLHOBO E E TLHOMAMENG"), "sba")
        self.assertEqual(fet.label_role("UKUHLOLA OKUNGAKAHLELWA: UKUBUYEKEZA"), "ignore")
        self.assertEqual(fet.label_role("DIKGONO"), "concept")


if __name__ == "__main__":
    unittest.main()
