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


class AlgebraConventionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): conventions
        title = Tex("Conventions of Algebra").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"3 \times x = 3x \qquad y \times 3 \times x = 3xy \qquad 1x = x \qquad -1x = -x").scale(0.95).shift(UP * 1.3)
        l2 = MathTex(r"x \div 2 = \frac{x}{2} = \tfrac{1}{2}x \qquad x + x = 2x \qquad x \times x = x^2").scale(0.95).shift(UP * 0.3)
        l3 = MathTex(r"2 \times 3x = 6x \qquad 2x \times 3x = 6x^2 \qquad (3x)^2 = 9x^2").scale(0.95).shift(DOWN * 0.7)
        l4 = MathTex(r"x = -2: \; 4(-2)^2 - 3(-2) + 7 = 16 + 6 + 7 = 29").scale(0.95).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): terms and coefficients
        self.next_band(1)
        b1_title = Tex("Terms, coefficients, constants").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"4x^2 \;\; - 3x \;\; + 7").scale(1.4).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"Three terms. Coefficients 4 and $-3$. Constant 7.").scale(0.95).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"\text{coefficient of } -x \text{ is } -1 \qquad \text{coefficient of } \tfrac{x}{2} \text{ is } \tfrac{1}{2} \qquad 3xy \text{ is one term}").scale(0.85).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"3k + 2: \; 3 = \text{rate per km (coefficient)},\; 2 = \text{flag fall (constant)}").scale(0.85).shift(band_shift(1) + DOWN * 1.8)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): exponents and degree
        self.next_band(2)
        b2_title = Tex("Exponent against coefficient; degree").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"x = 3: \quad 2x = 6 \qquad x^2 = 9 \qquad 4x^2 = 36").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"\deg(4x^2) = 2 \quad \deg(-3x) = 1 \quad \deg(7) = 0 \quad \deg(3x^2 y) = 3").scale(0.95).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"x^3 \cdot x^2 = x^5 \qquad \frac{x^6}{x^2} = x^4 \qquad (2x^2)^3 = 8x^6").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"3x^2 \neq (3x)^2 = 9x^2").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): like terms
        self.next_band(3)
        b3_title = Tex("Like and unlike terms").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"3x + 5x - 2x = 6x \qquad 2xy + 5yx = 7xy").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"3x + 2 \text{ stays} \qquad 3x + 5x^2 \text{ stays} \qquad 4a^2 b + 4ab^2 \text{ stays}").scale(0.9).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"7a - 3b + 2a + b = 9a - 2b").scale(1.05).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = MathTex(r"4x^2 - 3x + 7 + 2x^2 + 5x - 10 = 6x^2 + 2x - 3").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"3x + 2 = 5x \qquad x + x = x^2").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"2x^2 + 3x^2 = 5x^4").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"3x + 3x^2 = 6x^3").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"7a - 3b + 2a \to 7a + 2a + 3b").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): grammar
        self.next_band(5)
        b5_title = Tex("The grammar of algebra").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        rows = [
            r"\text{Numbers first, letters alphabetical, no times sign: } 3xy",
            r"\text{One of something is the something: } x,\; -x",
            r"\text{Added: } x + x = 2x \qquad \text{Multiplied: } x \cdot x = x^2",
            r"\text{Brackets protect the sign: } 4(-2)^2 = 16",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.85).shift(band_shift(5) + UP * (1.3 - 0.8 * i))
            self.play(Write(m))
            self.wait(2.0)
        self.wait(1.5)

        # --- Band 6 (subtopic_6): fruit bowl
        self.next_band(6)
        b6_title = Tex("Apples and bananas").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        apples = VGroup(*[Circle(radius=0.18, color=RED).shift(band_shift(6) + UP * 1.2 + LEFT * (4.5 - 0.45 * i)) for i in range(3)])
        apples2 = VGroup(*[Circle(radius=0.18, color=RED).shift(band_shift(6) + UP * 1.2 + LEFT * (2.6 - 0.45 * i)) for i in range(5)])
        self.play(Create(apples))
        self.play(Create(apples2))
        lab = MathTex(r"3x + 5x = 8x").scale(1.0).shift(band_shift(6) + UP * 1.2 + RIGHT * 2.8)
        self.play(Write(lab))
        self.wait(2)
        b6_l2 = MathTex(r"3x + 5y: \text{ different fruit, stays} \qquad 3x + 2: \text{ stays}").scale(0.9).shift(band_shift(6) + UP * 0.1)
        b6_l3 = MathTex(r"x \text{ and } x^2 \text{ are different fruit: } 3x + 5x^2 \text{ stays}").scale(0.9).shift(band_shift(6) + DOWN * 0.8)
        b6_l4 = MathTex(r"2x^2 + 3x^2 = 5x^2 \;\text{(the little number stays)}").scale(0.9).shift(band_shift(6) + DOWN * 1.7)
        for m in (b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): reading a sentence
        self.next_band(7)
        b7_title = Tex("Reading an expression like a sentence").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"\underbrace{4x^2}_{\text{4 lots of } x \cdot x} \quad \underbrace{-3x}_{\text{minus 3 lots of } x} \quad \underbrace{+7}_{\text{fixed bit}}").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("Coefficient: how many. Constant: the fixed bit. Exponent: copies multiplied.").scale(0.8).shift(band_shift(7) + DOWN * 0.2)
        b7_l3 = Tex("Degree: the biggest exponent, here 2.").scale(0.9).shift(band_shift(7) + DOWN * 1.0)
        b7_l4 = Tex("Every term owns its sign. Same fruit adds; the little number stays.").scale(0.8).shift(band_shift(7) + DOWN * 1.9)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
