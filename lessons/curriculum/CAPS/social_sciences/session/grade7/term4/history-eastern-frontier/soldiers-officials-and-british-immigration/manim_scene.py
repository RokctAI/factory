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

# Band-layout whiteboard scene for soldiers-officials-and-british-immigration (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/180/190/210/90/90/90 of 1020 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SoldiersOfficialsAndBritishImmigrationSession(MovingCameraScene):
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
        # --- Band 0: Soldiers on the Frontier
        self.write_rows(0, "Soldiers on the Frontier", [
            "British regiments defend the frontier",
            "Grahamstown 1812; forts along the rivers",
            "Cape Regiment: Khoikhoi soldiers",
            "Burgher commandos called up in wars",
        ], scale=0.86, box=1)
        # --- Band 1: Officials and Frontier Policy
        self.next_band(1)
        self.write_rows(1, "Officials and Frontier Policy", [
            "Governor makes policy; magistrates run districts",
            "Separation: fixed border, Ceded Territory",
            "1836: treaty system with chiefs",
            "Annexation; Grey's policies from 1854",
        ], scale=0.8, box=3)
        # --- Band 2: The 1820 Settlers
        self.next_band(2)
        self.write_rows(2, "The 1820 Settlers", [
            "1820: about 4000 British settlers",
            "Unemployment and poverty in Britain",
            "Buffer on the frontier; 100 acres each",
            "Algoa Bay landing; Port Elizabeth",
        ], scale=0.86, box=4)
        # --- Band 3: Impact of the Settlers
        self.next_band(3)
        self.write_rows(3, "Impact of the Settlers", [
            "Traders: Grahamstown and Port Elizabeth grow",
            "Wool from merino sheep",
            "Press freedom won in 1829",
            "More pressure on Xhosa land",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Soldiers and Forts
        self.next_band(4)
        self.write_rows(4, "Soldiers and Forts", [
            "Soldiers and forts",
            "Grahamstown, 1812",
            "Khoikhoi soldiers in the Cape Regiment",
        ], scale=0.86, box=0)
        # --- Band 5: Officials
        self.next_band(5)
        self.write_rows(5, "Officials", [
            "Governor makes rules",
            "Magistrates run districts",
            "Policies kept changing",
        ], scale=0.86, box=0)
        # --- Band 6: The 1820 Settlers
        self.next_band(6)
        self.write_rows(6, "The 1820 Settlers", [
            "1820: about 4000 settlers",
            "Many became traders",
            "More pressure on Xhosa land",
        ], scale=0.86, box=0)
        self.wait(4)
