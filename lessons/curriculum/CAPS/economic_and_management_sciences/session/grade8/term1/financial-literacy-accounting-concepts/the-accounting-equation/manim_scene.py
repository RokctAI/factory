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

# Band-layout whiteboard scene for the-accounting-equation (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (270/160/200/160/210/150/140 of 1290 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TheAccountingEquationSession(MovingCameraScene):
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
        self.write_rows(0, "A = OE + L", [
            "Assets: what the business owns",
            "OE: the owner's claim; L: outsiders' claims",
            "OE = A - L; L = A - OE",
            "R250 000 - R70 000 = R180 000",
        ], box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Five patterns", [
            "A up, OE up: capital, income",
            "A up, L up: loan received",
            "A down, OE down: expenses, drawings",
            "A down, L down: loan repaid; A up and A down: asset bought",
        ], box=0)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "The analysis table", [
            "Capital +80 000; loan +40 000",
            "Vehicle +100 000, bank -100 000",
            "Income +12 000; wages -4 000; fuel -1 500",
            "A 119 500 = OE 84 500 + L 35 000",
        ], box=3)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Profit, drawings and OE", [
            "Profit = 12 000 - 5 500 = 6 500",
            "OE = 80 000 + 6 500 - 2 000 = 84 500",
            "Missing profit: 30 000 - 10 000 + 18 000 = 38 000",
            "Loan is not income; asset is not an expense",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "A second business", [
            "Capital R30 000; equipment R12 000 by EFT",
            "Lawnmower as capital: A +3 000, OE +3 000",
            "Fees R7 500; advertising R900; telephone R450",
            "A 39 150 = OE 39 150 + L 0",
        ], box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "The scale that never tips", [
            "Left pan: bank and car",
            "Right pan: owner's share and loan",
            "Buying the car: swap on the left",
            "Own minus owe = owner's share",
        ], box=3)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Lessons, wages and the owner's share", [
            "Earned: owner's share up",
            "Running costs: owner's share down",
            "Borrowed or repaid: amount owed changes",
            "Level every time: 119 500",
        ], box=3)

        self.wait(4)
