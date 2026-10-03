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
# dwell time proportional to subtopics.json (280/190/160/200/240/190/210 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ExponentialFormSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Base, Exponent and Expanded Form
        t0 = Tex(r"Base, Exponent and Expanded Form").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"2^5 = 2 \times 2 \times 2 \times 2 \times 2 = 32").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"7 \times 7 \times 7 = 7^3 \qquad 3 \times 3 \times 5 \times 5 \times 5 = 3^2 \times 5^3").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"10^4 = 10\,000 \qquad 9^1 = 9 \qquad 9^0 = 1").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Base: the number multiplied. Exponent: how many factors.").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): Negative Bases
        self.next_band(1)
        t1 = Tex(r"Negative Bases").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"(-2)^5 = (-2)(-2)(-2)(-2)(-2) = -32").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"(-2)^4 = 16 \qquad (-3)^3 = -27 \qquad (-5)^2 = 25").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Even exponent: positive. Odd exponent: negative.").scale(1.05).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Decide the sign first, then the size.").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Brackets Change the Base
        self.next_band(2)
        t2 = Tex(r"Brackets Change the Base").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"(-3)^2 = (-3)(-3) = 9").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"-3^2 = -(3 \times 3) = -9").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"(-2)^4 = 16 \qquad -2^4 = -16").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"The exponent applies only to what is immediately to its left.").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Comparing Powers
        self.next_band(3)
        t3 = Tex(r"Comparing Powers").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"2^5 = 32 > 25 = 5^2 \qquad 3^4 = 81 > 64 = 4^3").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"-2^4 < (-2)^3 < 2^3 < (-3)^2").scale(1.1).shift(band_shift(3) + UP * 0.18)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"-16 < -8 < 8 < 9").scale(1.1).shift(band_shift(3) + DOWN * 0.85)
        self.play(Write(m15))
        self.wait(2)
        m16 = MathTex(r"2^6 = 4^3 = 8^2 = 64").scale(1.1).shift(band_shift(3) + DOWN * 1.87)
        self.play(Write(m16))
        self.wait(2)
        m17 = Tex(r"Evaluate first, then compare the values.").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m17))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m17, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): Why Powers Grow So Fast
        self.next_band(4)
        t4 = Tex(r"Why Powers Grow So Fast").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m18 = Tex(r"Fold a sheet: 2, 4, 8, 16, 32 layers").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"2 \times 7 = 14 \qquad 2^7 = 128").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"3^5 = 243 \qquad 3^6 = 729").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m20))
        self.wait(2)
        m21 = Tex(r"Base: what you do each time. Exponent: how many times.").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m21))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m21, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): Negatives That Flip
        self.next_band(5)
        t5 = Tex(r"Negatives That Flip").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m22 = MathTex(r"1 \to -2 \to 4 \to -8 \to 16 \to -32").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m22))
        self.wait(2)
        m23 = Tex(r"Each multiplication by a negative flips the sign").scale(1.05).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m23))
        self.wait(2)
        m24 = MathTex(r"(-3)^4 = 81 \qquad -3^4 = -81").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m24))
        self.wait(2)
        m25 = Tex(r"Brackets protect the sign.").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
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
        m26 = MathTex(r"(-5)^3 = -125").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"-2^4 + (-2)^4 = -16 + 16 = 0").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m27))
        self.wait(2)
        m28 = MathTex(r"(-4)^3 = -64 < -27 = (-3)^3").scale(1.1).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m28))
        self.wait(2)
        m29 = Tex(r"Find the base. Decide the sign. Compute the size.").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m29))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m29, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
