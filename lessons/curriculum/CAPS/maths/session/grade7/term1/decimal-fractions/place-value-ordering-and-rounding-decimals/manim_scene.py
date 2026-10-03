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
# dwell time proportional to subtopics.json (150/130/140/120/120 of
# 660 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class DecimalPlaceValueSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Place value: 3,457
        t0 = Tex(r"Place value: 3,457").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"3{,}457 = 3 + \frac{4}{10} + \frac{5}{100} + \frac{7}{1000}").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"units, tenths, hundredths, thousandths").scale(0.95).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"3{,}7; \; 3{,}8; \; 3{,}9; \; 4{,}0; \; 4{,}1").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = MathTex(r"3{,}47; \; 3{,}48; \; 3{,}49; \; 3{,}50; \; 3{,}51").scale(1.0).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(4)

        # --- Band 1 (subtopic_2): Ordering decimals
        self.next_band(1)
        t1 = Tex(r"Ordering decimals").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"3{,}457 \qquad 3{,}500 \qquad 3{,}450").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex(r"Line up the commas, fill with zeros, compare from the left").scale(0.95).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"3{,}5 > 3{,}457 > 3{,}45").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m7, color=GREEN)))
        self.wait(1.5)
        m8 = Tex(r"More digits does NOT mean bigger").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Rounding decimals
        self.next_band(2)
        t2 = Tex(r"Rounding decimals").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"3{,}457 \approx 3{,}46 \text{ (2 d.p.)} \approx 3{,}5 \text{ (1 d.p.)}").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m9, color=GREEN)))
        self.wait(1.5)
        m10 = MathTex(r"2{,}996 \approx 3{,}00 \text{ (2 d.p.)}").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"R14{,}567 \approx R14{,}57").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Round from the original number, never in a chain").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(4)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Who jumped furthest?
        self.next_band(3)
        t3 = Tex(r"Who jumped furthest?").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"3{,}457 \to 3{,}457 \quad 3{,}5 \to 3{,}500 \quad 3{,}45 \to 3{,}450").scale(1.0).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = Tex(r"Compare tenths first: 4, 5, 4").scale(0.95).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"\text{Bongani wins: } 3{,}5 \text{ m}").scale(1.0).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m15, color=GREEN)))
        self.wait(1.5)
        m16 = Tex(r"Amahle beats Cara by 7 mm").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Rounding like a scoreboard
        self.next_band(4)
        t4 = Tex(r"Rounding like a scoreboard").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = Tex(r"Find the place. Peek at the next digit.").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"3{,}4\underline{5}7 \to 3{,}46").scale(1.0).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"3{,}\underline{4}57 \to 3{,}5").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"2{,}996 \to 3{,}00").scale(1.0).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
