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

# Band-layout whiteboard scene for the Finance and Calculation Essentials
# revision session duo. One band per teaching beat, camera-only transitions,
# add-only lifecycle, exporter-supported mobjects only. Band time apportioned
# to subtopics.json (230/235/240/245/190/190/180 of 1510 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FinanceCalculationEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): percentage tools ---
        title = Tex("Finance and Calculation Essentials").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"30\% \text{ of R}650: \; 0{,}30 \times 650 = \text{R}195").scale(1.05).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_wrong = MathTex(r"\text{Fare 20} \to 23: \; 3 \div 23 = 13{,}0\%?").scale(1.0).shift(UP * 0.0)
        self.play(Write(b0_wrong))
        self.play(Create(strike(b0_wrong)))
        self.wait(2)
        b0_l2 = MathTex(r"\frac{\text{change}}{\text{original}} \times 100 = \frac{3}{20} \times 100 = 15\%").scale(0.91).shift(DOWN * 1.2)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2)
        b0_l3 = Tex("The ORIGINAL is always the denominator").scale(1.0).shift(DOWN * 2.5)
        self.play(Write(b0_l3))
        self.wait(3)

        # --- Band 1 (subtopic_1): ratio and unit price ---
        self.next_band(1)
        b1_t = Tex("Ratio, and the best-buy division").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Mix 1 : 3 means 4 parts in total").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"2 \text{ L}: \; 0{,}5 \text{ L concentrate} + 1{,}5 \text{ L water}").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"2{,}5 \text{ kg: } 62{,}50 \div 2{,}5 = \text{R}25{,}00 \text{ per kg}").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"10 \text{ kg: } 230 \div 10 = \text{R}23{,}00 \text{ per kg}").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_ans = Tex("Big bag wins by R2,00 per kg — say the verdict").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_ans))
        self.play(Create(SurroundingRectangle(b1_ans, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): VAT forwards and in reverse ---
        self.next_band(2)
        b2_t = Tex("VAT: 15\\%, both directions").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Bookshelf: } 320 \times 1{,}15 = \text{R}368").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_wrong = MathTex(r"391 - 15\% \text{ of } 391 = 332{,}35?").scale(1.0).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l2 = MathTex(r"\text{Including VAT: } 391 \div 1{,}15 = \text{R}340").scale(1.05).shift(band_shift(2) + DOWN * 1.0)
        b2_l3 = MathTex(r"\text{VAT itself: } 391 - 340 = \text{R}51").scale(1.05).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("The tag is 115\\%, not 100\\% — divide, don't subtract").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): discount and simple interest ---
        self.next_band(3)
        b3_t = Tex("Discount, and simple interest").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"20\% \text{ off R}1\;250: \; 1\;250 \times 0{,}80 = \text{R}1\;000").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex("Discount multiplies by what is LEFT").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"\text{R3 000 at } 6\%: \; 0{,}06 \times 3\;000 = \text{R}180 \text{ per year}").scale(0.88).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = MathTex(r"4 \text{ years: } 180 \times 4 = 720 \Rightarrow \text{R}3\;720").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l3))
        self.wait(2.5)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("Simple = same interest every year, on the original").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the household budget ---
        self.next_band(4)
        b4_t = Tex("Karabo's budget: two lists, one subtraction").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Income: } 7\;400 + 500 = \text{R}7\;900").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"\text{Expenses: } 2\;800 + 1\;500 + 950 + 700 + 1\;100 = \text{R}7\;050").scale(0.8).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"7\;900 - 7\;050 = \text{R}850 \text{ surplus}").scale(1.05).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex("Food up 10\\% (R150): surplus R700 — survives,").scale(0.95).shift(band_shift(4) + DOWN * 1.8)
        b4_l5 = Tex("and SAYING so with the numbers is the mark").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the tuck stand's profit ---
        self.next_band(5)
        b5_t = Tex("The tuck stand: the same subtraction").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Profit per vetkoek: } 7{,}00 - 4{,}00 = \text{R}3{,}00").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"\text{50 sold: } 3 \times 50 = \text{R}150").scale(1.05).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("Below cost = a LOSS — write the word").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("Rent: fixed. Electricity: variable.").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        b5_l5 = Tex("Advice targets the variable items").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): bank charges ---
        self.next_band(6)
        b6_t = Tex("Bank fee: fixed R3 + 1,5\\% of the amount").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{R400: } 3 + 0{,}015 \times 400 = 3 + 6 = \text{R}9").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\text{R1 200: } 3 + 18 = \text{R}21").scale(1.05).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Always: fixed part + variable part").scale(1.05).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex("Compare options AT the amount named —").scale(0.95).shift(band_shift(6) + DOWN * 1.9)
        b6_l5 = Tex("the winner can switch as the amount grows").scale(0.95).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the tariff and its graph ---
        self.next_band(7)
        b7_t = Tex("The tariff as a graph").scale(1.2).shift(band_shift(7) + UP * 2.6)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"250 \times 2{,}20 + 60 = 550 + 60 = \text{R}610").scale(1.0).shift(band_shift(7) + UP * 1.7)
        self.play(Write(b7_l1))
        self.wait(2.5)
        org7 = band_shift(7) + DOWN * 2.6 + LEFT * 4.6
        x7 = Arrow(org7, org7 + RIGHT * 8.6, buff=0, stroke_width=4)
        y7 = Arrow(org7, org7 + UP * 3.9, buff=0, stroke_width=4)
        self.play(Create(x7), Create(y7))
        lab_x = Tex("units").scale(0.75).shift(org7 + RIGHT * 8.0 + DOWN * 0.4)
        lab_y = Tex("cost").scale(0.75).shift(org7 + UP * 3.6 + RIGHT * 0.8)
        self.play(Write(lab_x), Write(lab_y))
        t1 = Line(org7 + UP * 0.7, org7 + UP * 3.1 + RIGHT * 7.6, color=BLUE, stroke_width=5)
        t1_lab = Tex("starts at R60 — the fixed charge").scale(0.8).shift(org7 + UP * 0.9 + RIGHT * 4.8)
        self.play(Create(t1), Write(t1_lab))
        self.wait(2)
        t2 = Line(org7, org7 + UP * 3.6 + RIGHT * 6.2, color=YELLOW, stroke_width=5)
        self.play(Create(t2))
        cross = Dot(org7 + RIGHT * 3.3 + UP * 1.85, color=RED)
        cross_lab = Tex("cross = same cost").scale(0.8).shift(org7 + RIGHT * 3.5 + UP * 2.5)
        self.play(Create(cross), Write(cross_lab))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): three questions every price must answer ---
        self.next_band(8)
        b8_t = Tex("Three questions every price must answer").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = MathTex(r"\text{Really cost? } 391 \div 1{,}15 = \text{R}340").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Really special? R23,00/kg beats R25,00/kg —").scale(0.95).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("no yellow sticker changes the arithmetic").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = MathTex(r"\text{Really paid? } 3\;000 + 4 \times 180 = \text{R}3\;720").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_ans = Tex("Interest is a percentage with a clock attached").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_ans))
        self.play(Create(SurroundingRectangle(b8_ans, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the budget is a seesaw ---
        self.next_band(9)
        b9_t = Tex("The budget is a seesaw").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"7\;900 \text{ vs } 7\;050: \text{ tips to income by R}850").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("R900 phone contract: expenses R7 950 —").scale(0.95).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("deficit of R50, something must give").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Rent is bolted down; food and power slide").scale(0.95).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = MathTex(r"\text{Stand: } 350 - 200 = \text{R}150 \text{ profit}").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): traps, and the last check ---
        self.next_band(10)
        b10_t = Tex("The four traps, and the last check").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("1. Subtracting 15\\% instead of dividing by 1,15").scale(0.95).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("2. Percentage change over the NEW value").scale(0.95).shift(band_shift(10) + UP * 0.3)
        b10_l3 = Tex("3. Comparing shelf prices, not unit prices").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10_l4 = Tex("4. Arithmetic without a verdict sentence").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.wait(2)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_ans = MathTex(r"\text{Reverse it: } 340 \times 1{,}15 = 391 \; \checkmark").scale(1.0).shift(band_shift(10) + DOWN * 2.3)
        self.play(Write(b10_ans))
        self.play(Create(SurroundingRectangle(b10_ans, color=GREEN)))
        b10_l5 = Tex("Every finance answer carries its own proof").scale(0.95).shift(band_shift(10) + DOWN * 3.2)
        self.play(Write(b10_l5))
        self.wait(4)
