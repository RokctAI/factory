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

# Band-layout whiteboard scene for adding-and-subtracting-six-digit-numbers (Part 1 Expert
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


class AddingAndSubtractingSixDigitNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Adding in Columns with Carrying
        self.write_rows(0, "Adding in Columns with Carrying", [
            "Units under units",
            "Start on the right",
            "10 or more: carry",
            "486 357 + 275 896 = 762 253",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Subtracting in Columns with Borrowing
        self.next_band(1)
        self.write_rows(1, "Subtracting in Columns with Borrowing", [
            "Top digit too small: borrow",
            "Zeros become 9",
            "604 020 minus 285 467 = 318 553",
            "Check: 318 553 + 285 467 = 604 020",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Adding and Subtracting Several Numbers
        self.next_band(2)
        self.write_rows(2, "Adding and Subtracting Several Numbers", [
            "Three numbers: line up the units",
            "You may carry 2",
            "125 408 + 67 395 + 209 087",
            "= 401 890",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``486 357 + 275 896 = 651 143''",
            "``604 020 minus 285 467 = 481 447''",
            "``Borrowing leaves the zero as 0''",
            "``67 395 lined up on the left''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Carry the Ten
        self.next_band(4)
        self.write_rows(4, "Carry the Ten", [
            "Carry the ten",
            "13: write 3, carry 1",
            "Start on the right",
            "762 253 visitors",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Borrow from Next Door
        self.next_band(5)
        self.write_rows(5, "Borrow from Next Door", [
            "Borrow from next door",
            "Zeros become 9",
            "318 553 kilolitres left",
            "Add back to check",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Line Them Up
        self.next_band(6)
        self.write_rows(6, "Line Them Up", [
            "Line up the units",
            "Add each column",
            "Carry 2 if you need to",
            "401 890 books",
        ], scale=0.9, box=0)

        last = Tex("Line up the units, work from the right, carry tens, borrow across zeros, and check by adding back.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
