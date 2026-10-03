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


class DecimalProblemsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Money problems
        t0 = Tex(r"Money problems").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"R4\,845{,}60 \div 38 \approx 4\,800 \div 40 = 120").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"R4\,845{,}60 \div 38 = R127{,}515\ldots \approx R127{,}52").scale(1.0).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m2, color=GREEN)))
        self.wait(1.5)
        m3 = Tex(r"Collecting money: round UP so the total is covered").scale(0.95).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = MathTex(r"127{,}52 + 35{,}50 + 12{,}75 = R175{,}77").scale(1.0).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(4)

        # --- Band 1 (subtopic_2): Measurement problems
        self.next_band(1)
        t1 = Tex(r"Measurement problems").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"1 \text{ km} = 1\,000 \text{ m} \quad 1 \text{ l} = 1\,000 \text{ ml} \quad 1 \text{ kg} = 1\,000 \text{ g}").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"184{,}5 \times 2 + 12{,}75 = 381{,}75 \text{ km}").scale(1.0).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"38 \times 0{,}75 \text{ l} = 28{,}5 \text{ l} \to 6 \text{ containers}").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m7, color=GREEN)))
        self.wait(1.5)
        m8 = MathTex(r"0{,}125 \text{ kg} = 125 \text{ g}").scale(1.0).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Rates and operations
        self.next_band(2)
        t2 = Tex(r"Rates and operations").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"381{,}75 \text{ km} \times 0{,}32 \text{ l/km} = 122{,}16 \text{ l}").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"122{,}16 \text{ l} \times R23{,}85 \approx R2\,913{,}52").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"\text{A: } R4\,771{,}88 \quad \text{B: } R4\,712{,}10").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m11, color=GREEN)))
        self.wait(1.5)
        m12 = Tex(r"Let the units choose the operation").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Paying for the bus
        self.next_band(3)
        t3 = Tex(r"Paying for the bus").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"\approx 4\,800 \div 40 = 120").scale(1.0).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"4\,845{,}60 \div 38 = 127{,}515\ldots").scale(1.0).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"\text{Round UP: } R127{,}52").scale(1.0).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m15, color=GREEN)))
        self.wait(1.5)
        m16 = Tex(r"Cover a cost: round up. Share out: round down.").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Water bottles and kilometres
        self.next_band(4)
        t4 = Tex(r"Water bottles and kilometres").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"750 \text{ ml} = 0{,}75 \text{ l}").scale(1.0).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"38 \times 0{,}75 = 28{,}5 \text{ l} \to 6 \text{ containers}").scale(1.0).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m18, color=GREEN)))
        self.wait(1.5)
        m19 = MathTex(r"184{,}5 + 184{,}5 + 12{,}75 = 381{,}75 \text{ km}").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"Units? Operation? Makes sense?").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m20))
        self.wait(2)
        self.wait(3)
