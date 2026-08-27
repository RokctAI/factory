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

# Band-layout whiteboard scene for "Balancing Chemical Equations" (Part 1
# Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe
# mobjects only; write-only reveals; camera moves down band by band. Band
# time apportioned to subtopics.json (220/250/230/280/160/160/170 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BalancingEquationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the equation that lies ---
        title = Tex("Balancing Chemical Equations").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"C_3H_8 + O_2 \rightarrow CO_2 + H_2O").scale(1.15).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("Left: 3 C, 8 H, 2 O").scale(1.05).shift(UP * 0.0)
        b0_l3 = Tex("Right: 1 C, 2 H, 3 O").scale(1.05).shift(DOWN * 0.8)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("as written, the equation LIES").scale(1.05).shift(DOWN * 1.7)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex("atoms are only ever REARRANGED").scale(1.05).shift(DOWN * 2.7)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): the one commandment ---
        self.next_band(1)
        b1_t = Tex("Coefficients, never subscripts").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("subscripts define IDENTITY:").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        b1_l2 = MathTex(r"H_2O \to H_2O_2 \quad \text{(now peroxide!)}").scale(1.05).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l2))
        self.play(Create(strike(b1_l2)))
        self.wait(2.5)
        b1_l3 = Tex("coefficients multiply the WHOLE formula:").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l3))
        b1_l4 = MathTex(r"4H_2O = 8\;\text{H} + 4\;\text{O}").scale(1.05).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = MathTex(r"5O_2 = 10\;\text{O atoms; no number} = 1").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the C, H, O order ---
        self.next_band(2)
        b2_t = Tex("Balance in the order C, H, O").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("C lives in ONE product; H in ONE product:").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("each settles immediately").scale(1.0).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("O sits in BOTH products and stands").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex(r"alone as O$_2$ — balance it LAST").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)
        b2_l5 = Tex("oxygen first = the classic tail-chase").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l5))
        self.play(Create(strike(b2_l5)))
        self.wait(3)

        # --- Band 3 (subtopic_3): propane balanced step by step ---
        self.next_band(3)
        b3_t = Tex("Propane, worked in the order").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{C: } 3 \Rightarrow 3CO_2").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\text{H: } 8 \div 2 \Rightarrow 4H_2O").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"\text{O demand: } 6 + 4 = 10 \Rightarrow 5O_2").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = MathTex(r"C_3H_8 + 5O_2 \rightarrow 3CO_2 + 4H_2O").scale(1.1).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the audit ---
        self.next_band(4)
        b4_t = Tex("The audit — never optional").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{C: } 3 = 3 \;\checkmark").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\text{H: } 8 = 4 \times 2 = 8 \;\checkmark").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\text{O: } 5 \times 2 = 10 = 6 + 4 \;\checkmark").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("three matches: PROVEN, not assumed").scale(1.05).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): ethane and the fraction ---
        self.next_band(5)
        b5_t = Tex("When oxygen lands on a fraction").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"C_2H_6: \; 2CO_2, \; 3H_2O").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\text{O demand: } 4 + 3 = 7 \Rightarrow \tfrac{7}{2}O_2").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("cure: double EVERY coefficient").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(1.5)
        b5_l4 = MathTex(r"2C_2H_6 + 7O_2 \rightarrow 4CO_2 + 6H_2O").scale(1.05).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        b5_l5 = MathTex(r"\text{audit: } 4{=}4, \; 12{=}12, \; 14{=}14").scale(1.0).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): smallest set + the road ahead ---
        self.next_band(6)
        b6_t = Tex("Final form: smallest whole numbers").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"2C_3H_8 + 10O_2 \rightarrow 6CO_2 + 8H_2O").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(strike(b6_l1)))
        b6_l2 = Tex("balanced but unfinished: all divide by 2").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("for 1, 5, 3, 4 nothing divides them: final").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex("next term these coefficients become").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        b6_l5 = Tex("MOLE RATIOS — stoichiometry's engine").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): nothing goes missing at the braai ---
        self.next_band(7)
        b7_t = Tex("Nothing goes missing at the braai").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("gas in + air in = smoke and steam out,").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("gram for gram — bricks rebuilt, not burned away").scale(0.95).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("every C leaves as CO$_2$; every H as water").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("if the sides do not tally, OUR counting").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        b7_l5 = Tex("is wrong — not the chemistry").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): buy more packets ---
        self.next_band(8)
        b8_t = Tex("Buy more packets, don't repack them").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("big number in front: number of packets —").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("yours to change").scale(1.0).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("little number inside: part of the label —").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex("LOCKED").scale(1.1).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = MathTex(r"4H_2O: \; 8\;\text{H and } 4\;\text{O, not } 4\;\text{and}\;4").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): easy ones first ---
        self.next_band(9)
        b9_t = Tex("Easy ones first, then the awkward one").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"\text{C: } 3 \to 3CO_2; \quad \text{H: } 8 \to 4H_2O").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"\text{O: } 6 + 4 = 10 \to 5\;\text{pairs}").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"C_3H_8 + 5O_2 \rightarrow 3CO_2 + 4H_2O").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("count out loud: 3 and 3, 8 and 8, 10 and 10").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("half a bottle? double the whole shopping list").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.wait(4)
