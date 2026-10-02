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
# dwell time proportional to subtopics.json (250/210/210/180/240/210/200 of
# 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ExponentRootOperationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Roots Undo Powers
        t0 = Tex(r"Roots Undo Powers").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"8^2 = 64 \;\Leftrightarrow\; \sqrt{64} = 8 \qquad 3^3 = 27 \;\Leftrightarrow\; \sqrt[3]{27} = 3").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"\sqrt[3]{-8} = -2 \qquad \sqrt{-16} \text{ has no answer}").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex(r"Squares: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144").scale(1.05).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Cubes: 1, 8, 27, 64, 125, 216, 343, 512, 729, 1 000").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): Root of a Product, Root of a Sum
        self.next_band(1)
        t1 = Tex(r"Root of a Product, Root of a Sum").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"\sqrt{4 \times 9} = \sqrt{4} \times \sqrt{9} = 6").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"\sqrt{9 + 16} = \sqrt{25} = 5 \neq 7 = \sqrt{9} + \sqrt{16}").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"\sqrt{1\,600} = \sqrt{16} \times \sqrt{100} = 40").scale(1.1).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Under a root sign, everything is in brackets.").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Roots of Powers
        self.next_band(2)
        t2 = Tex(r"Roots of Powers").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"\sqrt{2^6} = 2^3 \qquad \sqrt[3]{2^6} = 2^2").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"\sqrt{a^{2n}} = a^n \qquad \sqrt[3]{a^{3n}} = a^n").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"\sqrt{9x^4} = 3x^2 \qquad \sqrt[3]{27a^6} = 3a^2").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Square root: halve the exponent. Cube root: third it.").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Order of Operations
        self.next_band(3)
        t3 = Tex(r"Order of Operations").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"\sqrt{64} + \sqrt[3]{27} = 8 + 3 = 11").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"2^3 + \sqrt{100} \times 3 = 8 + 30 = 38").scale(1.1).shift(band_shift(3) + UP * 0.18)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"\sqrt{9 + 16} - 2^2 = 5 - 4 = 1").scale(1.1).shift(band_shift(3) + DOWN * 0.85)
        self.play(Write(m15))
        self.wait(2)
        m16 = MathTex(r"\frac{\sqrt[3]{125} - \sqrt{16}}{2^2} = \frac{1}{4}").scale(1.1).shift(band_shift(3) + DOWN * 1.87)
        self.play(Write(m16))
        self.wait(2)
        m17 = Tex(r"Brackets, then powers and roots, then x and /, then + and -").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m17))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m17, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): Tiling the Floor
        self.next_band(4)
        t4 = Tex(r"Tiling the Floor").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m18 = MathTex(r"64 \text{ tiles} \Rightarrow \sqrt{64} = 8 \text{ along each wall}").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"\sqrt{1\,600} = \sqrt{16} \times \sqrt{100} = 40").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"9 tiles + 16 tiles = 25 tiles: side 5, not 3 + 4").scale(1.05).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m20))
        self.wait(2)
        m21 = MathTex(r"27 \text{ cubes} \Rightarrow \sqrt[3]{27} = 3 \text{ along each edge}").scale(1.1).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m21))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m21, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): The Cashier Who Added First
        self.next_band(5)
        t5 = Tex(r"The Cashier Who Added First").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m22 = MathTex(r"\sqrt{64} + \sqrt[3]{27} = 8 + 3 = 11 \quad \text{not } \sqrt{91}").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"\sqrt{9 + 16} = 5 \quad \text{not } 3 + 4").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m23))
        self.wait(2)
        m24 = MathTex(r"2^3 + \sqrt{100} \times 3 = 8 + 30 = 38 \quad \text{not } 54").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m24))
        self.wait(2)
        m25 = Tex(r"Replace every power and root by its value, then do the arithmetic").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m25))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m25, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): Examination Technique
        self.next_band(6)
        t6 = Tex(r"Examination Technique").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m26 = MathTex(r"\sqrt{81} - \sqrt[3]{64} + 2^4 = 9 - 4 + 16 = 21").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"\sqrt{25x^6} = 5x^3 \qquad \sqrt{3^2 + 4^2} = \sqrt{25} = 5").scale(1.1).shift(band_shift(6) + UP * 0.18)
        self.play(Write(m27))
        self.wait(2)
        m28 = MathTex(r"\sqrt{16} \times \sqrt{9} = 12 \qquad \sqrt{16 + 9} = 5").scale(1.1).shift(band_shift(6) + DOWN * 0.85)
        self.play(Write(m28))
        self.wait(2)
        m29 = MathTex(r"\sqrt[3]{2^9} = 2^3 = 8").scale(1.1).shift(band_shift(6) + DOWN * 1.87)
        self.play(Write(m29))
        self.wait(2)
        m30 = Tex(r"Products split under a root; sums do not.").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m30))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m30, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
