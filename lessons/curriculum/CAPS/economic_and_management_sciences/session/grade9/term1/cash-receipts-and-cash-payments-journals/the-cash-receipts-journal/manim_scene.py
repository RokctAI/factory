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
# dwell time proportional to subtopics.json (220/230/220/230/180/190/180 of
# 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CashReceiptsJournalSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Purpose and Format of the Cash Receipts Journal
        b0_title = Tex("Cash receipts journal").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Book of first entry: money received").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Doc, Day, Details, Fol").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Bank, Sales, Cost of sales").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Sundry: amount, folio, details").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Recording Cash Sales and Cost of Sales
        self.next_band(1)
        b1_title = Tex("Cash sales at 50 percent mark-up").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("12 000 x 100 / 150 = 8 000").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("9 000 x 100 / 150 = 6 000").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("6 600 x 100 / 150 = 4 400").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Cost of sales: a memorandum column").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Recording Other Receipts in the Sundry Accounts Column
        self.next_band(2)
        b2_title = Tex("Sundry receipts").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("1: Capital 80 000").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("10: Rent income 2 500").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("20: Loan 30 000").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("31: Interest income 150").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Totalling, Cross-casting and Checking the CRJ
        self.next_band(3)
        b3_title = Tex("Totals and cross-cast").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Bank 140 250; Sales 27 600").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Cost of sales 18 400; Sundry 112 650").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("27 600 + 112 650 = 140 250").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Cost of sales left out of the check").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Totalling, Cross-casting and Checking the CRJ
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Add cost of sales in the cross-cast''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Capital goes in sales''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Cost = sales less 50 percent''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Payments go in the CRJ''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Notebook Just for Money Coming In
        self.next_band(5)
        b5_title = Tex("Notebook for money in").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Money in: CRJ; money out: CPJ").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Every rand in the bank column").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Sales or sundry says what kind").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Cost of sales: a note about stock").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Filling In the Columns Line by Line
        self.next_band(6)
        b6_title = Tex("Line by line").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Owner R80 000: sundry, Capital").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Sales R12 000: cost 8 000").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Rent R2 500: sundry, Rent income").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Loan R30 000: sundry, Loan").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Do the Totals Agree?
        self.next_band(7)
        b7_title = Tex("Do the totals agree?").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Bank 140 250").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Sales 27 600 + sundry 112 650").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("= 140 250: it cross-casts").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Underline totals twice").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(4)
