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
# dwell time proportional to subtopics.json (150/120/120/120/120 of
# 630 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class AreaProblemsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Composite shapes
        t0 = Tex(r"Composite shapes").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"6{,}5 \times 2{,}4 = 15{,}6 \qquad 3 \times 2{,}6 = 7{,}8").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"15{,}6 + 7{,}8 = 23{,}4 \text{ m}^2").scale(1.0).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m2, color=GREEN)))
        self.wait(1.5)
        m3 = MathTex(r"\text{Check: } 32{,}5 - 9{,}1 = 23{,}4 \text{ m}^2").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = MathTex(r"\text{Gable house: } 24 + 10 = 34 \text{ m}^2").scale(1.0).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(4)

        # --- Band 1 (subtopic_2): Holes and coverings
        self.next_band(1)
        t1 = Tex(r"Holes and coverings").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"4{,}5 \times 2{,}7 = 12{,}15 \qquad 0{,}9 \times 2{,}1 = 1{,}89").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"12{,}15 - 1{,}89 = 10{,}26 \text{ m}^2").scale(1.0).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m6, color=GREEN)))
        self.wait(1.5)
        m7 = MathTex(r"2 \times 10{,}26 \div 8 \approx 2{,}6 \text{ l (buy more)}").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"23{,}4 \div 0{,}09 = 260 \text{ tiles} \qquad 23{,}4 \times 185 = R4\,329").scale(1.0).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Perimeter or area?
        self.next_band(2)
        t2 = Tex(r"Perimeter or area?").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = Tex(r"Fence, border, frame: perimeter. Paint, tile, carpet: area.").scale(0.95).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"\text{Lawn: } A = 100 \text{ m}^2, \; P = 41 \text{ m}").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m10, color=GREEN)))
        self.wait(1.5)
        m11 = MathTex(r"P = 20: \; 5 \times 5 = 25 \text{ m}^2, \; 9 \times 1 = 9 \text{ m}^2").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"A = 36: \; P = 24, 30, 74").scale(1.0).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Painting the wall
        self.next_band(3)
        t3 = Tex(r"Painting the wall").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"4{,}5 \times 2{,}7 = 12{,}15 \text{ m}^2").scale(1.0).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"\text{Door: } 0{,}9 \times 2{,}1 = 1{,}89 \text{ m}^2").scale(1.0).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"12{,}15 - 1{,}89 = 10{,}26 \text{ m}^2").scale(1.0).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m15, color=GREEN)))
        self.wait(1.5)
        m16 = Tex(r"Two coats: about 2,6 l. Buy 3 tins.").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): The L-shaped floor
        self.next_band(4)
        t4 = Tex(r"The L-shaped floor").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"6{,}5 \times 2{,}4 = 15{,}6 \qquad 3 \times 2{,}6 = 7{,}8").scale(1.0).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"23{,}4 \text{ m}^2 \text{ of carpet}").scale(1.0).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m18, color=GREEN)))
        self.wait(1.5)
        m19 = MathTex(r"\text{Check: } 32{,}5 - 9{,}1 = 23{,}4").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"Covers: area. Goes around: perimeter.").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m20))
        self.wait(2)
        self.wait(3)
