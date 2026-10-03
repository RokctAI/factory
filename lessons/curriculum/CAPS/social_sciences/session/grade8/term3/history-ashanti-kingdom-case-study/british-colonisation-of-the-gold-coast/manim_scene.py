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

# Band-layout whiteboard scene for british-colonisation-of-the-gold-coast (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (280/250/280/220/130/130/130 of 1420 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class BritishColonisationGoldCoastSession(MovingCameraScene):
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
        # --- Band 0: From the coast to Kumasi
        self.write_rows(0, "From the coast to Kumasi", [
            "Danish forts, 1850",
            "Dutch forts, 1872",
            "Kumasi burned, 1874",
            "Gold Coast Colony, 1874",
        ], scale=0.86, box=2)
        # --- Band 1: The scramble and Prempeh
        self.next_band(1)
        self.write_rows(1, "The scramble and Prempeh", [
            "France and Germany close in",
            "Prempeh refuses, 1891",
            "Kumasi occupied, 1896",
            "Exile to the Seychelles",
        ], scale=0.86, box=3)
        # --- Band 2: The War of the Golden Stool
        self.next_band(2)
        self.write_rows(2, "The War of the Golden Stool", [
            "Hodgson's demand, 1900",
            "Yaa Asantewaa leads",
            "Siege of the Kumasi fort",
            "Colony from 1902",
        ], scale=0.86, box=1)
        # --- Band 3: Timeline and sources
        self.next_band(3)
        self.write_rows(3, "Timeline and sources", [
            "1902 - 1874 = 28 years",
            "British reports",
            "Asante oral traditions",
            "Rebellion or resistance?",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Kumasi burns
        self.next_band(4)
        self.write_rows(4, "Kumasi burns", [
            "1874",
        ], scale=0.86, box=0)
        # --- Band 5: A king taken away
        self.next_band(5)
        self.write_rows(5, "A king taken away", [
            "1896",
        ], scale=0.86, box=0)
        # --- Band 6: Yaa Asantewaa's war
        self.next_band(6)
        self.write_rows(6, "Yaa Asantewaa's war", [
            "1900",
        ], scale=0.86, box=0)
        self.wait(4)
