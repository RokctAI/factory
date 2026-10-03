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

# Band-layout whiteboard scene for salt-gold-and-trade-goods (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/170/200/200/90/90/100 of 1010 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SaltGoldAndTradeGoodsSession(MovingCameraScene):
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
        # --- Band 0: Why Trade Across the Desert
        self.write_rows(0, "Why Trade Across the Desert", [
            "Different regions, different goods",
            "North Africa, Sahara, Sahel, savanna",
            "Berber and Wangara merchants",
            "Kings taxed the trade",
        ], scale=0.86, box=1)
        # --- Band 1: Salt From the North
        self.next_band(1)
        self.write_rows(1, "Salt From the North", [
            "Salt: needed for life and preserving food",
            "Taghaza: houses built of salt",
            "Slabs of about 30 kg on camels",
            "Value rose with every kilometre south",
        ], scale=0.86, box=1)
        # --- Band 2: Gold and Other Goods From the South
        self.next_band(2)
        self.write_rows(2, "Gold and Other Goods From the South", [
            "Gold fields: Bambuk, Bure, Akan",
            "Much of Europe's gold came from West Africa",
            "North: ivory, feathers, kola nuts",
            "South: salt, cloth, copper, horses, books",
        ], scale=0.86, box=1)
        # --- Band 3: The Trade in Enslaved People
        self.next_band(3)
        self.write_rows(3, "The Trade in Enslaved People", [
            "Captives taken north across the desert",
            "Many died on the journey",
            "Different from the later Atlantic trade",
            "Wealth for some, suffering for others",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: You Have What I Need
        self.next_band(4)
        self.write_rows(4, "You Have What I Need", [
            "North: cloth, metal, books",
            "Desert: salt",
            "West Africa: gold",
        ], scale=0.86, box=0)
        # --- Band 5: Salt and Gold
        self.next_band(5)
        self.write_rows(5, "Salt and Gold", [
            "Salt: for health and food",
            "Taghaza: salt houses",
            "Gold for half the world",
        ], scale=0.86, box=0)
        # --- Band 6: People Were Sold Too
        self.next_band(6)
        self.write_rows(6, "People Were Sold Too", [
            "Captives taken north",
            "Many died on the walk",
            "Tell both sides",
        ], scale=0.86, box=0)
        self.wait(4)
