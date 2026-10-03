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

# Band-layout whiteboard scene for opening-accounts-and-posting-the-cash-journals (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (290/180/170/230/130/120/110 of 1230 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class OpeningAccountsAndPostingTheCashJournalsSession(MovingCameraScene):
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
        self.write_rows(0, "Opening the accounts", [
            "T-account, name and folio",
            "B1-B5 balance sheet; N1-N10 nominal",
            "1 April balance b/d",
            "Bank R74 180 Dr; capital R60 000 Cr",
        ], box=3)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Posting the CRJ", [
            "Bank Dr R31 330: total receipts",
            "Current income Cr R18 650",
            "Sundry: each to its own account",
            "Credits total R31 330",
        ], box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Posting the CPJ", [
            "Bank Cr R25 325: total payments",
            "Wages Dr R6 000; repair parts Dr R4 200",
            "Sundry R15 125: each debited",
            "Debits total R25 325",
        ], box=3)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Balancing the bank account", [
            "74 180 + 31 330 = 105 510",
            "105 510 - 25 325 = 80 185",
            "Balance c/d on the smaller side",
            "Balance b/d on 1 May",
        ], box=1)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Checking and reading", [
            "Every amount has a folio",
            "Balances on their normal side",
            "Bank agrees with statement",
            "Nominal accounts: year so far",
        ], box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Filing the folders", [
            "Opening balances already inside",
            "Money in: bank on the left",
            "Money out: bank on the right",
            "Write date, other folder, folio",
        ], box=0)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "What is left in each folder?", [
            "Bank R80 185",
            "Capital R70 000",
            "Wages R12 000",
            "Equipment R23 200",
        ], box=0)

        self.wait(4)
