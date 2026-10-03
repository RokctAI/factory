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

# Band-layout whiteboard scene for satyagraha-and-the-1913-land-act (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (310/240/230/250/130/130/130 of 1420 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SatyagrahaAndLandActSession(MovingCameraScene):
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
        # --- Band 0: The Natives Land Act, 1913
        self.write_rows(0, "The Natives Land Act, 1913", [
            "About 7 per cent of the land",
            "No buying or renting outside",
            "Sharecropping outlawed",
            "Mass evictions",
        ], scale=0.86, box=0)
        # --- Band 1: Satyagraha
        self.next_band(1)
        self.write_rows(1, "Satyagraha", [
            "Three-pound tax in Natal",
            "Searle judgment, 1913",
            "Truth-force: peaceful law-breaking",
            "Women lead the way",
        ], scale=0.86, box=2)
        # --- Band 2: The march and the Act
        self.next_band(2)
        self.write_rows(2, "The march and the Act", [
            "Coal miners strike, October 1913",
            "Volksrust, 6 November 1913",
            "Sugar workers strike",
            "Indian Relief Act, 1914",
        ], scale=0.86, box=3)
        # --- Band 3: Figures and sources
        self.next_band(3)
        self.write_rows(3, "Figures and sources", [
            "About 67 per cent African",
            "60 $\\div$ 20 = 3 months of wages",
            "Plaatje: Native Life, 1916",
            "Explain the purpose",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Pushed off the land
        self.next_band(4)
        self.write_rows(4, "Pushed off the land", [
            "Seven per cent",
        ], scale=0.86, box=0)
        # --- Band 5: Truth-force
        self.next_band(5)
        self.write_rows(5, "Truth-force", [
            "Break unfair laws peacefully",
        ], scale=0.86, box=0)
        # --- Band 6: What changed
        self.next_band(6)
        self.write_rows(6, "What changed", [
            "Tax ended, Land Act stayed",
        ], scale=0.86, box=0)
        self.wait(4)
