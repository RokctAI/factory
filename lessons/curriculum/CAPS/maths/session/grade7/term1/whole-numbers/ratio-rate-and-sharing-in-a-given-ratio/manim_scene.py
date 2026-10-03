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
# dwell time proportional to subtopics.json (180/160/140/120/120 of
# 720 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class RatioRateSharingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Ratio: same kind, same units
        t0 = Tex(r"Ratio: same kind, same units").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"\text{Lerato : Sipho} = 4 : 5").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"40 \text{ min} : 2 \text{ h} = 40 : 120").scale(1.0).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"40 : 120 = 1 : 3 \qquad 12 : 18 = 2 : 3").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m3, color=GREEN)))
        self.wait(1.5)
        m4 = Tex(r"Simplify by dividing every part by the HCF").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(4)

        # --- Band 1 (subtopic_2): Sharing R360 in the ratio 4 : 5
        self.next_band(1)
        t1 = Tex(r"Sharing R360 in the ratio 4 : 5").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"4 + 5 = 9 \text{ parts} \qquad R360 \div 9 = R40").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"\text{Lerato } 4 \times 40 = R160 \qquad \text{Sipho } 5 \times 40 = R200").scale(1.0).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m6, color=GREEN)))
        self.wait(1.5)
        m7 = MathTex(r"\text{Check: } 160 + 200 = 360 \qquad 160 : 200 = 4 : 5").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"R7\,200 \text{ in } 2:3:5 \to R1\,440, \; R2\,160, \; R3\,600").scale(1.0).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(4)

        # --- Band 2 (subtopic_3): Rate: different kinds, has units
        self.next_band(2)
        t2 = Tex(r"Rate: different kinds, has units").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"R360 \div 12 \text{ cars} = R30 \text{ per car}").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"240 \text{ km} \div 3 \text{ h} = 80 \text{ km/h}").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"R38 \div 2 = R19/\text{kg} \qquad R85 \div 5 = R17/\text{kg}").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m11, color=GREEN)))
        self.wait(1.5)
        m12 = MathTex(r"400 \text{ km} \div 80 \text{ km/h} = 5 \text{ h}").scale(1.0).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(4)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): A fair split at the car wash
        self.next_band(3)
        t3 = Tex(r"A fair split at the car wash").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = Tex(r"Lerato 4 slices, Sipho 5 slices: 9 slices").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"R360 \div 9 = R40 \text{ per slice}").scale(1.0).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"R160 \text{ and } R200").scale(1.0).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m15, color=GREEN)))
        self.wait(1.5)
        m16 = Tex(r"Check: adds to R360, still 4 : 5").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Per one
        self.next_band(4)
        t4 = Tex(r"Per one").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"12 \text{ cars} \to R360 \qquad 1 \text{ car} \to R30").scale(1.0).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"3 \text{ h} \to 240 \text{ km} \qquad 1 \text{ h} \to 80 \text{ km}").scale(1.0).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"\text{Small: } R19/\text{kg} \quad \text{Big: } R17/\text{kg}").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m19, color=GREEN)))
        self.wait(1.5)
        m20 = Tex(r"Compare prices per ONE kilogram").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m20))
        self.wait(2)
        self.wait(3)
