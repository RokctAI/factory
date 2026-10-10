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

# Band-layout whiteboard scene for ordering-comparing-and-representing-numbers (Part 1 Expert
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


class OrderingComparingAndRepresentingNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Comparing Nine-Digit Numbers
        self.write_rows(0, "Comparing Nine-Digit Numbers", [
            "More digits: bigger number",
            "Same digits: compare from the left",
            "245 380 000 is greater than 245 308 000",
            "Ten thousands: 8 beats 0",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Ordering Big Numbers
        self.next_band(1)
        self.write_rows(1, "Ordering Big Numbers", [
            "Ascending: smallest first",
            "Line up units under units",
            "245 308 000",
            "245 380 000, then 254 038 000",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Representing Numbers on a Number Line
        self.next_band(2)
        self.write_rows(2, "Representing Numbers on a Number Line", [
            "Marks in steps of 100 000",
            "245 380 000: between 245 300 000 and 245 400 000",
            "Closer to 245 400 000",
            "245 980 000 + 100 000 = 246 080 000",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``99 999 999 is bigger: more nines''",
            "``Compare from the right''",
            "``245 380 000 is less than 245 308 000''",
            "``245 980 000 + 100 000 = 245 1 080 000''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Count the Digits First
        self.next_band(4)
        self.write_rows(4, "Count the Digits First", [
            "Count the digits first",
            "Then start on the left",
            "First difference decides",
            "8 ten thousands beat 0",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Smallest to Biggest
        self.next_band(5)
        self.write_rows(5, "Smallest to Biggest", [
            "Ascending goes up",
            "Descending comes down",
            "R245 308 000, R245 380 000",
            "R254 038 000 is biggest",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Find Its Spot
        self.next_band(6)
        self.write_rows(6, "Find Its Spot", [
            "Find the two marks",
            "245 300 000 and 245 400 000",
            "Closer to 245 400 000",
            "Past 9? Carry over",
        ], scale=0.9, box=1)

        last = Tex("Count the digits, compare from the left, stop at the first difference, and the open side of the sign faces the bigger number.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
