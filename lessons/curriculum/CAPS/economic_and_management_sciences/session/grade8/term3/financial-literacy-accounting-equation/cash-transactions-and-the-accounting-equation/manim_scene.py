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

# Band-layout whiteboard scene for cash-transactions-and-the-accounting-equation (Part 1 Expert
# subtopics 1-6, Part 2 Simplifier subtopics 7-8). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (240/120/140/150/180/140/130/150 of 1250 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CashTransactionsAndTheAccountingEquationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.78, box=None):
        t = Tex(title).scale(1.1).shift(band_shift(k) + UP * 2.4)
        self.play(Write(t))
        self.wait(1.5)
        made = []
        for i, r in enumerate(rows):
            m = Tex(r).scale(scale).shift(band_shift(k) + UP * (1.3 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.3)
            made.append(m)
        if box is not None:
            self.play(Create(SurroundingRectangle(made[box], color=YELLOW)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1)
        self.write_rows(0, "Equation and rules", [
            "A = OE + L",
            "Capital and income increase OE",
            "Expenses and drawings decrease OE",
            "Every transaction keeps it balanced",
        ], box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Expenses and drawings", [
            "Bank down, OE down",
            "Reason: expense incurred",
            "Drawings: OE down directly",
            "Liabilities unaffected",
        ], box=1)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Assets and loans", [
            "Equipment up, bank down",
            "Total assets unchanged",
            "Loan repaid: bank and loan down",
            "Interest is an expense",
        ], box=1)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "April payments table", [
            "Parts, rent, wages: A and OE down",
            "Drawings: A and OE down",
            "Equipment: +5 200 and −5 200",
            "Charges and insurance: expenses",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "The whole month", [
            "Bank +R6 005, equipment +R5 200",
            "Assets +R11 205 = OE +R11 205",
            "Profit R21 330 − R17 625 = R3 705",
            "Profit is not the bank change",
        ], box=2)

        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Common errors", [
            "Drawings are not expenses",
            "Assets are not expenses",
            "Loan repaid: L, not OE",
            "Check both sides every row",
        ], box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Three kinds of money out", [
            "Expense or drawings: OE down",
            "Asset bought: a swap",
            "Loan repaid: L down",
            "Bank always goes down",
        ], box=3)

        # --- Band 7 (subtopic_8)
        self.next_band(7)
        self.write_rows(7, "April on the scale", [
            "Assets up R11 205",
            "OE up R11 205",
            "Profit R3 705",
            "Check both sides match",
        ], box=1)

        self.wait(4)
