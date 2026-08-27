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

# Band-layout whiteboard scene (see AUTHORING-SPEC / quadratics-by-factorisation
# worked example). One band per teaching beat, camera moves down, nothing is
# ever removed. Covers all seven subtopics of the session duo:
# Part 1 — Expert (subtopics 1-4), Part 2 — Simplifier (subtopics 5-7),
# band time apportioned to subtopics.json (205/245/240/230/185/200/190 of 1495 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GeometricSequencesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the constant ratio test
        title = Tex("Geometric Sequences").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Each term = previous term $\\times$ fixed ratio $r$").scale(1.1).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = MathTex(r"2;\; 6;\; 18;\; 54").scale(1.2).shift(DOWN * 0.1)
        self.play(Write(d2))
        self.wait(1.5)
        d3 = MathTex(r"\tfrac{6}{2} = 3, \quad \tfrac{18}{6} = 3, \quad \tfrac{54}{18} = 3").scale(0.95).shift(DOWN * 1.1)
        self.play(Write(d3))
        self.wait(2)
        d4 = MathTex(r"\text{Constant ratio: geometric, } r = 3").scale(1.1).shift(DOWN * 2.2)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): what r may and may not be
        self.next_band(1)
        b1_title = Tex("Check the quotient along the whole list").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"1;\; 2;\; 4;\; 6: \quad \tfrac{6}{4} = 1{,}5 \neq 2").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.play(Create(strike(b1_l1)))
        self.wait(2)
        b1_l2 = MathTex(r"80;\; 40;\; 20;\; 10: \quad r = \tfrac{1}{2} \text{ — decay}").scale(1.05).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"3;\; -6;\; 12;\; -24: \quad r = -2 \text{ — alternates}").scale(1.05).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = MathTex(r"r \neq 0 \text{ and no term may be } 0").scale(1.1).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the general term
        self.next_band(2)
        b2_title = Tex("The general term").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"T_1 = a, \;\; T_2 = ar, \;\; T_3 = ar^2, \;\; T_4 = ar^3").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"T_n = a \, r^{\,n-1}").scale(1.25).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = MathTex(r"2;\, 6;\, 18;\, 54: \;\; T_n = 2 \times 3^{\,n-1}").scale(1.05).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"\text{Test: } T_4 = 2 \times 3^3 = 54 \;\checkmark").scale(1.05).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = MathTex(r"T_{10} = 2 \times 3^9 = 39\;366").scale(1.05).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): backwards — which term is 1458?
        self.next_band(3)
        b3_title = Tex("Which term equals 1458?").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"2 \times 3^{\,n-1} = 1458").scale(1.1).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"3^{\,n-1} = 729 = 3^6").scale(1.1).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Force both sides to the same base").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"n - 1 = 6 \;\Rightarrow\; n = 7").scale(1.15).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_2): recovering a and r from two terms
        self.next_band(4)
        b4_title = Tex(r"Given $T_2 = 6$ and $T_5 = 48$").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"ar = 6 \quad \text{and} \quad ar^4 = 48").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\text{Divide: } r^3 = \frac{48}{6} = 8").scale(1.05).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"r = 2, \quad a = 3").scale(1.1).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"T_n = 3 \times 2^{\,n-1}").scale(1.15).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = MathTex(r"\text{Check: } T_5 = 3 \times 16 = 48 \;\checkmark").scale(1.05).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): unknowns in the terms
        self.next_band(5)
        b5_title = Tex(r"Consecutive terms: $x;\; x+6;\; x+9$").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Middle squared $=$ product of neighbours").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"(x + 6)^2 = x(x + 9)").scale(1.1).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"x^2 + 12x + 36 = x^2 + 9x").scale(1.1).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = MathTex(r"3x = -36 \;\Rightarrow\; x = -12").scale(1.1).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = MathTex(r"\text{Check: } -12;\; -6;\; -3, \;\; r = \tfrac{1}{2}").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_3): geometric means, the even-root caution
        self.next_band(6)
        b6_title = Tex("Insert two geometric means between 4 and 108").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"4 \text{ is } T_1, \; 108 \text{ is } T_4: \quad 108 = 4r^3").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"r^3 = 27 \;\Rightarrow\; r = 3").scale(1.1).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"4;\; 12;\; 36;\; 108").scale(1.1).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex("Two means, THREE multiplications: means $+$ 1").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = MathTex(r"r^2 = 9: \; r = 3 \text{ or } -3 \text{ — state both}").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the bouncing ball
        self.next_band(7)
        b7_title = Tex(r"Ball from 8 m, each bounce $\tfrac{3}{4}$ of the last").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"8;\; 6;\; 4{,}5;\; \ldots \quad a = 8, \; r = 0{,}75").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("Drop height is term 1, so bounce four is $T_5$").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"T_5 = 8 \times 0{,}75^4").scale(1.1).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = MathTex(r"T_5 = 2{,}53125 \approx 2{,}53 \text{ m}").scale(1.1).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("Write down which position the start owns").scale(1.0).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_4): growth and percentage ratios
        self.next_band(8)
        b8_title = Tex("Bacteria: 500 double every hour").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"\text{After } n \text{ hours: } 500 \times 2^n").scale(1.1).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"\text{After 10 h: } 500 \times 1024 = 512\;000").scale(1.05).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Percentages become ratios:").scale(1.05).shift(band_shift(8) + DOWN * 1.0)
        b8_l4 = MathTex(r"+6\%: \; r = 1{,}06 \qquad -15\%: \; r = 0{,}85").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l3))
        self.wait(1.5)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("The ratio is one plus or one minus the rate").scale(1.0).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the photocopier
        self.next_band(9)
        b9_title = Tex("The photocopier set to 75\\%").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Copy the copy: each page $\\tfrac{3}{4}$ of the last").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"2;\; 6;\; 18;\; 54: \text{ every division gives } 3").scale(1.05).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"1;\; 2;\; 4;\; 6: \text{ setting changed — not geometric}").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.play(Create(strike(b9_l3)))
        self.wait(2.5)
        b9_l4 = MathTex(r"r = -2 \text{ flips the page: } 3;\; -6;\; 12;\; -24").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        b9_l5 = Tex("The only forbidden setting is zero").scale(1.05).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_6): the chain of forwards
        self.next_band(10)
        b10_title = Tex("One message, a chain of forwards").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"\text{Rounds: } 2;\; 6;\; 18;\; \ldots \quad (\times 3 \text{ each})").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{Round } 10: \; 2 \times 3^9 = 39\;366").scale(1.1).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex("Nine forwards, not ten — round one is the start").scale(1.0).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = MathTex(r"1458: \;\; 3^{\,n-1} = 729 = 3^6, \; n = 7").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = MathTex(r"\text{Two rounds known: divide — } r^3 = 8, \; a = 3").scale(1.0).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_7): the fair middle, multiplied
        self.next_band(11)
        b11_title = Tex("The fair middle, multiplied").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = MathTex(r"4 \to 108 \text{ in 3 steps: } r^3 = 27, \; r = 3").scale(1.05).shift(band_shift(11) + UP * 1.1)
        b11_l2 = MathTex(r"4;\; 12;\; 36;\; 108").scale(1.1).shift(band_shift(11) + UP * 0.1)
        self.play(Write(b11_l1))
        self.wait(2.5)
        self.play(Write(b11_l2))
        self.wait(2)
        b11_l3 = MathTex(r"\text{Shortcut: } 12^2 = 144 = 4 \times 36").scale(1.05).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = MathTex(r"x;\, x+6;\, x+9: \; (x+6)^2 = x(x+9) \Rightarrow x = -12").scale(0.95).shift(band_shift(11) + DOWN * 1.9)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        self.wait(2.5)
        b11_l5 = MathTex(r"r^2 = 9: \text{ two possible machines, } \pm 3").scale(1.0).shift(band_shift(11) + DOWN * 2.9)
        self.play(Write(b11_l5))
        self.wait(4)
