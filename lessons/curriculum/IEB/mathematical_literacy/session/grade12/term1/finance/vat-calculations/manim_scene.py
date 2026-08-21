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

# Band-layout whiteboard scene for the VAT Calculations session duo.
# Part 1 — Expert: subtopics 1-4 (how VAT works, adding VAT, removing VAT,
# zero-rated goods and the till slip). Part 2 — Simplifier: subtopics 5-7
# retell the loaf-and-slice, the backwards trap and the till-slip detective.
# Durations 215/215/225/230/195/195/195 of 1470 s. Exporter-safe mobjects
# only; add-only lifecycle; camera moves down one band per teaching beat.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class VatCalculationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): how VAT works ---
        title = Tex("VAT Calculations").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Indirect tax: 15\\% on most goods and services").scale(0.95).shift(UP * 1.1)
        b0_l2 = Tex("Excl. VAT: before the tax — quotes, wholesale").scale(0.95).shift(UP * 0.2)
        b0_l3 = Tex("Incl. VAT: tax inside — shelves, till slips").scale(0.95).shift(DOWN * 0.7)
        b0_l4 = MathTex(r"\text{Exclusive } 100\% \to \text{ Inclusive } 115\%").scale(1.0).shift(DOWN * 1.7)
        b0_l5 = MathTex(r"\times 1,15 \text{ forward}, \; \div 1,15 \text{ back}").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2)); self.wait(2)
        self.play(Write(b0_l3)); self.wait(2)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b0_l5)); self.wait(3)

        # --- Band 1 (subtopic_2): adding VAT ---
        self.next_band(1)
        b1_title = Tex("Adding VAT: the friendly direction").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Quote: R9 600 excl. VAT}").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"9\;600 \times 0,15 = 1\;440").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"9\;600 + 1\;440 = 11\;040").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = MathTex(r"\text{One step: } 9\;600 \times 1,15 = 11\;040").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        b1_l5 = MathTex(r"\text{Boots: } 620 \times 1,15 = 713").scale(1.0).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b1_l4)); self.wait(2)
        self.play(Write(b1_l5)); self.wait(3)

        # --- Band 2 (subtopic_3): removing VAT ---
        self.next_band(2)
        b2_title = Tex("Removing VAT: working backwards").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"391 - 15\% \text{ of } 391 = 332,35").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Create(strike(b2_l1)))
        self.wait(1.5)
        b2_l2 = MathTex(r"391 \div 1,15 = 340,00").scale(1.05).shift(band_shift(2) + UP * 0.0)
        b2_l3 = MathTex(r"\text{VAT inside: } 391 - 340 = 51,00").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        b2_l4 = MathTex(r"\text{Check: } 340 \times 1,15 = 391").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        b2_l5 = MathTex(r"\text{Or directly: } 391 \times \tfrac{15}{115} = 51").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        self.play(Write(b2_l3)); self.wait(2)
        self.play(Write(b2_l4)); self.wait(2)
        self.play(Write(b2_l5)); self.wait(3)

        # --- Band 3 (subtopic_4): zero-rated and the till slip ---
        self.next_band(3)
        b3_title = Tex("Zero-rated basics vs starred goods").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Zero-rated: rice, samp, milk, eggs, bananas").scale(0.95).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{Zero-rated pile: } 214,60 \; (\text{no VAT})").scale(0.95).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"\text{Starred pile: } 356,50 \text{ incl. VAT}").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = MathTex(r"356,50 \times \tfrac{15}{115} = 46,50").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        b3_l5 = MathTex(r"\text{Trolley } 571,10; \text{ tax only } 46,50").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2)); self.wait(2)
        self.play(Write(b3_l3)); self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b3_l5)); self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 4 (subtopic_5): the fifteen percent that follows you ---
        self.next_band(4)
        b4_title = Tex("The loaf and the slice").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2.5)
        loaf = Rectangle(width=4.0, height=1.0).shift(band_shift(4) + LEFT * 1.5 + UP * 0.3)
        slice_r = Rectangle(width=0.6, height=1.0, color=YELLOW).shift(band_shift(4) + RIGHT * 0.8 + UP * 0.3)
        loaf_lab = MathTex(r"100\%").scale(0.9).shift(band_shift(4) + LEFT * 1.5 + UP * 0.3)
        slice_lab = MathTex(r"15\%").scale(0.7).shift(band_shift(4) + RIGHT * 0.8 + UP * 1.2)
        self.play(Create(loaf), Write(loaf_lab)); self.wait(2)
        self.play(Create(slice_r), Write(slice_lab)); self.wait(2)
        b4_l1 = MathTex(r"\text{Pay the lot: } 115\%").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        b4_l2 = MathTex(r"9\;600 \times 1,15 = 11\;040").scale(1.05).shift(band_shift(4) + DOWN * 1.8)
        b4_l3 = Tex("First ask: slice already on, or not?").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l1)); self.wait(3)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(3)
        self.play(Write(b4_l3)); self.wait(3.5)

        # --- Band 5 (subtopic_6): the backwards trap ---
        self.next_band(5)
        b5_title = Tex("The backwards trap").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2.5)
        b5_l1 = MathTex(r"391 - 58,65 = 332,35").scale(1.05).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_l1)); self.wait(2.5)
        self.play(Create(strike(b5_l1)))
        self.wait(2)
        b5_l2 = MathTex(r"391 \div 1,15 = 340").scale(1.1).shift(band_shift(5) + UP * 0.0)
        b5_l3 = MathTex(r"\text{VAT: } 391 - 340 = 51").scale(1.05).shift(band_shift(5) + DOWN * 0.9)
        b5_l4 = MathTex(r"\text{Prove it: } 340 \times 1,15 = 391").scale(1.05).shift(band_shift(5) + DOWN * 1.8)
        b5_l5 = Tex("On: times 1,15. Out: divide by 1,15.").scale(1.0).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(3)
        self.play(Write(b5_l3)); self.wait(3)
        self.play(Write(b5_l4)); self.wait(3)
        self.play(Write(b5_l5)); self.wait(3)

        # --- Band 6 (subtopic_7): the till slip detective ---
        self.next_band(6)
        b6_title = Tex("Reading the till slip like a detective").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2.5)
        b6_l1 = Tex("Starred lines carry VAT; plain lines don't").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("Brown bread free, white bread taxed").scale(1.0).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"\text{Starred: } 356,50 \times \tfrac{15}{115} = 46,50").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        b6_l4 = MathTex(r"\text{Never } \tfrac{15}{115} \text{ of } 571,10").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        b6_l5 = Tex("Sort first, then slice").scale(1.1).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l1)); self.wait(3)
        self.play(Write(b6_l2)); self.wait(3)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(3)
        self.play(Write(b6_l4)); self.wait(3)
        self.play(Write(b6_l5)); self.wait(4)
