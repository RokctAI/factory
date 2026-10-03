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

# Band-layout whiteboard scene for manuscripts-project-and-world-heritage-site (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/150/170/220/90/90/90 of 970 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ManuscriptsProjectAndWorldHeritageSiteSession(MovingCameraScene):
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
        # --- Band 0: The Timbuktu Manuscripts
        self.write_rows(0, "The Timbuktu Manuscripts", [
            "Hundreds of thousands of handwritten books",
            "Arabic and Ajami, mostly 1500s to 1900s",
            "Kept by families for generations",
            "Africa writing its own history",
        ], scale=0.86, box=1)
        # --- Band 1: Threats to the Manuscripts
        self.next_band(1)
        self.write_rows(1, "Threats to the Manuscripts", [
            "Heat, dust, damp, termites",
            "Trunks, sacks and poor storage",
            "Sold abroad and lost",
            "2012 to 2013: conflict and fire",
        ], scale=0.86, box=3)
        # --- Band 2: South Africa and the Timbuktu Manuscripts Project
        self.next_band(2)
        self.write_rows(2, "South Africa and the Timbuktu Manuscripts Project", [
            "2001: President Mbeki visits Timbuktu",
            "African Renaissance and NEPAD",
            "Conservators trained in Pretoria",
            "New Ahmed Baba Institute building, 2009",
        ], scale=0.86, box=2)
        # --- Band 3: Saving the Manuscripts and World Heritage
        self.next_band(3)
        self.write_rows(3, "Saving the Manuscripts and World Heritage", [
            "Trunks smuggled to Bamako, 2012 to 2013",
            "UNESCO World Heritage Site since 1988",
            "Three mosques and the mausoleums",
            "Rebuilt by local masons by 2015",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Treasure in Chests
        self.next_band(4)
        self.write_rows(4, "Treasure in Chests", [
            "Hundreds of thousands of manuscripts",
            "Maths, stars, medicine, history",
            "Kept safe by families",
        ], scale=0.86, box=0)
        # --- Band 5: Danger and Help
        self.next_band(5)
        self.write_rows(5, "Danger and Help", [
            "Heat, dust, damp, termites",
            "2001: President Mbeki offers help",
            "New library opened 2009",
        ], scale=0.86, box=0)
        # --- Band 6: The Great Rescue
        self.next_band(6)
        self.write_rows(6, "The Great Rescue", [
            "Trunks on donkey carts and boats",
            "Most manuscripts saved",
            "World Heritage since 1988",
        ], scale=0.86, box=0)
        self.wait(4)
