# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from manim import *

# Band layout: one frame-height band per teaching beat; the camera moves down,
# nothing is removed. Every mobject serializes to the exporter's
# text/line/rect/dot/circle vocabulary; every line of working is a
# single-string Tex/MathTex revealed with Write — no sub-part transforms.
#
# Covers all seven subtopics of the session duo (Part 1 — Expert: subtopics
# 1-4; Part 2 — Simplifier: subtopics 5-7), band time roughly proportional to
# subtopics.json (230/235/225/240/195/185/190 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class NumberPatternsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the three families ---
        title = Tex("Number Patterns and Growing Patterns").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        f1 = Tex(r"Constant difference: 17; 25; 33; 41 \; ($+8$)").scale(1.0).shift(UP * 1.1)
        f2 = Tex(r"Constant ratio: 4; 12; 36; 108 \; ($\times 3$)").scale(1.0).shift(UP * 0.2)
        f3 = Tex(r"Growing step: 1; 3; 6; 10 \; (steps 2, 3, 4)").scale(1.0).shift(DOWN * 0.7)
        self.play(Write(f1)); self.wait(2.5)
        self.play(Write(f2)); self.wait(2.5)
        self.play(Write(f3)); self.wait(2.5)
        f_rule = Tex("Naming the family is half the marks").scale(0.95).shift(DOWN * 1.8)
        self.play(Write(f_rule))
        self.wait(3)

        # --- Band 1 (subtopic_1): the vocabulary ---
        self.next_band(1)
        b1_title = Tex("The words the questions use").scale(1.1).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("TERMS: the numbers in the list").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("POSITION: first term, second term, ...").scale(1.0).shift(band_shift(1) + UP * 0.3)
        b1_l3 = Tex("CONSECUTIVE: terms standing side by side").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l1)); self.wait(2.5)
        self.play(Write(b1_l2)); self.wait(2.5)
        self.play(Write(b1_l3)); self.wait(2.5)
        b1_l4 = Tex("Describe in words: family $+$ number — add 8 each time").scale(0.9).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the difference row ---
        self.next_band(2)
        b2_title = Tex("The difference row — your first test").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_terms = MathTex(r"17 \quad 25 \quad 33 \quad 41").scale(1.15).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_terms))
        self.wait(2)
        b2_diffs = MathTex(r"+8 \qquad +8 \qquad +8").scale(1.0).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_diffs))
        self.wait(2.5)
        b2_l1 = MathTex(r"41 + 8 = 49; \quad 49 + 8 = 57").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l1)); self.wait(2.5)
        b2_l2 = Tex(r"Missing term: $25 + 8 = 33$ AND $41 - 8 = 33$").scale(0.95).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the tariff wrapper ---
        self.next_band(3)
        b3_title = Tex("Shuttle: R17 first km, R8 each extra km").scale(1.05).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"17; \; 25; \; 33; \; 41; \; 49; \; 57").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1)); self.wait(2.5)
        b3_l2 = Tex("Six kilometres: the SIXTH term").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2)); self.wait(2.5)
        b3_l3 = MathTex(r"\text{Cost} = R57").scale(1.15).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Answer inside the story — the rand sign is part of it").scale(0.9).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): the ratio test ---
        self.next_band(4)
        b4_title = Tex("When the differences refuse to settle").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_terms = MathTex(r"4 \quad 12 \quad 36 \quad 108").scale(1.15).shift(band_shift(4) + UP * 1.3)
        b4_diffs = MathTex(r"+8 \qquad +24 \qquad +72 \quad \text{(not constant)}").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_terms)); self.wait(2)
        self.play(Write(b4_diffs)); self.wait(2.5)
        b4_l1 = MathTex(r"12 \div 4 = 3; \; 36 \div 12 = 3; \; 108 \div 36 = 3").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2.5)
        b4_l2 = MathTex(r"\text{Next: } 108 \times 3 = 324; \; 324 \times 3 = 972").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l2))
        self.wait(3)

        # --- Band 5 (subtopic_3): same amount vs same factor ---
        self.next_band(5)
        b5_title = Tex("Same amount vs same factor").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Adding R8 forever: polite, predictable").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"Tripling: starts small, ends through the roof").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1)); self.wait(2.5)
        self.play(Write(b5_l2)); self.wait(2.5)
        b5_l3 = Tex("In the long run the ratio pattern wins — EVENTUALLY").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the stacked-rows table ---
        self.next_band(6)
        b6_title = Tex("Eight rows of cups: the running total").scale(1.1).shift(band_shift(6) + UP * 2.6)
        self.play(Write(b6_title))
        self.wait(1.5)
        rows = [
            (r"\text{Row } 1: \; 1", 1.7),
            (r"\text{Row } 2: \; 1 + 2 = 3", 1.0),
            (r"\text{Row } 3: \; 3 + 3 = 6", 0.3),
            (r"\text{Row } 4: \; 6 + 4 = 10", -0.4),
            (r"\text{Row } 5: \; 10 + 5 = 15", -1.1),
            (r"\text{Row } 6: \; 15 + 6 = 21", -1.8),
            (r"\text{Row } 7: \; 21 + 7 = 28", -2.5),
        ]
        for tex, y in rows:
            line = MathTex(tex).scale(0.85).shift(band_shift(6) + UP * y)
            self.play(Write(line))
            self.wait(1.5)
        last = MathTex(r"\text{Row } 8: \; 28 + 8 = 36").scale(0.9).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the pairing check and the trap ---
        self.next_band(7)
        b7_title = Tex("The pairing check — and the trap").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"1{+}8 = 9; \; 2{+}7 = 9; \; 3{+}6 = 9; \; 4{+}5 = 9").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l2 = MathTex(r"4 \times 9 = 36").scale(1.1).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1)); self.wait(2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_w = MathTex(r"\text{Answer: } 8 \quad \text{(the row, not the stack!)}").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_w))
        self.play(Create(strike(b7_w)))
        self.wait(2)
        b7_l3 = Tex("The display holds 36 cups — read what is counted").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l3))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the steady staircase ---
        self.next_band(8)
        b8_title = Tex("The same step every time").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = MathTex(r"17; \; 25; \; 33; \; 41 \quad (+8)").scale(1.05).shift(band_shift(8) + UP * 1.3)
        self.play(Write(b8_l1)); self.wait(3)
        b8_l2 = Tex("Subtract neighbours; when the gaps agree, add forward").scale(0.9).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2)); self.wait(3)
        b8_l3 = Tex("Missing term? Walk in from BOTH sides").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = Tex("Count positions on your fingers to term six: R57").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l3)); self.wait(3)
        self.play(Write(b8_l4)); self.wait(3.5)

        # --- Band 9 (subtopic_6): the clip that triples ---
        self.next_band(9)
        b9_title = Tex("The pattern that multiplies").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = MathTex(r"4; \; 12; \; 36; \; 108 \quad (\times 3)").scale(1.05).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1)); self.wait(3)
        b9_l2 = Tex("Starts behind the staircase, then leaves it for dead").scale(0.9).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2)); self.wait(3)
        b9_l3 = Tex("Test order: subtract first; gaps unequal? divide").scale(0.95).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): cans at the shop ---
        self.next_band(10)
        b10_title = Tex("Cans at the shop").scale(1.15).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = MathTex(r"\text{Totals: } 1; 3; 6; 10; 15; 21; 28; 36").scale(0.95).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1)); self.wait(3)
        b10_l2 = Tex("Gaps grow by one — every row is one can longer").scale(0.9).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2)); self.wait(3)
        b10_l3 = MathTex(r"\text{Pairs: } 4 \times 9 = 36 \text{ cans}").scale(1.05).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(3)
        b10_l4 = Tex("Row 8 holds 8; the DISPLAY holds 36 — answer the stack").scale(0.9).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.wait(4)
