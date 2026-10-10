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
        # --- Band 0 (subtopic_1): Adding Fractions with Related Denominators
        self.write_rows(0, "Adding Fractions with Related Denominators", [
            "Make the pieces match",
            "1/2 = 2/4",
            "2/4 + 1/4 = 3/4",
            "3/4 + 5/8 = 11/8 = 1 and 3/8",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Subtracting Fractions with Related Denominators
        self.next_band(1)
        self.write_rows(1, "Subtracting Fractions with Related Denominators", [
            "Match, then take away the tops",
            "5/6 minus 2/6 = 3/6 = 1/2",
            "7/8 minus 4/8 = 3/8",
            "1 whole = 12/12",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Adding and Subtracting Mixed Numbers
        self.next_band(2)
        self.write_rows(2, "Adding and Subtracting Mixed Numbers", [
            "Wholes with wholes, parts with parts",
            "2 and 1/4 + 1 and 3/8 = 3 and 5/8",
            "Break a whole: 3 and 2/4 = 2 and 6/4",
            "2 and 6/4 minus 1 and 3/4 = 1 and 3/4",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``1/2 + 1/4 = 2/6''",
            "``1/2 = 1/4''",
            "``Leave the answer as 11/8''",
            "``Take 2/4 from 3/4''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Match, Then Add
        self.next_band(4)
        self.write_rows(4, "Match, Then Add", [
            "Match, then add",
            "Halves into quarters",
            "3/4 of a cup",
            "11/8 is 1 and 3/8",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Match, Then Take Away
        self.next_band(5)
        self.write_rows(5, "Match, Then Take Away", [
            "Match, then take away",
            "Thirds into sixths",
            "1/2 a bottle left",
            "7/12 of the race to go",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Wholes and Parts
        self.next_band(6)
        self.write_rows(6, "Wholes and Parts", [
            "Wholes and parts",
            "3 and 5/8 km",
            "Break a whole",
            "1 and 3/4 km left",
        ], scale=0.9, box=2)

        last = Tex("Make the pieces the same size, add or take away the tops, keep the bottom, and handle wholes and parts separately.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
