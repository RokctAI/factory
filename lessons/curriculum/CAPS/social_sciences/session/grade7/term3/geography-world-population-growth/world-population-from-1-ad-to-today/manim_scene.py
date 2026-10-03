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

# Band-layout whiteboard scene for world-population-from-1-ad-to-today (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/190/180/190/90/90/90 of 1000 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class WorldPopulationFrom1AdToTodaySession(MovingCameraScene):
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
        # --- Band 0: Reading a Line Graph
        self.write_rows(0, "Reading a Line Graph", [
            "Title, x-axis: years, y-axis: billions",
            "Flat: little change; steep: fast growth",
            "Read: year up to the line, across to the axis",
            "Trend, changes, figures with units",
        ], scale=0.8, box=1)
        # --- Band 1: The Long, Slow Stage
        self.next_band(1)
        self.write_rows(1, "The Long, Slow Stage", [
            "1 AD: about 250 to 300 million",
            "1500: about 450 to 500 million",
            "High births and high deaths: almost balanced",
            "Black Death 1347: Europe loses a third or more",
        ], scale=0.8, box=2)
        # --- Band 2: The Population Explosion
        self.next_band(2)
        self.write_rows(2, "The Population Explosion", [
            "1 billion about 1804; 8 billion 2022",
            "Each extra billion came faster",
            "Peak growth: just over 2 percent, late 1960s",
            "Deaths fell first; births fell later",
        ], scale=0.86, box=3)
        # --- Band 3: Slowing Growth and the Future
        self.next_band(3)
        self.write_rows(3, "Slowing Growth and the Future", [
            "Growth now just under 1 percent a year",
            "Fertility: about 5 in 1950, about 2.3 now",
            "About 9.7 billion by 2050; peak in the 2080s",
            "Most future growth in Africa",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Reading the Line
        self.next_band(4)
        self.write_rows(4, "Reading the Line", [
            "Years along the bottom",
            "Billions up the side",
            "Flat: slow; steep: fast",
        ], scale=0.86, box=0)
        # --- Band 5: Slow, Then Fast
        self.next_band(5)
        self.write_rows(5, "Slow, Then Fast", [
            "1 AD: about 300 million",
            "1804: 1 billion",
            "2022: 8 billion",
        ], scale=0.86, box=0)
        # --- Band 6: Slowing Down
        self.next_band(6)
        self.write_rows(6, "Slowing Down", [
            "Fewer children per family now",
            "About 9.7 billion by 2050",
            "Most new growth in Africa",
        ], scale=0.86, box=0)
        self.wait(4)
