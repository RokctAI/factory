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

# Band-layout whiteboard scene for plantations-and-the-triangular-trade (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/190/180/230/90/90/100 of 1040 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class PlantationsAndTheTriangularTradeSession(MovingCameraScene):
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
        # --- Band 0: The Plantation
        self.write_rows(0, "The Plantation", [
            "Plantation: a huge farm, one cash crop",
            "Big house, quarters, fields, mill",
            "Overseers and forced labour",
            "Brazil, Caribbean, the American South",
        ], scale=0.86, box=1)
        # --- Band 1: Four Crops: Tobacco, Rice, Sugar and Cotton
        self.next_band(1)
        self.write_rows(1, "Four Crops: Tobacco, Rice, Sugar and Cotton", [
            "Tobacco: Virginia, from the 1610s",
            "Rice: Carolina swamps; African skills",
            "Sugar: most profitable, most deadly",
            "Cotton: after the 1793 cotton gin",
        ], scale=0.86, box=1)
        # --- Band 2: Why Enslaved Labour?
        self.next_band(2)
        self.write_rows(2, "Why Enslaved Labour?", [
            "No wages: more profit",
            "Indigenous peoples died of new diseases",
            "Indentured servants were temporary",
            "Slave codes and racism justified it",
        ], scale=0.86, box=3)
        # --- Band 3: The Triangular Trade and Where the Wealth Went
        self.next_band(3)
        self.write_rows(3, "The Triangular Trade and Where the Wealth Went", [
            "Europe to Africa: cloth, guns, metal",
            "Africa to the Americas: the Middle Passage",
            "Americas to Europe: sugar, tobacco, cotton",
            "Profits for Europe; nothing for the enslaved",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Giant Farms
        self.next_band(4)
        self.write_rows(4, "Giant Farms", [
            "Big house and quarters",
            "Tobacco, rice, sugar, cotton",
            "Cotton gin, 1793",
        ], scale=0.86, box=0)
        # --- Band 5: Why Enslaved People?
        self.next_band(5)
        self.write_rows(5, "Why Enslaved People?", [
            "No wages: more profit",
            "Slave codes: no rights",
            "Racist lies to excuse it",
        ], scale=0.86, box=0)
        # --- Band 6: Follow the Sugar
        self.next_band(6)
        self.write_rows(6, "Follow the Sugar", [
            "Europe to Africa to the Americas to Europe",
            "Cotton fed English factories",
            "The enslaved got nothing",
        ], scale=0.86, box=0)
        self.wait(4)
