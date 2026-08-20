# Copyright (c) 2026 RokctAI
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
# dwell time proportional to subtopics.json (220/235/230/235/185/190/185 of
# 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ExponentialAndQuadraticEquationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): zero-product law + first solve
        title = Tex("Exponential and Quadratic Equations").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        zpl = MathTex(r"A \times B = 0 \;\Rightarrow\; A = 0 \text{ or } B = 0").scale(1.1).shift(UP * 0.9)
        self.play(Write(zpl))
        self.play(Create(SurroundingRectangle(zpl, color=YELLOW)))
        self.wait(2)
        l1 = MathTex(r"x^2 - 5x + 6 = 0").scale(1.1).shift(DOWN * 0.3)
        l2 = MathTex(r"(x - 2)(x - 3) = 0").scale(1.1).shift(DOWN * 1.2)
        l3 = MathTex(r"x = 2 \quad \text{or} \quad x = 3").scale(1.1).shift(DOWN * 2.1)
        self.play(Write(l1))
        self.wait(2)
        self.play(Write(l2))
        self.wait(2)
        self.play(Write(l3))
        self.play(Create(SurroundingRectangle(l3, color=GREEN)))
        l4 = Tex(r"A product equal to 6 tells you nothing").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): keep both roots
        self.next_band(1)
        b1_title = Tex(r"Solve: $2x^2 = 8$").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"2x^2 - 8 = 0").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"2(x^2 - 4) = 0").scale(1.1).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"2(x - 2)(x + 2) = 0").scale(1.1).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = MathTex(r"x = 2 \quad \text{or} \quad x = -2").scale(1.1).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(1.5)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        b1_l5 = Tex(r"Square-rooting at the start loses $x = -2$").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): disguises — bracket = 6 and the fraction
        self.next_band(2)
        b2_title = Tex(r"Disguise: $(x+3)(x-2) = 6$").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_wrong = MathTex(r"x + 3 = 6 \;\text{ or }\; x - 2 = 6").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l1 = MathTex(r"x^2 + x - 6 = 6 \;\Rightarrow\; x^2 + x - 12 = 0").scale(1.05).shift(band_shift(2) + UP * 0.3)
        b2_l2 = MathTex(r"(x + 4)(x - 3) = 0 \;\Rightarrow\; x = -4 \text{ or } x = 3").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = MathTex(r"\frac{6}{x} = x - 5 \;\; (x \neq 0): \quad 6 = x^2 - 5x").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        b2_l4 = MathTex(r"(x-6)(x+1) = 0 \;\Rightarrow\; x = 6 \text{ or } x = -1").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): the lost solution
        self.next_band(3)
        b3_title = Tex(r"Solve: $x^2 = 5x$").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_wrong = MathTex(r"\div x: \;\; x = 5 \quad (x = 0 \text{ thrown away})").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2.5)
        b3_l1 = MathTex(r"x^2 - 5x = 0").scale(1.1).shift(band_shift(3) + UP * 0.1)
        b3_l2 = MathTex(r"x(x - 5) = 0").scale(1.1).shift(band_shift(3) + DOWN * 0.8)
        b3_l3 = MathTex(r"x = 0 \quad \text{or} \quad x = 5").scale(1.1).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        b3_rule = Tex("Never divide by the unknown — factorise it out").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_rule))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): same-base method, four solves
        self.next_band(4)
        b4_title = Tex("Exponentials: make the bases match").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"2^x = 32 = 2^5 \;\Rightarrow\; x = 5").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"3^{x+1} = 81 = 3^4 \;\Rightarrow\; x + 1 = 4, \; x = 3").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"9^x = 27: \;\; 3^{2x} = 3^3 \;\Rightarrow\; x = \tfrac{3}{2}").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = MathTex(r"5^{2x-1} = \tfrac{1}{125} = 5^{-3} \;\Rightarrow\; x = -1").scale(1.05).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex(r"Know the small powers of 2, 3 and 5 on sight").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): two-term exponential + rational exponent
        self.next_band(5)
        b5_title = Tex(r"Solve: $3^x + 3^{x+1} = 36$").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"3^x(1 + 3) = 36").scale(1.1).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"3^x = 9 = 3^2 \;\Rightarrow\; x = 2").scale(1.1).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2)
        b5_l3 = MathTex(r"x^{\frac{2}{3}} = 9").scale(1.1).shift(band_shift(5) + DOWN * 0.9)
        b5_l4 = MathTex(r"x = 9^{\frac{3}{2}} = (\sqrt{9})^3 = 27").scale(1.05).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the garden + trap museum
        self.next_band(6)
        b6_title = Tex("Garden: 3 m longer than wide, area 40 m$^2$").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"x(x + 3) = 40 \;\Rightarrow\; x^2 + 3x - 40 = 0").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = MathTex(r"(x + 8)(x - 5) = 0 \;\Rightarrow\; x = -8 \text{ or } x = 5").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex(r"Reject $x = -8$: a width cannot be negative").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex(r"Width 5 m, length 8 m").scale(1.05).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex(r"Traps: brackets $=$ non-zero, dividing by $x$,").scale(0.95).shift(band_shift(6) + DOWN * 2.3)
        b6_l6 = Tex(r"mixed bases equated, $2^x = 0$ has no solution").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): takings of zero
        self.next_band(7)
        b7_title = Tex("Two things that multiply to nothing").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"Takings R0: price was zero, or nothing sold").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"Takings R60: endless stories — zero alone talks").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"(x - 2)(x - 3) = 0").scale(1.1).shift(band_shift(7) + DOWN * 0.6)
        b7_l4 = MathTex(r"x = 2 \quad \text{or} \quad x = 3").scale(1.1).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        b7_l5 = Tex(r"Check like counting change: both leave nothing over").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): same currency
        self.next_band(8)
        b8_title = Tex("Get everything into the same currency").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"500 g vs 2 kg? Convert first: 2000 g").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"2^x = 32 = 2^5 \;\Rightarrow\; x = 5").scale(1.05).shift(band_shift(8) + UP * 0.3)
        b8_l3 = MathTex(r"9^x = 27: \;\; 3^{2x} = 3^3 \;\Rightarrow\; x = \tfrac{3}{2}").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = MathTex(r"5^{2x-1} = \tfrac{1}{125} = 5^{-3} \;\Rightarrow\; x = -1").scale(1.05).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2.5)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex(r"Know the families like phone numbers").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): the answer in the bin
        self.next_band(9)
        b9_title = Tex("The answer you threw in the bin").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_wrong = MathTex(r"x^2 = 5x, \; \div x: \;\; x = 5 \;\text{ (half the truth)}").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_wrong))
        self.play(Create(strike(b9_wrong)))
        self.wait(2)
        b9_l1 = MathTex(r"x(x - 5) = 0 \;\Rightarrow\; x = 0 \text{ or } x = 5").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.play(Create(SurroundingRectangle(b9_l1, color=GREEN)))
        self.wait(2.5)
        b9_l2 = Tex(r"The garden: $x = -8$ or $x = 5$; reject $-8$,").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        b9_l3 = Tex(r"in writing — a width cannot be negative").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex(r"Keep every root the algebra gives; reject only").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        b9_l5 = Tex(r"the ones reality refuses — out loud").scale(0.95).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(4)
