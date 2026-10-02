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

# Band-layout whiteboard scene for diamond-monopoly-and-black-claim-owners (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (280/290/240/230/150/150/150 of 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class DiamondMonopolyAndBlackClaimOwnersSession(MovingCameraScene):
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
        # --- Band 0: Digging the mine
        self.write_rows(0, "Digging the mine", [
            "Claims about 9.5 m on a side",
            "Cables like a spider's web",
            "Yellow ground, then blue ground",
            "Reef falls and flooding",
        ], scale=0.86, box=3)
        # --- Band 1: Black claim owners pushed out
        self.next_band(1)
        self.write_rows(1, "Black claim owners pushed out", [
            "Some black and coloured claim owners",
            "Accused of IDB; 1872 riots",
            "Licences and character certificates",
            "Black Flag Rebellion 1875",
        ], scale=0.86, box=2)
        # --- Band 2: Passes and compounds
        self.next_band(2)
        self.write_rows(2, "Passes and compounds", [
            "Migrant workers from far away",
            "Passes from 1872",
            "Closed compounds from 1885",
            "Searched before release",
        ], scale=0.86, box=2)
        # --- Band 3: Towards monopoly
        self.next_band(3)
        self.write_rows(3, "Towards monopoly", [
            "Falling prices; depression",
            "Claim limits lifted 1876",
            "Companies from 1880; crash 1881",
            "De Beers Consolidated 1888",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Digging the hole
        self.next_band(4)
        self.write_rows(4, "Digging the hole", [
            "Hundreds of little squares",
            "Walls fall, water floods",
            "Small diggers sell out",
        ], scale=0.86, box=2)
        # --- Band 5: Pushed out
        self.next_band(5)
        self.write_rows(5, "Pushed out", [
            "Black owners at first",
            "Riots and refused licences",
            "Claims lost or sold",
        ], scale=0.86, box=2)
        # --- Band 6: Passes and compounds
        self.next_band(6)
        self.write_rows(6, "Passes and compounds", [
            "A pass to move",
            "Locked in for months",
            "One company in control",
        ], scale=0.86, box=2)
        self.wait(4)
