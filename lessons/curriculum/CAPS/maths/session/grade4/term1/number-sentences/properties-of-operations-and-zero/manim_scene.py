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

# Band-layout whiteboard scene for properties-of-operations-and-zero (Part 1 Expert
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


class PropertiesOfOperationsAndZeroSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Commutative Property
        self.write_rows(0, "The Commutative Property", [
            "Commutative: swap the order",
            "4 times 3 equals 3 times 4",
            "Add from the bigger number",
            "Subtraction and division do not swap",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): The Associative Property
        self.next_band(1)
        self.write_rows(1, "The Associative Property", [
            "Associative: change the grouping",
            "Make a ten first: 8 plus 2",
            "2 times 5 first gives 10",
            "17 plus 3 and 25 plus 5: 50",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): The Distributive Property and Zero
        self.next_band(2)
        self.write_rows(2, "The Distributive Property and Zero", [
            "Distributive: split, multiply, add",
            "5 times 23 is 100 plus 15",
            "6 times 19 is 120 minus 6",
            "Adding zero changes nothing",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``457 minus 268 equals 268 minus 457''",
            "``Regrouping changes the answer''",
            "``5 times 23 is 5 times 20 plus 3''",
            "``348 times 0 is 348''",
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
            "4 times 3 is 3 times 4",
            "Start from the bigger number",
            "Never swap minus or divide",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Group It Differently
        self.next_band(5)
        self.write_rows(5, "Group It Differently", [
            "Choose which two to do first",
            "8 plus 2 makes 10",
            "2 times 5 makes 10",
            "Pairs that make tens",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Split It and Add Nothing
        self.next_band(6)
        self.write_rows(6, "Split It and Add Nothing", [
            "Split 23 into 20 and 3",
            "100 plus 15 is 115",
            "6 times 20 minus 6 is 114",
            "348 plus 0 is 348",
        ], scale=0.9, box=1)

        last = Tex("Swap and regroup for plus and times, split to multiply, and zero adds nothing.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
