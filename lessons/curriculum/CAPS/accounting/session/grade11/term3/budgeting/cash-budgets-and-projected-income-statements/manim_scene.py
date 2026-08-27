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

# Band-layout whiteboard scene for the CAPS Grade 11 Term 3 duo
# "Cash Budgets and Projected Income Statements". One band per teaching
# beat; camera moves down, nothing removed. Exporter-safe primitives only;
# the debtors' collection schedule is built line by line with the script's
# exact figures. Subtopic shares: 220/240/230/230/190/200/200 of 1510 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CashBudgetsProjectionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): two documents, two questions ---
        title = Tex("Cash Budgets and Projected Statements").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Projected income statement: PROFIT,").scale(1.05).shift(UP * 1.1)
        b0_l2 = Tex("accrual basis — earned when sold").scale(1.05).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Cash budget: BANK BALANCE,").scale(1.05).shift(DOWN * 0.5)
        b0_l4 = Tex("cash basis — counted when paid").scale(1.05).shift(DOWN * 1.2)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex("Depreciation NEVER enters the cash budget").scale(1.0).shift(DOWN * 2.1)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): what each refuses, and the test ---
        self.next_band(1)
        b1_title = Tex("Items the other document refuses").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Cash budget only: capital in, drawings,").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("loans and repayments, asset purchases, VAT").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Statement only: depreciation, bad debts,").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex("accrued portions of expenses").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("Test each line: moves MONEY this month?").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        b1_l6 = Tex("Earns or consumes VALUE this month?").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the debtors' collection schedule ---
        self.next_band(2)
        b2_title = Tex("Debtors' collection: March receipts").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        b2_rule = Line(band_shift(2) + UP * 1.95 + LEFT * 3.3,
                       band_shift(2) + UP * 1.95 + RIGHT * 3.3, stroke_width=3)
        self.play(Create(b2_rule))
        self.wait(1.5)
        b2_l1 = Tex(r"Credit sales (60\%): Dec 108 000,").scale(0.95).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("Jan 120 000, Feb 150 000").scale(0.95).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex(r"50\% of Feb: 75 000 $-$ 5\% = 71 250").scale(0.95).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex(r"30\% of Jan: 36 000; 15\% of Dec: 16 200").scale(0.95).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = Tex("From debtors: R123 450").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(2)
        b2_l6 = Tex(r"+ cash sales 40\% of 300 000 = 120 000:").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
        b2_l7 = Tex("receipts from trading R243 450").scale(0.95).shift(band_shift(2) + DOWN * 3.4)
        self.play(Write(b2_l6))
        self.play(Write(b2_l7))
        self.wait(3)

        # --- Band 3 (subtopic_2): the three disciplines ---
        self.next_band(3)
        b3_title = Tex("Three disciplines the marker checks").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_wrong = Tex("Discount taken off ALL collections?").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l1 = Tex(r"Only the 50\% prompt portion earns it").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("One month collects THREE months' sales —").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        b3_l3 = Tex("lay it out as a grid, never in your head").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex(r"The 5\% bad debts never enters the cash").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        b3_l5 = Tex("budget — it is the statement's expense").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): both documents, and the divergence ---
        self.next_band(4)
        b4_title = Tex("Assemble both, watch them diverge").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Cash budget chain: receipts $-$ payments").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("= surplus/deficit; + opening = closing").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Closing feeds next month's opening;").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex("a negative closing = forecast overdraft").scale(1.0).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex("Statement: full sales in month of sale,").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        b4_l6 = Tex("down to net profit — accrual throughout").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(2)
        b4_l7 = Tex("Healthy profit AND cash deficit can coexist").scale(0.95).shift(band_shift(4) + DOWN * 3.3)
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_4): variance analysis ---
        self.next_band(5)
        b5_title = Tex("Variances: budget vs actual").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("State: item, both figures, difference in").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"rand and \%, favourable or unfavourable").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_wrong = Tex("Expense under budget = always good?").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l3 = Tex("Advertising cut may explain the sales").scale(1.0).shift(band_shift(5) + DOWN * 1.3)
        b5_l4 = Tex("shortfall next to it").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Read variances together, never singly").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): ethics and control ---
        self.next_band(6)
        b6_title = Tex("Ethics and control over forecasts").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Inflated sales to win a loan = fraud;").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("padded expenses = room to hide waste").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Controls: built with those who deliver;").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("assumptions written down; approved;").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex("actuals compared monthly; spend limits").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(3)
        b6_l6 = Tex("Unchecked = a wish; built wrong = a lie").scale(1.05).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): owed money is not money ---
        self.next_band(7)
        b7_title = Tex("Owed money is not money").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Cousin does 40 heads: R8 000 of work").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("In hand R4 000; in promises R4 000").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Earned well? Yes — R8 000. Can she buy").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("stock tomorrow? Only R4 000 says yes").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(3)
        b7_l5 = Tex("Profit and cash keep different calendars").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(2.5)
        b7_l6 = Tex("Moves money: cash budget. Eats value").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        b7_l7 = Tex("without moving money: profit forecast").scale(0.95).shift(band_shift(7) + DOWN * 3.6)
        self.play(Write(b7_l6))
        self.play(Write(b7_l7))
        self.wait(3.5)

        # --- Band 8 (subtopic_6): the collection grid ---
        self.next_band(8)
        b8_title = Tex("What will actually arrive in March").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Not March's credit sales — they start").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("paying in April. Three older months land:").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(3)
        b8_l3 = Tex(r"Half of Feb 150 000 = 75 000 $-$ 5\% = 71 250").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex(r"30\% of Jan 120 000 = 36 000;").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex(r"15\% of Dec 108 000 = 16 200").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex("Arriving from debtors: R123 450").scale(1.05).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(2)
        b8_l7 = Tex(r"The never-coming 5\% belongs to bad debts").scale(0.95).shift(band_shift(8) + DOWN * 3.5)
        self.play(Write(b8_l7))
        self.wait(3.5)

        # --- Band 9 (subtopic_7): profitable and broke ---
        self.next_band(9)
        b9_title = Tex("Profitable and broke at the same time").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Best month ever: R300 000 sold on credit").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("But stock was paid in Feb, wages in March,").scale(0.95).shift(band_shift(9) + UP * 0.3)
        b9_l3 = Tex("a bakkie bought cash, R180 000 still owed").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(3)
        b9_l4 = Tex("Profit says deserving; cash says surviving").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("Seen in advance, options are cheap: delay").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        b9_l6 = Tex("the bakkie, arrange the overdraft calmly").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(3)
        b9_l7 = Tex("Then compare budget to actual, together").scale(0.95).shift(band_shift(9) + DOWN * 3.6)
        self.play(Write(b9_l7))
        self.wait(4)
