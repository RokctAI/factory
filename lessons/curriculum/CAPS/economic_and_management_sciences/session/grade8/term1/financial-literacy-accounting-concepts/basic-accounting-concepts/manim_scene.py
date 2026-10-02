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

# Band-layout whiteboard scene for basic-accounting-concepts (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (280/190/180/210/140/180/150 of 1330 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class BasicAccountingConceptsSession(MovingCameraScene):
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
        self.write_rows(0, "The sole trader", [
            "One owner: all profit, all risk",
            "Unlimited liability",
            "Business entity: business separate from owner",
            "Service, trading, manufacturing",
        ], box=2)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Capital, assets, liabilities", [
            "Capital: owner's contribution",
            "Assets: non-current (washer), current (bank)",
            "Liabilities: non-current (loan), current (creditors)",
            "Owner's equity = capital + profit - drawings",
        ], box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Income, expenses, profit", [
            "Profit = income - expenses",
            "R48 000 - R26 000 = R22 000",
            "OE: R50 000 + R22 000 - R6 000 = R66 000",
            "Buying equipment is not an expense",
        ], box=2)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Debit and credit", [
            "Debit = left; credit = right",
            "A = OE + L sets the sides",
            "DEAD: expenses, assets, drawings up on debit",
            "Capital, liabilities, income up on credit",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Classifying items", [
            "Owns it? Asset",
            "Owes outsiders? Liability",
            "Owner's? Capital or drawings",
            "Earned: income. Used up: expense",
        ], box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "The car wash on the corner", [
            "Savings in: capital",
            "Washer: asset; loan: liability",
            "Fees: income; wages: expenses",
            "Drawings: R6 000 taken home",
        ], box=3)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Left side, right side", [
            "Own on the left, owe on the right",
            "Income with the owner: right",
            "Expenses and drawings: left",
            "Left always equals right",
        ], box=3)

        self.wait(4)
