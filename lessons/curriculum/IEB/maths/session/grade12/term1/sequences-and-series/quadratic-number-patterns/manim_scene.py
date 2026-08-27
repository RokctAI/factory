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


class QuadraticNumberPatternsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the difference table verdict
        title = Tex("Quadratic Number Patterns").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"5;\; 9;\; 13;\; 17: \;\text{gaps } 4, 4, 4 \;\Rightarrow\; \text{linear}").scale(1.0).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = MathTex(r"T_n = 4n + 1").scale(1.1).shift(DOWN * 0.0)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"4;\; 11;\; 22;\; 37: \;\text{gaps } 7, 11, 15").scale(1.0).shift(DOWN * 1.0)
        self.play(Write(d3))
        self.wait(2)
        d4 = MathTex(r"\text{Second differences } 4, 4 \;\Rightarrow\; \text{quadratic}").scale(1.05).shift(DOWN * 2.0)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): the three-equation machine
        self.next_band(1)
        b1_title = Tex("Three equations recover $a$, $b$, $c$").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"2a = \text{second difference}").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"3a + b = \text{first gap}, \quad a + b + c = T_1").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"4;\, 11;\, 22;\, 37: \;\; 2a = 4 \Rightarrow a = 2").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"6 + b = 7 \Rightarrow b = 1, \quad 3 + c = 4 \Rightarrow c = 1").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = MathTex(r"T_n = 2n^2 + n + 1").scale(1.15).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): certify and use the formula
        self.next_band(2)
        b2_title = Tex("Certify, then reach far").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Test: } T_3 = 2(9) + 3 + 1 = 22 \;\checkmark").scale(1.05).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"T_{50} = 2(2500) + 50 + 1").scale(1.05).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"T_{50} = 5051").scale(1.15).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex("One line, no table to term fifty").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): which position holds 172
        self.next_band(3)
        b3_title = Tex(r"Which term equals 172?").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"2n^2 + n + 1 = 172 \;\Rightarrow\; 2n^2 + n - 171 = 0").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"(2n + 19)(n - 9) = 0").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"n = 9 \;\text{ or }\; n = -9{,}5 \;\text{(discard)}").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = MathTex(r"\text{Check: } T_9 = 162 + 9 + 1 = 172 \;\checkmark").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): the 250 trap
        self.next_band(4)
        b4_title = Tex(r"Is 250 a term?").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"2n^2 + n - 249 = 0").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\Delta = 1 + 1992 = 1993 \;\text{— not a perfect square}").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex(r"$n$ is not a natural number").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex("so 250 is NOT a term — write the sentence").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = MathTex(r"T_{10} = 211, \;\; T_{11} = 254 \;\text{— strides over 250}").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): hidden unknown in the terms
        self.next_band(5)
        b5_title = Tex(r"$x;\; 9;\; 22;\; 41$ with second difference 6").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\text{First diffs: } 9 - x, \; 13, \; 19").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\text{Second diffs: } 4 + x \;\text{ and }\; 6").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"4 + x = 6 \;\Rightarrow\; x = 2").scale(1.1).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = MathTex(r"2;\, 9;\, 22;\, 41 \;\Rightarrow\; T_n = 3n^2 - 2n + 1").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = MathTex(r"\text{Check: } T_4 = 48 - 8 + 1 = 41 \;\checkmark").scale(1.0).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the smallest term
        self.next_band(6)
        b6_title = Tex(r"The turning pattern $T_n = n^2 - 10n + 27$").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"18;\; 11;\; 6;\; 3;\; 2;\; 3;\; 6").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"\text{Vertex: } n = \tfrac{-b}{2a} = \tfrac{10}{2} = 5").scale(1.05).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"T_5 = 25 - 50 + 27 = 2").scale(1.1).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex("Vertex between positions? Test both neighbours").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): stacks where the gaps grow
        self.next_band(7)
        b7_title = Tex("Stacks where the gaps grow").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"\text{Tin displays: } 2;\; 6;\; 12;\; 20").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"\text{Gaps: } 4, \; 6, \; 8 \;\text{— growing by 2}").scale(1.05).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("A staircase that steepens by the same extra amount").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"\text{Next gap } 10 \;\Rightarrow\; \text{next display } 30").scale(1.05).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): three facts build the formula
        self.next_band(8)
        b8_title = Tex("Paving designs: 9; 20; 37; 60 stones").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\text{Gaps } 11, 17, 23; \;\text{ gaps of gaps } 6, 6").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"a = \tfrac{6}{2} = 3, \quad 9 + b = 11 \Rightarrow b = 2").scale(1.0).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"3 + 2 + c = 9 \Rightarrow c = 4").scale(1.05).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = MathTex(r"T_n = 3n^2 + 2n + 4").scale(1.15).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = MathTex(r"\text{Test } T_4 = 60 \;\checkmark, \quad T_{20} = 1244").scale(1.0).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): which stack holds 212 stones
        self.next_band(9)
        b9_title = Tex("Which design holds 212 stones?").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"3n^2 + 2n + 4 = 212 \;\Rightarrow\; 3n^2 + 2n - 208 = 0").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\Delta = 2500, \;\; n = \tfrac{-2 + 50}{6} = 8").scale(1.05).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{Tins } T_n = n^2 + n: \;\; 240 = 15 \times 16 \Rightarrow n = 15").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"150: \; T_{11} = 132, \; T_{12} = 156 \;\text{— skipped}").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.play(Create(strike(b9_l4)))
        self.wait(2)
        b9_l5 = Tex("Only a natural $n$ names a buildable design").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5))
        self.wait(4)
