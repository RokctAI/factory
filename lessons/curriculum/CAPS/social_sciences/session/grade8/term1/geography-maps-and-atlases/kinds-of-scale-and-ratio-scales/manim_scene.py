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

# Band-layout whiteboard scene for kinds-of-scale-and-ratio-scales (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (260/220/210/240/150/150/150 of 1380 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class KindsOfScaleAndRatioScalesSession(MovingCameraScene):
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
        # --- Band 0: Three kinds of atlas map
        self.write_rows(0, "Three kinds of atlas map", [
            "World map, 1:100 000 000: 1 cm = 1 000 km",
            "Regional map, 1:10 000 000: 1 cm = 100 km",
            "Local map, 1:250 000 or 1:50 000",
            "Larger area, smaller scale, less detail",
        ], scale=0.86, box=3)
        # --- Band 1: Ratio scale 1:50 000
        self.next_band(1)
        self.write_rows(1, "Ratio scale 1:50 000", [
            "1 unit on the map = 50 000 same units on the ground",
            "Same unit both sides: no units written",
            "Smaller denominator = larger scale",
            "1:10 000 > 1:50 000 > 1:1 000 000",
        ], scale=0.8, box=2)
        # --- Band 2: Converting scales
        self.next_band(2)
        self.write_rows(2, "Converting scales", [
            "1 km = 100 000 cm",
            "1:250 000: 250 000 $\\div$ 100 000 = 2,5, so 1 cm = 2,5 km",
            "1 cm = 5 km: 5 $\\times$ 100 000 = 500 000, so 1:500 000",
            "Line scale 4 cm = 2 km: 1 cm = 0,5 km, so 1:50 000",
        ], scale=0.8, box=0)
        # --- Band 3: Comparing scales
        self.next_band(3)
        self.write_rows(3, "Comparing scales", [
            "Map A 1:50 000: 1 cm = 0,5 km; 10 km = 20 cm",
            "Map B 1:250 000: 1 cm = 2,5 km; 10 km = 4 cm",
            "Map A is the larger scale, five times the detail",
            "Never write 1 cm:50 000 km",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Same page, different zoom
        self.next_band(4)
        self.write_rows(4, "Same page, different zoom", [
            "Zoom out: whole world, small scale",
            "Zoom in: your street, large scale",
            "Pick the zoom for the question",
        ], scale=0.86)
        # --- Band 5: The number after the one
        self.next_band(5)
        self.write_rows(5, "The number after the one", [
            "1:50 000: one of anything = 50 000 of the same",
            "Big number after the one: small scale",
            "Small number after the one: large scale",
        ], scale=0.86, box=1)
        # --- Band 6: Converting without fear
        self.next_band(6)
        self.write_rows(6, "Converting without fear", [
            "Knock off five zeros: 1:250 000 gives 2,5 km",
            "1:50 000 gives 0,5 km = 500 m",
            "Add five zeros: 1 cm = 5 km gives 1:500 000",
        ], scale=0.86, box=0)
        self.wait(4)
