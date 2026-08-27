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

# Band layout: one frame-height band per teaching beat; the camera moves down
# to fresh space and earlier work stays on the canvas. Only exporter-supported
# mobjects; every line of working is a single-string MathTex revealed with
# Write — no sub-part transforms.
#
# Mirrors script.md across all seven subtopics (Part 1 — Expert: 1-4;
# Part 2 — Simplifier: 5-7), band time roughly proportional to subtopics.json
# (225/225/220/235/190/190/185 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CompletingSquareFormulaSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the perfect-square pattern
        title = Tex("Completing the Square and the Formula").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"(x + b)^2 = x^2 + 2bx + b^2").scale(1.15).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex(r"The constant is the square of HALF the middle").scale(1.0).shift(DOWN * 0.1)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = MathTex(r"x^2 + 6x + 9 = (x + 3)^2").scale(1.1).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = MathTex(r"x^2 - 10x + 25 = (x - 5)^2").scale(1.1).shift(DOWN * 2.1)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex(r"Inside the bracket: the half, not the square").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): solve x^2 + 6x + 2 = 0
        self.next_band(1)
        b1_title = Tex(r"Solve $x^2 + 6x + 2 = 0$ — it won't factorise").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"x^2 + 6x = -2").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"x^2 + 6x + 9 = 7 \quad \text{(add 9 BOTH sides)}").scale(1.0).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"(x + 3)^2 = 7").scale(1.1).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"x + 3 = \pm\sqrt{7}").scale(1.1).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = MathTex(r"x = -3 + \sqrt{7} \;\text{ or }\; x = -3 - \sqrt{7}").scale(1.05).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_1 -> 2): graph form, then a not one
        self.next_band(2)
        b2_l1 = MathTex(r"x^2 + 6x + 2 = (x+3)^2 - 9 + 2 = (x+3)^2 - 7").scale(0.95).shift(band_shift(2) + UP * 2.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = Tex(r"Turning point read straight off: $(-3; -7)$").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_t = Tex(r"Solve $2x^2 - 8x + 5 = 0$: divide by 2 first").scale(1.05).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l3 = MathTex(r"x^2 - 4x = -\tfrac{5}{2}").scale(1.05).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"x^2 - 4x + 4 = \tfrac{3}{2} \;\Rightarrow\; (x-2)^2 = \tfrac{3}{2}").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = MathTex(r"x = 2 \pm \tfrac{\sqrt{6}}{2} \approx 3{,}22 \text{ or } 0{,}78").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the expression form and the trap
        self.next_band(3)
        b3_title = Tex(r"Rewrite $y = 2x^2 - 8x + 5$: factor 2 out").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"y = 2(x^2 - 4x) + 5").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"y = 2\left[(x-2)^2 - 4\right] + 5").scale(1.05).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_wrong = MathTex(r"y = 2(x-2)^2 - 4 + 5").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l3 = MathTex(r"y = 2(x-2)^2 - 8 + 5 = 2(x-2)^2 - 3").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex(r"TP $(2; -3)$; the 2 multiplies EVERYTHING inside").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): derivation, first half
        self.next_band(4)
        b4_title = Tex("Deriving the formula: the six lines").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"ax^2 + bx + c = 0, \quad a \neq 0").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"x^2 + \tfrac{b}{a}x = -\tfrac{c}{a}").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"x^2 + \tfrac{b}{a}x + \tfrac{b^2}{4a^2} = \tfrac{b^2 - 4ac}{4a^2}").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = MathTex(r"\left(x + \tfrac{b}{2a}\right)^2 = \tfrac{b^2 - 4ac}{4a^2}").scale(1.05).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): derivation, second half
        self.next_band(5)
        b5_l1 = MathTex(r"x + \tfrac{b}{2a} = \pm\tfrac{\sqrt{b^2 - 4ac}}{2a}").scale(1.1).shift(band_shift(5) + UP * 1.8)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(1.25).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(3)
        b5_l3 = Tex(r"The $2a$ divides the WHOLE numerator, $-b$ included").scale(0.95).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex(r"$b^2 - 4ac$ is the discriminant — it decides").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        b5_l5 = Tex(r"whether real solutions exist").scale(0.95).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): using the formula
        self.next_band(6)
        b6_title = Tex(r"Solve $3x^2 - 7x + 1 = 0$").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"a = 3, \quad b = -7, \quad c = 1").scale(1.05).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"b^2 - 4ac = 49 - 12 = 37").scale(1.05).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"x = \frac{7 \pm \sqrt{37}}{6} \quad \text{(exact)}").scale(1.1).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = MathTex(r"x \approx 2{,}18 \;\text{ or }\; x \approx 0{,}15").scale(1.05).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex(r"$-b = +7$: negative $b$ turns positive — mind it").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): rounding and method choice
        self.next_band(7)
        b7_wrong = MathTex(r"\sqrt{37} \approx 6 \;\to\; x = 2{,}17").scale(1.05).shift(band_shift(7) + UP * 2.1)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2)
        b7_l1 = Tex(r"Round once, at the very end: $2{,}18$").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"-2x^2 + 5x + 3 = 0 \;\xrightarrow{\times(-1)}\; 2x^2 - 5x - 3 = 0").scale(0.95).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"b^2 - 4ac = 25 + 24 = 49 = 7^2").scale(1.05).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = MathTex(r"x = \frac{5 \pm 7}{4} = 3 \;\text{ or }\; -\tfrac{1}{2}").scale(1.05).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex(r"Perfect-square discriminant: it factorised!").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): paving the corner of the yard
        self.next_band(8)
        b8_title = Tex("Paving the corner of the yard").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        sq = Square(side_length=1.6).shift(band_shift(8) + LEFT * 2.2 + UP * 0.4)
        strip_r = Rectangle(width=0.6, height=1.6).shift(band_shift(8) + LEFT * 1.1 + UP * 0.4)
        strip_b = Rectangle(width=1.6, height=0.6).shift(band_shift(8) + LEFT * 2.2 + DOWN * 0.7)
        hole = Square(side_length=0.6, color=RED).shift(band_shift(8) + LEFT * 1.1 + DOWN * 0.7)
        self.play(Create(sq))
        lbl_x = MathTex(r"x^2").scale(0.9).shift(band_shift(8) + LEFT * 2.2 + UP * 0.4)
        self.play(Write(lbl_x))
        self.play(Create(strip_r), Create(strip_b))
        self.wait(2)
        b8_l1 = Tex(r"Split $6x$ into two strips of $3x$").scale(1.0).shift(band_shift(8) + RIGHT * 1.9 + UP * 0.9)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Create(hole))
        b8_l2 = Tex(r"The corner hole: $3 \times 3 = 9$").scale(1.0).shift(band_shift(8) + RIGHT * 1.9 + DOWN * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Halve the middle, square it — every time").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = MathTex(r"(x+3)^2 = 7 \Rightarrow x + 3 = \pm\sqrt{7}").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the recipe someone already cooked
        self.next_band(9)
        b9_title = Tex("The recipe someone already cooked").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"The formula IS completing the square, done once").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(1.15).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex(r"Read the price tags: $a = 3$, $b = -7$, $c = 1$").scale(1.0).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"-b = +7, \quad b^2 = +49 \; \text{(two minus signs)}").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex(r"``All over $2a$'': the bar carries everything").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): exact or rounded — say which
        self.next_band(10)
        b10_title = Tex("Exact or rounded — say which").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Exact: the root still standing, $\tfrac{7 \pm \sqrt{37}}{6}$").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex(r"Rounding is sealing the envelope: last thing").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Factorises easily? Factorise — fast and exact").scale(0.95).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex(r"Refuses? The formula never fails").scale(0.95).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex(r"Turning point wanted? Complete the square").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
