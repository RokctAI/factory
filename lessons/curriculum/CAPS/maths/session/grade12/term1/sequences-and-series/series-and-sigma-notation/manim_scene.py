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
# band time apportioned to subtopics.json (215/245/230/245/185/200/195 of 1515 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SeriesAndSigmaNotationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(16)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): reading the instruction
        title = Tex("Series and Sigma Notation").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("A series adds the terms of a sequence").scale(1.1).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = MathTex(r"\sum_{k=1}^{5} (2k + 1)").scale(1.2).shift(DOWN * 0.2)
        self.play(Write(d2))
        self.wait(2.5)
        d3 = MathTex(r"= 3 + 5 + 7 + 9 + 11 = 35").scale(1.1).shift(DOWN * 1.4)
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(2)
        d4 = Tex("Bottom: start. Top: stop. Right: the recipe.").scale(1.0).shift(DOWN * 2.5)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): counting terms, writing the instruction
        self.next_band(1)
        b1_title = Tex("Counting terms and writing sigma").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Number of terms} = \text{top} - \text{bottom} + 1").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"k = 3 \text{ to } 20: \; 20 - 3 + 1 = 18 \text{ terms}").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("The counter is private — it never survives").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"4 + 7 + 10 + \ldots + 61: \; a = 4, \; d = 3").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = MathTex(r"3k+1 = 61: \; k = 20, \;\; \sum_{k=1}^{20}(3k+1)").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): folding proof of the arithmetic sum
        self.next_band(2)
        b2_title = Tex("The arithmetic sum: fold the list").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"S_n = a + (a + d) + \ldots + l").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"S_n = l + (l - d) + \ldots + a").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\text{Add columns: } 2S_n = n(a + l)").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"S_n = \tfrac{n}{2}(a + l)").scale(1.2).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = MathTex(r"\text{No } l? \;\; S_n = \tfrac{n}{2}(2a + (n-1)d)").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): forwards — forty terms
        self.next_band(3)
        b3_title = Tex(r"$5 + 8 + 11 + \ldots$ for forty terms").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"S_{40} = \tfrac{40}{2}\left(2(5) + 39 \times 3\right)").scale(1.1).shift(band_shift(3) + UP * 1.0)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"= 20(10 + 117) = 20 \times 127").scale(1.1).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"S_{40} = 2540").scale(1.15).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_2): backwards — how many terms make 155?
        self.next_band(4)
        b4_title = Tex(r"How many terms of $2 + 5 + 8 + \ldots$ make 155?").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\tfrac{n}{2}\left(4 + 3(n - 1)\right) = 155").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"n(3n + 1) = 310").scale(1.1).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"3n^2 + n - 310 = 0").scale(1.1).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"n = \frac{-1 \pm \sqrt{3721}}{6} = \frac{-1 \pm 61}{6}").scale(1.05).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = MathTex(r"n = 10 \;\; (\text{reject the negative root})").scale(1.05).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the collapsing proof
        self.next_band(5)
        b5_title = Tex("The geometric sum: multiply and subtract").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"S_n = a + ar + ar^2 + \ldots + ar^{\,n-1}").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"rS_n = \quad\;\; ar + ar^2 + \ldots + ar^{\,n}").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"S_n - rS_n = a - ar^{\,n}").scale(1.05).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"S_n = \frac{a(1 - r^{\,n})}{1 - r}, \quad r \neq 1").scale(1.1).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex("If $r = 1$: every term is $a$, sum is $na$").scale(1.0).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_3): geometric sum worked both ways
        self.next_band(6)
        b6_title = Tex(r"$3 + 6 + 12 + \ldots$ for ten terms").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"S_{10} = \frac{3(2^{10} - 1)}{2 - 1} = 3 \times 1023").scale(1.05).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"S_{10} = 3069").scale(1.15).shift(band_shift(6) + DOWN * 0.1)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        b6_l3 = MathTex(r"\text{How many terms of } 1 + 2 + 4 \text{ make } 255?").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"2^n - 1 = 255: \; 2^n = 256 = 2^8, \; n = 8").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): sum to infinity
        self.next_band(7)
        b7_title = Tex("When forever adds up").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"8 + 4 + 2 + 1 + \tfrac{1}{2} + \ldots").scale(1.1).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"\text{Totals: } 8;\; 12;\; 14;\; 15;\; 15{,}5 \to 16").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"-1 < r < 1: \; r^{\,n} \to 0").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = MathTex(r"S_\infty = \frac{a}{1 - r}").scale(1.2).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = MathTex(r"S_\infty = \frac{8}{1 - \tfrac{1}{2}} = 16").scale(1.05).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_4): the convergence condition with x
        self.next_band(8)
        b8_title = Tex(r"For which $x$ does ratio $2x - 1$ converge?").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"-1 < 2x - 1 < 1").scale(1.15).shift(band_shift(8) + UP * 1.0)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"0 < 2x < 2").scale(1.15).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = MathTex(r"0 < x < 1, \quad x \neq \tfrac{1}{2}").scale(1.15).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex(r"($r = 0$ excluded at $x = \tfrac{1}{2}$)").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_4): recurring decimals
        self.next_band(9)
        b9_title = Tex(r"The recurring decimal $0{,}555\ldots$").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(1.5)
        b9_l1 = MathTex(r"0{,}555\ldots = \tfrac{5}{10} + \tfrac{5}{100} + \ldots").scale(1.0).shift(band_shift(9) + UP * 1.0)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"a = \tfrac{5}{10}, \quad r = \tfrac{1}{10}").scale(1.1).shift(band_shift(9) + UP * 0.0)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"S_\infty = \frac{\tfrac{5}{10}}{\tfrac{9}{10}} = \frac{5}{9}").scale(1.1).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("Every repeating decimal is a fraction in disguise").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 10 (subtopic_5): the instruction on the crate
        self.next_band(10)
        b10_title = Tex("The instruction on the crate").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Sigma says: pack the crate, then add it up").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\sum_{k=1}^{5}(2k+1): \text{ in go } 3, 5, 7, 9, 11 = 35").scale(1.0).shift(band_shift(10) + UP * 0.0)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"\text{Items from 3 to 20: } 20 - 3 + 1 = 18").scale(1.05).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex("$k$ is the packer's clipboard — wiped at the end").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l4))
        self.wait(3)

        # --- Band 11 (subtopic_6): Gauss folds the queue
        self.next_band(11)
        b11_title = Tex("Gauss folds the queue").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = MathTex(r"1 + 100 = 101, \quad 2 + 99 = 101, \; \ldots").scale(1.05).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"50 \text{ pairs} \times 101 = 5050").scale(1.1).shift(band_shift(11) + UP * 0.1)
        self.play(Write(b11_l2))
        self.play(Create(SurroundingRectangle(b11_l2, color=GREEN)))
        self.wait(2.5)
        b11_l3 = MathTex(r"\text{Brick stack: } S_{40} = 20(10 + 117) = 2540").scale(1.0).shift(band_shift(11) + DOWN * 1.0)
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = MathTex(r"\text{Envelopes to R155: } 3n^2 + n - 310 = 0").scale(1.0).shift(band_shift(11) + DOWN * 2.0)
        b11_l5 = Tex("$n = 10$ — envelopes cannot be negative").scale(1.0).shift(band_shift(11) + DOWN * 2.9)
        self.play(Write(b11_l4))
        self.wait(2)
        self.play(Write(b11_l5))
        self.wait(3)

        # --- Band 12 (subtopic_7): half the oranges, forever
        self.next_band(12)
        b12_title = Tex("Half the oranges, forever").scale(1.2).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12_title))
        self.wait(2)
        b12_l1 = Tex("A bag of 16: take 8, then 4, then 2, then 1 \\ldots").scale(1.05).shift(band_shift(12) + UP * 1.1)
        self.play(Write(b12_l1))
        self.wait(2.5)
        b12_l2 = Tex("The total can never pass 16 — one bag only").scale(1.05).shift(band_shift(12) + UP * 0.2)
        self.play(Write(b12_l2))
        self.wait(2.5)
        b12_l3 = MathTex(r"S_\infty = \frac{8}{1 - \tfrac{1}{2}} = 16").scale(1.1).shift(band_shift(12) + DOWN * 0.9)
        self.play(Write(b12_l3))
        self.play(Create(SurroundingRectangle(b12_l3, color=GREEN)))
        self.wait(2.5)
        b12_l4 = Tex("Only for a genuine fraction: $-1 < r < 1$").scale(1.05).shift(band_shift(12) + DOWN * 1.9)
        self.play(Write(b12_l4))
        self.wait(2)
        b12_l5 = MathTex(r"0{,}555\ldots = \frac{5}{9}").scale(1.05).shift(band_shift(12) + DOWN * 2.9)
        self.play(Write(b12_l5))
        self.wait(4)
