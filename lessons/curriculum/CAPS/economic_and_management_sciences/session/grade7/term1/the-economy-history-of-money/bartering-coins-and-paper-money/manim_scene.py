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

# Band-layout whiteboard scene for bartering-coins-and-paper-money (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-5). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (180/190/220/140/110 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class BarteringCoinsAndPaperMoneySession(MovingCameraScene):
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
        self.write_rows(0, "Barter", [
            "Barter: goods swapped directly for goods",
            "Needs a double coincidence of wants",
            "Hard to value, divide and store",
            "Still used in small swaps today",
        ], box=1)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Commodity money and coins", [
            "Commodity money: cattle, salt, beads, shells",
            "Metal: gold, silver, copper",
            "Coins: stamped weight and value",
            "Heavy and risky over long distances",
        ], box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Notes, paper money and the rand", [
            "Promissory note: written promise to pay",
            "Banknotes: promise backed by a bank",
            "Rand issued by the Reserve Bank (SARB)",
            "Good money: accepted, durable, divisible",
        ], box=2)


        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "The goat's journey", [
            "Swap goat for grain: barter",
            "Goat worth 10 beads: commodity money",
            "Goat worth 5 silver coins: coins",
            "Goat worth R2 000 on paper: notes",
        ], box=0)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "What makes good money?", [
            "Accepted by everyone",
            "Lasts and is easy to carry",
            "Splits into small amounts",
            "Scarce and all the same",
        ], box=0)

        self.wait(4)
