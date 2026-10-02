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
# dwell time proportional to subtopics.json (230/190/210/190/230/220/220 of
# 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DividingDecimalsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Dividing Decimals
        t0 = Tex(r"Dividing Decimals").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"4{,}8 \div 0{,}6 = \frac{4{,}8}{0{,}6} = \frac{48}{6} = 8").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"0{,}144 \div 1{,}2 = \frac{1{,}44}{12} = 0{,}12").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"2{,}5 \div 0{,}04 = \frac{250}{4} = 62{,}5").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Scale both until the divisor is a whole number").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): The Anchor
        self.next_band(1)
        t1 = Tex(r"The Anchor").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"7{,}35 \div 0{,}5 = \frac{73{,}5}{5} = 14{,}7").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"\text{check: } 14{,}7 \times 0{,}5 = 7{,}35").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"3{,}6 \div 8 = 0{,}45 \qquad 9 \div 0{,}75 = \frac{900}{75} = 12").scale(1.1).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Quotient times divisor must give the dividend").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Powers of Ten and Size
        self.next_band(2)
        t2 = Tex(r"Powers of Ten and Size").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"347 \div 100 = 3{,}47 \qquad 3{,}47 \div 0{,}1 = 34{,}7").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = Tex(r"A small divisor fits many times: bigger answer").scale(1.05).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"8{,}4 \div 0{,}02 = \frac{840}{2} = 420 \qquad 0{,}9 \div 0{,}3 = 3").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"-4{,}8 \div (-0{,}6) = 8").scale(1.1).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Recurring and Technique
        self.next_band(3)
        t3 = Tex(r"Recurring and Technique").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"2 \div 0{,}3 = \frac{20}{3} = 6{,}\dot{6} \approx 6{,}67").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"0{,}7 \div 0{,}12 = \frac{70}{12} = 5{,}8\dot{3} \approx 5{,}83").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"Estimate, scale both, divide in line, check, round last").scale(1.05).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Scaling only the divisor is the classic error").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m16))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m16, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): How Many Halves?
        self.next_band(4)
        t4 = Tex(r"How Many Halves?").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"\text{halves in } 7{,}35: \quad 7{,}35 \div 0{,}5 = 14{,}7").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"4{,}8 \div 0{,}6: \quad 48 \text{ tenths} \div 6 \text{ tenths} = 8").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"2{,}5 \div 0{,}04: \quad 250 \div 4 = 62{,}5").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"Small pieces fit many times").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): Unit Prices
        self.next_band(5)
        t5 = Tex(r"Unit Prices").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m21 = MathTex(r"86{,}1 \div 3{,}5 = \frac{861}{35} = 24{,}60").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m21))
        self.wait(2)
        m22 = MathTex(r"1\,011{,}5 \div 23{,}8 = \frac{10\,115}{238} = 42{,}5 \text{ L}").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"12 \div 0{,}75 = 16 \qquad 18 \div 1{,}2 = 15").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m23))
        self.wait(2)
        m24 = Tex(r"Total divided by amount gives the unit price").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m24))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m24, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): Scale Both or Neither
        self.next_band(6)
        t6 = Tex(r"Scale Both or Neither").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m25 = MathTex(r"4{,}8 \div 0{,}6 = 48 \div 6 = 8 \qquad \text{not } 4{,}8 \div 6 = 0{,}8").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m25))
        self.wait(2)
        m26 = MathTex(r"73{,}5 \div 5 = 14{,}7 \quad \text{comma stays in line}").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"20 \div 3 = 6{,}666\ldots \approx 6{,}67").scale(1.1).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m27))
        self.wait(2)
        m28 = Tex(r"Direction, scale both, divide, check").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m28))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m28, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
