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

# Band layout: one frame-height band per teaching beat; the camera moves down
# to fresh space and earlier work stays on the canvas. Only exporter-supported
# mobjects; every line of working is a single-string MathTex revealed with
# Write — no sub-part transforms.
#
# Mirrors script.md across all seven subtopics (Part 1 — Expert: 1-4;
# Part 2 — Simplifier: 5-7), band time roughly proportional to subtopics.json
# (230/240/240/250/180/190/170 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FunctionsRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the family album
        title = Tex("Functions and Trig Graphs: Exam Essentials").scale(1.0).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"y = ax + q, \; ax^2 + q, \; \tfrac{a}{x} + q, \; ab^x + q, \; a\sin x + q").scale(0.85).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex(r"$q$: slides the graph up or down (asymptote, midline)").scale(0.9).shift(DOWN * 0.1)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"$a$: stretch or amplitude; negative $a$ flips").scale(0.9).shift(DOWN * 1.0)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = MathTex(r"y = 3\sin x - 1: \; \text{amplitude } 3, \text{ midline } y = -1").scale(0.9).shift(DOWN * 2.0)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_2): line meets parabola
        self.next_band(1)
        b1_title = Tex("Line meets parabola").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"y = x^2 - 4: \; \text{cuts } x = \pm 2, \; \text{TP } (0; -4)").scale(0.95).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"x^2 - 4 = x + 2 \Rightarrow x^2 - x - 6 = 0").scale(0.95).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"(x-3)(x+2) = 0 \Rightarrow (3; 5) \text{ and } (-2; 0)").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = Tex(r"Parabola below the line for $-2 < x < 3$").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_3): asymptotes
        self.next_band(2)
        b2_title = Tex("Forbidden lines: asymptotes").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"y = \tfrac{4}{x} - 2: \; x = 0, \; y = -2 \; \text{(dotted first)}").scale(0.9).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{x-intercept: } \tfrac{4}{x} = 2 \Rightarrow x = 2").scale(0.95).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"y = 3^x - 1: \; \text{asymptote } y = -1, \text{ through } (0; 0)").scale(0.9).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex(r"Range: $y > -1$ strictly — the power never dies").scale(0.9).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_4): trig graphs
        self.next_band(3)
        b3_title = Tex("Trig graphs, $0°$ to $360°$").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = Tex(r"Sine departs the midline; cosine departs its peak").scale(0.9).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex(r"Tangent: asymptotes at $90°$ and $270°$, unbounded").scale(0.9).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"y = 3\sin x - 1: \; \max 2 \text{ at } 90°, \; \min -4 \text{ at } 270°").scale(0.85).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = MathTex(r"\text{Range: } -4 \le y \le 2").scale(0.95).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): the two controls
        self.next_band(4)
        b4_title = Tex("The stretch slider and the height jack").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex(r"$q$ jacks the whole picture; the asymptote rides along").scale(0.9).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex(r"$a$ stretches; the mirror switch flips bowls to domes").scale(0.9).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Say the controls aloud BEFORE working").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_6): four reading verbs
        self.next_band(5)
        b5_title = Tex("Four verbs: locate, compare, measure, count").scale(1.0).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"Locate: intercepts, turning points, dotted lines").scale(0.9).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\text{Measure at } x=0: \; 2 - (-4) = 6 \text{ units}").scale(0.95).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex(r"Count: line at $y=1$ cuts the deep wave twice").scale(0.9).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex(r"Every claim traces to the equation or a labelled point").scale(0.85).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_7): the six-line checklist
        self.next_band(6)
        b6_title = Tex("Six lines that sketch everything").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"1. Family \; 2. Controls \; 3. Skeleton").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex(r"4. Anchors \; 5. Sweep the curve \; 6. Domain and range").scale(0.9).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex(r"Curves approach dotted lines, never cross them").scale(0.9).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex(r"Grade 11 adds sideways shifts — a third control").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(4)
