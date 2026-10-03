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

# Band-layout whiteboard scene for women-in-the-workplace (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (260/260/260/300/130/130/130 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class WomenInTheWorkplaceSession(MovingCameraScene):
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
        # --- Band 0: Before and why
        self.write_rows(0, "Before and why", [
            "Domestic service and mills",
            "Total war",
            "Shell crisis, 1915",
            "Dilution agreements",
        ], scale=0.86, box=2)
        # --- Band 1: Munitions and industry
        self.next_band(1)
        self.write_rows(1, "Munitions and industry", [
            "About 900 000 munitionettes",
            "The canaries and TNT",
            "Barnbow and Silvertown",
            "Buses, trams, offices",
        ], scale=0.86, box=1)
        # --- Band 2: Land, uniform and nursing
        self.next_band(2)
        self.write_rows(2, "Land, uniform and nursing", [
            "Women's Land Army, 1917",
            "WAAC, WRNS, WRAF",
            "VADs and the FANY",
            "Edith Cavell, 1915",
        ], scale=0.86, box=0)
        # --- Band 3: After the war
        self.next_band(3)
        self.write_rows(3, "After the war", [
            "7.3 - 5.9 = 1.4 million",
            "1.4 $\\div$ 5.9 = about 0.24",
            "Restoration Act, 1919",
            "Change, but limited",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: New jobs
        self.next_band(4)
        self.write_rows(4, "New jobs", [
            "Men away at war",
        ], scale=0.86, box=0)
        # --- Band 5: Shells, farms, uniforms
        self.next_band(5)
        self.write_rows(5, "Shells, farms, uniforms", [
            "Dangerous but better paid",
        ], scale=0.86, box=0)
        # --- Band 6: When the men came home
        self.next_band(6)
        self.write_rows(6, "When the men came home", [
            "Jobs lost, some gains",
        ], scale=0.86, box=0)
        self.wait(4)
