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

"""Curriculum labels on the three index builders (W1):

  * practice bank — every item carries `curriculum`; overlay items ride
    under the `~<curriculum>` id suffix with CAPS ids unchanged, and
    `needs_reauthor` items stay out of the bank;
  * skills index — `curriculum` lists the tree plus every sibling
    curriculum with a pointer file; `importance.exam_weight_by_curriculum`
    is added beside the untouched legacy `exam_weight`;
  * knowledge bites index — every bite carries `curriculum: [<tree>]`.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -v
"""

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_knowledge_bites_index as bites  # noqa: E402
import build_practice_bank as bank  # noqa: E402
import build_skills_index as skills  # noqa: E402
import curriculum_overlay as co  # noqa: E402
import overlay_fixture as fx  # noqa: E402


def _point(module, root):
    saved = module.CAPS_ROOT
    module.CAPS_ROOT = root
    return lambda: setattr(module, "CAPS_ROOT", saved)


class PracticeBankLabelTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        self.shared_root, _twin_root, self.shared, _ = fx.make_trees(self.tmp)
        self.addCleanup(_point(bank, self.shared_root))

    def _items(self):
        with redirect_stderr(io.StringIO()):
            return bank.scan_items()

    def test_every_item_is_labelled_and_ids_are_unchanged(self):
        items = self._items()
        self.assertEqual(
            sorted(items),
            [
                "maths.grade10.simple-growth.subtopic_1_q1",
                "maths.grade10.simple-growth.subtopic_1_q2",
                "maths.grade10.simple-growth.subtopic_2_q1",
            ],
        )
        self.assertTrue(all(i["curriculum"] == "CAPS" for i in items.values()))
        item = items["maths.grade10.simple-growth.subtopic_1_q2"]
        self.assertEqual(item["lesson"], "simple-growth")
        self.assertEqual(item["subtopic_ref"], "subtopic_1")
        self.assertEqual(item["correct_index"], 0)

    def test_overlay_items_ride_under_the_ieb_suffix(self):
        mcq = json.loads(json.dumps(fx.TWIN_MCQ))
        # Flag one question as case-bound: it must not be published.
        mcq["subtopics"][0]["questions"][1][co.NEEDS_REAUTHOR] = True
        co.write_overlay(
            self.shared,
            "IEB",
            mcq=mcq,
            comprehension=fx.TWIN_CC,
            transcript=fx.TWIN_TRANSCRIPT,
            break_qa="",
            exam_weight="",
            label=co.make_label("IEB"),
        )
        items = self._items()
        caps_ids = [i for i in items if "~" not in i]
        ieb_ids = [i for i in items if i.endswith("~ieb")]
        self.assertEqual(len(caps_ids), 3)
        self.assertEqual(
            ieb_ids,
            [
                "maths.grade10.simple-growth.subtopic_1_q1~ieb",
                "maths.grade10.simple-growth.subtopic_2_q1~ieb",
                "maths.grade10.simple-growth.subtopic_2_q2~ieb",
            ],
        )
        self.assertNotIn("maths.grade10.simple-growth.subtopic_1_q2~ieb", items)
        ieb = items["maths.grade10.simple-growth.subtopic_2_q2~ieb"]
        self.assertEqual(ieb["curriculum"], "IEB")
        self.assertEqual(ieb["lesson"], "simple-growth")
        self.assertEqual(ieb["question"], "Factorising 3mp + 3mq gives:")
        # CAPS items are unchanged by the overlay's presence.
        self.assertEqual(
            items["maths.grade10.simple-growth.subtopic_1_q2"]["question"],
            "R5 000 at 8% for 3 years grows to:",
        )

    def test_bank_signature_stable_across_runs(self):
        first = bank.content_signature(bank.build_bank())
        second = bank.content_signature(bank.build_bank())
        self.assertEqual(first, second)


