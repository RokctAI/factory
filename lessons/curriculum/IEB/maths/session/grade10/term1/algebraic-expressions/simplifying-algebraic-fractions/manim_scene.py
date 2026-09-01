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

# Band-layout whiteboard scene: one band per teaching beat, camera moves down
# to fresh space, nothing removed. Write-only reveals on single-string
# Tex/MathTex keep the export clean. Bands cover all seven subtopics
# (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7), dwell time proportional
# to subtopics.json (225/215/240/220/190/195/185 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SimplifyingAlgebraicFractionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the cancelling law
        title = Tex("Simplifying Algebraic Fractions").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l01 = Tex(r"Cancel FACTORS, never TERMS").scale(1.1).shift(UP * 0.9)
        self.play(Write(l01))
        self.play(Create(SurroundingRectangle(l01, color=YELLOW)))
        self.wait(2)
        l02 = MathTex(r"\frac{x^2 - 25}{x^2 + 8x + 15}").scale(1.1).shift(UP * 0.0 + DOWN * 0.3)
        self.play(Write(l02))
        self.wait(2)
        l03 = MathTex(r"= \frac{(x-5)(x+5)}{(x+3)(x+5)} = \frac{x-5}{x+3}").scale(1.05).shift(DOWN * 1.6)
        self.play(Write(l03))
        self.play(Create(SurroundingRectangle(l03, color=GREEN)))
        self.wait(2)
        l04 = Tex(r"Check at $x = 1$: both give $-1$").scale(1.0).shift(DOWN * 2.7)
        self.play(Write(l04))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): division and cubes
        self.next_band(1)
        b1_title = Tex("Divide: invert first, then factorise and cancel").scale(1.0).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\frac{x^2-1}{x+4} \div \frac{x+1}{x^2-16} = \frac{(x-1)(x+1)}{x+4} \times \frac{(x-4)(x+4)}{x+1}").scale(0.85).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"= (x-1)(x-4)").scale(1.1).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = MathTex(r"\frac{x^3+8}{x^2-4} = \frac{(x+2)(x^2-2x+4)}{(x-2)(x+2)} = \frac{x^2-2x+4}{x-2}").scale(0.9).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex(r"The irreducible trinomial stands — no term-cancelling").scale(0.9).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_3): LCD addition
        self.next_band(2)
        b2_title = Tex("Add and subtract on the LCD").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\frac{4}{x-2} - \frac{3}{x^2-4}, \quad x^2 - 4 = (x-2)(x+2)").scale(0.95).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"LCD: $(x-2)(x+2)$ — each distinct factor once").scale(0.95).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2)
        b2_l3 = MathTex(r"= \frac{4(x+2) - 3}{(x-2)(x+2)} = \frac{4x+5}{(x-2)(x+2)}").scale(0.95).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_3/4): subtraction trap + restrictions
        self.next_band(3)
        b3_title = Tex("Bracket every subtracted numerator").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\frac{3x+2}{x-5} - \frac{x-4}{x-5} = \frac{3x+2-(x-4)}{x-5}").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"= \frac{2x+6}{x-5} = \frac{2(x+3)}{x-5}").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_wrong = MathTex(r"3x + 2 - x - 4 \;\rightarrow\; 2x - 2").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l3 = Tex(r"Restrictions from ORIGINAL bottoms:").scale(0.95).shift(band_shift(3) + DOWN * 1.8)
        b3_l4 = MathTex(r"x \neq -3, \; x \neq -5 \;\text{ — the ban survives cancelling}").scale(0.9).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l3))
        self.wait(1.5)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): whole crates only
        self.next_band(4)
        b4_title = Tex("You can only cancel a whole crate").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex(r"8 crates over 12 crates $\rightarrow$ divide both by 4 $\rightarrow$ 2 over 3").scale(0.9).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex(r"8 crates PLUS one loose bottle: no more chopping").scale(0.9).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex(r"The loose bottle is a plus sign").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=YELLOW)))
        b4_l4 = MathTex(r"\frac{(x-5)(x+5)}{(x+3)(x+5)} \to \frac{x-5}{x+3}").scale(0.95).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_6): same slice size
        self.next_band(5)
        b5_title = Tex("Cut the slices the same size before you add").scale(1.0).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\tfrac{1}{2} + \tfrac{1}{3} = \tfrac{3}{6} + \tfrac{2}{6} = \tfrac{5}{6}").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\frac{4}{x-2} - \frac{3}{(x-2)(x+2)} = \frac{4x+5}{(x-2)(x+2)}").scale(0.9).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex(r"Subtract the WHOLE parcel: $-(x-4)$ removes $x$, adds 4").scale(0.85).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3))
        self.wait(2.5)

        # --- Band 6 (subtopic_7): the banned numbers
        self.next_band(6)
        b6_title = Tex("The numbers the fraction will not allow").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"R360 among 4: R90. Among 3: R120. Among 0: no answer").scale(0.85).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"(x+3)(x+5) = 0 \;\Rightarrow\; x \neq -3, \; x \neq -5").scale(0.95).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)
        b6_l3 = Tex(r"A number refused at the door stays refused").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex(r"Repack, cancel crates, match slices, ban the zeros").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(4)
