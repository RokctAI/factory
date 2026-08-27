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

# Band-layout whiteboard scene for "Final Accounts and the Year-End Run"
# (grade10 term2, year-end-procedures-and-final-accounts). One band per
# teaching beat, add-only lifecycle, camera moves down between bands.
# Exporter-safe mobjects only (Tex/MathTex/Line/Rectangle/
# SurroundingRectangle/VGroup).
#
# Subtopic time shares (subtopics.json, total 1400 s):
# 210/220/220/200/180/190/180 -> bands 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FinalAccountsYearEndRunSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the bridge and its sequence ---
        title = Tex("Final Accounts and the Year-End Run").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("The books describe the year AS RECORDED;").scale(1.0).shift(UP * 1.2)
        b0_l2 = Tex("some year-end truths have no document").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Adjustments align the records with fact").scale(1.05).shift(DOWN * 0.5)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("PRE-adjustment trial balance: the routine;").scale(0.95).shift(DOWN * 1.4)
        b0_l5 = Tex("POST-adjustment: what final accounts use").scale(0.95).shift(DOWN * 2.2)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the GAAP authority ---
        self.next_band(1)
        b1_title = Tex("The authority is GAAP").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Matching: this year's incomes against").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("this year's expenses -- no more, no less").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Prudence: losses recognised when").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex("discovered, not when convenient").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("Going concern holds useful values;").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        b1_l6 = Tex("historical cost anchors the prices").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): consumable stores on hand ---
        self.next_band(2)
        b2_title = Tex("Adjustment 1: stationery on hand").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Stationery account: R1 000 expensed;").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("the cupboard still holds R200").scale(1.05).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_w = Tex("Did the business use R1 000? No -- R800").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_w))
        self.wait(2)
        b2_l3 = Tex("Credit Stationery R200; debit").scale(1.05).shift(band_shift(2) + DOWN * 1.5)
        b2_l4 = Tex("Consumable Stores on Hand R200").scale(1.05).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex("Expense reports the used; the asset").scale(0.95).shift(band_shift(2) + DOWN * 3.1)
        b2_l6 = Tex("carries the rest into next year").scale(0.95).shift(band_shift(2) + DOWN * 3.8)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): the trading stock deficit ---
        self.next_band(3)
        b3_title = Tex("Adjustment 2: trading stock deficit").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Account claims R2 400; the count").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("finds R2 250 -- the shelf is the fact").scale(1.05).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_m = MathTex(r"2\,400 - 2\,250 = \text{R150 gone}").scale(1.1).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_m))
        self.wait(2)
        b3_l3 = Tex("Credit Trading Stock R150; debit").scale(1.05).shift(band_shift(3) + DOWN * 1.5)
        b3_l4 = Tex("Trading Stock Deficit (expense) R150").scale(1.05).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("Adjusted, but still balanced -- every").scale(0.95).shift(band_shift(3) + DOWN * 3.1)
        b3_l6 = Tex("adjustment was a full double entry").scale(0.95).shift(band_shift(3) + DOWN * 3.8)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): the Trading account ---
        self.next_band(4)
        b4_title = Tex("The Trading account: gross profit").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Close Sales R100 000 to its credit;").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("close Cost of Sales R80 000 to its debit").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_m1 = MathTex(r"100\,000 - 80\,000 = \text{R20 000 gross profit}").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_m1))
        self.play(Create(SurroundingRectangle(b4_m1, color=GREEN)))
        self.wait(2.5)
        b4_m2 = MathTex(r"\text{Check: } 25\% \times 80\,000 = 20\,000").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_m2))
        self.wait(2)
        b4_l3 = Tex("The final accounts confirm what the").scale(0.95).shift(band_shift(4) + DOWN * 2.6)
        b4_l4 = Tex("mark-up policy promised").scale(0.95).shift(band_shift(4) + DOWN * 3.3)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): Profit and Loss, and Capital ---
        self.next_band(5)
        b5_title = Tex("Profit and Loss: the net profit").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Credit side: } 20\,000 + 6\,000 = 26\,000").scale(1.0).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Debits: salaries 12 000, phone 1 200,").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("stationery 800, bank charges 350,").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("stock deficit 150").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_m1 = MathTex(r"26\,000 - 14\,500 = \text{R11 500 net profit}").scale(1.05).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_m1))
        self.play(Create(SurroundingRectangle(b5_m1, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex("Transfer to Capital -- the profit was").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        b5_l6 = Tex("always the owner's").scale(0.95).shift(band_shift(5) + DOWN * 3.7)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): the run, in order ---
        self.next_band(6)
        b6_title = Tex("The year-end run, in order").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("1. Pre-adjustment trial balance").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("2. Adjustments, journalised with narrations").scale(0.95).shift(band_shift(6) + UP * 0.5)
        b6_l3 = Tex("3. Post-adjustment trial balance").scale(1.0).shift(band_shift(6) + DOWN * 0.2)
        b6_l4 = Tex("4. Final accounts: Trading, then P\\&L").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        b6_l5 = Tex("5. Profit to Capital").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        b6_l6 = Tex("6. The financial statements").scale(1.0).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6_l1))
        self.wait(1.5)
        self.play(Write(b6_l2))
        self.wait(1.5)
        self.play(Write(b6_l3))
        self.wait(1.5)
        self.play(Write(b6_l4))
        self.wait(1.5)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(2)
        b6_l7 = Tex("Each step certifies the next: the").scale(1.0).shift(band_shift(6) + DOWN * 3.1)
        b6_l8 = Tex("order IS the control").scale(1.0).shift(band_shift(6) + DOWN * 3.8)
        self.play(Write(b6_l7))
        self.play(Write(b6_l8))
        self.wait(3)

        # --- Band 7 (subtopic_4): three exam habits ---
        self.next_band(7)
        b7_title = Tex("Three exam habits").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_w = Tex("Half an adjustment -- one account only").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_w))
        self.play(Create(strike(b7_w)))
        self.wait(1.5)
        b7_l1 = Tex("1. Every adjustment: both accounts,").scale(1.0).shift(band_shift(7) + UP * 0.2)
        b7_l2 = Tex("both directions").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("2. Track downstream: one fact, two").scale(1.0).shift(band_shift(7) + DOWN * 1.3)
        b7_l4 = Tex("appearances -- expense AND asset").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("3. Pair step with principle: matching,").scale(1.0).shift(band_shift(7) + DOWN * 2.8)
        b7_l6 = Tex("prudence, going concern").scale(1.0).shift(band_shift(7) + DOWN * 3.5)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): report card day ---
        self.next_band(8)
        b8_title = Tex("The shop's report card day").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("The diary records what was written --").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("some lines drifted from the truth").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Cupboard: R200 of ``spent'' stationery").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        b8_l4 = Tex("still there; shelf: R2 250, not R2 400").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Two jobs in strict order: TIDY the").scale(1.0).shift(band_shift(8) + DOWN * 2.3)
        b8_l6 = Tex("diary first, THEN squeeze the report").scale(1.0).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the two tidyings ---
        self.next_band(9)
        b9_title = Tex("Tidying the room before the photo").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Stationery: R800 truly used stays the").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("expense; R200 waiting becomes an asset").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Shelf count: the shelf always wins --").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        b9_l4 = Tex("books down R150, loss named and").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        b9_l5 = Tex("admitted NOW, not next year").scale(1.0).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2.5)
        b9_l6 = Tex("Bad news immediately; good news").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        b9_l7 = Tex("waits to be proven -- prudence").scale(1.0).shift(band_shift(9) + DOWN * 3.6)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.wait(3)

        # --- Band 10 (subtopic_7): two sieves and the owner's jar ---
        self.next_band(10)
        b10_title = Tex("Two sieves and the owner's jar").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Sieve one, buying-and-selling:").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_m1 = MathTex(r"100\,000 - 80\,000 = \text{R20 000 gross}").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_m1))
        self.wait(2.5)
        b10_l2 = Tex("Sieve two, running the shop:").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        b10_m2 = MathTex(r"20\,000 + 6\,000 - 14\,500 = \text{R11 500 net}").scale(1.0).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10_l2))
        self.play(Write(b10_m2))
        self.play(Create(SurroundingRectangle(b10_m2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex("R11 500 into the owner's jar -- Capital;").scale(1.0).shift(band_shift(10) + DOWN * 2.1)
        b10_l4 = Tex("the year's pages stand clean for the new").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(4)
