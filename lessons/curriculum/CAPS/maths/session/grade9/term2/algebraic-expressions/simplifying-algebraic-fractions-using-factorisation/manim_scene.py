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


def pizza(centre, slices, radius=0.9, color=ORANGE):
    """A circle cut into equal slices: the same-size-slices picture for a
    common denominator."""
    g = VGroup(Circle(radius=radius, color=color).move_to(centre))
    for i in range(slices):
        ang = TAU * i / slices
        g.add(Line(centre, centre + radius * np.array([np.cos(ang), np.sin(ang), 0]), color=color))
    return g


class AlgebraicFractionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): simplifying one fraction
        title = Tex("Algebraic fractions: cancel factors, never terms").scale(1.05).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"\frac{x^2 + 8x + 15}{x + 3} = \frac{(x + 3)(x + 5)}{x + 3} = x + 5").scale(1.0).shift(UP * 1.2)
        l2 = MathTex(r"\frac{6x^2 + 9x}{3x} = \frac{3x(2x + 3)}{3x} = 2x + 3").scale(1.0).shift(UP * 0.0)
        l3 = MathTex(r"\frac{2x^2 - 8}{4x + 8} = \frac{2(x + 2)(x - 2)}{4(x + 2)} = \frac{x - 2}{2}").scale(1.0).shift(DOWN * 1.2)
        l4 = MathTex(r"x = 2: \; \tfrac{35}{5} = 7 \quad\text{and}\quad 2 + 5 = 7 \;\checkmark").scale(0.85).shift(DOWN * 2.3)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l1, color=GREEN)))
        self.wait(2)

        # --- Band 1 (subtopic_2): multiply and divide
        self.next_band(1)
        b1_title = Tex("Multiply: factorise, cancel across. Divide: flip the second").scale(0.95).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\frac{x^2 - 4}{3x} \times \frac{6x^2}{x + 2} = \frac{(x + 2)(x - 2)}{3x} \times \frac{6x^2}{x + 2} = 2x(x - 2)").scale(0.85).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"\frac{x + 1}{4} \div \frac{x^2 + x}{8} = \frac{x + 1}{4} \times \frac{8}{x(x + 1)} = \frac{2}{x}").scale(0.9).shift(band_shift(1) + UP * 0.0)
        b1_l3 = MathTex(r"\frac{x^2 + 5x + 6}{x^2 + 2x} \times \frac{x}{x + 3} = \frac{(x + 2)(x + 3)}{x(x + 2)} \times \frac{x}{x + 3} = 1").scale(0.85).shift(band_shift(1) + DOWN * 1.2)
        b1_l4 = Tex("Flip first, then factorise, then cancel.").scale(0.9).shift(band_shift(1) + DOWN * 2.2)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): add and subtract
        self.next_band(2)
        b2_title = Tex("Add and subtract: lowest common denominator").scale(1.05).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\frac{x + 1}{3} - \frac{x - 2}{4} = \frac{4(x + 1) - 3(x - 2)}{12}").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"= \frac{4x + 4 - 3x + 6}{12} = \frac{x + 10}{12}").scale(1.0).shift(band_shift(2) + UP * 0.1)
        b2_l3 = MathTex(r"\frac{3}{2x} + \frac{5}{3x} = \frac{9}{6x} + \frac{10}{6x} = \frac{19}{6x} \qquad \frac{x + 2}{x} - \frac{1}{x} = \frac{x + 1}{x}").scale(0.9).shift(band_shift(2) + DOWN * 1.0)
        b2_l4 = Tex("Keep the second numerator in a bracket until the minus is distributed.").scale(0.8).shift(band_shift(2) + DOWN * 2.1)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): mixed expressions
        self.next_band(3)
        b3_title = Tex("Mixed expressions: simplify the fraction first").scale(1.05).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\frac{x^2 - 4}{x - 2} + 3x = (x + 2) + 3x = 4x + 2").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"\frac{2x + 6}{x^2 + 3x} = \frac{2(x + 3)}{x(x + 3)} = \frac{2}{x}").scale(1.0).shift(band_shift(3) + UP * 0.1)
        b3_l3 = MathTex(r"x = 3: \; \tfrac{5}{1} + 9 = 14 \quad\text{and}\quad 4(3) + 2 = 14 \;\checkmark").scale(0.9).shift(band_shift(3) + DOWN * 1.0)
        b3_l4 = Tex("Pick a value that makes no denominator zero.").scale(0.9).shift(band_shift(3) + DOWN * 2.0)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\frac{x^2 + 8x + 15}{x + 3} = x^2 + 5").scale(0.95).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"\frac{x^2 - 9}{x - 3} = x - 3").scale(0.95).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"\frac{x + 1}{4} \div \frac{x^2 + x}{8} = \frac{4}{x + 1} \times \frac{x^2 + x}{8}").scale(0.9).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"\frac{x + 1}{3} - \frac{x - 2}{4} = \frac{x + 1 - x - 2}{12}").scale(0.9).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): cross out factors, never terms
        self.next_band(5)
        b5_title = Tex("Cross out factors, never terms").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\frac{15}{5} = \frac{3 \times 5}{5} = 3 \qquad \frac{10 + 5}{5} = \frac{15}{5} = 3, \;\text{not } 10").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = MathTex(r"\frac{x^2 + 8x + 15}{x + 3} \;\to\; \frac{(x + 3)(x + 5)}{x + 3} \;\to\; x + 5").scale(1.0).shift(band_shift(5) + UP * 0.1)
        b5_l3 = Tex("Factorise the top, factorise the bottom, cross out whole brackets.").scale(0.85).shift(band_shift(5) + DOWN * 0.9)
        b5_l4 = MathTex(r"x = 2: \; \tfrac{35}{5} = 7 \qquad 2 + 5 = 7").scale(0.9).shift(band_shift(5) + DOWN * 1.8)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): flip the second one
        self.next_band(6)
        b6_title = Tex("Flip the second one").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"\tfrac{1}{2} \div \tfrac{1}{4} = \tfrac{1}{2} \times \tfrac{4}{1} = 2").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = MathTex(r"\frac{x + 1}{4} \div \frac{x^2 + x}{8} = \frac{x + 1}{4} \times \frac{8}{x(x + 1)} = \frac{2}{x}").scale(0.95).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"\frac{x^2 - 4}{3x} \times \frac{6x^2}{x + 2} = 2x(x - 2) \qquad x = 3: \; \tfrac{5}{9} \times \tfrac{54}{5} = 6").scale(0.85).shift(band_shift(6) + DOWN * 0.8)
        b6_l4 = Tex("Flip only the one you are dividing by. Then factorise and cross out.").scale(0.8).shift(band_shift(6) + DOWN * 1.8)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): same slices before you add
        self.next_band(7)
        b7_title = Tex("Same slices before you add").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        p1 = pizza(band_shift(7) + LEFT * 4.5 + UP * 0.9, 3)
        p2 = pizza(band_shift(7) + LEFT * 2.3 + UP * 0.9, 4)
        p3 = pizza(band_shift(7) + LEFT * 0.1 + UP * 0.9, 12, color=GREEN)
        self.play(Create(p1), Create(p2))
        self.wait(1.2)
        self.play(Create(p3))
        self.wait(1.5)
        b7_l1 = MathTex(r"\tfrac{1}{3} + \tfrac{1}{4} = \tfrac{4}{12} + \tfrac{3}{12} = \tfrac{7}{12}").scale(0.9).shift(band_shift(7) + RIGHT * 3.4 + UP * 1.2)
        b7_l2 = MathTex(r"\frac{x + 1}{3} - \frac{x - 2}{4} = \frac{4x + 4 - (3x - 6)}{12} = \frac{x + 10}{12}").scale(0.9).shift(band_shift(7) + RIGHT * 2.0 + DOWN * 0.3)
        b7_l3 = Tex("Factorise. Cross out factors. Flip the second. Same bottom. Try a number.").scale(0.8).shift(band_shift(7) + DOWN * 1.6)
        for m in (b7_l1, b7_l2):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
