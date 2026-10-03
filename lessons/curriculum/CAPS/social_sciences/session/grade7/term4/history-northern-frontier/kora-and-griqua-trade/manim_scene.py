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

# Band-layout whiteboard scene for kora-and-griqua-trade (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (140/180/180/200/90/90/90 of 970 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class KoraAndGriquaTradeSession(MovingCameraScene):
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
        # --- Band 0: Who Were the Kora?
        self.write_rows(0, "Who Were the Kora?", [
            "Kora: Khoikhoi who moved north",
            "Lived on the Orange and Vaal rivers",
            "Herders in independent clans",
            "Horses and guns gave them power",
        ], scale=0.86, box=1)
        # --- Band 1: Who Were the Griqua?
        self.next_band(1)
        self.write_rows(1, "Who Were the Griqua?", [
            "Griqua: people of mixed descent",
            "Dutch-speaking, Christian, horses and guns",
            "Leaders: Adam Kok, Barend Barends, Waterboer",
            "Klaarwater renamed Griquatown, 1813",
        ], scale=0.86, box=4)
        # --- Band 2: Trade with the Cape
        self.next_band(2)
        self.write_rows(2, "Trade with the Cape", [
            "From the Cape: guns, cloth, beads, tobacco",
            "Pack oxen, horses and wagons",
            "To the Cape: ivory, cattle, skins, feathers",
            "Middlemen between colony and interior",
        ], scale=0.86, box=3)
        # --- Band 3: Effects of the Northern Frontier Trade
        self.next_band(3)
        self.write_rows(3, "Effects of the Northern Frontier Trade", [
            "Griqua captaincies with laws and coins",
            "1823: Griqua horsemen at Dithakong",
            "Guns and horses spread inland",
            "1871: Britain annexes Griqualand West",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The Kora
        self.next_band(4)
        self.write_rows(4, "The Kora", [
            "Khoikhoi who moved north",
            "Orange and Vaal rivers",
            "Horses and guns",
        ], scale=0.86, box=0)
        # --- Band 5: The Griqua
        self.next_band(5)
        self.write_rows(5, "The Griqua", [
            "Mixed descent; moved north",
            "Dutch-speaking Christians",
            "Griquatown, 1813",
        ], scale=0.86, box=0)
        # --- Band 6: Trading Between Two Worlds
        self.next_band(6)
        self.write_rows(6, "Trading Between Two Worlds", [
            "Cape goods into the interior",
            "Ivory and skins to the Cape",
            "1823: Dithakong",
        ], scale=0.86, box=0)
        self.wait(4)
