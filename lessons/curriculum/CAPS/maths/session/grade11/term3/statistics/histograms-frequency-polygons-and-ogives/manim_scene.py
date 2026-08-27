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

# Band-layout whiteboard scene (reference: quadratics-by-factorisation).
# One band per teaching beat, add-only lifecycle, camera moves down between
# bands. Covers all seven subtopics: Part 1 Expert (grouped data revision,
# frequency polygons, building the ogive, reading the ogive) then Part 2
# Simplifier (skyline and mountain profile, the running total, across and
# down). One dataset runs through: 40 learners' travel times.
# Band dwell proportional to subtopics.json (230/220/225/235/195/185/195
# of 1485 s). Histogram bars are Rectangles, polygon/ogive are Dot + Line
# chains — exporter-supported primitives only.

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
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the dataset, totals first ---
        title = Tex("Histograms, Frequency Polygons and Ogives").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("40 learners' travel times, in classes:").scale(1.1).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(1.5)
        b0_l2 = MathTex(r"[0;10)\!: 6 \quad [10;20)\!: 10 \quad [20;30)\!: 14").scale(1.0).shift(UP * 0.1)
        b0_l3 = MathTex(r"[30;40)\!: 7 \quad [40;50)\!: 3").scale(1.0).shift(DOWN * 0.7)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = MathTex(r"\text{Check: } 6+10+14+7+3 = 40").scale(1.1).shift(DOWN * 1.7)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the histogram — touching bars ---
        self.next_band(1)
        b1_title = Tex("Histogram: touching bars, no gaps").scale(1.15).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        base = band_shift(1) + DOWN * 1.9 + LEFT * 2.6
        ax_x = Line(base + LEFT * 0.4, base + RIGHT * 5.6)
        ax_y = Line(base, base + UP * 3.4)
        self.play(Create(ax_x), Create(ax_y))
        freqs = [6, 10, 14, 7, 3]
        bars = []
        for i, f in enumerate(freqs):
            h = f * 0.2
            bar = Rectangle(width=1.0, height=h, color=BLUE).move_to(
                base + RIGHT * (0.5 + i * 1.0) + UP * h / 2)
            bars.append(bar)
        for bar in bars:
            self.play(Create(bar), run_time=0.6)
        labs = VGroup(*[
            MathTex(str(v)).scale(0.6).move_to(base + RIGHT * i + DOWN * 0.35)
            for i, v in [(0, 0), (1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]])
        self.play(Write(labs))
        self.wait(2)
        b1_l1 = Tex("Tallest bar $= [20;30)$: the modal class").scale(1.05).shift(band_shift(1) + UP * 1.6 + RIGHT * 2.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Bars touch — time is continuous").scale(1.0).shift(band_shift(1) + DOWN * 3.3)
        self.play(Write(b1_l2))
        self.wait(2.5)

        # --- Band 2 (subtopic_1): the estimated mean and the median class ---
        self.next_band(2)
        b2_title = Tex("Estimated mean: everyone at the midpoint").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Midpoints: } 5,\; 15,\; 25,\; 35,\; 45").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"6(5) + 10(15) + 14(25) + 7(35) + 3(45)").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"= 30 + 150 + 350 + 245 + 135 = 910").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"\bar{x} \approx \tfrac{910}{40} = 22{,}75 \text{ minutes}").scale(1.1).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)
        b2_l5 = Tex("Median: values 20 and 21 sit in $[20;30)$").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): the frequency polygon ---
        self.next_band(3)
        b3_title = Tex("Frequency polygon: midpoints, straight lines").scale(1.1).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        og = band_shift(3) + DOWN * 1.7 + LEFT * 2.5
        sx, sy = 0.075, 0.18
        ax2_x = Line(og + LEFT * 0.6, og + RIGHT * 5.1)
        ax2_y = Line(og, og + UP * 3.0)
        self.play(Create(ax2_x), Create(ax2_y))
        pts = [(-5, 0), (5, 6), (15, 10), (25, 14), (35, 7), (45, 3), (55, 0)]
        dots = [Dot(og + RIGHT * ((x + 5) * sx) + UP * (y * sy), radius=0.06)
                for x, y in pts]
        for d in dots:
            self.play(Create(d), run_time=0.4)
        segs = [Line(dots[i].get_center(), dots[i + 1].get_center(), color=BLUE)
                for i in range(len(dots) - 1)]
        for s in segs:
            self.play(Create(s), run_time=0.5)
        self.wait(2)
        b3_l1 = Tex(r"Anchor zeros at $-5$ and $55$ close the shape").scale(1.0).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("Built for comparison — two polygons, one grid").scale(1.0).shift(band_shift(3) + UP * 1.5 + RIGHT * 2.0)
        self.play(Write(b3_l2))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the cumulative frequency column ---
        self.next_band(4)
        b4_title = Tex("Ogive step 1: the running total").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"6 \to 6+10=16 \to 16+14=30").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"30+7=37 \to 37+3=40 = n").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex("Plot at UPPER class boundaries:").scale(1.05).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(1.5)
        b4_l4 = MathTex(r"(10;6),\,(20;16),\,(30;30),\,(40;37),\,(50;40)").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex(r"Start at $(0;0)$ — nothing has accumulated yet").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): drawing the lazy-S curve ---
        self.next_band(5)
        b5_title = Tex("The ogive: a lazy S that never dips").scale(1.15).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_title))
        self.wait(1.5)
        og5 = band_shift(5) + DOWN * 1.8 + LEFT * 2.4
        sx5, sy5 = 0.09, 0.075
        ax5_x = Line(og5 + LEFT * 0.5, og5 + RIGHT * 5.2)
        ax5_y = Line(og5, og5 + UP * 3.3)
        self.play(Create(ax5_x), Create(ax5_y))
        opts = [(0, 0), (10, 6), (20, 16), (30, 30), (40, 37), (50, 40)]
        odots = [Dot(og5 + RIGHT * (x * sx5) + UP * (y * sy5), radius=0.06)
                 for x, y in opts]
        for d in odots:
            self.play(Create(d), run_time=0.4)
        osegs = [Line(odots[i].get_center(), odots[i + 1].get_center(), color=BLUE)
                 for i in range(len(odots) - 1)]
        for s in osegs:
            self.play(Create(s), run_time=0.5)
        self.wait(2)
        b5_l1 = Tex("Steepest where the histogram is tallest").scale(1.0).shift(band_shift(5) + UP * 1.5 + RIGHT * 2.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("A running total can never shrink").scale(1.0).shift(band_shift(5) + DOWN * 3.4)
        self.play(Write(b5_l2))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): median and quartiles off the curve ---
        self.next_band(6)
        b6_title = Tex("Reading the ogive: across, then down").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Median at } \tfrac{n}{2} = 20: \approx 23 \text{ min}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"Q_1 \text{ at } \tfrac{n}{4} = 10: \approx 14 \text{ min}").scale(1.05).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"Q_3 \text{ at } \tfrac{3n}{4} = 30: \approx 30 \text{ min}").scale(1.05).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"IQR \approx 30 - 14 = 16 \text{ minutes}").scale(1.05).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): percentiles and threshold questions ---
        self.next_band(7)
        b7_title = Tex("Percentiles, and reading in reverse").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"P_{90} \text{ at } 0{,}9 \times 40 = 36: \approx 39 \text{ min}").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex(r"More than 35 min? UP from 35: $\approx 34$ below").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"40 - 34 \approx 6 \text{ learners}").scale(1.1).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Say ``approximately'' — readings are estimates").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Leave the ruler lines on — they earn marks").scale(1.0).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the skyline and the mountain profile ---
        self.next_band(8)
        b8_title = Tex("The skyline and the mountain profile").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Histogram $=$ skyline: touching buildings").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Tallest building $=$ modal class $[20;30)$").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("The building swallows the floor — so estimate:").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = MathTex(r"\text{mid-building: } \bar{x} \approx \tfrac{910}{40} = 22{,}75").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2.5)
        b8_l5 = Tex("Rooftop dots joined $=$ mountain profile (polygon)").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the running total tells a different story ---
        self.next_band(9)
        b9_title = Tex("The running total tells a different story").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Histogram: the this-month column").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Ogive: the total-so-far column, as a curve").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"6,\; 16,\; 30,\; 37,\; 40 \text{ — complete at class END}").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Steep $=$ deposits pouring in; flat $=$ quiet months").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Money already counted stays counted: never downhill").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): across and down — the whole toolkit ---
        self.next_band(10)
        b10_title = Tex("Across and down — the forty in a line").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"\text{Middle of the line (20): median} \approx 23 \text{ min}").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"Q_1 \approx 14, \; Q_3 \approx 30, \; IQR \approx 16").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"P_{90} \text{ (position } 36\text{)} \approx 39 \text{ min}").scale(1.05).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = MathTex(r"\text{Over } 35 \text{ min: } 40 - 34 = 6 \text{ learners}").scale(1.05).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex("Say approximately like you mean it").scale(1.05).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l5))
        self.wait(4)
