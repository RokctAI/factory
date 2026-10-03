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
# dwell time proportional to subtopics.json (200/160/150/150/150 of
# 810 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class OrderingPropertiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Place value: 1 384 000
        t0 = Tex(r"Place value: 1 384 000").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"1\,384\,000 = 1\,000\,000 + 300\,000 + 80\,000 + 4\,000").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Same number of digits? Compare from the LEFT").scale(0.95).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"1\,108\,000 < 1\,241\,000 < 1\,384\,000").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m3, color=GREEN)))
        self.wait(1.5)
        m4 = Tex(r"More digits = bigger: $999\,999 < 1\,000\,000$").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(5)

        # --- Band 1 (subtopic_2): Properties of operations
        self.next_band(1)
        t1 = Tex(r"Properties of operations").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"6 \times 7 = 7 \times 6 \quad \text{(commutative)}").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"(25 + 75) + 37 = 137 \quad \text{(associative)}").scale(1.0).shift(band_shift(1) + UP * 0.18)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"7 \times 103 = 7 \times 100 + 7 \times 3 = 721").scale(1.0).shift(band_shift(1) + DOWN * 0.85)
        self.play(Write(m7))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m7, color=GREEN)))
        self.wait(1.5)
        m8 = MathTex(r"10 - 4 \neq 4 - 10 \qquad 24 \div 6 \neq 6 \div 24").scale(1.0).shift(band_shift(1) + DOWN * 1.87)
        self.play(Write(m8))
        self.wait(2)
        m9 = Tex(r"Subtraction and division: work left to right").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m9))
        self.wait(2)
        self.wait(4)

        # --- Band 2 (subtopic_3): Zero, one and BODMAS
        self.next_band(2)
        t2 = Tex(r"Zero, one and BODMAS").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m10 = MathTex(r"a + 0 = a \qquad a \times 1 = a \qquad a \times 0 = 0").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"Division by zero is undefined").scale(0.95).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"18 + 6 \times 4 = 18 + 24 = 42").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        m13 = MathTex(r"(1\,384\,000 - 1\,108\,000) \div 1\,000 = 276").scale(1.0).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m13))
        self.wait(2)
        self.wait(4)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Which town is bigger?
        self.next_band(3)
        t3 = Tex(r"Which town is bigger?").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m14 = Tex(r"Step 1: count the digits").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"Step 2: compare from the left, stop at the first difference").scale(0.95).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"1 \textbf{3}84 000 $>$ 1 \textbf{2}41 000 $>$ 1 \textbf{1}08 000").scale(0.95).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m16))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m16, color=GREEN)))
        self.wait(1.5)
        m17 = Tex(r"Trap: 999 999 has fewer digits than 1 000 000").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m17))
        self.wait(2)
        self.wait(4)

        # --- Band 4 (subtopic_5): Shortcuts that are allowed
        self.next_band(4)
        t4 = Tex(r"Shortcuts that are allowed").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m18 = MathTex(r"25 + 37 + 75 = (25 + 75) + 37 = 137").scale(1.0).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"7 \times 103 = 700 + 21 = 721").scale(1.0).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"Swap and regroup: only for $+$ and $\times$").scale(0.95).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m20))
        self.wait(2)
        m21 = MathTex(r"18 + 6 \times 4 = 42").scale(1.0).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m21))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m21, color=GREEN)))
        self.wait(1.5)
        self.wait(4)
