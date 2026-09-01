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
# to subtopics.json (220/240/220/260/170/170/170 of 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LawsOfExponentsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the laws and why they are true
        title = Tex("Laws of Exponents").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l01 = MathTex(r"x^4 \times x^2 = x^6, \quad \frac{x^7}{x^3} = x^4").scale(1.0).shift(UP * 0.9)
        self.play(Write(l01))
        self.wait(2)
        l02 = MathTex(r"(x^4)^2 = x^8, \quad (3x)^2 = 9x^2").scale(1.0).shift(UP * 0.0)
        self.play(Write(l02))
        self.wait(2)
        l03 = MathTex(r"x^0 = 1 \;\text{ since } \frac{x^4}{x^4} = 1 = x^{4-4}").scale(0.95).shift(DOWN * 1.0)
        self.play(Write(l03))
        self.wait(2)
        l04 = MathTex(r"x^{-3} = \frac{1}{x^3} \;\text{ — an address, not a sign}").scale(0.95).shift(DOWN * 2.0)
        self.play(Write(l04))
        self.play(Create(SurroundingRectangle(l04, color=YELLOW)))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): the expression, brackets first
        self.next_band(1)
        b1_title = Tex(r"Simplify: $\dfrac{(3xy^2)^2 \times 2x^{-3}}{6xy^4}$").scale(1.0).shift(band_shift(1) + UP * 2.1)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"(3xy^2)^2 = 9x^2y^4").scale(1.05).shift(band_shift(1) + UP * 0.9)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"9x^2y^4 \times 2x^{-3} = 18x^{-1}y^4").scale(1.05).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"\frac{18x^{-1}y^4}{6xy^4} = 3x^{-2}y^0 = \frac{3}{x^2}").scale(1.05).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex(r"Check at $x = 1$, $y = 1$: both sides give 3").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_3): the equation
        self.next_band(2)
        b2_title = Tex(r"Solve: $3^{x+1} = 27$").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"27 = 3^3 \;\Rightarrow\; 3^{x+1} = 3^3").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"x + 1 = 3 \;\Rightarrow\; x = 2").scale(1.1).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = MathTex(r"81 = 3^4: x = 3; \quad 1 = 3^0: x = -1; \quad \tfrac{1}{9} = 3^{-2}: x = -3").scale(0.85).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex(r"Same machine for $2^{x+1} = 32$: \; $x = 4$").scale(0.95).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_4): the error museum
        self.next_band(3)
        b3_title = Tex("The error museum").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_e1 = MathTex(r"(3xy^2)^2 = 3x^2y^4").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_e1))
        self.play(Create(strike(b3_e1)))
        self.wait(1.5)
        b3_e2 = MathTex(r"x^2 \times y^3 = xy^5").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_e2))
        self.play(Create(strike(b3_e2)))
        self.wait(1.5)
        b3_e3 = MathTex(r"2x^{-3} = -2x^3").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_e3))
        self.play(Create(strike(b3_e3)))
        self.wait(1.5)
        b3_e4 = MathTex(r"3^{x+1} = 3(x+1)").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_e4))
        self.play(Create(strike(b3_e4)))
        self.wait(1.5)
        b3_l5 = Tex(r"If that were legal, $3^3$ would be 9, not 27").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): exponents just count
        self.next_band(4)
        b4_title = Tex("Exponents just count how many times").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex(r"Multiply piles: add counters. Divide: subtract.").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\frac{x^2}{x^5}: \text{ two cancel, three remain below } = \frac{1}{x^3}").scale(0.95).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex(r"The minus is an address: power moves downstairs").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=YELLOW)))
        self.wait(2.5)

        # --- Band 5 (subtopic_6): everyone pays the fare
        self.next_band(5)
        b5_title = Tex("Everyone in the taxi pays the fare").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"(3xy^2)^2: \;\; 3 \to 9, \;\; x \to x^2, \;\; y^2 \to y^4").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2)
        b5_l2 = Tex(r"Sort the washing: numbers, $x$'s, $y$'s — separate piles").scale(0.9).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"18 \div 6 = 3; \;\; x: -1 - 1 = -2; \;\; y: 4 - 4 = 0").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"\text{Answer: } \frac{3}{x^2}").scale(1.1).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_7): same language
        self.next_band(6)
        b6_title = Tex("Speak both sides in the same language").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"3^{x+1} = 27 \;\to\; 3^{x+1} = 3^3 \;\to\; x = 2").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2)
        b6_l2 = Tex(r"Translate the plain number into the left side's powers").scale(0.9).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_wrong = MathTex(r"3^{x+1} \to 3(x+1)").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_l3 = Tex(r"One language, then let the counters talk").scale(0.95).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l3))
        self.wait(4)
