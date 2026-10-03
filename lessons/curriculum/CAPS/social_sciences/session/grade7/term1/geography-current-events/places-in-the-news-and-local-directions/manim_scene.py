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

# Band-layout whiteboard scene for places-in-the-news-and-local-directions (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/190/210/220/90/90/100 of 1070 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class PlacesInTheNewsAndLocalDirectionsSession(MovingCameraScene):
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
        # --- Band 0: The World Map: Continents and Oceans
        self.write_rows(0, "The World Map: Continents and Oceans", [
            "7 continents, 5 oceans",
            "South Africa: Atlantic west, Indian east",
            "Flat maps distort size: Africa is huge",
            "0 degrees, 0 degrees: Gulf of Guinea",
        ], scale=0.86, box=1)
        # --- Band 1: Places in the News
        self.next_band(1)
        self.write_rows(1, "Places in the News", [
            "Mark each news place: date, event, place",
            "Earthquakes cluster round the Pacific",
            "Cyclone Idai, Beira, March 2019",
            "Continent, country, degrees",
        ], scale=0.86, box=1)
        # --- Band 2: Locating News Places in Degrees
        self.next_band(2)
        self.write_rows(2, "Locating News Places in Degrees", [
            "Nairobi: about 1 degree S, 37 degrees E",
            "Cairo 30 N, 31 E mirrors Durban 30 S, 31 E",
            "Estimate between the printed lines",
            "Atlas index lists latitude and longitude",
        ], scale=0.86, box=1)
        # --- Band 3: Compass Directions on a Local Sketch Map
        self.next_band(3)
        self.write_rows(3, "Compass Directions on a Local Sketch Map", [
            "Sketch map: simple, not to exact scale",
            "Find north first: compass or the sun",
            "Midday shadow points roughly south",
            "Use landmarks and the eight points",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The Big Picture
        self.next_band(4)
        self.write_rows(4, "The Big Picture", [
            "7 continents, 5 oceans",
            "Atlantic west, Indian east",
            "Africa is much bigger than it looks",
        ], scale=0.86, box=0)
        # --- Band 5: Pinning the News
        self.next_band(5)
        self.write_rows(5, "Pinning the News", [
            "Pin it: date, place, event",
            "Continent, country, numbers",
            "Check more than one source",
        ], scale=0.86, box=0)
        # --- Band 6: Which Way at Home?
        self.next_band(6)
        self.write_rows(6, "Which Way at Home?", [
            "Find north, draw the arrow first",
            "Landmarks: school, shop, tree",
            "Compass points, not left and right",
        ], scale=0.86, box=0)
        self.wait(4)
