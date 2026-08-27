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

# Band-layout whiteboard scene for "Reconciliations, Costing and VAT
# Essentials" (grade 11, term 4, revision). One band per teaching beat; the
# camera moves down and nothing is removed. Part 1 (Expert) = subtopics 1-4,
# Part 2 (Simplifier) = subtopics 5-7 in fresh bands. Exporter-safe
# primitives only; write-only reveals. Subtopic durations
# 220/220/230/230/190/200/200 of 1490 s guide the apportioning.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ToolkitRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): update your own books first ---
        title = Tex("Reconciliations, Costing and VAT Essentials").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Step 1: update YOUR books with what").scale(1.0).shift(UP * 1.2)
        b0_l2 = Tex("the statement knew first").scale(1.0).shift(UP * 0.5)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Ledger 14 730 $-$ charges 185").scale(1.0).shift(DOWN * 0.4)
        b0_l4 = Tex("$-$ debit order 515 $+$ interest 70").scale(1.0).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex("TRUE book balance: R14 100").scale(1.05).shift(DOWN * 2.0)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): both statements meet ---
        self.next_band(1)
        b1_t = Tex("Both records meet on one figure").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = Tex("Statement 12 900 $+$ deposit 4 800").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("$-$ payments 3 600 $=$ R14 100").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Creditors: ours 9 400 $+$ invoice 1 050").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = Tex("$=$ 10 450; theirs 11 950 $-$ payment").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        b1_l5 = Tex("in transit 1 500 $=$ 10 450").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(2)
        b1_l6 = Tex("Timing reconciles; errors get corrected").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): contribution and break-even ---
        self.next_band(2)
        b2_t = Tex("Contribution and the break-even line").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("Variable costs ride with each unit;").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("fixed costs stand rooted").scale(1.0).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("Price R18 $-$ variable R6 $=$ contribution R12").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"\text{Break-even} = \tfrac{9\,600}{12} = 800 \text{ units}").scale(1.05).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex("799: loss. 800: level. Past the line:").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        b2_l6 = Tex("each unit carries its whole R12 home").scale(1.0).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): profit at 1 040, proved both ways ---
        self.next_band(3)
        b3_t = Tex("Profit at 1 040 units, both ways").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = Tex("Short way: 240 past the line $\\times$ 12 $=$ R2 880").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("Long way: sales 18 720 $-$ variable 6 240").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex("$=$ contribution 12 480 $-$ fixed 9 600 $=$ R2 880").scale(0.95).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Price to R14: contribution R8;").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        b3_l5 = Tex("break-even leaps to 1 200 units").scale(1.0).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = Tex("Behaviour, contribution, then decisions").scale(0.95).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): stock systems and periodic cost of sales ---
        self.next_band(4)
        b4_t = Tex("Perpetual eye, periodic count").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = Tex("Perpetual: cost written with every sale —").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("theft visible against the count").scale(1.0).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Periodic: opening 18 000 $+$ purchases 52 000").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex("$+$ carriage 4 000 $-$ closing 20 000").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        b4_l5 = Tex("$=$ cost of sales R54 000").scale(1.05).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(2)
        b4_l6 = Tex("Cheaper, blinder: cannot tell sold from stolen").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): the debtors collection schedule ---
        self.next_band(5)
        b5_t = Tex("The debtors collection schedule").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = Tex("30\\% pay in the month; 60\\% the next;").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("10\\% never — written off").scale(1.0).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("October: 30\\% of 36 000 $=$ 10 800").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("$+$ 60\\% of September's 40 000 $=$ 24 000").scale(1.0).shift(band_shift(5) + DOWN * 1.1)
        b5_l5 = Tex("Total collected: R34 800").scale(1.05).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2)
        b5_l6 = Tex("Budgeted receipts always trail budgeted sales").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): VAT skeleton and categories ---
        self.next_band(6)
        b6_t = Tex("VAT: the collector's skeleton").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("Charge output on sales; recover input").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("on purchases; pay over the difference").scale(1.0).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Standard 15\\%; zero-rated: taxable at 0,").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("inputs recovered; exempt: outside, no inputs").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Splitter: may the seller recover its VAT?").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): both directions, and the return ---
        self.next_band(7)
        b7_t = Tex("Both directions, and the return").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_trap = Tex("VAT in R6 900 $=$ 15\\% of R6 900?").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_trap))
        self.play(Create(strike(b7_trap)))
        self.wait(2)
        b7_l1 = MathTex(r"6\,900 \times \tfrac{15}{115} = \text{R}900").scale(1.1).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(2)
        b7_l2 = Tex("Return: output 12 400 $-$ input 8 900").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        b7_l3 = Tex("$=$ R3 500 payable to SARS").scale(1.05).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Trust money: gathered for the state,").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        b7_l5 = Tex("never the vendor's to spend").scale(1.0).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): when two notebooks disagree ---
        self.next_band(8)
        b8_t = Tex("When two notebooks disagree").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Mismatch at month-end is NORMAL").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Enter what the bank knew first —").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("your notebook now says 14 100").scale(1.0).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("List what YOU knew first — the bank's").scale(1.0).shift(band_shift(8) + DOWN * 1.1)
        b8_l5 = Tex("number walks to the same 14 100").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2)
        b8_l6 = Tex("Wholesaler: both sides land on 10 450 —").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        b8_l7 = Tex("pay the meeting point, not the shout").scale(0.95).shift(band_shift(8) + DOWN * 3.4)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): the koeksister line ---
        self.next_band(9)
        b9_t = Tex("The koeksister line that pays the rent").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Sells R18; costs R6 $\\Rightarrow$ carries R12").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("Fixed life: R9 600 a month").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"\tfrac{9\,600}{12} = 800").scale(1.1).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("1 to 799: the landlord's. 800: level.").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        b9_l5 = Tex("801: the first one working for YOU").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("Sell 1 040: 240 $\\times$ 12 $=$ R2 880 profit;").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        b9_l7 = Tex("price R14 moves the line to 1 200").scale(0.95).shift(band_shift(9) + DOWN * 3.7)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.wait(3)

        # --- Band 10 (subtopic_7): the slip, the shelf, the month ahead ---
        self.next_band(10)
        b10_t = Tex("The slip, the shelf, the month ahead").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Slip: R6 900 incl. holds 15/115 $=$ R900 —").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("passing THROUGH the shop, never resting").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Shelf: 18 in, 52 bought, 4 transport,").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        b10_l4 = Tex("20 remain $\\Rightarrow$ 54 000 went out").scale(1.0).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("Month ahead: plan on 30 now, 60 later,").scale(1.0).shift(band_shift(10) + DOWN * 2.1)
        b10_l6 = Tex("and release the 10 that never comes").scale(1.0).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(2)
        b10_l7 = Tex("Reconciling, costing, counting, collecting, planning").scale(0.9).shift(band_shift(10) + DOWN * 3.6)
        self.play(Write(b10_l7))
        self.play(Create(SurroundingRectangle(b10_l7, color=GREEN)))
        self.wait(4)
