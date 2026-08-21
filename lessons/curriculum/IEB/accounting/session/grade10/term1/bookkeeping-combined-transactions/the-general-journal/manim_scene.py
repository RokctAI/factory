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

# Band-layout whiteboard scene for the general-journal session duo.
# Exporter-safe primitives only (Tex/MathTex/Line/Arrow/Rectangle/VGroup);
# write-only reveals. Band time follows subtopics.json
# (190/210/190/190/170/190/170 of 1310 s).

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
        l01 = Tex("For transactions no specialised").scale(1.0).shift(UP * 1.2)
        l02 = Tex("journal accommodates").scale(1.0).shift(UP * 0.4)
        self.play(Write(l01)); self.play(Write(l02)); self.wait(2.5)
        l03 = Tex("Debit line; indented credit line;").scale(0.95).shift(DOWN * 0.6)
        l04 = Tex("NARRATION — one honest sentence").scale(0.95).shift(DOWN * 1.4)
        self.play(Write(l03)); self.wait(2)
        self.play(Write(l04))
        self.play(Create(SurroundingRectangle(l04, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): you name both sides; analysis columns ---
        self.next_band(1)
        b1_t = Tex("No columns think for you here").scale(1.15).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_t)); self.wait(2)
        b1_l1 = Tex("YOU name both sides of every entry —").scale(0.95).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("pure double-entry analysis").scale(1.0).shift(band_shift(1) + UP * 0.6)
        self.play(Write(b1_l1)); self.play(Write(b1_l2)); self.wait(2.5)
        b1_l3 = Tex("Analysis columns: Debtors Control dr/cr,").scale(0.9).shift(band_shift(1) + DOWN * 0.4)
        b1_l4 = Tex("Creditors Control dr/cr — totals monthly").scale(0.9).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3)); self.play(Write(b1_l4)); self.wait(2)
        b1_l5 = Tex("Personal accounts: daily, as always").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): bad debts ---
        self.next_band(2)
        b2_t = Tex("Classic 1: the bad debt").scale(1.2).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_t)); self.wait(2)
        b2_l1 = Tex("N. Mahlangu owes R1 100 — gone").scale(1.0).shift(band_shift(2) + UP * 1.4)
        self.play(Write(b2_l1)); self.wait(2)
        b2_l2 = Tex("Debit Bad Debts 1 100 — the loss absorbed").scale(0.95).shift(band_shift(2) + UP * 0.5)
        b2_l3 = Tex("Credit Debtors Control 1 100 — asset removed").scale(0.95).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(b2_l2)); self.play(Write(b2_l3)); self.wait(2.5)
        b2_l4 = Tex("No cash moved: an asset died,").scale(0.95).shift(band_shift(2) + DOWN * 1.2)
        b2_l5 = Tex("an expense was born").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4)); self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): interest, both directions ---
        self.next_band(3)
        b3_t = Tex("Classic 2: interest on overdue accounts").scale(1.05).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_t)); self.wait(2)
        b3_l1 = Tex("Pillay 60 days late: charge R60").scale(0.95).shift(band_shift(3) + UP * 1.4)
        b3_l2 = Tex("Debit Debtors Control; credit Interest Income").scale(0.9).shift(band_shift(3) + UP * 0.6)
        self.play(Write(b3_l1)); self.play(Write(b3_l2)); self.wait(2.5)
        b3_l3 = Tex("Mirror: Coastal charges US R150").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = Tex("Debit Interest Expense; credit Creditors Control").scale(0.85).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_l3)); self.wait(2)
        self.play(Write(b3_l4)); self.wait(2)
        b3_l5 = Tex("Through the GJ: the DEBT grew, not the cash").scale(0.9).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_2): drawings of stock ---
        self.next_band(4)
        b4_t = Tex("Classic 3: drawings of stock").scale(1.15).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_t)); self.wait(2)
        b4_l1 = Tex("Owner takes goods costing R480 home").scale(0.95).shift(band_shift(4) + UP * 1.4)
        self.play(Write(b4_l1)); self.wait(2)
        b4_l2 = Tex("Debit Drawings 480; credit Trading Stock 480").scale(0.9).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l2)); self.wait(2)
        b4_wrong = Tex("Record at the marked-up selling price").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        b4_l3 = Tex("At COST, always — no sale occurred").scale(0.95).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): correcting errors without erasing ---
        self.next_band(5)
        b5_t = Tex("Correct without erasing").scale(1.2).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_t)); self.wait(2)
        b5_l1 = Tex("Was done: Trading Stock debited R320").scale(0.95).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("Should have been: Stationery debited R320").scale(0.95).shift(band_shift(5) + UP * 0.6)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        b5_l3 = Tex("Fix: debit Stationery 320;").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        b5_l4 = Tex("credit Trading Stock 320 — narrated").scale(0.95).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3)); self.play(Write(b5_l4)); self.wait(2.5)
        b5_l5 = Tex("Only the broken leg — the credit was right").scale(0.9).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): control columns and the month's proof ---
        self.next_band(6)
        b6_t = Tex("Month end: columns and proof").scale(1.15).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_t)); self.wait(2)
        b6_l1 = Tex("Debtors Control: dr 60, cr 1 100;").scale(0.95).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("Creditors Control: cr 150 — totals post").scale(0.95).shift(band_shift(6) + UP * 0.6)
        self.play(Write(b6_l1)); self.play(Write(b6_l2)); self.wait(2.5)
        b6_l3 = MathTex(r"1\,100 + 60 + 150 + 480 + 320 = 2\,110").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l3)); self.wait(2)
        b6_l4 = Tex("Credits also total 2 110 — balanced").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("Six journals: every event, one front door").scale(0.9).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the odd-jobs notebook ---
        self.next_band(7)
        b7_t = Tex("The odd-jobs notebook").scale(1.2).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("Mrs Mahlangu's R1 100: no money in,").scale(0.95).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("none out, nothing sold or returned").scale(0.95).shift(band_shift(7) + UP * 0.6)
        self.play(Write(b7_l1)); self.play(Write(b7_l2)); self.wait(2.5)
        b7_l3 = Tex("Every specialised diary shrugs — GJ").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        self.play(Write(b7_l3)); self.wait(2)
        b7_l4 = Tex("Tell the story in full: up, down, and WHY").scale(0.9).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l4)); self.wait(2)
        b7_l5 = Tex("The five-step analysis, holding a pen").scale(0.9).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): three stories ---
        self.next_band(8)
        b8_t = Tex("Three stories the big diaries can't tell").scale(1.0).shift(band_shift(8) + UP * 2.5)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("The funeral: R1 100 buried, loss recorded").scale(0.9).shift(band_shift(8) + UP * 1.4)
        b8_l2 = Tex("Home-shopping: R480 at COST — drawings").scale(0.9).shift(band_shift(8) + UP * 0.5)
        b8_l3 = Tex("Lateness priced: R60 earned, R150 paid").scale(0.9).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l1)); self.wait(2)
        self.play(Write(b8_l2)); self.wait(2)
        self.play(Write(b8_l3)); self.wait(2)
        b8_l4 = Tex("The books charge both directions,").scale(0.95).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = Tex("without favouritism").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l4)); self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): fixing mistakes in pen ---
        self.next_band(9)
        b9_t = Tex("Fixing mistakes in pen").scale(1.2).shift(band_shift(9) + UP * 2.5)
        self.play(Write(b9_t)); self.wait(2)
        b9_wrong = Tex("Erase it, paint it, tear out the page").scale(0.95).shift(band_shift(9) + UP * 1.4)
        self.play(Write(b9_wrong))
        self.play(Create(strike(b9_wrong)))
        self.wait(2)
        b9_l1 = Tex("New entry: Stationery up 320,").scale(0.95).shift(band_shift(9) + UP * 0.4)
        b9_l2 = Tex("Trading Stock down 320 — dated, explained").scale(0.9).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l1)); self.play(Write(b9_l2)); self.wait(2.5)
        b9_l3 = Tex("Mistake visible, repair beside it:").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        b9_l4 = Tex("the audit trail — trust in ink").scale(1.0).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l3)); self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(4)