class SkillsIndexLabelTests(unittest.TestCase):
    SKILL = {
        "skill_ref": "maths.simple_growth",
        "name": "Simple growth",
        "subject": "Maths",
        "grade": 10,
        "topic": "Skills",
        "importance": {
            "summary": "Finance section of Paper 1.",
            "exam_weight": [
                {
                    "grade": 10,
                    "paper": "paper1",
                    "section": "Finance",
                    "marks": 15,
                    "paper_total": 100,
                }
            ],
        },
        "covered_by": [
            {"grade": 10, "topic": "Finance and growth", "subtopic": "Simple growth"}
        ],
    }

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        self.caps = self.tmp / "lessons" / "curriculum" / "CAPS"
        self.ieb = self.tmp / "lessons" / "curriculum" / "IEB"
        skill_dir = self.caps / "maths" / "skills" / "grade10"
        skill_dir.mkdir(parents=True)
        (skill_dir / "simple_growth.json").write_text(
            json.dumps(self.SKILL), encoding="utf-8"
        )
        self.addCleanup(_point(skills, self.caps))

    def _pointer(self):
        ptr_dir = self.ieb / "maths" / "skills" / "grade10"
        ptr_dir.mkdir(parents=True)
        (ptr_dir / "simple_growth.json").write_text(
            json.dumps(
                {
                    "skill_ref": "maths.simple_growth",
                    "curriculum": "IEB",
                    "inherits_from": "lessons/curriculum/CAPS/maths/skills/grade10/simple_growth.json",
                    "overrides_pending": ["importance.exam_weight"],
                }
            ),
            encoding="utf-8",
        )

    def test_caps_only_skill(self):
        entry = skills.scan_skills()["maths.simple_growth"]
        self.assertEqual(entry["curriculum"], ["CAPS"])
        self.assertEqual(
            entry["importance"]["exam_weight_by_curriculum"],
            {"CAPS": self.SKILL["importance"]["exam_weight"]},
        )
        self.assertEqual(
            entry["importance"]["exam_weight"], self.SKILL["importance"]["exam_weight"]
        )

    def test_pointer_adds_the_sibling_curriculum_as_pending(self):
        self._pointer()
        entry = skills.scan_skills()["maths.simple_growth"]
        self.assertEqual(entry["curriculum"], ["CAPS", "IEB"])
        by = entry["importance"]["exam_weight_by_curriculum"]
        self.assertEqual(by["CAPS"], self.SKILL["importance"]["exam_weight"])
        self.assertEqual(by["IEB"], {"status": "pending_sag"})
        # Legacy key untouched, and the lookup keys still lead the entry.
        self.assertEqual(
            entry["importance"]["exam_weight"], self.SKILL["importance"]["exam_weight"]
        )
        self.assertEqual(list(entry)[:3], ["card_id", "subject", "grade"])
        self.assertEqual(entry["subtopic"], "Simple growth")

    def test_pointer_without_inherits_from_is_ignored(self):
        ptr_dir = self.ieb / "maths" / "skills" / "grade10"
        ptr_dir.mkdir(parents=True)
        (ptr_dir / "simple_growth.json").write_text("{}", encoding="utf-8")
        self.assertEqual(
            skills.scan_skills()["maths.simple_growth"]["curriculum"], ["CAPS"]
        )


class KnowledgeBitesLabelTests(unittest.TestCase):
    def test_every_bite_carries_the_tree_curriculum(self):
        with tempfile.TemporaryDirectory() as tmp:
            caps = Path(tmp) / "lessons" / "curriculum" / "CAPS"
            bite = (
                caps
                / "maths"
                / "knowledge_bites"
                / "grade10"
                / "simple-growth"
                / "dbe-maths-g10-p1-2024-nov-q3-1"
            )
            bite.mkdir(parents=True)
            (bite / "question.md").write_text(
                "# Past-Paper Worked Item — Q3.1\n\n**Source:** Department "
                "of Basic Education — Grade 10 Maths P1, November 2024.\n\n"
                "## Question (3 marks)\n",
                encoding="utf-8",
            )
            restore = _point(bites, caps)
            try:
                index = bites.scan_bites()
            finally:
                restore()
        (entry,) = index["simple-growth"]
        self.assertEqual(entry["curriculum"], ["CAPS"])
        self.assertEqual(entry["bite_slug"], "dbe-maths-g10-p1-2024-nov-q3-1")
        self.assertEqual(entry["title"], "Past-Paper Worked Item — Q3.1")


if __name__ == "__main__":
    unittest.main()
