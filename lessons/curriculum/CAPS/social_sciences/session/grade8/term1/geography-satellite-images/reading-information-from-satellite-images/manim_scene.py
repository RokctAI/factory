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

# Band-layout whiteboard scene for reading-information-from-satellite-images (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/210/200/320/150/150/150 of 1370 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ReadingInformationFromSatelliteImagesSession(MovingCameraScene):
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
        # --- Band 0: The interpreter's clues
        self.write_rows(0, "The interpreter's clues", [
            "Tone and colour, texture, shape, size",
            "Pattern, shadow, location and association",
            "Check: north, resolution, date, true or false colour",
            "People: straight lines and circles. Nature: irregular",
        ], scale=0.8, box=3)
        # --- Band 1: Water and vegetation
        self.next_band(1)
        self.write_rows(1, "Water and vegetation", [
            "Deep water: dark. Muddy water: brown",
            "Dam: straight wall, arms up the valleys",
            "Plantations: dark blocks with straight edges",
            "Green circles: centre-pivot irrigation on the Orange River",
        ], scale=0.8, box=3)
        # --- Band 2: Land use and settlements
        self.next_band(2)
        self.write_rows(2, "Land use and settlements", [
            "Suburbs: grids. Informal settlements: dense fine texture",
            "Witwatersrand mine dumps: pale yellow, east to west",
            "Harbours, runways, roads and railways",
            "Change detection: compare two dates",
        ], scale=0.8, box=1)
        # --- Band 3: Cloud patterns
        self.next_band(3)
        self.write_rows(3, "Cloud patterns", [
            "Cold front: long curved band moving east",
            "Thunderstorms: bright clusters over the Highveld",
            "Cyclone: spiral with an eye, clockwise in the south",
            "Infrared: brightest = coldest = highest",
        ], scale=0.8, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Be a detective
        self.next_band(4)
        self.write_rows(4, "Be a detective", [
            "Colour, roughness, shape, size, pattern, neighbours",
            "Check north, detail, date, colour type",
            "Start big: sea, coast, mountains",
        ], scale=0.8)
        # --- Band 5: Water, plants and people
        self.next_band(5)
        self.write_rows(5, "Water, plants and people", [
            "Dark water; red plants in false colour",
            "Green circles of irrigated fields",
            "Pale yellow mine dumps along the reef",
        ], scale=0.86, box=2)
        # --- Band 6: Reading the sky from above
        self.next_band(6)
        self.write_rows(6, "Reading the sky from above", [
            "Cold front: long band of cloud",
            "Thunderstorm: bright blob. Cyclone: spiral",
            "Fog: smooth grey sheet on the west coast",
        ], scale=0.86, box=0)
        self.wait(4)
