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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex keep the export to the
# allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (210/230/220/240/180/190/180 of
# 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ClassificationOfAccountsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The General Ledger and Its Two Sections
        b0_title = Tex("The general ledger").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Book of final entry").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Dr: left side; Cr: right side").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Balance sheet section: folios B").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Nominal section: folios N").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Classifying Balance Sheet Accounts
        self.next_band(1)
        b1_title = Tex("Balance sheet accounts").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Owner's equity: Capital, Drawings").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Non-current assets: Equipment").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Current assets: Trading stock, Bank").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Liabilities: Loan, Creditors control").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Classifying Nominal Accounts: Income and Expenses
        self.next_band(2)
        b2_title = Tex("Nominal accounts").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Income: Sales, Rent income").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Interest income").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Expenses: Cost of sales, Wages").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Rent expense, Telephone, Bank charges").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Debit and Credit Rules and Normal Balances
        self.next_band(3)
        b3_title = Tex("Debit and credit rules").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Debit family: assets, expenses, drawings").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Credit family: liabilities, capital, income").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Decrease: write on the other side").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Every debit has an equal credit").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Debit and Credit Rules and Normal Balances
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Debit means increase''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Drawings is an expense''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Trading stock is nominal''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Rent income and expense: one account''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Sorting Accounts into Two Drawers
        self.next_band(5)
        b5_title = Tex("Two drawers").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("B: owns, owes, owner's stake").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("N: earned or used up").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Stock: top drawer").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Loan: top drawer, not income").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Which Side Makes It Grow?
        self.next_band(6)
        b6_title = Tex("Which side makes it grow?").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Assets live left: debit").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("OE and liabilities live right: credit").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Income right; expenses left").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Capital R80 000: Dr Bank, Cr Capital").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Building the Ledger List for Ridgeview Hardware
        self.next_band(7)
        b7_title = Tex("Ridgeview's ledger list").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("B1 Capital ... B6 Loan").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("N1 Sales, N2 Cost of sales").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("N3-N8 incomes and expenses").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("9 debit family, 5 credit family").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(4)
