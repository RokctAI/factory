# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene. One band per teaching beat; the camera moves
# down to clean space and nothing is ever removed. Bars are Rectangles on
# Line axes (exporter-safe primitives only). Covers all seven subtopics of
# the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7), dwell times
# roughly proportional to subtopics.json (160/170/180/180/160/160/160 of
# 1170 s).

BAND = config.frame_height

FREQS = [6, 16, 9, 6, 3]
BAR_W = 0.9
UNIT_H = 0.15


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


def histogram(org, freqs=FREQS, color=BLUE, gap=0.0):
    """Touching bars standing on a baseline starting at org (bottom-left)."""
    bars = VGroup()
    x = 0.0
    for f in freqs:
        h = f * UNIT_H
        bar = Rectangle(width=BAR_W, height=h, color=color)
        bar.move_to(org + RIGHT * (x + BAR_W / 2) + UP * (h / 2))
        bars.add(bar)
        x += BAR_W + gap
    return bars


class HistogramsInterpretingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): raw data to frequency table
        title = Tex("From Raw Data to a Frequency Table").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"40 homework times, in minutes — a heap of numbers").scale(0.95).shift(UP * 1.3)
        b0_l2 = Tex(r"Equal class intervals: $0$–$20$, $20$–$40$, $40$–$60$, $60$–$80$, $80$–$100$").scale(0.9).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"Boundary rule: keep the bottom, refuse the top — exactly 40 $\to$ class $40$–$60$").scale(0.8).shift(DOWN * 0.5)
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = MathTex(r"\text{Frequencies: } 6, \; 16, \; 9, \; 6, \; 3").scale(1.0).shift(DOWN * 1.4)
        b0_l5 = MathTex(r"6 + 16 + 9 + 6 + 3 = 40 \;\checkmark").scale(1.0).shift(DOWN * 2.3)
        self.play(Write(b0_l4))
        self.wait(2.5)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): building the histogram
        self.next_band(1)
        b1_title = Tex("Building the histogram").scale(1.2).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        org1 = band_shift(1) + DOWN * 1.8 + LEFT * 2.6
        x_axis1 = Line(org1 + LEFT * 0.4, org1 + RIGHT * 5.4)
        y_axis1 = Line(org1, org1 + UP * 3.0)
        self.play(Create(x_axis1), Create(y_axis1))
        self.wait(1.5)
        xlabs = VGroup(*[
            MathTex(str(v)).scale(0.55).next_to(org1 + RIGHT * (i * BAR_W), DOWN, buff=0.2)
            for i, v in enumerate([0, 20, 40, 60, 80, 100])
        ])
        self.play(Write(xlabs))
        self.wait(1.5)
        bars1 = histogram(org1)
        for bar, f in zip(bars1, FREQS):
            self.play(Create(bar), run_time=0.7)
            self.play(Write(MathTex(str(f)).scale(0.6).next_to(bar, UP, buff=0.1)), run_time=0.4)
        self.wait(2)
        b1_l1 = Tex(r"Horizontal: minutes. \; Vertical: frequency. \; Label everything").scale(0.8).next_to(x_axis1, DOWN, buff=0.8)
        self.play(Write(b1_l1))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the bars touch — and why
        self.next_band(2)
        b2_title = Tex("The bars TOUCH — and why").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        org2 = band_shift(2) + DOWN * 0.6 + LEFT * 4.6
        bars2 = histogram(org2)
        self.play(Create(bars2))
        self.wait(1.5)
        b2_l1 = Tex(r"Continuous: 39,9 flows into 40,0 — nothing in between").scale(0.8).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l1))
        self.wait(2.5)
        org2b = band_shift(2) + DOWN * 0.6 + RIGHT * 1.0
        bars2b = histogram(org2b, freqs=[8, 12, 6], color=ORANGE, gap=0.45)
        self.play(Create(bars2b))
        self.wait(1.5)
        b2_l2 = Tex(r"Categories (subjects, sports): separated bars — a bar graph").scale(0.8).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex(r"Gaps mean categories; touching bars mean measurement").scale(0.85).shift(band_shift(2) + DOWN * 3.2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): peak, middle, mean
        self.next_band(3)
        b3_title = Tex("Three passes: peak, middle, mean").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"1. Peak: modal class $20$–$40$ (16 of the 40)").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex(r"2. Middle: cumulative $6, 22, 31, 37, 40$").scale(1.0).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex(r"20th and 21st sit in class $20$–$40$ — the median class").scale(0.9).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = MathTex(r"3. \; \bar{x} \approx \frac{60 + 480 + 450 + 420 + 270}{40} = \frac{1\,680}{40} = 42").scale(0.9).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)
        b3_l5 = Tex(r"Midpoints $10, 30, 50, 70, 90$ stand in for their classes").scale(0.85).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the tail names the skew
        self.next_band(4)
        b4_title = Tex("The tail names the skew").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        org4 = band_shift(4) + DOWN * 0.4 + LEFT * 2.2
        bars4 = histogram(org4)
        self.play(Create(bars4))
        self.wait(1.5)
        tail_arrow = Arrow(org4 + RIGHT * 2.2 + UP * 1.6, org4 + RIGHT * 4.9 + UP * 0.6, color=YELLOW)
        self.play(Create(tail_arrow))
        self.wait(2)
        b4_l1 = Tex(r"Long tail RIGHT $\Rightarrow$ skewed to the right (positive)").scale(0.9).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex(r"Named after the TAIL, never the peak —").scale(0.9).shift(band_shift(4) + DOWN * 2.2)
        b4_l3 = Tex(r"a right-skewed histogram peaks on the LEFT").scale(0.9).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): the comment template
        self.next_band(5)
        b5_title = Tex("The comment: centre, spread, shape").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Centre: modal class $20$–$40$, mean 42 min —").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"a typical learner works around forty minutes").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Spread: under 20 to nearly 100 — habits differ sharply").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex(r"Shape: skewed right — most moderate, a few very long").scale(0.95).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex(r"Every sentence: a feature $+$ its meaning in context").scale(0.95).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): comparisons and hygiene
        self.next_band(6)
        b6_title = Tex("Comparisons, and two hygiene rules").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Compare like with like: centre vs centre, spread vs spread").scale(0.9).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex(r"Second grade: same peak, nobody past 60 —").scale(0.9).shift(band_shift(6) + UP * 0.3)
        b6_l3 = Tex(r"similar centre, narrower spread, more uniform habits").scale(0.9).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex(r"Rule 1: stay in context — talk about learners, not bars").scale(0.9).shift(band_shift(6) + DOWN * 1.5)
        b6_l5 = Tex(r"Rule 2: claim only what the display shows — no exact times, no whys").scale(0.8).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l4))
        self.wait(2.5)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): sorting the stack into pigeonholes
        self.next_band(7)
        b7_title = Tex("Sorting the stack into pigeonholes").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        holes = VGroup(*[
            Rectangle(width=1.5, height=1.1).shift(band_shift(7) + UP * 0.6 + LEFT * 4.0 + RIGHT * i * 1.7)
            for i in range(5)
        ])
        hole_labels = VGroup(*[
            Tex(lab).scale(0.5).next_to(holes[i], DOWN, buff=0.15)
            for i, lab in enumerate(["0–20", "20–40", "40–60", "60–80", "80–100"])
        ])
        self.play(Create(holes), Write(hole_labels))
        self.wait(2)
        counts = VGroup(*[
            MathTex(str(f)).scale(0.8).move_to(holes[i])
            for i, f in enumerate(FREQS)
        ])
        self.play(Write(counts))
        self.wait(2.5)
        b7_l1 = Tex(r"Exactly 40? Keep the bottom, refuse the top: hole $40$–$60$").scale(0.85).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"\text{Count the counts: } 6 + 16 + 9 + 6 + 3 = 40 \;\checkmark").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): the mountain range tells the story
        self.next_band(8)
        b8_title = Tex("The mountain range tells the story").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        org8 = band_shift(8) + DOWN * 0.6 + LEFT * 2.2
        bars8 = histogram(org8)
        self.play(Create(bars8))
        self.wait(2)
        summit = Tex("summit").scale(0.7).next_to(bars8[1], UP, buff=0.15)
        self.play(Write(summit))
        self.wait(2)
        b8_l1 = Tex(r"Summit over $20$–$40$: where the times crowd").scale(0.9).shift(band_shift(8) + DOWN * 1.5)
        b8_l2 = Tex(r"Foothills run right: the long-homework tail").scale(0.9).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Tall means many; wide means nothing").scale(0.95).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): saying what the picture means
        self.next_band(9)
        b9_title = Tex("Saying what the picture means").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Where is the crowd? \; 16 of 40 in $20$–$40$; mean 42").scale(0.9).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"How scattered? \; Under 20 to nearly 100 minutes").scale(0.9).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex(r"Lopsided? \; Ridge runs right — skewed right").scale(0.9).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex(r"Each sentence returns the numbers to real learners").scale(0.9).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex(r"Compare in pairs: crowd–crowd, scatter–scatter, ridge–ridge").scale(0.85).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(4)
