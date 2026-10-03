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
# dwell time proportional to subtopics.json (140/120/120/120/120 of
# 620 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class EstimatingDecimalsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Estimate first
        t0 = Tex(r"Estimate first").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"42{,}6 \times 23{,}85 \approx 40 \times 25 = 1\,000").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"23{,}85 + 18{,}40 + 7{,}95 \approx 24 + 18 + 8 = 50").scale(1.0).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"98{,}4 \div 3{,}9 \approx 100 \div 4 = 25").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m3, color=GREEN)))
        self.wait(1.5)
        m4 = Tex(r"An estimate is a calculation, not a guess").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(4)

        # --- Band 1 (subtopic_2): Predict the decimal places
        self.next_band(1)
        t1 = Tex(r"Predict the decimal places").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = Tex(r"Multiply: add the places. 1 + 2 = 3").scale(0.95).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"426 \times 2\,385 = 1\,016\,010").scale(1.0).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"42{,}6 \times 23{,}85 = 1\,016{,}010 = R1\,016{,}01").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m7, color=GREEN)))
        self.wait(1.5)
        m8 = Tex(r"Places say how many digits; estimate says how big").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Check your answer
        self.next_band(2)
        t2 = Tex(r"Check your answer").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"R1\,016{,}01 + R83{,}99 = R1\,100{,}00").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"1\,016{,}01 \div 42{,}6 \approx 23{,}85").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"R10\,160{,}10 \text{ for } 42{,}6 \text{ l? Impossible}").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m11, color=GREEN)))
        self.wait(1.5)
        m12 = Tex(r"Calculator: confirms, never replaces").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): About how much?
        self.next_band(3)
        t3 = Tex(r"About how much?").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"42{,}6 \to 40 \qquad 23{,}85 \to 25").scale(1.0).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"40 \times 25 = 1\,000").scale(1.0).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m14, color=GREEN)))
        self.wait(1.5)
        m15 = Tex(r"Pump shows R1 016,01: matches!").scale(0.95).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"R10 160,10 or R101,60? Something is wrong.").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Three ways to check
        self.next_band(4)
        t4 = Tex(r"Three ways to check").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"1\,016{,}01 + 83{,}99 = 1\,100").scale(1.0).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m17))
        self.wait(2)
        m18 = Tex(r"Makes sense? A bit less than R100 change").scale(0.95).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"\text{Calculator agrees: } 83{,}99").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m19, color=GREEN)))
        self.wait(1.5)
        m20 = Tex(r"Your working first, calculator second").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m20))
        self.wait(2)
        self.wait(3)
