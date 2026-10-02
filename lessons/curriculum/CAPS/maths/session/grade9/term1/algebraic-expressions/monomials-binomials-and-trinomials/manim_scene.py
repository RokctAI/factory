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


class PolynomialNamesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): counting terms
        title = Tex("Monomials, Binomials, Trinomials").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"4x^3 \;\text{(1 term)} \qquad x^2 - 9 \;\text{(2)} \qquad 3x^2 - 5x + 2 \;\text{(3)}").scale(0.95).shift(UP * 1.3)
        l2 = MathTex(r"3xy \text{ is ONE term: factors, not terms} \qquad \frac{6x}{3} \text{ is one term}").scale(0.9).shift(UP * 0.3)
        l3 = MathTex(r"2x(x + 1) \text{ is one term; expanded, } 2x^2 + 2x \text{ is two}").scale(0.9).shift(DOWN * 0.7)
        l4 = MathTex(r"2x^2 + 3x + 1 + x = 2x^2 + 4x + 1 \;\text{(count AFTER simplifying)}").scale(0.9).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): degree names
        self.next_band(1)
        b1_title = Tex("Degree gives the first name").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        rows = [
            r"3x^2 - 5x + 2: \text{ quadratic trinomial}",
            r"x^2 - 9: \text{ quadratic binomial} \qquad 4x^3: \text{ cubic monomial}",
            r"3x + 2: \text{ linear binomial} \qquad 7: \text{ constant monomial}",
            r"2 - x^3: \text{ leading term } -x^3, \text{ leading coefficient } -1",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.9).shift(band_shift(1) + UP * (1.3 - 0.8 * i))
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # --- Band 2 (subtopic_3): not polynomials
        self.next_band(2)
        b2_title = Tex("Not polynomials").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\frac{x}{2} = \tfrac{1}{2}x \;\checkmark \qquad \frac{2}{x} = 2x^{-1} \;\text{(not a polynomial)}").scale(0.95).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"\sqrt{x} = x^{1/2} \;\text{(not)} \qquad \sqrt{2}\,x \;\checkmark").scale(0.95).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"5x^{-2} = \frac{5}{x^2} \;\text{(not)}").scale(0.95).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = Tex("Test: every variable exponent a whole number").scale(0.95).shift(band_shift(2) + DOWN * 1.8)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): standard form
        self.next_band(3)
        b3_title = Tex("Standard form: descending powers").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"2 - 5x + 3x^2 \;\to\; 3x^2 - 5x + 2").scale(1.05).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"x + x^3 - 4 \;\to\; x^3 + x - 4").scale(1.05).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"5x - 2x^2 + 3 + 4x^2 - x = 2x^2 + 4x + 3 \;\text{(quadratic trinomial)}").scale(0.9).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = Tex("Simplify, order, then read terms and degree").scale(0.95).shift(band_shift(3) + DOWN * 1.8)
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
        b4_l1 = MathTex(r"2x + 3x \text{ ``a binomial''}").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"3xy \text{ ``a trinomial''} \qquad \tfrac{2}{x} \text{ ``a monomial''}").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"4x^3 \text{ ``a trinomial''}").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"2 - 5x + 3x^2 \to 3x^2 + 5x + 2").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): count the pieces
        self.next_band(5)
        b5_title = Tex("Count the pieces").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Mono: monorail. Bi: bicycle. Tri: tricycle.").scale(1.0).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Only plus and minus make gaps. Times and divide do not.").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l3 = MathTex(r"3xy: \text{ one piece, three ingredients} \qquad x + y + z: \text{ three pieces}").scale(0.9).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = MathTex(r"4x^3 \ldots 1 \qquad x^2 - 9 \ldots 2 \qquad 3x^2 - 5x + 2 \ldots 3").scale(0.95).shift(band_shift(5) + DOWN * 1.5)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): tidy first
        self.next_band(6)
        b6_title = Tex("Tidy first, then name").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"2x + 3x = 5x: \text{ a monomial in disguise}").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = MathTex(r"5x - 2x^2 + 3 + 4x^2 - x \to 2x^2 + 4x + 3").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Biggest power first; every piece keeps its sign").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = MathTex(r"\tfrac{x}{2} \;\checkmark \qquad \tfrac{2}{x},\; \sqrt{x}: \text{ not polynomials}").scale(0.95).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): the name tag
        self.next_band(7)
        b7_title = Tex("The full name tag").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        rows = [
            r"\text{Power 1: linear. 2: quadratic. 3: cubic. None: constant.}",
            r"3x^2 - 5x + 2 \to \text{quadratic trinomial}",
            r"4x^3 \to \text{cubic monomial (3 is the power, not the pieces)}",
            r"x^2 - 9 \to \text{quadratic binomial: difference of squares next term}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.85).shift(band_shift(7) + UP * (1.3 - 0.75 * i))
            self.play(Write(m))
            self.wait(2.0)
        b7_l5 = Tex("Tidy. Count. Name. Read the tag, pick the tool.").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
