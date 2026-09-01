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

# Band-layout whiteboard scene for the credit sales (DJ + DAJ) session duo.
# Exporter-safe primitives only; write-only reveals; camera moves down bands.
# Band time follows subtopics.json (190/210/210/190/180/180/170 of 1330 s).

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
        title = Tex("Credit Sales: the Debtors Journal").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Invoice = the birth certificate of a debt").scale(1.05).shift(UP * 1.0)
        self.play(Write(l01)); self.wait(2)
        l02 = Tex("From issue, the customer is a DEBTOR —").scale(1.0).shift(UP * 0.2)
        l03 = Tex("an asset: money receivable").scale(1.05).shift(DOWN * 0.6)
        self.play(Write(l02)); self.play(Write(l03)); self.wait(2.5)
        l04 = Tex("DJ columns: doc, day, NAME, Sales,").scale(1.0).shift(DOWN * 1.6)
        l05 = Tex("Cost of Sales — two truths per sale").scale(1.0).shift(DOWN * 2.4)
        self.play(Write(l04)); self.play(Write(l05))
        self.play(Create(SurroundingRectangle(l05, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): the month's credit sales ---
        self.next_band(1)
        b1_t = Tex("The month, mark-up 25\\% on cost").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_t)); self.wait(1.5)
        b1_l1 = Tex("4th, inv 61, L. Dube: R2 000; cost R1 600").scale(1.0).shift(band_shift(1) + UP * 1.3)
        b1_l2 = Tex("10th, inv 62, S. Naidoo: R1 500; cost R1 200").scale(1.0).shift(band_shift(1) + UP * 0.5)
        b1_l3 = Tex("18th, inv 63, L. Dube: R1 000; cost R800").scale(1.0).shift(band_shift(1) + DOWN * 0.3)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3)); self.wait(2)
        b1_l4 = MathTex(r"\text{cost} = \text{selling price} \div 1{,}25").scale(1.05).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex("Daily: each personal account DEBITED —").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        b1_l6 = Tex("they owe more; folio DJ 1").scale(1.0).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l5)); self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): month-end posting ---
        self.next_band(2)
        b2_t = Tex("Month end: post the totals").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_t)); self.wait(1.5)
        b2_l1 = Tex("Sales R4 500; Cost of Sales R3 600").scale(1.05).shift(band_shift(2) + UP * 1.4)
        self.play(Write(b2_l1)); self.wait(2)
        b2_l2 = Tex("DEBIT Debtors Control R4 500;").scale(1.0).shift(band_shift(2) + UP * 0.5)
        b2_l3 = Tex("CREDIT Sales R4 500").scale(1.0).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(b2_l2)); self.play(Write(b2_l3)); self.wait(2.5)
        b2_l4 = Tex("DEBIT Cost of Sales R3 600;").scale(1.0).shift(band_shift(2) + DOWN * 1.0)
        b2_l5 = Tex("CREDIT Trading Stock R3 600").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l4)); self.play(Write(b2_l5)); self.wait(2)
        b2_l6 = MathTex(r"\text{Check: } 8\,100 = 8\,100\ \checkmark").scale(0.9).shift(band_shift(2) + DOWN * 2.45)
        self.play(Write(b2_l6))
        b2_l7 = Tex("Detail daily, totals monthly").scale(0.9).shift(band_shift(2) + DOWN * 3.05)
        self.play(Write(b2_l7))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): return versus allowance ---
        self.next_band(3)
        b3_t = Tex("Return or allowance? Follow the goods").scale(1.1).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_t)); self.wait(2)
        b3_l1 = Tex("12th: Dube RETURNS R500 (wrong size)").scale(1.0).shift(band_shift(3) + UP * 1.3)
        b3_l2 = Tex("Goods come back: allowances R500,").scale(1.0).shift(band_shift(3) + UP * 0.5)
        b3_l3 = Tex("cost column carries R400").scale(1.0).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2)); self.play(Write(b3_l3)); self.wait(2.5)
        b3_l4 = Tex("20th: Naidoo keeps a scratched item — R150 off").scale(0.95).shift(band_shift(3) + DOWN * 1.2)
        b3_l5 = Tex("ALLOWANCE: cost column stays EMPTY").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l4)); self.wait(2)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(2)
        b3_l6 = Tex("Source document: the CREDIT NOTE — the anti-invoice").scale(0.9).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): posting the DAJ ---
        self.next_band(4)
        b4_t = Tex("Posting the DAJ").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_t)); self.wait(1.5)
        b4_l1 = Tex("DEBIT Debtors Allowances R650;").scale(1.0).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("CREDIT Debtors Control R650").scale(1.0).shift(band_shift(4) + UP * 0.6)
        self.play(Write(b4_l1)); self.play(Write(b4_l2)); self.wait(2.5)
        b4_l3 = Tex("DEBIT Trading Stock R400;").scale(1.0).shift(band_shift(4) + DOWN * 0.3)
        b4_l4 = Tex("CREDIT Cost of Sales R400 (return only)").scale(1.0).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3)); self.play(Write(b4_l4)); self.wait(2.5)
        b4_wrong = Tex("Just debit Sales directly").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(1.5)
        b4_l5 = Tex("Management needs gross sales AND returns visible").scale(0.9).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): personal balances and the list ---
        self.next_band(5)
        b5_t = Tex("The Debtors Ledger at month end").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_t)); self.wait(1.5)
        b5_l1 = MathTex(r"\text{Dube: } 2\,000 + 1\,000 - 500 = 2\,500\ \text{debit}").scale(0.95).shift(band_shift(5) + UP * 1.3)
        b5_l2 = MathTex(r"\text{Naidoo: } 1\,500 - 150 = 1\,350\ \text{debit}").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        b5_l3 = MathTex(r"\text{List: } 2\,500 + 1\,350 = 3\,850").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l3)); self.wait(2)
        b5_l4 = MathTex(r"\text{Control: } 4\,500 - 650 = 3\,850\ \checkmark").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)
        b5_l5 = Tex("Disagreement = an error with an address").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): internal control for credit ---
        self.next_band(6)
        b6_t = Tex("Keeping credit selling safe").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_t)); self.wait(1.5)
        b6_l1 = Tex("Screen customers; set a CREDIT LIMIT").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("Monthly STATEMENT to every debtor").scale(1.0).shift(band_shift(6) + UP * 0.5)
        b6_l3 = Tex("Watch the AGE of debts — chase on time").scale(1.0).shift(band_shift(6) + DOWN * 0.3)
        b6_l4 = Tex("Recorder of debtors $\\neq$ receiver of payments").scale(1.0).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l1)); self.wait(2)
        self.play(Write(b6_l2)); self.wait(2)
        self.play(Write(b6_l3)); self.wait(2)
        self.play(Write(b6_l4)); self.wait(2)
        b6_l5 = Tex("Credit is a privilege, managed — never forgotten").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the exercise-book of names ---
        self.next_band(7)
        b7_t = Tex("The exercise-book of names").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("A page per person: Mrs Dube takes R2 000 —").scale(0.95).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex("invoice for her, entry on her page").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1)); self.play(Write(b7_l2)); self.wait(2.5)
        b7_l3 = Tex("Pages for the people, one line for the street:").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("pages total = Debtors Control, always").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3)); self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l5 = Tex("The shelf still tells its truth: cost of sales").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        b7_l6 = Tex("rides along — the shelf ignores HOW they pay").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l5)); self.play(Write(b7_l6))
        self.wait(3)

        # --- Band 8 (subtopic_6): the week Mrs Dube changed her mind ---
        self.next_band(8)
        b8_t = Tex("The week Mrs Dube changed her mind").scale(1.1).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Shirt comes BACK: page credited R500,").scale(1.0).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("shelf regains R400 — both stories reversed").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1)); self.play(Write(b8_l2)); self.wait(2.5)
        b8_l3 = Tex("Kettle STAYS: page credited R150,").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex("shelf untouched — price moved alone").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l3)); self.play(Write(b8_l4)); self.wait(2.5)
        b8_l5 = Tex("R4 500 sold with R650 back $\\neq$ R3 850 sold clean:").scale(0.9).shift(band_shift(8) + DOWN * 2.1)
        b8_l6 = Tex("separate books keep separate truths visible").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5)); self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): keeping the names good ---
        self.next_band(9)
        b9_t = Tex("Keeping the names good").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = Tex("Credit limits: Mrs Dube R3 000; new name R500").scale(0.95).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1)); self.wait(2)
        b9_l2 = Tex("Statements monthly: remind politely,").scale(1.0).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex("surface disputes in week one").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l2)); self.play(Write(b9_l3)); self.wait(2.5)
        b9_l4 = Tex("Thirty days is normal; ninety is a gift —").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        b9_l5 = Tex("chase the day a promise goes overdue").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l4)); self.play(Write(b9_l5)); self.wait(2)
        b9_l6 = Tex("Page-writer $\\neq$ payment-taker — paper between").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l6))
        self.wait(4)
