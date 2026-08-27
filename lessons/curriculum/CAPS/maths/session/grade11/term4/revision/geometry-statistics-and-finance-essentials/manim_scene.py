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
# bands. Covers all seven subtopics: Part 1 Expert (circle geometry toolkit,
# analytical geometry with inclination, statistics with deviation and
# outliers, finance and probability) then Part 2 Simplifier (the circle as a
# crime scene, data that tells on itself, two slopes and one honest rate).
# Band dwell proportional to subtopics.json (250/240/240/250/185/185/180
# of 1530 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GeometryStatsFinanceRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(16)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): centre theorems, Pythagoras in chords ---
        title = Tex("Geometry, Statistics and Finance Essentials").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Perpendicular from centre bisects the chord").scale(1.05).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"r = 13, \; d = 5: \; \text{half-chord} = \sqrt{169 - 25} = 12").scale(1.0).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = MathTex(r"\text{Chord} = 24 \text{ — Pythagoras hides inside}").scale(1.05).shift(DOWN * 0.8)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = Tex(r"Centre $=$ 2 $\times$ circumference: $140^\circ \to 70^\circ$").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex(r"Angle in a semicircle: $90^\circ$").scale(1.05).shift(DOWN * 2.8)
        self.play(Write(b0_l5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): same-arc and tangent families ---
        self.next_band(1)
        b1_title = Tex("Same-arc and tangent families").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Same arc, same side: equal angles").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"Cyclic quad opposites: $95^\circ + 85^\circ = 180^\circ$").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex(r"Tangent $\perp$ radius; two tangents equal").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Tan-chord: the angle teleports to the alternate segment").scale(0.95).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("Every statement carries its reason — half the mark").scale(1.0).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): gradient and inclination ---
        self.next_band(2)
        b2_title = MathTex(r"m = \tan\theta, \; 0^\circ \leq \theta < 180^\circ").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"A(-2; 1), \; B(4; 5): \; m = \tfrac{5 - 1}{4 + 2} = \tfrac{2}{3}").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\theta = \tan^{-1}\tfrac{2}{3} = 33{,}7^\circ").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = MathTex(r"m = -1: \; \theta = 180^\circ - 45^\circ = 135^\circ").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("Negative gradient always means obtuse inclination").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): lines, parallel, perpendicular ---
        self.next_band(3)
        b3_title = Tex("One point and a gradient build the line").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"y - y_1 = m(x - x_1)").scale(1.15).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2)
        b3_l2 = MathTex(r"y - 5 = \tfrac{2}{3}(x - 4)").scale(1.1).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"\parallel: \text{copy } m; \; \perp: \tfrac{2}{3} \to -\tfrac{3}{2}").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex("Chained questions are one tool per step — sketch first").scale(0.95).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): variance and standard deviation ---
        self.next_band(4)
        b4_title = Tex("Spread, professionally: 4; 6; 8; 10; 12").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\bar{x} = \tfrac{40}{5} = 8").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\text{Deviations: } -4, -2, 0, 2, 4 \;\; (\text{sum } 0)").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"16, 4, 0, 4, 16: \text{variance} = \tfrac{40}{5} = 8").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = MathTex(r"\sigma = \sqrt{8} \approx 2{,}83").scale(1.15).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): ogives and the outlier fences ---
        self.next_band(5)
        b5_title = Tex("Ogives and fences").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Cumulative totals at UPPER boundaries, climb to $n$").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Median and quartiles: across, touch, down").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"Q_1 = 20, \; Q_3 = 32: \; IQR = 12").scale(1.05).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"\text{Fences: } 20 - 18 = 2 \text{ and } 32 + 18 = 50").scale(1.05).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = MathTex(r"55 > 50 \Rightarrow \text{outlier — by definition}").scale(1.05).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the two decay slopes ---
        self.next_band(6)
        b6_title = Tex("Decay: R80 000 car, 15\\% per year, 4 years").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Straight line: } A = P(1 - in)").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"80\,000(1 - 0{,}6) = \text{R}32\,000").scale(1.05).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"\text{Reducing balance: } A = P(1 - i)^n").scale(1.05).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"80\,000(0{,}85)^4 = \text{R}41\,760{,}50").scale(1.05).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("The formula choice IS the question").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l5))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): effective rates and independence ---
        self.next_band(7)
        b7_title = Tex("Honest rates, and independence proven").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"12\% \text{ nominal, monthly: } (1{,}01)^{12} - 1").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"= 12{,}68\% \text{ effective — the true price}").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = MathTex(r"\text{Test: } P(A)P(B) = 0{,}4 \times 0{,}5 = 0{,}2 = P(A \text{ and } B)").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("Equal — independent: proven, not assumed").scale(1.05).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Museum: no reason; acute slip; unsquared; wrong slope").scale(0.9).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the circle as a crime scene ---
        self.next_band(8)
        b8_title = Tex("The circle as a crime scene").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Witness 1 — the centre: chords hide right angles").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Witness 2 — the arc: ask every angle which arc it watches").scale(0.95).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Witness 3 — the tangent: $90^\\circ$, plus the whisper").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("High-value patterns: diameter, cyclic quad, tangent").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("File every reason — it is half the mark").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): data that tells on itself ---
        self.next_band(9)
        b9_title = Tex("Data that tells on itself").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Square the strays — deviations sum to zero by design").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\sigma = \sqrt{8} \approx 2{,}83").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("The ogive staircase: across, touch, down").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Fences at $1{,}5 \\times IQR$: judged, not debated").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Mean far above median? The data tells on its extremes").scale(0.95).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 10 (subtopic_7): two slopes, one honest rate ---
        self.next_band(10)
        b10_title = Tex("Two slopes, one honest rate — final sweep").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("The ramp: same rand lost yearly — R32 000 left").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("The bouncing ball: 15\\% of what REMAINS — R41 760,50").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Labels vs contents: 12\\% monthly is really 12,68\\%").scale(0.95).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("Independence: multiply, compare, conclude").scale(1.0).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex("Audit each answer against its own picture — free proof").scale(0.95).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l5))
        self.wait(4)
