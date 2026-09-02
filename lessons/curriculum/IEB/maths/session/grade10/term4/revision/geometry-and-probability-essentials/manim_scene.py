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
# (240/240/240/240/185/185/170 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GeometryProbabilityRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the shape family
        title = Tex("Geometry and Probability Essentials").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Parallelogram $\to$ rectangle / rhombus $\to$ square").scale(0.95).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex(r"Each generation ADDS a property, keeps the rest").scale(0.9).shift(DOWN * 0.1)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_l3 = Tex(r"Minimum tests: bisecting diagonals; one right angle; adjacent sides").scale(0.8).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex(r"Midpoint theorem: parallel to the third side, HALF of it (16 $\to$ 8)").scale(0.8).shift(DOWN * 2.1)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_2): two points, three formulas
        self.next_band(1)
        b1_title = Tex(r"A$(1; 3)$ and B$(6; 15)$").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"AB = \sqrt{5^2 + 12^2} = \sqrt{169} = 13").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2.5)
        b1_l2 = MathTex(r"\text{Midpoint} = (3{,}5; \; 9), \quad m = \tfrac{12}{5}").scale(1.0).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"\perp: \; \tfrac{12}{5} \times (-\tfrac{5}{12}) = -1").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex(r"Parallelogram proof: both diagonals share one midpoint").scale(0.85).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_3): probability and the addition rule
        self.next_band(2)
        b2_title = Tex("Count once, never twice").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_w1 = MathTex(r"22 + 15 = 37 \text{ players}").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_w1))
        self.play(Create(strike(b2_w1)))
        self.wait(2)
        b2_l1 = MathTex(r"22 + 15 - 9 = 28, \quad \text{neither} = 8").scale(1.0).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = MathTex(r"P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)").scale(0.9).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex(r"Exclusive: overlap $0$. Complementary: $P(\text{not }A) = 1 - P(A)$").scale(0.8).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l3))
        self.wait(3)

        # --- Band 3 (subtopic_4): statistics
        self.next_band(3)
        b3_title = Tex(r"Data: $4; 6; 9; 11; 14; 18; 22$").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\text{Mean} = \tfrac{84}{7} = 12, \quad \text{median} = 11").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"Q_1 = 6, \; Q_3 = 18, \; IQR = 12").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex(r"Five numbers: $4, 6, 11, 18, 22$ — box and whiskers").scale(0.9).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex(r"Mean above median, long right whisker: leans right").scale(0.85).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): inheritance
        self.next_band(4)
        b4_title = Tex("Properties down, proofs up").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex(r"Downwards: the square inherits every list above it").scale(0.9).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex(r"Upwards: pay only the cheapest entry ticket").scale(0.9).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex(r"`Midpoint' twice in a triangle = the theorem's calling card").scale(0.85).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(3)

        # --- Band 5 (subtopic_6): fair fractions
        self.next_band(5)
        b5_title = Tex("Fair fractions and the overlap fix").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"P(\text{red}) = \tfrac{5}{20} = 0{,}25 \; \text{(theory before drawing)}").scale(0.9).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex(r"More trials $\to$ relative frequency leans to theory").scale(0.9).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Venn golden rule: fill the overlap FIRST, work outwards").scale(0.9).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = MathTex(r"9 + 13 + 6 + 8 = 36 \; \checkmark").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_7): the box and the last patrol
        self.next_band(6)
        b6_title = Tex("Reading the box, running the patrol").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Order the data FIRST — quartiles demand it").scale(0.9).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex(r"Skewed data: report the median and say why").scale(0.9).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"Gradient is rise OVER run; overlap subtracted once").scale(0.9).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex(r"Totals confess: regions sum, five numbers ascend").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(4)
