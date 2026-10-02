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
# dwell time proportional to subtopics.json (210/220/230/240/180/190/180 of
# 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CashPaymentsJournalSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Purpose and Format of the Cash Payments Journal
        b0_title = Tex("Cash payments journal").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Book of first entry: money paid").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Doc, Day, Name of payee, Fol").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Bank, Trading stock, Wages").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Sundry: amount, folio, details").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Recording Purchases of Trading Stock and Wages
        self.next_band(1)
        b1_title = Tex("Stock and wages").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("2: stock R20 000; 18: stock R9 000").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("At cost price, no mark-up").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("12 and 26: wages R6 000 each").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Owner's withdrawals: never wages").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Recording Other Payments in the Sundry Accounts Column
        self.next_band(2)
        b2_title = Tex("Sundry payments").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Rent expense 5 000; Equipment 7 500").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Drawings 2 000").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Telephone 850").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Bank charges 240 (bank statement)").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Totalling, Cross-casting and the Bank Balance
        self.next_band(3)
        b3_title = Tex("Totals and the bank balance").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Bank 56 590").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("29 000 + 12 000 + 15 590 = 56 590").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("140 250 - 56 590 = 83 660").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Stock: 29 000 - 18 400 = 10 600").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Totalling, Cross-casting and the Bank Balance
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Shelving is trading stock''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``The owner's pay is wages''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Ignore the bank charges''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Rent paid is rent income''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Notebook Just for Money Going Out
        self.next_band(5)
        b5_title = Tex("Money going out").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Money out: CPJ").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Every rand in the bank column").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("EFT proof or bank statement").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Two people approve payments").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Every Payment Needs a Home
        self.next_band(6)
        b6_title = Tex("Every payment needs a home").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Customer buys it? Trading stock").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Pay for an employee? Wages").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Anything else: sundry with a name").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Owner's money: drawings").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Money In Minus Money Out
        self.next_band(7)
        b7_title = Tex("Money in minus money out").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("In: 140 250").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Out: 56 590").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Left in the bank: 83 660").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Stock left: 10 600").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(4)
