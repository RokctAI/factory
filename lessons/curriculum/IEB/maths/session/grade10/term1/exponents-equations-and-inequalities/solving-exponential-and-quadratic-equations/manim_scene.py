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
# to subtopics.json (220/235/230/235/185/190/185 of 1480 s).

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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): zero-product law
        title = Tex("Quadratic and Exponential Equations").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l01 = Tex(r"Product $= 0 \Rightarrow$ at least one factor $= 0$").scale(1.0).shift(UP * 0.9)
        self.play(Write(l01))
        self.play(Create(SurroundingRectangle(l01, color=YELLOW)))
        self.wait(2)
        l02 = MathTex(r"x^2 - 7x + 12 = 0 \;\Rightarrow\; (x-3)(x-4) = 0").scale(1.0).shift(UP * 0.0)
        l03 = MathTex(r"x = 3 \;\text{ or }\; x = 4").scale(1.05).shift(DOWN * 0.9)
        self.play(Write(l02))
        self.wait(2)
        self.play(Write(l03))
        self.play(Create(SurroundingRectangle(l03, color=GREEN)))
        self.wait(2)
        l04 = MathTex(r"3x^2 = 27 \;\Rightarrow\; 3(x-3)(x+3) = 0 \;\Rightarrow\; x = \pm 3").scale(0.95).shift(DOWN * 1.9)
        self.play(Write(l04))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): disguises
        self.next_band(1)
        b1_title = Tex("Quadratics in disguise").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"(x+2)(x-5) = 8 \;\Rightarrow\; x^2 - 3x - 18 = 0").scale(0.95).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"(x-6)(x+3) = 0 \;\Rightarrow\; x = 6 \text{ or } -3").scale(0.95).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"\frac{8}{x} = x - 2 \;(x \neq 0) \;\Rightarrow\; (x-4)(x+2) = 0").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_wrong = MathTex(r"x^2 = 7x \;\to\; \text{divide by } x \;\to\; x = 7").scale(0.9).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        b1_l4 = MathTex(r"x(x - 7) = 0 \;\Rightarrow\; x = 0 \text{ or } 7").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_3): same-base method
        self.next_band(2)
        b2_title = Tex("One base to rule both sides").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"2^x = 64 = 2^6 \;\Rightarrow\; x = 6").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"5^{x-2} = 125 \;\Rightarrow\; x - 2 = 3 \;\Rightarrow\; x = 5").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"4^x = 32: \; 2^{2x} = 2^5 \;\Rightarrow\; x = \tfrac{5}{2}").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = MathTex(r"3^{2x+1} = \tfrac{1}{81} = 3^{-4} \;\Rightarrow\; x = -\tfrac{5}{2}").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_4): common factor, rational exponents, context
        self.next_band(3)
        b3_title = Tex("Two harder types, one context").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"2^x + 2^{x+2} = 40: \; 2^x(1 + 4) = 40 \;\Rightarrow\; 2^x = 8, \; x = 3").scale(0.9).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"x^{3/2} = 8 \;\Rightarrow\; x = 8^{2/3} = 4").scale(0.95).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"x(x + 2) = 35 \;\Rightarrow\; (x+7)(x-5) = 0").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex(r"Reject $x = -7$ IN WRITING: width cannot be negative").scale(0.9).shift(band_shift(3) + DOWN * 1.6)
        b3_l5 = Tex(r"Bed: 5 m wide, 7 m long").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): takings of zero
        self.next_band(4)
        b4_title = Tex("Two things that multiply to nothing").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex(r"Takings R0: price was zero, or nothing sold").scale(0.95).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"Takings R80: endless stories — zero alone talks").scale(0.95).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=YELLOW)))
        self.wait(2)
        b4_l3 = MathTex(r"(x-3)(x-4) = 0 \;\Rightarrow\; x = 3 \text{ or } 4").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_6): same currency
        self.next_band(5)
        b5_title = Tex("Get everything into the same currency").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"750 g vs 1,5 kg: convert before comparing").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"4^x = 32 \;\to\; 2^{2x} = 2^5 \;\to\; x = \tfrac{5}{2}").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2)
        b5_l3 = Tex(r"Five parcels weigh 40: each weighs 8 — so $2^x = 8$, $x = 3$").scale(0.85).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2.5)

        # --- Band 6 (subtopic_7): the binned answer
        self.next_band(6)
        b6_title = Tex("The answer you threw in the bin").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_wrong = MathTex(r"x^2 = 7x \;\to\; x = 7 \;\text{only}").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_l1 = MathTex(r"x(x-7) = 0 \;\Rightarrow\; x = 0 \text{ or } x = 7").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2)
        b6_l2 = Tex(r"Never divide by the unknown — factorise instead").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex(r"And reject impossible roots out loud, with reasons").scale(0.95).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l3))
        self.wait(4)
