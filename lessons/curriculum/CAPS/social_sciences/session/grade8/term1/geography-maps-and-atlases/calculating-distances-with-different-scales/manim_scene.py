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

# Band-layout whiteboard scene for calculating-distances-with-different-scales (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/300/240/190/160/150/150 of 1370 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CalculatingDistancesWithDifferentScalesSession(MovingCameraScene):
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
        # --- Band 0: One method for every scale
        self.write_rows(0, "One method for every scale", [
            "Measure centre to centre, in cm",
            "Ratio route 1: 6,4 $\\times$ 250 000 = 1 600 000 cm = 16 km",
            "Ratio route 2: 1 cm = 2,5 km; 6,4 $\\times$ 2,5 = 16 km",
            "1:50 000: 7,4 cm $\\times$ 0,5 = 3,7 km",
        ], scale=0.8, box=1)
        # --- Band 1: South Africa at regional scales
        self.next_band(1)
        self.write_rows(1, "South Africa at regional scales", [
            "1:10 000 000: Johannesburg to Cape Town 12,6 cm = 1 260 km",
            "1:5 000 000: Johannesburg to Durban 10 cm = 500 km",
            "N1 by road: about 1 400 km",
            "Time = distance $\\div$ speed: 570 $\\div$ 80 is about 7 h 8 min",
        ], scale=0.8, box=0)
        # --- Band 2: Across the world
        self.next_band(2)
        self.write_rows(2, "Across the world", [
            "1:100 000 000: 1 cm = 1 000 km",
            "Johannesburg to London 9,1 cm: about 9 100 km",
            "Flat maps stretch the round Earth: projection",
            "Globe and taut string: the shortest route",
        ], scale=0.86, box=3)
        # --- Band 3: Working backwards
        self.next_band(3)
        self.write_rows(3, "Working backwards", [
            "Map distance = real distance $\\div$ what 1 cm represents",
            "1 260 km $\\div$ 100 = 12,6 cm",
            "Scale: 3 000 000 cm $\\div$ 12 cm = 250 000, so 1:250 000",
            "Always state the unit and check it is sensible",
        ], scale=0.8, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Ruler, multiply, kilometres
        self.next_band(4)
        self.write_rows(4, "Ruler, multiply, kilometres", [
            "What does 1 cm stand for? Knock off five zeros",
            "1:50 000: half a kilometre",
            "7,4 cm on that map: 3,7 km",
        ], scale=0.86)
        # --- Band 5: Same trip, bigger map
        self.next_band(5)
        self.write_rows(5, "Same trip, bigger map", [
            "Straight line: 1 260 km. N1: about 1 400 km",
            "Road distance: follow it with string",
            "Long trips: globe and string",
        ], scale=0.86, box=2)
        # --- Band 6: Working backwards
        self.next_band(6)
        self.write_rows(6, "Working backwards", [
            "Real to map: divide",
            "30 km = 3 000 000 cm; $\\div$ 12 = 250 000",
            "Scale 1:250 000",
        ], scale=0.86, box=2)
        self.wait(4)
