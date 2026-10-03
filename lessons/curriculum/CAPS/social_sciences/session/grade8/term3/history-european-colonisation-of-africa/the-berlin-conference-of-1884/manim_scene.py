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

# Band-layout whiteboard scene for the-berlin-conference-of-1884 (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/270/280/260/130/130/130 of 1440 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class BerlinConferenceSession(MovingCameraScene):
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
        # --- Band 0: Africa before 1884
        self.write_rows(0, "Africa before 1884", [
            "About 10 per cent European, 1870",
            "African states and kingdoms",
            "Industry and rivalry",
            "Egypt 1882, the Congo",
        ], scale=0.86, box=3)
        # --- Band 1: Who met in Berlin
        self.next_band(1)
        self.write_rows(1, "Who met in Berlin", [
            "15 Nov 1884 to 26 Feb 1885",
            "Called by Bismarck",
            "Fourteen countries",
            "No Africans invited",
        ], scale=0.86, box=3)
        # --- Band 2: What was decided
        self.next_band(2)
        self.write_rows(2, "What was decided", [
            "Free trade on the Congo",
            "Congo Free State: Leopold II",
            "Effective occupation",
            "Borders drawn later",
        ], scale=0.86, box=2)
        # --- Band 3: Source and speed
        self.next_band(3)
        self.write_rows(3, "Source and speed", [
            "90 - 10 = 80 points",
            "1914 - 1870 = 44 years",
            "Ethiopia and Liberia free",
            "Who wrote the General Act?",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Before Berlin
        self.next_band(4)
        self.write_rows(4, "Before Berlin", [
            "Africans rule most of Africa",
        ], scale=0.86, box=0)
        # --- Band 5: A meeting without Africans
        self.next_band(5)
        self.write_rows(5, "A meeting without Africans", [
            "The empty chair",
        ], scale=0.86, box=0)
        # --- Band 6: The rules of the scramble
        self.next_band(6)
        self.write_rows(6, "The rules of the scramble", [
            "Occupy to claim",
        ], scale=0.86, box=0)
        self.wait(4)
