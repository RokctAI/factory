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

# Band-layout whiteboard scene for enlargements-and-reductions (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/160/160/110/110/110 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EnlargementsAndReductionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.15).shift(band_shift(k) + UP * 2.4)
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
        self.wait(42)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Same Shape, New Size
        self.write_rows(0, "Same Shape, New Size", [
            "Enlarge: bigger, same shape",
            "Reduce: smaller, same shape",
            "3 by 2, twice as long: 6 by 4",
            "Angles stay the same",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Drawing on a Grid
        self.next_band(1)
        self.write_rows(1, "Drawing on a Grid", [
            "Base 4, height 3, times 3",
            "Base 12, height 9",
            "Half of 6 and 4: 3 and 2",
            "Copy onto a bigger grid",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Comparing Size and Shape
        self.next_band(2)
        self.write_rows(2, "Comparing Size and Shape", [
            "6 by 4: enlargement of 3 by 2",
            "6 by 3: stretched, not enlarged",
            "6 squares become 24 squares",
            "Double sides: 4 times inside",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3 by 2 plus 2 each side: 5 by 4''",
            "``3 by 2 to 6 by 2''",
            "``Enlarging makes angles bigger''",
            "``Double sides, double inside''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Bigger or Smaller, Same Shape
        self.next_band(4)
        self.write_rows(4, "Bigger or Smaller, Same Shape", [
            "Same shape",
            "Bigger or smaller",
            "Same multiplier",
            "Same angles",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Count and Multiply
        self.next_band(5)
        self.write_rows(5, "Count and Multiply", [
            "Count and multiply",
            "4 and 3",
            "times 3",
            "12 and 9",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Same Number for Every Side
        self.next_band(6)
        self.write_rows(6, "Same Number for Every Side", [
            "Same number for every side",
            "6 by 4: yes",
            "6 by 3: no",
            "Inside: 4 times",
        ], scale=0.9, box=1)

        last = Tex("In an enlargement or reduction, multiply every side by the same number: the angles stay the same.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
