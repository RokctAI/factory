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


def bags(labels, origin, w=1.7):
    g = VGroup()
    for i, lab in enumerate(labels):
        r = Rectangle(width=w, height=0.8, color=ORANGE).move_to(origin + RIGHT * i * (w + 0.3))
        g.add(r)
        g.add(MathTex(lab).scale(0.9).move_to(r))
    return g


class DistributingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): integer times polynomial
        title = Tex("Multiplying and Dividing by Monomials").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"3(2x - 5) = 6x - 15 \qquad 4(x^2 + 3x - 2) = 4x^2 + 12x - 8").scale(0.95).shift(UP * 1.3)
        l2 = MathTex(r"-2(x^2 - 3x + 4) = -2x^2 + 6x - 8 \qquad -(a - b) = -a + b").scale(0.95).shift(UP * 0.3)
        l3 = MathTex(r"5(x - 2) - 3(x - 4) = 5x - 10 - 3x + 12 = 2x + 2").scale(0.95).shift(DOWN * 0.7)
        l4 = MathTex(r"x = 1: \; -5 + 9 = 4 \quad\text{and}\quad 2 + 2 = 4 \;\checkmark").scale(0.95).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): monomial times polynomial
        self.next_band(1)
        b1_title = Tex("A monomial multiplier").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"2x(3x^2 - x + 4) = 6x^3 - 2x^2 + 8x").scale(1.1).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"-3ab(2a - 5b) = -6a^2 b + 15ab^2 \qquad x^2(x^3 - 2x + 1) = x^5 - 2x^3 + x^2").scale(0.9).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"2x(x + 3) - x(x - 1) = 2x^2 + 6x - x^2 + x = x^2 + 7x").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"x = 2: \; 20 - 2 = 18 \quad\text{and}\quad 4 + 14 = 18 \;\checkmark").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): dividing
        self.next_band(2)
        b2_title = Tex("Dividing: every term above the bar").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\frac{6x^2 - 9x}{3} = 2x^2 - 3x \qquad \frac{6x + 3}{3} = 2x + 1").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"\frac{12x^3 - 8x^2 + 4x}{4x} = 3x^2 - 2x + 1 \;\text{(the 1 is a term)}").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"\frac{10a^2 b - 15ab^2}{-5ab} = -2a + 3b").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"\text{Check: } 4x(3x^2 - 2x + 1) = 12x^3 - 8x^2 + 4x \;\checkmark").scale(0.95).shift(band_shift(2) + DOWN * 1.8)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): checks
        self.next_band(3)
        b3_title = Tex("Two checks").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Substitute $x = 2$ (not 1 when exponents matter; never a value that zeroes a divisor)").scale(0.85).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"Reverse: multiply a quotient back by the divisor").scale(0.95).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex(r"Layout: every product on line 1, collect on line 2, order on line 3").scale(0.9).shift(band_shift(3) + DOWN * 0.8)
        for m in (b3_l1, b3_l2, b3_l3):
            self.play(Write(m))
            self.wait(2.4)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"3(2x - 5) = 6x - 5 \qquad \frac{6x + 3}{3} = 2x + 3").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"-2(x^2 - 3x + 4) = -2x^2 - 6x - 8").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"\frac{4x}{4x} = 0 \qquad 2x(3x^2) = 6x^2").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        for m in (b4_l1, b4_l2, b4_l3):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): bags
        self.next_band(5)
        b5_title = Tex("Sharing out the multiplier").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        row = bags([r"3x^2", r"-x", r"+4"], band_shift(5) + UP * 1.2 + LEFT * 2.0)
        mult = MathTex(r"2x \;\times").scale(1.1).next_to(row, LEFT, buff=0.4)
        self.play(Create(row), Write(mult))
        self.wait(1.5)
        b5_l1 = MathTex(r"6x^3 \qquad -2x^2 \qquad +8x").scale(1.1).shift(band_shift(5) + UP * 0.1)
        b5_l2 = Tex(r"Every bag gets the delivery. $x = 1$: $2 \times 6 = 12$ and $6 - 2 + 8 = 12$.").scale(0.85).shift(band_shift(5) + DOWN * 0.8)
        b5_l3 = MathTex(r"3(2x - 5) + 2(x + 7) = 6x - 15 + 2x + 14 = 8x - 1").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        for m in (b5_l1, b5_l2, b5_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): minus flips
        self.next_band(6)
        b6_title = Tex("The minus sign flips everything").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"-2(x^2 - 3x + 4): \; -2x^2 \quad +6x \quad -8").scale(1.05).shift(band_shift(6) + UP * 1.3)
        b6_l2 = MathTex(r"x = 1: \; -2 \times 2 = -4 \qquad -2 + 6 - 8 = -4 \;\checkmark \qquad -2 - 6 - 8 = -16 \;\times").scale(0.85).shift(band_shift(6) + UP * 0.4)
        b6_l3 = MathTex(r"5(x - 2) - 3(x - 4): \; -3 \times -4 = +12 \;\Rightarrow\; 2x + 2").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex(r"Say ``flip'' out loud for each bag").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): dividing shares
        self.next_band(7)
        b7_title = Tex("Dividing shares too").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"\frac{12x^3 - 8x^2 + 4x}{4x}: \; 3x^2 \quad -2x \quad +1").scale(1.05).shift(band_shift(7) + UP * 1.3)
        b7_l2 = MathTex(r"4x \times (3x^2 - 2x + 1) = 12x^3 - 8x^2 + 4x \;\checkmark").scale(0.95).shift(band_shift(7) + UP * 0.4)
        b7_l3 = MathTex(r"\frac{10a^2 b - 15ab^2}{-5ab} = -2a + 3b \qquad \frac{6x + 3}{3} = 2x + 1").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("Deliver to every bag. Flip on a negative. Divide every term. Check.").scale(0.85).shift(band_shift(7) + DOWN * 1.5)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
