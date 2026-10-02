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

# Band-layout whiteboard scene for distance-from-the-sea-johannesburg-and-cape-town (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (210/290/280/230/150/150/150 of 1460 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class DistanceFromTheSeaJohannesburgAndCapeTownSession(MovingCameraScene):
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
        # --- Band 0: Land and sea
        self.write_rows(0, "Land and sea", [
            "Water: high specific heat",
            "Sunlight penetrates; waves mix",
            "Evaporation uses energy",
            "The sea stores heat",
        ], scale=0.86, box=3)
        # --- Band 1: Johannesburg and Cape Town
        self.next_band(1)
        self.write_rows(1, "Johannesburg and Cape Town", [
            "July: 17 \\textdegree{}C and 4 \\textdegree{}C in Johannesburg",
            "July: 18 \\textdegree{}C and 7 \\textdegree{}C in Cape Town",
            "Daily range: 13 \\textdegree{}C against 11 \\textdegree{}C",
            "Altitude and latitude differ too",
        ], scale=0.86, box=2)
        # --- Band 2: Maritime and continental
        self.next_band(2)
        self.write_rows(2, "Maritime and continental", [
            "Vancouver range about 14 \\textdegree{}C",
            "Winnipeg range about 36 \\textdegree{}C",
            "Upington: hot days, frosty nights",
            "Sea breeze by day, land breeze by night",
        ], scale=0.86, box=1)
        # --- Band 3: Writing explanations
        self.next_band(3)
        self.write_rows(3, "Writing explanations", [
            "Data, factor, property of water, result",
            "About 6.5 \\textdegree{}C per 1 000 m",
            "Check latitude and currents",
            "The sea moderates; it does not heat",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Hot sand, cool water
        self.next_band(4)
        self.write_rows(4, "Hot sand, cool water", [
            "Land: fast to heat and cool",
            "Water: slow to heat and cool",
            "The sea is a storage heater",
        ], scale=0.86, box=2)
        # --- Band 5: Frost and dew
        self.next_band(5)
        self.write_rows(5, "Frost and dew", [
            "Johannesburg: frosty nights",
            "Cape Town: mild nights",
        ], scale=0.86, box=0)
        # --- Band 6: Coasts and insides
        self.next_band(6)
        self.write_rows(6, "Coasts and insides", [
            "Big continents, big extremes",
            "Upington against Durban",
        ], scale=0.86, box=0)
        self.wait(4)
