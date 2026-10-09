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

# Band-layout whiteboard scene for revision-of-numbers-operations-and-patterns (Part 1 Expert
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


class RevisionOfNumbersOperationsAndPatternsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Whole Numbers: Place Value, Ordering and Rounding
        self.write_rows(0, "Whole Numbers: Place Value, Ordering and Rounding", [
            "4 736 = 4 000 + 700 + 30 + 6",
            "3 095, 3 509, 3 950",
            "4 736: 4 740, 4 700, 5 000",
            "Count in 25s: 1 250, 1 275, 1 300",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): The Four Operations and Their Checks
        self.next_band(1)
        self.write_rows(1, "The Four Operations and Their Checks", [
            "2 468 + 1 375 = 3 843",
            "24 times 13: 240 + 72 = 312",
            "156 divided by 6 = 26",
            "50 learners, 8 a table: 7 tables",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Number Sentences and Patterns
        self.next_band(2)
        self.write_rows(2, "Number Sentences and Patterns", [
            "Box + 375 = 1 000: box is 625",
            "6 times 23: 120 + 18 = 138",
            "5, 9, 13, 17, 21: add 4",
            "Squares: times 3, plus 1",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``4 736 to the nearest 100: 4 800''",
            "``2 468 + 1 375 = 3 733''",
            "``50 learners, 8 a table: 6 tables''",
            "``3, 6, 12, 24, then 27''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Place Value and Rounding
        self.next_band(4)
        self.write_rows(4, "Place Value and Rounding", [
            "4 000 + 700 + 30 + 6",
            "Biggest place first",
            "Look one place right",
            "4 736 is about 4 700",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Calculate and Check
        self.next_band(5)
        self.write_rows(5, "Calculate and Check", [
            "Estimate first",
            "Check add with take away",
            "Check divide with times",
            "Remainder: think about the story",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Spot the Rule
        self.next_band(6)
        self.write_rows(6, "Spot the Rule", [
            "Add the same each time",
            "Or multiply the same",
            "Times 3, plus 1",
            "Box: undo the sum",
        ], scale=0.9, box=2)

        last = Tex("Place value, estimate, calculate, check with the inverse, and find the rule.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
