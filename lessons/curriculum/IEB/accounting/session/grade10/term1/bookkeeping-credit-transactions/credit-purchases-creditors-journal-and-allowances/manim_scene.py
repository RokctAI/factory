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

# Band-layout whiteboard scene for the credit-purchases / creditors-journal
# session duo. Exporter-safe primitives only (Tex/MathTex/Line/Arrow/
# Rectangle/VGroup); write-only reveals. Band time follows subtopics.json
# (180/200/190/200/170/180/180 of 1300 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CreditPurchasesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the mirror and the invoice received ---
        title = Tex("Buying on Credit").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Same invoice, two books:").scale(1.0).shift(UP * 1.2)
        l02 = Tex("in theirs, we are a debtor;").scale(1.0).shift(UP * 0.4)
        l03 = Tex("in ours, they are a CREDITOR — a liability").scale(0.95).shift(DOWN * 0.4)
        self.play(Write(l01)); self.play(Write(l02)); self.wait(2)
        self.play(Write(l03)); self.wait(2.5)
        l04 = Tex("Invoice RECEIVED — renumbered, matched").scale(0.95).shift(DOWN * 1.4)
        self.play(Write(l04))
        self.wait(3)

        # --- Band 1 (subtopic_1): the CJ's columns ---
        self.next_band(1)
        b1_t = Tex("The Creditors Journal").scale(1.2).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_t)); self.wait(2)
        b1_l1 = Tex("Creditors Control: every line strikes it").scale(0.95).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("Lanes: Trading Stock, Stationery,").scale(0.95).shift(band_shift(1) + UP * 0.6)
        b1_l3 = Tex("Equipment, Sundries").scale(0.95).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.play(Write(b1_l3)); self.wait(2.5)
        b1_wrong = Tex("A cost of sales column for buying").scale(0.95).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        b1_l4 = Tex("Buying: ONE truth — the shelf loads at cost").scale(0.9).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the month's purchases ---
        self.next_band(2)
        b2_t = Tex("The month's invoices").scale(1.2).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_t)); self.wait(2)
        b2_l1 = Tex("4th, inv 91: Coastal, stock R8 500").scale(0.9).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("10th, inv 92: Karoo, stationery R600").scale(0.9).shift(band_shift(2) + UP * 0.6)
        b2_l3 = Tex("16th, inv 93: FitOut, counter R4 000 — EQUIPMENT").scale(0.85).shift(band_shift(2) + DOWN * 0.2)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2)); self.wait(2)
        self.play(Write(b2_l3)); self.wait(2.5)
        b2_l4 = Tex("Daily: CREDIT each supplier's page —").scale(0.95).shift(band_shift(2) + DOWN * 1.2)
        b2_l5 = Tex("we owe more; liabilities grow credit").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4)); self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): totals, cross-cast, posting ---
        self.next_band(3)
        b3_t = Tex("Total, prove, post").scale(1.2).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_t)); self.wait(2)
        b3_l1 = MathTex(r"8\,500 + 600 + 4\,000 = 13\,100\ \checkmark").scale(1.0).shift(band_shift(3) + UP * 1.4)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2.5)
        b3_l2 = Tex("Credit Creditors Control 13 100").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l2)); self.wait(2)
        b3_l3 = Tex("Debit Trading Stock 8 500;").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex("debit Stationery 600; debit Equipment 4 000").scale(0.9).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l3)); self.play(Write(b3_l4)); self.wait(2.5)
        b3_l5 = Tex("Debits 13 100 = credit 13 100").scale(0.95).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): returns — debit note and CAJ ---
        self.next_band(4)
        b4_t = Tex("Returns to suppliers: the CAJ").scale(1.15).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_t)); self.wait(2)
        b4_l1 = Tex("WE issue the DEBIT NOTE:").scale(1.0).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("`your account is reduced — here is why'").scale(0.95).shift(band_shift(4) + UP * 0.6)
        self.play(Write(b4_l1)); self.play(Write(b4_l2)); self.wait(2.5)
        b4_l3 = Tex("DN 31: Coastal — control 700, stock 700").scale(0.9).shift(band_shift(4) + DOWN * 0.3)
        b4_l4 = Tex("DN 32: Karoo — control 150, stationery 150").scale(0.9).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3)); self.wait(2)
        self.play(Write(b4_l4)); self.wait(2)
        b4_l5 = Tex("Post: debit Control 850; credit Stock 700;").scale(0.9).shift(band_shift(4) + DOWN * 2.0)
        b4_l6 = Tex("credit Stationery 150").scale(0.9).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5)); self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): what returns do NOT touch ---
        self.next_band(5)
        b5_t = Tex("What returns do NOT touch").scale(1.15).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_t)); self.wait(2)
        b5_wrong1 = Tex("Adjust cost of sales on a purchase return").scale(0.9).shift(band_shift(5) + UP * 1.4)
        self.play(Write(b5_wrong1))
        self.play(Create(strike(b5_wrong1)))
        b5_l1 = Tex("Bought at cost, returned at cost —").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l2 = Tex("only SELLING creates the two truths").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l1)); self.play(Write(b5_l2)); self.wait(2.5)
        b5_wrong2 = Tex("A return moves money").scale(0.95).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_wrong2))
        self.play(Create(strike(b5_wrong2)))
        b5_l3 = Tex("Returns adjust the DEBT; payment is separate").scale(0.9).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_l3))
        self.wait(3)

        # --- Band 6 (subtopic_4): the pages, the list, the lock ---
        self.next_band(6)
        b6_t = Tex("Pages, list, lock").scale(1.2).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_t)); self.wait(2)
        b6_l1 = Tex("Coastal: 8 500 $-$ 700 = R7 800 cr").scale(0.9).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("Karoo: 600 $-$ 150 = R450 cr; FitOut R4 000 cr").scale(0.85).shift(band_shift(6) + UP * 0.6)
        self.play(Write(b6_l1)); self.wait(2)
        self.play(Write(b6_l2)); self.wait(2)
        b6_l3 = Tex("List: 7 800 + 450 + 4 000 = R12 250").scale(0.9).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(b6_l3)); self.wait(2)
        b6_l4 = Tex("Control: 13 100 $-$ 850 = R12 250").scale(0.9).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the other side of the counter ---
        self.next_band(7)
        b7_t = Tex("The other side of the counter").scale(1.2).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("Lindi is a name in Coastal's book now").scale(0.95).shift(band_shift(7) + UP * 1.4)
        self.play(Write(b7_l1)); self.wait(2)
        b7_l2 = Tex("Her own book about THEM: a page each —").scale(0.95).shift(band_shift(7) + UP * 0.5)
        b7_l3 = Tex("the Creditors Ledger; one summary line").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        self.play(Write(b7_l2)); self.play(Write(b7_l3)); self.wait(2.5)
        b7_l4 = Tex("Debtors: more coming in — debit side").scale(0.9).shift(band_shift(7) + DOWN * 1.2)
        b7_l5 = Tex("Creditors: more going out — credit side").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l4)); self.wait(2)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the month of buying on trust ---
        self.next_band(8)
        b8_t = Tex("The month of buying on trust").scale(1.15).shift(band_shift(8) + UP * 2.5)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Stock R8 500; stationery R600; counter R4 000").scale(0.85).shift(band_shift(8) + UP * 1.4)
        b8_l2 = Tex("Three homes: stock, expense, asset").scale(0.95).shift(band_shift(8) + UP * 0.6)
        self.play(Write(b8_l1)); self.wait(2)
        self.play(Write(b8_l2)); self.wait(2)
        b8_l3 = Tex("Damaged box: debit note, R700 —").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        b8_l4 = Tex("a letter with numbers, our timeline").scale(0.95).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8_l3)); self.play(Write(b8_l4)); self.wait(2.5)
        b8_l5 = Tex("Pages 12 250 = summary line 12 250").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): paying like a pro ---
        self.next_band(9)
        b9_t = Tex("Paying like a pro").scale(1.2).shift(band_shift(9) + UP * 2.5)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = Tex("1. Three papers, one story:").scale(0.95).shift(band_shift(9) + UP * 1.4)
        b9_l2 = Tex("order, delivery note, invoice").scale(0.95).shift(band_shift(9) + UP * 0.6)
        self.play(Write(b9_l1)); self.play(Write(b9_l2)); self.wait(2.5)
        b9_l3 = Tex("2. On terms, on time — never late,").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        b9_l4 = Tex("never needlessly early").scale(0.95).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l3)); self.play(Write(b9_l4)); self.wait(2.5)
        b9_l5 = Tex("3. Reconcile their statement to our page").scale(0.9).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(4)
