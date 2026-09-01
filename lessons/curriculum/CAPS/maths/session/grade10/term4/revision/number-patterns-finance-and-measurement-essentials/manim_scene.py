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

# Band layout: one frame-height band per teaching beat; the camera moves down
# to fresh space and earlier work stays on the canvas. Only exporter-supported
# mobjects; every line of working is a single-string MathTex revealed with
# Write — no sub-part transforms.
#
# Mirrors script.md across all seven subtopics (Part 1 — Expert: 1-4;
# Part 2 — Simplifier: 5-7), band time roughly proportional to subtopics.json
# (235/245/240/235/185/190/170 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PatternsFinanceMeasurementSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the general term from the difference
        title = Tex("Patterns, Finance and Measurement").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"5; \; 8; \; 11; \; 14: \quad d = 3").scale(1.1).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = MathTex(r"n = 1: \; 3(1) = 3, \text{ need } 5 \; \to \; +2").scale(1.05).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = MathTex(r"T_n = 3n + 2").scale(1.2).shift(DOWN * 0.9)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)
        b0_l4 = MathTex(r"\text{Check } T_4: \; 12 + 2 = 14 \; \checkmark").scale(1.05).shift(DOWN * 2.0)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): forwards, backwards, membership
        self.next_band(1)
        b1_l1 = MathTex(r"\text{Forwards: } T_{50} = 3(50) + 2 = 152").scale(1.05).shift(band_shift(1) + UP * 2.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"\text{Is 302 a term? } 3n = 300, \; n = 100 \; \checkmark").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"\text{Is 100? } 3n = 98, \; n = \tfrac{98}{3}").scale(1.05).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex(r"Not a natural number — 100 is NOT a term").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2.5)
        b1_l5 = MathTex(r"7; 12; 17: \; T_n = 5n + 2, \; T_{20} = 102").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the ladder and the snowball race
        self.next_band(2)
        b2_title = Tex(r"R2\,000 at 8\% for 5 years — two machines").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Simple: } A = P(1 + in)").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"A = 2000(1 + 0{,}4) = \text{R}2\,800").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{Compound: } A = P(1 + i)^n").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"A = 2000(1{,}08)^5 = \text{R}2\,938{,}66").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex(r"The snowball beats the ladder, and pulls away").scale(0.95).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): hire purchase, inflation, exchange
        self.next_band(3)
        b3_title = Tex(r"Hire purchase: R6\,000 TV, 10\% deposit").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\text{Balance: } 6000 - 600 = 5400").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"5400(1 + 0{,}24) = 6696 \; \text{(SIMPLE, 2 yrs)}").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"6696 \div 24 = \text{R}279 \text{ per month}").scale(1.05).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = MathTex(r"\text{Inflation: } 100(1{,}06)^3 = \text{R}119{,}10").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = MathTex(r"\$1 = \text{R}18{,}50: \; \$200 = \text{R}3\,700").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the catalogue — prism and cylinder
        self.next_band(4)
        b4_title = Tex("The catalogue: prism and cylinder").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\text{Prism } 4 \times 3 \times 5: \; V = 60").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"A = 2(12 + 20 + 15) = 94").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{Cylinder } r=3, h=10: \; V = 90\pi \approx 282{,}74").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = MathTex(r"A = 2\pi r(r + h) = 78\pi \approx 245{,}04").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): sphere, cone, pyramid
        self.next_band(5)
        b5_l1 = MathTex(r"\text{Sphere } r=6: \; V = \tfrac{4}{3}\pi(216) = 288\pi").scale(1.0).shift(band_shift(5) + UP * 2.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\text{Cone } r=3, h=4: \; V = \tfrac{1}{3}\pi r^2 h = 12\pi").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"s = \sqrt{9 + 16} = 5, \;\; A = \pi r(r+s) = 24\pi").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"\text{Pyramid, base 6, } h=4: \; V = 48, \; A = 96").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex(r"Perpendicular fills, slant wraps;").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        b5_l6 = Tex(r"the one-third is for pointy solids only").scale(1.0).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): the scale factor law
        self.next_band(6)
        b6_l1 = MathTex(r"\text{length} \times k, \text{area} \times k^2, \text{volume} \times k^3").scale(1.0).shift(band_shift(6) + UP * 2.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(3)
        b6_l2 = MathTex(r"k = 3: \; V = 50 \to 50 \times 27 = 1350").scale(1.05).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_wrong = Tex(r"Double every side: volume doubles").scale(1.05).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_l3 = MathTex(r"\text{It multiplies by } 2^3 = 8").scale(1.05).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex(r"Double ONLY $r$ in $\pi r^2 h$: volume $\times 4$ —").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        b6_l5 = Tex(r"one factor per appearance of the letter").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the error museum
        self.next_band(7)
        b7_title = Tex("The error museum").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"1. A fractional $n$ read as a yes — it means NO").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex(r"2. Compound computed as simple — flattened snowball").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"3. Slant height inside a volume formula").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex(r"4. Doubling lengths, doubling volume — it cubes").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex(r"Rehearse the exhibits; keep the marks").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): patterns as staircases
        self.next_band(8)
        b8_title = Tex("Patterns as staircases").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Equal steps of 3; the ground floor is $5 - 3 = 2$").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\text{Height at step } n: \; 3n + 2").scale(1.1).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex(r"Ride up: step 50 sits at height 152").scale(1.0).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex(r"A staircase has no step $\tfrac{98}{3}$ —").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        b8_l5 = Tex(r"a fractional step means: not in the pattern").scale(1.0).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): money on two ladders
        self.next_band(9)
        b9_title = Tex("Money on two ladders").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Ladder: R160 a year, five rungs, R2\,800").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"Snowball: interest joins the ball — R2\,938,66").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex(r"Hire purchase = the ladder with a shop sign:").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = MathTex(r"5400 \to 6696 \to \text{R}279/\text{month}").scale(1.05).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex(r"``Compounded'' or ``inflation'' names the snowball").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): boxes, tins and the final sweep
        self.next_band(10)
        b10_title = Tex("Boxes, tins and the final sweep").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Volume: stack the base. Surface: wrap the faces").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex(r"Pointy cousins hold one third of their tin").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Inside height fills; leaning height wraps").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"Match the power to the dimension: $k$, $k^2$, $k^3$").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex(r"Test a known term; recompute one interest line;").scale(0.9).shift(band_shift(10) + DOWN * 2.2)
        b10_l6 = Tex(r"sense-check every volume — free proofs").scale(0.9).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
