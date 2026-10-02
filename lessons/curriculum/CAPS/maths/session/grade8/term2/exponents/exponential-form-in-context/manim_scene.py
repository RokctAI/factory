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
# dwell time proportional to subtopics.json (270/200/200/210/260/220/190 of
# 1550 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ExponentsInContextSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Repeated Doubling and Tripling
        t0 = Tex(r"Repeated Doubling and Tripling").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"\text{cells after } h \text{ hours} = 2^h \qquad 2^6 = 64").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"\text{start} \times \text{factor}^n: \quad 5 \times 2^6 = 320").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"3^5 = 243 \qquad 2^9 = 512 \Rightarrow 9 \text{ hours}").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Exponent = number of periods, not number of hours").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): Squares and Cubes in Geometry
        self.next_band(1)
        t1 = Tex(r"Squares and Cubes in Geometry").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"A = s^2 \qquad V = e^3").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"s = \sqrt{6\,400} = 80 \text{ m} \qquad e = \sqrt[3]{343} = 7 \text{ cm}").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"\text{surface area} = 6 \times 7^2 = 294 \text{ cm}^2").scale(1.1).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"(2s)^2 = 4s^2 \qquad (3e)^3 = 27e^3").scale(1.1).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Scientific Notation in Context
        self.next_band(2)
        t2 = Tex(r"Scientific Notation in Context").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"6{,}2 \times 10^7 \times 2 \times 10^2 = 12{,}4 \times 10^9 = 1{,}24 \times 10^{10}").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"\frac{1{,}5 \times 10^8}{3 \times 10^5} = 0{,}5 \times 10^3 = 500 \text{ s}").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"3 \times 10^6 + 5 \times 10^5 = 3 \times 10^6 + 0{,}5 \times 10^6 = 3{,}5 \times 10^6").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Multiply: first factors, then add exponents, then normalise").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Growth by a Fixed Factor
        self.next_band(3)
        t3 = Tex(r"Growth by a Fixed Factor").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"1\,000 \times 1{,}1^3 = 1\,000 \times 1{,}331 = 1\,331").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"8\,000 \times 3^3 = 216\,000 \qquad 320 \div 2^3 = 40").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"\left(\tfrac{12}{0{,}5}\right)^2 = 24^2 = 576 \text{ tiles}").scale(1.1).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = MathTex(r"\left(\tfrac{0{,}6}{0{,}2}\right)^3 = 3^3 = 27 \text{ boxes}").scale(1.1).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m16))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m16, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): The Chessboard of Rice
        self.next_band(4)
        t4 = Tex(r"The Chessboard of Rice").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = Tex(r"Square 1: 1 grain, square 2: 2, square 3: 4, ... square n: 2^(n-1)").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"2^{10} = 1\,024 \qquad 2^{20} \approx 10^6 \qquad 2^{30} \approx 10^9").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"2^{63} \approx 9 \times 10^{18}").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"Exponent = number of doublings = square number minus one").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): The Cube-Shaped Water Tank
        self.next_band(5)
        t5 = Tex(r"The Cube-Shaped Water Tank").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m21 = MathTex(r"1\,000 \text{ litres} = 10^6 \text{ cm}^3 \Rightarrow \text{edge} = \sqrt[3]{10^6} = 10^2 \text{ cm}").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m21))
        self.wait(2)
        m22 = MathTex(r"\sqrt[3]{8 \times 10^6} = 2 \times 10^2 \text{ cm}").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"3^2 - 2^2 = 9 - 4 = 5 \text{ m}^2 \text{ of paving}").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m23))
        self.wait(2)
        m24 = MathTex(r"\sqrt{2{,}25} = 1{,}5 \text{ m}").scale(1.1).shift(band_shift(5) + DOWN * 2.9)
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
        m25 = MathTex(r"40 \times 2^6 = 2\,560").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m25))
        self.wait(2)
        m26 = MathTex(r"\sqrt[3]{1\,728} = 12 \qquad 12^2 = 144 \text{ cm}^2").scale(1.1).shift(band_shift(6) + UP * 0.18)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"\frac{6 \times 10^{24}}{7 \times 10^{22}} \approx 0{,}86 \times 10^2 \approx 86").scale(1.1).shift(band_shift(6) + DOWN * 0.85)
        self.play(Write(m27))
        self.wait(2)
        m28 = MathTex(r"1{,}5^2 = 2{,}25").scale(1.1).shift(band_shift(6) + DOWN * 1.87)
        self.play(Write(m28))
        self.wait(2)
        m29 = Tex(r"Base, exponent, direction, calculate, units").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m29))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m29, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
