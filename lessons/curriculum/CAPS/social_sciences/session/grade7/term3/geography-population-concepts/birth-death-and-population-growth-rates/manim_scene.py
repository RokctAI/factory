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

# Band-layout whiteboard scene for birth-death-and-population-growth-rates (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/210/190/200/90/90/90 of 1040 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class BirthDeathAndPopulationGrowthRatesSession(MovingCameraScene):
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
        # --- Band 0: Population and the Census
        self.write_rows(0, "Population and the Census", [
            "Population: people in an area at a time",
            "Census: count everyone; 2022: about 62 million",
            "Stats SA plans schools, clinics, water",
            "Every count is an estimate",
        ], scale=0.8, box=1)
        # --- Band 1: Birth Rate and Death Rate
        self.next_band(1)
        self.write_rows(1, "Birth Rate and Death Rate", [
            "Rates per 1000 compare places fairly",
            "Birth rate: births / population x 1000",
            "1000 / 50 000 x 1000 = 20",
            "SA: about 19 births, 9 to 10 deaths per 1000",
        ], scale=0.86, box=1)
        # --- Band 2: Natural Increase and Growth Rate
        self.next_band(2)
        self.write_rows(2, "Natural Increase and Growth Rate", [
            "Natural increase = birth rate - death rate",
            "20 - 8 = 12 per 1000 = 1.2 percent",
            "Add migration for the full growth rate",
            "Doubling time: about 70 / growth rate",
        ], scale=0.86, box=1)
        # --- Band 3: Reading Population Figures
        self.next_band(3)
        self.write_rows(3, "Reading Population Figures", [
            "Niger: over 3 percent a year",
            "South Africa: about 1 percent",
            "Japan: natural decrease",
            "Formula, numbers, answer, meaning",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Counting Everyone
        self.next_band(4)
        self.write_rows(4, "Counting Everyone", [
            "A census counts everyone",
            "About 62 million in 2022",
            "Numbers help plan services",
        ], scale=0.86, box=0)
        # --- Band 5: Per Thousand
        self.next_band(5)
        self.write_rows(5, "Per Thousand", [
            "Births per 1000 people",
            "Deaths per 1000 people",
            "Births minus deaths; divide by 10 for percent",
        ], scale=0.8, box=0)
        # --- Band 6: Fast, Slow and Shrinking
        self.next_band(6)
        self.write_rows(6, "Fast, Slow and Shrinking", [
            "Niger: fast",
            "South Africa: about 1 percent",
            "Japan: shrinking",
        ], scale=0.86, box=0)
        self.wait(4)
