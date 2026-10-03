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

# Band-layout whiteboard scene for scientific-developments-disease-sanitation-and-food (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/180/170/160/90/90/90 of 940 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ScientificDevelopmentsDiseaseSanitationAndFoodSession(MovingCameraScene):
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
        # --- Band 0: Controlling Disease and Infection
        self.write_rows(0, "Controlling Disease and Infection", [
            "1796 Jenner: smallpox vaccine",
            "1860s Pasteur: germ theory",
            "1867 Lister: antiseptics",
            "1928 Fleming: penicillin",
        ], scale=0.86, box=1)
        # --- Band 1: Improved Sanitation and Clean Water
        self.next_band(1)
        self.write_rows(1, "Improved Sanitation and Clean Water", [
            "Sanitation: safe waste disposal, clean water",
            "1854 John Snow: cholera from a pump",
            "1858 Great Stink: London builds sewers",
            "Clean water cut cholera and typhoid",
        ], scale=0.86, box=2)
        # --- Band 2: Canned Food and Refrigeration
        self.next_band(2)
        self.write_rows(2, "Canned Food and Refrigeration", [
            "Traditional: drying, salting, smoking",
            "1810 Appert: sealed and heated jars",
            "Cold slows bacteria; refrigerated ships",
            "Better food, fewer illnesses",
        ], scale=0.86, box=3)
        # --- Band 3: The Combined Effect on Population
        self.next_band(3)
        self.write_rows(3, "The Combined Effect on Population", [
            "Death rates fell, births stayed high",
            "After 1945: rapid spread worldwide",
            "Life expectancy: about 32 in 1900, 73 now",
            "New challenge: antibiotic resistance",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Fighting Germs
        self.next_band(4)
        self.write_rows(4, "Fighting Germs", [
            "Jenner: first vaccine",
            "Pasteur: germs cause disease",
            "Fleming: penicillin",
        ], scale=0.86, box=0)
        # --- Band 5: Clean Water and Toilets
        self.next_band(5)
        self.write_rows(5, "Clean Water and Toilets", [
            "Sewage in water spreads cholera",
            "John Snow's map and the pump",
            "Sewers and clean water save lives",
        ], scale=0.86, box=0)
        # --- Band 6: Keeping Food Safe
        self.next_band(6)
        self.write_rows(6, "Keeping Food Safe", [
            "1810: canned food",
            "Fridges slow germs",
            "Better food, fewer deaths",
        ], scale=0.86, box=0)
        self.wait(4)
