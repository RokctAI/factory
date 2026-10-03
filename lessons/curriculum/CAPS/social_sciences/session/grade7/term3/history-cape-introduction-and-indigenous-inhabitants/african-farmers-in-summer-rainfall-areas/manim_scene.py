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

# Band-layout whiteboard scene for african-farmers-in-summer-rainfall-areas (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/170/180/180/90/90/90 of 960 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class AfricanFarmersInSummerRainfallAreasSession(MovingCameraScene):
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
        # --- Band 0: The Arrival of African Farmers
        self.write_rows(0, "The Arrival of African Farmers", [
            "Arrived about 2000 years ago from the north",
            "Bantu-speaking Iron Age farmers",
            "Ancestors of Nguni and Sotho-Tswana peoples",
            "Settled villages, crops, cattle, iron",
        ], scale=0.86, box=1)
        # --- Band 1: Rainfall and the 500 mm Line
        self.next_band(1)
        self.write_rows(1, "Rainfall and the 500 mm Line", [
            "Rainfall decreases from east to west",
            "Summer rain in most of SA",
            "Winter rain in the south-western Cape",
            "500 mm line: crops to the east",
        ], scale=0.86, box=4)
        # --- Band 2: Sorghum and Millet
        self.next_band(2)
        self.write_rows(2, "Sorghum and Millet", [
            "Sorghum and millet: African grains",
            "Need summer rain, about 500 mm",
            "Porridge and sorghum beer",
            "Maize came later from the Americas",
        ], scale=0.86, box=2)
        # --- Band 3: Cattle, Society and Meeting the Colony
        self.next_band(3)
        self.write_rows(3, "Cattle, Society and Meeting the Colony", [
            "Cattle: wealth, lobola, ceremonies",
            "Homesteads around a central kraal",
            "Chief allocated communal land",
            "1770s: trekboers meet Xhosa in the Zuurveld",
        ], scale=0.86, box=4)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The Farmers
        self.next_band(4)
        self.write_rows(4, "The Farmers", [
            "Arrived about 2000 years ago",
            "Villages, crops, cattle, iron",
            "Ancestors of many South Africans",
        ], scale=0.86, box=0)
        # --- Band 5: Follow the Rain
        self.next_band(5)
        self.write_rows(5, "Follow the Rain", [
            "More rain in the east",
            "Summer rain except around Cape Town",
            "Crops need about 500 mm",
        ], scale=0.86, box=0)
        # --- Band 6: Crops and Cattle
        self.next_band(6)
        self.write_rows(6, "Crops and Cattle", [
            "Sorghum and millet",
            "Cattle: wealth and lobola",
            "1770s: trekboers meet Xhosa",
        ], scale=0.86, box=0)
        self.wait(4)
