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

# Band-layout whiteboard scene for john-brown-and-the-end-of-slavery (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/200/210/240/90/90/120 of 1140 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class JohnBrownAndTheEndOfSlaverySession(MovingCameraScene):
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
        # --- Band 0: The Abolition Movement
        self.write_rows(0, "The Abolition Movement", [
            "Abolition: ending by law",
            "Britain: trade 1807, slavery 1834",
            "Garrison, Douglass, Sojourner Truth",
            "Newspapers, petitions, Uncle Tom's Cabin, 1852",
        ], scale=0.8, box=1)
        # --- Band 1: Who Was John Brown?
        self.next_band(1)
        self.write_rows(1, "Who Was John Brown?", [
            "Born 1800; deeply religious; opposed slavery",
            "Lived among free Black farmers",
            "Bleeding Kansas: Pottawatomie killings, 1856",
            "Plan: armed uprising from the mountains",
        ], scale=0.86, box=1)
        # --- Band 2: The Raid on Harpers Ferry, 1859
        self.next_band(2)
        self.write_rows(2, "The Raid on Harpers Ferry, 1859", [
            "16 October 1859: 21 raiders",
            "Armoury seized; few enslaved people join",
            "Marines under Robert E. Lee storm the engine house",
            "Tried for treason; hanged 2 December 1859",
        ], scale=0.8, box=2)
        # --- Band 3: Perspectives and the Road to Freedom
        self.next_band(3)
        self.write_rows(3, "Perspectives and the Road to Freedom", [
            "South: terrorist; many in the North: martyr",
            "Civil War, 1861 to 1865",
            "Emancipation Proclamation, 1863",
            "13th Amendment, 1865: about 4 million freed",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Ending Slavery
        self.next_band(4)
        self.write_rows(4, "Ending Slavery", [
            "Abolition: end it by law",
            "Britain: 1807 and 1834",
            "Douglass, Truth, Garrison",
        ], scale=0.86, box=0)
        # --- Band 5: John Brown's Raid
        self.next_band(5)
        self.write_rows(5, "John Brown's Raid", [
            "Slavery is a sin",
            "Harpers Ferry, October 1859",
            "Captured and hanged",
        ], scale=0.86, box=0)
        # --- Band 6: Hero or Villain?
        self.next_band(6)
        self.write_rows(6, "Hero or Villain?", [
            "Terrorist or martyr?",
            "Civil War 1861 to 1865",
            "1865: slavery abolished",
        ], scale=0.86, box=0)
        self.wait(4)
