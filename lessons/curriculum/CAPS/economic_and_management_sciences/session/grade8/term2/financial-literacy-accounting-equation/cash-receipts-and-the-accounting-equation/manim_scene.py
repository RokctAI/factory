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

# Band-layout whiteboard scene for cash-receipts-and-the-accounting-equation (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (240/170/190/170/140/200/140 of 1250 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CashReceiptsAndTheAccountingEquationSession(MovingCameraScene):
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
        self.write_rows(0, "Every receipt increases bank", [
            "Bank is debited for every receipt",
            "Pattern 1: A up, OE up",
            "Pattern 2: A up, L up",
            "Pattern 3: A up, another A down",
        ], box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Receipts that increase OE", [
            "Capital R40 000: OE +, capital contribution",
            "Current income R3 500: OE +, income",
            "Rent income R1 200; interest R85",
            "Capital and income: different reasons",
        ], box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Loans and conversions", [
            "Loan R30 000: A +, L +",
            "Camera at book value: A +2 400, A -2 400",
            "Debtor pays R1 500: A +, A -",
            "None of these is income",
        ], box=3)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "The full analysis", [
            "Bank receipts: R83 685",
            "Swaps: R3 900",
            "Net A +79 785 = OE +49 785 + L +30 000",
            "Income part: R4 785",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "From equation to journal", [
            "Every receipt: CRJ bank column",
            "Current income: own column",
            "Capital, loan, rent, interest: sundry",
            "Same question decides the column",
        ], box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Three kinds of money in", [
            "Owner's or earned: owner's share up",
            "Borrowed: debts up",
            "Swapped: one asset for another",
            "A loan is never income",
        ], box=3)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "The month on the scale", [
            "Left pan grew by 79 785",
            "Owner's share 49 785 + debts 30 000",
            "Capital 45 000, earned 4 785",
            "Level every time",
        ], box=1)

        self.wait(4)
