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
# dwell time proportional to subtopics.json (240/200/180/180/220/220/210 of
# 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MultiplyingDecimalsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Multiplying Decimals
        t0 = Tex(r"Multiplying Decimals").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"0{,}6 \times 0{,}4 = \frac{6}{10} \times \frac{4}{10} = \frac{24}{100} = 0{,}24").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Decimal places add because the denominators multiply").scale(1.05).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"0{,}05 \times 0{,}3 = \frac{5}{100} \times \frac{3}{10} = \frac{15}{1000} = 0{,}015").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Multiplying by less than one shrinks").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): The Anchor Laid Out
        self.next_band(1)
        t1 = Tex(r"The Anchor Laid Out").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = Tex(r"Estimate: about 2,4 times about 1, a little more than 2,4").scale(1.05).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"235 \times 12 = 2\,820").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"2{,}35 \times 1{,}2 = 2{,}820 = 2{,}82 \quad \text{(3 places)}").scale(1.1).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"3{,}2 \times 0{,}25 = 0{,}8 \qquad 12{,}5 \times 0{,}04 = 0{,}5").scale(1.1).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Powers of Ten and Tenths
        self.next_band(2)
        t2 = Tex(r"Powers of Ten and Tenths").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"3{,}47 \times 10 = 34{,}7 \qquad 3{,}47 \times 100 = 347").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"3{,}47 \times 0{,}1 = 0{,}347 \qquad 3{,}47 \times 0{,}01 = 0{,}0347").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"2{,}5 \times 0{,}4 = 1 \qquad 1{,}25 \times 16 = 16 + 4 = 20").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Times a tenth is divide by ten").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Estimation and Technique
        self.next_band(3)
        t3 = Tex(r"Estimation and Technique").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = Tex(r"Estimate, multiply digits, count places, keep zeros, compare").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"3{,}2 \times 0{,}25: \quad 32 \times 25 = 800 \to 0{,}800 = 0{,}8").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"0{,}3^2 = 0{,}09 \qquad 1{,}5^2 = 2{,}25").scale(1.1).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Two methods for the comma must agree").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m16))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m16, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): The Butcher's Scale
        self.next_band(4)
        t4 = Tex(r"The Butcher's Scale").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = Tex(r"Estimate: about R25 a kilo, about 3,5 kilos, about R87").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"246 \times 35 = 8\,610 \qquad 24{,}6 \times 3{,}5 = 86{,}10").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = Tex(r"Tenths of a rand times tenths of a kilo gives cents").scale(1.05).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"0{,}05 \times 0{,}3 = 0{,}015").scale(1.1).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): Pump and Fabric
        self.next_band(5)
        t5 = Tex(r"Pump and Fabric").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m21 = MathTex(r"238 \times 425 = 101\,150 \qquad 23{,}8 \times 42{,}5 = 1\,011{,}50").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m21))
        self.wait(2)
        m22 = MathTex(r"2{,}35 \times 1{,}2 = 2{,}82").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"3{,}2 \times 0{,}25 = 0{,}800 = 0{,}80").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m23))
        self.wait(2)
        m24 = Tex(r"A familiar fraction beats the digit method").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m24))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m24, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): Where Does the Comma Go?
        self.next_band(6)
        t6 = Tex(r"Where Does the Comma Go?").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m25 = Tex(r"Counting says where; estimating says whether").scale(1.05).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m25))
        self.wait(2)
        m26 = MathTex(r"0{,}6 \times 0{,}4 = 0{,}24 \quad \text{(about a quarter)}").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"12{,}5 \times 0{,}04 = 0{,}500 = 0{,}5 \quad \text{(a bit under half)}").scale(1.1).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m27))
        self.wait(2)
        m28 = Tex(r"Estimate, digits, places, zeros, compare").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m28))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m28, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
