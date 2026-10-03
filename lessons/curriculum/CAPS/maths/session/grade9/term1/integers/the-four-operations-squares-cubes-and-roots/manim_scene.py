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
# dwell time proportional to subtopics.json (210/210/230/260/180/190/190 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IntegerOperationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): adding and subtracting on the number line
        title = Tex("Operations with Integers").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        nl = Line(LEFT * 5.5 + UP * 1.2, RIGHT * 5.5 + UP * 1.2)
        self.play(Create(nl))
        for k in range(-10, 11, 2):
            d = Dot(RIGHT * k * 0.5 + UP * 1.2, radius=0.05)
            t = Tex(str(k)).scale(0.6).next_to(d, DOWN, buff=0.1)
            self.play(Create(d), Write(t), run_time=0.25)
        self.wait(1)
        l1 = MathTex(r"-7 + 3 = -4 \qquad -7 + (-3) = -10").scale(1.05).shift(DOWN * 0.1)
        l2 = MathTex(r"5 - (-3) = 5 + 3 = 8 \qquad -4 - (-6) = -4 + 6 = 2").scale(1.0).shift(DOWN * 1.0)
        l3 = MathTex(r"7 - (-8) = 15^\circ\text{C rise}").scale(1.05).shift(DOWN * 1.9)
        for m in (l1, l2, l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): the sign rules
        self.next_band(1)
        b1_title = Tex("Multiply and divide: same signs $+$, different signs $-$").scale(1.05).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"(-6)(-4) = 24 \qquad (-6)(4) = -24").scale(1.1).shift(band_shift(1) + UP * 1.3)
        b1_l2 = MathTex(r"-36 \div 9 = -4 \qquad -36 \div (-4) = 9").scale(1.1).shift(band_shift(1) + UP * 0.4)
        b1_l3 = MathTex(r"(-2)(-3)(-5) = -30 \;\text{(three negatives: odd)}").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = MathTex(r"3(-2) = -6,\; 2(-2) = -4,\; 1(-2) = -2,\; 0(-2) = 0").scale(0.95).shift(band_shift(1) + DOWN * 1.4)
        b1_l5 = MathTex(r"(-1)(-2) = 2,\; (-2)(-2) = 4 \;\text{— forced by the pattern}").scale(0.95).shift(band_shift(1) + DOWN * 2.3)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4, b1_l5):
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # --- Band 2 (subtopic_3): squares and cubes
        self.next_band(2)
        b2_title = Tex("Squares and cubes: the bracket decides").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"(-5)^2 = (-5)(-5) = 25").scale(1.1).shift(band_shift(2) + UP * 1.3)
        b2_l2 = MathTex(r"-5^2 = -(5 \times 5) = -25").scale(1.1).shift(band_shift(2) + UP * 0.4)
        b2_l3 = MathTex(r"(-3)^3 = (-3)(-3)(-3) = -27").scale(1.1).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex(r"Squares of non-zero integers: always positive. Cubes: keep the sign.").scale(0.95).shift(band_shift(2) + DOWN * 1.5)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(VGroup(b2_l1, b2_l2), color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_3): roots
        self.next_band(3)
        b3_title = Tex("Roots: the asymmetry").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\sqrt{25} = 5 \;\text{(positive root only)}").scale(1.1).shift(band_shift(3) + UP * 1.3)
        b3_l2 = MathTex(r"\sqrt{-25}\;\text{: no real value}").scale(1.1).shift(band_shift(3) + UP * 0.4)
        b3_l3 = MathTex(r"\sqrt[3]{125} = 5 \qquad \sqrt[3]{-27} = -3").scale(1.1).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex(r"Squares: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225").scale(0.85).shift(band_shift(3) + DOWN * 1.5)
        b3_l5 = Tex(r"Cubes: 1, 8, 27, 64, 125, 216").scale(0.95).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(strike(b3_l2)))
        self.wait(2)
        for m in (b3_l3, b3_l4, b3_l5):
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): the anchor expression
        self.next_band(4)
        b4_title = MathTex(r"5 - 2 \times (-3)^2 + \sqrt[3]{-8}").scale(1.3).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"= 5 - 2 \times 9 + (-2) \quad\text{(powers and roots)}").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"= 5 - 18 + (-2) \quad\text{(multiply)}").scale(1.05).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"= -13 + (-2) \quad\text{(left to right)}").scale(1.05).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = MathTex(r"= -15").scale(1.3).shift(band_shift(4) + DOWN * 1.6)
        for m in (b4_l1, b4_l2, b4_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): contrast pairs
        self.next_band(5)
        b5_title = Tex("Brackets change the answer").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"-3 + 4 \times (-2) = -3 + (-8) = -11").scale(1.05).shift(band_shift(5) + UP * 1.3)
        b5_l2 = MathTex(r"(-3 + 4) \times (-2) = 1 \times (-2) = -2").scale(1.05).shift(band_shift(5) + UP * 0.4)
        b5_l3 = MathTex(r"2 - 3^2 = -7 \qquad (2 - 3)^2 = 1").scale(1.05).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = MathTex(r"-12 \div (-4) + (-2)^3 = 3 + (-8) = -5").scale(1.05).shift(band_shift(5) + DOWN * 1.4)
        b5_l5 = MathTex(r"\sqrt{16 + 9} = \sqrt{25} = 5 \neq \sqrt{16} + \sqrt{9} = 7").scale(1.0).shift(band_shift(5) + DOWN * 2.3)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4, b5_l5):
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): money and temperature
        self.next_band(6)
        b6_title = Tex("Money and temperature: adding and taking away").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Owe R7, earn R3: $-7 + 3 = -4$").scale(1.05).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex(r"Owe R7, borrow R3: $-7 + (-3) = -10$").scale(1.05).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex(r"Hold R5, a R3 debt is cancelled: $5 - (-3) = 8$").scale(1.05).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex(r"Sutherland: $-8^\circ$ to $7^\circ$ is $7 - (-8) = 15$ degrees").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        b6_l5 = Tex("Taking away a debt feels like being given cash").scale(1.0).shift(band_shift(6) + DOWN * 2.3)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4, b6_l5):
            self.play(Write(m))
            self.wait(2.2)
        self.play(Create(SurroundingRectangle(b6_l5, color=YELLOW)))
        self.wait(1.5)

        # --- Band 7 (subtopic_6): minus times minus
        self.next_band(7)
        b7_title = Tex("Why a minus times a minus is a plus").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"$3 \times (-2) = -6$: three debts of R2").scale(1.05).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex(r"$(-3) \times (-2) = 6$: take AWAY three debts of R2").scale(1.05).shift(band_shift(7) + UP * 0.4)
        b7_l3 = MathTex(r"-6,\; -4,\; -2,\; 0,\; 2,\; 4 \;\text{(up by 2 each step)}").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("Count the minuses: even is plus, odd is minus").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        b7_l5 = MathTex(r"(-5)^2 = 25 \quad\text{but}\quad -5^2 = -25").scale(1.05).shift(band_shift(7) + DOWN * 2.3)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4, b7_l5):
            self.play(Write(m))
            self.wait(2.2)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(1.5)

        # --- Band 8 (subtopic_7): roots and the order of doing things
        self.next_band(8)
        b8_title = Tex("Roots, and jobs with priorities").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\sqrt[3]{-27} = -3 \;\checkmark \qquad \sqrt{-25}\;\text{: nothing squares to a negative}").scale(0.95).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("Powers and roots first; then multiply/divide; then add/subtract").scale(0.95).shift(band_shift(8) + UP * 0.4)
        b8_l3 = MathTex(r"5 - 2 \times (-3)^2 + \sqrt[3]{-8} = 5 - 2 \times 9 + (-2)").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = MathTex(r"= 5 - 18 - 2 = -15").scale(1.15).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = MathTex(r"\sqrt{16 + 9} = 5 \;\text{— the root is a lid over everything under it}").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        for m in (b8_l1, b8_l2, b8_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b8_l5))
        self.wait(4)
