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

from manim import *

# Band-layout whiteboard scene (see AUTHORING-SPEC / quadratics-by-factorisation
# worked example). One band per teaching beat, camera moves down, nothing is
# ever removed. Covers all seven subtopics of the session duo:
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
        # --- Band 0 (subtopic_1): linear recap — constant first difference
        title = Tex("Quadratic Number Patterns").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"3;\; 7;\; 11;\; 15").scale(1.2).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(1.5)
        d2 = MathTex(r"\text{First differences: } 4, \; 4, \; 4 \text{ — constant}").scale(1.05).shift(DOWN * 0.1)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"\text{Linear: } T_n = 4n - 1").scale(1.1).shift(DOWN * 1.1)
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(2)
        d4 = MathTex(r"\text{Test: } T_4 = 4(4) - 1 = 15 \;\checkmark").scale(1.0).shift(DOWN * 2.1)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): second differences — the quadratic verdict
        self.next_band(1)
        b1_title = Tex("The difference table verdict").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"6;\; 15;\; 28;\; 45").scale(1.2).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"\text{First differences: } 9, \; 13, \; 17 \text{ — not constant}").scale(1.0).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"\text{Second differences: } 13 - 9 = 4, \;\; 17 - 13 = 4").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"\text{Constant second difference: quadratic, } T_n = an^2 + bn + c").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three equations
        self.next_band(2)
        b2_title = Tex("Three equations recover $a$, $b$ and $c$").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"T_1 = a + b + c, \;\; T_2 = 4a + 2b + c, \;\; T_3 = 9a + 3b + c").scale(0.9).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"\text{Second difference} = 2a").scale(1.1).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = MathTex(r"T_2 - T_1 = 3a + b").scale(1.1).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"T_1 = a + b + c").scale(1.1).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Solve in order: $a$, then $b$, then $c$").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): running the machine on 6; 15; 28; 45
        self.next_band(3)
        b3_title = MathTex(r"6;\; 15;\; 28;\; 45").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"2a = 4 \;\Rightarrow\; a = 2").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"3a + b = 9 \;\Rightarrow\; b = 3").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"a + b + c = 6 \;\Rightarrow\; c = 1").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"T_n = 2n^2 + 3n + 1").scale(1.2).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = MathTex(r"T_3 = 18 + 9 + 1 = 28 \;\checkmark \qquad T_{50} = 5000 + 150 + 1 = 5151").scale(0.9).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): which position holds 190
        self.next_band(4)
        b4_title = Tex("Which term equals 190?").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"2n^2 + 3n + 1 = 190 \;\Rightarrow\; 2n^2 + 3n - 189 = 0").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"(2n + 21)(n - 9) = 0").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"n = 9 \;\text{ or }\; n = -10{,}5 \text{ (rejected: not natural)}").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("190 is the ninth term").scale(1.1).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = MathTex(r"\text{Check: } T_9 = 162 + 27 + 1 = 190 \;\checkmark").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): is 300 a term?
        self.next_band(5)
        b5_title = Tex("Is 300 a term?").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"2n^2 + 3n - 299 = 0").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\Delta = 9 + 2392 = 2401, \quad \sqrt{2401} = 49").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"n = \tfrac{-3 + 49}{4} = 11{,}5").scale(1.05).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.play(Create(strike(b5_l3)))
        self.wait(2)
        b5_l4 = Tex(r"$n$ is not a natural number, so 300 is NOT a term").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = MathTex(r"T_{11} = 276, \;\; T_{12} = 325 \text{ — the pattern jumps over } 300").scale(0.95).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): hidden unknown in the terms
        self.next_band(6)
        b6_title = Tex(r"Quadratic pattern $x;\; 13;\; 30;\; 53$, second difference 6").scale(1.0).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"\text{First differences: } 13 - x, \;\; 17, \;\; 23").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"17 - (13 - x) = 4 + x = 6 \;\Rightarrow\; x = 2").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        b6_l3 = MathTex(r"2;\; 13;\; 30;\; 53: \;\; 2a = 6, \; 3a + b = 11, \; a + b + c = 2").scale(0.9).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"T_n = 3n^2 + 2n - 3").scale(1.15).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = MathTex(r"\text{Check: } T_4 = 48 + 8 - 3 = 53 \;\checkmark").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the smallest term
        self.next_band(7)
        b7_title = Tex(r"Smallest term of $T_n = n^2 - 12n + 40$").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"29;\; 20;\; 13;\; 8;\; 5;\; 4;\; 5 \text{ — falls, bottoms out, rises}").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"n = \tfrac{-b}{2a} = \tfrac{12}{2} = 6").scale(1.1).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"T_6 = 36 - 72 + 40 = 4").scale(1.1).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex("Vertex between positions? Test the whole numbers either side").scale(0.9).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): stacks where the gaps grow
        self.next_band(8)
        b8_title = Tex("Stacks where the gaps grow").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\text{Can stacks: } 1;\; 3;\; 6;\; 10").scale(1.1).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\text{Gaps: } 2, \; 3, \; 4 \text{ — growing by 1 each time}").scale(1.0).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("A staircase that steepens: quadratic, second difference 1").scale(0.95).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = MathTex(r"\text{Next gap 5, so next stack } 10 + 5 = 15").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): three facts build the formula
        self.next_band(9)
        b9_title = Tex("Patios: 5; 12; 23; 38 stones").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"\text{Gaps } 7, 11, 15; \quad \text{gaps of gaps } 4, 4").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"a = \tfrac{4}{2} = 2, \quad 3a + b = 7 \Rightarrow b = 1, \quad a + b + c = 5 \Rightarrow c = 2").scale(0.85).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"T_n = 2n^2 + n + 2").scale(1.2).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = MathTex(r"T_4 = 32 + 4 + 2 = 38 \;\checkmark \qquad T_{20} = 800 + 20 + 2 = 822").scale(0.9).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): which stack holds the order
        self.next_band(10)
        b10_title = Tex("Which design uses exactly 212 stones?").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"2n^2 + n + 2 = 212 \;\Rightarrow\; (2n + 21)(n - 10) = 0 \;\Rightarrow\; n = 10").scale(0.9).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.play(Create(SurroundingRectangle(b10_l1, color=GREEN)))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{Cans: } \tfrac{n(n+1)}{2} = 120 \;\Rightarrow\; (n - 15)(n + 16) = 0 \;\Rightarrow\; n = 15").scale(0.9).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"100 \text{ cans? } T_{13} = 91, \;\; T_{14} = 105").scale(1.0).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.play(Create(strike(b10_l3)))
        self.wait(2.5)
        b10_l4 = Tex("The stacks jump from 91 to 105 — no stack holds 100").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Only a natural number $n$ names a real term").scale(1.0).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.wait(4)
