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

# Band-layout whiteboard scene for the posting / trial-balance session duo.
# Exporter-safe primitives only (Tex/MathTex/Line/Arrow/Rectangle/VGroup);
# write-only reveals. Band time follows subtopics.json
# (180/210/190/200/160/190/190 of 1320 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PostingAndTrialBalanceSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(15)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the ledger's architecture ---
        title = Tex("The General Ledger").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("One account per item — a T:").scale(1.0).shift(UP * 1.2)
        l02 = Tex("debit left, credit right").scale(1.0).shift(UP * 0.4)
        self.play(Write(l01)); self.play(Write(l02)); self.wait(2.5)
        l03 = Tex("Balance sheet section: what endures").scale(0.95).shift(DOWN * 0.6)
        l04 = Tex("Nominal section: incomes and expenses,").scale(0.95).shift(DOWN * 1.4)
        l05 = Tex("measuring the year, closed at year end").scale(0.95).shift(DOWN * 2.2)
        self.play(Write(l03)); self.wait(2)
        self.play(Write(l04)); self.play(Write(l05))
        self.wait(3)

        # --- Band 1 (subtopic_1): folios; totals post ---
        self.next_band(1)
        b1_t = Tex("Folios and the totals rule").scale(1.2).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_t)); self.wait(2)
        b1_l1 = Tex("Ledger folio: which journal page — CRJ 1").scale(0.95).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("Journal folio: which account received it").scale(0.95).shift(band_shift(1) + UP * 0.6)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        b1_l3 = Tex("Any amount traceable both ways").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l3)); self.wait(2)
        b1_l4 = Tex("TOTALS post, not lines —").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        b1_l5 = Tex("only sundries post by name").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l4)); self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): posting the CRJ ---
        self.next_band(2)
        b2_t = Tex("Posting the CRJ").scale(1.2).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_t)); self.wait(2)
        b2_l1 = Tex("Bank total R67 700: DEBIT Bank").scale(1.0).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("Sales R4 500: CREDIT Sales").scale(1.0).shift(band_shift(2) + UP * 0.6)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2)); self.wait(2)
        b2_l3 = Tex("Cost of Sales R3 000 posts TWICE:").scale(1.0).shift(band_shift(2) + DOWN * 0.3)
        b2_l4 = Tex("debit Cost of Sales, credit Trading Stock").scale(0.95).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3)); self.play(Write(b2_l4)); self.wait(2.5)
        b2_l5 = Tex("Sundries by name: Capital 60 000 cr;").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        b2_l6 = Tex("Rent Income 3 200 cr").scale(0.95).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l5)); self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): auditing the CRJ's double entry ---
        self.next_band(3)
        b3_t = Tex("Audit the CRJ posting").scale(1.15).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_t)); self.wait(2)
        b3_l1 = Tex("Debits: 67 700 + 3 000 = 70 700").scale(1.0).shift(band_shift(3) + UP * 1.4)
        self.play(Write(b3_l1)); self.wait(2)
        b3_l2 = Tex("Credits: 4 500 + 60 000 + 3 200 + 3 000").scale(0.95).shift(band_shift(3) + UP * 0.5)
        b3_l3 = Tex("= 70 700").scale(1.05).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(b3_l2)); self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_wrong = Tex("Trading Stock's credit partners Bank").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        b3_l4 = Tex("It partners the Cost of Sales debit").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): posting the CPJ ---
        self.next_band(4)
        b4_t = Tex("Posting the CPJ").scale(1.2).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_t)); self.wait(2)
        b4_l1 = Tex("Bank total R25 300: CREDIT Bank").scale(1.0).shift(band_shift(4) + UP * 1.4)
        self.play(Write(b4_l1)); self.wait(2)
        b4_l2 = Tex("Trading Stock 9 500 dr; Wages 3 600 dr").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l2)); self.wait(2)
        b4_l3 = Tex("Sundries: Rent Expense 4 200 dr;").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex("Equipment 5 500 dr; Drawings 2 500 dr").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l3)); self.play(Write(b4_l4)); self.wait(2.5)
        b4_l5 = Tex("Check: debits 25 300 = credit 25 300").scale(0.95).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): balancing the Bank account ---
        self.next_band(5)
        b5_t = Tex("Balancing Bank").scale(1.2).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_t)); self.wait(2)
        b5_l1 = Tex("Debit side 67 700; credit side 25 300").scale(1.0).shift(band_shift(5) + UP * 1.4)
        self.play(Write(b5_l1)); self.wait(2)
        b5_l2 = Tex("Balance c/d 42 400 on the credit side;").scale(0.95).shift(band_shift(5) + UP * 0.5)
        b5_l3 = Tex("Balance b/d 42 400, debit — money held").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(b5_l2)); self.play(Write(b5_l3)); self.wait(2.5)
        b5_l4 = Tex("Stock: 9 500 $-$ 3 000 = 6 500 b/d dr").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l4)); self.wait(2)
        b5_l5 = Tex("Nominal accounts accumulate — no balancing").scale(0.9).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the trial balance ---
        self.next_band(6)
        b6_t = Tex("The trial balance").scale(1.2).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_t)); self.wait(2)
        b6_l1 = Tex("Debits: Bank 42 400, Stock 6 500,").scale(0.9).shift(band_shift(6) + UP * 1.5)
        b6_l2 = Tex("Equipment 5 500, Drawings 2 500,").scale(0.9).shift(band_shift(6) + UP * 0.8)
        b6_l3 = Tex("CoS 3 000, Wages 3 600, Rent Exp 4 200").scale(0.9).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l1)); self.play(Write(b6_l2)); self.play(Write(b6_l3)); self.wait(2.5)
        b6_l4 = Tex("Credits: Capital 60 000, Sales 4 500,").scale(0.9).shift(band_shift(6) + DOWN * 0.7)
        b6_l5 = Tex("Rent Income 3 200").scale(0.9).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l4)); self.play(Write(b6_l5)); self.wait(2)
        b6_l6 = MathTex(r"67\,700 = 67\,700\ \checkmark").scale(1.1).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): what it proves; hunting differences ---
        self.next_band(7)
        b7_t = Tex("What level columns prove").scale(1.15).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_t)); self.wait(2)
        b7_wrong = Tex("Balanced, therefore correct").scale(1.0).shift(band_shift(7) + UP * 1.4)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        b7_l1 = Tex("Arithmetic equality only — a smoke detector").scale(0.95).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1)); self.wait(2.5)
        b7_l2 = Tex("Gap = an amount: posted once").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l3 = Tex("Gap $\\div$ 2: wrong side").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        b7_l4 = Tex("Gap $\\div$ 9: digits transposed").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l2)); self.wait(1.6)
        self.play(Write(b7_l3)); self.wait(1.6)
        self.play(Write(b7_l4))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the filing cabinet ---
        self.next_band(8)
        b8_t = Tex("The filing cabinet").scale(1.2).shift(band_shift(8) + UP * 2.5)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Diaries = sorting room, by date").scale(1.0).shift(band_shift(8) + UP * 1.4)
        b8_l2 = Tex("Cabinet = one drawer per thing").scale(1.0).shift(band_shift(8) + UP * 0.6)
        self.play(Write(b8_l1)); self.wait(2)
        self.play(Write(b8_l2)); self.wait(2)
        b8_l3 = Tex("Money and possessions grow LEFT;").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex("stake, debts and earnings grow RIGHT").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l3)); self.play(Write(b8_l4)); self.wait(2)
        b8_l5 = Tex("Folio codes: the return tickets").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): one month comes home ---
        self.next_band(9)
        b9_t = Tex("One month comes home").scale(1.2).shift(band_shift(9) + UP * 2.5)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = Tex("In: 67 700 left of Bank; 4 500 right of Sales").scale(0.9).shift(band_shift(9) + UP * 1.4)
        b9_l2 = Tex("Pair: 3 000 left of CoS, 3 000 right of Stock").scale(0.9).shift(band_shift(9) + UP * 0.6)
        self.play(Write(b9_l1)); self.wait(2)
        self.play(Write(b9_l2)); self.wait(2)
        b9_l3 = Tex("Out: 25 300 right of Bank; 9 500 left of Stock;").scale(0.85).shift(band_shift(9) + DOWN * 0.3)
        b9_l4 = Tex("wages, rent, shelving, drawings — left").scale(0.9).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l3)); self.play(Write(b9_l4)); self.wait(2.5)
        b9_l5 = Tex("Bank drawer: 67 700 $-$ 25 300 = R42 400").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the weigh-in ---
        self.next_band(10)
        b10_t = Tex("The weigh-in").scale(1.2).shift(band_shift(10) + UP * 2.5)
        self.play(Write(b10_t)); self.wait(2)
        b10_l1 = Tex("Every amount: a left and a right, equal").scale(0.95).shift(band_shift(10) + UP * 1.4)
        self.play(Write(b10_l1)); self.wait(2)
        b10_l2 = Tex("Lefts 67 700 = rights 67 700: level scales").scale(0.95).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2)
        b10_l3 = Tex("Scales test the WEIGHING, not the FILING").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l3)); self.wait(2)
        b10_l4 = Tex("Gaps whisper: dropped once, wrong side,").scale(0.95).shift(band_shift(10) + DOWN * 1.4)
        b10_l5 = Tex("or digits swapped — read the gap first").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l4)); self.play(Write(b10_l5))
        self.wait(4)
