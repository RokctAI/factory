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

# Band-layout whiteboard scene for entering-and-closing-the-crj (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (300/180/190/160/220/150/140 of 1340 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class EnteringAndClosingTheCrjSession(MovingCameraScene):
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
        self.write_rows(0, "The entering routine", [
            "Doc, Day, Details",
            "Bank (or analysis + bank total)",
            "Current income or sundry with account name",
            "Date order; ask what kind of money",
        ], box=2)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Entering April", [
            "1: CRR 3 950",
            "4: 005 1 250 + CRR 2 100 = bank 3 350",
            "8: capital 10 000; 18: rent 2 500",
            "22: EFT 1 750 is current income; 30: interest 180",
        ], box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Closing off", [
            "Current income: R18 650",
            "Sundry: R12 680",
            "Bank: R31 330 = 18 650 + 12 680",
            "Single line above, double line below",
        ], box=2)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Posting", [
            "Bank Dr 31 330: total receipts",
            "Current income Cr 18 650",
            "Capital 10 000; rent 2 500; interest 180: Cr",
            "Folio CRJ 4",
        ], box=0)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "A second business", [
            "Capital 20 000; loan 15 000; interest 45",
            "Fees 1 800 + CRR 950: bank 2 750",
            "Current income 6 750; sundry 35 045",
            "Bank 41 795 = 6 750 + 35 045",
        ], box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "April day by day", [
            "Till rolls: current income",
            "Owner's top-up: sundry, capital",
            "EFT for a repair: still current income",
            "Interest: sundry",
        ], box=2)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Does it add up?", [
            "Current income + sundry = bank",
            "18 650 + 12 680 = 31 330",
            "One line above, two below",
            "Post: bank left, the rest right",
        ], box=1)

        self.wait(4)
