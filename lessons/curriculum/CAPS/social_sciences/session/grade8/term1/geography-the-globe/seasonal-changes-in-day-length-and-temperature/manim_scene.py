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

# Band-layout whiteboard scene for seasonal-changes-in-day-length-and-temperature (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (210/190/250/250/150/150/150 of 1350 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SeasonalChangesInDayLengthAndTemperatureSession(MovingCameraScene):
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
        # --- Band 0: Why day length changes
        self.write_rows(0, "Why day length changes", [
            "Tilt: circle of illumination cuts parallels unequally",
            "December: southern days longer than 12 hours",
            "Equinoxes: 12 hours everywhere; equator: 12 hours always",
            "Cape Town: about 14 h 25 min in December, 9 h 54 min in June",
        ], scale=0.72, box=3)
        # --- Band 1: Day length across the world
        self.next_band(1)
        self.write_rows(1, "Day length across the world", [
            "Musina, 22\\textdegree{}S: swing under 3 hours",
            "Cape Town, 34\\textdegree{}S: about 4,5 hours",
            "London, 51,5\\textdegree{}N: nearly 9 hours",
            "Poles: about 6 months day, 6 months night",
        ], scale=0.86, box=3)
        # --- Band 2: From day length to temperature
        self.next_band(2)
        self.write_rows(2, "From day length to temperature", [
            "High sun: concentrated energy",
            "Long days: more hours of heating, fewer of cooling",
            "Johannesburg: about 26\\textdegree{}C in January, 17\\textdegree{}C in July",
            "Durban: 28\\textdegree{}C and 23\\textdegree{}C, a small range beside the warm sea",
        ], scale=0.8, box=1)
        # --- Band 3: The seasonal lag
        self.next_band(3)
        self.write_rows(3, "The seasonal lag", [
            "Hottest: January and February, not December",
            "Coldest: July, not June",
            "Land and sea store heat",
            "Summer Dec to Feb; autumn Mar to May; winter Jun to Aug; spring Sep to Nov",
        ], scale=0.72, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Long days, short days
        self.next_band(4)
        self.write_rows(4, "Long days, short days", [
            "Cape Town: 14,5 hours in December, under 10 in June",
            "Equator: about 12 hours all year",
            "Poles: one long day, one long night",
        ], scale=0.8, box=0)
        # --- Band 5: Two reasons it gets hot
        self.next_band(5)
        self.write_rows(5, "Two reasons it gets hot", [
            "High sun: straight torch",
            "Long days: more heating, less cooling",
            "Warm sea keeps Durban mild",
        ], scale=0.86, box=1)
        # --- Band 6: The stove that keeps heating
        self.next_band(6)
        self.write_rows(6, "The stove that keeps heating", [
            "Hottest month after the longest day",
            "Coldest month after the shortest day",
            "Seasons set farming, nature and school holidays",
        ], scale=0.86, box=0)
        self.wait(4)
