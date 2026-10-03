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

# Band-layout whiteboard scene for crj-transactions-and-the-accounting-equation (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (250/170/160/160/180/180/170 of 1270 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CrjTransactionsAndTheAccountingEquationSession(MovingCameraScene):
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
        self.write_rows(0, "Reading a CRJ line", [
            "Every line: bank up, assets up",
            "Current income: OE up, income",
            "Sundry: read the account name",
            "Capital, income: OE; loan: L; debtors: swap",
        ], box=2)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Summarising a month", [
            "April: A +31 330 = OE +31 330",
            "March: A +103 550",
            "OE +78 550; L +25 000",
            "Split sundry by account type",
        ], box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Capital versus income", [
            "March: capital 60 000, income 18 550",
            "April: capital 10 000, income 21 330",
            "CRJ cannot show profit: no expenses",
            "Drawings appear in the CPJ",
        ], box=1)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Exam-style analysis", [
            "Rent 2 500: A+, OE+ income",
            "Loan 20 000: A+, L+",
            "Debtor 1 200: A+ and A-",
            "A +34 500 = OE +14 500 + L +20 000",
        ], box=3)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Ledger link and errors", [
            "Debits posted: assets up (left)",
            "Credits posted: OE or L up (right)",
            "Errors: loan as income; no reason",
            "Swaps as income; missing bank; receipts as income",
        ], box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Two questions for every line", [
            "Did the bank go up? Always",
            "What kind of money was it?",
            "Earned or capital: OE up",
            "Borrowed: L up; swapped: no change",
        ], box=1)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "What the month is telling you", [
            "March: mostly capital and loan",
            "April: mostly earned",
            "Big bank balance is not profit",
            "Profit needs the CPJ too",
        ], box=2)

        self.wait(4)
