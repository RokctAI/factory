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
# dwell time proportional to subtopics.json (250/210/200/220/220/210/210 of
# 1520 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class NumberPropertiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Properties of Operations
        t0 = Tex(r"Properties of Operations").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"a + b = b + a \qquad a \times b = b \times a").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Commutative: ORDER does not matter").scale(1.05).shift(UP * 0.18)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"(a + b) + c = a + (b + c)").scale(1.1).shift(DOWN * 0.85)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Associative: GROUPING does not matter").scale(1.05).shift(DOWN * 1.87)
        self.play(Write(m4))
        self.wait(2)
        m5 = Tex(r"Addition and multiplication ONLY").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m5))
        self.wait(2)
        self.wait(3)

        # --- Band 1 (subtopic_1): Subtraction and division refuse
        self.next_band(1)
        t1 = Tex(r"Subtraction and division refuse").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m6 = MathTex(r"8 - 3 = 5 \quad \text{but} \quad 3 - 8 = -5").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"12 \div 4 = 3 \quad \text{but} \quad 4 \div 12 = \tfrac{1}{3}").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Anchor: $4 \times 37 \times 25$").scale(1.05).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m8))
        self.wait(2)
        m9 = MathTex(r"= 37 \times (4 \times 25) = 37 \times 100 = 3\,700").scale(1.1).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m9))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m9, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_2): The distributive law
        self.next_band(2)
        t2 = Tex(r"The distributive law").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m10 = MathTex(r"a(b + c) = ab + ac \qquad a(b - c) = ab - ac").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"25 \times 12 = 25 \times (10 + 2)").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"= 250 + 50 = 300").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        m13 = MathTex(r"7 \times 98 = 7 \times (100 - 2) = 700 - 14 = 686").scale(1.1).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m13))
        self.wait(2)
        self.wait(3)

        # --- Band 3 (subtopic_2): Run it backwards: factorise
        self.next_band(3)
        t3 = Tex(r"Run it backwards: factorise").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m14 = MathTex(r"36 \times 8 + 64 \times 8 = (36 + 64) \times 8 = 800").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m14))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m14, color=GREEN)))
        self.wait(1.5)
        m15 = MathTex(r"3 \times (4 + 5) = 12 + 5").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m15))
        self.wait(2)
        self.play(Create(strike(m15)))
        self.wait(1.5)
        m16 = MathTex(r"3 \times (4 + 5) = 12 + 15 = 27").scale(1.1).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m16))
        self.wait(2)
        m17 = Tex(r"Every term inside receives the multiplier").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m17))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_3): The identity elements
        self.next_band(4)
        t4 = Tex(r"The identity elements").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m18 = MathTex(r"a + 0 = a \qquad \text{additive identity: } 0").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"a \times 1 = a \qquad \text{multiplicative identity: } 1").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m19))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m19, color=YELLOW)))
        self.wait(1.5)
        m20 = MathTex(r"a \times 0 = 0 \qquad \text{zero PROPERTY, not identity}").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m20))
        self.wait(2)
        m21 = MathTex(r"\tfrac{3}{4} \times \tfrac{2}{2} = \tfrac{6}{8} \qquad (\tfrac{2}{2} = 1)").scale(1.1).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m21))
        self.wait(2)
        self.wait(3)

        # --- Band 5 (subtopic_4): Calculate smartly, name the law
        self.next_band(5)
        t5 = Tex(r"Calculate smartly, name the law").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m22 = MathTex(r"8 \times 125 \times 7 = (8 \times 125) \times 7 = 7\,000").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"999 \times 6 = 6\,000 - 6 = 5\,994").scale(1.1).shift(band_shift(5) + DOWN * 0.85)
        self.play(Write(m23))
        self.wait(2)
        m24 = MathTex(r"15 \times 24 = (15 \times 4) \times 6 = 60 \times 6 = 360").scale(1.1).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m24))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m24, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_4): Where the laws go next: Term 2
        self.next_band(6)
        t6 = Tex(r"Where the laws go next: Term 2").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m25 = MathTex(r"3x + 5x = (3 + 5)x = 8x \quad \text{(distributive)}").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m25))
        self.wait(2)
        m26 = MathTex(r"3(x + 2) = 3x + 6 \quad \text{(distributive)}").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"2x \times 3y = 6xy \quad \text{(commutative, associative)}").scale(1.1).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m27))
        self.wait(2)
        m28 = Tex(r"Legal step $=$ a law you can name").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m28))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): Swapping and regrouping at the till
        self.next_band(7)
        t7 = Tex(r"Swapping and regrouping at the till").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(t7))
        self.wait(1.5)
        m29 = Tex(r"3 cooldrinks then 2 chips, or chips first: same total").scale(1.05).shift(band_shift(7) + UP * 1.2)
        self.play(Write(m29))
        self.wait(2)
        m30 = MathTex(r"17 + 59 + 83 = (17 + 83) + 59 = 100 + 59 = 159").scale(1.1).shift(band_shift(7) + UP * 0.18)
        self.play(Write(m30))
        self.wait(2)
        m31 = Tex(r"Find the friends that make 100").scale(1.05).shift(band_shift(7) + DOWN * 0.85)
        self.play(Write(m31))
        self.wait(2)
        m32 = MathTex(r"4 \times 37 \times 25 = (4 \times 25) \times 37 = 3\,700").scale(1.1).shift(band_shift(7) + DOWN * 1.87)
        self.play(Write(m32))
        self.wait(2)
        m33 = Tex(r"Taking away and sharing do NOT swap").scale(1.05).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(m33))
        self.wait(2)
        self.wait(3)

        # --- Band 8 (subtopic_6): Breaking a number into easy pieces
        self.next_band(8)
        t8 = Tex(r"Breaking a number into easy pieces").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(t8))
        self.wait(1.5)
        m34 = MathTex(r"25 \times 12 \;\to\; 25 \times 10 = 250, \;\; 25 \times 2 = 50").scale(1.1).shift(band_shift(8) + UP * 1.2)
        self.play(Write(m34))
        self.wait(2)
        m35 = MathTex(r"250 + 50 = 300").scale(1.1).shift(band_shift(8) + DOWN * 0.17)
        self.play(Write(m35))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m35, color=GREEN)))
        self.wait(1.5)
        m36 = MathTex(r"7 \times 98 \;\to\; 700 - 14 = 686").scale(1.1).shift(band_shift(8) + DOWN * 1.53)
        self.play(Write(m36))
        self.wait(2)
        m37 = Tex(r"Every piece gets multiplied — check both roads meet").scale(1.05).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(m37))
        self.wait(2)
        self.wait(3)

        # --- Band 9 (subtopic_7): The do-nothing numbers
        self.next_band(9)
        t9 = Tex(r"The do-nothing numbers").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(t9))
        self.wait(1.5)
        m38 = MathTex(r"40 + 0 = 40 \qquad \text{zero: do-nothing for adding}").scale(1.1).shift(band_shift(9) + UP * 1.2)
        self.play(Write(m38))
        self.wait(2)
        m39 = MathTex(r"12 \times 1 = 12 \qquad \text{one: do-nothing for multiplying}").scale(1.1).shift(band_shift(9) + DOWN * 0.17)
        self.play(Write(m39))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m39, color=YELLOW)))
        self.wait(1.5)
        m40 = MathTex(r"12 \times 0 = 0 \qquad \text{zero WIPES OUT a product}").scale(1.1).shift(band_shift(9) + DOWN * 1.53)
        self.play(Write(m40))
        self.wait(2)
        m41 = MathTex(r"\tfrac{1}{2} \times \tfrac{2}{2} = \tfrac{2}{4} \qquad \text{multiplying by 1 in disguise}").scale(1.1).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(m41))
        self.wait(2)
        self.wait(3)
