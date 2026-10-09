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

# Band-layout whiteboard scene for properties-of-operations-zero-and-one (Part 1 Expert
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


class PropertiesOfOperationsZeroAndOneSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Swapping the Order
        self.write_rows(0, "Swapping the Order", [
            "Commutative: swap the order",
            "25 rows of 16 equals 16 rows of 25",
            "386 plus 7: start from the bigger number",
            "Minus and divide do not swap",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Changing the Grouping
        self.next_band(1)
        self.write_rows(1, "Changing the Grouping", [
            "Associative: change the grouping",
            "37 plus 63 first makes 100",
            "(4 times 25) times 7 is 700",
            "Minus and divide do not regroup",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Splitting to Multiply, 0 and 1
        self.next_band(2)
        self.write_rows(2, "Splitting to Multiply, 0 and 1", [
            "Distributive: split, multiply, add",
            "23 times 25 is 500 plus 75",
            "8 times 99 is 800 minus 8",
            "Plus 0 and times 1 change nothing",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``50 minus 20 equals 20 minus 50''",
            "``(50 minus 20) minus 10 is 40''",
            "``6 times 47 is 240 plus 7''",
            "``575 times 0 is 575''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Swap It Round
        self.next_band(4)
        self.write_rows(4, "Swap It Round", [
            "Swap plus and times freely",
            "25 times 16 is 16 times 25",
            "Start from the bigger number",
            "Never swap minus or divide",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Group It Your Way
        self.next_band(5)
        self.write_rows(5, "Group It Your Way", [
            "Group to make tens and hundreds",
            "37 plus 63 is 100",
            "4 times 25 is 100",
            "Then 100 times 7 is 700",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Split It, and Two Special Numbers
        self.next_band(6)
        self.write_rows(6, "Split It, and Two Special Numbers", [
            "Split, multiply each part, add",
            "23 times 25 is 500 plus 75",
            "Plus 0: no change",
            "Times 1: no change",
        ], scale=0.9, box=1)

        last = Tex("Swap and group for plus and times, split to multiply, and remember that plus 0 and times 1 change nothing.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
