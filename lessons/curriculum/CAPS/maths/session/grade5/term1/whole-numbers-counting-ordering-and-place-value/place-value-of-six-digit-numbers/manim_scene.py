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

# Band-layout whiteboard scene for place-value-of-six-digit-numbers (Part 1 Expert
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


class PlaceValueOfSixDigitNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Six Places and Their Values
        self.write_rows(0, "Six Places and Their Values", [
            "Units, tens, hundreds, thousands",
            "Ten thousands, hundred thousands",
            "Each place is ten times the place to its right",
            "The 3 in 136 482 is worth 30 000",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Expanded Notation and Building Numbers
        self.next_band(1)
        self.write_rows(1, "Expanded Notation and Building Numbers", [
            "136 482 in expanded notation",
            "100 000 + 30 000 + 6 000 + 400 + 80 + 2",
            "300 000 + 4 000 + 50 + 9 = 304 059",
            "R765 430 is 765 notes of R1 000 and R430",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Changing Digits and Digit Cards
        self.next_band(2)
        self.write_rows(2, "Changing Digits and Digit Cards", [
            "136 482 + 10 000 = 146 482",
            "Cards 4, 0, 7, 2, 9, 5: biggest 975 420",
            "Smallest six-digit number: 204 579",
            "765 430 to 795 430: add 30 000",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The 3 in 136 482 is worth 3''",
            "``300 000 + 4 000 + 50 + 9 = 34 059''",
            "``The smallest number is 024 579''",
            "``765 430 has only 5 thousands''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Every Digit Has a Seat
        self.next_band(4)
        self.write_rows(4, "Every Digit Has a Seat", [
            "Six seats from the right",
            "Each seat is ten times bigger",
            "6 in 136 482 is 6 000",
            "6 in 765 430 is 60 000",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Break It Up, Build It Back
        self.next_band(5)
        self.write_rows(5, "Break It Up, Build It Back", [
            "Break it up into places",
            "300 000 + 4 000 + 50 + 9 = 304 059",
            "Empty seats get zeros",
            "765 notes of R1 000 and R430 over",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Swap a Digit, Make a Number
        self.next_band(6)
        self.write_rows(6, "Swap a Digit, Make a Number", [
            "Add 10 000: 146 482",
            "Biggest: 975 420",
            "Smallest: 204 579",
            "Zero cannot go first",
        ], scale=0.9, box=2)

        last = Tex("Find the seat, give the digit its value, and keep zeros in the empty seats.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
