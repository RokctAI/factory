# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene for the double-entry / accounting-equation duo.
# Exporter-safe primitives only; write-only reveals, camera moves down bands.
# Band time follows subtopics.json (200/230/210/240/160/190/170 of 1400 s).

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
        l01 = Tex("Owns = assets (A); owner supplied = equity (O);").scale(0.95).shift(UP * 1.1)
        l02 = Tex("outsiders supplied = liabilities (L)").scale(1.0).shift(UP * 0.3)
        self.play(Write(l01)); self.wait(2)
        self.play(Write(l02)); self.wait(2)
        eq = MathTex(r"A = O + L").scale(1.5).shift(DOWN * 0.8)
        self.play(Write(eq))
        self.play(Create(SurroundingRectangle(eq, color=GREEN)))
        self.wait(2.5)
        l03 = Tex("True at every moment — if it stops").scale(1.0).shift(DOWN * 2.0)
        l04 = Tex("balancing, the books contain an error").scale(1.0).shift(DOWN * 2.8)
        self.play(Write(l03)); self.play(Write(l04))
        self.wait(3)

        # --- Band 1 (subtopic_1): sides and the double-entry principle ---
        self.next_band(1)
        b1_t = Tex("Debit left, credit right").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_t)); self.wait(1.5)
        # T-account rails
        t_top = Line(LEFT * 3.0 + UP * 1.5, RIGHT * 3.0 + UP * 1.5,
                     stroke_width=4).shift(band_shift(1))
        t_stem = Line(UP * 1.5, DOWN * 0.6, stroke_width=4).shift(band_shift(1))
        self.play(Create(t_top), Create(t_stem))
        t_dr = Tex("Debit").scale(1.0).move_to([-1.6, 1.0, 0]).shift(band_shift(1))
        t_cr = Tex("Credit").scale(1.0).move_to([1.6, 1.0, 0]).shift(band_shift(1))
        self.play(Write(t_dr), Write(t_cr)); self.wait(2)
        b1_l1 = Tex("Assets increase on the DEBIT side").scale(1.05).shift(band_shift(1) + DOWN * 1.2)
        b1_l2 = Tex("O and L increase on the CREDIT side").scale(1.05).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        b1_l3 = Tex("Every transaction: total debits = total credits").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l3))
        self.wait(3)

        # --- Band 2 (subtopic_2): transaction (a) capital ---
        self.next_band(2)
        b2_t = Tex("(a) Owner deposits capital R100 000").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_t)); self.wait(2)
        b2_l1 = Tex("Bank grew: A up R100 000").scale(1.05).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex("Funded by the owner: O up R100 000").scale(1.05).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2)); self.wait(2)
        b2_l3 = MathTex(r"A\ +100\,000; \quad O\ +100\,000; \quad L\ 0").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_l3)); self.wait(2)
        b2_l4 = Tex("Debit Bank R100 000; Credit Capital R100 000").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex("Record the BUSINESS's view, never the owner's").scale(0.95).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): transaction (b) asset swap ---
        self.next_band(3)
        b3_t = Tex("(b) Buys equipment R30 000, pays cash").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_t)); self.wait(2)
        b3_l1 = Tex("Asset swap: Equipment up, Bank down").scale(1.05).shift(band_shift(3) + UP * 1.3)
        b3_l2 = MathTex(r"A\ +30\,000 - 30\,000 = 0; \quad O, L\ \text{unchanged}").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2)); self.wait(2)
        b3_wrong = Tex("No effect on A $\\Rightarrow$ no entries needed").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l3 = Tex("There are ALWAYS two entries:").scale(1.05).shift(band_shift(3) + DOWN * 1.5)
        b3_l4 = Tex("Debit Equipment R30 000; Credit Bank R30 000").scale(1.0).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l3)); self.wait(1.5)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): transaction (c) credit purchase ---
        self.next_band(4)
        b4_t = Tex("(c) Buys trading stock on credit R12 000").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_t)); self.wait(2)
        b4_l1 = Tex("Stock arrives: A up R12 000").scale(1.05).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("Owes a supplier: L up R12 000; O unchanged").scale(1.0).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2)
        b4_l3 = Tex("Left up R12 000, right up R12 000 — balanced").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l3)); self.wait(2)
        b4_l4 = Tex("Debit Trading Stock R12 000;").scale(1.05).shift(band_shift(4) + DOWN * 1.4)
        b4_l5 = Tex("Credit Creditors Control R12 000").scale(1.05).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l4)); self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): transaction (d) paying the creditor ---
        self.next_band(5)
        b5_t = Tex("(d) Pays a creditor R5 000").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_t)); self.wait(2)
        b5_l1 = MathTex(r"A\ -5\,000; \quad L\ -5\,000; \quad O\ \text{unchanged}").scale(1.0).shift(band_shift(5) + UP * 1.3)
        self.play(Write(b5_l1)); self.wait(2)
        b5_l2 = Tex("Debit Creditors Control R5 000;").scale(1.05).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("Credit Bank R5 000").scale(1.05).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l2)); self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex("Pattern: every transaction — one debit,").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        b5_l5 = Tex("one credit, equal; equation always level").scale(1.0).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l4)); self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): verifying the whole picture ---
        self.next_band(6)
        b6_t = Tex("Verify the whole picture").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_t)); self.wait(1.5)
        b6_l1 = MathTex(r"\text{Bank: } 100\,000 - 30\,000 - 5\,000 = 65\,000").scale(0.95).shift(band_shift(6) + UP * 1.4)
        self.play(Write(b6_l1)); self.wait(2)
        b6_l2 = MathTex(r"A = 65\,000 + 30\,000 + 12\,000 = 107\,000").scale(0.95).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l2)); self.wait(2)
        b6_l3 = MathTex(r"O = 100\,000; \quad L = 12\,000 - 5\,000 = 7\,000").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l3)); self.wait(2)
        b6_l4 = MathTex(r"O + L = 100\,000 + 7\,000 = 107\,000 = A\ \checkmark").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2.5)
        b6_l5 = Tex("Totals disagree? Hunt the unequal entry").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): incomes, expenses, five steps ---
        self.next_band(7)
        b7_t = Tex("Incomes and expenses live inside O").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("Income: O up $\\rightarrow$ credit side").scale(1.05).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex("Expense: O down $\\rightarrow$ debit side").scale(1.05).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1)); self.wait(2)
        self.play(Write(b7_l2)); self.wait(2)
        b7_l3 = Tex("Paid wages R2 000: debit Wages, credit Bank").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(b7_l3)); self.wait(2)
        b7_l4 = Tex("Routine: name 2 accounts; classify;").scale(1.0).shift(band_shift(7) + DOWN * 1.3)
        b7_l5 = Tex("up or down; apply sides; check A = O + L").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l4)); self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(VGroup(b7_l4, b7_l5), color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the two-pocket rule ---
        self.next_band(8)
        b8_t = Tex("The two-pocket rule").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Everything owned was paid from one of").scale(1.05).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("two pockets: own money, or owed money").scale(1.05).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1)); self.play(Write(b8_l2)); self.wait(2.5)
        b8_l3 = Tex("Owned = assets; owner's pocket = equity;").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex("owed pocket = liabilities").scale(1.05).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l3)); self.play(Write(b8_l4)); self.wait(2)
        b8_l5 = MathTex(r"A = O + L").scale(1.3).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): four moves on the kitchen table ---
        self.next_band(9)
        b9_t = Tex("Four moves on the kitchen table").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = Tex("1. R100 000 in: owned up, owner up — level").scale(1.0).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex("2. Fridge for cash: shuffle INSIDE owned — level").scale(0.95).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex("3. Stock on credit: owned up, owed up — level").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        b9_l4 = Tex("4. Pay R5 000: owned down, owed down — level").scale(0.95).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l1)); self.wait(2)
        self.play(Write(b9_l2)); self.wait(2)
        self.play(Write(b9_l3)); self.wait(2)
        self.play(Write(b9_l4)); self.wait(2)
        b9_l5 = Tex("A level table never means skip the writing").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the question that never fails ---
        self.next_band(10)
        b10_t = Tex("Which two places, and which way?").scale(1.2).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_t)); self.wait(2)
        b10_l1 = Tex("Wages R2 000: bank down (place one)").scale(1.05).shift(band_shift(10) + UP * 1.3)
        b10_l2 = Tex("Work is used up — owner's pocket shrinks").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1)); self.wait(2)
        self.play(Write(b10_l2)); self.wait(2)
        b10_l3 = Tex("Expenses = pocket shrinking (debit);").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        b10_l4 = Tex("incomes = pocket growing (credit)").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l3)); self.play(Write(b10_l4)); self.wait(2.5)
        b10_l5 = Tex("Two places, two directions, one level table").scale(1.0).shift(band_shift(10) + DOWN * 2.3)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
