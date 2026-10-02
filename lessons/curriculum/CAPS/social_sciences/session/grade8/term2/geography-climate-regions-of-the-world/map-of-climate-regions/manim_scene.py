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

# Band-layout whiteboard scene for map-of-climate-regions (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (260/260/260/240/150/150/150 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class MapOfClimateRegionsSession(MovingCameraScene):
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
        # --- Band 0: Reading the map
        self.write_rows(0, "Reading the map", [
            "Read the key first",
            "Equator, tropics, polar circles",
            "Side of the continent matters",
            "Matches vegetation maps",
        ], scale=0.86, box=0)
        # --- Band 1: Global belts
        self.next_band(1)
        self.write_rows(1, "Global belts", [
            "Rainforest near the equator",
            "Savanna, then deserts near the tropics",
            "Mediterranean west, subtropical east",
            "Temperate, continental, tundra, ice",
        ], scale=0.86, box=1)
        # --- Band 2: Southern Africa
        self.next_band(2)
        self.write_rows(2, "Southern Africa", [
            "Namib in the west",
            "Karoo and Kalahari semi-desert",
            "Summer rain in the east; Mediterranean south-west",
            "Rain decreases east to west",
        ], scale=0.8, box=3)
        # --- Band 3: Describing distribution
        self.next_band(3)
        self.write_rows(3, "Describing distribution", [
            "Latitude, continents, side, features",
            "Two or three examples",
            "150 $\\div$ 3 = 50 million km²",
            "Check the key",
        ], scale=0.86, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The coloured map
        self.next_band(4)
        self.write_rows(4, "The coloured map", [
            "Key first, then latitudes",
        ], scale=0.86, box=0)
        # --- Band 5: Belts around the earth
        self.next_band(5)
        self.write_rows(5, "Belts around the earth", [
            "Stripes from the equator to the poles",
        ], scale=0.86, box=0)
        # --- Band 6: Southern Africa's colours
        self.next_band(6)
        self.write_rows(6, "Southern Africa's colours", [
            "Wet east, dry west",
        ], scale=0.86, box=0)
        self.wait(4)
