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

# Band-layout whiteboard scene for defeat-of-the-xhosa-pedi-and-zulu-kingdoms (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (260/250/240/220/150/150/150 of 1420 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class DefeatOfTheXhosaPediAndZuluKingdomsSession(MovingCameraScene):
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
        # --- Band 0: Diamonds and confederation
        self.write_rows(0, "Diamonds and confederation", [
            "Britain wants control of the region",
            "Frere sent in 1877",
            "Kingdoms seen as obstacles",
            "Land, labour, guns, security",
        ], scale=0.86, box=0)
        # --- Band 1: Xhosa and Pedi
        self.next_band(1)
        self.write_rows(1, "Xhosa and Pedi", [
            "Ninth Frontier War, 1877 to 1878",
            "Sandile killed, Sarhili in hiding",
            "Pedi under Sekhukhune",
            "Defeated at Tsate, 1879",
        ], scale=0.86, box=3)
        # --- Band 2: Anglo-Zulu War, 1879
        self.next_band(2)
        self.write_rows(2, "Anglo-Zulu War, 1879", [
            "Ultimatum: disband in 30 days",
            "Isandlwana, 22 January: Zulu victory",
            "Ulundi, 4 July: Zulu defeat",
            "Cetshwayo exiled; 13 chiefdoms",
        ], scale=0.86, box=1)
        # --- Band 3: Results
        self.next_band(3)
        self.write_rows(3, "Results", [
            "1 700 -- 1 300 = 400 survived",
            "Land lost, hut taxes",
            "Gun War: Sotho resist",
            "Link to mines and labour",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Why Britain wanted control
        self.next_band(4)
        self.write_rows(4, "Why Britain wanted control", [
            "Land, labour, control",
        ], scale=0.86, box=0)
        # --- Band 5: Two kingdoms fall
        self.next_band(5)
        self.write_rows(5, "Two kingdoms fall", [
            "Xhosa 1878, Pedi 1879",
        ], scale=0.86, box=0)
        # --- Band 6: Isandlwana and Ulundi
        self.next_band(6)
        self.write_rows(6, "Isandlwana and Ulundi", [
            "A great victory, a lost war",
        ], scale=0.86, box=0)
        self.wait(4)
