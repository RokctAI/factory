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

# Band-layout whiteboard scene for trench-warfare-music-and-poetry (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (250/300/290/250/130/130/130 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TrenchWarfareMusicPoetrySession(MovingCameraScene):
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
        # --- Band 0: Stalemate
        self.write_rows(0, "Stalemate", [
            "The Marne, 1914",
            "700 km of trenches",
            "Machine guns, wire, artillery",
            "Gas 1915, tanks 1916",
        ], scale=0.86, box=2)
        # --- Band 1: Life in the trenches
        self.next_band(1)
        self.write_rows(1, "Life in the trenches", [
            "Front, support, reserve",
            "No man's land",
            "Mud, rats, lice, trench foot",
            "Shell shock",
        ], scale=0.86, box=3)
        # --- Band 2: Songs and poems
        self.next_band(2)
        self.write_rows(2, "Songs and poems", [
            "Tipperary and Kit-Bag",
            "Brooke: The Soldier",
            "McCrae: the poppy",
            "Owen: the old lie",
        ], scale=0.86, box=3)
        # --- Band 3: The first day of the Somme
        self.next_band(3)
        self.write_rows(3, "The first day of the Somme", [
            "About 57 470 casualties",
            "About 19 240 killed",
            "19 240 $\\div$ 57 470 = about 0.33",
            "Who, when, why, audience",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Stuck in the trenches
        self.next_band(4)
        self.write_rows(4, "Stuck in the trenches", [
            "Stalemate",
        ], scale=0.86, box=0)
        # --- Band 5: Mud, rats and fear
        self.next_band(5)
        self.write_rows(5, "Mud, rats and fear", [
            "No man's land",
        ], scale=0.86, box=0)
        # --- Band 6: Songs and poems
        self.next_band(6)
        self.write_rows(6, "Songs and poems", [
            "Proud, then angry",
        ], scale=0.86, box=0)
        self.wait(4)
