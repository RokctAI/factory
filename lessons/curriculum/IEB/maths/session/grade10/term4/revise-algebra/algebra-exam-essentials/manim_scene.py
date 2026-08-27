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


class AlgebraRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the factorising order
        title = Tex("Algebra Exam Essentials").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Order: common factor $\to$ squares $\to$ trinomial $\to$ grouping").scale(0.9).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = MathTex(r"5x^2 - 45 = 5(x^2 - 9) = 5(x-3)(x+3)").scale(1.0).shift(DOWN * 0.1)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_l3 = MathTex(r"x^2 + 3x - 28 = (x+7)(x-4)").scale(1.0).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = MathTex(r"x^3 - 8 = (x-2)(x^2 + 2x + 4)").scale(1.0).shift(DOWN * 2.1)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_2): three equation species
        self.next_band(1)
        b1_title = Tex("Three species, three strategies").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"6x - 5 = 2x + 19 \Rightarrow 4x = 24 \Rightarrow x = 6").scale(0.95).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"x^2 - 3x - 10 = 0 \Rightarrow (x-5)(x+2) = 0 \Rightarrow x = 5 \text{ or } -2").scale(0.85).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_w1 = MathTex(r"x^2 = 7x \;\xrightarrow{\div x}\; x = 7").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_w1))
        self.play(Create(strike(b1_w1)))
        self.wait(2)
        b1_l3 = MathTex(r"x(x - 7) = 0 \Rightarrow x = 0 \text{ or } 7").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l3))
        self.wait(3)

        # --- Band 2 (subtopic_3): inequalities and the mirror
        self.next_band(2)
        b2_title = Tex("Mind the mirror").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"-3x + 4 > 19 \Rightarrow -3x > 15").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\div(-3): \; x < -5 \; \text{(sign flips)}").scale(1.0).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = MathTex(r"-5 < 3x + 1 \le 10 \Rightarrow -2 < x \le 3").scale(0.95).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex(r"Open dot at $-2$, filled dot at $3$; interval $(-2; 3]$").scale(0.9).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_4): exponent laws and chains
        self.next_band(3)
        b3_title = Tex("Exponent laws and chained questions").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"x^4 \cdot x^2 = x^6, \quad (3x^2)^3 = 27x^6, \quad x^{-3} = \tfrac{1}{x^3}").scale(0.85).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_w1 = MathTex(r"x^4 + x^2 = x^6").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_w1))
        self.play(Create(strike(b3_w1)))
        self.wait(2)
        b3_l2 = MathTex(r"3^{x-2} = 27 = 3^3 \Rightarrow x - 2 = 3 \Rightarrow x = 5").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = MathTex(r"\tfrac{x^2 - 25}{x - 5} = \tfrac{(x-5)(x+5)}{x-5} = x + 5, \; x \neq 5").scale(0.9).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l3))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): the sorting desk
        self.next_band(4)
        b4_title = Tex("The sorting desk: four counters").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex(r"1. Factorise \; 2. Solve \; 3. Inequality \; 4. Exponents").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex(r"Route by label: `factorise', `solve $=$', `$<$ or $>$', powers").scale(0.9).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Say the counter's name, THEN open its procedure").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_6): rewinding the tape
        self.next_band(5)
        b5_title = Tex("Rewinding the tape").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"6x - 5 = 2x + 19 \to 4x - 5 = 19 \to 4x = 24 \to x = 6").scale(0.85).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex(r"Zero-product: factors hit zero only through a zero").scale(0.95).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"(x-5)(x+2) = 0 \Rightarrow x = 5 \text{ or } x = -2").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = MathTex(r"5^x = 125 = 5^3 \Rightarrow x = 3").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_7): trap patrol and the free proof
        self.next_band(6)
        b6_title = Tex("Trap patrol and the free proof").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Cancel only whole brackets; never divide by $x$").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex(r"Flip on negative division; no laws for sums").scale(0.95).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"x = 6: \; 6(6) - 5 = 31 = 2(6) + 19 \; \checkmark").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex(r"Substitute back, expand back, test a value — free proof").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(4)
