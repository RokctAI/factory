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
# dwell time proportional to subtopics.json (140/150/120/130/120 of
# 660 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class FractionWordProblemsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Fractions of whole numbers
        t0 = Tex(r"Fractions of whole numbers").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"\frac{3}{5} \text{ of } 360 = 360 \div 5 \times 3 = 216").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m1, color=GREEN)))
        self.wait(1.5)
        m2 = MathTex(r"\frac{1}{4} \text{ of } 216 = 54").scale(1.0).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"\frac{2}{5} \text{ of } 360 = 144 \qquad 216 + 144 = 360").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"If 72 is one fifth, the whole is $5 \times 72 = 360$").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(4)

        # --- Band 1 (subtopic_2): Grouping and sharing
        self.next_band(1)
        t1 = Tex(r"Grouping and sharing").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"20 \text{ l} \div 2\tfrac{1}{2} \text{ l} = 8 \text{ tables}").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m5, color=GREEN)))
        self.wait(1.5)
        m6 = MathTex(r"8 \times 2\tfrac{1}{2} = 20 \text{ (check)}").scale(1.0).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"3 \text{ pizzas} \div 4 = \tfrac{3}{4} \text{ each}").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"3\tfrac{3}{4} \times 400 \text{ m} = 1\,500 \text{ m}").scale(1.0).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(4)

        # --- Band 2 (subtopic_3): Percentages in context
        self.next_band(2)
        t2 = Tex(r"Percentages in context").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"40\% \text{ of } R1\,200 = R480 \quad 25\% = R300").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"\text{Decorations } 35\% = R420").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m10, color=GREEN)))
        self.wait(1.5)
        m11 = MathTex(r"\frac{288}{360} = \frac{4}{5} = 80\%").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"R15 + 20\% = R15 + R3 = R18").scale(1.0).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Planning the fun day
        self.next_band(3)
        t3 = Tex(r"Planning the fun day").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"360 \div 5 = 72 \qquad 3 \times 72 = 216 \text{ runners}").scale(1.0).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"20 \text{ l}: \; 8 \text{ tables of } 2\tfrac{1}{2} \text{ l}").scale(1.0).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m14, color=GREEN)))
        self.wait(1.5)
        m15 = MathTex(r"3 \text{ pizzas} = 12 \text{ quarters} \quad 12 \div 4 = 3 \text{ quarters each}").scale(1.0).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Which question am I answering?").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Spending the budget
        self.next_band(4)
        t4 = Tex(r"Spending the budget").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"10\% = R120 \quad 40\% = R480 \quad 25\% = R300").scale(1.0).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"R1\,200 - R480 - R300 = R420").scale(1.0).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m18, color=GREEN)))
        self.wait(1.5)
        m19 = MathTex(r"\frac{288}{360} = \frac{4}{5} = 80\%").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"R15 \to R18 \; (+20\%)").scale(1.0).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m20))
        self.wait(2)
        self.wait(3)
