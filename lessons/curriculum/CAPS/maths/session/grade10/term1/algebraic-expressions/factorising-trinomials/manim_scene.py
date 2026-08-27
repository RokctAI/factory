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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing removed.
# Write-only reveals on single-string Tex/MathTex keep the export clean. Bands
# cover all seven subtopics (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# with dwell time proportional to subtopics.json
# (210/240/250/250/170/170/170 of 1460 s).

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
        # --- Band 0 (subtopic_1): expanding reversed = factorising
        title = Tex("Factorising Trinomials").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l01 = MathTex(r"(x+2)(x+4) = x^2 + 6x + 8").scale(1.15).shift(UP * 0.9)
        self.play(Write(l01))
        self.wait(2)
        l02 = MathTex(r"8 = 2 \times 4, \quad 6 = 2 + 4").scale(1.15).shift(DOWN * 0.1)
        self.play(Write(l02))
        self.wait(2)
        l03 = Tex(r"Hunt: product $= c$, sum $= b$").scale(1.1).shift(DOWN * 1.1)
        self.play(Write(l03))
        self.wait(2)
        l04 = Tex(r"Common factor FIRST:").scale(1.05).shift(DOWN * 2.0)
        l05 = MathTex(r"3x^2 + 18x + 24 = 3(x^2 + 6x + 8)").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(l04))
        self.play(Write(l05))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): the anchor problem, a not 1 — setup
        self.next_band(1)
        b1_title = Tex(r"Factorise fully: $6x^2 - 7x - 3$").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"a = 6, \quad b = -7, \quad c = -3").scale(1.15).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"\text{Product } = a \times c = 6 \times (-3) = -18").scale(1.1).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"\text{Sum } = b = -7").scale(1.1).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l2))
        self.wait(2.5)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex(r"Product negative $\Rightarrow$ opposite signs").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        b1_l5 = Tex(r"Sum negative $\Rightarrow$ bigger number is negative").scale(1.05).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the factor-pair hunt
        self.next_band(2)
        b2_title = Tex("Hunt the pair (difference must be 7)").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"1 \text{ and } 18: \text{ difference } 17").scale(1.1).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"2 \text{ and } 9: \text{ difference } 7 \;\checkmark").scale(1.1).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"3 \text{ and } 6: \text{ difference } 3").scale(1.1).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l1))
        self.wait(1.5)
        self.play(Write(b2_l2))
        self.wait(1.5)
        self.play(Write(b2_l3))
        self.wait(1.5)
        b2_l4 = MathTex(r"\text{The pair: } -9 \text{ and } +2").scale(1.15).shift(band_shift(2) + DOWN * 1.7)
        b2_l5 = MathTex(r"-9 \times 2 = -18, \quad -9 + 2 = -7").scale(1.1).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): split the middle term, group
        self.next_band(3)
        b3_title = Tex("Split the middle term").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"-7x = -9x + 2x").scale(1.1).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"6x^2 - 9x + 2x - 3").scale(1.15).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"6x^2 - 9x = 3x(2x - 3)").scale(1.1).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = MathTex(r"2x - 3 = 1(2x - 3)").scale(1.1).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex(r"Matching brackets — the checkpoint").scale(1.05).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): factor the bracket out
        self.next_band(4)
        b4_l0 = MathTex(r"3x(2x-3) + 1(2x-3)").scale(1.15).shift(band_shift(4) + UP * 2.0)
        self.play(Write(b4_l0))
        self.wait(2)
        b4_l1 = MathTex(r"= (2x - 3)(3x + 1)").scale(1.2).shift(band_shift(4) + UP * 0.9)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2.5)
        b4_l2 = Tex(r"Other split order, same answer:").scale(1.05).shift(band_shift(4) + DOWN * 0.4)
        b4_l3 = MathTex(r"6x^2 + 2x - 9x - 3").scale(1.05).shift(band_shift(4) + DOWN * 1.3)
        b4_l4 = MathTex(r"2x(3x+1) - 3(3x+1) = (3x+1)(2x-3)").scale(1.0).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l2))
        self.wait(1.5)
        self.play(Write(b4_l3))
        self.wait(1.5)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): verify + sign patterns
        self.next_band(5)
        b5_title = Tex("Verify by expanding").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"(2x-3)(3x+1) = 6x^2 + 2x - 9x - 3").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"= 6x^2 - 7x - 3 \;\checkmark").scale(1.1).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_s1 = Tex(r"$ac > 0$, sum $> 0$: both positive").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        b5_s2 = Tex(r"$ac > 0$, sum $< 0$: both negative").scale(1.05).shift(band_shift(5) + DOWN * 1.6)
        b5_s3 = Tex(r"$ac < 0$: opposite signs, sum's sign on the bigger").scale(1.0).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_s1))
        self.wait(1.5)
        self.play(Write(b5_s2))
        self.wait(1.5)
        self.play(Write(b5_s3))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the full method + boundary
        self.next_band(6)
        b6_title = Tex("The seven-step method").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_s1 = Tex(r"1. Common factor first \quad 2. Name $a, b, c$ with signs").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_s2 = Tex(r"3. Product $a \times c$, sum $b$ \quad 4. Read the signs").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_s3 = Tex(r"5. Hunt the pair \quad 6. Split and group").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        b6_s4 = Tex(r"7. Verify by expanding; factorise fully").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        for m in (b6_s1, b6_s2, b6_s3, b6_s4):
            self.play(Write(m))
            self.wait(1.5)
        b6_note = Tex(r"No pair passes both tests? Irreducible — say so").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_note))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): two numbers that multiply and add
        self.next_band(7)
        b7_title = Tex("Two numbers that multiply and add").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"R2 and R4 airtime: together R6, multiplied 8").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"x^2 + 6x + 8: \;\text{ multiply to } 8, \text{ add to } 6").scale(1.05).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"2 \times 4 = 8, \quad 2 + 4 = 6").scale(1.1).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = MathTex(r"x^2 + 6x + 8 = (x+2)(x+4)").scale(1.1).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        b7_l5 = Tex(r"Shared factor first: $3x^2+18x+24 = 3(x^2+6x+8)$").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): number in front is not one
        self.next_band(8)
        b8_title = Tex("When the number in front is not a one").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"6x^2 - 7x - 3").scale(1.15).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"Multiply-target: $6 \times (-3) = -18$").scale(1.05).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex(r"Add-target: $-7$").scale(1.05).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex(r"Signs say: one plus, one minus; minus on the bigger").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = MathTex(r"2 \text{ and } 9 \text{ differ by } 7: \;\; -9 \text{ and } +2").scale(1.05).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): splitting the bill, checking change
        self.next_band(9)
        b9_title = Tex("Split the bill, check your change").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"6x^2 - 9x + 2x - 3").scale(1.1).shift(band_shift(9) + UP * 1.2)
        b9_l2 = MathTex(r"3x(2x - 3) + 1(2x - 3)").scale(1.1).shift(band_shift(9) + UP * 0.3)
        b9_l3 = MathTex(r"= (2x - 3)(3x + 1)").scale(1.15).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex(r"Multiply back: $6x^2 + 2x - 9x - 3$ — all there").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        b9_l5 = Tex(r"No pair works? ``It does not factorise'' is the answer").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.wait(2.5)
        self.play(Write(b9_l5))
        self.wait(4)
