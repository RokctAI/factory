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
# dwell time proportional to subtopics.json (220/240/230/260/180/180/180 of
# 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DebtorsConsolidationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Full Debtors Cycle
        b0_title = Tex("The debtors cycle").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Invoice: DJ, debit debtor").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Receipt: CRJ, credit debtor").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Ledger: detail per debtor").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Control: the total").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Opening Balances and July's Credit Sales
        self.next_band(1)
        b1_title = Tex("July credit sales").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Opening debtors 8 400").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Invoices 141 to 144").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Sales 12 000, cost 8 000").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Gross profit 4 000").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Receipts from Debtors in the CRJ
        self.next_band(2)
        b2_title = Tex("Receipts from debtors").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Hilltop 4 800, Ace 2 100").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Sunset 1 000, part payment").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Debtors control column 7 900").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("No sales, no cost of sales").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Debtors Ledger, Control Account and Debtors List
        self.next_band(3)
        b3_title = Tex("Debtors list at 31 July").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Hilltop 5 400").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Ace 4 200").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Sunset 2 900").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Total 12 500").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Debtors Ledger, Control Account and Debtors List
        self.next_band(4)
        b4_title = Tex("Debtors control").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Balance b/d 8 400").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("Plus DJ 12 000").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("Minus CRJ 7 900").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("Balance 12 500: agrees").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)

        # --- Band 5 (subtopic_4): Debtors Ledger, Control Account and Debtors List
        self.next_band(5)
        b5_title = Tex("Error museum").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("``Add opening balance to the DJ''").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("``Debtor payment is a sale''").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("``Post payments as debits''").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("``Credit limits are optional''").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)



        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): Sell, Record, Collect
        self.next_band(6)
        b6_title = Tex("Sell, record, collect").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Credit sale: DJ").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Payment: CRJ").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("DJ up, CRJ down").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("A payment is not a sale").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_6): Every Customer's Story
        self.next_band(7)
        b7_title = Tex("Every customer's story").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Start with what they owed").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Add invoices").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Subtract payments").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Balance after every line").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)

        # --- Band 8 (subtopic_7): One Total, Two Proofs
        self.next_band(8)
        b8_title = Tex("One total, two proofs").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("Pages add to 12 500").scale(0.9).shift(band_shift(8) + UP * 1.30)
        b8_l2 = Tex("Control: 8 400 + 12 000 - 7 900").scale(0.9).shift(band_shift(8) + UP * 0.35)
        b8_l3 = Tex("Also 12 500").scale(0.9).shift(band_shift(8) + DOWN * 0.60)
        b8_l4 = Tex("Statements and follow-ups").scale(0.9).shift(band_shift(8) + DOWN * 1.55)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(4)
