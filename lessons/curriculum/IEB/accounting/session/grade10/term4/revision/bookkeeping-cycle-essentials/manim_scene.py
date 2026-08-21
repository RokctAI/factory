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

# Band-layout whiteboard scene for the IEB Grade 10 Term 4 revision duo
# "Bookkeeping Cycle Essentials". Add-only lifecycle, one band per teaching
# beat, camera moves down between bands. Covers all seven subtopics:
# Part 1 Expert (subtopics 1-4), Part 2 Simplifier (subtopics 5-7).
# subtopics.json durations 220/220/220/220/180/190/190 of 1440 s. Lerato's
# month runs through the machine: equation, journals, ledger balances, the
# trial balance scale, and the control-account agreement.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BookkeepingCycleSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the equation and the compass
        title = Tex("The Bookkeeping Machine, Rebuilt").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"\text{ASSETS} = \text{OWNER'S EQUITY} + \text{LIABILITIES}").scale(0.95).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(2.5)
        b0_l2 = Tex("Every transaction: two equal effects —").scale(1.0).shift(UP * 0.2)
        b0_l3 = Tex("a debit and a credit; the equation stays level").scale(1.0).shift(DOWN * 0.6)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex("Assets, expenses, drawings: increase DEBIT").scale(0.95).shift(DOWN * 1.6)
        b0_l5 = Tex("Equity, liabilities, income: increase CREDIT").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_2): six journals, six documents
        self.next_band(1)
        b1_title = Tex("Six diaries, six documents").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex("CRJ: cash in — receipts, till tapes").scale(0.95).shift(band_shift(1) + UP * 1.3)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("CPJ: cash out — EFT records, counterfoils").scale(0.95).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("DJ: duplicate invoices; DAJ: credit notes").scale(0.95).shift(band_shift(1) + DOWN * 0.3)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("CJ: original invoices; CAJ: debit notes").scale(0.95).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("GJ: the catch-all for everything else").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the month recorded, door by door
        self.next_band(2)
        b2_title = Tex("Lerato's month, door by door").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex("Cash sales 7 500, cost 6 000 — CRJ carries both").scale(0.9).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"\text{Mark-up check: } 6\,000 \times 1{,}25 = 7\,500").scale(0.95).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("Naidoo on credit 2 500 — DJ; return 500 — DAJ").scale(0.9).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("Stock 6 500, rent 2 000, wages 1 200 — CPJ").scale(0.9).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Wholesaler 4 000 — CJ; payments — CPJ, CRJ").scale(0.9).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_3): posting and balancing the ledger
        self.next_band(3)
        b3_title = Tex("The ledger, balanced").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\text{Bank: } 23\,700 - 12\,200 = 11\,500 \text{ dr}").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"\text{Stock: } 10\,900 - 8\,000 = 2\,900 \text{ dr}").scale(0.95).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{Debtors: } 2\,500 - 500 - 1\,200 = 800 \text{ dr}").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = MathTex(r"\text{Creditors: } 4\,000 - 2\,500 = 1\,500 \text{ cr}").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex("Sales 9 500 cr; cost of sales 7 600 dr").scale(0.95).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the trial balance and its blind spots
        self.next_band(4)
        b4_title = Tex("The month on a scale").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex("Debits: 11 500 + 2 900 + 800 + 7 600 + 2 000 + 1 200").scale(0.85).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("Credits: 15 000 + 9 500 + 1 500").scale(0.9).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"26\,000 = 26\,000").scale(1.1).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_wrong = Tex("A level scale proves every figure correct").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2)
        b4_l4 = Tex("Blind spots: wrong account; omitted both sides").scale(0.95).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_4): the control account as a T-account
        self.next_band(5)
        b5_title = Tex("Debtors control — the second count").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        t_v = Line(UP * 1.4, DOWN * 1.4).shift(band_shift(5) + UP * 0.1)
        t_h = Line(LEFT * 3.4, RIGHT * 3.4).shift(band_shift(5) + UP * 1.5)
        self.play(Create(t_v), Create(t_h))
        b5_l1 = Tex("Sales 2 500").scale(0.9).shift(band_shift(5) + UP * 0.7 + LEFT * 1.8)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Allowances 500").scale(0.9).shift(band_shift(5) + UP * 0.7 + RIGHT * 1.9)
        b5_l3 = Tex("Receipts 1 200").scale(0.9).shift(band_shift(5) + UP * 0.0 + RIGHT * 1.9)
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("Balance 800").scale(0.95).shift(band_shift(5) + DOWN * 0.9 + LEFT * 1.8)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)
        b5_l5 = Tex("Naidoo's page: 2 500 $-$ 500 $-$ 1 200 = 800 — agreement").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): what the agreement catches
        self.next_band(6)
        b6_title = Tex("What the agreement catches").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Receipt on the wrong page: list wrong,").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("control right").scale(0.95).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Journal total miscast: control wrong, list right").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("Invoice never posted to a page: list short").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Two independent records, facing each other monthly").scale(0.9).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): one slip, six boxes
        self.next_band(7)
        b7_title = Tex("One slip, six boxes").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        r1 = Rectangle(width=3.2, height=1.1).shift(band_shift(7) + UP * 1.0 + LEFT * 3.7)
        r2 = Rectangle(width=3.2, height=1.1).shift(band_shift(7) + UP * 1.0)
        r3 = Rectangle(width=3.2, height=1.1).shift(band_shift(7) + UP * 1.0 + RIGHT * 3.7)
        r4 = Rectangle(width=3.2, height=1.1).shift(band_shift(7) + DOWN * 0.4 + LEFT * 3.7)
        r5 = Rectangle(width=3.2, height=1.1).shift(band_shift(7) + DOWN * 0.4)
        r6 = Rectangle(width=3.2, height=1.1).shift(band_shift(7) + DOWN * 0.4 + RIGHT * 3.7)
        self.play(Create(r1), Create(r2), Create(r3))
        self.play(Create(r4), Create(r5), Create(r6))
        c1 = Tex("cash in").scale(0.8).shift(band_shift(7) + UP * 1.0 + LEFT * 3.7)
        c2 = Tex("cash out").scale(0.8).shift(band_shift(7) + UP * 1.0)
        c3 = Tex("sold on trust").scale(0.8).shift(band_shift(7) + UP * 1.0 + RIGHT * 3.7)
        c4 = Tex("goods back in").scale(0.8).shift(band_shift(7) + DOWN * 0.4 + LEFT * 3.7)
        c5 = Tex("bought on trust").scale(0.8).shift(band_shift(7) + DOWN * 0.4)
        c6 = Tex("goods back out").scale(0.8).shift(band_shift(7) + DOWN * 0.4 + RIGHT * 3.7)
        self.play(Write(c1), Write(c2), Write(c3))
        self.play(Write(c4), Write(c5), Write(c6))
        self.wait(2.5)
        b7_l1 = Tex("Two questions: cash or promise? Which way?").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the month that adds up twice
        self.next_band(8)
        b8_title = Tex("The month that adds up twice").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("The ledger answers: where do we STAND?").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Bank 11 500; shelf 2 900; Naidoo 800").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{The weigh-in: } 26\,000 = 26\,000").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("The scale cannot smell wrong pages,").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        b8_l5 = Tex("or a slip that never arrived").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): counting the street twice
        self.next_band(9)
        b9_title = Tex("Counting the street twice").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Exercise book: a page per customer").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Main books: one total line").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"\text{Both counts: R}800").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Disagreement gives directions: wrong page — book;").scale(0.9).shift(band_shift(9) + DOWN * 1.5)
        b9_l5 = Tex("wrong column total — the total line").scale(0.9).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2.5)
        b9_l6 = Tex("Five habits, one machine").scale(1.0).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9_l6))
        self.wait(4)
