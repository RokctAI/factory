# Copyright (c) 2026 RokctAI
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

# Band-layout whiteboard scene. One band per teaching beat, camera moves down,
# nothing is ever removed. Covers all seven subtopics of the session duo:
# Part 1 — Expert (subtopics 1-4), Part 2 — Simplifier (subtopics 5-7),
# band time apportioned to subtopics.json (200/245/235/225/185/200/190 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ArithmeticSequencesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the constant difference test
        title = Tex("Arithmetic Sequences").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Each term = previous term + fixed number $d$").scale(1.1).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = MathTex(r"4;\; 11;\; 18;\; 25").scale(1.2).shift(DOWN * 0.1)
        self.play(Write(d2))
        self.wait(1.5)
        d3 = MathTex(r"11 - 4 = 7, \quad 18 - 11 = 7, \quad 25 - 18 = 7").scale(1.05).shift(DOWN * 1.1)
        self.play(Write(d3))
        self.wait(2)
        d4 = MathTex(r"\text{Constant difference: arithmetic, } d = 7").scale(1.1).shift(DOWN * 2.1)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): direction, thoroughness, labels
        self.next_band(1)
        b1_title = Tex("Two rules for the subtraction").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"31;\; 26;\; 21: \quad d = 26 - 31 = -5").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Negative $d$ is legal — the sequence decreases").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"3;\; 6;\; 12: \quad 6 - 3 = 3 \text{ but } 12 - 6 = 6").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.play(Create(strike(b1_l3)))
        self.wait(2)
        b1_l4 = Tex("Measure the gap more than once").scale(1.1).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = MathTex(r"\text{Labels: } a, \; d, \; T_n").scale(1.05).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): building the general term
        self.next_band(2)
        b2_title = Tex("The general term").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"T_1 = a, \;\; T_2 = a + d, \;\; T_3 = a + 2d").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"T_n = a + (n - 1)d").scale(1.25).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = MathTex(r"4;\, 11;\, 18;\, 25: \;\; T_n = 4 + (n-1)(7) = 7n - 3").scale(1.0).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"\text{Test: } T_4 = 7(4) - 3 = 25 \;\checkmark").scale(1.05).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = MathTex(r"T_{200} = 7(200) - 3 = 1397").scale(1.1).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): using T_n backwards
        self.next_band(3)
        b3_title = Tex(r"Is 88 a term? Is 150?").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"7n - 3 = 88: \;\; 7n = 91, \;\; n = 13").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("Yes: 88 is the thirteenth term").scale(1.1).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = MathTex(r"7n - 3 = 150 \;\Rightarrow\; n = \tfrac{153}{7} \approx 21{,}86").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex(r"$n$ is not a natural number").scale(1.05).shift(band_shift(3) + DOWN * 1.8)
        b3_l5 = Tex("so 150 is NOT a term — write the sentence").scale(1.05).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_2): recovering a and d from two terms
        self.next_band(4)
        b4_title = Tex(r"Given $T_4 = 19$ and $T_9 = 39$").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"a + 3d = 19").scale(1.1).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"a + 8d = 39").scale(1.1).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(1.5)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\text{Subtract: } 5d = 20 \;\Rightarrow\; d = 4, \; a = 7").scale(1.05).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"T_n = 4n + 3").scale(1.15).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = MathTex(r"\text{Check: } T_9 = 4(9) + 3 = 39 \;\checkmark").scale(1.05).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): unknowns in the terms
        self.next_band(5)
        b5_title = Tex(r"Consecutive terms: $x+3;\; 2x+1;\; 4x-5$").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Equal gaps: second $-$ first $=$ third $-$ second").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"(2x + 1) - (x + 3) = (4x - 5) - (2x + 1)").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"x - 2 = 2x - 6").scale(1.1).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = MathTex(r"x = 4").scale(1.1).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = MathTex(r"\text{Check: } 7;\; 9;\; 11 \text{ with } d = 2 \;\checkmark").scale(1.05).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_3): arithmetic means
        self.next_band(6)
        b6_title = Tex("Insert four arithmetic means between 3 and 18").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"3 \text{ is } T_1, \; 18 \text{ is } T_6: \quad 18 = 3 + 5d").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"5d = 15 \;\Rightarrow\; d = 3").scale(1.1).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"3;\; 6;\; 9;\; 12;\; 15;\; 18").scale(1.1).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex("Four means create FIVE jumps: means $+$ 1").scale(1.05).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = MathTex(r"\text{One mean of } 6 \text{ and } 20: \; \tfrac{6 + 20}{2} = 13").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): word problem — seedlings, term value
        self.next_band(7)
        b7_title = Tex(r"Rows: 12 seedlings first, 5 more each row").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"a = 12, \quad d = 5").scale(1.1).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"T_n = 12 + (n - 1)(5)").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"T_9 = 12 + 8 \times 5").scale(1.05).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = MathTex(r"T_9 = 52").scale(1.1).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("Row nine uses EIGHT increases, not nine").scale(1.05).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_4): word problem — position where value is reached
        self.next_band(8)
        b8_title = Tex(r"Which row first holds 92 seedlings?").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"12 + (n - 1)(5) = 92").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"(n - 1)(5) = 80").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"n - 1 = 16 \;\Rightarrow\; n = 17").scale(1.1).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("Row seventeen").scale(1.1).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Decimal $n$? Round UP to the next term, never nearest").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): steps of the same size
        self.next_band(9)
        b9_title = Tex("Steps of the same size").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("A staircase: every step the same rise $d$").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"4;\; 11;\; 18;\; 25 \quad \text{every step lifts by } 7").scale(1.05).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"3;\; 6;\; 12: \text{ gaps } 3 \text{ then } 6 \text{ — broken}").scale(1.05).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.play(Create(strike(b9_l3)))
        self.wait(2.5)
        b9_l4 = MathTex(r"31;\; 26;\; 21: \; d = 26 - 31 = -5").scale(1.05).shift(band_shift(9) + DOWN * 1.9)
        b9_l5 = Tex("A staircase to the basement — still arithmetic").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_6): jumping straight to term two hundred
        self.next_band(10)
        b10_title = Tex("The scooter fare: R4 first km, R7 per km after").scale(1.05).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"1 \text{ km}: 4, \quad 2 \text{ km}: 11, \quad 3 \text{ km}: 18").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"T_n = a + (n - 1)d = 7n - 3").scale(1.1).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = MathTex(r"\text{R}88: \; 7n - 3 = 88 \;\Rightarrow\; n = 13 \text{ km}").scale(1.05).shift(band_shift(10) + DOWN * 1.0)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = MathTex(r"\text{R}150: \; n \approx 21{,}86 \text{ — never on the display}").scale(1.0).shift(band_shift(10) + DOWN * 2.0)
        b10_l5 = Tex("The display steps from 144 to 151").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_7): the missing rung and the fair middle
        self.next_band(11)
        b11_title = Tex("The missing rung and the fair middle").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex("Ladder rule: gap below a rung $=$ gap above it").scale(1.0).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"x + 3;\; 2x + 1;\; 4x - 5 \;\Rightarrow\; x = 4").scale(1.05).shift(band_shift(11) + UP * 0.1)
        b11_l3 = MathTex(r"\text{Real rungs: } 7;\; 9;\; 11 \;\; (d = 2) \;\checkmark").scale(1.05).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l2))
        self.wait(2.5)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2.5)
        b11_l4 = Tex("Fence posts: 4 inserted means, FIVE equal spaces").scale(1.0).shift(band_shift(11) + DOWN * 1.9)
        self.play(Write(b11_l4))
        self.wait(2)
        b11_l5 = MathTex(r"\text{Fair middle of } 6 \text{ and } 20: \; 13").scale(1.05).shift(band_shift(11) + DOWN * 2.8)
        self.play(Write(b11_l5))
        self.wait(4)
