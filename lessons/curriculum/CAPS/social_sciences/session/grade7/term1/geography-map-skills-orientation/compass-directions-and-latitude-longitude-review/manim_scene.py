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

# Band-layout whiteboard scene for compass-directions-and-latitude-longitude-review (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/210/190/200/90/90/100 of 1070 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CompassDirectionsAndLatitudeLongitudeReviewSession(MovingCameraScene):
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
        # --- Band 0: Social Sciences in Grade 7
        self.write_rows(0, "Social Sciences in Grade 7", [
            "Social Sciences: Geography and History",
            "Formal tasks count; informal tasks guide",
            "Term 1 project: local maps (50 marks)",
            "Name, describe, explain, compare, calculate",
        ], scale=0.86, box=1)
        # --- Band 1: The Eight Points of the Compass
        self.next_band(1)
        self.write_rows(1, "The Eight Points of the Compass", [
            "N, E, S, W: the cardinal points",
            "NE, SE, SW, NW: the intermediate points",
            "45 degrees between neighbouring points",
            "Stand at the from-place and face north",
        ], scale=0.86, box=1)
        # --- Band 2: Latitude in Degrees
        self.next_band(2)
        self.write_rows(2, "Latitude in Degrees", [
            "Latitude: north or south of the equator",
            "Equator 0 degrees; poles 90 degrees N and S",
            "Tropic of Capricorn: about 23.5 degrees S",
            "South Africa: about 22 to 35 degrees S",
        ], scale=0.86, box=1)
        # --- Band 3: Longitude and Giving a Position
        self.next_band(3)
        self.write_rows(3, "Longitude and Giving a Position", [
            "Longitude: east or west of Greenwich",
            "Prime Meridian 0 degrees; up to 180 degrees",
            "Latitude first, longitude second",
            "Cape Town: about 34 degrees S, 18 degrees E",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A Year of Geography
        self.next_band(4)
        self.write_rows(4, "A Year of Geography", [
            "Two parts: Geography and History",
            "Practice work and work for marks",
            "Explain means because",
        ], scale=0.86, box=0)
        # --- Band 5: Which Way Is It?
        self.next_band(5)
        self.write_rows(5, "Which Way Is It?", [
            "N, NE, E, SE, S, SW, W, NW",
            "Stand at the from-place, face north",
            "Flip it round: NE becomes SW",
        ], scale=0.86, box=0)
        # --- Band 6: An Address for Every Place
        self.next_band(6)
        self.write_rows(6, "An Address for Every Place", [
            "Latitude: across, from the equator",
            "Longitude: pole to pole, from Greenwich",
            "Latitude first, letters always",
        ], scale=0.86, box=0)
        self.wait(4)
