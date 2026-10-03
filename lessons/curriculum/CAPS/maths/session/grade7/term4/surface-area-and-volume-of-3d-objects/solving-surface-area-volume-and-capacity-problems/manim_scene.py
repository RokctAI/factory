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
# dwell time proportional to subtopics.json (130/120/120/120/120 of
# 610 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class VolumeProblemsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Volume and capacity
        t0 = Tex(r"Volume and capacity").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"2{,}5 \times 1{,}2 \times 1{,}5 = 4{,}5 \text{ m}^3 = 4\,500 \text{ l}").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m1, color=GREEN)))
        self.wait(1.5)
        m2 = MathTex(r"4\,500 \div 20 = 225 \text{ min} = 3 \text{ h } 45 \text{ min}").scale(1.0).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"\text{Depth: } 3{,}3 \div 3 = 1{,}1 \text{ m}").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = MathTex(r"4\,500 \div 600 = 7{,}5 \text{ days}").scale(1.0).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(3)

        # --- Band 1 (subtopic_2): Surface area problems
        self.next_band(1)
        t1 = Tex(r"Surface area problems").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"\text{4 sides: } 2(2{,}5 \times 1{,}5) + 2(1{,}2 \times 1{,}5) = 11{,}1 \text{ m}^2").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"\text{+ top: } 11{,}1 + 3 = 14{,}1 \text{ m}^2").scale(1.0).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m6, color=GREEN)))
        self.wait(1.5)
        m7 = MathTex(r"2 \times 14{,}1 \div 10 = 2{,}82 \text{ l} \to 3 \text{ l}").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"\text{Open box } 10 \times 8 \times 6: \; 80 + 120 + 96 = 296 \text{ cm}^2").scale(1.0).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Multi-step problems
        self.next_band(2)
        t2 = Tex(r"Multi-step problems").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"10 \times 6 \times 20 = 1\,200 \text{ cm}^3 = 1{,}2 \text{ l}").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"1\,200 \div 250 = 4{,}8 \to 4 \text{ full glasses}").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"\text{Crate: } 6 \times 5 \times 2 = 60 \text{ cartons}").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m11, color=GREEN)))
        self.wait(1.5)
        m12 = MathTex(r"25 \times 10 \times 1{,}6 = 400 \text{ m}^3 = 400 \text{ kl}").scale(1.0).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Filling the tank
        self.next_band(3)
        t3 = Tex(r"Filling the tank").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"2{,}5 \times 1{,}2 \times 1{,}5 = 4{,}5 \text{ m}^3").scale(1.0).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"4\,500 \text{ l}").scale(1.0).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m14, color=GREEN)))
        self.wait(1.5)
        m15 = MathTex(r"4\,500 \div 20 = 225 \text{ min}").scale(1.0).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = MathTex(r"3\,300 \text{ l} \div 3 \text{ m}^2 \to 1{,}1 \text{ m deep}").scale(1.0).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Painting and packing
        self.next_band(4)
        t4 = Tex(r"Painting and packing").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = Tex(r"Bottom on the slab: not painted").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"7{,}5 + 3{,}6 + 3 = 14{,}1 \text{ m}^2").scale(1.0).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"2 \text{ coats} \to 2{,}82 \text{ l} \to \text{buy } 3 \text{ l}").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m19, color=GREEN)))
        self.wait(1.5)
        m20 = MathTex(r"\text{Crate: } 6 \times 5 \times 2 = 60 \text{ cartons}").scale(1.0).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m20))
        self.wait(2)
        self.wait(3)
