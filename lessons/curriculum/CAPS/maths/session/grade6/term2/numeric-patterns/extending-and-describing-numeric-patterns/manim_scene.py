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

# Band-layout whiteboard scene for extending-and-describing-numeric-patterns (Part 1 Expert
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


class ExtendingAndDescribingNumericPatternsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Patterns with a Constant Difference
        self.write_rows(0, "Patterns with a Constant Difference", [
            "Same gap each time",
            "7, 15, 23, 31: add 8",
            "Week 10: 7 + 9 times 8 = 79",
            "500, 475, 450: subtract 25",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Patterns with a Constant Ratio
        self.next_band(1)
        self.write_rows(1, "Patterns with a Constant Ratio", [
            "Times the same each time",
            "1, 3, 9, 27, 81: times 3",
            "3, 6, 12, 24, 48: double",
            "6 400, 3 200, 1 600: halve",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Patterns with a Changing Difference
        self.next_band(2)
        self.write_rows(2, "Patterns with a Changing Difference", [
            "The gaps make a pattern",
            "1, 3, 6, 10, 15",
            "Gaps 2, 3, 4, 5",
            "Next: 21, then 28",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``1, 3, 9, 27 adds 2''",
            "``1, 3, 6, 10, then 14''",
            "``Week 10 is 10 times 8 = 80''",
            "``The rule is: it goes up''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Add the Same Each Time
        self.next_band(4)
        self.write_rows(4, "Add the Same Each Time", [
            "Add the same each time",
            "Gaps of 8",
            "7, 15, 23, 31, 39",
            "Table: position and term",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Multiply the Same Each Time
        self.next_band(5)
        self.write_rows(5, "Multiply the Same Each Time", [
            "Multiply the same each time",
            "1, 3, 9, 27, 81",
            "Grows very fast",
            "Divide to check the ratio",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Watch the Gaps Grow
        self.next_band(6)
        self.write_rows(6, "Watch the Gaps Grow", [
            "Watch the gaps grow",
            "Gaps 2, 3, 4, 5, 6",
            "Next term 21",
            "1, 4, 9, 16, 25, 36",
        ], scale=0.9, box=1)

        last = Tex("Write the gaps: equal gaps mean add, equal multipliers mean multiply, and growing gaps have a pattern of their own.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
