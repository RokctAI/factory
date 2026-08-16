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

# Band-layout whiteboard scene for the debtors/creditors control accounts duo.
# Exporter-safe primitives only; write-only reveals; camera moves down bands.
# Band time follows subtopics.json (200/190/230/220/170/180/180 of 1370 s).

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
        title = Tex("The Debtors Control Account").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Forty debtors, forty personal accounts —").scale(1.0).shift(UP * 1.1)
        l02 = Tex("but ONE summary account for the group").scale(1.05).shift(UP * 0.3)
        self.play(Write(l01)); self.wait(2)
        self.play(Write(l02)); self.wait(2)
        l03 = Tex("Detail in the Debtors Ledger,").scale(1.05).shift(DOWN * 0.7)
        l04 = Tex("TOTALS in the control account").scale(1.05).shift(DOWN * 1.5)
        self.play(Write(l03)); self.play(Write(l04))
        self.play(Create(SurroundingRectangle(VGroup(l03, l04), color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the agreement rule; which side ---
        self.next_band(1)
        b1_t = Tex("The built-in check").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_t)); self.wait(1.5)
        b1_l1 = Tex("Month end: control balance MUST equal").scale(1.05).shift(band_shift(1) + UP * 1.3)
        b1_l2 = Tex("the list of individual debtors' balances").scale(1.05).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l1)); self.play(Write(b1_l2)); self.wait(2.5)
        b1_l3 = Tex("Disagree? An error exists — hunt it").scale(1.05).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1_l3)); self.wait(2)
        b1_l4 = Tex("Debtors are an ASSET: owe us more = debit;").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        b1_l5 = Tex("owe us less = credit").scale(1.05).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l4)); self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the debit side ---
        self.next_band(2)
        b2_t = Tex("June: the debit side").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_t)); self.wait(1.5)
        # T-account rails
        t_top = Line(LEFT * 4.2 + UP * 1.6, RIGHT * 4.2 + UP * 1.6,
                     stroke_width=4).shift(band_shift(2))
        t_stem = Line(UP * 1.6, DOWN * 0.6, stroke_width=4).shift(band_shift(2))
        self.play(Create(t_top), Create(t_stem))
        b2_r1 = Tex("Balance b/d 15 400").scale(0.9).move_to([-2.2, 1.1, 0]).shift(band_shift(2))
        self.play(Write(b2_r1)); self.wait(2)
        b2_r2 = Tex("Sales (DJ total) 48 200").scale(0.9).move_to([-2.2, 0.4, 0]).shift(band_shift(2))
        self.play(Write(b2_r2)); self.wait(2)
        b2_wrong = Tex("Post each invoice to the control account").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l1 = Tex("Invoices go to personal accounts;").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        b2_l2 = Tex("the control receives only journal TOTALS").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l1)); self.play(Write(b2_l2))
        self.wait(3)

        # --- Band 3 (subtopic_3): the credit side ---
        self.next_band(3)
        b3_t = Tex("The credit side: debtors owe us less").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_t)); self.wait(1.5)
        b3_l1 = Tex("Payments received: CREDIT R31 500 (Bank)").scale(1.0).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_l1)); self.wait(2)
        b3_l2 = Tex("Returns: CREDIT R2 300").scale(1.0).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex("(Debtors Allowances)").scale(0.95).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(b3_l2)); self.play(Write(b3_l3)); self.wait(2)
        b3_l4 = Tex("Bad debt written off: CREDIT R900 (Bad Debts)").scale(0.95).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l4)); self.wait(2)
        b3_l5 = Tex("Write-off = absorb the loss —").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        b3_l6 = Tex("never overstate the asset").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5)); self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): balancing the account ---
        self.next_band(4)
        b4_t = Tex("Balance the account").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_t)); self.wait(1.5)
        b4_l1 = MathTex(r"\text{Debits: } 15\,400 + 48\,200 = 63\,600").scale(1.05).shift(band_shift(4) + UP * 1.3)
        self.play(Write(b4_l1)); self.wait(2)
        b4_l2 = MathTex(r"\text{Credits: } 31\,500 + 2\,300 + 900 = 34\,700").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l2)); self.wait(2)
        b4_l3 = MathTex(r"63\,600 - 34\,700 = 28\,900").scale(1.1).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l3)); self.wait(2)
        b4_l4 = Tex("Balance c/d credit side; b/d debit side 1 July").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l4)); self.wait(2)
        b4_l5 = Tex("Debtors as a group owe the business R28 900").scale(1.0).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): the agreement check ---
        self.next_band(5)
        b5_t = Tex("The agreement check").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_t)); self.wait(1.5)
        b5_l1 = Tex("List every debtor's balance and add:").scale(1.05).shift(band_shift(5) + UP * 1.3)
        b5_l2 = MathTex(r"\text{list total} = \text{R28 900} = \text{control balance}").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1)); self.wait(1.5)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("List says R29 800? Detail and summary").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        b5_l4 = Tex("went different ways — an error exists").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l3)); self.play(Write(b5_l4)); self.wait(2.5)
        b5_l5 = Tex("The books policing themselves — internal control").scale(0.95).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the creditors mirror image ---
        self.next_band(6)
        b6_t = Tex("Creditors Control: the mirror image").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_t)); self.wait(1.5)
        b6_l1 = Tex("Creditors = liability: balance on the CREDIT side").scale(0.95).shift(band_shift(6) + UP * 1.3)
        self.play(Write(b6_l1)); self.wait(2)
        b6_l2 = Tex("Credit purchases: owe more $\\rightarrow$ credit").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Payments and returns: owe less $\\rightarrow$ debit").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l2)); self.wait(2)
        self.play(Write(b6_l3)); self.wait(2)
        b6_l4 = Tex("Must agree with the Creditors Ledger list").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l4)); self.wait(2)
        b6_l5 = Tex("Totals only; balance; check against the list").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): counting the street twice ---
        self.next_band(7)
        b7_t = Tex("Counting the street twice").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("Pages hold the people;").scale(1.05).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex("the control line holds the street").scale(1.05).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1)); self.play(Write(b7_l2)); self.wait(2.5)
        b7_l3 = Tex("Two independent journeys: line by line daily,").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("column totals monthly").scale(1.0).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l3)); self.play(Write(b7_l4)); self.wait(2.5)
        b7_l5 = Tex("Two counts agree $\\Rightarrow$ trust both").scale(1.05).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the month in one line ---
        self.next_band(8)
        b8_t = Tex("June, one line: more owed, or less?").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Opened owing R15 400 — debit b/d").scale(1.0).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("Credit sales R48 200 — more: debit").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1)); self.wait(2)
        self.play(Write(b8_l2)); self.wait(2)
        b8_l3 = Tex("Paid R31 500; returns R2 300;").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex("bad debt R900 — all less: credit").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l3)); self.play(Write(b8_l4)); self.wait(2.5)
        b8_l5 = MathTex(r"63\,600 - 34\,700 = \text{R28 900 debit}").scale(1.05).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): when the two counts disagree ---
        self.next_band(9)
        b9_t = Tex("When the two counts disagree").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = MathTex(r"\text{Pages: } 29\,800; \quad \text{control: } 28\,900").scale(1.0).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex("R900 apart — read the clue").scale(1.05).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1)); self.wait(2)
        self.play(Write(b9_l2)); self.wait(2)
        b9_l3 = Tex("The R900 write-off never reached her page").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3)); self.wait(2)
        b9_l4 = MathTex(r"\text{Fix the page: } 28\,900 = 28\,900\ \checkmark").scale(1.05).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("Creditors: same machine in the mirror —").scale(0.95).shift(band_shift(9) + DOWN * 2.3)
        b9_l6 = Tex("we owe them, so their line grows credit-side").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l5)); self.play(Write(b9_l6))
        self.wait(4)
