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

"""Unit tests for lessons/scripts/CAPS/math_verify.py.

Every verdict is exercised (verified, MISMATCH, MULTIPLE_CORRECT,
NO_CORRECT, UNPARSEABLE, SKIPPED), including a deliberately wrong key and
gibberish maths. math_verify needs sympy, which the stdlib-only Unit tests
workflow does not install, so the whole module is skipped there and runs in
.github/workflows/math_verify.yml instead.

Run from the repo root:
    pip install -r lessons/scripts/CAPS/requirements-math-verify.txt
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -p 'test_math_verify.py' -v
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

try:
    import math_verify as mv  # noqa: E402
except ImportError:  # sympy missing
    mv = None


def q(question, options, key):
    return {"id": "t_q1", "question": question, "options": options,
            "correct_index": key}


def verdict(question, options, key):
    return mv.verify_question(q(question, options, key))


@unittest.skipIf(mv is None, "sympy not installed")
class NormaliseTests(unittest.TestCase):
    def test_comma_decimal_currency_and_thousands(self):
        self.assertEqual(mv.normalise("R4 900,17"), "4900.17")
        self.assertEqual(mv.normalise("1,85"), "1.85")
        self.assertEqual(mv.normalise("3, 11, 22"), "3, 11, 22")  # a list

    def test_unicode_operators(self):
        self.assertEqual(mv.normalise("6 × 3 ÷ 2 − 1"), "6 * 3 / 2 - 1")
        self.assertEqual(mv.normalise("x²"), "x^(2)")
        self.assertEqual(mv.normalise("√(x + 7)"), "sqrt(x + 7)")
        self.assertEqual(mv.normalise("√12"), "sqrt(12)")

    def test_degrees_become_radians_inside_trig(self):
        e = mv.parse_math(mv.normalise("sin 30°"))
        self.assertEqual(e, mv.sp.Rational(1, 2))

    def test_implicit_multiplication(self):
        x = mv.sp.Symbol("x")
        self.assertEqual(mv.parse_math("2x(x + 1)"), 2 * x * (x + 1))

    def test_gibberish_raises(self):
        for bad in ("(x + 3(x - 2)", "3x +* 2", "x^"):
            with self.assertRaises(mv.ParseFailure):
                mv.parse_math(bad)


@unittest.skipIf(mv is None, "sympy not installed")
class VerifiedTests(unittest.TestCase):
    def check(self, question, options, key, qtype):
        res = verdict(question, options, key)
        self.assertEqual(res["verdict"], "verified", res)
        self.assertEqual(res["type"], qtype, res)

    def test_solve_equation(self):
        self.check("Solving 5x − 7 = 2x + 8 gives:",
                   ["x = 5", "x = 3", "x = −5", "x = 15/7"], 0, "solve")

    def test_solve_quadratic_or(self):
        self.check("Solve 2x² − 8x = 0.",
                   ["x = 4 only", "x = 0 or x = 4", "x = 0 or x = −4",
                    "x = 2 or x = 8"], 1, "solve")

    def test_solve_inequality(self):
        self.check("The solution of x² − x − 6 < 0 is:",
                   ["x < −2 or x > 3", "−2 < x < 3", "x < 3", "−3 < x < 2"],
                   1, "solve")

    def test_factorise(self):
        self.check("3x² − 5x − 2 = 0 factorises to:",
                   ["(3x − 1)(x + 2) = 0", "(x − 3)(3x + 2) = 0",
                    "(3x + 1)(x − 2) = 0", "(3x − 2)(x + 1) = 0"], 2, "factorise")

    def test_fully_factorised_beats_partial(self):
        self.check("Fully factorise 2x² − 8:",
                   ["2(x² − 4)", "2(x − 2)(x + 2)", "(2x − 4)(x + 2)",
                    "2(x − 4)(x + 4)"], 1, "factorise")

    def test_exponent_laws(self):
        self.check("x³ × x² simplifies to:", ["x⁶", "x⁹", "x⁵", "2x⁵"], 2,
                   "exponent_laws")

    def test_evaluate_trig_degrees(self):
        self.check("sin 60° × cos 30° − tan 45° evaluates to:",
                   ["3/4", "0", "−3/4", "−1/4"], 3, "evaluate")

    def test_substitute(self):
        self.check("For y = −2x², the value of y when x = 3 is:",
                   ["18", "−12", "−18", "36"], 2, "substitute")

    def test_percent_with_rand_and_comma(self):
        self.check("25% off a R799 jacket leaves a sale price of:",
                   ["R199,75", "R774", "R599,25", "R639,20"], 2, "percent")

    def test_ratio_share(self):
        self.check("Sharing R2 400 in the ratio 5 : 3 : 2, the middle share is:",
                   ["R720", "R480", "R1 200", "R800"], 0, "ratio")

    def test_compound_growth(self):
        self.check("R5 000 at 8% per annum compounded annually for 3 years "
                   "accumulates to:",
                   ["R6 200", "R6 240", "R6 298,56", "R6 300 exactly"], 2,
                   "finance")

    def test_exact_surd_option(self):
        self.check("cos 75° in simplest surd form is:",
                   ["(√6 − √2)/4", "(√6 + √2)/4", "(√3 − √2)/2", "0,2588"], 0,
                   "evaluate")


@unittest.skipIf(mv is None, "sympy not installed")
class FlagTests(unittest.TestCase):
    def test_mismatch_on_deliberately_wrong_key(self):
        res = verdict("Solving 5x − 7 = 2x + 8 gives:",
                      ["x = 5", "x = 3", "x = −5", "x = 15/7"], 1)
        self.assertEqual(res["verdict"], "MISMATCH")
        self.assertEqual(res["correct"], [0])

    def test_mismatch_numeric_wrong_key(self):
        res = verdict("25% of R480 is:", ["R120", "R25", "R360", "R192"], 2)
        self.assertEqual(res["verdict"], "MISMATCH")
        self.assertEqual(res["correct"], [0])

    def test_mismatch_when_key_is_only_close(self):
        # R6 300 is within 0,5% of R6 298,56 but the stem asks for the exact value
        res = verdict("R5 000 at 8% per annum compounded annually for 3 years "
                      "accumulates to:",
                      ["R6 200", "R6 240", "R6 298,56", "R6 300 exactly"], 3)
        self.assertEqual(res["verdict"], "MISMATCH")

    def test_multiple_correct(self):
        res = verdict("Factorise x² − 4:",
                      ["(x − 2)(x + 2)", "(x + 2)(x − 2)", "(x − 4)(x + 1)",
                       "(x − 2)²"], 0)
        self.assertEqual(res["verdict"], "MULTIPLE_CORRECT")
        self.assertEqual(res["correct"], [0, 1])

    def test_no_correct(self):
        res = verdict("Solving 5x − 7 = 2x + 8 gives:",
                      ["x = 4", "x = 3", "x = −5", "x = 15/7"], 0)
        self.assertEqual(res["verdict"], "NO_CORRECT")

    def test_no_correct_when_key_out_of_range(self):
        res = verdict("Solve x + 1 = 2.", ["x = 1", "x = 2", "x = 3", "x = 0"], 7)
        self.assertEqual(res["verdict"], "NO_CORRECT")

    def test_keyed_working_with_false_arithmetic(self):
        res = verdict("Taxable income R310 000; bracket: R42 678 + 26% of the "
                      "amount above R237 100. Tax before rebates:",
                      ["R61 632,00 — 42 678 + 26% × 72 900 = 61 732",
                       "R80 600,00", "R44 397,00", "R18 954,00"], 0)
        self.assertEqual(res["verdict"], "MISMATCH")
        self.assertEqual(res["type"], "keyed_working")

    def test_keyed_working_that_is_right_is_not_flagged(self):
        res = verdict("Taxable income R310 000; bracket: R42 678 + 26% of the "
                      "amount above R237 100. Tax before rebates:",
                      ["R61 632,00 — 42 678 + 26% × 72 900 = 61 632",
                       "R80 600,00", "R44 397,00", "R18 954,00"], 0)
        self.assertEqual(res["verdict"], "SKIPPED")


@unittest.skipIf(mv is None, "sympy not installed")
class UnparseableTests(unittest.TestCase):
    def test_unbalanced_brackets_in_stem(self):
        res = verdict("Expand (x + 3(x − 2):",
                      ["x² + x − 6", "x² − 6", "x² + 5x − 6", "2x + 1"], 0)
        self.assertEqual(res["verdict"], "UNPARSEABLE")

    def test_gibberish_operators(self):
        res = verdict("Simplify 3x +* 2x:", ["5x", "6x", "x", "5"], 0)
        self.assertEqual(res["verdict"], "UNPARSEABLE")

    def test_malformed_option(self):
        res = verdict("Expand (x + 2)(x + 3):",
                      ["x² + 5x + 6)", "x² + 6", "x² + 6x + 5", "2x + 5"], 0)
        self.assertEqual(res["verdict"], "UNPARSEABLE")
        self.assertEqual(res["detail"]["where"], "option 0")

    def test_intervals_are_not_unbalanced(self):
        res = verdict("On which interval is f increasing?",
                      ["[2; 5)", "(−∞; 2]", "(0; 3)", "[1; 4]"], 0)
        self.assertNotEqual(res["verdict"], "UNPARSEABLE")


@unittest.skipIf(mv is None, "sympy not installed")
class SkippedTests(unittest.TestCase):
    def test_concept_question(self):
        res = verdict("Factorising is described as:",
                      ["Repacking a messy pile into neat crates",
                       "Sharing the pile", "Cutting the pile", "Throwing away"], 0)
        self.assertEqual(res["verdict"], "SKIPPED")

    def test_process_question_is_not_flagged(self):
        # a stem about a step, not the answer: never MISMATCH
        res = verdict("The first step to solve 2x + 3 = 7 is:",
                      ["x = 2", "Subtract 3 from both sides", "x = 5", "Divide by 2"],
                      1)
        self.assertEqual(res["verdict"], "SKIPPED")

    def test_word_problem(self):
        res = verdict("Four painters take 15 days. How many days would 6 painters take?",
                      ["10 days", "22,5 days", "9 days", "11 days"], 0)
        self.assertEqual(res["verdict"], "SKIPPED")

    def test_context_may_reject_a_root(self):
        res = verdict("Solving n(n + 1)/2 = 120 for the can stacks gives:",
                      ["n = 12", "No natural-number solution", "n = 15",
                       "n = 16"], 2)
        self.assertEqual(res["verdict"], "verified")


@unittest.skipIf(mv is None, "sympy not installed")
class ReportTests(unittest.TestCase):
    def test_cli_writes_json_and_markdown_and_exits_zero(self):
        data = {"subtopics": [{"ref": "subtopic_1", "questions": [
            q("Solving 5x − 7 = 2x + 8 gives:",
              ["x = 5", "x = 3", "x = −5", "x = 15/7"], 1) | {"id": "subtopic_1_q1"},
            q("Factorising is described as:", ["a", "b", "c", "d"], 0)
            | {"id": "subtopic_1_q2"},
        ]}]}
        with tempfile.TemporaryDirectory() as tmp:
            lesson = Path(tmp) / "maths" / "session" / "grade10" / "term1" / "x"
            lesson.mkdir(parents=True)
            path = lesson / "mcq.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            out_json, out_md = Path(tmp) / "r.json", Path(tmp) / "r.md"
            rc = mv.main([str(path), "--json", str(out_json), "--md", str(out_md)])
            self.assertEqual(rc, 0)  # findings never fail the build
            report = json.loads(out_json.read_text(encoding="utf-8"))
            self.assertEqual(report["total_questions"], 2)
            self.assertEqual(report["totals"]["MISMATCH"], 1)
            self.assertEqual(report["totals"]["SKIPPED"], 1)
            self.assertIn("maths grade10 (base)", report["by_grade"])
            flagged = report["flagged"][0]
            self.assertEqual(flagged["id"], "subtopic_1_q1")
            self.assertTrue(flagged["path"].endswith("mcq.json"))
            md = out_md.read_text(encoding="utf-8")
            self.assertIn("MISMATCH", md)
            self.assertIn("subtopic_1_q1", md)


if __name__ == "__main__":
    unittest.main()
