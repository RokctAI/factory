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
gibberish maths. The step checks (STEP_OK, STEP_WRONG, ANSWER_WRONG,
WARNING, UNPARSEABLE, SKIPPED, CONSISTENT, CONTRADICTS_SCREEN) are exercised
on chains, spoken maths, animations and narration-vs-screen, including an
unconventional-but-valid route that must pass (truth, not method). math_verify needs sympy, which the stdlib-only Unit tests
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


# --- step checks: what we teach -------------------------------------------

def steps(text, lit=False):
    found, _ = mv.check_written_line(text, 1, lit=lit)
    return [f["verdict"] for f in found], found


def spoken(text):
    found, _ = mv.check_spoken_text(text, 1)
    return [f["verdict"] for f in found], found


FLAGS = {"STEP_WRONG", "ANSWER_WRONG", "UNPARSEABLE"}


@unittest.skipIf(mv is None, "sympy not installed")
class StepChainTests(unittest.TestCase):
    def test_correct_chain_is_ok_at_every_step(self):
        v, found = steps("x² − 5x + 6 = 0 → (x−2)(x−3) = 0 → x = 2 or x = 3")
        self.assertEqual(v, ["STEP_OK", "STEP_OK"])
        self.assertEqual([f["step"] for f in found], [1, 2])

    def test_wrong_factorisation_step_names_the_step(self):
        v, found = steps("x² − 5x + 6 = 0 → (x−2)(x+3) = 0 → x = 2 or x = −3")
        wrong = [f for f in found if f["verdict"] == "STEP_WRONG"]
        self.assertEqual(len(wrong), 1)
        self.assertEqual(wrong[0]["step"], 1)

    def test_wrong_final_root_is_answer_wrong(self):
        v, found = steps("x² − 5x + 6 = 0 → (x−2)(x−3) = 0 → x = 2 or x = 4")
        self.assertEqual(v, ["STEP_OK", "ANSWER_WRONG"])
        self.assertEqual(found[1]["step"], 2)

    def test_root_losing_step_is_a_warning_not_wrong(self):
        v, found = steps("x² = 3x → x = 3")
        self.assertIn("WARNING", v)
        self.assertFalse(FLAGS & set(v))
        self.assertIn("dividing", [f for f in found
                                   if f["verdict"] == "WARNING"][0]["reason"])

    def test_squaring_gains_roots_as_a_warning(self):
        v, found = steps("√(x + 2) = x → x + 2 = x² → x = 2 or x = −1")
        warn = [f for f in found if f["verdict"] == "WARNING"]
        self.assertEqual(len(warn), 1)
        self.assertIn("squaring", warn[0]["reason"])
        self.assertFalse(FLAGS & set(v))

    def test_gibberish_is_unparseable(self):
        v, _ = steps("x² + 3x = (x + 2)((x − ")
        self.assertEqual(v, ["UNPARSEABLE"])
        v, _ = steps("2x +* 3 = 7")
        self.assertEqual(v, ["UNPARSEABLE"])

    def test_numeric_equals_chain(self):
        v, _ = steps("2(−1)² + 5(−1) + 3 = 2 − 5 + 3 = 0 ✓")
        self.assertEqual(v, ["STEP_OK", "STEP_OK"])
        v, found = steps("Range = 140 − 20 = 110 minutes")
        self.assertEqual(v, ["STEP_WRONG"])

    def test_identity_claims(self):
        self.assertEqual(steps("a^m × a^n = a^(m+n)")[0], ["STEP_OK"])
        self.assertEqual(steps("a^m × a^n = a^(mn)")[0], ["STEP_WRONG"])

    def test_unit_conversion_and_percent_labels_are_not_flagged(self):
        v, _ = steps("1 m = 1 000 mm", lit=True)
        self.assertFalse(FLAGS & set(v))
        v, _ = steps("Percentage = 34/60 × 100 = 56,67%")
        self.assertEqual(v, ["STEP_OK"])
        v, _ = steps("1 cm = 50 cm = 0,5 m", lit=True)
        self.assertFalse(FLAGS & set(v))


