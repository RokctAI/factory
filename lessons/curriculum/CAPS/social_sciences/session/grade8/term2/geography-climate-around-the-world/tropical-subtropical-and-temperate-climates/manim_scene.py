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

# Band-layout whiteboard scene for tropical-subtropical-and-temperate-climates (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (200/260/280/240/150/150/150 of 1430 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TropicalSubtropicalAndTemperateClimatesSession(MovingCameraScene):
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
        # --- Band 0: Classifying climates
        self.write_rows(0, "Classifying climates", [
            "Köppen: temperature and rainfall",
            "How hot? How big a range?",
            "How much rain? When?",
            "Boundaries are gradual",
        ], scale=0.86, box=0)
        # --- Band 1: Tropical climates
        self.next_band(1)
        self.write_rows(1, "Tropical climates", [
            "Every month hot, above about 18 \\textdegree{}C",
            "Rainforest: wet all year, range 1 to 3 \\textdegree{}C",
            "Savanna: wet summer, dry winter",
            "Monsoon: a very wet season",
        ], scale=0.86, box=2)
        # --- Band 2: Subtropical and temperate
        self.next_band(2)
        self.write_rows(2, "Subtropical and temperate", [
            "Durban: about 24.5 \\textdegree{}C and 17 \\textdegree{}C",
            "Summer rain, mild winters",
            "London: about 19 \\textdegree{}C and 5 \\textdegree{}C",
            "Rain in every month",
        ], scale=0.86, box=1)
        # --- Band 3: Comparing climates
        self.next_band(3)
        self.write_rows(3, "Comparing climates", [
            "Kisangani range about 1 \\textdegree{}C",
            "Kano range about 9 \\textdegree{}C",
            "Durban 7.5 \\textdegree{}C; London 14 \\textdegree{}C",
            "Range grows with latitude",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Sorting climates
        self.next_band(4)
        self.write_rows(4, "Sorting climates", [
            "Four questions to sort a place",
        ], scale=0.86, box=0)
        # --- Band 5: The hot tropics
        self.next_band(5)
        self.write_rows(5, "The hot tropics", [
            "Wet every month in the rainforest",
            "Wet and dry in the savanna",
        ], scale=0.86, box=1)
        # --- Band 6: Subtropical and temperate
        self.next_band(6)
        self.write_rows(6, "Subtropical and temperate", [
            "Durban: hot and wet summers",
            "London: cool and drizzly",
        ], scale=0.86, box=1)
        self.wait(4)
