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

# Band-layout whiteboard scene for the IEB Grade 11 Term 1 duo
# "Bank Reconciliation". One band per teaching beat; camera moves down,
# nothing removed. Exporter-safe primitives only; the corrected Bank
# account and the reconciliation statement are built line by line in
# script order, totals last. Subtopic shares: 215/225/215/215/180/200/190
# of 1440 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BankReconciliationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): why two records differ — the three-way sort ---
        title = Tex("Bank Reconciliation").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Two records of one account never agree").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("1. TIMING: both right, time closes the gap").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("2. OMISSIONS: fees, interest, stop orders,").scale(1.0).shift(DOWN * 0.4)
        b0_l4 = Tex("dishonoured EFTs — the bank knew first").scale(1.0).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex("3. ERRORS: ours, or the bank's").scale(1.0).shift(DOWN * 1.9)
        self.play(Write(b0_l5))
        self.wait(2)
        b0_l6 = Tex("Ours: journalise. Timing + bank's: reconcile").scale(1.0).shift(DOWN * 2.8)
        self.play(Write(b0_l6))
        self.play(Create(SurroundingRectangle(b0_l6, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): findings one to five ---
        self.next_band(1)
        b1_title = Tex("The statement arrives: enter the news").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Provisional Bank balance: R72 540 Dr").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Bank charges 2 140: Dr Bank charges, Cr Bank").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Interest 520: Dr Bank, Cr Interest income").scale(0.95).shift(band_shift(1) + DOWN * 0.3)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Stop order 2 750: Dr Insurance, Cr Bank").scale(0.95).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Debit order 1 430: Dr Sundry exp, Cr Bank").scale(0.95).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l5))
        self.wait(2)
        b1_l6 = Tex("Dishonoured EFT 5 400:").scale(0.95).shift(band_shift(1) + DOWN * 2.4)
        b1_l7 = Tex("Dr Debtors control, Cr Bank — debt is back").scale(0.95).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.wait(3)

        # --- Band 2 (subtopic_2): errors, stale cheque, corrected balance ---
        self.next_band(2)
        b2_title = Tex("Our error, the stale cheque, the balance").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"CPJ says 5 270, bank paid 5 720: R450 short").scale(0.95).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("Divisible by 9 = transposition fingerprint").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("Cheque 0873, R8 100, six months old: STALE").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex("Cancel: Dr Bank, Cr Creditors control").scale(0.95).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = Tex(r"72 540 $-$ 2 140 + 520 $-$ 2 750 $-$ 1 430").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        b2_l6 = Tex(r"$-$ 5 400 $-$ 450 + 8 100 = R68 990").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l5))
        self.wait(2)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): the reconciliation statement ---
        self.next_band(3)
        b3_title = Tex("Bank Reconciliation Statement, 28 Feb").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        b3_rule = Line(band_shift(3) + UP * 1.95 + LEFT * 3.3,
                       band_shift(3) + UP * 1.95 + RIGHT * 3.3, stroke_width=3)
        self.play(Create(b3_rule))
        self.wait(1.5)
        b3_l1 = Tex("Balance per bank statement: 67 540").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("Add outstanding deposit: 19 800").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Add bank's wrong debit: 2 950").scale(1.0).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("Less outstanding EFTs: (21 300)").scale(1.0).shift(band_shift(3) + DOWN * 1.0)
        b3_l4b = Tex("EFT 0524 R11 460 + EFT 0531 R9 840").scale(0.9).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l4))
        self.play(Write(b3_l4b))
        self.wait(2)
        b3_l5 = Tex("= R68 990 — matches the Bank account").scale(1.05).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(2)
        b3_l6 = Tex("Direction test: what will the BANK still do?").scale(0.95).shift(band_shift(3) + DOWN * 3.2)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_4): the four traps ---
        self.next_band(4)
        b4_title = Tex("The four traps").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_w1 = Tex("Journalise the outstanding deposit?").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_w1))
        self.play(Create(strike(b4_w1)))
        self.wait(2)
        b4_l1 = Tex("Outstanding items are ALREADY in our books").scale(0.95).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("Overdraft: credit balance, in brackets —").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        b4_l3 = Tex("same question decides every sign").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_w2 = Tex("Dishonoured EFT written off as a loss?").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_w2))
        self.play(Create(strike(b4_w2)))
        self.wait(1.5)
        b4_l4 = Tex("It is a reversal — and never forget 0873").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_4): method marks and internal control ---
        self.next_band(5)
        b5_title = Tex("Method marks and the control purpose").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Show structure: corrected account with").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("contra names; statement with full heading").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Workings earn marks even if totals slip").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("Control: the bank is an independent record").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Monthly; done by a non-cash-handler;").scale(1.0).shift(band_shift(5) + DOWN * 2.2)
        b5_l6 = Tex("signed by a partner; chase old items").scale(1.0).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): two people counting the same money ---
        self.next_band(6)
        b6_title = Tex("Two people counting the same money").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Savings club: your notebook at home,").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("the treasurer's book at the bank").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Same money, two clocks — time closes it").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("And the bank acts without phoning you:").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        b6_l5 = Tex("fees, interest, standing orders, bounces").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex("The statement is a letter of its news").scale(1.0).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): the three piles ---
        self.next_band(7)
        b7_title = Tex("Sort everything into three piles").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("NEWS — into the journals: 2 140, 520,").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("2 750, 1 430, and the bounced 5 400").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(3)
        b7_l3 = Tex("YOUR SLIPS: the R450 digit-swap, and").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("cheque 0873 R8 100 — stale like old bread").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(3)
        b7_l5 = Tex("LEAVE ALONE: 19 800 clearing, 21 300").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        b7_l6 = Tex("leaving, 2 950 the bank must fix").scale(1.0).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3.5)

        # --- Band 8 (subtopic_7): the bridge ---
        self.next_band(8)
        b8_title = Tex("The bridge between the two numbers").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Your book: R68 990. The bank: R67 540").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("67 540 + 19 800 + 2 950 $-$ 21 300").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("= R68 990 — the bridge holds").scale(1.1).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(3)
        b8_l4 = Tex("Only question: what will the bank still do?").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Split the jobs, reconcile monthly,").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        b8_l6 = Tex("partner signs, chase what sits too long").scale(1.0).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(4)
