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

# BAND LAYOUT: sequential vertical bands, one frame-height each; the camera
# moves down between teaching steps and nothing is ever removed. Only
# exporter-supported mobjects (Tex/MathTex, Line, Rectangle/
# SurroundingRectangle) with write-only reveals — no sub-part transforms.
# Every calculation is built line by line in SA currency format.
#
# Mirrors script.md across the seven subtopics of the duo (Part 1 — Expert:
# subtopics 1-4; Part 2 — Simplifier: 5-7); band time proportional to
# subtopics.json.

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


class VatDiscountSimpleInterestSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): VAT forwards ---
        title = Tex("VAT, Discount and Simple Interest").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("VAT: 15\\%, collected for SARS").scale(1.0).shift(UP * 1.2)
        self.play(Write(l01))
        self.wait(2)
        l02 = Tex("Exclusive $\\to$ inclusive: multiply").scale(1.0).shift(UP * 0.3)
        self.play(Write(l02))
        self.wait(1.5)
        l03 = MathTex(r"840 \times 0{,}15 = 126").scale(1.05).shift(DOWN * 0.6)
        l04 = MathTex(r"840 \times 1{,}15 = 966").scale(1.05).shift(DOWN * 1.5)
        self.play(Write(l03))
        self.wait(2)
        self.play(Write(l04))
        self.play(Create(SurroundingRectangle(l04, color=GREEN)))
        l05 = Tex("Shelf prices in SA are ALWAYS inclusive").scale(0.95).shift(DOWN * 2.5)
        self.play(Write(l05))
        self.wait(3)

        # --- Band 1 (subtopic_1): VAT backwards ---
        self.next_band(1)
        b1_t = Tex("Backwards: divide, never subtract").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Slip shows R1 069,50 including VAT").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"1\,069{,}50 \div 1{,}15 = 930{,}00").scale(1.05).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = MathTex(r"\text{VAT: } 1\,069{,}50 - 930 = 139{,}50").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        b1_l4 = MathTex(r"\text{Check: } 930 \times 0{,}15 = 139{,}50").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Subtracting 15\\% removes too much").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_1): the basket and the zero-rated list ---
        self.next_band(2)
        b2_t = Tex("The basket: zero-rated vs standard").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("Zero-rated: rice 145 + eggs 55 + veg 48 = R248").scale(0.9).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("Standard: 62,50 + 41,00 + 34,50 = R138").scale(0.9).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"138 \div 1{,}15 = 120 \;\Rightarrow\; \text{VAT} = 18").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = MathTex(r"\text{Trap: } 0{,}15 \times 386 = 57{,}90 \;\; \text{(wrong)}").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Separate zero-rated items FIRST").scale(0.95).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): discount, and discounts that chain ---
        self.next_band(3)
        b3_t = Tex("Discount: what comes off, and off what").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"780 \times 0{,}75 = 585 \;\; \text{(25\% off)}").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"15\% \text{ then } 10\%: \; 780 \times 0{,}85 = 663").scale(0.95).shift(band_shift(3) + UP * 0.3)
        b3_l3 = MathTex(r"663 \times 0{,}90 = 596{,}70").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"0{,}85 \times 0{,}90 = 0{,}765 \Rightarrow 23{,}5\% \text{ off}").scale(0.95).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("Never 25\\% — chains multiply, not add").scale(0.95).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): simple interest forwards ---
        self.next_band(4)
        b4_t = Tex("Simple interest: growth in a straight line").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("R6 000 at 6,5\\% per year, 4 years").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\text{Interest} = 6\,000 \times 0{,}065 \times 4").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"= 390 \times 4 = 1\,560").scale(1.05).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = Tex("R390 every year — identical, a straight line").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        b4_l5 = MathTex(r"\text{Closing balance: } 6\,000 + 1\,560 = 7\,560").scale(0.95).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): simple interest backwards ---
        self.next_band(5)
        b5_t = Tex("Backwards: find the rate").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("R6 000 grows to R6 660 in 2 years").scale(1.0).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"660 = 6\,000 \times r \times 2 = 12\,000\,r").scale(1.0).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"r = 660 \div 12\,000 = 0{,}055 = 5{,}5\% \text{ p.a.}").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex("Months become years: 9 months = 0,75").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): the washing-machine decision ---
        self.next_band(6)
        b6_t = Tex("The washing-machine decision").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Sale: } 6\,800 \times 0{,}80 = 5\,440 \;\; (-1\,360)").scale(0.95).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"\text{Wait: } 5\,900 \times 0{,}05 \times 0{,}5 = 147{,}50").scale(0.95).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Wait: savings R6 047,50 vs price R6 800").scale(0.95).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = MathTex(r"\text{Short by } 752{,}50; \text{ net loss } 1\,212{,}50").scale(0.95).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("Buy during the sale — and say so in words").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the habits that earn marks ---
        self.next_band(7)
        b7_t = Tex("The habits that earn the marks").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("1. Write the multiplier or formula first").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("2. Divide to undo VAT or a discount").scale(0.95).shift(band_shift(7) + UP * 0.4)
        b7_l3 = Tex("3. Months $\\div$ 12 before substituting").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("4. Round once, at the end, to the cent").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        b7_l5 = Tex("5. Close with a sentence and a decision").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        for l in (b7_l1, b7_l2, b7_l3, b7_l4, b7_l5):
            self.play(Write(l))
            self.wait(1.6)
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the till slip at the corner shop ---
        self.next_band(8)
        b8_t = Tex("The till slip at the corner shop").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("The tax is already IN the shelf price").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"\text{Taxed part: } 138 \div 1{,}15 = 120").scale(1.0).shift(band_shift(8) + UP * 0.3)
        b8_l3 = MathTex(r"\text{VAT} = 138 - 120 = 18").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("Rice, eggs, veg: R248 the taxman never touches").scale(0.9).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Basket R386 — only R18 of it is tax").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the sale sign that says more ---
        self.next_band(9)
        b9_t = Tex("The sale sign that says more than it gives").scale(1.0).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"780 \times 0{,}85 = 663").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"663 \times 0{,}90 = 596{,}70 \;\; \text{not } 585").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2)
        b9_l3 = Tex("Second bite: R66,30 — not R78,00").scale(0.95).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("You paid R11,70 more than the signs felt like").scale(0.95).shift(band_shift(9) + DOWN * 1.5)
        b9_l5 = Tex("Buy two get one free = a third off, not half").scale(0.95).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): same growth every year, and the machine ---
        self.next_band(10)
        b10_t = Tex("Money that grows the same amount every year").scale(1.0).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = MathTex(r"6\,000 \times 0{,}065 = 390 \text{ each year}").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = MathTex(r"4 \text{ years: } 1\,560 \Rightarrow 7\,560").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("Six months is 0,5 — never 6").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = MathTex(r"\text{Machine: } 1\,360 \text{ off} \gg 147{,}50 \text{ interest}").scale(0.95).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("Buying now wins — and it is not close").scale(1.0).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l5))
        self.wait(4)
