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

# Band-layout whiteboard scene (reference: quadratics-by-factorisation).
# One band per teaching beat, add-only lifecycle, camera moves down between
# bands. Covers all seven subtopics: Part 1 Expert (circle geometry toolkit,
# gradient and inclination, statistics with deviation and outliers, finance
# and probability) then Part 2 Simplifier (the circle as a crime scene, data
# that tells on itself, two slopes and the final sweep). Band dwell
# proportional to subtopics.json (250/240/240/250/185/185/180 of 1530 s).

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
        circ = Circle(radius=1.5, color=BLUE).shift(UP * 0.6 + LEFT * 3.5)
        chord = Line(circ.point_at_angle(PI / 6), circ.point_at_angle(5 * PI / 6), color=YELLOW)
        self.play(Create(circ), Create(chord))
        self.wait(2)
        b0_l1 = MathTex(r"\text{radius } 17, \text{ distance } 8").scale(1.0).shift(UP * 1.0 + RIGHT * 2.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"\text{half-chord} = \sqrt{17^2 - 8^2} = 15").scale(1.0).shift(UP * 0.0 + RIGHT * 2.2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = MathTex(r"\text{chord} = 30").scale(1.05).shift(DOWN * 0.9 + RIGHT * 2.2)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = MathTex(r"\text{Centre angle } 130^\circ \Rightarrow \text{circumference } 65^\circ").scale(0.95).shift(DOWN * 2.0)
        self.play(Write(b0_l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): same-arc and tangent families ---
        self.next_band(1)
        b1_title = Tex("Same-arc and tangent families").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Angles on the same arc, same side: equal").scale(0.95).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"\text{Cyclic quad: } 110^\circ \text{ opposite } 70^\circ").scale(1.0).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Tangent $\\perp$ radius; two tangents equal").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Tan-chord: the angle teleports to the alternate segment").scale(0.9).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2.5)
        b1_l5 = Tex("Every statement travels WITH its reason").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l5))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): gradient and inclination ---
        self.next_band(2)
        b2_title = MathTex(r"m = \tan\theta, \quad 0^\circ \le \theta < 180^\circ").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.play(Create(SurroundingRectangle(b2_title, color=GREEN)))
        self.wait(2)
        b2_l1 = MathTex(r"A(1; -2), \; B(5; 6): \; m = \frac{6 - (-2)}{5 - 1} = 2").scale(0.95).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\theta = \tan^{-1} 2 \approx 63{,}4^\circ").scale(1.0).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"m = -2: \; \theta = 180^\circ - 63{,}4^\circ = 116{,}6^\circ").scale(0.95).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("Negative gradient always means obtuse inclination").scale(0.9).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): lines, parallel, perpendicular ---
        self.next_band(3)
        b3_title = MathTex(r"y - y_1 = m(x - x_1)").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Through } B(5; 6), \; m = 2: \; y - 6 = 2(x - 5)").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex("Parallel: copy the gradient").scale(0.95).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"\text{Perpendicular: } 2 \to -\tfrac{1}{2}, \;\; \text{product } -1").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Sketch first — the sketch predicts every sign").scale(0.95).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): variance and standard deviation ---
        self.next_band(4)
        b4_title = MathTex(r"3;\; 5;\; 9;\; 11;\; 12 \quad \bar{x} = 8").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Deviations: } -5, -3, 1, 3, 4 \; (\text{sum } 0)").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\text{Squares: } 25, 9, 1, 9, 16 \Rightarrow \text{variance } \tfrac{60}{5} = 12").scale(0.95).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"\sigma = \sqrt{12} \approx 3{,}46").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex("Small $\\sigma$: huddled. Large $\\sigma$: scattered").scale(0.95).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): ogives and the outlier fences ---
        self.next_band(5)
        b5_title = Tex("Ogive: across, touch, down").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Plot cumulative totals at UPPER boundaries").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Half of $n$: median. Quarters: quartiles").scale(0.95).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"Q_1 = 15, \; Q_3 = 25: \; \text{fences } 0 \text{ and } 40").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"44 > 40 \Rightarrow \text{outlier, by definition}").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the two decay slopes ---
        self.next_band(6)
        b6_title = Tex("R120 000 bakkie, 20\\% p.a., 3 years").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Straight line: } 120\,000(1 - 0{,}6) = \text{R}48\,000").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\text{Reducing balance: } 120\,000(0{,}8)^3 = \text{R}61\,440").scale(0.95).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex("Same rate — R13 440 apart").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("The wording chooses the formula").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): effective rates and independence ---
        self.next_band(7)
        b7_title = Tex("Labels, contents, and independence").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"18\% \text{ monthly: } (1{,}015)^{12} - 1 \approx 19{,}56\%").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(2.5)
        b7_l2 = Tex("Nominal is the label; effective is the contents").scale(0.95).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"P(A)P(B) = 0{,}3 \times 0{,}6 = 0{,}18 = P(A \text{ and } B)").scale(0.9).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("Independent — proven by multiplication, never assumed").scale(0.9).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the circle as a crime scene ---
        self.next_band(8)
        b8_title = Tex("The circle as a crime scene").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Witness 1 — the centre: $90^\\circ$ to any chord").scale(0.95).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Witness 2 — the arc: doubled at the centre, equal at the rim").scale(0.9).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Witness 3 — the tangent: $90^\\circ$, plus the alternate whisper").scale(0.9).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Mark givens, chase one theorem at a time, file reasons").scale(0.9).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2.5)
        b8_l5 = Tex("Hunt: diameter, cyclic quad, tangent").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): data that tells on itself ---
        self.next_band(9)
        b9_title = Tex("Data that tells on itself").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Recipe: mean, deviations, square, average, root").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.play(Create(SurroundingRectangle(b9_l1, color=GREEN)))
        self.wait(2.5)
        b9_l2 = Tex("Square because raw deviations cancel to zero").scale(0.95).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Ogive staircase: across, touch, down").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"\text{Fences: } Q_1 - 1{,}5\,\text{IQR}, \;\; Q_3 + 1{,}5\,\text{IQR}").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Mean far above median? The data is telling on its extremes").scale(0.85).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.wait(2.5)

        # --- Band 10 (subtopic_7): two slopes, one honest rate ---
        self.next_band(10)
        b10_title = Tex("Two slopes, one honest rate").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Ramp: same chunk of the ORIGINAL, every year").scale(0.95).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Bouncing ball: shrinking bites of what REMAINS").scale(0.95).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"\text{R}48\,000 \text{ vs R}61\,440 \text{ — the words decide}").scale(0.95).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex("Sweep: reasons filed, $180^\\circ$ minus, square first, ball vs ramp").scale(0.85).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Audit everything against its own picture — free proof").scale(0.9).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.wait(4)
