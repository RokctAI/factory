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

# Band layout: one frame-height band per teaching beat; the camera moves down
# to fresh space and earlier work stays on the canvas. Only exporter-supported
# mobjects; every line of working is a single-string MathTex revealed with
# Write — no sub-part transforms.
#
# Mirrors script.md across all seven subtopics (Part 1 — Expert: 1-4;
# Part 2 — Simplifier: 5-7), band time roughly proportional to subtopics.json
# (215/210/240/245/185/190/190 of 1475 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RationalExponentsAndSurdsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the definition and two evaluations
        title = Tex("Rational Exponents and Surds").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"x^{\frac{p}{q}} = \left(\sqrt[q]{x}\right)^{p}, \quad x > 0").scale(1.1).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex(r"Bottom = root, \; top = power").scale(1.0).shift(DOWN * 0.1)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_l3 = MathTex(r"81^{\frac{3}{4}} = (3^4)^{\frac{3}{4}} = 3^3 = 27").scale(1.05).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = MathTex(r"8^{-\frac{2}{3}} = \frac{1}{8^{\frac{2}{3}}} = \frac{1}{2^2} = \frac{1}{4}").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): roots never split a sum
        self.next_band(1)
        b1_wrong = MathTex(r"\sqrt{36 + 64} = 6 + 8 = 14").scale(1.05).shift(band_shift(1) + UP * 1.6)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l1 = MathTex(r"\sqrt{36 + 64} = \sqrt{100} = 10").scale(1.05).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2.5)
        b1_l2 = Tex(r"Roots distribute over $\times$ and $\div$ — never $+$ or $-$").scale(0.95).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"(81x^{12})^{\frac{3}{4}} = 27x^9").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.wait(3)

        # --- Band 2 (subtopic_2): family one — common prime base
        self.next_band(2)
        b2_title = Tex(r"Simplify $\dfrac{4^{x+2} \cdot 2^{3x-1}}{8^{x}}$").scale(1.0).shift(band_shift(2) + UP * 2.1)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"4 = 2^2, \quad 8 = 2^3").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"\frac{2^{2x+4} \cdot 2^{3x-1}}{2^{3x}} = 2^{(5x+3) - 3x}").scale(1.0).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"= 2^{2x+3}").scale(1.1).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): family two — factor the smaller power out
        self.next_band(3)
        b3_title = Tex(r"Simplify $\dfrac{5^{x+2} - 5^{x}}{8 \cdot 5^{x}}$").scale(1.0).shift(band_shift(3) + UP * 2.1)
        self.play(Write(b3_title))
        self.wait(2)
        b3_wrong = MathTex(r"5^{x+2} = 5^x + 25").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l1 = MathTex(r"5^{x+2} = 25 \cdot 5^x").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\frac{5^x(25 - 1)}{8 \cdot 5^x} = \frac{24}{8} = 3").scale(1.0).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex(r"$+$ or $-$ between powers: factorise, never add exponents").scale(0.85).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l3))
        self.wait(3)

        # --- Band 4 (subtopic_3): same base, then reciprocal powers
        self.next_band(4)
        b4_l1 = MathTex(r"2^{3x+1} = 32 = 2^5 \;\Rightarrow\; 3x + 1 = 5 \;\Rightarrow\; x = \tfrac{4}{3}").scale(0.9).shift(band_shift(4) + UP * 1.9)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"x^{\frac{3}{4}} = 8 \;\Rightarrow\; x = 8^{\frac{4}{3}} = 2^4 = 16").scale(0.95).shift(band_shift(4) + UP * 0.8)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"x^{\frac{2}{3}} = 9 \;\Rightarrow\; x^2 = 729 \;\Rightarrow\; x = \pm 27").scale(0.95).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex(r"Even numerator: BOTH signs survive the check").scale(0.9).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): the hidden quadratic
        self.next_band(5)
        b5_title = Tex(r"Solve $2^{2x} - 6 \cdot 2^{x} + 8 = 0$").scale(1.05).shift(band_shift(5) + UP * 2.1)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\text{Let } k = 2^x: \quad k^2 - 6k + 8 = 0").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"(k - 2)(k - 4) = 0 \;\Rightarrow\; k = 2 \text{ or } 4").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"2^x = 2 \Rightarrow x = 1; \quad 2^x = 4 \Rightarrow x = 2").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex(r"A negative $k$? Reject in writing: $2^x > 0$ always").scale(0.9).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): simplify and combine surds
        self.next_band(6)
        b6_l1 = MathTex(r"\sqrt{75} = \sqrt{25 \times 3} = 5\sqrt{3}").scale(1.0).shift(band_shift(6) + UP * 1.9)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"2\sqrt{27} - \sqrt{75} + \sqrt{12} = 6\sqrt{3} - 5\sqrt{3} + 2\sqrt{3}").scale(0.9).shift(band_shift(6) + UP * 0.8)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"= 3\sqrt{3}").scale(1.1).shift(band_shift(6) + DOWN * 0.2)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = MathTex(r"(3\sqrt{2} - 1)(\sqrt{2} + 5) = 1 + 14\sqrt{2}").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): rationalise, then the surd equation
        self.next_band(7)
        b7_l1 = MathTex(r"\frac{5}{\sqrt{3}} = \frac{5\sqrt{3}}{3}").scale(1.0).shift(band_shift(7) + UP * 2.0)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"\frac{8}{\sqrt{7} - \sqrt{3}} \times \frac{\sqrt{7} + \sqrt{3}}{\sqrt{7} + \sqrt{3}} = \frac{8(\sqrt{7} + \sqrt{3})}{4} = 2\sqrt{7} + 2\sqrt{3}").scale(0.85).shift(band_shift(7) + UP * 0.9)
        self.play(Write(b7_l2))
        self.wait(3)
        b7_l3 = MathTex(r"\sqrt{x + 11} = x - 1 \;\Rightarrow\; x^2 - 3x - 10 = 0").scale(0.95).shift(band_shift(7) + DOWN * 0.2)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"x = 5 \text{ or } x = -2").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_wrong = MathTex(r"x = -2: \;\; \sqrt{9} = 3 \neq -3").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2)
        b7_l5 = MathTex(r"\text{Only } x = 5").scale(1.0).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): half a doubling
        self.next_band(8)
        b8_title = Tex("Half a doubling").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Views double daily: day 1 $\times 2$, day 2 $\times 2^2$, day 3 $\times 2^3$").scale(0.85).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\text{Half a day: } 2^{\frac{1}{2}} = \sqrt{2}, \;\text{ since } \sqrt{2} \times \sqrt{2} = 2").scale(0.9).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex(r"Bottom: how many equal steps. Top: how many you take").scale(0.85).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = MathTex(r"81^{\frac{3}{4}}: \;\; \sqrt[4]{81} = 3, \;\; 3^3 = 27").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): everything in the same currency
        self.next_band(9)
        b9_title = Tex("Everything in the same currency").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"2^{3x+1} = 32 = 2^5 \;\Rightarrow\; 3x + 1 = 5").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"4, 8, 16 are all notes of the currency 2").scale(0.9).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\frac{5^x(25-1)}{8 \cdot 5^x} = 3 \quad \text{(the } 5^x \text{ cancels)}").scale(0.9).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"k = 2^x: \; k^2 - 6k + 8 = 0 \Rightarrow x = 1 \text{ or } 2").scale(0.9).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): tidying the awkward bottom
        self.next_band(10)
        b10_title = Tex("Tidying the awkward bottom").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"\sqrt{75} = 5\sqrt{3}: \;\text{roll the loose change}").scale(0.9).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"6\sqrt{3} - 5\sqrt{3} + 2\sqrt{3} = 3\sqrt{3}").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"\frac{8}{\sqrt{7} - \sqrt{3}} \;\to\; \text{conjugate } \sqrt{7} + \sqrt{3} \;\to\; 2\sqrt{7} + 2\sqrt{3}").scale(0.85).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex(r"Squared an equation? March every answer back to the original").scale(0.8).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l4))
        self.wait(4)
