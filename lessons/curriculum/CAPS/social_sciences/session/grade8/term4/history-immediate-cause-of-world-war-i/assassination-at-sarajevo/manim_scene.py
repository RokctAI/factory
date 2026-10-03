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

# Band-layout whiteboard scene for assassination-at-sarajevo (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/320/250/240/130/130/130 of 1440 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class AssassinationAtSarajevoSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
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
            self.play(Create(SurroundingRectangle(made[box], color=box_color)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0: Background
        self.write_rows(0, "Background", [
            "Bosnia annexed, 1908",
            "Serbian nationalism",
            "Black Hand and Young Bosnia",
            "Visit on 28 June",
        ], scale=0.86, box=0)
        # --- Band 1: The assassination
        self.next_band(1)
        self.write_rows(1, "The assassination", [
            "Bomb misses the car",
            "Wrong turn, car stops",
            "Princip fires two shots",
            "Died in prison, 1918",
        ], scale=0.86, box=2)
        # --- Band 2: The July Crisis
        self.next_band(2)
        self.write_rows(2, "The July Crisis", [
            "Blank cheque, 5 to 6 July",
            "Ultimatum, 23 July",
            "War on Serbia, 28 July",
            "Britain at war, 4 August",
        ], scale=0.86, box=3)
        # --- Band 3: Counting the days
        self.next_band(3)
        self.write_rows(3, "Counting the days", [
            "28 June to 28 July = 30 days",
            "28 July to 4 August = 7 days",
            "30 + 7 = 37 days",
            "Spark and powder",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The shot
        self.next_band(4)
        self.write_rows(4, "The shot", [
            "28 June 1914",
        ], scale=0.86, box=0)
        # --- Band 5: Dominoes fall
        self.next_band(5)
        self.write_rows(5, "Dominoes fall", [
            "37 days to war",
        ], scale=0.86, box=0)
        # --- Band 6: Spark and powder
        self.next_band(6)
        self.write_rows(6, "Spark and powder", [
            "Immediate and long-term",
        ], scale=0.86, box=0)
        self.wait(4)
