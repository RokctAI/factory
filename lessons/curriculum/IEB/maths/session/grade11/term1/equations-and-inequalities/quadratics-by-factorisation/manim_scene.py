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

# Band layout: one frame-height band per teaching beat; the camera moves down
# to fresh space and earlier work stays on the canvas. Only exporter-supported
# mobjects; every line of working is a single-string MathTex revealed with
# Write — no sub-part transforms.
#
# Mirrors script.md across all seven subtopics (Part 1 — Expert: 1-4;
# Part 2 — Simplifier: 5-7), band time roughly proportional to subtopics.json
# (220/220/240/235/185/185/190 of 1475 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class QuadraticsByFactorisationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): standard form and the zero-product principle
        title = Tex("Quadratic Equations by Factorisation").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"A \times B = 0 \;\Rightarrow\; A = 0 \text{ or } B = 0").scale(1.1).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = MathTex(r"A \times B = 6 \;\Rightarrow\; \text{nothing about } A").scale(1.05).shift(DOWN * 0.1)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"$6 = 1 \times 6 = 3 \times 2 = 12 \times \tfrac{1}{2} = \ldots$").scale(1.0).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex(r"Only ZERO forces a factor to confess").scale(1.0).shift(DOWN * 2.1)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the =6 trap, worked in full
        self.next_band(1)
        b1_title = Tex(r"Solve $(x+1)(x-4) = 6$").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_wrong = MathTex(r"x + 1 = 6 \;\Rightarrow\; x = 5?").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l1 = MathTex(r"x^2 - 3x - 4 = 6").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"x^2 - 3x - 10 = 0").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"(x - 5)(x + 2) = 0").scale(1.05).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"x = 5 \;\text{ or }\; x = -2").scale(1.05).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_1): never divide by a variable
        self.next_band(2)
        b2_title = Tex(r"Solve $x^2 = 7x$").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_wrong = MathTex(r"\div x: \quad x = 7 \;\text{ only}").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l1 = Tex(r"Dividing by $x$ deletes the solution $x = 0$").scale(0.95).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"x^2 - 7x = 0 \;\Rightarrow\; x(x - 7) = 0").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"x = 0 \;\text{ or }\; x = 7").scale(1.05).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): shapes 1 and 2 — common factor, simple trinomial
        self.next_band(3)
        b3_title = Tex("The four factorising shapes").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"3x^2 - 15x = 0 \;\Rightarrow\; 3x(x - 5) = 0").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"x = 0 \;\text{ or }\; x = 5").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"x^2 - 2x - 15 = 0: \;\; \times\, {-15},\; +\, {-2}").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = MathTex(r"(x - 5)(x + 3) = 0 \;\Rightarrow\; x = 5 \text{ or } -3").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_2): shape 3 — leading coefficient not one
        self.next_band(4)
        b4_title = Tex(r"Solve $2x^2 + 7x - 4 = 0$: split the middle").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"a \times c = -8: \;\; 8 \text{ and } -1").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"2x^2 + 8x - x - 4 = 0").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"2x(x + 4) - 1(x + 4) = 0").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"(2x - 1)(x + 4) = 0").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = MathTex(r"x = \tfrac{1}{2} \;\text{ or }\; x = -4").scale(1.0).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_2): shape 4 — difference of squares, both roots
        self.next_band(5)
        b5_l1 = MathTex(r"9x^2 - 49 = (3x - 7)(3x + 7) = 0").scale(1.0).shift(band_shift(5) + UP * 1.8)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"x = \tfrac{7}{3} \;\text{ or }\; x = -\tfrac{7}{3}").scale(1.05).shift(band_shift(5) + UP * 0.8)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_wrong = MathTex(r"25x^2 = 4 \;\Rightarrow\; x = \tfrac{2}{5} \text{ only}").scale(1.0).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l3 = MathTex(r"x = \tfrac{2}{5} \;\text{ or }\; x = -\tfrac{2}{5}").scale(1.05).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex(r"Each bracket on its own line; at most TWO solutions").scale(0.9).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_3): fractions — restrictions first
        self.next_band(6)
        b6_title = Tex(r"Solve $x + \tfrac{10}{x} = 7$").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Restriction FIRST: $x \neq 0$").scale(1.0).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2)
        b6_l2 = MathTex(r"\times x: \quad x^2 + 10 = 7x").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"x^2 - 7x + 10 = 0 \;\Rightarrow\; (x-2)(x-5) = 0").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"x = 2 \;\text{ or }\; x = 5 \quad \text{(neither banned)}").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_3): two denominators
        self.next_band(7)
        b7_title = Tex(r"Solve $\tfrac{2}{x} + \tfrac{2}{x+3} = 1$").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"Restrictions: $x \neq 0$ and $x \neq -3$").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"\times\, x(x+3): \;\; 2(x+3) + 2x = x(x+3)").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"4x + 6 = x^2 + 3x \;\Rightarrow\; x^2 - x - 6 = 0").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = MathTex(r"(x - 3)(x + 2) = 0 \;\Rightarrow\; x = 3 \text{ or } -2").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex(r"Multiply EVERY term — the lone 1 included").scale(0.9).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_4): substitution — the repeated expression
        self.next_band(8)
        b8_title = Tex(r"$(x^2 - 2x)^2 - 11(x^2 - 2x) + 24 = 0$").scale(1.0).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\text{Let } k = x^2 - 2x").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"k^2 - 11k + 24 = (k - 8)(k - 3) = 0").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"k = 8: \; x^2 - 2x - 8 = 0 \;\Rightarrow\; x = 4 \text{ or } -2").scale(0.9).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = MathTex(r"k = 3: \; x^2 - 2x - 3 = 0 \;\Rightarrow\; x = 3 \text{ or } -1").scale(0.9).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex(r"Four solutions: $-2$, $-1$, $3$ and $4$").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_4): one linear with one quadratic
        self.next_band(9)
        b9_title = Tex(r"$x + y = 7$ \; and \; $x^2 + y^2 = 25$").scale(1.0).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"\text{From the LINEAR one: } y = 7 - x").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"x^2 + (7 - x)^2 = 25").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"2x^2 - 14x + 24 = 0 \;\Rightarrow\; x^2 - 7x + 12 = 0").scale(0.95).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"(x-3)(x-4) = 0 \;\Rightarrow\; x = 3 \text{ or } 4").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex(r"Pairs: $(3; 4)$ and $(4; 3)$ — pairing is marked").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 10 (subtopic_5): zero is the only number that talks
        self.next_band(10)
        b10_title = Tex("Zero is the only number that talks").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Takings $\times$ takings $= 0$: someone sold NOTHING").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex(r"Takings $\times$ takings $= 600$: no clue at all").scale(0.95).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"x^2 = 7x: \;\text{never divide by } x").scale(0.95).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = MathTex(r"x(x - 7) = 0 \;\Rightarrow\; x = 0 \text{ or } 7").scale(1.0).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_6): clear the fractions before you fight
        self.next_band(11)
        b11_title = Tex("Clear the fractions before you fight").scale(1.1).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex(r"Banned values first: denominators may not be zero").scale(0.9).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"x + \tfrac{10}{x} = 7 \;\xrightarrow{\times x}\; x^2 + 10 = 7x").scale(1.0).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = MathTex(r"(x - 2)(x - 5) = 0 \;\Rightarrow\; x = 2 \text{ or } 5").scale(1.0).shift(band_shift(11) + DOWN * 0.8)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2)
        b11_l4 = Tex(r"Multiply every term — the 7 as well").scale(0.95).shift(band_shift(11) + DOWN * 1.8)
        self.play(Write(b11_l4))
        self.wait(3)

        # --- Band 12 (subtopic_7): nicknames, and keeping the pairs together
        self.next_band(12)
        b12_title = Tex("Nicknames, and keeping the pairs together").scale(1.05).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12_title))
        self.wait(2)
        b12_l1 = MathTex(r"k = x^2 - 2x: \;\; k^2 - 11k + 24 = 0").scale(0.95).shift(band_shift(12) + UP * 1.2)
        self.play(Write(b12_l1))
        self.wait(2.5)
        b12_l2 = Tex(r"$k$ is an alias — swap the real chunk back in").scale(0.95).shift(band_shift(12) + UP * 0.3)
        self.play(Write(b12_l2))
        self.wait(2.5)
        b12_l3 = Tex(r"Add to 7, squares add to 25: use the simple fact").scale(0.9).shift(band_shift(12) + DOWN * 0.6)
        self.play(Write(b12_l3))
        self.wait(2)
        b12_l4 = Tex(r"Answers travel in pairs, like gloves: $(3;4)$, $(4;3)$").scale(0.9).shift(band_shift(12) + DOWN * 1.5)
        self.play(Write(b12_l4))
        self.play(Create(SurroundingRectangle(b12_l4, color=GREEN)))
        self.wait(4)
