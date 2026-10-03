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
# dwell time proportional to subtopics.json (210/240/230/230/180/190/180 of
# 1460 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TrialBalanceSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Purpose and Format of a Trial Balance
        b0_title = Tex("Trial balance").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("List of ledger balances on a date").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Balance sheet section, then nominal").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Debit: assets, expenses, drawings").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Credit: capital, liabilities, income").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Preparing Ridgeview Hardware's Trial Balance
        self.next_band(1)
        b1_title = Tex("Ridgeview on 31 March").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Dr: 2 000, 7 500, 10 600, 83 660").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("18 400, 5 000, 12 000, 850, 240").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Cr: 80 000, 30 000, 27 600, 2 500, 150").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Both columns total 140 250").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Errors a Trial Balance Reveals and Errors It Hides
        self.next_band(2)
        b2_title = Tex("Errors").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Revealed: one-sided, wrong side").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Revealed: wrong amount, bad addition").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Hidden: omission, commission, principle").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Hidden: original entry, reversal").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_3): Errors a Trial Balance Reveals and Errors It Hides
        self.next_band(3)
        b3_title = Tex("Finding a difference").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Look for the difference").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Look for half the difference").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Divisible by 9: transposition").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("850 - 580 = 270; 270 / 9 = 30").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Reading the Trial Balance: Gross Profit and Net Result
        self.next_band(4)
        b4_title = Tex("Reading the trial balance").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("27 600 - 18 400 = 9 200").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("Other income 2 650").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("Expenses 18 090").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("9 200 + 2 650 - 18 090 = -6 240").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b4_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 5 (subtopic_4): Reading the Trial Balance: Gross Profit and Net Result
        self.next_band(5)
        b5_title = Tex("Error museum").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("``List bank at its side total''").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("``Drawings in the credit column''").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("``Balanced means error-free''").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("``Capital and loans are income''").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): A Class Register for Accounts
        self.next_band(6)
        b6_title = Tex("A register for accounts").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Call every account").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Balance sheet group, nominal group").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Debit family left, credit family right").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Only the balance").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_6): Two Columns That Must Agree
        self.next_band(7)
        b7_title = Tex("Two columns agree").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Debits 140 250").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Credits 140 250").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Gross profit 9 200").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("First month: loss of 6 240").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)

        # --- Band 8 (subtopic_7): Hunting for the Missing Rand
        self.next_band(8)
        b8_title = Tex("Hunting the missing rand").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("Find the difference").scale(0.9).shift(band_shift(8) + UP * 1.30)
        b8_l2 = Tex("Halve it: wrong column?").scale(0.9).shift(band_shift(8) + UP * 0.35)
        b8_l3 = Tex("Divide by 9: swapped digits?").scale(0.9).shift(band_shift(8) + DOWN * 0.60)
        b8_l4 = Tex("Balanced can still hide errors").scale(0.9).shift(band_shift(8) + DOWN * 1.55)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b8_l4, color=YELLOW)))
        self.wait(4)
