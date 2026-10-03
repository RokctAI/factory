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

# Band-layout whiteboard scene for defeat-of-germany-and-treaty-of-versailles (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (280/250/260/280/130/130/130 of 1460 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class DefeatOfGermanyTreatyOfVersaillesSession(MovingCameraScene):
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
        # --- Band 0: Defeat in 1918
        self.write_rows(0, "Defeat in 1918", [
            "Spring Offensive fails",
            "Amiens, 8 August",
            "Americans and the blockade",
            "Armistice, 11 November",
        ], scale=0.86, box=3)
        # --- Band 1: The Big Three
        self.next_band(1)
        self.write_rows(1, "The Big Three", [
            "Clemenceau: security",
            "Lloyd George: in between",
            "Wilson: Fourteen Points",
            "Botha and Smuts attend",
        ], scale=0.86, box=2)
        # --- Band 2: The terms
        self.next_band(2)
        self.write_rows(2, "The terms", [
            "Article 231: war guilt",
            "Reparations: 132 billion marks",
            "Army: 100 000 men",
            "Land, colonies, the League",
        ], scale=0.86, box=1)
        # --- Band 3: Dates and debate
        self.next_band(3)
        self.write_rows(3, "Dates and debate", [
            "1919 - 1914 = 5 years",
            "Armistice to treaty: 229 days",
            "A Diktat to Germans",
            "Too harsh or too weak?",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: How Germany lost
        self.next_band(4)
        self.write_rows(4, "How Germany lost", [
            "11 November 1918",
        ], scale=0.86, box=0)
        # --- Band 5: Making the peace
        self.next_band(5)
        self.write_rows(5, "Making the peace", [
            "The Big Three",
        ], scale=0.86, box=0)
        # --- Band 6: The treaty
        self.next_band(6)
        self.write_rows(6, "The treaty", [
            "Blame, pay, disarm",
        ], scale=0.86, box=0)
        self.wait(4)
