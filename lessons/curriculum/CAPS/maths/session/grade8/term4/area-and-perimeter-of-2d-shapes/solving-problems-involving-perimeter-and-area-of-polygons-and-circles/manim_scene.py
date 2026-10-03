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
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (320/210/230/230/250/230/210 of
# 1680 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PerimeterAreaProblemsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Path Around the Garden
        t0 = Tex(r"The Path Around the Garden").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"(12 + 2) \times (8 + 2) = 14 \times 10 = 140").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"140 - 12 \times 8 = 140 - 96 = 44 \text{ m}^2").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"44 \times 165 = 7\,260 \text{ rand}").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Read, sketch, identify, decide, calculate, answer in context").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): The Running Track
        self.next_band(1)
        t1 = Tex(r"The Running Track").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"2 \times 80 + 2\pi \times 30 \approx 160 + 188{,}50 = 348{,}50 \text{ m}").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"80 \times 60 + \pi \times 30^2 \approx 4\,800 + 2\,827{,}43 = 7\,627{,}43 \text{ m}^2").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Two semicircles make one circle").scale(1.05).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Perimeter: outside edges only. Area: every inside region.").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Shaded Regions
        self.next_band(2)
        t2 = Tex(r"Shaded Regions").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"10^2 - \pi \times 5^2 = 100 - 25\pi \approx 21{,}46").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"\pi \times 7^2 - \pi \times 4^2 = 33\pi \approx 103{,}67").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"8^2 - \tfrac{1}{4} \times \pi \times 8^2 = 64 - 16\pi \approx 13{,}73").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Outer area minus inner area; never subtract the radii first").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Without a Calculator
        self.next_band(3)
        t3 = Tex(r"Without a Calculator").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"\tfrac{22}{7} \times 7^2 = 154 \qquad 3{,}14 \times 25 = 75 + 3{,}5 = 78{,}5").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"4{,}2 \times 3{,}6 = 15{,}12 \qquad 15{,}12 \div 0{,}09 = 168").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"168 \times 1{,}1 = 184{,}8 \to 185 \text{ tiles} \to 16 \text{ boxes}").scale(1.1).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Whole items from a shop: always round up").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m16))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m16, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): The Rondavel
        self.next_band(4)
        t4 = Tex(r"The Rondavel").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"\pi \times 3^2 \approx 28{,}27 \text{ m}^2 \qquad \pi \times 6 \approx 18{,}85 \text{ m}").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"18{,}85 \times 2{,}4 \approx 45{,}24 \qquad 45{,}24 - 2{,}97 = 42{,}27 \text{ m}^2").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"42{,}27 \times 12{,}5 \approx 528{,}4 \to 529 \text{ blocks}").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"For a given area, the circle has the shortest boundary").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): Kitchen and Path
        self.next_band(5)
        t5 = Tex(r"Kitchen and Path").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m21 = MathTex(r"4{,}2 \div 0{,}3 = 14, \quad 3{,}6 \div 0{,}3 = 12, \quad 14 \times 12 = 168").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m21))
        self.wait(2)
        m22 = MathTex(r"2 \times (4{,}2 + 3{,}6) - 0{,}9 = 14{,}7 \qquad 14{,}7 \div 2{,}4 \approx 6{,}125 \to 7").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"40 \times 1 + 4 = 44 = 140 - 96").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m23))
        self.wait(2)
        m24 = Tex(r"Corners are where quick estimates go wrong").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m24))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m24, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): Examination Technique
        self.next_band(6)
        t6 = Tex(r"Examination Technique").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m25 = Tex(r"Sketch, shapes, perimeter or area, parts, combine, context, sentence").scale(1.05).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m25))
        self.wait(2)
        m26 = MathTex(r"2 \times 20 + 2 \times \tfrac{22}{7} \times 7 = 40 + 44 = 84").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"95 \div 8 = 11{,}875 \text{ litres} \to 3 \text{ tins}").scale(1.1).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m27))
        self.wait(2)
        m28 = MathTex(r"\pi \times 10^2 - \pi \times 6^2 = 64\pi").scale(1.1).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m28))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m28, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
