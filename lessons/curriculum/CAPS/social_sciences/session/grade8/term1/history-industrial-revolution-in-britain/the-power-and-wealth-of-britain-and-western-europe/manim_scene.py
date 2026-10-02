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

# Band-layout whiteboard scene for the-power-and-wealth-of-britain-and-western-europe (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (300/280/250/260/150/150/150 of 1540 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ThePowerAndWealthOfBritainAndWesternEuropeSession(MovingCameraScene):
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
        # --- Band 0: The workshop of the world
        self.write_rows(0, "The workshop of the world", [
            "About 2 percent of world population",
            "About half the world's iron and coal by 1860",
            "Coal, inventions, banks, railways",
            "Great Exhibition, Crystal Palace, 1851",
        ], scale=0.86, box=1)
        # --- Band 1: Trade, money and the navy
        self.next_band(1)
        self.write_rows(1, "Trade, money and the navy", [
            "Cotton in, cloth and machines out",
            "1846 Corn Laws repealed: free trade",
            "London banks finance the world",
            "Royal Navy guards routes, including the Cape",
        ], scale=0.86, box=3)
        # --- Band 2: Europe industrialises
        self.next_band(2)
        self.write_rows(2, "Europe industrialises", [
            "Belgium first on the continent",
            "Germany: Ruhr coal and steel; ahead in steel by 1900",
            "Second Industrial Revolution: steel, chemicals, electricity",
            "Rivalry for markets and colonies",
        ], scale=0.72, box=3)
        # --- Band 3: The cost to the world
        self.next_band(3)
        self.write_rows(3, "The cost to the world", [
            "Indian hand-weavers undercut",
            "Cotton grown by enslaved people until 1865",
            "Industrial weapons enable conquest of Africa",
            "South Africa: diamonds, gold, sugar",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Britain the workshop
        self.next_band(4)
        self.write_rows(4, "Britain the workshop", [
            "A glass palace full of machines",
            "Coal and iron side by side",
            "Railways from 1830",
        ], scale=0.86, box=0)
        # --- Band 5: Ships, money and empire
        self.next_band(5)
        self.write_rows(5, "Ships, money and empire", [
            "Cotton and wool in; goods out",
            "The strongest navy guards the seas",
            "Germany and others catch up",
        ], scale=0.86, box=1)
        # --- Band 6: Who paid the price
        self.next_band(6)
        self.write_rows(6, "Who paid the price", [
            "Indian weavers lose their work",
            "Europe conquers Africa",
            "Mine profits go overseas",
        ], scale=0.86, box=2)
        self.wait(4)
