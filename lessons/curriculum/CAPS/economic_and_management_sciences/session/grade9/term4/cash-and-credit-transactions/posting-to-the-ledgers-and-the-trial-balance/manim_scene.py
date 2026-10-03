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
# dwell time proportional to subtopics.json (240/240/240/240/180/180/180 of
# 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LedgersTrialBalanceSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Posting the Cash Journals to the General Ledger
        b0_title = Tex("Posting the cash journals").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Bank Dr 21 000: Total receipts").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Bank Cr 16 700: Total payments").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Columns to their accounts").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Bank: 14 000 + 21 000 - 16 700").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Posting the Credit Journals to the General Ledger
        self.next_band(1)
        b1_title = Tex("Posting the credit journals").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("DJ: Dr Debtors control 7 500").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("DJ: Dr CoS 5 000, Cr stock").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("CJ: Dr Trading stock 11 000").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("CJ: Cr Creditors control 11 000").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The Debtors and Creditors Ledgers
        self.next_band(2)
        b2_title = Tex("Debtors ledger").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Mzansi: 3 600 + 4 500 - 3 600").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Mzansi owes 4 500").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Greenway owes 3 000").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("List 7 500 = Debtors control").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_3): The Debtors and Creditors Ledgers
        self.next_band(3)
        b3_title = Tex("Creditors ledger").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Bike Parts: 5 000 + 7 000 - 5 000").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Bike Parts owed 7 000").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Trail Supplies owed 4 000").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("List 11 000 = Creditors control").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): The Trial Balance
        self.next_band(4)
        b4_title = Tex("Trial balance, 30 November").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Debits: 95 500").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("Credits: 62 000 + 11 000 + 22 500").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("Credits: 95 500").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("Profit: 22 500 - 15 000 - 6 700").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)

        # --- Band 5 (subtopic_4): The Trial Balance
        self.next_band(5)
        b5_title = Tex("Error museum").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("``Post CoS against Bank''").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("``Post DJ totals to the debtors ledger''").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("``Balanced means error-free''").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("``Post Sundry as one total''").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): From Notebooks to Pages
        self.next_band(6)
        b6_title = Tex("Notebooks to pages").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Every amount: two pages").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Bank ends at 18 300").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Sales: 15 000 + 7 500").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Stock left: 18 000").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_6): Every Customer and Supplier
        self.next_band(7)
        b7_title = Tex("Customers and suppliers").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Mzansi 4 500, Greenway 3 000").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Together 7 500").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Bike Parts 7 000, Trail 4 000").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Together 11 000").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 8 (subtopic_7): Do Both Sides Agree?
        self.next_band(8)
        b8_title = Tex("Do both sides agree?").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("Left: 95 500").scale(0.9).shift(band_shift(8) + UP * 1.30)
        b8_l2 = Tex("Right: 95 500").scale(0.9).shift(band_shift(8) + UP * 0.35)
        b8_l3 = Tex("Profit: R800").scale(0.9).shift(band_shift(8) + DOWN * 0.60)
        b8_l4 = Tex("Difference points to the error").scale(0.9).shift(band_shift(8) + DOWN * 1.55)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(4)
