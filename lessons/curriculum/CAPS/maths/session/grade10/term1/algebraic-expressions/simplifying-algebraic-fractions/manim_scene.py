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
# band per teaching beat, camera moves down to fresh space, nothing removed.
# Write-only reveals on single-string Tex/MathTex keep the export clean. Bands
# cover all seven subtopics (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# dwell time proportional to subtopics.json (225/215/240/220/190/195/185 of
# 1470 s).

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
        # --- Band 0 (subtopic_1): the cancelling law + the x^2 trap
        title = Tex("Simplifying Algebraic Fractions").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        law = Tex(r"Cancel FACTORS, never TERMS").scale(1.2).shift(UP * 0.9)
        self.play(Write(law))
        self.play(Create(SurroundingRectangle(law, color=YELLOW)))
        self.wait(2)
        ex = MathTex(r"\frac{x^2 - 9}{x^2 + 7x + 12}").scale(1.15).shift(DOWN * 0.4)
        self.play(Write(ex))
        self.wait(2)
        wrong = Tex(r"Strike out both $x^2$?").scale(1.05).shift(DOWN * 1.6)
        self.play(Write(wrong))
        self.play(Create(strike(wrong)))
        self.wait(1.5)
        test = Tex(r"$x=1$: true value $-\tfrac{2}{5}$, illegal gives $-\tfrac{9}{19}$").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(test))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the correct simplification
        self.next_band(1)
        b1_title = Tex("Factorise first, cancel second").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"x^2 - 9 = (x-3)(x+3)").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"x^2 + 7x + 12 = (x+3)(x+4)").scale(1.1).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"\frac{(x-3)(x+3)}{(x+3)(x+4)} = \frac{x-3}{x+4}").scale(1.1).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex(r"At $x=1$: still $-\tfrac{2}{5}$ — value unchanged").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): division — invert and multiply
        self.next_band(2)
        b2_title = Tex(r"Divide: $\frac{x^2-4}{x+3} \div \frac{x+2}{x^2-9}$").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex(r"Invert the divisor FIRST, then multiply").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\frac{x^2-4}{x+3} \times \frac{x^2-9}{x+2}").scale(1.1).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\frac{(x-2)(x+2)}{x+3} \times \frac{(x-3)(x+3)}{x+2}").scale(1.05).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = MathTex(r"= (x-2)(x-3)").scale(1.15).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): difference of cubes in the numerator
        self.next_band(3)
        b3_title = Tex(r"Simplify: $\frac{x^3 - 8}{x^2 - 4}$").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"x^3 - 8 = (x-2)(x^2 + 2x + 4)").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"x^2 - 4 = (x-2)(x+2)").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"= \frac{x^2 + 2x + 4}{x + 2}").scale(1.15).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex(r"$x^2+2x+4$ is irreducible — leave it standing").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): LCD addition/subtraction
        self.next_band(4)
        b4_title = Tex(r"Simplify: $\frac{3}{x-3} - \frac{2}{x^2-9}$").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"x^2 - 9 = (x-3)(x+3)").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"\text{LCD} = (x-3)(x+3)").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\frac{3(x+3) - 2}{(x-3)(x+3)}").scale(1.1).shift(band_shift(4) + DOWN * 0.9)
        b4_l4 = MathTex(r"= \frac{3x + 7}{(x-3)(x+3)}").scale(1.1).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the subtraction bracket trap
        self.next_band(5)
        b5_title = Tex(r"Simplify: $\frac{2x+1}{x-4} - \frac{x-3}{x-4}$").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_wrong = MathTex(r"2x + 1 - x - 3 = x - 2").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l1 = MathTex(r"2x + 1 - (x - 3)").scale(1.1).shift(band_shift(5) + UP * 0.1)
        b5_l2 = MathTex(r"= 2x + 1 - x + 3 = x + 4").scale(1.1).shift(band_shift(5) + DOWN * 0.9)
        b5_l3 = MathTex(r"= \frac{x+4}{x-4}").scale(1.15).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        b5_rule = Tex("Bracket every numerator you subtract").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_rule))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): restrictions + error museum
        self.next_band(6)
        b6_title = Tex("Restrictions — from the ORIGINAL denominators").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"\frac{x^2-9}{(x+3)(x+4)}: \quad x \neq -3, \; x \neq -4").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex(r"Cancelling cannot un-ban a value").scale(1.05).shift(band_shift(6) + UP * 0.2)
        b6_l3 = Tex(r"Division example: $x \neq -3, \; 3, \; -2$").scale(1.05).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex(r"Never: cancel terms, cancel before factorising,").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        b6_l5 = Tex(r"drop the bracket, or add denominators").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): only whole crates cancel
        self.next_band(7)
        b7_title = Tex("You can only cancel a whole crate").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"6 crates over 9 crates $\rightarrow$ 2 over 3 — fine").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"6 crates + 1 loose bottle? No cancelling").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"\frac{(x-3)(x+3)}{(x+3)(x+4)} = \frac{x-3}{x+4}").scale(1.05).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex(r"Till check at $x=1$: both give $-\tfrac{2}{5}$").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l4))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): same slice size before adding
        self.next_band(8)
        b8_title = Tex("Cut the slices the same size first").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\tfrac{4}{12} + \tfrac{3}{12} = \tfrac{7}{12}").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"\frac{3}{x-3} - \frac{2}{(x-3)(x+3)}").scale(1.05).shift(band_shift(8) + UP * 0.0)
        b8_l3 = MathTex(r"= \frac{3x + 9 - 2}{(x-3)(x+3)} = \frac{3x+7}{(x-3)(x+3)}").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex(r"Subtract the WHOLE parcel: $-(x-3)$ gives $-x+3$").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l4))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): the banned numbers
        self.next_band(9)
        b9_title = Tex("The numbers the fraction will not allow").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Sharing R240 among 0 learners: no answer exists").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"So the bottom may never be zero").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"(x+3)(x+4): \quad x \neq -3, \; x \neq -4").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex(r"Ban from the ORIGINAL bottoms — cancelling").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        b9_l5 = Tex(r"cannot let a refused number back in").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(4)
