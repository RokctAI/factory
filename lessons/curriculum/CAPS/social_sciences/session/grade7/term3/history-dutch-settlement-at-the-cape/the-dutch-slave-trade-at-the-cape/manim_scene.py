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

# Band-layout whiteboard scene for the-dutch-slave-trade-at-the-cape (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/170/170/190/90/90/90 of 960 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TheDutchSlaveTradeAtTheCapeSession(MovingCameraScene):
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
        # --- Band 0: Why the Cape Turned to Slavery
        self.write_rows(0, "Why the Cape Turned to Slavery", [
            "Slavery: people owned as property",
            "Labour short; Europeans expensive",
            "VOC rules forbade enslaving the Khoikhoi",
            "1795: more slaves than free burghers",
        ], scale=0.86, box=1)
        # --- Band 1: Where Enslaved People Came From
        self.next_band(1)
        self.write_rows(1, "Where Enslaved People Came From", [
            "Africa: Mozambique, East Africa, Angola",
            "Madagascar",
            "India and Sri Lanka",
            "Indonesia: Java, Bali, Sulawesi, Timor",
        ], scale=0.86, box=2)
        # --- Band 2: How Enslaved People Were Brought
        self.next_band(2)
        self.write_rows(2, "How Enslaved People Were Brought", [
            "Captured in wars and raids, or sold in famine",
            "VOC voyages to Madagascar and Mozambique",
            "Crowded, deadly voyages",
            "Sold at auction; given new names",
        ], scale=0.8, box=3)
        # --- Band 3: The Slave Lodge and the End of the Trade
        self.next_band(3)
        self.write_rows(3, "The Slave Lodge and the End of the Trade", [
            "Slave Lodge, 1679: VOC's slaves",
            "Most slaves owned by wine and wheat farmers",
            "Trade to the Cape ended 1808",
            "Slavery abolished 1834; apprenticeship to 1838",
        ], scale=0.8, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Why Slaves?
        self.next_band(4)
        self.write_rows(4, "Why Slaves?", [
            "Workers needed",
            "First slaves arrived 1658",
            "More slaves than colonists by 1795",
        ], scale=0.86, box=0)
        # --- Band 5: From Where?
        self.next_band(5)
        self.write_rows(5, "From Where?", [
            "Africa and Madagascar",
            "India and Sri Lanka",
            "Indonesia",
        ], scale=0.86, box=0)
        # --- Band 6: How?
        self.next_band(6)
        self.write_rows(6, "How?", [
            "Captured or bought",
            "Sold at auction; renamed",
            "Slavery ended 1834",
        ], scale=0.86, box=0)
        self.wait(4)
