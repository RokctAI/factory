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

# Band-layout whiteboard scene for delville-wood-and-the-mendi (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (280/270/270/250/130/130/130 of 1460 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class DelvilleWoodAndMendiSession(MovingCameraScene):
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
        # --- Band 0: South Africans in the war
        self.write_rows(0, "South Africans in the war", [
            "Brigade under Lukin",
            "Segregated forces",
            "SANLC: unarmed labour",
            "Cape Corps",
        ], scale=0.86, box=2)
        # --- Band 1: Delville Wood
        self.next_band(1)
        self.write_rows(1, "Delville Wood", [
            "15 to 20 July 1916",
            "Hold at all costs",
            "Fire from three sides",
            "Memorial, 1926",
        ], scale=0.86, box=1)
        # --- Band 2: The SS Mendi
        self.next_band(2)
        self.write_rows(2, "The SS Mendi", [
            "21 February 1917",
            "Struck by the Darro in fog",
            "Sank in about 20 minutes",
            "616 South Africans died",
        ], scale=0.86, box=3)
        # --- Band 3: Memory and numbers
        self.next_band(3)
        self.write_rows(3, "Memory and numbers", [
            "780 $\\div$ 3 150 = about 0.25",
            "607 + 9 = 616",
            "616 + 30 = 646",
            "Honoured after 1994",
        ], scale=0.86, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Delville Wood
        self.next_band(4)
        self.write_rows(4, "Delville Wood", [
            "Six days",
        ], scale=0.86, box=0)
        # --- Band 5: The Mendi
        self.next_band(5)
        self.write_rows(5, "The Mendi", [
            "21 February 1917",
        ], scale=0.86, box=0)
        # --- Band 6: Remembering
        self.next_band(6)
        self.write_rows(6, "Remembering", [
            "After 1994",
        ], scale=0.86, box=0)
        self.wait(4)
