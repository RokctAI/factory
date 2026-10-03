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

# Band-layout whiteboard scene for transactions-banking-and-subsidiary-journals (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (280/180/190/210/180/170/160 of 1370 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TransactionsBankingAndSubsidiaryJournalsSession(MovingCameraScene):
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
        self.write_rows(0, "Transactions", [
            "Changes financial position, measured in money",
            "Cash: paid now; credit: paid later",
            "Cash receipts in, cash payments out",
            "No source document, no entry",
        ], box=3)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "The bank", [
            "Current account keeps money safe",
            "EFT, debit orders, card payments",
            "Bank statement and bank charges",
            "Cheques stopped by 2021",
        ], box=1)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Receipts and payments", [
            "Receipts: income, capital, loans",
            "Payments: expenses, assets, loan repayments, drawings",
            "R8 000 + R14 600 - R12 600 = R10 000",
            "A loan is a receipt, not income",
        ], box=2)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Subsidiary journals", [
            "Books of first entry",
            "CRJ: all money received",
            "CPJ: all money paid out",
            "Grade 9: DJ, CJ, petty cash, GJ",
        ], box=1)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Internal control over cash", [
            "Pre-numbered receipts; deposit intact daily",
            "Separate receiving from recording",
            "Pay by EFT, with approval and documents",
            "Compare records with the bank statement",
        ], box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "A week at the salon", [
            "Card tap, cash cuts: receipts",
            "Rent and wages by EFT: payments",
            "Every transaction has a document",
            "Bank ends at R10 000",
        ], box=3)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Two boxes on the counter", [
            "Money-in box: CRJ",
            "Money-out box: CPJ",
            "Columns like taxi lines",
            "Transaction, document, journal, ledger",
        ], box=3)

        self.wait(4)
