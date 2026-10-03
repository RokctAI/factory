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
# dwell time proportional to subtopics.json (170/130/120/120/120 of
# 660 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class MultiplyDecimalsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Decimals times whole numbers
        t0 = Tex(r"Decimals times whole numbers").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"1{,}375 \times 10 = 13{,}75 \quad \times 100 = 137{,}5 \quad \times 1\,000 = 1\,375").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"1\,375 \times 6 = 8\,250").scale(1.0).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"1{,}375 \times 6 = 8{,}250 = 8{,}25 \text{ kg}").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m3, color=GREEN)))
        self.wait(1.5)
        m4 = Tex(r"Estimate: a bit less than $6 \times 1{,}5 = 9$").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(4)

        # --- Band 1 (subtopic_2): Decimal times decimal
        self.next_band(1)
        t1 = Tex(r"Decimal times decimal").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"1\,245 \times 25 = 31\,125").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex(r"2 decimal places + 1 decimal place = 3").scale(0.95).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"12{,}45 \times 2{,}5 = 31{,}125 \approx R31{,}13").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m7, color=GREEN)))
        self.wait(1.5)
        m8 = MathTex(r"\text{hundredths} \times \text{tenths} = \text{thousandths}").scale(1.0).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Placing the comma
        self.next_band(2)
        t2 = Tex(r"Placing the comma").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"38 \times 47 = 1\,786").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"3{,}8 \times 4{,}7 = 17{,}86 \quad (\approx 4 \times 5 = 20)").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m10, color=GREEN)))
        self.wait(1.5)
        m11 = MathTex(r"2{,}5 \times 1{,}4 = 3{,}50 = 3{,}5").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Count places on the FULL product").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Six boxes of tomatoes
        self.next_band(3)
        t3 = Tex(r"Six boxes of tomatoes").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"1\,375 \times 6 = 8\,250").scale(1.0).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"1{,}375 \times 6 = 8{,}25 \text{ kg}").scale(1.0).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m14, color=GREEN)))
        self.wait(1.5)
        m15 = Tex(r"Check: about $6 \times 1{,}5 = 9$").scale(0.95).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = MathTex(r"10 \text{ boxes} = 13{,}75 \text{ kg} \quad 100 \text{ boxes} = 137{,}5 \text{ kg}").scale(1.0).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Paying by weight
        self.next_band(4)
        t4 = Tex(r"Paying by weight").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = Tex(r"Rough: R12 a kg $\times$ 2,5 kg $\approx$ R30").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"1\,245 \times 25 = 31\,125").scale(1.0).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"12{,}45 \times 2{,}5 = 31{,}125 \approx R31{,}13").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m19, color=GREEN)))
        self.wait(1.5)
        m20 = Tex(r"Times less than 1: the answer gets smaller").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m20))
        self.wait(2)
        self.wait(3)
