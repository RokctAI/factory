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

# Band-layout whiteboard scene for free-burghers-huguenots-and-expanding-frontiers (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/170/170/200/90/90/90 of 990 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class FreeBurghersHuguenotsAndExpandingFrontiersSession(MovingCameraScene):
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
        # --- Band 0: The First Free Burghers
        self.write_rows(0, "The First Free Burghers", [
            "Burgher: citizen",
            "1657: nine free burghers on the Liesbeek",
            "Aim: cheaper food, defence",
            "Had to sell to the VOC at fixed prices",
        ], scale=0.86, box=1)
        # --- Band 1: The French Huguenots
        self.next_band(1)
        self.write_rows(1, "The French Huguenots", [
            "Huguenots: French Protestants",
            "1685: Edict of Nantes revoked",
            "1688: about 200 arrive at the Cape",
            "Settled at Franschhoek and Drakenstein",
        ], scale=0.86, box=4)
        # --- Band 2: Wine, Wheat and the Western Cape Farms
        self.next_band(2)
        self.write_rows(2, "Wine, Wheat and the Western Cape Farms", [
            "1679: Stellenbosch founded",
            "Mediterranean climate: wheat and wine",
            "Cape Dutch homesteads built with slave labour",
            "1706: Adam Tas protests; governor recalled",
        ], scale=0.8, box=2)
        # --- Band 3: Expanding Frontiers
        self.next_band(3)
        self.write_rows(3, "Expanding Frontiers", [
            "Frontier: a zone where societies meet",
            "Loan farms pushed stock farmers inland",
            "1713 smallpox devastated the Khoikhoi",
            "1778: boundary at the Great Fish River",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Free Burghers
        self.next_band(4)
        self.write_rows(4, "Free Burghers", [
            "1657: nine free burghers",
            "Farms on Khoikhoi land",
            "Sold to the VOC at set prices",
        ], scale=0.86, box=0)
        # --- Band 5: The Huguenots
        self.next_band(5)
        self.write_rows(5, "The Huguenots", [
            "French Protestants",
            "1688: about 200 arrive",
            "Franschhoek: French Corner",
        ], scale=0.86, box=0)
        # --- Band 6: Farms and Frontiers
        self.next_band(6)
        self.write_rows(6, "Farms and Frontiers", [
            "1679: Stellenbosch",
            "Settlers moved inland",
            "1713 smallpox",
        ], scale=0.86, box=0)
        self.wait(4)
