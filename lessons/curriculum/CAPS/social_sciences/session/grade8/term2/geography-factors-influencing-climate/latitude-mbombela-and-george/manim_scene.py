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

# Band-layout whiteboard scene for latitude-mbombela-and-george (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (290/230/240/240/150/150/150 of 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class LatitudeMbombelaAndGeorgeSession(MovingCameraScene):
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
        # --- Band 0: What latitude does
        self.write_rows(0, "What latitude does", [
            "Direct rays: concentrated heat",
            "Slanting rays: spread thin",
            "More atmosphere at a slant",
            "Bigger seasons further from the equator",
        ], scale=0.86, box=0)
        # --- Band 1: Mbombela and George
        self.next_band(1)
        self.write_rows(1, "Mbombela and George", [
            "Mbombela about 25.5\\textdegree{} S; George about 34\\textdegree{} S",
            "January: about 24 \\textdegree{}C and 20 \\textdegree{}C",
            "Annual range: 9 \\textdegree{}C and 7 \\textdegree{}C",
            "Mbombela higher, yet warmer",
        ], scale=0.86, box=3)
        # --- Band 2: Latitude and rainfall
        self.next_band(2)
        self.write_rows(2, "Latitude and rainfall", [
            "Rising air at the equator: rain",
            "Sinking air near 30\\textdegree{}: dry",
            "Belts move south in summer",
            "Summer, winter and all-year rainfall",
        ], scale=0.86, box=3)
        # --- Band 3: Using climate data
        self.next_band(3)
        self.write_rows(3, "Using climate data", [
            "30-year averages",
            "Lines for temperature, bars for rain",
            "About 111 km per degree of latitude",
            "Name the factor, explain, qualify",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The torch test
        self.next_band(4)
        self.write_rows(4, "The torch test", [
            "Straight down: bright spot",
            "Tilted: dim patch",
            "Near the equator is warmer",
        ], scale=0.86, box=2)
        # --- Band 5: Mbombela versus George
        self.next_band(5)
        self.write_rows(5, "Mbombela versus George", [
            "24 \\textdegree{}C against 20 \\textdegree{}C in January",
            "Higher but still warmer",
        ], scale=0.86, box=1)
        # --- Band 6: When the rain comes
        self.next_band(6)
        self.write_rows(6, "When the rain comes", [
            "Summer storms in Mbombela",
            "Rain all year in George",
        ], scale=0.86, box=1)
        self.wait(4)
