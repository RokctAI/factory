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

# Band-layout whiteboard scene for emmeline-pankhurst-and-votes-for-women (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/290/280/280/130/130/130 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class EmmelinePankhurstVotesForWomenSession(MovingCameraScene):
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
        # --- Band 0: Suffragists
        self.write_rows(0, "Suffragists", [
            "NUWSS, 1897",
            "Millicent Fawcett",
            "Petitions and marches",
            "Arguments for and against",
        ], scale=0.86, box=1)
        # --- Band 1: Suffragettes
        self.next_band(1)
        self.write_rows(1, "Suffragettes", [
            "WSPU, 1903",
            "Deeds, not words",
            "Hunger strikes",
            "Cat and Mouse Act, 1913",
        ], scale=0.86, box=2)
        # --- Band 2: War and the vote
        self.next_band(2)
        self.write_rows(2, "War and the vote", [
            "Militancy stopped, 1914",
            "War work and soldiers' votes",
            "Act of 1918: women over 30",
            "Nancy Astor, 1919",
        ], scale=0.86, box=2)
        # --- Band 3: Counting the gains
        self.next_band(3)
        self.write_rows(3, "Counting the gains", [
            "30 - 21 = 9 years apart",
            "1928 - 1918 = 10 years",
            "8.4 $\\div$ 21.4 = about 0.39",
            "SA: 1930 and 1994",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Asking nicely
        self.next_band(4)
        self.write_rows(4, "Asking nicely", [
            "Suffragists",
        ], scale=0.86, box=0)
        # --- Band 5: Deeds, not words
        self.next_band(5)
        self.write_rows(5, "Deeds, not words", [
            "Suffragettes",
        ], scale=0.86, box=0)
        # --- Band 6: Votes at last
        self.next_band(6)
        self.write_rows(6, "Votes at last", [
            "1918 and 1928",
        ], scale=0.86, box=0)
        self.wait(4)
