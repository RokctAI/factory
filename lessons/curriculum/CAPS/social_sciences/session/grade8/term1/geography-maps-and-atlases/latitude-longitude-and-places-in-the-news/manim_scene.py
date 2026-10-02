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

# Band-layout whiteboard scene for latitude-longitude-and-places-in-the-news (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/200/180/220/160/150/150 of 1330 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class LatitudeLongitudeAndPlacesInTheNewsSession(MovingCameraScene):
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
        # --- Band 0: Latitude and longitude
        self.write_rows(0, "Latitude and longitude", [
            "Latitude: N or S of the equator, 0\\textdegree{} to 90\\textdegree{}",
            "Longitude: E or W of Greenwich, 0\\textdegree{} to 180\\textdegree{}",
            "Tropic of Capricorn about 23\\textdegree{}26'S, just north of Polokwane",
            "South Africa: about 22\\textdegree{}S to 35\\textdegree{}S, 16\\textdegree{}E to 33\\textdegree{}E",
        ], scale=0.8, box=0)
        # --- Band 1: Degrees and minutes
        self.next_band(1)
        self.write_rows(1, "Degrees and minutes", [
            "1\\textdegree{} = 60'; 1\\textdegree{} of latitude is about 111 km",
            "Latitude first: Johannesburg 26\\textdegree{}12'S 28\\textdegree{}03'E",
            "Cape Town 33\\textdegree{}55'S 18\\textdegree{}25'E",
            "Halfway from 28\\textdegree{}E to 29\\textdegree{}E: 28\\textdegree{}30'E",
        ], scale=0.86, box=1)
        # --- Band 2: The atlas index
        self.next_band(2)
        self.write_rows(2, "The atlas index", [
            "Name, country, page, grid square, coordinates",
            "Polokwane: page 25, C3, 23\\textdegree{}54'S 29\\textdegree{}28'E",
            "In reverse: 19\\textdegree{}50'S 34\\textdegree{}51'E is Beira",
            "Check: South African towns fall in 22\\textdegree{}S to 35\\textdegree{}S",
        ], scale=0.86, box=2)
        # --- Band 3: Places in the news
        self.next_band(3)
        self.write_rows(3, "Places in the news", [
            "Cyclone Idai, March 2019: Beira, Mozambique",
            "Durban floods, April 2022: 29\\textdegree{}52'S 31\\textdegree{}01'E",
            "Absolute location: coordinates. Relative: near what?",
            "Never 26\\textdegree{}75'S; never longitude N or S",
        ], scale=0.8, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: An address for the whole planet
        self.next_band(4)
        self.write_rows(4, "An address for the whole planet", [
            "Belts: latitude, how far north or south",
            "Orange segments: longitude, how far east or west",
            "South Africa: always S and E",
        ], scale=0.86, box=2)
        # --- Band 5: Degrees and minutes like a clock
        self.next_band(5)
        self.write_rows(5, "Degrees and minutes like a clock", [
            "60 minutes in a degree, like an hour",
            "Latitude first, letters always",
            "Halfway is 30 minutes; a fifth is 12",
        ], scale=0.86, box=1)
        # --- Band 6: From headline to map pin
        self.next_band(6)
        self.write_rows(6, "From headline to map pin", [
            "Index: page, square, address",
            "Beira 19\\textdegree{}50'S 34\\textdegree{}51'E: warm Indian Ocean coast",
            "Keep a news map all year",
        ], scale=0.86, box=2)
        self.wait(4)
