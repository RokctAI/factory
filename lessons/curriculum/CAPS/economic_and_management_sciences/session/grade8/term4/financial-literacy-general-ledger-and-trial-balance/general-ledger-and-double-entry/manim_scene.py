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

# Band-layout whiteboard scene for general-ledger-and-double-entry (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (300/170/160/160/220/120/130 of 1260 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class GeneralLedgerAndDoubleEntrySession(MovingCameraScene):
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
        self.write_rows(0, "The general ledger", [
            "Book of final entry",
            "Balance sheet accounts: B1, B2...",
            "Nominal accounts: N1, N2...",
            "Folios make the audit trail",
        ], box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "The T-account", [
            "Debit left, credit right",
            "Date, details, folio, amount",
            "Details: the contra account",
            "Folio: CRJ 4 or CPJ 4",
        ], box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Double entry", [
            "Every debit has an equal credit",
            "Capital: Dr bank, Cr capital",
            "Wages: Dr wages, Cr bank",
            "Total debits = total credits",
        ], box=0)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Debit and credit rules", [
            "Assets, expenses, drawings: Dr",
            "Capital, liabilities, income: Cr",
            "Decrease on the opposite side",
            "Matches A = OE + L",
        ], box=3)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "April into debits and credits", [
            "Receipts: Dr bank",
            "Payments: Cr bank",
            "Equipment: Dr equipment, Cr bank",
            "Receipts R31 330; payments R25 325",
        ], box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Two sides of every story", [
            "One folder per item",
            "Owner adds capital: two folders",
            "One left, one right, same amount",
            "Write the other folder's name",
        ], box=2)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Which side?", [
            "Team debit: A, E, D",
            "Team credit: C, L, I",
            "Grow on your side",
            "Two lefts? Check again",
        ], box=3)

        self.wait(4)
