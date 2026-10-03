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


def bags(labels, centre, width=2.0, gap=0.5, color=ORANGE):
    """A row of labelled bags (rectangles), one per term."""
    g = VGroup()
    n = len(labels)
    total = n * width + (n - 1) * gap
    x0 = -total / 2 + width / 2
    for i, lab in enumerate(labels):
        pos = centre + RIGHT * (x0 + i * (width + gap))
        g.add(Rectangle(width=width, height=0.9, color=color).move_to(pos))
        g.add(MathTex(lab).scale(0.9).move_to(pos))
    return g


class FactorisingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): common factor
        title = Tex("Factorising: expansion run backwards").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"6x^2 + 9x = 3x(2x + 3) \qquad\text{HCF } 3x").scale(1.05).shift(UP * 1.3)
        l2 = MathTex(r"3(2x^2 + 3x) \;\text{is not fully factorised}").scale(0.95).shift(UP * 0.3)
        l3 = MathTex(r"4a^2 b - 6ab^2 = 2ab(2a - 3b)").scale(1.05).shift(DOWN * 0.7)
        l4 = MathTex(r"\text{Check: } 3x \times 2x = 6x^2, \quad 3x \times 3 = 9x \;\checkmark").scale(0.9).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(strike(l2)))
        self.play(Create(SurroundingRectangle(l1, color=GREEN)))
        self.wait(2)

        # --- Band 1 (subtopic_2): difference of two squares
        self.next_band(1)
        b1_title = Tex("Difference of two squares").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"a^2 - b^2 = (a + b)(a - b)").scale(1.1).shift(band_shift(1) + UP * 1.3)
        b1_l2 = MathTex(r"x^2 - 49 = (x + 7)(x - 7) \qquad 9x^2 - 4 = (3x + 2)(3x - 2)").scale(0.95).shift(band_shift(1) + UP * 0.3)
        b1_l3 = MathTex(r"2x^2 - 50 = 2(x^2 - 25) = 2(x + 5)(x - 5)").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = MathTex(r"x^2 + 49 \;\text{does not factorise:}\; (x + 7)^2 = x^2 + 14x + 49").scale(0.9).shift(band_shift(1) + DOWN * 1.7)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): trinomials
        self.next_band(2)
        b2_title = Tex("Trinomials: product $c$, sum $b$").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"x^2 + 8x + 15: \; 3 \times 5 = 15,\; 3 + 5 = 8 \;\Rightarrow\; (x + 3)(x + 5)").scale(0.9).shift(band_shift(2) + UP * 1.3)
        b2_l2 = MathTex(r"x^2 - 3x - 10: \; 2 \times (-5) = -10,\; 2 + (-5) = -3 \;\Rightarrow\; (x + 2)(x - 5)").scale(0.85).shift(band_shift(2) + UP * 0.3)
        b2_l3 = MathTex(r"x^2 - 8x + 16 = (x - 4)^2 \qquad x^2 + 2x - 24 = (x + 6)(x - 4)").scale(0.9).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = Tex(r"$c$ negative: different signs, hunt for a difference; larger number takes the sign of $b$").scale(0.8).shift(band_shift(2) + DOWN * 1.7)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): common factor then trinomial
        self.next_band(3)
        b3_title = Tex("Common factor first, then the trinomial").scale(1.05).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"3x^2 - 3x - 18 = 3(x^2 - x - 6) = 3(x - 3)(x + 2)").scale(1.0).shift(band_shift(3) + UP * 1.3)
        b3_l2 = MathTex(r"2x^2 + 16x + 30 = 2(x^2 + 8x + 15) = 2(x + 3)(x + 5)").scale(1.0).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex("1. Common factor \\quad 2. Count the terms: two or three \\quad 3. Expand to check").scale(0.85).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex("Two terms, minus, both squares: DOTS. \\quad Three terms: product and sum.").scale(0.85).shift(band_shift(3) + DOWN * 1.7)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=YELLOW)))
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"x^2 - 49 = (x - 7)^2").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"x^2 + 8x + 15 = (x + 15)(x + 1)").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"6x^2 + 9x = 3(2x^2 + 3x) \;\text{(not fully)}").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"x^2 - 3x - 10 = (x - 2)(x + 5)").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): pull out what every term shares
        self.next_band(5)
        b5_title = Tex("Pull out what every bag shares").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        row = bags([r"6x^2", r"9x"], band_shift(5) + UP * 1.1)
        self.play(Create(row))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Both hold } 3 \text{ and } x \;\Rightarrow\; 3x \text{ in front}").scale(0.95).shift(band_shift(5) + UP * 0.1)
        b5_l2 = MathTex(r"6x^2 + 9x = 3x(2x + 3) \qquad 4a^2 b - 6ab^2 = 2ab(2a - 3b)").scale(0.95).shift(band_shift(5) + DOWN * 0.8)
        b5_l3 = Tex("Pull out everything shared, not just the number. Multiply back to check.").scale(0.85).shift(band_shift(5) + DOWN * 1.7)
        for m in (b5_l1, b5_l2, b5_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): the two-number game
        self.next_band(6)
        b6_title = Tex("The two-number game").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"x^2 + 8x + 15: \;\text{multiply to } 15,\;\text{add to } 8").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = MathTex(r"1 \text{ and } 15 \;(\text{adds to } 16) \qquad 3 \text{ and } 5 \;(\text{adds to } 8) \;\checkmark").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = MathTex(r"(x + 3)(x + 5)").scale(1.2).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("Last sign minus: different signs, hunt for a difference. $x^2 - 3x - 10 = (x + 2)(x - 5)$").scale(0.8).shift(band_shift(6) + DOWN * 1.6)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): spot the shape, then check
        self.next_band(7)
        b7_title = Tex("Spot the shape, then check").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Shared part out. Then count: two terms or three?").scale(0.95).shift(band_shift(7) + UP * 1.3)
        b7_l2 = MathTex(r"x^2 - 49 = (x + 7)(x - 7) \qquad 2x^2 - 50 = 2(x + 5)(x - 5)").scale(0.95).shift(band_shift(7) + UP * 0.4)
        b7_l3 = MathTex(r"3x^2 - 3x - 18 = 3(x - 3)(x + 2)").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("Shared part out, count the terms, spot the shape, multiply back.").scale(0.85).shift(band_shift(7) + DOWN * 1.6)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
