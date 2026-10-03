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

# Band-layout whiteboard scene for trial-balance-of-a-service-business (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (230/190/240/200/160/100/110 of 1230 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TrialBalanceOfAServiceBusinessSession(MovingCameraScene):
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
            "All ledger balances on one date",
            "Account, folio, debit, credit",
            "Balance sheet accounts, then nominal",
            "Equal totals: arithmetic is correct",
        ], box=3)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Balance sheet accounts", [
            "Capital R70 000 Cr; loan R25 000 Cr",
            "Drawings R5 500 Dr",
            "Equipment R23 200 Dr",
            "Bank R80 185 Dr (favourable)",
        ], box=1)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Nominal accounts and totals", [
            "Income R39 880 Cr",
            "Expenses R25 995 Dr",
            "Debit total R134 880",
            "Credit total R134 880",
        ], box=3)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Errors", [
            "Revealed: one half missing, wrong side",
            "R680 as R860: difference 180 = 9 x 20",
            "Hidden: omission, wrong account",
            "Hidden: reversal, compensating errors",
        ], box=1)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Using the trial balance", [
            "39 880 - 25 995 = 13 885 profit",
            "A = 80 185 + 23 200 = 103 385",
            "OE = 70 000 + 13 885 - 5 500 = 78 385",
            "78 385 + 25 000 = 103 385",
        ], box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "One page, two columns", [
            "Left: owns, expenses, drawings",
            "Right: capital, owes, income",
            "Left R134 880",
            "Right R134 880",
        ], box=3)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "When it does not balance", [
            "Half the difference: wrong column?",
            "Divides by 9: swapped digits?",
            "Forgotten transaction still balances",
            "Profit so far R13 885",
        ], box=2)

        self.wait(4)