@unittest.skipIf(mv is None, "sympy not installed")
class TruthNotMethodTests(unittest.TestCase):
    """The checker judges whether each stated step is TRUE, never the route."""

    def test_guess_and_check_route_passes(self):
        v, _ = steps("Solve x² − 5x + 6 = 0 by guess-and-check: try x = 2: "
                     "4 − 10 + 6 = 0 ✓; try x = 3: 9 − 15 + 6 = 0 ✓. "
                     "So x = 2 or x = 3.")
        self.assertIn("STEP_OK", v)
        self.assertFalse(FLAGS & set(v))
        self.assertNotIn("WARNING", v)

    def test_big_jump_and_non_textbook_order_pass(self):
        v, _ = steps("x² − 5x + 6 = 0 → x = 2 or x = 3")  # one leap
        self.assertEqual(v, ["STEP_OK"])
        v, _ = steps("−2x + 6 = (1/2)x − 4 → 10 = (5/2)x → 5x = 20 → x = 4")
        self.assertEqual(set(v) - {"SKIPPED"}, {"STEP_OK"})

    def test_mental_shortcut_passes(self):
        v, _ = steps("99 × 12 = 100 × 12 − 12 = 1 188")
        self.assertEqual(v, ["STEP_OK", "STEP_OK"])

    def test_arrow_between_values_is_never_judged(self):
        # 'maps to' / 'next term' / derivative arrows are not rewrites
        for text in ("5 → 10 → 20 → 40", "x² → 2x", "7 cm → 3,5 km"):
            v, _ = steps(text)
            self.assertFalse(FLAGS & set(v), text)

    def test_error_example_is_never_flagged(self):
        v, _ = spoken("A common mistake: learners write that two plus two "
                      "is five.")
        self.assertFalse(FLAGS & set(v))


@unittest.skipIf(mv is None, "sympy not installed")
class SpokenMathsTests(unittest.TestCase):
    def test_spoken_chain_ok_and_wrong_answer(self):
        self.assertEqual(spoken("So x plus one equals three, which gives x "
                                "equals two.")[0], ["STEP_OK"])
        self.assertEqual(spoken("So x plus one equals three, which gives x "
                                "equals five.")[0], ["ANSWER_WRONG"])

    def test_spoken_numeric_fact(self):
        self.assertEqual(spoken("Multiply: four times four is sixteen.")[0],
                         ["STEP_OK"])
        self.assertEqual(spoken("Multiply: four times four is fifteen.")[0],
                         ["STEP_WRONG"])

    def test_spoken_factorisation_identity(self):
        v, _ = spoken("The factorisation: six x squared minus seven x minus "
                      "three equals the quantity two x minus three, times the "
                      "quantity three x plus one.")
        self.assertEqual(v, ["STEP_OK"])

    def test_spoken_two_roots_in_one_breath(self):
        v, _ = spoken("So x squared minus five x plus six equals zero, which "
                      "gives x equals two or x equals three.")
        self.assertEqual(v, ["STEP_OK"])

    def test_unhandled_vocabulary_is_never_flagged(self):
        v, _ = spoken("Half of six is three, and sine thirty is one half.")
        self.assertFalse(FLAGS & set(v))

    def test_factorise_task_answer(self):
        ok = mv._spoken_task_answer(
            "Factorise six x squared minus seven x minus three. Split the "
            "middle term. Two x minus three, times three x plus one.", 4)
        self.assertEqual([f["verdict"] for f in ok], ["STEP_OK"])
        bad = mv._spoken_task_answer(
            "Factorise six x squared minus seven x minus three. Split the "
            "middle term. Two x plus three, times three x plus one.", 4)
        self.assertEqual([f["verdict"] for f in bad], ["ANSWER_WRONG"])
        self.assertEqual(bad[0]["line"], 4)


