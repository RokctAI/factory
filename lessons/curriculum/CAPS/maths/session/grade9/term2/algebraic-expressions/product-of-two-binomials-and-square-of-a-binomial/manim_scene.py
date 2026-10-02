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


def grid2x2(top, side, cells, centre, size=1.1):
    """Two-by-two multiplication grid: headers along the top and side, one
    product per cell. Returns a VGroup of the lines and labels."""
    g = VGroup()
    for i in range(3):
        g.add(Line(centre + LEFT * size + UP * (size - i * size),
                   centre + RIGHT * size + UP * (size - i * size), color=GREY))
        g.add(Line(centre + UP * size + RIGHT * (i * size - size),
                   centre + DOWN * size + RIGHT * (i * size - size), color=GREY))
    for j, t in enumerate(top):
        g.add(MathTex(t).scale(0.8).move_to(centre + UP * (size + 0.4) + RIGHT * (j * size - size / 2)))
    for i, t in enumerate(side):
        g.add(MathTex(t).scale(0.8).move_to(centre + LEFT * (size + 0.5) + UP * (size / 2 - i * size)))
    for i in range(2):
        for j in range(2):
            g.add(MathTex(cells[i][j]).scale(0.8).move_to(
                centre + RIGHT * (j * size - size / 2) + UP * (size / 2 - i * size)))
    return g


class BinomialProductsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the grid
        title = Tex("Product of Two Binomials").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        g = grid2x2([r"x", r"+3"], [r"x", r"+5"],
                    [[r"x^2", r"3x"], [r"5x", r"15"]], LEFT * 3.2 + DOWN * 0.3)
        self.play(Create(g))
        self.wait(2.5)
        l1 = MathTex(r"(x + 3)(x + 5) = x^2 + 5x + 3x + 15").scale(0.95).shift(RIGHT * 2.6 + UP * 1.0)
        l2 = MathTex(r"= x^2 + 8x + 15").scale(1.1).shift(RIGHT * 2.6 + UP * 0.1)
        l3 = MathTex(r"(2x - 3)(x + 4) = 2x^2 + 8x - 3x - 12 = 2x^2 + 5x - 12").scale(0.85).shift(RIGHT * 2.6 + DOWN * 0.9)
        l4 = MathTex(r"x = 1: \; 4 \times 6 = 24 \quad\text{and}\quad 1 + 8 + 15 = 24 \;\checkmark").scale(0.85).shift(RIGHT * 2.6 + DOWN * 1.8)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l2, color=GREEN)))
        self.wait(2)

        # --- Band 1 (subtopic_2): square of a binomial
        self.next_band(1)
        b1_title = Tex("Square of a binomial: the middle term exists").scale(1.05).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"(2x + 5)^2 = (2x + 5)(2x + 5) = 4x^2 + 10x + 10x + 25").scale(0.9).shift(band_shift(1) + UP * 1.3)
        b1_l2 = MathTex(r"= 4x^2 + 20x + 25").scale(1.1).shift(band_shift(1) + UP * 0.4)
        b1_l3 = MathTex(r"(a + b)^2 = a^2 + 2ab + b^2 \qquad (a - b)^2 = a^2 - 2ab + b^2").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = MathTex(r"(x - 4)^2 = x^2 - 8x + 16 \qquad (x + 5)^2 \neq x^2 + 25").scale(0.95).shift(band_shift(1) + DOWN * 1.5)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): sum times difference
        self.next_band(2)
        b2_title = Tex("Sum times difference: the middle cancels").scale(1.05).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"(x + 7)(x - 7) = x^2 - 7x + 7x - 49 = x^2 - 49").scale(0.95).shift(band_shift(2) + UP * 1.3)
        b2_l2 = MathTex(r"(3x - 2)(3x + 2) = 9x^2 - 4").scale(1.0).shift(band_shift(2) + UP * 0.4)
        b2_l3 = MathTex(r"(a + b)(a - b) = a^2 - b^2").scale(1.1).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = MathTex(r"\text{but } (x - 7)^2 = x^2 - 14x + 49 \quad\text{(same sign, three terms)}").scale(0.85).shift(band_shift(2) + DOWN * 1.5)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): mixed expansions
        self.next_band(3)
        b3_title = Tex("Mixed: expand each product on its own line").scale(1.05).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"(x + 3)(x + 5) - (x - 2)^2").scale(1.0).shift(band_shift(3) + UP * 1.3)
        b3_l2 = MathTex(r"= x^2 + 8x + 15 - (x^2 - 4x + 4)").scale(1.0).shift(band_shift(3) + UP * 0.4)
        b3_l3 = MathTex(r"= x^2 + 8x + 15 - x^2 + 4x - 4 = 12x + 11").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = MathTex(r"(x - 3)^2 - (x + 3)(x - 3) = x^2 - 6x + 9 - x^2 + 9 = -6x + 18").scale(0.85).shift(band_shift(3) + DOWN * 1.5)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"(x + 5)^2 = x^2 + 25").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"(2x - 3)(x + 4) = 2x^2 - 12").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"(x - 4)^2 = x^2 - 8x - 16").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"-(x^2 - 4x + 4) = -x^2 - 4x + 4").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): every term meets every term
        self.next_band(5)
        b5_title = Tex("Every term meets every term: four meetings").scale(1.05).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        bag1 = Rectangle(width=2.4, height=0.9, color=ORANGE).shift(band_shift(5) + LEFT * 3.5 + UP * 1.0)
        bag2 = Rectangle(width=2.4, height=0.9, color=ORANGE).shift(band_shift(5) + LEFT * 0.5 + UP * 1.0)
        lab1 = MathTex(r"2x \quad -3").scale(0.9).move_to(bag1)
        lab2 = MathTex(r"x \quad +4").scale(0.9).move_to(bag2)
        self.play(Create(bag1), Create(bag2), Write(lab1), Write(lab2))
        self.wait(1.5)
        g5 = grid2x2([r"x", r"+4"], [r"2x", r"-3"],
                     [[r"2x^2", r"8x"], [r"-3x", r"-12"]], band_shift(5) + RIGHT * 3.6 + UP * 0.3, size=0.9)
        self.play(Create(g5))
        self.wait(2)
        b5_l1 = MathTex(r"2x^2 + 8x - 3x - 12 = 2x^2 + 5x - 12").scale(0.95).shift(band_shift(5) + LEFT * 2.0 + DOWN * 0.3)
        b5_l2 = Tex(r"$x = 1$: bags give $(-1)(5) = -5$; answer gives $2 + 5 - 12 = -5$. Match.").scale(0.8).shift(band_shift(5) + DOWN * 1.4)
        for m in (b5_l1, b5_l2):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): the middle term is not zero
        self.next_band(6)
        b6_title = Tex("The middle term is not zero").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        big = Square(side_length=1.6, color=BLUE).shift(band_shift(6) + LEFT * 3.9 + UP * 0.3)
        r1 = Rectangle(width=0.8, height=1.6, color=GREEN).next_to(big, RIGHT, buff=0)
        r2 = Rectangle(width=1.6, height=0.8, color=GREEN).next_to(big, DOWN, buff=0)
        small = Square(side_length=0.8, color=ORANGE).next_to(r1, DOWN, buff=0)
        self.play(Create(big), Create(r1), Create(r2), Create(small))
        self.wait(1.5)
        t_big = MathTex(r"x^2").scale(0.8).move_to(big)
        t_r1 = MathTex(r"5x").scale(0.7).move_to(r1)
        t_r2 = MathTex(r"5x").scale(0.7).move_to(r2)
        t_small = MathTex(r"25").scale(0.7).move_to(small)
        self.play(Write(t_big), Write(t_r1), Write(t_r2), Write(t_small))
        self.wait(2)
        b6_l1 = MathTex(r"(x + 5)^2 = x^2 + 10x + 25").scale(1.0).shift(band_shift(6) + RIGHT * 2.2 + UP * 1.0)
        b6_l2 = MathTex(r"x = 1: \; 6^2 = 36 \qquad 1 + 25 = 26 \;\text{(10 missing)}").scale(0.85).shift(band_shift(6) + RIGHT * 2.2 + UP * 0.1)
        b6_l3 = Tex("First squared, double the product, last squared.").scale(0.85).shift(band_shift(6) + RIGHT * 2.2 + DOWN * 0.8)
        b6_l4 = MathTex(r"(x - 4)^2 = x^2 - 8x + 16 \;\text{(last term always positive)}").scale(0.8).shift(band_shift(6) + RIGHT * 1.6 + DOWN * 1.7)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): two terms vanish, then check
        self.next_band(7)
        b7_title = Tex("Two terms vanish, then check everything").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"(x + 7)(x - 7) = x^2 - 7x + 7x - 49 = x^2 - 49").scale(0.95).shift(band_shift(7) + UP * 1.3)
        b7_l2 = MathTex(r"(x + 3)(x + 5) - (x - 2)^2 = x^2 + 8x + 15 - x^2 + 4x - 4 = 12x + 11").scale(0.85).shift(band_shift(7) + UP * 0.4)
        b7_l3 = MathTex(r"x = 1: \; 24 - 1 = 23 \qquad 12 + 11 = 23 \;\checkmark").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("Four meetings with signs. Keep the second bag. Sort. Check with 1.").scale(0.8).shift(band_shift(7) + DOWN * 1.6)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
