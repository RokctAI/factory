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

# Band-layout whiteboard scene for the debtors/creditors-control session duo.
# Exporter-safe primitives only (Tex/MathTex/Line/Arrow/Rectangle/VGroup);
# write-only reveals. Band time follows subtopics.json
# (200/190/230/220/170/180/180 of 1370 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DebtorsCreditorsControlSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(15)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): what a control account is ---
        title = Tex("The Debtors Control Account").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Forty debtors, forty personal accounts —").scale(0.95).shift(UP * 1.1)
        l02 = Tex("one question: what do they ALL owe?").scale(1.0).shift(UP * 0.3)
        self.play(Write(l01)); self.play(Write(l02)); self.wait(2.5)
        l03 = Tex("One summary account: totals only").scale(1.0).shift(DOWN * 0.7)
        self.play(Write(l03)); self.wait(2)
        l04 = Tex("Detail in the Debtors Ledger,").scale(0.95).shift(DOWN * 1.6)
        l05 = Tex("totals in Debtors Control").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(l04)); self.play(Write(l05))
        self.wait(3)

        # --- Band 1 (subtopic_1): the agreement rule; which side ---
        self.next_band(1)
        b1_t = Tex("The agreement rule").scale(1.2).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_t)); self.wait(2)
        b1_l1 = Tex("Control balance = total of the").scale(1.0).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("list of debtors' balances").scale(1.0).shift(band_shift(1) + UP * 0.6)
        self.play(Write(b1_l1)); self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Debtors: an asset — owe us MORE, debit;").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex("owe us LESS, credit").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(b1_l3)); self.play(Write(b1_l4)); self.wait(2)
        b1_l5 = Tex("Ask it every time: more, or less?").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the debit side ---
        self.next_band(2)
        b2_t = Tex("The debit side: owing us more").scale(1.15).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_t)); self.wait(2)
        b2_l1 = Tex("1 Aug: Balance b/d R18 700").scale(1.0).shift(band_shift(2) + UP * 1.4)
        self.play(Write(b2_l1)); self.wait(2)
        b2_l2 = Tex("Credit sales: DJ total R52 600 — one entry").scale(0.95).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l2)); self.wait(2)
        b2_wrong = Tex("Post each invoice to control").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        b2_l3 = Tex("Totals only — that IS the control").scale(0.95).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l3)); self.wait(2)
        b2_l4 = Tex("Debit side so far: R71 300").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): the credit side ---
        self.next_band(3)
        b3_t = Tex("The credit side: owing us less").scale(1.15).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_t)); self.wait(2)
        b3_l1 = Tex("Payments in: Bank R36 400").scale(1.0).shift(band_shift(3) + UP * 1.4)
        b3_l2 = Tex("Returns: Debtors Allowances R3 100").scale(1.0).shift(band_shift(3) + UP * 0.5)
        b3_l3 = Tex("Write-off: Bad Debts R1 200").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2)); self.wait(2)
        self.play(Write(b3_l3)); self.wait(2)
        b3_l4 = Tex("A write-off: no money received —").scale(0.95).shift(band_shift(3) + DOWN * 1.4)
        b3_l5 = Tex("the loss absorbed, the asset un-claimed").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l4)); self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): balancing the account ---
        self.next_band(4)
        b4_t = Tex("Balance the account").scale(1.2).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_t)); self.wait(2)
        b4_l1 = MathTex(r"18\,700 + 52\,600 = 71\,300").scale(1.0).shift(band_shift(4) + UP * 1.4)
        b4_l2 = MathTex(r"36\,400 + 3\,100 + 1\,200 = 40\,700").scale(1.0).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2)
        b4_l3 = MathTex(r"71\,300 - 40\,700 = 30\,600").scale(1.05).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = Tex("Balance c/d credit; b/d debit 1 Sep —").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        b4_l5 = Tex("debtors owe the business R30 600").scale(0.95).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4_l4)); self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): the agreement check ---
        self.next_band(5)
        b5_t = Tex("The agreement check").scale(1.2).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_t)); self.wait(2)
        b5_l1 = Tex("List every personal balance; add the list").scale(0.95).shift(band_shift(5) + UP * 1.4)
        self.play(Write(b5_l1)); self.wait(2)
        b5_l2 = Tex("It must land on R30 600 exactly").scale(1.0).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2)
        b5_l3 = Tex("R31 800 instead? An error exists —").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("detail and summary took different roads").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l3)); self.play(Write(b5_l4)); self.wait(2)
        b5_l5 = Tex("The books policing themselves").scale(1.0).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the creditors mirror image ---
        self.next_band(6)
        b6_t = Tex("The creditors mirror").scale(1.2).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_t)); self.wait(2)
        b6_l1 = Tex("Creditors: a liability — balance credit side").scale(0.95).shift(band_shift(6) + UP * 1.4)
        self.play(Write(b6_l1)); self.wait(2)
        b6_l2 = Tex("Credit purchases: owe more — credit").scale(0.95).shift(band_shift(6) + UP * 0.5)
        b6_l3 = Tex("Payments and returns: owe less — debit").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(b6_l2)); self.wait(2)
        self.play(Write(b6_l3)); self.wait(2)
        b6_l4 = Tex("Same lock: control = list of creditors").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l4)); self.wait(2)
        b6_l5 = Tex("Understand one side; the other comes free").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): counting the street twice ---
        self.next_band(7)
        b7_t = Tex("Counting the street twice").scale(1.2).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("Pages: the people, line by line, daily").scale(0.95).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("Control line: the street, totals, monthly").scale(0.95).shift(band_shift(7) + UP * 0.6)
        self.play(Write(b7_l1)); self.wait(2)
        self.play(Write(b7_l2)); self.wait(2)
        b7_l3 = Tex("Two independent journeys —").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("they MUST meet at the same number").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3)); self.play(Write(b7_l4)); self.wait(2)
        b7_l5 = Tex("The street auditing itself").scale(1.0).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the month in one line ---
        self.next_band(8)
        b8_t = Tex("August in one line").scale(1.2).shift(band_shift(8) + UP * 2.5)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Already owed: 18 700 — debit").scale(0.95).shift(band_shift(8) + UP * 1.4)
        b8_l2 = Tex("Sold on trust: 52 600 — more: debit").scale(0.95).shift(band_shift(8) + UP * 0.6)
        b8_l3 = Tex("Paid in: 36 400 — less: credit").scale(0.95).shift(band_shift(8) + DOWN * 0.2)
        b8_l4 = Tex("Returned: 3 100; buried: 1 200 — credit").scale(0.95).shift(band_shift(8) + DOWN * 1.0)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4):
            self.play(Write(m))
            self.wait(1.8)
        b8_l5 = Tex("The line settles: R30 600, debit").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): when the two counts disagree ---
        self.next_band(9)
        b9_t = Tex("When the two counts disagree").scale(1.15).shift(band_shift(9) + UP * 2.5)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = Tex("Pages: 31 800. Line: 30 600.").scale(1.0).shift(band_shift(9) + UP * 1.4)
        self.play(Write(b9_l1)); self.wait(2)
        b9_l2 = Tex("Gap: R1 200 — read the clue").scale(1.0).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l2)); self.wait(2)
        b9_l3 = Tex("The bad debt never reached the page").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l3)); self.wait(2)
        b9_l4 = Tex("Fix the page: 30 600 = 30 600").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("Records that check records — both streets").scale(0.95).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l5))
        self.wait(4)
