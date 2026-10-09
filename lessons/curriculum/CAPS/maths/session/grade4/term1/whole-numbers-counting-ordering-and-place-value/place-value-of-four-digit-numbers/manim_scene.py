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

# Band-layout whiteboard scene for place-value-of-four-digit-numbers (Part 1 Expert
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


class PlaceValueOfFourDigitNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Thousands, Hundreds, Tens and Units
        self.write_rows(0, "Thousands, Hundreds, Tens and Units", [
            "Units, tens, hundreds, thousands",
            "Each place is ten of the one to its right",
            "4 736: the 7 is worth 700",
            "Digits count the boxes",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Face Value, Place Value and Expanded Notation
        self.next_band(1)
        self.write_rows(1, "Face Value, Place Value and Expanded Notation", [
            "Face value: the digit itself",
            "Place value: what it is worth there",
            "4 736 is 4 000 plus 700 plus 30 plus 6",
            "7 times 100 is 700",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): The Job of Zero
        self.next_band(2)
        self.write_rows(2, "The Job of Zero", [
            "Zero holds a place open",
            "2 305 has no tens",
            "Without the 0, 2 305 would read 235",
            "Read only the filled places",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The 7 in 4 736 is worth 7''",
            "``Five thousand and eight is 508''",
            "``2 305 is the same as 235''",
            "``4 736 is two numbers''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Four Places
        self.next_band(4)
        self.write_rows(4, "Four Places", [
            "Units, tens, hundreds, thousands",
            "Read the places from the right",
            "Ten of one place make the next",
            "Four piles of R1 000 is 4 000",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): What Is the Digit Worth
        self.next_band(5)
        self.write_rows(5, "What Is the Digit Worth", [
            "Face value: the digit",
            "Place value: where it stands",
            "4 000 plus 700 plus 30 plus 6",
            "Change the hundreds, change by 100s",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Zero Keeps the Place
        self.next_band(6)
        self.write_rows(6, "Zero Keeps the Place", [
            "Zero holds the place open",
            "2 305: no tens",
            "Say only the filled places",
            "2 000: three zeros hold the places",
        ], scale=0.9, box=0)

        last = Tex("Face value is the digit, place value is where it stands, and zero holds the place.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
