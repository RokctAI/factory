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

# Band-layout whiteboard scene for place-value-of-nine-digit-numbers (Part 1 Expert
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


class PlaceValueOfNineDigitNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Place Value to Hundred Millions
        self.write_rows(0, "Place Value to Hundred Millions", [
            "Nine places in three groups",
            "Millions, thousands, units",
            "62 027 503: the 6 is worth 60 000 000",
            "R125 000 000: the 2 is worth R20 000 000",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Expanded Notation
        self.next_band(1)
        self.write_rows(1, "Expanded Notation", [
            "Add the value of each digit",
            "149 600 000 = 100 000 000 + 40 000 000",
            "+ 9 000 000 + 600 000",
            "Zeros hold the seats: 305 040 009",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Reading and Writing Nine-Digit Numbers
        self.next_band(2)
        self.write_rows(2, "Reading and Writing Nine-Digit Numbers", [
            "Group in threes from the right",
            "62 027 503",
            "Sixty-two million, twenty-seven thousand,",
            "five hundred and three",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The 6 in 62 027 503 is worth 6''",
            "``300 million + 5 million + 40 000 + 9 = 354 009''",
            "``8 million, 6 thousand and 12 is 8 612''",
            "``Grouping from the left: 620 275 03''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Three Seats in Every Group
        self.next_band(4)
        self.write_rows(4, "Three Seats in Every Group", [
            "Groups of three",
            "62 027 503",
            "The 6 sits in ten millions",
            "It is worth 60 000 000",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Break It Up
        self.next_band(5)
        self.write_rows(5, "Break It Up", [
            "Break it up",
            "149 600 000",
            "100 000 000 + 40 000 000 + 9 000 000 + 600 000",
            "Empty seats get a 0",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Say It in Groups
        self.next_band(6)
        self.write_rows(6, "Say It in Groups", [
            "Say it in groups",
            "62 027 503",
            "Sixty-two million, twenty-seven thousand",
            "8 006 012",
        ], scale=0.9, box=2)

        last = Tex("Every digit has a seat, the seat sets its value, and zeros keep the other digits in their places.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