MANIM = """from manim import *

class S(MovingCameraScene):
    def construct(self):
        # --- Band 0 (subtopic_1): the equation
        a = MathTex(r"3x + 1 = 7")
        b = MathTex(r"3x = 6 \\Rightarrow x = 2")
        # --- Band 1 (subtopic_2): the error museum
        w = MathTex(r"\\sqrt{9 + 16} = 3 + 4 = 7")
        self.play(Create(strike(w)))
        c = MathTex(r"\\frac{54^\\circ}{360^\\circ} = 0{,}15 = 15\\%")
"""


def lesson(tmp, narration):
    d = Path(tmp) / "maths" / "session" / "grade10" / "term1" / "t" / "l"
    d.mkdir(parents=True)
    (d / "script.md").write_text(
        "# Part 1 — Expert\n\n## Subtopic: One\n\n" + narration +
        "\n\n## Subtopic: Two\n\nSquare roots do not split over plus.\n",
        encoding="utf-8")
    (d / "manim_scene.py").write_text(MANIM, encoding="utf-8")
    return d


@unittest.skipIf(mv is None, "sympy not installed")
class AnimationAndConsistencyTests(unittest.TestCase):
    def test_animation_steps_and_struck_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = lesson(tmp, "Three x plus one equals seven, so x equals two.")
            found = mv.check_manim(d / "manim_scene.py")
            verdicts = [f["verdict"] for f in found]
            self.assertIn("STEP_OK", verdicts)
            self.assertFalse(FLAGS & set(verdicts))  # the struck line is skipped
            self.assertEqual(
                [f["line"] for f in found if f["verdict"] == "STEP_OK"
                 and f["kind"] == "equals-chain"], [11, 11])

    def test_narration_matching_screen_with_other_wording(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = lesson(tmp, "Take one away from both sides: three x plus one "
                            "equals seven, which gives x equals two.")
            found = mv.check_consistency(d / "script.md", d / "manim_scene.py")
            self.assertEqual([f["verdict"] for f in found], ["CONSISTENT"])

    def test_narration_contradicting_screen(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = lesson(tmp, "Three x plus one equals seven, so x equals three.")
            found = mv.check_consistency(d / "script.md", d / "manim_scene.py")
            self.assertEqual([f["verdict"] for f in found],
                             ["CONTRADICTS_SCREEN"])
            self.assertEqual(found[0]["line"], 5)

    def test_cli_steps_only_exits_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            lesson(tmp, "So x plus one equals three, which gives x equals five.")
            out = Path(tmp) / "s.json"
            rc = mv.main(["--steps-only", "--root", tmp, "--steps-json", str(out),
                          "--steps-md", str(Path(tmp) / "s.md")])
            self.assertEqual(rc, 0)  # report-only
            report = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(report["totals"].get("ANSWER_WRONG"), 1)
            self.assertIn("script | maths grade10", report["by_type_grade"])


@unittest.skipIf(mv is None, "sympy not installed")
class AgentPrivacyTests(unittest.TestCase):
    def test_agent_rows_carry_no_text(self):
        secret = ("Factorise six x squared minus seven x minus three. Two x "
                  "plus three, times three x plus one.")
        sample = json.dumps({"samples": [{"id": "s1", "grade": 11,
                                          "script": secret}]}, indent=2)
        orig = (mv._agent_tree, mv._agent_get)
        mv._agent_tree = lambda repo, ref, token: [
            "lms/team/tutors/CAPS/tutor_x/samples.json"]
        mv._agent_get = lambda repo, path, ref, token: sample
        try:
            rows = mv.check_agent(token="t")
        finally:
            mv._agent_tree, mv._agent_get = orig
        self.assertIn("ANSWER_WRONG", [r["verdict"] for r in rows])
        for r in rows:
            self.assertEqual(r["text"], "")
            self.assertEqual(r["reason"], "")
            self.assertNotIn("six x", json.dumps(r))
            self.assertEqual(r["line"], 6)


if __name__ == "__main__":
    unittest.main()
