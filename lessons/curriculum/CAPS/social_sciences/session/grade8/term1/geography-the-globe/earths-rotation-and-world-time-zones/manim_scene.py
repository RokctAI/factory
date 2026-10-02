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

# Band-layout whiteboard scene for earths-rotation-and-world-time-zones (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/190/280/230/150/150/150 of 1340 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class EarthsRotationAndWorldTimeZonesSession(MovingCameraScene):
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
        # --- Band 0: Rotation: day and night
        self.write_rows(0, "Rotation: day and night", [
            "West to east, once in 24 hours",
            "Circle of illumination: day side and night side",
            "Sun appears to rise in the east",
            "Equator speed: 40 000 km $\\div$ 24 h, about 1 670 km/h",
        ], scale=0.8, box=0)
        # --- Band 1: Longitude and time
        self.next_band(1)
        self.write_rows(1, "Longitude and time", [
            "360\\textdegree{} $\\div$ 24 h = 15\\textdegree{} per hour",
            "60 min $\\div$ 15 = 4 min per degree",
            "East is ahead: Durban about 52 min before Cape Town",
            "45\\textdegree{} apart: 45 $\\div$ 15 = 3 hours",
        ], scale=0.8, box=0)
        # --- Band 2: Time zones and SAST
        self.next_band(2)
        self.write_rows(2, "Time zones and SAST", [
            "Zones about 15\\textdegree{} wide; UTC at Greenwich",
            "SAST = UTC + 2, based on 30\\textdegree{}E",
            "14:00 SAST: 12:00 UTC, 21:00 Tokyo, 07:00 New York (winter)",
            "No daylight saving in South Africa",
        ], scale=0.72, box=1)
        # --- Band 3: The international date line
        self.next_band(3)
        self.write_rows(3, "The international date line", [
            "Roughly along 180\\textdegree{}",
            "Westward: add a day. Eastward: subtract a day",
            "Samoa, 2011: skipped Friday 30 December",
            "Flight: 20:00 SAST + 11 h = 07:00 SAST = 05:00 London",
        ], scale=0.8, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The ball and the torch
        self.next_band(4)
        self.write_rows(4, "The ball and the torch", [
            "Half lit, half dark",
            "Spin it: sunrise, day, sunset, night",
            "We are carried round to face the sun",
        ], scale=0.86)
        # --- Band 5: Fifteen degrees every hour
        self.next_band(5)
        self.write_rows(5, "Fifteen degrees every hour", [
            "15\\textdegree{} = 1 hour",
            "East is ahead",
            "South Africa: one zone, Greenwich + 2",
        ], scale=0.86, box=0)
        # --- Band 6: Where tomorrow begins
        self.next_band(6)
        self.write_rows(6, "Where tomorrow begins", [
            "Date line in the Pacific",
            "West across it: tomorrow. East: yesterday",
            "Leave 8 pm, fly 11 h, land 5 am London time",
        ], scale=0.86, box=2)
        self.wait(4)
