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

# Band-layout whiteboard scene for urbanisation-in-south-africa-and-apartheid-controls (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/280/280/230/130/130/130 of 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class UrbanisationInSouthAfricaSession(MovingCameraScene):
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
        # --- Band 0: How the cities grew
        self.write_rows(0, "How the cities grew", [
            "Diamonds 1867, gold 1886",
            "Migrant labour",
            "Factories in the 1940s",
            "Fear of African urbanisation",
        ], scale=0.86, box=2)
        # --- Band 1: Controlling the cities
        self.next_band(1)
        self.write_rows(1, "Controlling the cities", [
            "Urban Areas Act, 1923",
            "Influx control and the dompas",
            "Section 10",
            "Group Areas Act, 1950",
        ], scale=0.86, box=1)
        # --- Band 2: Homelands and 1986
        self.next_band(2)
        self.write_rows(2, "Homelands and 1986", [
            "Homelands on 13 per cent",
            "Displaced urbanisation",
            "Influx control ends, 1986",
            "Homelands reincorporated, 1994",
        ], scale=0.86, box=1)
        # --- Band 3: Commuting and sources
        self.next_band(3)
        self.write_rows(3, "Commuting and sources", [
            "2.5 x 2 = 5 hours a day",
            "5 x 5 = 25 hours a week",
            "Who made the source?",
            "The pattern remains",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: How the cities grew
        self.next_band(4)
        self.write_rows(4, "How the cities grew", [
            "Mining camp to city",
        ], scale=0.86, box=0)
        # --- Band 5: Passes and removals
        self.next_band(5)
        self.write_rows(5, "Passes and removals", [
            "The dompas",
        ], scale=0.86, box=0)
        # --- Band 6: Homelands and long journeys
        self.next_band(6)
        self.write_rows(6, "Homelands and long journeys", [
            "Hours on the bus",
        ], scale=0.86, box=0)
        self.wait(4)
