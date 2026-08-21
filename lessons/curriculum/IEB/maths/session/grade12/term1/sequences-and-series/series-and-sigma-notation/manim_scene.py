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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): reading sigma notation
        title = Tex("Series and Sigma Notation").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"\sum_{k=1}^{6} (3k + 2)").scale(1.2).shift(UP * 0.8)
        self.play(Write(d1))
        self.wait(2)
        d2 = MathTex(r"5 + 8 + 11 + 14 + 17 + 20 = 75").scale(1.05).shift(DOWN * 0.3)
        self.play(Write(d2))
        self.play(Create(SurroundingRectangle(d2, color=GREEN)))
        self.wait(2)
        d3 = MathTex(r"\text{Terms: top} - \text{bottom} + 1").scale(1.05).shift(DOWN * 1.3)
        self.play(Write(d3))
        self.wait(2)
        d4 = MathTex(r"k = 4 \text{ to } 25: \; 25 - 4 + 1 = 22 \text{ terms}").scale(1.0).shift(DOWN * 2.3)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): writing a series in sigma form
        self.next_band(1)
        b1_title = Tex("Writing the instruction").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"7 + 11 + 15 + \cdots + 83").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"a = 7, \; d = 4 \;\Rightarrow\; \text{recipe } 4k + 3").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"4k + 3 = 83 \;\Rightarrow\; k = 20").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"\sum_{k=1}^{20} (4k + 3)").scale(1.15).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the folding proof
        self.next_band(2)
        b2_title = Tex("Fold the list in half").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"S_n = a + (a + d) + \cdots + l").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"S_n = l + (l - d) + \cdots + a").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\text{Add columns: } 2S_n = n(a + l)").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"S_n = \tfrac{n}{2}(a + l) = \tfrac{n}{2}\left(2a + (n-1)d\right)").scale(1.05).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): arithmetic sums forwards and backwards
        self.next_band(3)
        b3_title = Tex("Forwards and backwards").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"6 + 10 + 14 + \cdots, \; 30 \text{ terms}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"S_{30} = 15(12 + 116) = 15 \times 128 = 1920").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = MathTex(r"3 + 7 + 11 + \cdots = 210: \;\; 2n^2 + n - 210 = 0").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"\sqrt{1681} = 41 \;\Rightarrow\; n = 10 \;\text{(reject negative)}").scale(0.95).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = MathTex(r"\text{Check: } S_{10} = 5(6 + 36) = 210 \;\checkmark").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the collapsing proof and geometric sums
        self.next_band(4)
        b4_title = Tex("The collapsing proof").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"S_n - rS_n = a - ar^n").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"S_n = \frac{a(1 - r^n)}{1 - r}, \quad r \neq 1").scale(1.1).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"2 + 6 + 18 + \cdots, \; 9 \text{ terms: } S_9 = \tfrac{2(3^9 - 1)}{2} = 19\;682").scale(0.9).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"3 + 6 + 12 + \cdots = 381: \; 2^n = 128 \Rightarrow n = 7").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_4): sum to infinity
        self.next_band(5)
        b5_title = Tex("When forever adds up").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"27 + 9 + 3 + 1 + \cdots \quad (r = \tfrac{1}{3})").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\text{Totals: } 27, \; 36, \; 39, \; 40, \; 40\tfrac{1}{3}, \ldots").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"S_\infty = \frac{a}{1 - r} = \frac{27}{2/3} = 40{,}5").scale(1.1).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = MathTex(r"\text{Exists only for } -1 < r < 1, \; r \neq 0").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = MathTex(r"\text{Ratio } 3x - 2: \;\; \tfrac{1}{3} < x < 1, \; x \neq \tfrac{2}{3}").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): the instruction on the crate
        self.next_band(6)
        b6_title = Tex("The instruction on the crate").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Bottom: start. Top: stop. Right: the recipe.").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\sum_{k=1}^{6}(3k+2): \; 5, 8, 11, 14, 17, 20 \;\to\; 75").scale(0.95).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex("Boxes 4 to 25: touch 22 boxes, not 21").scale(1.0).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("The tally letter $k$ never reaches the answer").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_6): Gauss folds the queue
        self.next_band(7)
        b7_title = Tex("Gauss folds the queue").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"1 + 100 = 101, \quad 2 + 99 = 101, \ldots").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"50 \text{ pairs} \times 101 = 5050").scale(1.1).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = MathTex(r"\text{Bricks } 6, 10, 14, \ldots \; 30 \text{ rows: } 1920").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"\text{Envelopes to R210: } n = 10 \;\text{(reject } n < 0)").scale(0.95).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_7): half the oranges, forever
        self.next_band(8)
        b8_title = Tex("Half the oranges, forever").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"24 \text{ oranges: } 12 + 6 + 3 + 1{,}5 + \cdots").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Never past 24 — there was only one bag").scale(1.0).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"S_\infty = \frac{12}{1 - \tfrac{1}{2}} = 24").scale(1.1).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = MathTex(r"0{,}777\ldots = \tfrac{7/10}{9/10} = \tfrac{7}{9}").scale(1.05).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Every repeating decimal is a converged series").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l5))
        self.wait(4)
