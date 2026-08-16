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

# Band-layout whiteboard scene (see the quadratics-by-factorisation worked
# example). One band per teaching beat; the camera moves down to clean space
# and nothing is ever removed. The box-and-whisker diagram is built from
# Line/Rectangle/Dot/Tex only (exporter-safe primitives). Covers all seven
# subtopics of the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# dwell times roughly proportional to subtopics.json
# (150/180/170/180/160/170/160 of 1170 s).

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


class DispersionBoxPlotsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): range, and why spread matters
        title = Tex("Measures of Dispersion").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"A: 45, 48, 50, 52, 55 \qquad B: 20, 35, 50, 65, 80").scale(1.0).shift(UP * 1.2)
        b0_l2 = Tex(r"Both means are exactly 50 — completely different stories").scale(0.95).shift(UP * 0.3)
        self.play(Write(b0_l1))
        self.wait(2.5)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = MathTex(r"\text{Range} = \text{max} - \text{min}: \; A: 10, \; B: 60").scale(0.9).shift(DOWN * 0.7)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = Tex(r"Weakness: one 98 in $A$ explodes the range from 10 to 53").scale(0.95).shift(DOWN * 1.7)
        b0_l5 = Tex(r"Quick, fragile, owned by the extremes").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(b0_l4))
        self.wait(2.5)
        self.play(Write(b0_l5))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): quartiles of the tuck-shop data
        self.next_band(1)
        b1_title = Tex("Eleven days of sandwich sales, ordered").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"4, 7, 8, 10, 12, 13, 15, 17, 18, 20, 25").scale(1.05).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex(r"Median $=$ 6th value $= 13$ (five each side)").scale(1.05).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex(r"$Q_1$: middle of $4, 7, 8, 10, 12 \;\to\; 8$").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = Tex(r"$Q_3$: middle of $15, 17, 18, 20, 25 \;\to\; 18$").scale(1.05).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex(r"Odd count: the median is the fence, not a resident").scale(0.95).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l5))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the interquartile range
        self.next_band(2)
        b2_title = Tex("The interquartile range").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"IQR = Q_3 - Q_1 = 18 - 8 = 10").scale(1.15).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = Tex(r"The middle 50\% of days sold between 8 and 18").scale(1.0).shift(band_shift(2) + UP * 0.1)
        b2_l3 = Tex(r"The 4 and the 25 cannot touch it — outlier-resistant").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l2))
        self.wait(2.5)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = MathTex(r"\text{Semi-IQR} = \tfrac{10}{2} = 5").scale(1.05).shift(band_shift(2) + DOWN * 1.7)
        b2_l5 = Tex(r"Range $25 - 4 = 21$ vs IQR 10: extremes stretch twice as wide").scale(0.9).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): five-number summary and the diagram
        self.next_band(3)
        b3_title = Tex(r"Five-number summary: $4, \; 8, \; 13, \; 18, \; 25$").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        u = 0.4
        org3 = band_shift(3) + LEFT * 6.0 + DOWN * 1.6

        def pos3(v):
            return org3 + RIGHT * v * u

        nline = Line(org3, pos3(30))
        ticks = VGroup(*[MathTex(str(v)).scale(0.6).next_to(pos3(v), DOWN, buff=0.15) for v in [0, 5, 10, 15, 20, 25, 30]])
        self.play(Create(nline), Write(ticks))
        self.wait(2)
        box = Rectangle(width=10 * u, height=1.2).move_to(pos3(13) + UP * 0.9)
        self.play(Create(box))
        self.wait(1.5)
        med = Line(pos3(13) + UP * 0.3, pos3(13) + UP * 1.5, color=YELLOW)
        self.play(Create(med))
        self.wait(1.5)
        wl = Line(pos3(4) + UP * 0.9, pos3(8) + UP * 0.9)
        wr = Line(pos3(18) + UP * 0.9, pos3(25) + UP * 0.9)
        dmin = Dot(pos3(4) + UP * 0.9, radius=0.06)
        dmax = Dot(pos3(25) + UP * 0.9, radius=0.06)
        self.play(Create(wl), Create(dmin))
        self.play(Create(wr), Create(dmax))
        self.wait(2)
        b3_l1 = Tex(r"Box from $Q_1$ to $Q_3$ — its length IS the IQR").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex(r"Median line inside; whiskers to min and max").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): every section holds a quarter
        self.next_band(4)
        b4_title = Tex("Each section holds ONE QUARTER of the data").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.play(Create(SurroundingRectangle(b4_title, color=GREEN)))
        self.wait(2.5)
        b4_l1 = Tex(r"A long section holds the SAME quarter, spread wider").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"Long: spread-out quarter; short: bunched quarter").scale(0.95).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Left whisker 4 to 8: quiet days, tightly packed").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        b4_l4 = Tex(r"Right whisker 18 to 25: busy days, more spread out").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_4): percentiles
        self.next_band(5)
        b5_title = Tex("Percentiles — quartiles' fine-grained cousins").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"$p$-th percentile: the value below which $p\%$ of data lies").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"Q_1: 25\%, \quad \text{median}: 50\%, \quad Q_3: 75\%").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex(r"``The 75th percentile was 18'' $=$ ``$Q_3$ was 18''").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        b5_l4 = Tex(r"90th percentile: beaten by only 10\% of candidates").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l3))
        self.wait(2.5)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): skew, and comparing two plots
        self.next_band(6)
        b6_title = Tex("Skew, and comparing two box plots").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Median near $Q_1$ $+$ long right whisker: skewed RIGHT").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"Most values bunch low, with a tail of large values").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"A: median 60, IQR 12 \;\; vs \;\; B: median 55, IQR 30").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex(r"A scored higher AND was more consistent").scale(1.05).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l3))
        self.wait(2.5)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex(r"Two sentences always: centres, then spreads").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): same average, different story
        self.next_band(7)
        b7_title = Tex("Two taxi routes, same poster: average 30 min").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"\text{Route 1: } 28, 29, 30, 31, 32 \;\;\to\;\; \text{range } 4").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = MathTex(r"\text{Route 2: } 15, 20, 30, 40, 45 \;\;\to\;\; \text{range } 30").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"An average hides the wandering; spread measures it").scale(0.85).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex(r"Blind spot: one breakdown balloons the range").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): folding the line
        self.next_band(8)
        b8_title = Tex("Fold the line in half, then in half again").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Eleven learners in order — the 6th holds 13: the median").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"Left five: their middle holds 8. Right five: 18").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{Three fences: } 8, \; 13, \; 18").scale(1.1).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex(r"Ordinary days live between the fences: 8 to 18, ten wide").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        b8_l5 = Tex(r"The IQR is the range that ignores drama; half of it is 5").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l4))
        self.wait(2.5)
        self.play(Write(b8_l5))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): drawing the box in words
        self.next_band(9)
        b9_title = Tex(r"Five landmarks: $4, 8, 13, 18, 25$").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Walls at 8 and 18, median line at 13, whiskers to 4 and 25").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"Ordinary days live in the box; whiskers reach the extremes").scale(0.95).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex(r"LONG never means many — long means spread").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex(r"Two boxes: compare median lines, then box lengths").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        b9_l5 = Tex(r"Long right side: skewed right — a tail of big values").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l4))
        self.wait(2.5)
        self.play(Write(b9_l5))
        self.wait(4)
