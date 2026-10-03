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
# dwell time proportional to subtopics.json (220/230/220/250/180/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CreditEquationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Accounting Cycle with Credit Transactions
        b0_title = Tex("The accounting cycle").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Source document").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Journals: CRJ, CPJ, DJ").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("General ledger and debtors ledger").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Trial balance; statements in Grade 10").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): A Credit Sale in the Accounting Equation
        self.next_band(1)
        b1_title = Tex("Credit sale: moment one").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Cost: 6 000 x 100 / 150 = 4 000").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("A +6 000 debtors; OE +6 000 sales").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("A -4 000 stock; OE -4 000 cost of sales").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Net: A +2 000, OE +2 000").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Receiving Payment from a Debtor
        self.next_band(2)
        b2_title = Tex("Debtor pays: moment two").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("A +6 000 bank").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("A -6 000 debtors control").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("OE: no effect").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Part payment: 3 600 - 2 000 = 1 600").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Comparing Cash and Credit Transactions in a Table
        self.next_band(3)
        b3_title = Tex("April in a table").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Hilltop: +2 000 profit").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Ace: +1 200; cash sale: +1 500").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Hilltop pays: no profit").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Total: 4 700 = 4 700").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Comparing Cash and Credit Transactions in a Table
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``A debtor's payment is income''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``A credit sale increases bank''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Credit sales have no cost''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Debtors are a liability''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Five Steps of the Bookkeeping Loop
        self.next_band(5)
        b5_title = Tex("The bookkeeping loop").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("1 Paper proof").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("2 Notebooks: CRJ, CPJ, DJ").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("3 Ledgers; 4 trial balance").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("5 Year-end statements").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Sell Today, Collect Later
        self.next_band(6)
        b6_title = Tex("Sell today, collect later").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Debtors +6 000; sales +6 000").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Stock -4 000; cost of sales +4 000").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Profit made today: 2 000").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Same profit as cash").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Two Moments, Two Records
        self.next_band(7)
        b7_title = Tex("Two moments").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("3 April: goods go, profit made").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("20 April: money comes, a swap").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Owner's equity unchanged").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Never count a sale twice").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
