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

# Band-layout whiteboard scene for the double-entry / accounting-equation
# session duo. Exporter-safe primitives only (Tex/MathTex/Line/Arrow/
# Rectangle/VGroup); write-only reveals. Band time follows subtopics.json
# (200/230/210/240/160/190/170 of 1400 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DoubleEntryAccountingEquationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(15)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the equation ---
        title = Tex("The Accounting Equation").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Everything owned was funded by somebody").scale(1.0).shift(UP * 1.2)
        self.play(Write(l01)); self.wait(2)
        eq = MathTex("A = O + L").scale(1.6).shift(UP * 0.1)
        self.play(Write(eq)); self.wait(2)
        l02 = Tex("A: assets — what the business owns").scale(0.9).shift(DOWN * 1.0)
        l03 = Tex("O: owner's equity — the owner's funding").scale(0.9).shift(DOWN * 1.8)
        l04 = Tex("L: liabilities — outsiders' funding").scale(0.9).shift(DOWN * 2.6)
        self.play(Write(l02)); self.wait(1.5)
        self.play(Write(l03)); self.wait(1.5)
        self.play(Write(l04))
        self.wait(3)

        # --- Band 1 (subtopic_1): sides and the double-entry principle ---
        self.next_band(1)
        b1_t = Tex("Sides, and the double-entry promise").scale(1.15).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_t)); self.wait(2)
        b1_l1 = Tex("Assets grow on the DEBIT side, left").scale(1.0).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("O and L grow on the CREDIT side, right").scale(1.0).shift(band_shift(1) + UP * 0.6)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        b1_l3 = Tex("Decreases: opposite side, every time").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l3)); self.wait(2)
        b1_l4 = Tex("Every transaction: two accounts,").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        b1_l5 = Tex("total debits = total credits").scale(1.05).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l4)); self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): transaction (a) capital ---
        self.next_band(2)
        b2_t = Tex("(a) Owner deposits R80 000 capital").scale(1.1).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_t)); self.wait(2)
        b2_l1 = Tex("Bank, an asset: up R80 000").scale(1.0).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("Capital, owner's equity: up R80 000").scale(1.0).shift(band_shift(2) + UP * 0.6)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2)); self.wait(2)
        b2_l3 = Tex("Debit Bank 80 000; credit Capital 80 000").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_l3)); self.wait(2)
        b2_l4 = Tex("Left up 80 000, right up 80 000: level").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): transaction (b) asset swap ---
        self.next_band(3)
        b3_t = Tex("(b) Scooter R24 000, paid cash").scale(1.1).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_t)); self.wait(2)
        b3_l1 = Tex("Vehicles up 24 000; Bank down 24 000").scale(1.0).shift(band_shift(3) + UP * 1.4)
        self.play(Write(b3_l1)); self.wait(2)
        b3_l2 = Tex("An asset SWAP: net effect on A is nil").scale(1.0).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l2)); self.wait(2)
        b3_wrong = Tex("No equation change, so no entries").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l3 = Tex("Debit Vehicles 24 000; credit Bank 24 000").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        b3_l4 = Tex("Two entries, always").scale(1.05).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l3)); self.wait(2)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): transaction (c) credit purchase ---
        self.next_band(4)
        b4_t = Tex("(c) Stock R15 000 bought on credit").scale(1.1).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_t)); self.wait(2)
        b4_l1 = Tex("Trading Stock, an asset: up 15 000").scale(1.0).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("Creditors, a liability: up 15 000").scale(1.0).shift(band_shift(4) + UP * 0.6)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2)
        b4_l3 = Tex("Debit Trading Stock 15 000;").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex("credit Creditors Control 15 000").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l3)); self.play(Write(b4_l4)); self.wait(2)
        b4_l5 = Tex("Both sides up 15 000: level").scale(1.0).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): transaction (d) paying the creditor ---
        self.next_band(5)
        b5_t = Tex("(d) Pay a creditor R6 000").scale(1.1).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_t)); self.wait(2)
        b5_l1 = Tex("Bank, an asset: down 6 000").scale(1.0).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("Creditors, a liability: down 6 000").scale(1.0).shift(band_shift(5) + UP * 0.6)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        b5_l3 = Tex("Debit Creditors Control 6 000;").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("credit Bank 6 000").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l3)); self.play(Write(b5_l4)); self.wait(2)
        b5_l5 = Tex("Both sides down 6 000: still level").scale(1.0).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): verifying the whole picture ---
        self.next_band(6)
        b6_t = Tex("Verify: add everything up").scale(1.15).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_t)); self.wait(2)
        b6_l1 = Tex("Bank: 80 000 $-$ 24 000 $-$ 6 000 = 50 000").scale(0.95).shift(band_shift(6) + UP * 1.5)
        b6_l2 = Tex("Vehicles 24 000; Trading Stock 15 000").scale(0.95).shift(band_shift(6) + UP * 0.7)
        b6_l3 = Tex("Total assets: R89 000").scale(1.05).shift(band_shift(6) + DOWN * 0.1)
        self.play(Write(b6_l1)); self.wait(2)
        self.play(Write(b6_l2)); self.wait(2)
        self.play(Write(b6_l3)); self.wait(2)
        b6_l4 = Tex("O: 80 000; L: 15 000 $-$ 6 000 = 9 000").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        b6_l5 = Tex("O + L = 89 000 = A").scale(1.1).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l4)); self.wait(2)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): incomes, expenses, five steps ---
        self.next_band(7)
        b7_t = Tex("Incomes and expenses live inside O").scale(1.1).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("Income: O up, credit side").scale(1.0).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("Expense: O down, debit side").scale(1.0).shift(band_shift(7) + UP * 0.6)
        self.play(Write(b7_l1)); self.wait(2)
        self.play(Write(b7_l2)); self.wait(2)
        b7_l3 = Tex("Wages R1 800: debit Wages, credit Bank").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(b7_l3)); self.wait(2)
        b7_l4 = Tex("Five steps: accounts, classify, direction,").scale(0.9).shift(band_shift(7) + DOWN * 1.4)
        b7_l5 = Tex("sides, equation check").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l4)); self.play(Write(b7_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the two-pocket rule ---
        self.next_band(8)
        b8_t = Tex("The two-pocket rule").scale(1.2).shift(band_shift(8) + UP * 2.5)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Your bicycle: own money, or owed money").scale(1.0).shift(band_shift(8) + UP * 1.4)
        b8_l2 = Tex("There is no third pocket").scale(1.05).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1)); self.wait(2)
        self.play(Write(b8_l2)); self.wait(2)
        b8_l3 = Tex("Owned = owner's pocket + owed pocket").scale(1.05).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3)); self.wait(2)
        b8_l4 = Tex("Assets = Owner's equity + Liabilities").scale(1.05).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): four moves on the kitchen table ---
        self.next_band(9)
        b9_t = Tex("Four moves on the kitchen table").scale(1.15).shift(band_shift(9) + UP * 2.5)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = Tex("1. R80 000 in: owned up, owner's pocket up").scale(0.9).shift(band_shift(9) + UP * 1.4)
        b9_l2 = Tex("2. Scooter for cash: shuffle inside owned").scale(0.9).shift(band_shift(9) + UP * 0.6)
        b9_l3 = Tex("3. Stock on credit: owned up, owed up").scale(0.9).shift(band_shift(9) + DOWN * 0.2)
        b9_l4 = Tex("4. Pay R6 000: owned down, owed down").scale(0.9).shift(band_shift(9) + DOWN * 1.0)
        for m in (b9_l1, b9_l2, b9_l3, b9_l4):
            self.play(Write(m))
            self.wait(1.8)
        b9_l5 = Tex("The table never tips: that IS double entry").scale(1.0).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the question that never fails ---
        self.next_band(10)
        b10_t = Tex("Which two places, and which way?").scale(1.15).shift(band_shift(10) + UP * 2.5)
        self.play(Write(b10_t)); self.wait(2)
        b10_l1 = Tex("Wages R1 800: owned pile down;").scale(1.0).shift(band_shift(10) + UP * 1.3)
        b10_l2 = Tex("owner's pocket down — an expense").scale(1.0).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1)); self.wait(2)
        self.play(Write(b10_l2)); self.wait(2)
        b10_l3 = Tex("Expenses: debit. Incomes: credit.").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        b10_l4 = Tex("Just the owner's pocket, shrinking and growing").scale(0.9).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l3)); self.wait(2)
        self.play(Write(b10_l4)); self.wait(2)
        b10_l5 = Tex("Two places, two directions, one level table").scale(1.0).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l5))
        self.wait(4)
