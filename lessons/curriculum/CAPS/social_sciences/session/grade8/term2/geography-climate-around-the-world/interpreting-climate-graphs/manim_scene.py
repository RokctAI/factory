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

# Band-layout whiteboard scene for interpreting-climate-graphs (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (260/200/280/200/150/150/150 of 1390 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class InterpretingClimateGraphsSession(MovingCameraScene):
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
        # --- Band 0: Parts of a climate graph
        self.write_rows(0, "Parts of a climate graph", [
            "Months along the bottom",
            "Temperature: a line, in \\textdegree{}C",
            "Rainfall: bars, in mm",
            "30-year averages",
        ], scale=0.86, box=1)
        # --- Band 1: Station A
        self.next_band(1)
        self.write_rows(1, "Station A", [
            "Range: 22 -- 13 = 9 \\textdegree{}C",
            "Total: 515 mm",
            "May to August: 321 mm, about 62 percent",
            "Mediterranean: winter rain",
        ], scale=0.86, box=3)
        # --- Band 2: Station B
        self.next_band(2)
        self.write_rows(2, "Station B", [
            "Range: 22 -- 11 = 11 \\textdegree{}C",
            "Total: 671 mm",
            "October to March: 570 mm, about 85 percent",
            "Summer rain, dry winter",
        ], scale=0.86, box=3)
        # --- Band 3: Writing the answer
        self.next_band(3)
        self.write_rows(3, "Writing the answer", [
            "Highest, lowest, range",
            "Total and wettest season",
            "Identify with two pieces of evidence",
            "Figures with units",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A line and some bars
        self.next_band(4)
        self.write_rows(4, "A line and some bars", [
            "Line for warmth, bars for rain",
            "Read the right axis",
        ], scale=0.86, box=1)
        # --- Band 5: The winter-rain town
        self.next_band(5)
        self.write_rows(5, "The winter-rain town", [
            "Tall bars under the low line",
        ], scale=0.86, box=0)
        # --- Band 6: The summer-rain town
        self.next_band(6)
        self.write_rows(6, "The summer-rain town", [
            "Tall bars under the high line",
        ], scale=0.86, box=0)
        self.wait(4)
