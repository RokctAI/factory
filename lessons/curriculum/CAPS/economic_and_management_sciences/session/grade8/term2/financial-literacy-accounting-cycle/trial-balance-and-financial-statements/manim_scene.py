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

# Band-layout whiteboard scene for trial-balance-and-financial-statements (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (330/190/180/180/140/150/140 of 1310 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TrialBalanceAndFinancialStatementsSession(MovingCameraScene):
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
        self.write_rows(0, "The trial balance", [
            "List every ledger balance on a date",
            "Debit: assets, expenses, drawings",
            "Credit: capital, liabilities, income",
            "103 550 = 103 550: it balances",
        ], box=3)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "The income statement", [
            "Performance for a period",
            "Income 18 550 - expenses 8 370",
            "Net profit R10 180",
            "No equipment, capital, loan or drawings",
        ], box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "The balance sheet", [
            "Financial position at a date",
            "Assets: equipment 18 000 + bank 74 180",
            "OE: 60 000 + 10 180 - 3 000 = 67 180",
            "92 180 = 67 180 + 25 000",
        ], box=3)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "How the statements connect", [
            "Nominal accounts: income statement",
            "Balance sheet accounts: balance sheet",
            "Net profit is the bridge",
            "Users: owner, bank, SARS, buyers",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Common errors", [
            "Wrong column: use DEAD",
            "Transposition: difference divisible by 9",
            "Drawings or equipment as expenses",
            "Period vs date in headings",
        ], box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "The checklist", [
            "Left: owns, spends, takes",
            "Right: owner's money, owed, earned",
            "Same total: the adding is right",
            "Not proof of no errors",
        ], box=3)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Report card and photograph", [
            "Report card: profit for March",
            "Photograph: position on 31 March",
            "Profit jumps into owner's equity",
            "Both sides match: 92 180",
        ], box=2)

        self.wait(4)
