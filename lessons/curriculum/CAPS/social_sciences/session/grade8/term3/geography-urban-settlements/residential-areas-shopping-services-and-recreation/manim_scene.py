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

# Band-layout whiteboard scene for residential-areas-shopping-services-and-recreation (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (280/280/250/220/130/130/130 of 1420 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ResidentialAreasSession(MovingCameraScene):
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
        # --- Band 0: Residential areas
        self.write_rows(0, "Residential areas", [
            "High income: low density",
            "Middle income: medium density",
            "Low income: high density",
            "Informal settlements",
        ], scale=0.86, box=2)
        # --- Band 1: The apartheid city
        self.next_band(1)
        self.write_rows(1, "The apartheid city", [
            "Group Areas Act, 1950",
            "Forced removals",
            "Townships on the edge",
            "Buffer zones",
        ], scale=0.86, box=0)
        # --- Band 2: Shops, services, recreation
        self.next_band(2)
        self.write_rows(2, "Shops, services, recreation", [
            "Spaza shop to regional mall",
            "Low order and high order",
            "Clinics, schools, hospitals",
            "Parks on flood plains",
        ], scale=0.86, box=1)
        # --- Band 3: Density and evidence
        self.next_band(3)
        self.write_rows(3, "Density and evidence", [
            "10 000 $\\div$ 1 000 = 10 per ha",
            "10 000 $\\div$ 250 = 40 per ha",
            "Pools or packed roofs?",
            "Income plus history",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Where people live
        self.next_band(4)
        self.write_rows(4, "Where people live", [
            "Big plots, packed roofs",
        ], scale=0.86, box=0)
        # --- Band 5: Why it is so unequal
        self.next_band(5)
        self.write_rows(5, "Why it is so unequal", [
            "Group Areas Act",
        ], scale=0.86, box=0)
        # --- Band 6: Shops, services and fun
        self.next_band(6)
        self.write_rows(6, "Shops, services and fun", [
            "Local to city-wide",
        ], scale=0.86, box=0)
        self.wait(4)
