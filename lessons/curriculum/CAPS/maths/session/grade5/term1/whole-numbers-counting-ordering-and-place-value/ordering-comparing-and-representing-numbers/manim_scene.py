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
        # --- Band 0 (subtopic_1): Reading and Writing Six-Digit Numbers
        self.write_rows(0, "Reading and Writing Six-Digit Numbers", [
            "Group in threes from the right",
            "245 318 is 245 thousand and 318",
            "407 052: no hundreds in the second group",
            "Empty places get a zero: 300 006",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Comparing Six-Digit Numbers
        self.next_band(1)
        self.write_rows(1, "Comparing Six-Digit Numbers", [
            "More digits means a bigger number",
            "Same digits: compare from the left",
            "254 138 beats 245 318 in the ten thousands",
            "Open side faces the bigger number",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Ordering and Representing on a Number Line
        self.next_band(2)
        self.write_rows(2, "Ordering and Representing on a Number Line", [
            "Ascending: smallest to biggest",
            "245 318, 245 381, 254 138",
            "1 000 more than 245 318 is 246 318",
            "1 less than 300 000 is 299 999",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``99 999 is bigger than 100 000''",
            "``Three hundred thousand and six is 3 006''",
            "``245318 is written 2 453 18''",
            "``Ascending means biggest first''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Say It, Write It
        self.next_band(4)
        self.write_rows(4, "Say It, Write It", [
            "Two groups of three",
            "Left group, then say thousand",
            "Empty places get a zero",
            "300 006 has six digits",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Bigger or Smaller
        self.next_band(5)
        self.write_rows(5, "Bigger or Smaller", [
            "Count the digits first",
            "Then start on the left",
            "R198 590 beats R189 950",
            "100 000 beats 99 999",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Put Them in a Line
        self.next_band(6)
        self.write_rows(6, "Put Them in a Line", [
            "Ascending climbs up",
            "Descending comes down",
            "245 318 and 245 381 sit close together",
            "254 138 is far along",
        ], scale=0.9, box=0)

        last = Tex("Split into groups of three, compare from the left, and let the number line show the gaps.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
