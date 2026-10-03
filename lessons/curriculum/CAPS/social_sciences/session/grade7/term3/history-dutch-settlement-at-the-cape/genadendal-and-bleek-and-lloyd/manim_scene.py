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

# Band-layout whiteboard scene for genadendal-and-bleek-and-lloyd (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/180/210/90/90/90 of 1030 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class GenadendalAndBleekAndLloydSession(MovingCameraScene):
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
        # --- Band 0: Georg Schmidt and the First Mission
        self.write_rows(0, "Georg Schmidt and the First Mission", [
            "1738: Georg Schmidt, Moravian missionary",
            "Baviaanskloof: first school for Khoikhoi",
            "1744: Schmidt forced to leave",
            "1792: mission restarts; 1806 Genadendal",
        ], scale=0.86, box=1)
        # --- Band 1: Life and Significance of Genadendal
        self.next_band(1)
        self.write_rows(1, "Life and Significance of Genadendal", [
            "Grew to over 1000 by 1806",
            "Skills: carpentry, blacksmiths, cutlers",
            "1838: first teachers' training college",
            "Refuge from forced farm labour",
        ], scale=0.86, box=3)
        # --- Band 2: Bleek, Lloyd and the !Xam
        self.next_band(2)
        self.write_rows(2, "Bleek, Lloyd and the !Xam", [
            "Wilhelm Bleek: German linguist",
            "Lucy Lloyd: did much of the recording",
            "!Xam prisoners at the Breakwater",
            "1870s: stories written in notebooks",
        ], scale=0.86, box=3)
        # --- Band 3: The Bleek and Lloyd Archive
        self.next_band(3)
        self.write_rows(3, "The Bleek and Lloyd Archive", [
            "Over 12 000 pages of !Xam texts",
            "1997: UNESCO Memory of the World",
            "Helps explain San rock art",
            "Coat of arms motto in !Xam",
        ], scale=0.86, box=4)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The First Mission
        self.next_band(4)
        self.write_rows(4, "The First Mission", [
            "1738: Georg Schmidt",
            "First school for Khoikhoi",
            "1792: mission returns",
        ], scale=0.86, box=0)
        # --- Band 5: Valley of Grace
        self.next_band(5)
        self.write_rows(5, "Valley of Grace", [
            "1806: named Genadendal",
            "Refuge and trades",
            "1838: first teachers' college",
        ], scale=0.86, box=0)
        # --- Band 6: Saving the !Xam Stories
        self.next_band(6)
        self.write_rows(6, "Saving the !Xam Stories", [
            "Bleek and Lloyd, 1870s",
            "Thousands of pages of stories",
            "Motto in !Xam",
        ], scale=0.86, box=0)
        self.wait(4)
