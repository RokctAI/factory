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

# Band-layout whiteboard scene for the Profit, Loss and Financial Documents
# session duo. One band per teaching beat, camera-only transitions, add-only
# lifecycle, exporter-supported mobjects only. Band time apportioned to
# subtopics.json (210/220/210/280/180/190/190 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ProfitLossFinancialDocumentsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): definitions + the income side ---
        title = Tex("Profit, Loss and Financial Documents").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Profit = income $-$ expenditure").scale(1.15).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("Negative answer? That is a LOSS").scale(1.05).shift(UP * 0.3)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = MathTex(r"\text{Vetkoek: } 190 \times \text{R}6 = \text{R}1\;140").scale(1.1).shift(DOWN * 0.7)
        b0_l4 = MathTex(r"\text{Cooldrink: } 150 \times \text{R}10 = \text{R}1\;500").scale(1.1).shift(DOWN * 1.6)
        b0_l5 = MathTex(r"\text{Total income: } \text{R}2\;640").scale(1.1).shift(DOWN * 2.6)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the expenditure side and the profit line ---
        self.next_band(1)
        b1_t = Tex("Zanele's expenditure, then the profit line").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Ingredients: } 200 \times \text{R}2{,}50 = \text{R}500").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"\text{Cans: } 150 \times \text{R}6 = \text{R}900").scale(1.0).shift(band_shift(1) + UP * 0.4)
        b1_l3 = MathTex(r"1\;400 + 250 + 180 + 120 = \text{R}1\;950").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = MathTex(r"\text{Profit: } 2\;640 - 1\;950 = \text{R}690").scale(1.1).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex("10 unsold vetkoek: R25 spent, nothing in").scale(1.0).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the till slip and its VAT line ---
        self.next_band(2)
        b2_t = Tex("The wholesaler's till slip").scale(1.2).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_t))
        self.wait(1.5)
        slip = Rectangle(width=7.5, height=3.0).shift(band_shift(2) + UP * 0.4)
        self.play(Create(slip))
        s1 = Tex("Subtotal \\quad R780,00").scale(1.0).shift(band_shift(2) + UP * 1.2)
        s2 = Tex("VAT @ 15\\% \\quad R117,00").scale(1.0).shift(band_shift(2) + UP * 0.4)
        s3 = Tex("Total due \\quad R897,00").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.wait(2)
        self.play(Write(s3))
        self.wait(2)
        b2_l1 = MathTex(r"0{,}15 \times 780 = 117").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        b2_l2 = MathTex(r"780 + 117 = 897 \; \checkmark").scale(1.05).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the invoice and the vocabulary ---
        self.next_band(3)
        b3_t = Tex("The invoice: check the multiplication").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Qty } 150 \times \text{R}6{,}00 = \text{R}900{,}00 \; \checkmark").scale(0.98).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex("Invoice: a promise to pay (due in 30 days)").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex("Till slip: money already paid").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("Balance: what is owed now").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        b3_l5 = Tex("Statement: a month's transactions + balance").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): fixed, variable, occasional ---
        self.next_band(4)
        b4_t = Tex("Fixed, variable or occasional?").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("Fixed: same every period — rent R250").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("Variable: follows trade — stock, gas, taxi").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Occasional: rare, irregular — cooler box R350").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex("Fixed costs set the floor: R250 owed before").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        b4_l5 = Tex("a single vetkoek is sold").scale(1.0).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2)
        b4_rule = Tex("The one-line reason IS the mark").scale(1.0).shift(band_shift(4) + DOWN * 3.1).scale(1.0)
        self.play(Write(b4_rule))
        self.wait(3)

        # --- Band 5 (subtopic_4): the income-and-expenditure statement ---
        self.next_band(5)
        b5_t = Tex("The income-and-expenditure statement").scale(1.1).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_t))
        self.wait(1.5)
        page = Rectangle(width=9.6, height=4.8).shift(band_shift(5) + DOWN * 0.3)
        self.play(Create(page))
        b5_i1 = Tex("Income: vetkoek R1 140, cooldrink R1 500").scale(0.9).shift(band_shift(5) + UP * 1.5)
        b5_i2 = Tex("Total income: R2 640").scale(0.95).shift(band_shift(5) + UP * 0.7)
        self.play(Write(b5_i1))
        self.wait(2)
        self.play(Write(b5_i2))
        self.wait(2)
        mid = Line(LEFT * 4.8, RIGHT * 4.8).shift(band_shift(5) + UP * 0.2)
        self.play(Create(mid))
        b5_e1 = Tex("Expenditure: stock R1 400, rent R250,").scale(0.9).shift(band_shift(5) + DOWN * 0.4)
        b5_e2 = Tex("gas R180, transport R120").scale(0.9).shift(band_shift(5) + DOWN * 1.1)
        b5_e3 = Tex("Total expenditure: R1 950").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_e1))
        self.play(Write(b5_e2))
        self.wait(2)
        self.play(Write(b5_e3))
        self.wait(2)
        b5_ans = MathTex(r"2\;640 - 1\;950 = \text{R}690 \text{ surplus}").scale(1.05).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5_ans))
        self.play(Create(SurroundingRectangle(b5_ans, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the December deficit and the method ---
        self.next_band(6)
        b6_t = Tex("December: two trading weeks, not four").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"1\;800 - 1\;950 = -\text{R}150 \;\; \text{deficit}").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=RED)))
        self.wait(2.5)
        b6_l2 = Tex("Income halved; fixed costs stood still").scale(1.05).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_m1 = Tex("1. Sort each amount: in or out").scale(0.95).shift(band_shift(6) + DOWN * 0.8)
        b6_m2 = Tex("2. Total each side \\quad 3. Income $-$ expenditure").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        b6_m3 = Tex("4. NAME the result \\quad 5. Explain with categories").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_m1))
        self.wait(2)
        self.play(Write(b6_m2))
        self.wait(2)
        self.play(Write(b6_m3))
        self.wait(2)
        b6_trap = Tex("Trap: unsold stock is NOT income").scale(0.95).shift(band_shift(6) + DOWN * 3.1)
        self.play(Write(b6_trap))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): two shoeboxes ---
        self.next_band(7)
        b7_t = Tex("Two shoeboxes: IN and OUT").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = MathTex(r"\text{IN box: } 1\;140 + 1\;500 = \text{R}2\;640").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{OUT box: } 500 + 900 + 250 + 180 + 120 = \text{R}1\;950").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"\text{Left over: } 2\;640 - 1\;950 = \text{R}690").scale(1.05).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Making things does not earn money;").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        b7_l5 = Tex("selling them does — the R25 never came back").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): three piles of washing ---
        self.next_band(8)
        b8_t = Tex("Sort the costs like washing: three piles").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Never budge: rent R250, bumper or dead month").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Follow the crowd: flour, cans, gas, taxi").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Ambushes: the cracked cooler box, R350 once").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_ans = Tex("A loss happens when income falls").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        b8_ans2 = Tex("but the fixed pile stays the same").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_ans))
        self.play(Write(b8_ans2))
        self.play(Create(SurroundingRectangle(b8_ans2, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): one page that settles the argument ---
        self.next_band(9)
        b9_t = Tex("One page settles the argument").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Top half: everything in — R2 640").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("Bottom half: everything out — R1 950").scale(1.05).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("Last line: R690 surplus — R690 of truth").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"\text{December: } 1\;800 - 1\;950 = -\text{R}150 \text{ deficit}").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_ans = Tex("Correct side, both totals, name the bottom line").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_ans))
        self.play(Create(SurroundingRectangle(b9_ans, color=GREEN)))
        self.wait(4)
