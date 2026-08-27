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

# Band-layout whiteboard scene for the session duo "Histograms, Frequency
# Polygons and Ogives" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier:
# subtopics 5-7). One band per teaching beat, add-only lifecycle, camera
# moves down between bands. Only exporter-supported mobjects; write-only
# reveals. Band dwell times follow subtopics.json
# (230/220/225/235/195/185/195 of 1485 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class HistogramsPolygonsOgivesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the dataset, totals first ---
        title = Tex("Histograms, Frequency Polygons and Ogives").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("50 study times, five classes of width 15:").scale(1.05).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"[0;15)\!:4 \quad [15;30)\!:9 \quad [30;45)\!:17").scale(0.95).shift(UP * 0.1)
        b0_l3 = MathTex(r"[45;60)\!:12 \quad [60;75)\!:8").scale(0.95).shift(DOWN * 0.7)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = MathTex(r"\text{Audit: } 4+9+17+12+8 = 50 \checkmark").scale(1.0).shift(DOWN * 1.7)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the histogram — touching bars ---
        self.next_band(1)
        b1_title = Tex("The histogram: touching bars, height = frequency").scale(1.0).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        base = band_shift(1) + DOWN * 2.6 + LEFT * 3.75
        heights = [4, 9, 17, 12, 8]
        scale_h = 0.18
        bar_w = 1.5
        for i, h in enumerate(heights):
            bar = Rectangle(width=bar_w, height=h * scale_h)
            bar.move_to(base + RIGHT * (bar_w * i + bar_w / 2) + UP * (h * scale_h / 2))
            self.play(Create(bar), run_time=0.7)
        self.wait(2)
        b1_l1 = Tex("Tallest bar: modal class $[30;45)$").scale(1.0).shift(band_shift(1) + UP * 1.6)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Touching, because time has no gaps").scale(0.95).shift(band_shift(1) + UP * 0.8)
        self.play(Write(b1_l2))
        self.wait(3)

        # --- Band 2 (subtopic_1): the estimated mean and the median class ---
        self.next_band(2)
        b2_title = Tex("Estimated mean: everyone at the midpoint").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Midpoints: } 7{,}5;\; 22{,}5;\; 37{,}5;\; 52{,}5;\; 67{,}5").scale(0.95).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"30 + 202{,}5 + 637{,}5 + 630 + 540 = 2\,040").scale(0.95).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\bar{x} \approx \tfrac{2\,040}{50} = 40{,}8 \text{ minutes}").scale(1.05).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Median class: 25th and 26th values lie in $[30;45)$").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): the frequency polygon ---
        self.next_band(3)
        b3_title = Tex("Frequency polygon: midpoints, straight lines").scale(1.05).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        pbase = band_shift(3) + DOWN * 2.4 + LEFT * 3.75
        pts = [(-0.75, 0), (0.75, 4), (2.25, 9), (3.75, 17), (5.25, 12), (6.75, 8), (8.25, 0)]
        scale_h = 0.16
        dots = []
        for x, h in pts:
            d = Dot(pbase + RIGHT * x + UP * h * scale_h, radius=0.06)
            dots.append(d)
        segs = [Line(dots[i].get_center(), dots[i + 1].get_center()) for i in range(len(dots) - 1)]
        for d in dots:
            self.play(Create(d), run_time=0.35)
        for s in segs:
            self.play(Create(s), run_time=0.5)
        self.wait(2)
        b3_l1 = Tex("Anchor zeros at $-7{,}5$ and $82{,}5$").scale(0.95).shift(band_shift(3) + UP * 1.6)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("Built for comparisons: two profiles, one grid").scale(0.95).shift(band_shift(3) + UP * 0.8)
        self.play(Write(b3_l2))
        self.wait(3)

        # --- Band 4 (subtopic_3): the cumulative frequency column ---
        self.next_band(4)
        b4_title = Tex("Ogive: how many SO FAR").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"4,\; 13,\; 30,\; 42,\; 50").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("Final value must equal $n = 50$").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("Plot at UPPER class boundaries:").scale(1.05).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(1.5)
        b4_l4 = MathTex(r"(15;4)\;(30;13)\;(45;30)\;(60;42)\;(75;50)").scale(0.9).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex("Start the curve at $(0;0)$").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): drawing the lazy-S curve ---
        self.next_band(5)
        b5_title = Tex("The lazy-S curve").scale(1.2).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_title))
        self.wait(1.5)
        obase = band_shift(5) + DOWN * 2.6 + LEFT * 3.4
        oscale_x = 0.088
        oscale_y = 0.088
        opts = [(0, 0), (15, 4), (30, 13), (45, 30), (60, 42), (75, 50)]
        odots = [Dot(obase + RIGHT * x * oscale_x + UP * y * oscale_y, radius=0.06) for x, y in opts]
        osegs = [Line(odots[i].get_center(), odots[i + 1].get_center()) for i in range(len(odots) - 1)]
        for d in odots:
            self.play(Create(d), run_time=0.35)
        for s in osegs:
            self.play(Create(s), run_time=0.5)
        self.wait(2)
        b5_l1 = Tex("Steepest where the histogram is tallest").scale(0.95).shift(band_shift(5) + UP * 1.6)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Never downhill: a running total cannot shrink").scale(0.95).shift(band_shift(5) + UP * 0.8)
        self.play(Write(b5_l2))
        self.wait(3)

        # --- Band 6 (subtopic_4): median and quartiles off the curve ---
        self.next_band(6)
        b6_title = Tex("Across, then down").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Median at } \tfrac{n}{2} = 25: \approx 41 \text{ min}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = MathTex(r"Q_1 \text{ at } 12{,}5: \approx 29 \text{ min}").scale(1.05).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"Q_3 \text{ at } 37{,}5: \approx 54 \text{ min}").scale(1.05).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"\text{IQR} \approx 54 - 29 = 25 \text{ min}").scale(1.05).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): percentiles and threshold questions ---
        self.next_band(7)
        b7_title = Tex("Percentiles and thresholds").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"P_{90} \text{ at } 0{,}9 \times 50 = 45: \approx 66 \text{ min}").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("More than 55 min? UP from 55: about 38 below").scale(0.95).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"50 - 38 \approx 12 \text{ learners}").scale(1.05).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Say APPROXIMATELY — readings are estimates").scale(0.95).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the skyline and the mountain profile ---
        self.next_band(8)
        b8_title = Tex("The skyline and the mountain profile").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Buildings shoulder to shoulder: the histogram").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Tallest building $=$ modal class $[30;45)$").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Everyone stands mid-building: mean $\\approx 40{,}8$ min").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Rooftop dots joined: the mountain profile").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the running total tells a different story ---
        self.next_band(9)
        b9_title = Tex("The running total tells a different story").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Tuckshop book: TODAY column vs SO-FAR column").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Histogram = today. Ogive = so far.").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"4,\; 13,\; 30,\; 42,\; 50 \text{ — complete at class END}").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Steep = busy trading; flat = quiet; never downhill").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): across and down — the whole toolkit ---
        self.next_band(10)
        b10_title = Tex("Across and down — the whole toolkit").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Fifty learners in a line along the curve").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{Middle (25): } \approx 41. \; \text{Quarters: } \approx 29, \; \approx 54").scale(0.95).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = MathTex(r"P_{90} \text{ (45): } \approx 66. \;\; >55 \text{ min: } \approx 12 \text{ learners}").scale(0.95).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("Estimates, always — leave the ruler lines visible").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.wait(4)
