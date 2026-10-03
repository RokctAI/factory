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

# Band-layout whiteboard scene for allied-and-central-powers (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/280/300/260/130/130/130 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class AlliedAndCentralPowersSession(MovingCameraScene):
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
        # --- Band 0: The Allies
        self.write_rows(0, "The Allies", [
            "Britain, France, Russia",
            "Japan 1914, Italy 1915",
            "United States, April 1917",
            "Russia left, March 1918",
        ], scale=0.86, box=2)
        # --- Band 1: The Central Powers
        self.next_band(1)
        self.write_rows(1, "The Central Powers", [
            "Germany and Austria-Hungary",
            "Ottoman Empire, 1914",
            "Bulgaria, 1915",
            "Blockade and hunger",
        ], scale=0.86, box=3)
        # --- Band 2: A world war
        self.next_band(2)
        self.write_rows(2, "A world war", [
            "Western and Eastern Fronts",
            "Gallipoli and the Middle East",
            "South West Africa, 1915",
            "East Africa to 1918",
        ], scale=0.86, box=2)
        # --- Band 3: Counting the months
        self.next_band(3)
        self.write_rows(3, "Counting the months", [
            "48 + 3 = 51 months",
            "United States: 19 months",
            "19 $\\div$ 51 = about 0.37",
            "Two colours and neutrals",
        ], scale=0.86, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Two sides
        self.next_band(4)
        self.write_rows(4, "Two sides", [
            "Allies and Central Powers",
        ], scale=0.86, box=0)
        # --- Band 5: War around the world
        self.next_band(5)
        self.write_rows(5, "War around the world", [
            "South Africa in Namibia",
        ], scale=0.86, box=0)
        # --- Band 6: Colours on the map
        self.next_band(6)
        self.write_rows(6, "Colours on the map", [
            "Germany surrounded",
        ], scale=0.86, box=0)
        self.wait(4)
