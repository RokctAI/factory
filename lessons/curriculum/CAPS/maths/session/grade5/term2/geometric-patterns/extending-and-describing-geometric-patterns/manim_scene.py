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

# Band-layout whiteboard scene for extending-and-describing-geometric-patterns (Part 1 Expert
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


class ExtendingAndDescribingGeometricPatternsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Patterns That Grow by the Same Amount
        self.write_rows(0, "Patterns That Grow by the Same Amount", [
            "4, 7, 10, 13 matches",
            "Each new square adds 3",
            "Shape 10: 10 times 3, plus 1, is 31",
            "Shared sides are counted once",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Patterns That Grow Faster
        self.next_band(1)
        self.write_rows(1, "Patterns That Grow Faster", [
            "Triangles: 1, 3, 6, 10, 15",
            "Differences grow: 2, 3, 4, 5",
            "Squares: 1, 4, 9, 16, 25",
            "Doubling: 1, 2, 4, 8, 16",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Describing and Using Rules
        self.next_band(2)
        self.write_rows(2, "Describing and Using Rules", [
            "Next-shape rule: add 3",
            "Any-shape rule: times 3, plus 1",
            "Shape 20 has 61 matches",
            "Triangle 10 has 55 dots",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``1, 3, 6, 10, then 14''",
            "``Shape 10 has 40 matches''",
            "``Shape 20 is double shape 10: 62''",
            "``1, 4, 9, 16, then 20''",
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
            "Count the matches each time",
            "4, 7, 10, 13, 16",
            "Add 3 each time",
            "The first square needs 4",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Faster and Faster
        self.next_band(5)
        self.write_rows(5, "Faster and Faster", [
            "Some patterns grow faster",
            "Triangles: add 2, then 3, then 4",
            "Squares: 1, 4, 9, 16, 25",
            "Doubling: 1, 2, 4, 8, 16",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Say the Rule
        self.next_band(6)
        self.write_rows(6, "Say the Rule", [
            "Say the rule in your own words",
            "Times 3, plus 1",
            "Shape 7: 22 matches",
            "Shape 20: 61 matches",
        ], scale=0.9, box=1)

        last = Tex("Count, look at how the pattern grows, say the rule in your own words, and use the shape number to jump ahead.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
