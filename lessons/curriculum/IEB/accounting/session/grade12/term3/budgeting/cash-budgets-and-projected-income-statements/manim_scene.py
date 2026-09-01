# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene for the IEB grade 12 accounting session duo
# "Cash Budgets and Projected Income Statements". One band per teaching
# beat; camera moves down, earlier work stays. Exporter-safe mobjects only;
# write-only reveals — no Transform/FadeOut/sub-part indexing on MathTex.
#
# Subtopic time shares (subtopics.json, total 1560 s):
# 230/240/240/235 expert, 195/210/210 simplifier.

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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): two forecasts, two questions ---
        title = Tex("Cash Budgets and Projections").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Projected income statement: will we be PROFITABLE?").scale(1.0).shift(UP * 1.3)
        b0_l2 = Tex("Accrual rules: earned and incurred, not paid").scale(1.0).shift(UP * 0.5)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Cash budget: will there be MONEY IN THE BANK?").scale(1.0).shift(DOWN * 0.4)
        b0_l4 = Tex("Only cash, only when it actually moves").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex(r"Receipts $-$ payments $\rightarrow$ surplus/shortfall $\rightarrow$ bank").scale(0.95).shift(DOWN * 2.1)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the boundary items ---
        self.next_band(1)
        b1_title = Tex("The boundary items every exam probes").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_wrong = Tex("Depreciation as a payment in the cash budget").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l1 = Tex("Depreciation: income statement only").scale(1.0).shift(band_shift(1) + UP * 0.3)
        b1_l2 = Tex("New scooter: cash budget in full; only its").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        b1_l3 = Tex("depreciation reaches the income statement").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex("Loan received, drawings: cash budget only").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        b1_l5 = Tex("Bad debts: income statement; cash that never arrives").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the debtors' collection schedule ---
        self.next_band(2)
        b2_title = Tex("Debtors' collection schedule — September").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Pattern: 25\% same month, 55\% next,").scale(1.0).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex(r"15\% second month, 5\% never pay").scale(1.0).shift(band_shift(2) + UP * 0.6)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex(r"Sep sales: $25\% \times 110\,000 = $ R27\,500").scale(1.0).shift(band_shift(2) + DOWN * 0.3)
        b2_l4 = Tex(r"Aug sales: $55\% \times 90\,000 = $ R49\,500").scale(1.0).shift(band_shift(2) + DOWN * 1.1)
        b2_l5 = Tex(r"Jul sales: $15\% \times 60\,000 = $ R9\,000").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.wait(2)
        b2_l6 = Tex(r"September collections $=$ R86\,000").scale(1.1).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): creditors' payment with discount ---
        self.next_band(3)
        b3_title = Tex("Creditors mirror the schedule").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Pay month after purchase, 4\% prompt discount").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"August purchases R70\,000").scale(1.05).shift(band_shift(3) + UP * 0.4)
        b3_l3 = MathTex(r"96\% \times 70\,000 = R67\,200").scale(1.1).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex(r"R2\,800 discount $=$ income earned by paying on time").scale(0.95).shift(band_shift(3) + DOWN * 1.4)
        b3_l5 = Tex(r"Only 25\% pays in-month: Lerato finances 75\%").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): assembling September's cash budget ---
        self.next_band(4)
        b4_title = Tex("Dube Cycles: cash budget for September").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Receipts: cash sales 64\,000; debtors 86\,000;").scale(0.95).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex(r"commission 5\,000 $\Rightarrow$ total R155\,000").scale(0.95).shift(band_shift(4) + UP * 0.7)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Payments: creditors 67\,200; wages 41\,000;").scale(0.95).shift(band_shift(4) + DOWN * 0.1)
        b4_l4 = Tex(r"scooter 18\,000; loan 8\,800; sundry 12\,000").scale(0.95).shift(band_shift(4) + DOWN * 0.8)
        b4_l5 = Tex(r"Total payments R147\,000").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        self.play(Write(b4_l5))
        self.wait(2)
        b4_l6 = Tex(r"Surplus R8\,000; opening $(3\,000)$; closing R5\,000").scale(0.95).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        b4_l7 = Tex("Surplus, opening, closing — chained month to month").scale(0.9).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_3): reading the budget ---
        self.next_band(5)
        b5_title = Tex("Now READ the budget").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Scooter R18\,000 $>$ month's surplus R8\,000").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("Overdraft clears in September — interest stops").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex(r"Over half the receipts flow through the schedule").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex("What if collections slip? Would the overdraft return?").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("A shortfall is INFORMATION, arriving early").scale(1.0).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): budget vs actual + ethics ---
        self.next_band(6)
        b6_title = Tex("Budget against actual: October").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Sales: budget 150\,000, actual 126\,000 $-$ down R24\,000").scale(0.9).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"Advertising: budget 6\,000, actual 1\,500").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_wrong = Tex(r"``Advertising saved R4\,500 — favourable''").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_l3 = Tex(r"False economy: saved 4\,500 to lose 24\,000").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex(r"Wages over R6\,000: explain BEFORE judging").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        b6_l5 = Tex("Ethics: padding, fantasy targets, budgets as weapons").scale(0.9).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): Karabo's two lists ---
        self.next_band(7)
        b7_title = Tex("The month written down before it happens").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("List 1: will the photography MAKE MONEY?").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("counts wear on the cameras, bookings earned").scale(0.95).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("List 2: will money be IN THE ACCOUNT on the day?").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        b7_l4 = Tex("subscription on the 1st; couple pays after the 28th").scale(0.95).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Profitable and broke are different things").scale(1.05).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        b7_l6 = Tex("Sister's R2\\,500 repaid: money in, never income").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l6))
        self.wait(3)

        # --- Band 8 (subtopic_6): when will the money arrive? ---
        self.next_band(8)
        b8_title = Tex("When will the money actually arrive?").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Invoices: Jul R6\,000, Aug R8\,000, Sep R10\,000").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex(r"$25\% \times 10\,000 = 2\,500$; $55\% \times 8\,000 = 4\,400$").scale(0.95).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex(r"$15\% \times 6\,000 = 900$ \; $\Rightarrow$ \; September R7\,800").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("September's bank balance is mostly AUGUST's work").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex(r"Print lab: pay R4\,800, keep R200 for punctuality").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        b8_l6 = Tex("Missing the discount is a cash warning light").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5))
        self.wait(2)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_7): the plan meets the month ---
        self.next_band(9)
        b9_title = Tex("The plan meets the month").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Bookings: planned 15\,000, actual 11\,800").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex(r"Posts and flyers: planned 600, spent nothing").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex(r"Saved R600, lost R3\,200 of bookings").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex(r"Travel over budget — but two extra weddings fed bookings").scale(0.9).shift(band_shift(9) + DOWN * 1.2)
        b9_l5 = Tex("Judge variances in PAIRS and in stories").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("Plan, live, compare, explain, fix, carry forward").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l6))
        self.wait(4)
