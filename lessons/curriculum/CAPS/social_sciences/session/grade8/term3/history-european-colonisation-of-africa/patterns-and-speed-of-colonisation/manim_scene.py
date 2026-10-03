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

# Band-layout whiteboard scene for patterns-and-speed-of-colonisation (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (300/240/290/230/130/130/130 of 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class PatternsAndSpeedSession(MovingCameraScene):
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
        # --- Band 0: Patterns of colonisation
        self.write_rows(0, "Patterns of colonisation", [
            "Coast to interior",
            "Rivers, routes, railways",
            "Settler and non-settler",
            "Direct and indirect rule",
        ], scale=0.86, box=0)
        # --- Band 1: Why so fast?
        self.next_band(1)
        self.write_rows(1, "Why so fast?", [
            "Maxim gun and rifles",
            "Quinine, steamships, telegraph",
            "African soldiers, divide and rule",
            "Rinderpest in the 1890s",
        ], scale=0.86, box=0)
        # --- Band 2: African resistance
        self.next_band(2)
        self.write_rows(2, "African resistance", [
            "Samori Toure",
            "Herero and Nama genocide",
            "Maji Maji, 1905 to 1907",
            "Adwa, 1 March 1896",
        ], scale=0.86, box=3)
        # --- Band 3: Weighing the reasons
        self.next_band(3)
        self.write_rows(3, "Weighing the reasons", [
            "10 000 $\\div$ 50 = 200",
            "Technology, divisions, disease",
            "Adwa: closing the gap",
            "Read sources for purpose",
        ], scale=0.86, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Coast first, then inland
        self.next_band(4)
        self.write_rows(4, "Coast first, then inland", [
            "Arrows from the coast",
        ], scale=0.86, box=0)
        # --- Band 5: Why so fast?
        self.next_band(5)
        self.write_rows(5, "Why so fast?", [
            "Guns, medicine, divisions",
        ], scale=0.86, box=0)
        # --- Band 6: Africans fought back
        self.next_band(6)
        self.write_rows(6, "Africans fought back", [
            "Adwa, 1896",
        ], scale=0.86, box=0)
        self.wait(4)
