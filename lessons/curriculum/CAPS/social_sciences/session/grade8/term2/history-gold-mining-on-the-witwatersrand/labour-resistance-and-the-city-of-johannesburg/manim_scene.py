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

# Band-layout whiteboard scene for labour-resistance-and-the-city-of-johannesburg (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/220/240/240/150/150/150 of 1420 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class LabourResistanceAndTheCityOfJohannesburgSession(MovingCameraScene):
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
        # --- Band 0: Everyday resistance
        self.write_rows(0, "Everyday resistance", [
            "No vote, no union, strikes risky",
            "Desertion",
            "Choosing mines, go-slows",
            "Burial societies, churches, music",
        ], scale=0.86, box=1)
        # --- Band 1: Strikes
        self.next_band(1)
        self.write_rows(1, "Strikes", [
            "White strikes: 1907, 1913, 1914",
            "Black miners' strike, 1913",
            "About 70 000 strike in 1920",
            "Chinese and Indian workers resist",
        ], scale=0.86, box=1)
        # --- Band 2: Johannesburg grows
        self.next_band(2)
        self.write_rows(2, "Johannesburg grows", [
            "1886: camp on Randjeslaagte",
            "1896: about 102 000 people",
            "Rich ridges, crowded centre",
            "Klipspruit, 1904",
        ], scale=0.86, box=3)
        # --- Band 3: City life
        self.next_band(3)
        self.write_rows(3, "City life", [
            "237 000 -- 102 000 = 135 000",
            "135 000 $\\div$ 15 = 9 000 a year",
            "Amawasha, traders, musicians",
            "Segregation before apartheid",
        ], scale=0.86, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Quiet ways of fighting back
        self.next_band(4)
        self.write_rows(4, "Quiet ways of fighting back", [
            "Run away, warn friends",
        ], scale=0.86, box=0)
        # --- Band 5: Strikes
        self.next_band(5)
        self.write_rows(5, "Strikes", [
            "Different groups, separate struggles",
        ], scale=0.86, box=0)
        # --- Band 6: The city of gold
        self.next_band(6)
        self.write_rows(6, "The city of gold", [
            "From tents to a divided city",
        ], scale=0.86, box=0)
        self.wait(4)
