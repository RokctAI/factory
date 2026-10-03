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

# Band-layout whiteboard scene for british-arrival-and-expanding-frontiers (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/160/180/190/90/90/90 of 990 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class BritishArrivalAndExpandingFrontiersSession(MovingCameraScene):
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
        # --- Band 0: Why the British Came
        self.write_rows(0, "Why the British Came", [
            "VOC bankrupt; dissolved 1799",
            "Britain protects the sea route to India",
            "1795: First British Occupation",
            "1806: Battle of Blaauwberg; 1814 ceded",
        ], scale=0.86, box=1)
        # --- Band 1: The Cape Under British Rule
        self.next_band(1)
        self.write_rows(1, "The Cape Under British Rule", [
            "English official: government 1822, courts 1828",
            "Circuit courts from 1811",
            "Governors such as Lord Charles Somerset",
            "Wine, then wool exports",
        ], scale=0.8, box=2)
        # --- Band 2: Laws Affecting Khoikhoi and Slaves
        self.next_band(2)
        self.write_rows(2, "Laws Affecting Khoikhoi and Slaves", [
            "1809 Caledon Code: passes for Khoikhoi",
            "1812: children apprenticed to farmers",
            "1828 Ordinance 50: freedom of movement",
            "1829: Kat River Settlement",
        ], scale=0.86, box=3)
        # --- Band 3: Expanding Frontiers
        self.next_band(3)
        self.write_rows(3, "Expanding Frontiers", [
            "1812: Xhosa expelled from the Zuurveld",
            "Grahamstown founded as military base",
            "Northern frontier: Kora, Griqua, Tswana",
            "Frontier: co-operation and conflict",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The British Arrive
        self.next_band(4)
        self.write_rows(4, "The British Arrive", [
            "1795: British take the Cape",
            "1803: back to the Dutch",
            "1806: Blaauwberg; British for good",
        ], scale=0.86, box=0)
        # --- Band 5: New Rules
        self.next_band(5)
        self.write_rows(5, "New Rules", [
            "English and British money",
            "1809: passes for Khoikhoi",
            "1828: Ordinance 50 frees movement",
        ], scale=0.86, box=0)
        # --- Band 6: Moving Frontiers
        self.next_band(6)
        self.write_rows(6, "Moving Frontiers", [
            "East: Zuurveld, Grahamstown, 1820 settlers",
            "North: Kora, Griqua, Tswana",
            "Trade and conflict",
        ], scale=0.86, box=0)
        self.wait(4)
