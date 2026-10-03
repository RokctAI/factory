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

# Band-layout whiteboard scene for index-grid-and-street-maps (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/190/230/210/90/90/110 of 1110 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class IndexGridAndStreetMapsSession(MovingCameraScene):
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
        # --- Band 0: What a Street Map Shows
        self.write_rows(0, "What a Street Map Shows", [
            "Street map: streets, names, buildings",
            "Key explains the symbols",
            "N roads national; R roads provincial",
            "Street guide: key map and page numbers",
        ], scale=0.86, box=1)
        # --- Band 1: The Index
        self.next_band(1)
        self.write_rows(1, "The Index", [
            "Index: street names in alphabetical order",
            "Entry: name, suburb, page, square",
            "Mandela Street, Central, 47 D3",
            "Same name, different suburbs",
        ], scale=0.86, box=1)
        # --- Band 2: The Grid and Grid References
        self.next_band(2)
        self.write_rows(2, "The Grid and Grid References", [
            "Columns lettered, rows numbered",
            "C4: go to column C, down to row 4",
            "A reference names a square, not a point",
            "Grid works on one map; degrees on all",
        ], scale=0.86, box=1)
        # --- Band 3: Street Maps and Map Apps
        self.next_band(3)
        self.write_rows(3, "Street Maps and Map Apps", [
            "Map app: GPS shows where you are",
            "Search box replaces the index",
            "Printed maps: no data, the big picture",
            "Check the app with common sense",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A Map of the Streets
        self.next_band(4)
        self.write_rows(4, "A Map of the Streets", [
            "Streets, names and buildings",
            "The key explains symbols",
            "N1 national, R roads provincial",
        ], scale=0.86, box=0)
        # --- Band 5: Finding a Street
        self.next_band(5)
        self.write_rows(5, "Finding a Street", [
            "Index: names A to Z",
            "Page, then square",
            "Across to the letter, down to the number",
        ], scale=0.86, box=0)
        # --- Band 6: Maps on Your Phone
        self.next_band(6)
        self.write_rows(6, "Maps on Your Phone", [
            "Blue dot: GPS from satellites",
            "Type the name instead of the index",
            "App as a helper, not a boss",
        ], scale=0.86, box=0)
        self.wait(4)
