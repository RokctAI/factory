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
# dwell time proportional to subtopics.json (190/160/150/160/150 of
# 810 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CalculationTechniquesSession(MovingCameraScene):
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
        m1 = MathTex(r"247 \approx 250 \text{ (nearest 10)} \qquad 247 \approx 200 \text{ (nearest 100)}").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"38 \times 247 \approx 40 \times 250 = 10\,000").scale(1.0).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m2, color=GREEN)))
        self.wait(1.5)
        m3 = MathTex(r"9\,386 \div 13 \approx 9\,100 \div 13 = 700").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Estimates catch slipped digits").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(5)

        # --- Band 1 (subtopic_2): Column methods
        self.next_band(1)
        t1 = Tex(r"Column methods").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"247 \times 8 = 1\,976 \qquad 247 \times 30 = 7\,410").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"1\,976 + 7\,410 = 9\,386").scale(1.0).shift(band_shift(1) + UP * 0.18)
        self.play(Write(m6))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m6, color=GREEN)))
        self.wait(1.5)
        m7 = MathTex(r"9\,386 \div 13: \; 93 \to 7, \; 28 \to 2, \; 26 \to 2").scale(1.0).shift(band_shift(1) + DOWN * 0.85)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"9\,386 \div 13 = 722").scale(1.0).shift(band_shift(1) + DOWN * 1.87)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        m9 = Tex(r"Divide, multiply, subtract, bring down").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m9))
        self.wait(2)
        self.wait(4)

        # --- Band 2 (subtopic_3): Compensate and check
        self.next_band(2)
        t2 = Tex(r"Compensate and check").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m10 = MathTex(r"247 + 198 = 247 + 200 - 2 = 445").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"247 \times 40 - 247 \times 2 = 9\,880 - 494").scale(1.0).shift(band_shift(2) + UP * 0.18)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"= 9\,386").scale(1.0).shift(band_shift(2) + DOWN * 0.85)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        m13 = MathTex(r"\text{Check: } 722 \times 13 = 7\,220 + 2\,166 = 9\,386").scale(1.0).shift(band_shift(2) + DOWN * 1.87)
        self.play(Write(m13))
        self.wait(2)
        m14 = Tex(r"Calculator: only to CHECK your answer").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m14))
        self.wait(2)
        self.wait(4)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): The rough answer that saves you
        self.next_band(3)
        t3 = Tex(r"The rough answer that saves you").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m15 = MathTex(r"38 \times 247 \approx 40 \times 250 = 10\,000").scale(1.0).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Exact: R9 386 -- a bit under. Believable!").scale(0.95).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m16))
        self.wait(2)
        m17 = Tex(r"R93 860? Ten times too big!").scale(0.95).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m17))
        self.wait(2)
        m18 = Tex(r"Round: 5 or more goes up; 4 or less stays").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m18))
        self.wait(2)
        self.wait(4)

        # --- Band 4 (subtopic_5): Sharing books the long way
        self.next_band(4)
        t4 = Tex(r"Sharing books the long way").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m19 = MathTex(r"93 \text{ hundreds} \div 13 = 7 \text{ r } 2").scale(1.0).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"28 \text{ tens} \div 13 = 2 \text{ r } 2 \qquad 26 \div 13 = 2").scale(1.0).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m20))
        self.wait(2)
        m21 = MathTex(r"700 + 20 + 2 = 722 \text{ books each}").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m21))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m21, color=GREEN)))
        self.wait(1.5)
        m22 = MathTex(r"\text{Check: } 722 \times 13 = 9\,386").scale(1.0).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m22))
        self.wait(2)
        self.wait(4)
