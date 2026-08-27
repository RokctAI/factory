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

# Band-layout whiteboard scene. One band per teaching beat; the camera moves
# down to clean space and nothing is ever removed. Covers all seven subtopics
# of the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7), dwell times
# roughly proportional to subtopics.json (150/180/170/180/160/170/160 of
# 1170 s).

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
        title = Tex("Range, and Why Spread Matters").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"A: 56, 58, 60, 62, 64 \quad B: 30, 45, 60, 75, 90").scale(0.95).shift(UP * 1.2)
        b0_l2 = Tex(r"Both means exactly 60 — completely different stories").scale(0.9).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.wait(2.5)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = MathTex(r"\text{Range A} = 64 - 56 = 8 \qquad \text{Range B} = 90 - 30 = 60").scale(0.9).shift(DOWN * 0.6)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = Tex(r"Weakness: one 95 joins A and the range leaps 8 $\to$ 39").scale(0.85).shift(DOWN * 1.7)
        self.play(Write(b0_l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): quartiles of the juice data
        self.next_band(1)
        b1_title = Tex("Quartiles of the juice-kiosk data").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"3, 5, 8, 10, 12, \underline{13}, 18, 21, 24, 26, 33").scale(0.95).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex(r"Median: sixth of eleven $= 13$ — the fence between halves").scale(0.85).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"Q_1 = \text{middle of } 3, 5, \underline{8}, 10, 12 = 8").scale(0.95).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = MathTex(r"Q_3 = \text{middle of } 18, 21, \underline{24}, 26, 33 = 24").scale(0.95).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the interquartile range
        self.next_band(2)
        b2_title = Tex("The interquartile range").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"IQR = Q_3 - Q_1 = 24 - 8 = 16").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = Tex(r"The middle 50\% of days sold between 8 and 24 cups").scale(0.9).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex(r"Outlier-resistant: the days at 3 and 33 sit outside the fences").scale(0.85).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = MathTex(r"\text{Semi-IQR} = \tfrac{16}{2} = 8 \qquad \text{Range} = 33 - 3 = 30").scale(0.95).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): five-number summary and the diagram
        self.next_band(3)
        b3_title = Tex("Five-number summary: 3, 8, 13, 24, 33").scale(1.1).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(2)

        def pos3(v):
            return band_shift(3) + DOWN * 0.6 + RIGHT * ((v - 17.0) * 0.28)

        nline = Line(pos3(0), pos3(35))
        self.play(Create(nline))
        ticks = VGroup()
        for v in [0, 5, 10, 15, 20, 25, 30, 35]:
            ticks.add(Line(pos3(v) + DOWN * 0.12, pos3(v) + UP * 0.12))
            ticks.add(MathTex(str(v)).scale(0.5).move_to(pos3(v) + DOWN * 0.45))
        self.play(Create(ticks))
        self.wait(1.5)
        box = Rectangle(width=(24 - 8) * 0.28, height=1.0).move_to(pos3(16) + UP * 1.1)
        med = Line(pos3(13) + UP * 0.6, pos3(13) + UP * 1.6)
        wl = Line(pos3(3) + UP * 1.1, pos3(8) + UP * 1.1)
        wr = Line(pos3(24) + UP * 1.1, pos3(33) + UP * 1.1)
        self.play(Create(box))
        self.wait(1.5)
        self.play(Create(med))
        self.wait(1.5)
        self.play(Create(wl), Create(wr))
        self.wait(2)
        b3_l1 = Tex(r"Box $= Q_1$ to $Q_3$ (length $=$ IQR); whiskers to the extremes").scale(0.8).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l1))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): every section holds a quarter
        self.next_band(4)
        b4_title = Tex("Every section holds a QUARTER of the data").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex(r"Left whisker 3–8: a quarter, packed into five units").scale(0.9).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"Right whisker 24–33: the SAME quarter, spread over nine").scale(0.9).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Long section $=$ spread-out quarter, never more days").scale(0.95).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex(r"That one sentence reads every box plot ever drawn").scale(0.9).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): percentiles
        self.next_band(5)
        b5_title = Tex("Percentiles: quartiles' fine-grained cousins").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"$p$-th percentile: the value below which $p\%$ of the data lies").scale(0.85).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"Q_1 = P_{25} \qquad \text{median} = P_{50} \qquad Q_3 = P_{75}").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex(r"90th percentile for the squad: only 10\% beat that mark").scale(0.9).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex(r"Percentiles rank you against the group, not the paper").scale(0.9).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): skew, and comparing two plots
        self.next_band(6)
        b6_title = Tex("Skew, and comparing two box plots").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Median 5 units from $Q_1$, 11 from $Q_3$; long right whisker").scale(0.85).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"$\Rightarrow$ skewed to the RIGHT: bunched low, tail of big days").scale(0.9).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"Compare in two sentences:").scale(0.95).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex(r"Centres: A median 62 vs B median 58 — A typically higher").scale(0.85).shift(band_shift(6) + DOWN * 1.4)
        b6_l5 = Tex(r"Spreads: A IQR 10 vs B IQR 26 — A more consistent").scale(0.85).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l3))
        self.wait(1.5)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): same average, different story
        self.next_band(7)
        b7_title = Tex("Same average, different story").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"Both flyers: ``average delivery 40 minutes''").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex(r"Place one: 38, 39, 40, 41, 42 — range 4").scale(0.95).shift(band_shift(7) + UP * 0.2)
        b7_l3 = Tex(r"Place two: 25, 30, 40, 50, 55 — range 30").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex(r"The average shows the centre; spread is the wandering").scale(0.9).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): folding the strip
        self.next_band(8)
        b8_title = Tex("Fold the strip: middle, then middles of halves").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"3, 5, 8, 10, 12, 13, 18, 21, 24, 26, 33").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex(r"Fold one: crease at 13 — the median").scale(0.95).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex(r"Fold two and three: creases at 8 and 24 — the quartiles").scale(0.9).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex(r"Ordinary days live between the creases: 16 cups wide").scale(0.9).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex(r"The IQR is the range that ignores drama").scale(0.95).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): drawing the box in words
        self.next_band(9)
        b9_title = Tex("Drawing the box in words").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)

        def pos9(v):
            return band_shift(9) + UP * 0.6 + RIGHT * ((v - 17.0) * 0.28)

        nline9 = Line(pos9(0), pos9(35))
        box9 = Rectangle(width=(24 - 8) * 0.28, height=0.9).move_to(pos9(16) + UP * 1.0)
        med9 = Line(pos9(13) + UP * 0.55, pos9(13) + UP * 1.45)
        wl9 = Line(pos9(3) + UP * 1.0, pos9(8) + UP * 1.0)
        wr9 = Line(pos9(24) + UP * 1.0, pos9(33) + UP * 1.0)
        self.play(Create(nline9))
        self.play(Create(box9), Create(med9))
        self.play(Create(wl9), Create(wr9))
        self.wait(2)
        b9_l1 = Tex(r"Walls at 8 and 24, median line at 13, whiskers to 3 and 33").scale(0.8).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"Long means spread, never many").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2)
        b9_l3 = Tex(r"Two boxes, two sentences: medians, then box lengths").scale(0.9).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l3))
        self.wait(4)
