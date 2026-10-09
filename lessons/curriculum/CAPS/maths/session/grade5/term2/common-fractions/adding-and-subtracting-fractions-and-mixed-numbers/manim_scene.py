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

# Band-layout whiteboard scene for adding-and-subtracting-fractions-and-mixed-numbers (Part 1 Expert
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


class AddingAndSubtractingFractionsAndMixedNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Adding Fractions with the Same Bottom Number
        self.write_rows(0, "Adding Fractions with the Same Bottom Number", [
            "Same bottom: same-size pieces",
            "Add the tops, keep the bottom",
            "3/8 + 2/8 = 5/8",
            "3/4 + 3/4 = 6/4 = 1 and 2/4",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Subtracting Fractions with the Same Bottom Number
        self.next_band(1)
        self.write_rows(1, "Subtracting Fractions with the Same Bottom Number", [
            "Take away the tops, keep the bottom",
            "7/8 minus 3/8 is 4/8",
            "The whole pizza is 12/12",
            "12/12 minus 5/12 is 7/12",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Adding and Subtracting Mixed Numbers
        self.next_band(2)
        self.write_rows(2, "Adding and Subtracting Mixed Numbers", [
            "Add wholes, then add fractions",
            "2 and 3/8 + 1 and 2/8 = 3 and 5/8",
            "3 and 5/4 is 4 and 1/4",
            "Break a whole: 3 and 1/4 is 2 and 5/4",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3/8 + 2/8 = 5/16''",
            "``1 minus 5/12 is 4/12''",
            "``3 and 1/4 minus 1 and 3/4 is 2 and 2/4''",
            "``Leave the answer as 3 and 5/4''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Count the Same Pieces
        self.next_band(4)
        self.write_rows(4, "Count the Same Pieces", [
            "Count the pieces",
            "Add the tops",
            "Keep the bottom",
            "6/4 is 1 and 2/4",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Take Some Pieces Away
        self.next_band(5)
        self.write_rows(5, "Take Some Pieces Away", [
            "Take pieces away",
            "7/8 minus 3/8 is 4/8",
            "A whole pizza is 12/12",
            "7/12 is left",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Wholes and Pieces Together
        self.next_band(6)
        self.write_rows(6, "Wholes and Pieces Together", [
            "Wholes with wholes",
            "Pieces with pieces",
            "5/4 is 1 and 1/4",
            "Too few pieces? Break a whole",
        ], scale=0.9, box=3)

        last = Tex("Same bottom: add or take away the tops, keep the bottom, and swap between wholes and pieces when you need to.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
