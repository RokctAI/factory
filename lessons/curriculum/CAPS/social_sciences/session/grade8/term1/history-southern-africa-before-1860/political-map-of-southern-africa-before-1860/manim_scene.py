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

# Band-layout whiteboard scene for political-map-of-southern-africa-before-1860 (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (280/250/260/230/150/150/150 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class PoliticalMapOfSouthernAfricaBefore1860Session(MovingCameraScene):
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
        # --- Band 0: The British colonies
        self.write_rows(0, "The British colonies", [
            "Cape: Dutch from 1652, British from 1806",
            "Slavery ends 1834; parliament 1853",
            "Natal: British from 1843; colony 1856",
            "Shepstone's locations for Africans",
        ], scale=0.86, box=1)
        # --- Band 1: The Boer republics
        self.next_band(1)
        self.write_rows(1, "The Boer republics", [
            "Great Trek from 1835",
            "1852 Sand River: South African Republic",
            "1854 Bloemfontein: Orange Free State",
            "Vote only for white men",
        ], scale=0.86, box=1)
        # --- Band 2: African kingdoms
        self.next_band(2)
        self.write_rows(2, "African kingdoms", [
            "Zulu: Mpande, Cetshwayo rising",
            "Swazi: Mswati II",
            "Basotho: Moshoeshoe at Thaba Bosiu",
            "Pedi, Tswana, Xhosa, Mpondo, Venda, Griqua",
        ], scale=0.86, box=2)
        # --- Band 3: Relations on the map
        self.next_band(3)
        self.write_rows(3, "Relations on the map", [
            "Trade: ivory and cattle for guns and cloth",
            "Conflict over land, cattle and labour",
            "Diplomacy and treaties",
            "No single South Africa until 1910",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Two British colonies
        self.next_band(4)
        self.write_rows(4, "Two British colonies", [
            "The Cape on the sea road to India",
            "Natal on the east coast",
            "Sugar from the 1850s",
        ], scale=0.86, box=0)
        # --- Band 5: Two Boer republics
        self.next_band(5)
        self.write_rows(5, "Two Boer republics", [
            "Wagons leave the Cape from 1835",
            "Transvaal north of the Vaal",
            "Free State between Orange and Vaal",
        ], scale=0.86, box=0)
        # --- Band 6: African kingdoms everywhere
        self.next_band(6)
        self.write_rows(6, "African kingdoms everywhere", [
            "Most of the land under African rulers",
            "Thaba Bosiu never captured",
            "Land and cattle at the centre",
        ], scale=0.86, box=0)
        self.wait(4)
