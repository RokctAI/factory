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

# Band-layout whiteboard scene for mali-at-its-height-under-mansa-musa (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/160/150/210/90/90/90 of 970 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class MaliAtItsHeightUnderMansaMusaSession(MovingCameraScene):
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
        # --- Band 0: Sundiata and the Founding of Mali
        self.write_rows(0, "Sundiata and the Founding of Mali", [
            "Mali grew on the upper Niger",
            "Sundiata defeats Sumanguru, about 1235",
            "Epic of Sundiata: told by griots",
            "Mansa: king or emperor",
        ], scale=0.86, box=1)
        # --- Band 1: The Size and Wealth of the Empire
        self.next_band(1)
        self.write_rows(1, "The Size and Wealth of the Empire", [
            "About 2000 km, Atlantic to the Niger bend",
            "Walata, Djenne, Timbuktu, Gao",
            "Gold, trade taxes, farming, tribute",
            "The mansa kept all the nuggets",
        ], scale=0.86, box=2)
        # --- Band 2: Governing a Great Empire
        self.next_band(2)
        self.write_rows(2, "Governing a Great Empire", [
            "Mansa: ruler, judge, commander",
            "Provinces and loyal local kings",
            "Cavalry and safe roads",
            "Scholars as advisers and judges",
        ], scale=0.86, box=1)
        # --- Band 3: Mansa Musa's Golden Age
        self.next_band(3)
        self.write_rows(3, "Mansa Musa's Golden Age", [
            "Mansa Musa: about 1312 to 1337",
            "Gao and Timbuktu brought into Mali",
            "Catalan Atlas, about 1375",
            "Later overtaken by Songhay",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Sundiata, the Lion King
        self.next_band(4)
        self.write_rows(4, "Sundiata, the Lion King", [
            "Sundiata, the first mansa",
            "Battle of Kirina, about 1235",
            "Story kept by the griots",
        ], scale=0.86, box=0)
        # --- Band 5: Big, Rich and Well Run
        self.next_band(5)
        self.write_rows(5, "Big, Rich and Well Run", [
            "About 2000 km wide",
            "Gold, taxes, farming, tribute",
            "Safe roads, loyal local kings",
        ], scale=0.86, box=0)
        # --- Band 6: Mansa Musa
        self.next_band(6)
        self.write_rows(6, "Mansa Musa", [
            "Mansa Musa, about 1312 to 1337",
            "Gao and Timbuktu joined Mali",
            "On a European map with a gold nugget",
        ], scale=0.86, box=0)
        self.wait(4)
