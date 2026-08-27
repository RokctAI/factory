# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from manim import *

# Band-layout whiteboard scene: one band per teaching beat, camera moves down
# to fresh space, nothing removed. Write-only reveals on single-string
# Tex/MathTex keep the export clean. Bands cover all seven subtopics
# (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7), dwell time proportional
# to subtopics.json (210/240/250/250/170/170/170 of 1460 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FactorisingTrinomialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): expanding read backwards
        title = Tex("Factorising Trinomials").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l01 = MathTex(r"(x + 2)(x + 5) = x^2 + 7x + 10").scale(1.1).shift(UP * 0.9)
        self.play(Write(l01))
        self.wait(2)
        l02 = Tex(r"$10 = 2 \times 5$ (product), \quad $7 = 2 + 5$ (sum)").scale(1.0).shift(UP * 0.0)
        self.play(Write(l02))
        self.play(Create(SurroundingRectangle(l02, color=YELLOW)))
        self.wait(2)
        l03 = Tex(r"Factorising = expansion in reverse").scale(1.05).shift(DOWN * 1.0)
        self.play(Write(l03))
        self.wait(2)
        l04 = MathTex(r"2x^2 + 14x + 20 = 2(x^2 + 7x + 10)").scale(1.0).shift(DOWN * 2.0)
        l05 = Tex(r"Common factor FIRST, always").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(l04))
        self.wait(2)
        self.play(Write(l05))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): the hunt when a is not one
        self.next_band(1)
        b1_title = Tex(r"Factorise: $4x^2 - 4x - 15$").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"a = 4,\; b = -4,\; c = -15").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"\text{Product } a c = -60, \quad \text{Sum } b = -4").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)
        b1_l3 = Tex(r"Negative product: opposite signs; bigger one negative").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"6 \;\text{and}\; 10: \text{ difference } 4 \;\Rightarrow\; -10 \;\text{and}\; +6").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_3): split and group
        self.next_band(2)
        b2_title = Tex("Split the middle term, then group").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"4x^2 - 10x + 6x - 15").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"2x(2x - 5) + 3(2x - 5)").scale(1.1).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"Identical brackets — the method's checkpoint").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"= (2x - 5)(2x + 3)").scale(1.15).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_4): verify + sign patterns
        self.next_band(3)
        b3_title = Tex("Verify, then bank the sign patterns").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"(2x-5)(2x+3) = 4x^2 + 6x - 10x - 15").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"= 4x^2 - 4x - 15 \;\checkmark").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_m1 = Tex(r"$ac > 0$, sum $> 0$: both positive").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        b3_m2 = Tex(r"$ac > 0$, sum $< 0$: both negative").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        b3_m3 = Tex(r"$ac < 0$: opposite signs, minus on the bigger").scale(0.95).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_m1))
        self.wait(1.5)
        self.play(Write(b3_m2))
        self.wait(1.5)
        self.play(Write(b3_m3))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): two numbers that multiply and add
        self.next_band(4)
        b4_title = Tex("Two numbers that multiply and add").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex(r"Two taxi fares: R2 and R5 — add to 7, multiply to 10").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"x^2 + 7x + 10 = (x + 2)(x + 5)").scale(1.05).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        b4_l3 = Tex(r"Backwards game: product 10, sum 7 — find 2 and 5").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(2.5)

        # --- Band 5 (subtopic_6): the front number
        self.next_band(5)
        b5_title = Tex("When the number in front is not a one").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"4x^2 - 4x - 15: \;\; \text{multiply-target } 4 \times (-15) = -60").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex(r"Opposite signs, so adding means differencing").scale(0.95).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"6 \text{ and } 10 \text{ differ by } 4: \; -10 \text{ and } +6").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex(r"Check both promises: product $-60$, sum $-4$ \; ✓").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_7): split the bill, check the change
        self.next_band(6)
        b6_title = Tex("Split the bill, check your change").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"4x^2 - 10x + 6x - 15").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"2x(2x - 5) + 3(2x - 5)").scale(1.05).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"= (2x - 5)(2x + 3)").scale(1.1).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex(r"Multiply back: $4x^2 - 4x - 15$ — change correct").scale(0.95).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex(r"No pair passes both tests? Say so — that IS the answer").scale(0.9).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l5))
        self.wait(4)
