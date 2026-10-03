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
# dwell time proportional to subtopics.json (230/220/230/230/190/180/190 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IntegerPropertiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): commutative and associative
        title = Tex("Properties of Integers and Inverses").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"a + b = b + a \qquad a \times b = b \times a").scale(1.1).shift(UP * 1.2)
        l2 = MathTex(r"(a + b) + c = a + (b + c) \qquad (ab)c = a(bc)").scale(1.05).shift(UP * 0.3)
        l3 = MathTex(r"5 - 3 = 2 \neq 3 - 5 = -2 \qquad 12 \div 4 \neq 4 \div 12").scale(1.0).shift(DOWN * 0.7)
        l4 = MathTex(r"(8 - 3) - 2 = 3 \neq 8 - (3 - 2) = 7").scale(1.0).shift(DOWN * 1.6)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(strike(l3)), Create(strike(l4)))
        l5 = Tex("Only addition and multiplication swap and regroup").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(l5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): regroup for zeros and tens
        self.next_band(1)
        b1_title = Tex("Regroup to make zeros and tens").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"-7 + 15 + 7 = (-7 + 7) + 15 = 0 + 15 = 15").scale(1.05).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"(-2) \times 17 \times (-5) = (-2)(-5) \times 17 = 10 \times 17 = 170").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"48 - 19 + 52 = 48 + (-19) + 52 = 100 + (-19) = 81").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        for m in (b1_l1, b1_l2, b1_l3):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_2): distributive property
        self.next_band(2)
        b2_title = MathTex(r"a(b + c) = ab + ac \qquad a(b - c) = ab - ac").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"7 \times 98 = 7(100 - 2) = 700 - 14 = 686").scale(1.1).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"-3(4 - 9) = -12 + 27 = 15 \quad\text{check: } -3 \times (-5) = 15").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"6 \times 23 + 6 \times 7 = 6(23 + 7) = 6 \times 30 = 180").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"-(5 - 9) = -5 + 9 = 4 \qquad 3(x + 4) = 3x + 12").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_3): identities and inverses
        self.next_band(3)
        b3_title = Tex("Identities and inverses").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"a + 0 = a \qquad a \times 1 = a").scale(1.1).shift(band_shift(3) + UP * 1.3)
        b3_l2 = MathTex(r"a + (-a) = 0: \quad 8 + (-8) = 0,\; -5 + 5 = 0").scale(1.0).shift(band_shift(3) + UP * 0.4)
        b3_l3 = MathTex(r"a \times \tfrac{1}{a} = 1: \quad 4 \times \tfrac{1}{4} = 1,\; -\tfrac{2}{3} \times -\tfrac{3}{2} = 1").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex(r"0 has no multiplicative inverse: nothing $\times\, 0 = 1$").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(b3_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_3): inverses solve equations
        self.next_band(4)
        b4_title = Tex("Inverses solve equations").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"x + 7 = 3 \;\Rightarrow\; x + 7 + (-7) = 3 + (-7) \;\Rightarrow\; x = -4").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"-5x = 35 \;\Rightarrow\; x = 35 \times \left(-\tfrac{1}{5}\right) = -7").scale(1.05).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"\text{check: } -5 \times (-7) = 35 \;\checkmark").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex(r"Subtracting 7 is adding $-7$; dividing by $-5$ is multiplying by $-\tfrac{1}{5}$").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)

        # --- Band 5 (subtopic_4): strategic use and naming
        self.next_band(5)
        b5_title = Tex("Use them on purpose; name them on demand").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"25 \times 17 \times 4 = (25 \times 4) \times 17 = 1\,700").scale(1.0).shift(band_shift(5) + UP * 1.3)
        b5_l2 = MathTex(r"48 + (-19) + 52 + 19 = 100 + 0 = 100").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l3 = MathTex(r"4(-7) + 4(-3) = 4(-10) = -40 \qquad 12 \times 11 = 120 + 12 = 132").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("Order changed: commutative. Brackets moved: associative.").scale(0.95).shift(band_shift(5) + DOWN * 1.5)
        b5_l5 = Tex("Multiplication spread or gathered: distributive. Opposites to 0: inverse.").scale(0.9).shift(band_shift(5) + DOWN * 2.4)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4, b5_l5):
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): swap it, group it
        self.next_band(6)
        b6_title = Tex("Swap it, group it").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Trolley: $17 + 34 + 49 = 100$ in any order, any grouping").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex(r"But R5 spend R3: $5 - 3 = 2$, while $3 - 5 = -2$ — no swap").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = MathTex(r"-7 + 15 + 7 \to (-7 + 7) + 15 = 15").scale(1.05).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = MathTex(r"(-2) \times 17 \times (-5) \to 10 \times 17 = 170").scale(1.05).shift(band_shift(6) + DOWN * 1.4)
        b6_l5 = Tex("Hunt for pairs that make zero or ten").scale(1.0).shift(band_shift(6) + DOWN * 2.3)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4, b6_l5):
            self.play(Write(m))
            self.wait(2.2)
        self.play(Create(SurroundingRectangle(b6_l5, color=YELLOW)))
        self.wait(1.5)

        # --- Band 7 (subtopic_6): sharing out the multiplication
        self.next_band(7)
        b7_title = Tex("Sharing out the multiplication").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"7 packets of 98: $7(100 - 2) = 700 - 14 = 686$").scale(1.05).shift(band_shift(7) + UP * 1.3)
        b7_l2 = MathTex(r"-3(4 - 9) = -12 + 27 = 15").scale(1.05).shift(band_shift(7) + UP * 0.4)
        b7_l3 = Tex(r"6 at R23 and 6 at R7: $6(23 + 7) = 6 \times 30 = 180$").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = MathTex(r"-(5 - 9) = -5 + 9 = 4 \;\text{— every sign flips}").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        b7_l5 = MathTex(r"2(3 \times 4) = 24,\; \text{not } (2 \times 3)(2 \times 4) = 48").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l5))
        self.play(Create(strike(b7_l5)))
        self.wait(2)

        # --- Band 8 (subtopic_7): undo buttons
        self.next_band(8)
        b8_title = Tex("Undo buttons: zero, one and the inverses").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Do-nothing numbers: $+\,0$ and $\times\,1$").scale(1.05).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex(r"Undo $+8$ with $+(-8)$; undo $\times 4$ with $\times \tfrac{1}{4}$").scale(1.05).shift(band_shift(8) + UP * 0.4)
        b8_l3 = MathTex(r"x + 7 = 3 \to x = 3 + (-7) = -4").scale(1.05).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = MathTex(r"-5x = 35 \to x = 35 \times (-\tfrac{1}{5}) = -7").scale(1.05).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = Tex("Zero has no undo button for multiplying — so no dividing by zero").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.play(Write(b8_l5))
        self.wait(4)
