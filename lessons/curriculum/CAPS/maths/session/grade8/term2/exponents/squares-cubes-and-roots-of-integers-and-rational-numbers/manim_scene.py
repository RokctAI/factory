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
# dwell time proportional to subtopics.json (260/180/190/200/230/230/170 of
# 1460 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PowersRootsRationalSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Integers Revised
        t0 = Tex(r"Integers Revised").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"(-12)^2 = 144 \qquad (-5)^3 = -125").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"\sqrt{169} = 13 \qquad \sqrt[3]{-729} = -9").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"\sqrt{324} = \sqrt{2^2 \times 3^4} = 2 \times 3^2 = 18").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Prime factors turn a big root into exponent arithmetic").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): Powers of Fractions
        self.next_band(1)
        t1 = Tex(r"Powers of Fractions").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"\left(\tfrac{2}{3}\right)^2 = \tfrac{2^2}{3^2} = \tfrac{4}{9}").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"\left(\tfrac{3}{4}\right)^3 = \tfrac{27}{64} \qquad \left(-\tfrac{2}{5}\right)^3 = -\tfrac{8}{125}").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"\left(1\tfrac{1}{2}\right)^2 = \left(\tfrac{3}{2}\right)^2 = \tfrac{9}{4}").scale(1.1).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Top and bottom separately. Convert mixed numbers first.").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Roots of Fractions
        self.next_band(2)
        t2 = Tex(r"Roots of Fractions").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"\sqrt{\tfrac{25}{64}} = \tfrac{5}{8} \qquad \sqrt[3]{\tfrac{8}{27}} = \tfrac{2}{3}").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"\sqrt{\tfrac{18}{50}} = \sqrt{\tfrac{9}{25}} = \tfrac{3}{5}").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"\sqrt{2\tfrac{1}{4}} = \sqrt{\tfrac{9}{4}} = \tfrac{3}{2}").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Simplify first; convert mixed numbers first").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Decimals
        self.next_band(3)
        t3 = Tex(r"Decimals").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"0{,}3^2 = 0{,}09 \qquad 0{,}2^3 = 0{,}008").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"\sqrt{0{,}09} = 0{,}3 \qquad \sqrt{0{,}0036} = 0{,}06").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"\sqrt[3]{0{,}008} = 0{,}2 \qquad \sqrt[3]{0{,}125} = 0{,}5").scale(1.1).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Square: places double. Root: places halve (must be even).").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m16))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m16, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): The Pizza Slice Squared
        self.next_band(4)
        t4 = Tex(r"The Pizza Slice Squared").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = Tex(r"Two thirds of two thirds: a 2 x 2 block out of a 3 x 3 grid").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"\left(\tfrac{2}{3}\right)^2 = \tfrac{4}{9} \qquad \left(\tfrac{2}{3}\right)^3 = \tfrac{8}{27}").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"\text{side} = \sqrt{\tfrac{25}{64}} = \tfrac{5}{8}").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"1\tfrac{1}{2} \times 1\tfrac{1}{2} = \tfrac{3}{2} \times \tfrac{3}{2} = 2\tfrac{1}{4}").scale(1.1).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): The Dropped Comma
        self.next_band(5)
        t5 = Tex(r"The Dropped Comma").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m21 = MathTex(r"0{,}03^2 = 0{,}0009 \neq 0{,}09 \qquad 0{,}3^2 = 0{,}09").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m21))
        self.wait(2)
        m22 = MathTex(r"\sqrt{0{,}09} = \sqrt{\tfrac{9}{100}} = \tfrac{3}{10} = 0{,}3").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"\sqrt[3]{0{,}008} = \sqrt[3]{\tfrac{8}{1\,000}} = \tfrac{2}{10} = 0{,}2").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m23))
        self.wait(2)
        m24 = Tex(r"Square your answer; do you get the original back?").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m24))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m24, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): Examination Technique
        self.next_band(6)
        t6 = Tex(r"Examination Technique").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m25 = MathTex(r"\left(-\tfrac{3}{4}\right)^2 = \tfrac{9}{16} \qquad \sqrt{1\tfrac{9}{16}} = \sqrt{\tfrac{25}{16}} = \tfrac{5}{4}").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m25))
        self.wait(2)
        m26 = MathTex(r"\sqrt[3]{-0{,}027} = -0{,}3 \qquad 0{,}5^2 + \sqrt{0{,}16} = 0{,}25 + 0{,}4 = 0{,}65").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"\sqrt{\tfrac{4}{9}} \times \sqrt[3]{\tfrac{27}{8}} = \tfrac{2}{3} \times \tfrac{3}{2} = 1").scale(1.1).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m27))
        self.wait(2)
        m28 = Tex(r"Convert, decide the sign, top and bottom separately, simplify").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m28))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m28, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
