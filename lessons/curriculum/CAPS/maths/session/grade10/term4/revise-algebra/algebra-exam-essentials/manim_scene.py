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
# (235/240/230/250/185/190/170 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AlgebraExamEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the decision tree, questions 1 and 2
        title = Tex("Algebra Exam Essentials").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Factorising tree: common factor FIRST").scale(1.05).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"3x^2 - 12 = 3(x^2 - 4)").scale(1.15).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = MathTex(r"= 3(x-2)(x+2)").scale(1.15).shift(DOWN * 0.8)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)
        b0_l4 = Tex(r"A SUM of squares, $x^2+4$, does not split").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = MathTex(r"9x^2 - 25 = (3x-5)(3x+5)").scale(1.05).shift(DOWN * 2.7)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): trinomials, cubes, the tree in one breath
        self.next_band(1)
        b1_l1 = MathTex(r"x^2 - 5x - 14: \; -7 \times 2 = -14, \; -7 + 2 = -5").scale(0.95).shift(band_shift(1) + UP * 2.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"= (x-7)(x+2)").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"2x^2 + 5x - 3 = (2x-1)(x+3)").scale(1.05).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex(r"Multiply back out — the professional proof").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = MathTex(r"x^3 + 27 = (x+3)(x^2 - 3x + 9)").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l5))
        self.wait(2)
        b1_rule = Tex(r"Common factor, squares, trinomial, grouping").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_rule))
        self.play(Create(SurroundingRectangle(b1_rule, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): linear and quadratic types
        self.next_band(2)
        b2_l1 = MathTex(r"\text{Linear: } 5x - 7 = 2x + 8 \Rightarrow x = 5").scale(0.95).shift(band_shift(2) + UP * 2.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_t = Tex(r"Quadratic: $x^2 = 5x + 6$ — everything to zero").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l2 = MathTex(r"x^2 - 5x - 6 = 0 \Rightarrow (x-6)(x+1) = 0").scale(1.05).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"x = 6 \quad \text{or} \quad x = -1").scale(1.1).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_wrong = MathTex(r"x^2 = 5x \; \xrightarrow{\div x} \; x = 5").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(1.5)
        b2_l4 = MathTex(r"x(x-5) = 0: \; x = 0 \text{ or } 5").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): exponential equations
        self.next_band(3)
        b3_title = Tex("Exponential: force the same base").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"3^x = 81 = 3^4 \;\Rightarrow\; x = 4").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2.5)
        b3_l2 = MathTex(r"5 \times 2^x = 40").scale(1.1).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"2^x = 8 = 2^3 \;\Rightarrow\; x = 3").scale(1.1).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex(r"Divide the 5 away first: $5 \times 2^x \neq 10^x$").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_rule = Tex(r"Classify first: squared, upstairs, or plain").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_rule))
        self.wait(3)

        # --- Band 4 (subtopic_3): the flip
        self.next_band(4)
        b4_title = Tex("Inequalities: the flip").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"-2x + 6 > 12").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"-2x > 6").scale(1.1).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\div(-2): \quad x < -3").scale(1.1).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex(r"$3 < 5$ but $-3 > -5$: negatives mirror the line").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex(r"Only negative $\times$ and $\div$ flip — never $+$ or $-$").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the fence and the number line
        self.next_band(5)
        b5_l1 = MathTex(r"-3 \le 2x + 1 < 7").scale(1.1).shift(band_shift(5) + UP * 2.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"-4 \le 2x < 6").scale(1.1).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"-2 \le x < 3").scale(1.15).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        nline = Line(LEFT * 3.2, RIGHT * 3.2).shift(band_shift(5) + DOWN * 1.1)
        self.play(Create(nline))
        filled = Dot(LEFT * 1.6 + DOWN * 1.1).shift(band_shift(5))
        openc = Circle(radius=0.12, color=WHITE).shift(band_shift(5) + RIGHT * 1.6 + DOWN * 1.1)
        seg = Line(LEFT * 1.6 + DOWN * 1.1, RIGHT * 1.45 + DOWN * 1.1, stroke_width=8, color=YELLOW).shift(band_shift(5))
        self.play(FadeIn(filled))
        self.play(Create(openc))
        self.play(Create(seg))
        lbl_m2 = MathTex(r"-2").scale(0.9).shift(band_shift(5) + LEFT * 1.6 + DOWN * 1.7)
        lbl_3 = MathTex(r"3").scale(0.9).shift(band_shift(5) + RIGHT * 1.6 + DOWN * 1.7)
        self.play(Write(lbl_m2), Write(lbl_3))
        self.wait(2)
        b5_l4 = Tex(r"Filled dot: included. Open dot: excluded. $[-2; 3)$").scale(0.95).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): exponent laws rapid-fire
        self.next_band(6)
        b6_title = Tex("Exponent laws, rapid-fire").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"x^3 \times x^4 = x^7 \qquad \frac{6x^5}{2x^2} = 3x^3").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"(2x^3)^2 = 4x^6 \qquad a^0 = 1 \qquad x^{-2} = \tfrac{1}{x^2}").scale(0.95).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_wrong = MathTex(r"x^3 + x^4 = x^7").scale(1.1).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_l3 = Tex(r"No law for sums — only like terms combine").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex(r"And $2^x \times 3$ never becomes $6^x$").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the integrated question
        self.next_band(7)
        b7_title = Tex("Topics chain together").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"2^{x+1} = 16 = 2^4").scale(1.1).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"x + 1 = 4 \;\Rightarrow\; x = 3").scale(1.1).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = MathTex(r"\frac{x^2 - 9}{x + 3} = \frac{(x-3)(x+3)}{x+3}").scale(1.05).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"= x - 3, \quad x \neq -3").scale(1.1).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        b7_rule = Tex(r"Only whole brackets cancel — never terms").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_rule))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): four drawers in one toolbox
        self.next_band(8)
        b8_title = Tex("Four drawers in one toolbox").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"1. Factorise — take-apart tools, in order").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex(r"2. Solve — one tool per species of $x$").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex(r"3. Inequalities — plus the red flip sticker").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex(r"4. Exponents — five laws, never on sums").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex(r"Read the label, name the drawer, then open it").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3.5)

        # --- Band 9 (subtopic_6): untying the linear knot
        self.next_band(9)
        b9_title = Tex("Untie the knot in reverse").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"5x - 7 = 2x + 8").scale(1.1).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"3x - 7 = 8").scale(1.1).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"3x = 15").scale(1.1).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"x = 5").scale(1.15).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_rule = Tex(r"A balanced scale: both sides, every move").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_rule))
        self.wait(3)

        # --- Band 10 (subtopic_6): zero's magic and the same-base move
        self.next_band(10)
        b10_l1 = Tex(r"Things multiply to zero only THROUGH a zero").scale(1.0).shift(band_shift(10) + UP * 2.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"(x-6)(x+1) = 0 \Rightarrow x = 6 \text{ or } -1").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex(r"A quadratic question expects BOTH answers").scale(1.0).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = MathTex(r"2^x = 8 = 2^3 \;\Rightarrow\; x = 3").scale(1.1).shift(band_shift(10) + DOWN * 1.0)
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex(r"Coefficient in the way? Divide it off first").scale(1.0).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_7): the final sweep
        self.next_band(11)
        b11_title = Tex("The final sweep: traps and the last check").scale(1.1).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex(r"1. Cancel factors, never terms — factorise first").scale(0.95).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11_l1))
        self.wait(2)
        b11_l2 = Tex(r"2. Never divide by $x$ — a solution dies").scale(0.95).shift(band_shift(11) + UP * 0.4)
        self.play(Write(b11_l2))
        self.wait(2)
        b11_l3 = Tex(r"3. Divide by a negative? Circle and flip").scale(0.95).shift(band_shift(11) + DOWN * 0.4)
        self.play(Write(b11_l3))
        self.wait(2)
        b11_l4 = Tex(r"4. No exponent law for sums").scale(0.95).shift(band_shift(11) + DOWN * 1.2)
        self.play(Write(b11_l4))
        self.wait(2)
        b11_l5 = Tex(r"Substitute back: $5(5)-7 = 18 = 2(5)+8$ \checkmark").scale(0.95).shift(band_shift(11) + DOWN * 2.1)
        self.play(Write(b11_l5))
        self.play(Create(SurroundingRectangle(b11_l5, color=GREEN)))
        self.wait(4)
