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

# Band-layout whiteboard scene for the General Journal session duo.
# Exporter-safe primitives only; write-only reveals; camera moves down bands.
# Band time follows subtopics.json (190/210/190/190/170/190/170 of 1310 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GeneralJournalSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the journal for everything else ---
        title = Tex("The General Journal").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Book of first entry for what no").scale(1.05).shift(UP * 1.1)
        l02 = Tex("specialised journal accommodates").scale(1.05).shift(UP * 0.3)
        self.play(Write(l01)); self.play(Write(l02)); self.wait(2.5)
        # Entry shape
        l03 = Tex("Account debited \\quad R900").scale(1.0).shift(DOWN * 0.7 + LEFT * 1.5)
        l04 = Tex("Account credited \\quad R900").scale(1.0).shift(DOWN * 1.5)
        l05 = Tex("Narration: the reason, one sentence").scale(0.95).shift(DOWN * 2.3 + LEFT * 0.5)
        self.play(Write(l03)); self.wait(1.5)
        self.play(Write(l04)); self.wait(1.5)
        self.play(Write(l05))
        self.play(Create(SurroundingRectangle(l05, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): you name both sides; analysis columns ---
        self.next_band(1)
        b1_t = Tex("No design thinks for you here").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_t)); self.wait(1.5)
        b1_l1 = Tex("In the CRJ every line debited Bank;").scale(1.05).shift(band_shift(1) + UP * 1.3)
        b1_l2 = Tex("in the GJ, YOU name both sides").scale(1.05).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l1)); self.play(Write(b1_l2)); self.wait(2.5)
        b1_l3 = Tex("An entry without a narration").scale(1.05).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex("is incomplete — it loses its mark").scale(1.05).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(b1_l3)); self.play(Write(b1_l4)); self.wait(2.5)
        b1_l5 = Tex("Analysis columns collect Debtors and").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        b1_l6 = Tex("Creditors Control amounts for monthly posting").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l5)); self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): bad debts ---
        self.next_band(2)
        b2_t = Tex("Classic 1: the bad debt").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_t)); self.wait(1.5)
        b2_l1 = Tex("L. Jacobs owes R900 — irrecoverable").scale(1.05).shift(band_shift(2) + UP * 1.3)
        self.play(Write(b2_l1)); self.wait(2)
        b2_l2 = Tex("Debit Bad Debts R900 (expense born)").scale(1.05).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("Credit Debtors Control R900 (asset dies)").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l2)); self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex("``Debt written off as irrecoverable''").scale(1.0).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l4)); self.wait(2)
        b2_l5 = Tex("No cash moved — prudence refuses to").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        b2_l6 = Tex("overstate an asset that no longer exists").scale(1.0).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_l5)); self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): interest, both directions ---
        self.next_band(3)
        b3_t = Tex("Classic 2: interest on overdue accounts").scale(1.1).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_t)); self.wait(1.5)
        b3_l1 = Tex("Adams 60 days late on R1 500: charge R45").scale(1.0).shift(band_shift(3) + UP * 1.3)
        b3_l2 = Tex("Debit Debtors Control R45;").scale(1.05).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex("Credit Interest Income R45").scale(1.05).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2)); self.play(Write(b3_l3)); self.wait(2.5)
        b3_l4 = Tex("Mirror: Metro charges us R120 —").scale(1.0).shift(band_shift(3) + DOWN * 1.3)
        b3_l5 = Tex("Debit Interest Expense; Credit Creditors R120").scale(0.95).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l4)); self.wait(1.5)
        self.play(Write(b3_l5)); self.wait(2)
        b3_l6 = Tex("Through the GJ: the DEBT grew, not the cash").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_2): drawings of stock ---
        self.next_band(4)
        b4_t = Tex("Classic 3: drawings of stock").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_t)); self.wait(1.5)
        b4_l1 = Tex("Owner takes goods costing R350 home").scale(1.05).shift(band_shift(4) + UP * 1.3)
        self.play(Write(b4_l1)); self.wait(2)
        b4_wrong = Tex("Record the goods at selling price").scale(1.05).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2)
        b4_l2 = Tex("At COST, always — no sale occurred").scale(1.05).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l2)); self.wait(2)
        b4_l3 = Tex("Debit Drawings R350;").scale(1.05).shift(band_shift(4) + DOWN * 1.4)
        b4_l4 = Tex("Credit Trading Stock R350").scale(1.05).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l3)); self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): correcting errors without erasing ---
        self.next_band(5)
        b5_t = Tex("Corrections: nothing is ever erased").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_t)); self.wait(1.5)
        b5_l1 = Tex("Stationery R250 wrongly debited to").scale(1.05).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Trading Stock; the credit leg was correct").scale(1.0).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l1)); self.play(Write(b5_l2)); self.wait(2.5)
        b5_wrong = Tex("Redo the whole entry, credit Creditors again").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l3 = Tex("That double-counts the liability!").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l3)); self.wait(1.5)
        b5_l4 = Tex("Debit Stationery R250; Credit Trading Stock R250").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        b5_l5 = Tex("Correct ONLY the leg that was wrong").scale(1.0).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): control columns and the month's proof ---
        self.next_band(6)
        b6_t = Tex("Month end: columns, postings, proof").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_t)); self.wait(1.5)
        b6_l1 = Tex("Debtors Control: debit R45, credit R900").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("Creditors Control: credit R120").scale(1.0).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1)); self.wait(2)
        self.play(Write(b6_l2)); self.wait(2)
        b6_l3 = MathTex(r"\text{Debits: } 900 + 45 + 120 + 350 + 250 = 1\,665").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = MathTex(r"\text{Credits: } 900 + 45 + 120 + 350 + 250 = 1\,665").scale(0.95).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l3)); self.wait(2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2.5)
        b6_l5 = Tex("Six journals: every transaction has").scale(1.0).shift(band_shift(6) + DOWN * 2.3)
        b6_l6 = Tex("exactly one front door").scale(1.0).shift(band_shift(6) + DOWN * 3.1)
        self.play(Write(b6_l5)); self.play(Write(b6_l6))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the odd-jobs notebook ---
        self.next_band(7)
        b7_t = Tex("The odd-jobs notebook").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("Mrs Jacobs's R900 is not coming back —").scale(1.0).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex("no diary takes it: no money moved, no sale").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1)); self.play(Write(b7_l2)); self.wait(2.5)
        b7_l3 = Tex("So: THIS account up, THAT account down,").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("and one honest sentence why").scale(1.05).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l3)); self.play(Write(b7_l4)); self.wait(2.5)
        b7_l5 = Tex("It is week one's five-step analysis, in pen").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): three stories ---
        self.next_band(8)
        b8_t = Tex("Three stories the big diaries can't tell").scale(1.1).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("1. The funeral: bury the R900 asset,").scale(1.0).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("the loss lands in Bad Debts").scale(1.0).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1)); self.play(Write(b8_l2)); self.wait(2.5)
        b8_l3 = Tex("2. Home shopping: R350 of stock, at cost —").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex("drawings in goods, not rands").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l3)); self.play(Write(b8_l4)); self.wait(2.5)
        b8_l5 = Tex("3. Lateness has a price: Adams +R45 income;").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        b8_l6 = Tex("our lateness to Metro: R120 expense").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5)); self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_7): fixing mistakes in pen ---
        self.next_band(9)
        b9_t = Tex("Fixing mistakes in pen").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_t)); self.wait(2)
        b9_wrong = Tex("Erase it, tippex it, tear out the page").scale(1.05).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_wrong))
        self.play(Create(strike(b9_wrong)))
        self.wait(2)
        b9_l1 = Tex("A book that can quietly change proves nothing").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1)); self.wait(2)
        b9_l2 = Tex("New entry: Stationery up R250,").scale(1.05).shift(band_shift(9) + DOWN * 0.5)
        b9_l3 = Tex("Trading Stock down R250 — plus the sentence").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l2)); self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Surgeon's rule: operate on the broken leg,").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        b9_l5 = Tex("leave the healthy one alone").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l4)); self.play(Write(b9_l5))
        self.wait(4)
