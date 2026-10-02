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
# dwell time proportional to subtopics.json (260/200/190/200/250/220/190 of
# 1510 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MultiplyMonomialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Monomial Times Monomial
        t0 = Tex(r"Monomial Times Monomial").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"3x \times 4x^2 = 12x^3 \quad \text{coefficients multiply, exponents add}").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"-2x \times 3x = -6x^2 \qquad -2x \times -3x = 6x^2").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"(2x)^2 = 4x^2 \qquad (-3a^2)^3 = -27a^6").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Same letter: add exponents. Different letters: side by side.").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): Monomial Times Binomial
        self.next_band(1)
        t1 = Tex(r"Monomial Times Binomial").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"a(b + c) = ab + ac").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"2x(3x - 5) = 6x^2 - 10x").scale(1.1).shift(band_shift(1) + UP * 0.18)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"3(2a + 7) = 6a + 21 \quad \text{not } 6a + 7").scale(1.1).shift(band_shift(1) + DOWN * 0.85)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"4a^2(2a - 3b) = 8a^3 - 12a^2b").scale(1.1).shift(band_shift(1) + DOWN * 1.87)
        self.play(Write(m8))
        self.wait(2)
        m9 = Tex(r"An arc from the monomial to every term inside").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m9))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m9, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Negative Monomials and Trinomials
        self.next_band(2)
        t2 = Tex(r"Negative Monomials and Trinomials").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m10 = MathTex(r"-3a(a^2 - 2a + 4) = -3a^3 + 6a^2 - 12a").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"A negative monomial flips every sign inside").scale(1.05).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"-x(x - 1) = -x^2 + x").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m12))
        self.wait(2)
        m13 = MathTex(r"5(a - 2) - 2(a + 4) = 5a - 10 - 2a - 8 = 3a - 18").scale(1.1).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m13))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m13, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Geometry and Checking
        self.next_band(3)
        t3 = Tex(r"Geometry and Checking").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m14 = MathTex(r"A = 2x(3x + 2) = 6x^2 + 4x \quad \text{(two strips)}").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"P = 2(3x + 2) + 2(2x) = 10x + 4").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m15))
        self.wait(2)
        m16 = MathTex(r"(4a)^2 = 16a^2 \qquad (2b)^3 = 8b^3").scale(1.1).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m16))
        self.wait(2)
        m17 = Tex(r"Check with a = 2: exponent errors show, zero and one hide them").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m17))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m17, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): The Garden With an Unknown Side
        self.next_band(4)
        t4 = Tex(r"The Garden With an Unknown Side").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m18 = Tex(r"Breadth 2x, length 3x + 2: two strips").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"2x \times 3x = 6x^2 \qquad 2x \times 2 = 4x").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"A = 6x^2 + 4x \qquad x = 3: \; 54 + 12 = 66").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m20))
        self.wait(2)
        m21 = Tex(r"Every term in the bracket is a strip with the full breadth").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m21))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m21, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): Boxes and the Mirror
        self.next_band(5)
        t5 = Tex(r"Boxes and the Mirror").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m22 = MathTex(r"5(3p + 2n + r) = 15p + 10n + 5r").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"x(xp + 2n) = x^2p + 2xn").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m23))
        self.wait(2)
        m24 = MathTex(r"-2(3a - 4) = -6a + 8 \quad \text{every sign through the mirror}").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m24))
        self.wait(2)
        m25 = Tex(r"Did every sign change? If not, a term missed the mirror.").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m25))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m25, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): Examination Technique
        self.next_band(6)
        t6 = Tex(r"Examination Technique").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m26 = MathTex(r"3x(2x - 1) - x(x + 4) = 6x^2 - 3x - x^2 - 4x = 5x^2 - 7x").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"-2a^2(3a^2 - ab + 2b^2) = -6a^4 + 2a^3b - 4a^2b^2").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m27))
        self.wait(2)
        m28 = MathTex(r"(2x)^2 \times 3x = 4x^2 \times 3x = 12x^3").scale(1.1).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m28))
        self.wait(2)
        m29 = Tex(r"Arc to every term; sign, coefficient, exponent; collect; check with 2").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m29))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m29, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
