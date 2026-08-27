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

# Band-layout whiteboard scene for the session duo "Rational Exponents and
# Surds" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7).
# One band per teaching beat, camera moves down to clean space, nothing is
# ever removed. Only exporter-supported mobjects (Tex/MathTex/Line/
# SurroundingRectangle), write-only reveals — no sub-part transforms.
# Band dwell times follow subtopics.json (215/210/240/245/185/190/190 of
# 1475 s); Level 6 rescales to the real audio, so proportion is what matters.

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
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the definition, restriction, laws survive
        title = Tex("Rational Exponents and Surds").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        d1 = MathTex(r"x^{\frac{1}{q}} = \sqrt[q]{x}, \quad x > 0").scale(1.2).shift(UP * 0.9)
        d2 = MathTex(r"x^{\frac{p}{q}} = \sqrt[q]{x^p}").scale(1.2)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.wait(2)
        d3 = Tex("Bottom number = root, top number = power").scale(1.1).shift(DOWN * 1.1)
        d4 = Tex("Base stays positive; every exponent law survives").scale(1.05).shift(DOWN * 2.1)
        self.play(Write(d3))
        self.wait(2)
        self.play(Write(d4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): 16^(3/4) both routes, 27^(-2/3)
        self.next_band(1)
        b1_title = Tex(r"Evaluate $16^{3/4}$ and $27^{-2/3}$").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"16^{\frac{3}{4}} = (2^4)^{\frac{3}{4}} = 2^3 = 8").scale(1.15).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"\text{Root route: } \sqrt[4]{16} = 2, \quad 2^3 = 8").scale(1.1).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"27^{-\frac{2}{3}} = \frac{1}{27^{\frac{2}{3}}}").scale(1.15).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"27^{\frac{2}{3}} = (3^3)^{\frac{2}{3}} = 3^2 = 9").scale(1.1).shift(band_shift(1) + DOWN * 1.8)
        b1_l5 = MathTex(r"27^{-\frac{2}{3}} = \tfrac{1}{9} \;\text{ — never negative}").scale(1.05).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(1.5)
        self.play(Write(b1_l4))
        self.wait(1.5)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_1): variables, and the plus-sign trap
        self.next_band(2)
        b2_title = Tex("Variables, and the plus-sign trap").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"(16x^8)^{\frac{3}{4}} = 8x^6").scale(1.15).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2)
        b2_wrong = MathTex(r"\sqrt{9 + 16} = 3 + 4 = 7").scale(1.1).shift(band_shift(2))
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l2 = MathTex(r"\sqrt{9 + 16} = \sqrt{25} = 5").scale(1.15).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l2))
        self.wait(1.5)
        b2_rule = Tex(r"Roots split over $\times$ and $\div$, never over $+$").scale(1.1).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_rule))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): family 1 — common prime base
        self.next_band(3)
        b3_title = Tex(r"Simplify $\dfrac{9^{x+1} \times 3^{2x-1}}{27^x}$").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"9^{x+1} = 3^{2x+2}, \quad 27^x = 3^{3x}").scale(1.1).shift(band_shift(3) + UP * 1.0)
        b3_l2 = MathTex(r"= \frac{3^{2x+2} \times 3^{2x-1}}{3^{3x}}").scale(1.1).shift(band_shift(3))
        b3_l3 = MathTex(r"= 3^{4x+1-3x}").scale(1.1).shift(band_shift(3) + DOWN * 1.0)
        b3_l4 = MathTex(r"= 3^{x+1}").scale(1.15).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_2): family 2 — common factor
        self.next_band(4)
        b4_title = Tex(r"Simplify $\dfrac{2^{x+3} - 2^{x+1}}{3 \times 2^x}$").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_wrong = MathTex(r"2^{x+3} = 2^x + 8").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2)
        b4_l1 = MathTex(r"2^{x+3} = 2^x \times 8, \quad 2^{x+1} = 2^x \times 2").scale(1.05).shift(band_shift(4) + UP * 0.2)
        b4_l2 = MathTex(r"\text{numerator} = 2^x(8 - 2) = 6 \times 2^x").scale(1.1).shift(band_shift(4) + DOWN * 0.8)
        b4_l3 = MathTex(r"\frac{6 \times 2^x}{3 \times 2^x} = 2").scale(1.15).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        b4_rule = Tex("Plus or minus between powers? Factorise").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_rule))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): same base, and the reciprocal power
        self.next_band(5)
        b5_title = Tex("Unknown in the exponent: force one base").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"3^{2x-1} = 81 = 3^4").scale(1.15).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"2x - 1 = 4 \;\Rightarrow\; x = \tfrac{5}{2}").scale(1.15).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = MathTex(r"x^{\frac{3}{2}} = 27 \;\Rightarrow\; x = 27^{\frac{2}{3}} = 9").scale(1.1).shift(band_shift(5) + DOWN * 1.0)
        b5_l4 = MathTex(r"\text{Check: } 9^{\frac{3}{2}} = (\sqrt{9})^3 = 27").scale(1.1).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l3))
        self.wait(2.5)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_3): the even-numerator case
        self.next_band(6)
        b6_title = Tex(r"Even numerator: solve $x^{2/3} = 4$").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Cube both sides: } x^2 = 64").scale(1.15).shift(band_shift(6) + UP * 1.0)
        b6_l2 = MathTex(r"x = 8 \quad \text{or} \quad x = -8").scale(1.15).shift(band_shift(6))
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        b6_rule = Tex("Both survive the check — never drop the negative").scale(1.05).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_rule))
        self.wait(2.5)

        # --- Band 7 (subtopic_3): the hidden quadratic
        self.next_band(7)
        b7_title = Tex(r"Solve $3^{2x} - 10 \times 3^x + 9 = 0$").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"\text{Let } k = 3^x: \quad k^2 - 10k + 9 = 0").scale(1.1).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"(k - 1)(k - 9) = 0 \;\Rightarrow\; k = 1 \text{ or } k = 9").scale(1.05).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"3^x = 1 \;\Rightarrow\; x = 0").scale(1.1).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = MathTex(r"3^x = 9 \;\Rightarrow\; x = 2").scale(1.1).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        b7_rule = Tex(r"A negative $k$ gets rejected in writing").scale(1.05).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_rule))
        self.wait(2.5)

        # --- Band 8 (subtopic_4): simplify surds, add like surds
        self.next_band(8)
        b8_title = Tex(r"Simplify $3\sqrt{8} - \sqrt{18} + \sqrt{50}$").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"\sqrt{50} = \sqrt{25 \times 2} = 5\sqrt{2}").scale(1.1).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"3\sqrt{8} = 6\sqrt{2}, \quad \sqrt{18} = 3\sqrt{2}").scale(1.1).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"6\sqrt{2} - 3\sqrt{2} + 5\sqrt{2} = 8\sqrt{2}").scale(1.15).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        b8_rule = Tex("Like surds add like like terms").scale(1.05).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_rule))
        self.wait(2.5)

        # --- Band 9 (subtopic_4): expanding and rationalising
        self.next_band(9)
        b9_title = Tex("Expanding, and clearing the denominator").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(1.5)
        b9_l1 = MathTex(r"(2\sqrt{3} - 1)(\sqrt{3} + 4) = 6 + 8\sqrt{3} - \sqrt{3} - 4").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"= 2 + 7\sqrt{3}").scale(1.1).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"\frac{3}{\sqrt{7}} = \frac{3\sqrt{7}}{7}").scale(1.1).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = MathTex(r"\frac{6}{\sqrt{5} - \sqrt{2}} \times \frac{\sqrt{5} + \sqrt{2}}{\sqrt{5} + \sqrt{2}}").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        b9_l5 = MathTex(r"= \frac{6(\sqrt{5} + \sqrt{2})}{3} = 2\sqrt{5} + 2\sqrt{2}").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2.5)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 10 (subtopic_4): the surd equation and its compulsory check
        self.next_band(10)
        b10_title = Tex(r"Solve $\sqrt{x+7} = x - 5$").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(1.5)
        b10_l1 = MathTex(r"x + 7 = x^2 - 10x + 25").scale(1.1).shift(band_shift(10) + UP * 1.1)
        b10_l2 = MathTex(r"x^2 - 11x + 18 = 0").scale(1.1).shift(band_shift(10) + UP * 0.2)
        b10_l3 = MathTex(r"(x - 2)(x - 9) = 0 \;\Rightarrow\; x = 2 \text{ or } x = 9").scale(1.05).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex(r"$x = 2$: LHS $= \sqrt{9} = 3$, RHS $= -3$ — reject").scale(1.0).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = MathTex(r"x = 9").scale(1.2).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 11 (subtopic_5): half a doubling
        self.next_band(11)
        b11_title = Tex("Half a doubling").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex(r"Money doubles: 1 year $\times 2$, 3 years $\times 2^3$").scale(1.05).shift(band_shift(11) + UP * 1.1)
        b11_l2 = Tex(r"Half a year? $2^{1/2} = \sqrt{2}$ — half a doubling").scale(1.05).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11_l1))
        self.wait(2.5)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = MathTex(r"16^{\frac{3}{4}}: \; \sqrt[4]{16} = 2, \;\; 2^3 = 8").scale(1.1).shift(band_shift(11) + DOWN * 0.8)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2.5)
        b11_l4 = Tex(r"$27^{-2/3} = \tfrac{1}{9}$ — the minus flips, never negates").scale(1.0).shift(band_shift(11) + DOWN * 1.8)
        b11_l5 = MathTex(r"\sqrt{9 + 16} = 5, \;\text{ not } 3 + 4").scale(1.05).shift(band_shift(11) + DOWN * 2.8)
        self.play(Write(b11_l4))
        self.wait(2.5)
        self.play(Write(b11_l5))
        self.wait(3)

        # --- Band 12 (subtopic_6): everything in the same currency
        self.next_band(12)
        b12_title = Tex("Everything in the same currency").scale(1.2).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12_title))
        self.wait(2)
        b12_l1 = Tex("You cannot compare exponents on different bases").scale(1.0).shift(band_shift(12) + UP * 1.1)
        b12_l2 = MathTex(r"3^{2x-1} = 81 = 3^4 \;\Rightarrow\; x = \tfrac{5}{2}").scale(1.05).shift(band_shift(12) + UP * 0.2)
        self.play(Write(b12_l1))
        self.wait(2.5)
        self.play(Write(b12_l2))
        self.wait(2.5)
        b12_l3 = MathTex(r"2^{x+3} - 2^{x+1} = 2^x(8 - 2) = 6 \times 2^x").scale(1.0).shift(band_shift(12) + DOWN * 0.8)
        self.play(Write(b12_l3))
        self.wait(2.5)
        b12_l4 = Tex(r"Nickname the monster: $k = 3^x$").scale(1.05).shift(band_shift(12) + DOWN * 1.7)
        b12_l5 = MathTex(r"k = 1 \text{ or } 9 \;\Rightarrow\; x = 0 \text{ or } x = 2").scale(1.05).shift(band_shift(12) + DOWN * 2.7)
        self.play(Write(b12_l4))
        self.wait(2.5)
        self.play(Write(b12_l5))
        self.play(Create(SurroundingRectangle(b12_l5, color=GREEN)))
        self.wait(3)

        # --- Band 13 (subtopic_7): tidying the awkward bottom
        self.next_band(13)
        b13_title = Tex("Tidying the awkward bottom").scale(1.2).shift(band_shift(13) + UP * 2.2)
        self.play(Write(b13_title))
        self.wait(2)
        b13_l1 = Tex(r"Pack the crate: $\sqrt{50} = \sqrt{25 \times 2} = 5\sqrt{2}$").scale(1.05).shift(band_shift(13) + UP * 1.1)
        b13_l2 = Tex(r"Count like units: $6\sqrt{2} - 3\sqrt{2} + 5\sqrt{2} = 8\sqrt{2}$").scale(1.0).shift(band_shift(13) + UP * 0.2)
        self.play(Write(b13_l1))
        self.wait(2.5)
        self.play(Write(b13_l2))
        self.wait(2.5)
        b13_l3 = Tex(r"Two-term bottom? Use the opposite-sign partner").scale(1.0).shift(band_shift(13) + DOWN * 0.8)
        b13_l4 = MathTex(r"\frac{6}{\sqrt{5} - \sqrt{2}} = 2\sqrt{5} + 2\sqrt{2}").scale(1.05).shift(band_shift(13) + DOWN * 1.8)
        self.play(Write(b13_l3))
        self.wait(2.5)
        self.play(Write(b13_l4))
        self.play(Create(SurroundingRectangle(b13_l4, color=GREEN)))
        self.wait(2.5)
        b13_l5 = Tex(r"Squared an equation? Check: $x = 2$ was a gate-crasher").scale(1.0).shift(band_shift(13) + DOWN * 2.8)
        self.play(Write(b13_l5))
        self.wait(4)
