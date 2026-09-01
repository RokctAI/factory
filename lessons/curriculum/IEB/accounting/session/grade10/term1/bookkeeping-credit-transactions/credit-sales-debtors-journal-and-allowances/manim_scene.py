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

# Band-layout whiteboard scene for the credit-sales / debtors-journal session
# duo. Exporter-safe primitives only (Tex/MathTex/Line/Arrow/Rectangle/
# VGroup); write-only reveals. Band time follows subtopics.json
# (190/210/210/190/180/180/170 of 1330 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CreditSalesDebtorsJournalSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): selling on credit and the DJ ---
        title = Tex("Selling on Credit").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Goods now, money later —").scale(1.0).shift(UP * 1.2)
        l02 = Tex("the INVOICE is the debt's birth certificate").scale(0.95).shift(UP * 0.4)
        self.play(Write(l01)); self.play(Write(l02)); self.wait(2.5)
        l03 = Tex("Debtors Journal: credit sales of stock ONLY").scale(0.95).shift(DOWN * 0.6)
        self.play(Write(l03)); self.wait(2)
        l04 = Tex("Two destinations: personal accounts daily,").scale(0.95).shift(DOWN * 1.5)
        l05 = Tex("general ledger totals monthly").scale(0.95).shift(DOWN * 2.3)
        self.play(Write(l04)); self.play(Write(l05))
        self.wait(3)

        # --- Band 1 (subtopic_2): the month's credit sales ---
        self.next_band(1)
        b1_t = Tex("The month's invoices").scale(1.2).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_t)); self.wait(2)
        b1_l1 = Tex("5th, inv 81, M. Sithole: R2 400; cost R1 600").scale(0.9).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("11th, inv 82, P. Govender: R1 800; cost R1 200").scale(0.9).shift(band_shift(1) + UP * 0.6)
        b1_l3 = Tex("19th, inv 83, M. Sithole: R900; cost R600").scale(0.9).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3)); self.wait(2)
        b1_l4 = Tex("Cost = price $\\div$ 1,5 — mark-up 50\\% on cost").scale(0.9).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l4)); self.wait(2)
        b1_l5 = Tex("Daily: debit each debtor's page").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): month-end posting ---
        self.next_band(2)
        b2_t = Tex("Month end: post the totals").scale(1.15).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_t)); self.wait(2)
        b2_l1 = Tex("Sales R5 100; Cost of Sales R3 400").scale(1.0).shift(band_shift(2) + UP * 1.4)
        self.play(Write(b2_l1)); self.wait(2)
        b2_l2 = Tex("Debit Debtors Control 5 100;").scale(0.95).shift(band_shift(2) + UP * 0.5)
        b2_l3 = Tex("credit Sales 5 100").scale(0.95).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(b2_l2)); self.play(Write(b2_l3)); self.wait(2.5)
        b2_l4 = Tex("Debit Cost of Sales 3 400;").scale(0.95).shift(band_shift(2) + DOWN * 1.1)
        b2_l5 = Tex("credit Trading Stock 3 400").scale(0.95).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4)); self.play(Write(b2_l5)); self.wait(2)
        b2_l6 = Tex("Check: 8 500 = 8 500").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): return versus allowance ---
        self.next_band(3)
        b3_t = Tex("Return vs allowance — the DAJ").scale(1.15).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_t)); self.wait(2)
        b3_l1 = Tex("Credit note: the invoice's mirror").scale(1.0).shift(band_shift(3) + UP * 1.4)
        self.play(Write(b3_l1)); self.wait(2)
        b3_l2 = Tex("RETURN: goods come back —").scale(0.95).shift(band_shift(3) + UP * 0.5)
        b3_l3 = Tex("allowances R600 AND cost R400").scale(0.95).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(b3_l2)); self.play(Write(b3_l3)); self.wait(2.5)
        b3_l4 = Tex("ALLOWANCE: goods stay —").scale(0.95).shift(band_shift(3) + DOWN * 1.1)
        b3_l5 = Tex("allowances R200, cost column EMPTY").scale(0.95).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4)); self.play(Write(b3_l5)); self.wait(2)
        b3_l6 = Tex("Follow the goods, not the money").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): posting the DAJ ---
        self.next_band(4)
        b4_t = Tex("Posting the DAJ").scale(1.2).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_t)); self.wait(2)
        b4_l1 = Tex("Debit Debtors Allowances 800;").scale(0.95).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("credit Debtors Control 800").scale(0.95).shift(band_shift(4) + UP * 0.6)
        self.play(Write(b4_l1)); self.play(Write(b4_l2)); self.wait(2.5)
        b4_l3 = Tex("Return only: debit Trading Stock 400;").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex("credit Cost of Sales 400").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l3)); self.play(Write(b4_l4)); self.wait(2.5)
        b4_l5 = Tex("Why separate from Sales? Gross sales AND").scale(0.9).shift(band_shift(4) + DOWN * 2.1)
        b4_l6 = Tex("what came back — two visible truths").scale(0.9).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5)); self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_4): personal balances and the list ---
        self.next_band(5)
        b5_t = Tex("The Debtors Ledger at month end").scale(1.1).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_t)); self.wait(2)
        b5_l1 = Tex("Sithole: 2 400 + 900 $-$ 600 = R2 700 dr").scale(0.9).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("Govender: 1 800 $-$ 200 = R1 600 dr").scale(0.9).shift(band_shift(5) + UP * 0.6)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        b5_l3 = Tex("List of debtors: 2 700 + 1 600 = R4 300").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l3)); self.wait(2)
        b5_l4 = Tex("Control: 5 100 $-$ 800 = R4 300").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): internal control for credit ---
        self.next_band(6)
        b6_t = Tex("Keeping credit safe").scale(1.2).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_t)); self.wait(2)
        b6_l1 = Tex("Screen customers; set credit limits").scale(0.95).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("Monthly statements to every debtor").scale(0.95).shift(band_shift(6) + UP * 0.6)
        b6_l3 = Tex("Watch the age of debts; chase overdue").scale(0.95).shift(band_shift(6) + DOWN * 0.2)
        b6_l4 = Tex("Recorder $\\neq$ receiver of payments").scale(0.95).shift(band_shift(6) + DOWN * 1.0)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(1.8)
        b6_l5 = Tex("Credit: a privilege, managed").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the exercise-book of names ---
        self.next_band(7)
        b7_t = Tex("The exercise-book of names").scale(1.2).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("A page per person: the Debtors Ledger").scale(1.0).shift(band_shift(7) + UP * 1.4)
        self.play(Write(b7_l1)); self.wait(2)
        b7_l2 = Tex("One line for the street: Debtors Control").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l2)); self.wait(2)
        b7_l3 = Tex("The lock: sum of pages = the street's line").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex("The shelf still writes: cost rides along").scale(0.95).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_6): the week Mr Sithole changed his mind ---
        self.next_band(8)
        b8_t = Tex("The week Mr Sithole changed his mind").scale(1.05).shift(band_shift(8) + UP * 2.5)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Shirt returns: page credited R600,").scale(0.95).shift(band_shift(8) + UP * 1.4)
        b8_l2 = Tex("shelf regains R400 — both stories reverse").scale(0.95).shift(band_shift(8) + UP * 0.6)
        self.play(Write(b8_l1)); self.play(Write(b8_l2)); self.wait(2.5)
        b8_l3 = Tex("Kettle stays: page credited R200,").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex("shelf untouched — price moved alone").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l3)); self.play(Write(b8_l4)); self.wait(2.5)
        b8_l5 = Tex("R5 100 sold, R800 back $\\neq$ R4 300 clean —").scale(0.9).shift(band_shift(8) + DOWN * 2.1)
        b8_l6 = Tex("separate books keep the stories visible").scale(0.9).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5)); self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_7): keeping the names good ---
        self.next_band(9)
        b9_t = Tex("Keeping the names good").scale(1.2).shift(band_shift(9) + UP * 2.5)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = Tex("Limits before trust — R3 500 for a good name").scale(0.9).shift(band_shift(9) + UP * 1.4)
        b9_l2 = Tex("Statements: remind politely, correct early").scale(0.9).shift(band_shift(9) + UP * 0.6)
        b9_l3 = Tex("Chase the day a promise goes overdue").scale(0.9).shift(band_shift(9) + DOWN * 0.2)
        b9_l4 = Tex("Two sets of hands, paper between them").scale(0.9).shift(band_shift(9) + DOWN * 1.0)
        for m in (b9_l1, b9_l2, b9_l3, b9_l4):
            self.play(Write(m))
            self.wait(1.8)
        b9_l5 = Tex("Credit: an engine with working brakes").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(4)
