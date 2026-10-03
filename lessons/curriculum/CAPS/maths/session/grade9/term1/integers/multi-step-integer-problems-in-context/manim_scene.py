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
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IntegerContextsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): translating contexts
        title = Tex("Integers in Context").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = Tex(r"Rise, gain, deposit, earn $\to +$ \quad Fall, lose, pay, spend $\to -$").scale(0.95).shift(UP * 1.3)
        l2 = Tex(r"Below, under, overdrawn, in debt $\to$ negative START").scale(0.95).shift(UP * 0.4)
        l3 = MathTex(r"\text{Diver: } -12 + 5 - 9 = -16 \text{ m}").scale(1.05).shift(DOWN * 0.5)
        l4 = MathTex(r"\text{Difference: } 1\,753 - (-430) = 2\,183 \text{ m}").scale(1.05).shift(DOWN * 1.5)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): the anchor account
        self.next_band(1)
        b1_title = Tex("The account: one expression").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"-250 + 1\,200 - 3 \times 180 - 45").scale(1.15).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"= -250 + 1\,200 - 540 - 45").scale(1.05).shift(band_shift(1) + UP * 0.3)
        b1_l3 = MathTex(r"= 950 - 540 - 45 = 410 - 45").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = MathTex(r"= 365 \;\text{(R365 in credit)}").scale(1.2).shift(band_shift(1) + DOWN * 1.6)
        for m in (b1_l1, b1_l2, b1_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the spaza
        self.next_band(2)
        b2_title = Tex("The spaza: income minus cost").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Cost: } 24 \times 8 = 192 \;\text{(all 24 paid for)}").scale(1.05).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"\text{Income: } 20 \times 12 = 240").scale(1.05).shift(band_shift(2) + UP * 0.3)
        b2_l3 = MathTex(r"\text{Profit: } 240 - 192 = 48").scale(1.1).shift(band_shift(2) + DOWN * 0.6)
        b2_l4 = MathTex(r"\text{Only 15 sold: } 180 - 192 = -12 \;\text{(a loss)}").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_3): temperature, mean, scores, lifts
        self.next_band(3)
        b3_title = Tex("Rate times time, signed sums, scores").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"-6 + 3 \times 5 - 2 \times 4 = -6 + 15 - 8 = 1^\circ\text{C}").scale(1.0).shift(band_shift(3) + UP * 1.3)
        b3_l2 = MathTex(r"\text{Mean: } \frac{-4 + (-1) + 3 + 6 + 1}{5} = \frac{5}{5} = 1").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"\text{Quiz: } 7 \times 5 - 4 \times 3 = 23 \qquad 3 \times 5 - 8 \times 3 = -9").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = MathTex(r"\text{Lift: } -2 + 9 - 4 + 6 = 9").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.4)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): estimate and check
        self.next_band(4)
        b4_title = Tex("Estimate the sign; check by reversing").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Out: } 250 + 540 + 45 = 835 < 1\,200 \text{ in} \;\Rightarrow\; \text{positive}").scale(0.95).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"\text{Reverse: } 365 + 45 + 540 - 1\,200 = -250 \;\checkmark").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex("Layout: expression, products, walk, answer with meaning").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        for m in (b4_l1, b4_l2, b4_l3):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)

        # --- Band 5 (subtopic_4): the error museum
        self.next_band(5)
        b5_title = Tex("Error museum").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"1\,753 - 430 = 1\,323 \;\text{(wrong: the Dead Sea is below zero)}").scale(0.95).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Three debit orders charged once").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex(r"``Overdrawn by R250'' entered as $+250$: every line off by 500").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("Expired stock left out of the cost").scale(0.95).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l1))
        self.play(Create(strike(b5_l1)))
        self.wait(2)
        for m in (b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): up means plus
        self.next_band(6)
        b6_title = Tex("Up means plus, down means minus").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Find the zero: empty account, freezing, ground floor, surface").scale(0.95).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex(r"Diver: $-12 \to -7 \to -16$ m").scale(1.05).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex(r"Lift: basement 2 to floor 7 is $7 - (-2) = 9$ floors").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex(r"Opposite sides of zero: ADD the sizes, $1\,753 + 430 = 2\,183$").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_6): follow the money
        self.next_band(7)
        b7_title = Tex("Follow the money through the month").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        rows = [
            r"\text{Start: } -250",
            r"\text{Salary: } -250 + 1\,200 = 950",
            r"\text{3 debit orders: } 950 - 540 = 410",
            r"\text{Fee: } 410 - 45 = 365",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(1.0).shift(band_shift(7) + UP * (1.3 - 0.85 * i))
            self.play(Write(m))
            self.wait(2)
        b7_l5 = Tex(r"Spaza: $240 - 192 = 48$; only 15 sold: $180 - 192 = -12$").scale(0.95).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # --- Band 8 (subtopic_7): scores, degrees, check
        self.next_band(8)
        b8_title = Tex("Scores, degrees and the check at the end").scale(1.1).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\text{Quiz: } 35 - 12 = 23 \qquad 15 - 24 = -9").scale(1.0).shift(band_shift(8) + UP * 1.3)
        b8_l2 = MathTex(r"-6 + 15 = 9, \quad 9 - 8 = 1^\circ\text{C}").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex(r"Guess the sign: out 835, in 1 200 $\Rightarrow$ positive").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = MathTex(r"\text{Walk back: } 365 + 45 + 540 - 1\,200 = -250").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = Tex("Find the zero, match the words, multiply repeats, check").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=YELLOW)))
        self.wait(4)
