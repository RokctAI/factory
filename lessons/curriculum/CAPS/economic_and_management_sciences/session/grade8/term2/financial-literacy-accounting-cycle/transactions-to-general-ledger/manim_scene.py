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

# Band-layout whiteboard scene for transactions-to-general-ledger (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (270/210/190/190/170/140/150 of 1320 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TransactionsToGeneralLedgerSession(MovingCameraScene):
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
        self.write_rows(0, "The accounting cycle", [
            "1 Transaction  2 Source document",
            "3 Journal (first entry)  4 Ledger (final entry)",
            "5 Trial balance  6 Financial statements",
            "T, S, J, L, T, F",
        ], box=3)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Document to journal", [
            "CRJ: receipts, CRR, bank statement",
            "CPJ: EFT confirmations, bank statement",
            "Current income total R15 900; sundry R87 650",
            "Bank R103 550 = 15 900 + 87 650",
        ], box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "The general ledger", [
            "One T-account per item",
            "Balance sheet accounts: capital, loan, bank",
            "Nominal accounts: income and expenses",
            "Folio numbers link journal and ledger",
        ], box=1)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Posting", [
            "CRJ bank total: debit Bank",
            "Income and sundry receipts: credit",
            "CPJ bank total: credit Bank",
            "Bank: 103 550 - 29 370 = 74 180 Dr",
        ], box=3)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Manual and computerised", [
            "Same cycle, same steps",
            "Software posts and balances automatically",
            "Risks: capture errors, data loss, fraud",
            "Garbage in, garbage out",
        ], box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "The road every rand travels", [
            "Fridge repair paid: transaction",
            "Receipt copy: document",
            "Diary, folders, check, report cards",
            "Then the road starts again",
        ], box=2)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Diary and folders", [
            "Journal: the story by date",
            "Ledger: one folder per item",
            "Posting: totals into folders, two sides",
            "R74 180 left in the bank",
        ], box=2)

        self.wait(4)
