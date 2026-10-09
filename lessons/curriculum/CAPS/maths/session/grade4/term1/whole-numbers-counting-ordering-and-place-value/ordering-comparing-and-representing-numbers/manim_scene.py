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
        # --- Band 0 (subtopic_1): Comparing from the Left
        self.write_rows(0, "Comparing from the Left", [
            "More digits means a bigger number",
            "Same digits: compare from the left",
            "1 850 beats 1 805 in the tens",
            "Open side faces the bigger number",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Ordering and Representing Numbers
        self.next_band(1)
        self.write_rows(1, "Ordering and Representing Numbers", [
            "Ascending: smallest to largest",
            "Descending: largest to smallest",
            "3 450 is 3 000 plus 400 plus 50",
            "Words: say and before the tens",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Odd and Even to 1 000
        self.next_band(2)
        self.write_rows(2, "Odd and Even to 1 000", [
            "Even shares into two equal groups",
            "Last digit 0, 2, 4, 6, 8 means even",
            "1 085 ends in 5: odd",
            "Odd plus odd is even",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``999 beats 1 850 because 9 beats 1''",
            "``1 085 is one thousand eight hundred and five''",
            "``Add the digits to test odd or even''",
            "``Ending in 0 is neither odd nor even''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Which Is Bigger
        self.next_band(4)
        self.write_rows(4, "Which Is Bigger", [
            "Count digits first",
            "Then compare from the left",
            "Hundreds 8, 5, 8: the 5 loses",
            "Open side faces the bigger number",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Lining Them Up
        self.next_band(5)
        self.write_rows(5, "Lining Them Up", [
            "Ascending: going up",
            "Descending: going down",
            "Digits, words, expanded form",
            "1 085: no hundreds word",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Odd Side, Even Side
        self.next_band(6)
        self.write_rows(6, "Odd Side, Even Side", [
            "Even: two equal groups",
            "Odd: one left over",
            "Look at the last digit only",
            "346 even, 1 085 odd",
        ], scale=0.9, box=2)

        last = Tex("Compare from the left, open side to the bigger number, last digit tells odd or even.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
