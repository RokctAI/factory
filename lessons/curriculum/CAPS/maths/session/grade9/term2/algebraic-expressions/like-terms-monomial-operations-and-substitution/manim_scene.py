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


class MonomialOperationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): like terms and the minus bracket
        title = Tex("Like Terms, Monomials, Substitution").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"(3x^2 - 2x + 5) - (x^2 + 4x - 1)").scale(1.1).shift(UP * 1.3)
        l2 = MathTex(r"= 3x^2 - 2x + 5 - x^2 - 4x + 1 \;\text{(every sign flips)}").scale(1.0).shift(UP * 0.3)
        l3 = MathTex(r"= 2x^2 - 6x + 6").scale(1.15).shift(DOWN * 0.7)
        l4 = MathTex(r"x = 1: \; 6 - 4 = 2 \quad\text{and}\quad 2 - 6 + 6 = 2 \;\checkmark \qquad \tfrac{1}{2}x + \tfrac{1}{3}x = \tfrac{5}{6}x").scale(0.9).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l3, color=GREEN)))
        self.wait(2)

        # --- Band 1 (subtopic_2): monomials
        self.next_band(1)
        b1_title = Tex("Monomials: coefficients multiply, exponents add").scale(1.05).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"3x^2 \times 4x^3 = 12x^5 \qquad -2ab \times 5a^2 b = -10a^3 b^2").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"12x^5 \div 3x^2 = 4x^3 \qquad 15a^3 b^2 \div (-5ab) = -3a^2 b").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"(2x^2 y)^3 = 8x^6 y^3 \qquad (-3a^2)^2 = 9a^4").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"3x \times 2x = 6x^2 \quad\text{but}\quad 3x + 2x = 5x").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): substitution
        self.next_band(2)
        b2_title = Tex("Substitution: brackets around every value").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"2\left(\tfrac{1}{2}\right)^2 - 3\left(\tfrac{1}{2}\right) + 1 = \tfrac{1}{2} - \tfrac{3}{2} + 1 = 0").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"2(0{,}5)^2 - 3(0{,}5) + 1 = 0{,}5 - 1{,}5 + 1 = 0").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"2\left(-\tfrac{3}{4}\right)^2 - 3\left(-\tfrac{3}{4}\right) + 1 = \tfrac{9}{8} + \tfrac{18}{8} + \tfrac{8}{8} = \tfrac{35}{8}").scale(0.95).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"3a^2 b: \; 3(1{,}5)^2(-2) = -13{,}5 \qquad P = 2(2{,}5 + 1{,}25) = 7{,}5").scale(0.9).shift(band_shift(2) + DOWN * 1.8)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): mixed
        self.next_band(3)
        b3_title = Tex("Products first, then collect").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"3x \cdot 2x + 4x^2 - x \cdot 5x = 6x^2 + 4x^2 - 5x^2 = 5x^2").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"12x^3 \div 4x + 2x^2 = 3x^2 + 2x^2 = 5x^2").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"2x^2 - (3x \cdot x - 4x^2) = 2x^2 - (-x^2) = 3x^2").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = Tex("Check at $x = 1$ or $x = 2$: original and answer must agree").scale(0.9).shift(band_shift(3) + DOWN * 1.8)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"3x \times 2x = 5x^2 \qquad x^2 \cdot x^3 = x^6").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"-(x - 3) = -x - 3").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"x = -2: \; -2^2 = -4 \;\text{(no brackets)}").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"\tfrac{1}{2}x + \tfrac{1}{3}x = \tfrac{2}{5}x").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the bag
        self.next_band(5)
        b5_title = Tex("Take away the whole bag").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        bag = Rectangle(width=4.2, height=0.9, color=ORANGE).shift(band_shift(5) + UP * 1.2)
        bag_lab = MathTex(r"x^2 + 4x - 1").scale(1.0).move_to(bag)
        minus = MathTex(r"-").scale(1.6).next_to(bag, LEFT, buff=0.3)
        self.play(Create(bag), Write(bag_lab), Write(minus))
        self.wait(1.5)
        b5_l1 = MathTex(r"-x^2 \quad -4x \quad +1 \;\text{(everything in the bag flips)}").scale(1.0).shift(band_shift(5) + UP * 0.1)
        b5_l2 = MathTex(r"3x^2 - 2x + 5 - x^2 - 4x + 1 = 2x^2 - 6x + 6").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        b5_l3 = Tex(r"Prove it: $x = 1$ gives 2 both ways. Flip only the first sign: 8. Busted.").scale(0.85).shift(band_shift(5) + DOWN * 1.7)
        for m in (b5_l1, b5_l2, b5_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): numbers times, little numbers add
        self.next_band(6)
        b6_title = Tex("Numbers times, little numbers add").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"3x^2 \times 4x^3: \; 3 \times 4 = 12,\; 2 + 3 = 5 \;\Rightarrow\; 12x^5").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = MathTex(r"12x^5 \div 3x^2: \; 12 \div 3 = 4,\; 5 - 2 = 3 \;\Rightarrow\; 4x^3").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = MathTex(r"-2ab \times 5a^2 b = -10a^3 b^2 \qquad (2x^2 y)^3 = 8x^6 y^3").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = MathTex(r"x = 2: \; 3x \times 2x = 24 \qquad 3x + 2x = 10").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): plug in carefully
        self.next_band(7)
        b7_title = Tex("Plug in carefully").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"x = \tfrac{1}{2}: \; 2\left(\tfrac{1}{2}\right)^2 - 3\left(\tfrac{1}{2}\right) + 1 = 0 \qquad x = 0{,}5: \; 0").scale(0.95).shift(band_shift(7) + UP * 1.3)
        b7_l2 = MathTex(r"x = -\tfrac{3}{4}: \; 2\left(-\tfrac{3}{4}\right)^2 = +\tfrac{9}{8},\; -3\left(-\tfrac{3}{4}\right) = +\tfrac{9}{4}").scale(0.95).shift(band_shift(7) + UP * 0.3)
        b7_l3 = Tex("Brackets first. Square the $x$, then multiply by the number in front.").scale(0.85).shift(band_shift(7) + DOWN * 0.6)
        b7_l4 = Tex("Bag flips all. Numbers times, little numbers add. Brackets. Check with 1.").scale(0.8).shift(band_shift(7) + DOWN * 1.6)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
