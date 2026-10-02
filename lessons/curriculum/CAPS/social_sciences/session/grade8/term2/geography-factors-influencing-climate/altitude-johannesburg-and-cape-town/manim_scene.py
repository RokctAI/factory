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

# Band-layout whiteboard scene for altitude-johannesburg-and-cape-town (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (310/230/260/240/150/150/150 of 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class AltitudeJohannesburgAndCapeTownSession(MovingCameraScene):
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
        # --- Band 0: Why higher is colder
        self.write_rows(0, "Why higher is colder", [
            "Air heated from the ground below",
            "Thin air holds less heat",
            "Rising air expands and cools",
            "About 6.5 \\textdegree{}C per 1 000 m",
        ], scale=0.86, box=3)
        # --- Band 1: Johannesburg and Cape Town
        self.next_band(1)
        self.write_rows(1, "Johannesburg and Cape Town", [
            "Johannesburg about 1 750 m; Cape Town 0 m",
            "Means: about 16 \\textdegree{}C and 17 \\textdegree{}C",
            "1.75 $\\times$ 6.5 $\\approx$ 11.4 \\textdegree{}C cooler",
            "Frost and boiling at about 94 \\textdegree{}C",
        ], scale=0.86, box=2)
        # --- Band 2: Altitude in South Africa
        self.next_band(2)
        self.write_rows(2, "Altitude in South Africa", [
            "Plateau 1 000 to 2 000 m",
            "Drakensberg over 3 000 m",
            "Sutherland: cold and clear",
            "Kilimanjaro: ice near the equator",
        ], scale=0.86, box=2)
        # --- Band 3: Calculations
        self.next_band(3)
        self.write_rows(3, "Calculations", [
            "Height $\\div$ 1 000 $\\times$ 6.5",
            "2 $\\times$ 6.5 = 13",
            "24 -- 13 = 11 \\textdegree{}C",
            "Inversions in valleys",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Colder as you climb
        self.next_band(4)
        self.write_rows(4, "Colder as you climb", [
            "The sun heats the ground first",
            "Thin air, no blanket",
        ], scale=0.86, box=1)
        # --- Band 5: Johannesburg up high
        self.next_band(5)
        self.write_rows(5, "Johannesburg up high", [
            "Closer to the equator but cooler",
            "Frosty winter mornings",
        ], scale=0.86, box=1)
        # --- Band 6: Snow on the equator
        self.next_band(6)
        self.write_rows(6, "Snow on the equator", [
            "Kilimanjaro's icy top",
            "Snow in the Drakensberg",
        ], scale=0.86, box=0)
        self.wait(4)
