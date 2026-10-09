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

# Band-layout whiteboard scene for dividing-three-digit-by-two-digit-numbers (Part 1 Expert
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


class DividingThreeDigitByTwoDigitNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Dividing by Tens and by One Digit
        self.write_rows(0, "Dividing by Tens and by One Digit", [
            "Use multiplication facts",
            "480 divided by 60 is 8",
            "864 divided by 4 is 200 + 16",
            "840 divided by 20 is 42",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Dividing by Taking Away Chunks
        self.next_band(1)
        self.write_rows(1, "Dividing by Taking Away Chunks", [
            "864 divided by 24",
            "Take away 30 times 24: 720, 144 left",
            "Take away 6 times 24: 144, 0 left",
            "30 + 6 = 36 boxes",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Building a Table and Checking
        self.next_band(2)
        self.write_rows(2, "Building a Table and Checking", [
            "Table of 24: 24, 48, 120, 240, 480",
            "Check: 36 times 24 is 864",
            "500 divided by 32: 15 remainder 20",
            "The remainder is smaller than 32",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``24 divided by 864''",
            "``The answer is 144''",
            "``900 divided by 24 is 36 remainder 36''",
            "``No check needed''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Use Your Times Tables
        self.next_band(4)
        self.write_rows(4, "Use Your Times Tables", [
            "Times facts work backwards",
            "480 divided by 6 is 80",
            "Bigger groups, fewer groups",
            "720 divided by 24 is 30",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Big Bites
        self.next_band(5)
        self.write_rows(5, "Big Bites", [
            "Big bite: 30 boxes use 720",
            "Small bite: 6 boxes use 144",
            "Add the bites: 36",
            "Nothing left over",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Count, Check, Remainder
        self.next_band(6)
        self.write_rows(6, "Count, Check, Remainder", [
            "Multiply back to check",
            "36 times 24 is 864",
            "The remainder must be smaller",
            "900 divided by 24: 37 remainder 12",
        ], scale=0.9, box=1)

        last = Tex("Use your tables, take big chunks, add up the groups, keep the remainder small, and multiply back to check.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
