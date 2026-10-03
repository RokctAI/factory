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

# Band-layout whiteboard scene for map-of-southern-africa-1913-and-1860 (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/250/260/230/130/130/130 of 1400 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class MapOfSouthernAfricaSession(MovingCameraScene):
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
        # --- Band 0: Southern Africa, 1860
        self.write_rows(0, "Southern Africa, 1860", [
            "Cape Colony and Natal",
            "Orange Free State and Transvaal",
            "Zulu, Pedi, Swazi, Basotho",
            "Xhosa, Tswana, Venda, Griqua",
        ], scale=0.86, box=2)
        # --- Band 1: Southern Africa, 1913
        self.next_band(1)
        self.write_rows(1, "Southern Africa, 1913", [
            "Union: four provinces",
            "Basutoland, Bechuanaland",
            "Swaziland",
            "German South West Africa",
        ], scale=0.86, box=0)
        # --- Band 2: Explaining the change
        self.next_band(2)
        self.write_rows(2, "Explaining the change", [
            "Diamonds, 1867",
            "Conquest, 1879",
            "Gold, 1886",
            "Union, 1910",
        ], scale=0.86, box=1)
        # --- Band 3: Map skills
        self.next_band(3)
        self.write_rows(3, "Map skills", [
            "Title, date, key",
            "Same, changed, explained",
            "1913 - 1860 = 53 years",
            "Who drew the map?",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Many pieces
        self.next_band(4)
        self.write_rows(4, "Many pieces", [
            "Colonies, republics, kingdoms",
        ], scale=0.86, box=0)
        # --- Band 5: One big piece
        self.next_band(5)
        self.write_rows(5, "One big piece", [
            "The Union and its neighbours",
        ], scale=0.86, box=0)
        # --- Band 6: Why it changed
        self.next_band(6)
        self.write_rows(6, "Why it changed", [
            "Diamonds and gold",
        ], scale=0.86, box=0)
        self.wait(4)
