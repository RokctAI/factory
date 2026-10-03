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
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ExponentLawsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): multiply and divide powers
        title = Tex("Laws of Exponents").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"a^m \times a^n = a^{m+n} \qquad 2^3 \times 2^4 = 2^7 = 128").scale(1.0).shift(UP * 1.3)
        l2 = MathTex(r"a^m \div a^n = a^{m-n} \qquad 3^5 \div 3^2 = 3^3 = 27").scale(1.0).shift(UP * 0.3)
        l3 = MathTex(r"2^3 \times 3^2 = 8 \times 9 = 72 \;\text{(unlike bases: no law)}").scale(0.95).shift(DOWN * 0.7)
        l4 = MathTex(r"3x^2 \times 4x^5 = 12x^7").scale(1.0).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): power of a power, power of a product
        self.next_band(1)
        b1_title = Tex("Power of a power; power of a product").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"(a^m)^n = a^{mn} \qquad (2^3)^2 = 2^6 = 64").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"(a \times t)^n = a^n t^n \qquad (2 \times 5)^3 = 8 \times 125 = 1\,000").scale(0.95).shift(band_shift(1) + UP * 0.3)
        b1_l3 = MathTex(r"(3x)^2 = 9x^2 \qquad (2a^2 b)^3 = 8a^6 b^3").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = MathTex(r"(3 + 4)^2 = 49 \neq 3^2 + 4^2 = 25").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): zero exponent
        self.next_band(2)
        b2_title = Tex(r"The zero exponent: $a^0 = 1$, $a \neq 0$").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\frac{5^4}{5^4} = 1 \quad\text{and}\quad \frac{5^4}{5^4} = 5^{4-4} = 5^0").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"2^3 = 8,\; 2^2 = 4,\; 2^1 = 2,\; 2^0 = 1").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"3 \times 5^0 = 3 \qquad (3 \times 5)^0 = 1").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"(-3)^0 = 1 \qquad 7^4 \div 7^4 = 1").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): mixed expressions
        self.next_band(3)
        b3_title = Tex("Laws together").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"2^5 \times 2^3 \div 2^6 = 2^8 \div 2^6 = 2^2 = 4").scale(1.05).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"6x^5 \div 2x^2 = 3x^3").scale(1.0).shift(band_shift(3) + UP * 0.3)
        b3_l3 = MathTex(r"(2a^2 b)^3 \div 4a^4 = 8a^6 b^3 \div 4a^4 = 2a^2 b^3").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = MathTex(r"2^3 \times 3^2 \times 2^2 \times 3 = 2^5 \times 3^3 = 864").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"2^3 \times 2^4 = 4^7").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"2^3 \times 2^4 = 2^{12}").scale(1.0).shift(band_shift(4) + UP * 0.4)
        b4_l3 = MathTex(r"(3x)^2 = 3x^2").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = MathTex(r"(a+b)^2 = a^2 + b^2 \qquad a^0 = 0").scale(1.0).shift(band_shift(4) + DOWN * 1.4)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): counting the twos
        self.next_band(5)
        b5_title = Tex("Counting the twos").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"[2 \cdot 2 \cdot 2] \times [2 \cdot 2 \cdot 2 \cdot 2] = 2^7").scale(1.0).shift(band_shift(5) + UP * 1.3)
        b5_l2 = MathTex(r"\frac{3 \cdot 3 \cdot 3 \cdot 3 \cdot 3}{3 \cdot 3} = 3^3").scale(1.0).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex("Unlike bases cannot be counted together: $8 \\times 9 = 72$").scale(0.95).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = MathTex(r"2^3 + 2^4 = 8 + 16 = 24 \;\text{(no law for adding)}").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): boxes of boxes, sharing
        self.next_band(6)
        b6_title = Tex("Boxes of boxes; sharing the exponent").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"(2^3)^2 = [2 \cdot 2 \cdot 2][2 \cdot 2 \cdot 2] = 2^6").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = MathTex(r"(2 \times 5)^3 = 2 \cdot 5 \cdot 2 \cdot 5 \cdot 2 \cdot 5 = 2^3 \times 5^3").scale(0.95).shift(band_shift(6) + UP * 0.3)
        b6_l3 = MathTex(r"(3x)^2 = 3 \cdot x \cdot 3 \cdot x = 9x^2").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex("Side by side: add. Wrapped in a bracket: multiply.").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): zero exponent and summary
        self.next_band(7)
        b7_title = Tex("Why anything to the zero is one").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"16 \to 8 \to 4 \to 2 \to 1 \quad\text{so}\quad 2^0 = 1").scale(1.0).shift(band_shift(7) + UP * 1.3)
        b7_l2 = MathTex(r"\frac{5^4}{5^4} = 1 = 5^0").scale(1.0).shift(band_shift(7) + UP * 0.3)
        rows = [
            r"\text{Multiply: add. Divide: subtract.}",
            r"\text{Power of a power: multiply. Product in a bracket: share.}",
            r"\text{Anything non-zero to the } 0 \text{: one.}",
        ]
        for m in (b7_l1, b7_l2):
            self.play(Write(m))
            self.wait(2.3)
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.9).shift(band_shift(7) + DOWN * (0.6 + 0.8 * i))
            self.play(Write(m))
            self.wait(2)
        self.wait(3)
