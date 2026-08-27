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

# Band-layout whiteboard scene (see the quadratics-by-factorisation worked
# example). One band per teaching beat; the camera moves down to clean space
# and nothing is ever removed. The histogram is drawn from touching
# Rectangles on Arrow axes (exporter-safe primitives only). Covers all seven
# subtopics of the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# dwell times roughly proportional to subtopics.json
# (160/170/180/180/160/160/160 of 1170 s).

BAND = config.frame_height

FREQS = [3, 8, 11, 5, 3]


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


def histogram(org, bw, hu, color=BLUE):
    """Five touching bars for the travel-time data, drawn from Rectangles."""
    bars = VGroup()
    for j, f in enumerate(FREQS):
        bar = Rectangle(width=bw, height=f * hu, color=color)
        bar.move_to(org + RIGHT * (j + 0.5) * bw + UP * f * hu / 2)
        bars.add(bar)
    return bars


class HistogramsInterpretingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): raw data to frequency table
        title = Tex("From Raw Data to a Frequency Table").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"30 travel times, in minutes — a jumble organises nothing").scale(0.95).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex(r"Equal class intervals: $0$–$10$, $10$–$20$, $20$–$30$, $30$–$40$, $40$–$50$").scale(0.95).shift(UP * 0.3)
        b0_l3 = Tex(r"Keep the bottom, refuse the top: 20 $\to$ the 20–30 class").scale(0.9).shift(DOWN * 0.6)
        self.play(Write(b0_l2))
        self.wait(2.5)
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = MathTex(r"\text{Frequencies: } 3, \; 8, \; 11, \; 5, \; 3").scale(1.1).shift(DOWN * 1.6)
        b0_l5 = MathTex(r"3 + 8 + 11 + 5 + 3 = 30 \;\checkmark").scale(1.1).shift(DOWN * 2.5)
        self.play(Write(b0_l4))
        self.wait(2.5)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): building the histogram
        self.next_band(1)
        b1_title = Tex("Building the histogram").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        org1 = band_shift(1) + LEFT * 5.4 + DOWN * 2.4
        ax1 = VGroup(Arrow(org1 + LEFT * 0.3, org1 + RIGHT * 7.6, buff=0),
                     Arrow(org1 + DOWN * 0.3, org1 + UP * 4.2, buff=0))
        xt = VGroup(*[MathTex(str(10 * j)).scale(0.6).next_to(org1 + RIGHT * j * 1.4, DOWN, buff=0.15) for j in range(6)])
        xlab = Tex("time (min)").scale(0.7).next_to(org1 + RIGHT * 7.4, UP, buff=0.2)
        ylab = Tex("frequency").scale(0.7).next_to(org1 + UP * 4.2, RIGHT, buff=0.2)
        self.play(Create(ax1), Write(xt), Write(xlab), Write(ylab))
        self.wait(2)
        bars = histogram(org1, 1.4, 0.32)
        heights = VGroup(*[MathTex(str(f)).scale(0.7).next_to(bars[j], UP, buff=0.1) for j, f in enumerate(FREQS)])
        for j in range(5):
            self.play(Create(bars[j]), Write(heights[j]), run_time=0.9)
            self.wait(1.2)
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the bars touch — and why
        self.next_band(2)
        b2_title = Tex("The defining feature: the bars TOUCH").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex(r"Continuous data: 19,9 flows into 20,0 — nothing between").scale(0.9).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex(r"A connected skyline, not separated towers").scale(1.05).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex(r"Bar graph: CATEGORIES, bars stand apart").scale(1.05).shift(band_shift(2) + DOWN * 0.6)
        b2_l4 = Tex(r"Gaps mean categories; touching means measurement").scale(1.05).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex(r"Label everything: axis titles with units, a heading").scale(0.95).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): peak, middle, mean
        self.next_band(3)
        b3_title = Tex("Reading the shape: three passes").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"1. Peak: modal class $20$–$30$ (11 of the 30)").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex(r"2. Middle: cumulative $3, 11, 22$ — 15th and 16th in bar 3").scale(0.95).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex(r"Median class: $20$ to below $30$").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"15 + 120 + 275 + 175 + 135 = 720").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        b3_l5 = MathTex(r"\text{Estimated mean} = \frac{720}{30} = 24 \text{ min}").scale(1.05).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l4))
        self.wait(2.5)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the tail names the skew
        self.next_band(4)
        b4_title = Tex("3. Shape: ask where the tail is").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Rises fast, peaks at $20$–$30$, trails right through 5 and 3").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"Longer RIGHT tail: skewed to the right (positive)").scale(1.05).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Longer left tail: skewed left; mirror sides: symmetrical").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex(r"Skew is named after the TAIL, not the peak").scale(1.05).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex(r"A right-skewed histogram has its peak on the LEFT").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): the comment template
        self.next_band(5)
        b5_title = Tex("The analysis comment: CENTRE, SPREAD, SHAPE").scale(0.95).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"Centre: modal class $20$–$30$, mean 24 min —").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"a typical learner travels twenty-odd minutes").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Spread: below 10 to nearly 50 — travel differs greatly").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex(r"Shape: skewed right — most short, a few travel far").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex(r"Each sentence quotes a number, then returns to context").scale(0.95).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): comparisons and hygiene
        self.next_band(6)
        b6_title = Tex("Comparing two displays").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Second class: peak on $10$–$20$, nobody past 30").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"Lower centre, narrower spread — more uniform access").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"Compare like with like: centre vs centre, spread vs spread").scale(0.95).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex(r"Stay in context; claim only what the display shows").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        b6_l5 = Tex(r"Grouped data trades detail for overview — say so").scale(1.0).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l4))
        self.wait(2.5)
        self.play(Write(b6_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): sorting the pile into buckets
        self.next_band(7)
        b7_title = Tex("Thirty slips of paper, five buckets").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"A pile answers nothing — sort it like laundry").scale(1.05).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"Slip 7 $\to$ bucket 1; \; 23 $\to$ bucket 3; \; 41 $\to$ bucket 5").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Boundary rule: a bucket keeps its bottom, refuses its top").scale(0.95).shift(band_shift(7) + DOWN * 0.6)
        b7_l4 = Tex(r"Exactly 20 $\to$ the twenty-to-thirty bucket").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l3))
        self.wait(2.5)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = MathTex(r"3 + 8 + 11 + 5 + 3 = 30 \;\;\text{— count the counts}").scale(1.0).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): the skyline tells the story
        self.next_band(8)
        b8_title = Tex("The skyline tells the story").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        org8 = band_shift(8) + LEFT * 5.6 + DOWN * 2.6
        bars8 = histogram(org8, 1.1, 0.26)
        base8 = Line(org8, org8 + RIGHT * 5.9)
        self.play(Create(base8))
        self.play(Create(bars8))
        self.wait(2)
        b8_l1 = Tex(r"Downtown — the tallest tower — is the twenties").scale(0.95).shift(band_shift(8) + RIGHT * 3.1 + UP * 1.0)
        b8_l2 = Tex(r"Suburbs sprawl right: 5 then 3, the long commutes").scale(0.95).shift(band_shift(8) + RIGHT * 3.1 + UP * 0.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Tall means many, wide means nothing").scale(1.0).shift(band_shift(8) + RIGHT * 3.1 + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex(r"Towers touch: minutes are one unbroken road").scale(0.95).shift(band_shift(8) + RIGHT * 3.1 + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): saying what the picture means
        self.next_band(9)
        b9_title = Tex("Three questions, three sentences").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Where is the crowd? 11 of 30 in the twenties; mean 24").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex(r"How scattered? Under 10 to nearly 50 — a wide spread").scale(0.95).shift(band_shift(9) + UP * 0.3)
        b9_l3 = Tex(r"Lopsided? The tail points right — a few travel very far").scale(0.95).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex(r"``Skewed right'' is homework; context is analysis").scale(0.9).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex(r"Two skylines: compare crowd to crowd, tail to tail").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(4)
