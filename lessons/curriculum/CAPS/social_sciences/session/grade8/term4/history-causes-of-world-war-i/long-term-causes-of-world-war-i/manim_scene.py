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

# Band-layout whiteboard scene for long-term-causes-of-world-war-i (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (260/260/320/250/130/130/130 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class LongTermCausesWorldWarOneSession(MovingCameraScene):
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
        # --- Band 0: Militarism
        self.write_rows(0, "Militarism", [
            "Conscript armies",
            "The Schlieffen Plan",
            "HMS Dreadnought, 1906",
            "The naval race",
        ], scale=0.86, box=3)
        # --- Band 1: Alliances
        self.next_band(1)
        self.write_rows(1, "Alliances", [
            "Triple Alliance, 1882",
            "Triple Entente, 1907",
            "Two armed camps",
            "Italy changed sides, 1915",
        ], scale=0.86, box=1)
        # --- Band 2: Imperialism and nationalism
        self.next_band(2)
        self.write_rows(2, "Imperialism and nationalism", [
            "Moroccan crises, 1905 and 1911",
            "A place in the sun",
            "Bosnia annexed, 1908",
            "The Balkan powder keg",
        ], scale=0.86, box=3)
        # --- Band 3: Counting the years
        self.next_band(3)
        self.write_rows(3, "Counting the years", [
            "1914 - 1871 = 43 years",
            "1907 - 1882 = 25 years",
            "1914 - 1906 = 8 years",
            "M, A, I, N work together",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Guns and ships
        self.next_band(4)
        self.write_rows(4, "Guns and ships", [
            "Big armies",
        ], scale=0.86, box=0)
        # --- Band 5: Two teams
        self.next_band(5)
        self.write_rows(5, "Two teams", [
            "Alliance and Entente",
        ], scale=0.86, box=0)
        # --- Band 6: Colonies and pride
        self.next_band(6)
        self.write_rows(6, "Colonies and pride", [
            "The powder keg",
        ], scale=0.86, box=0)
        self.wait(4)
