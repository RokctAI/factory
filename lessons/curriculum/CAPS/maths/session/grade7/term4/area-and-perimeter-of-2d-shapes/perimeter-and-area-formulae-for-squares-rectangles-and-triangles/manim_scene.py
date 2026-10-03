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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all 5 subtopics
# (Part 1 — Expert: subtopics 1-3; Part 2 — Simplifier: subtopics 4-5), with
# dwell time proportional to subtopics.json (160/140/120/120/120 of
# 660 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class AreaFormulaeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Squares and rectangles
        t0 = Tex(r"Squares and rectangles").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"A = l \times b = 8 \times 6 = 48 \text{ m}^2").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m1, color=GREEN)))
        self.wait(1.5)
        m2 = MathTex(r"A = s^2 = 1{,}2 \times 1{,}2 = 1{,}44 \text{ m}^2").scale(1.0).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"P = 2l + 2b = 28 \text{ m} \qquad P = 4s").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Perimeter: m. Area: m$^2$.").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(4)

        # --- Band 1 (subtopic_2): Area of a triangle
        self.next_band(1)
        t1 = Tex(r"Area of a triangle").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"A = \tfrac{1}{2} \times b \times h").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m5, color=GREEN)))
        self.wait(1.5)
        m6 = Tex(r"Triangle = half of the rectangle around it").scale(0.95).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"\tfrac{1}{2} \times 40 \times 30 = 600 \text{ cm}^2").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Height is PERPENDICULAR to the base, not a slope").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(4)

        # --- Band 2 (subtopic_3): Using formulae
        self.next_band(2)
        t2 = Tex(r"Using formulae").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = Tex(r"Formula, substitute, calculate, unit").scale(0.95).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"7{,}5 \times 4 = 30 \text{ m}^2 \qquad P = 23 \text{ m}").scale(1.0).shift(band_shift(2) + UP * 0.18)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"2 \text{ m} \times 0{,}5 \text{ m} = 1 \text{ m}^2").scale(1.0).shift(band_shift(2) + DOWN * 0.85)
        self.play(Write(m11))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m11, color=GREEN)))
        self.wait(1.5)
        m12 = MathTex(r"b = 48 \div 8 = 6 \text{ m} \qquad 600 = 20h \Rightarrow h = 30").scale(1.0).shift(band_shift(2) + DOWN * 1.87)
        self.play(Write(m12))
        self.wait(2)
        m13 = MathTex(r"s = \sqrt{49} = 7 \text{ cm}").scale(1.0).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m13))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Tiling the floor
        self.next_band(3)
        t3 = Tex(r"Tiling the floor").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m14 = Tex(r"8 tiles in a row, 6 rows").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"6 \times 8 = 48 \text{ m}^2").scale(1.0).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m15))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m15, color=GREEN)))
        self.wait(1.5)
        m16 = Tex(r"Skirting board (edge): 28 m").scale(0.95).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m16))
        self.wait(2)
        m17 = Tex(r"Tiles (surface): 48 m$^2$").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m17))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Half a rectangle
        self.next_band(4)
        t4 = Tex(r"Half a rectangle").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m18 = MathTex(r"40 \times 30 = 1\,200 \text{ cm}^2").scale(1.0).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"\tfrac{1}{2} \times 1\,200 = 600 \text{ cm}^2").scale(1.0).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m19))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m19, color=GREEN)))
        self.wait(1.5)
        m20 = Tex(r"Two corner pieces make a second flag").scale(0.95).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m20))
        self.wait(2)
        m21 = Tex(r"Height: straight up, not along the slope").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m21))
        self.wait(2)
        self.wait(3)
