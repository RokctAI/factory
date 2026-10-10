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

# Band-layout whiteboard scene for counting-and-place-value-of-decimal-fractions (Part 1 Expert
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


class CountingAndPlaceValueOfDecimalFractionsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Tenths and Hundredths as Decimals
        self.write_rows(0, "Tenths and Hundredths as Decimals", [
            "Tenths: first place after the comma",
            "Hundredths: second place",
            "7/10 = 0,7 and 7/100 = 0,07",
            "3,68 m = 3 and 68/100 m",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Place Value of Decimal Digits
        self.next_band(1)
        self.write_rows(1, "Place Value of Decimal Digits", [
            "3,68: units, tenths, hundredths",
            "3 + 0,6 + 0,08",
            "12,45 = 10 + 2 + 0,4 + 0,05",
            "4,05 is not 4,5",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Counting Forwards and Backwards in Decimals
        self.next_band(2)
        self.write_rows(2, "Counting Forwards and Backwards in Decimals", [
            "Tenths: 2,8; 2,9; 3,0; 3,1",
            "Hundredths: 0,98; 0,99; 1,00",
            "Back in 0,2: 1,2; 1,0; 0,8",
            "Ten tenths make a whole",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``2,8; 2,9; 2,10''",
            "``7/100 = 0,7''",
            "``The 6 in 3,68 is worth 6''",
            "``4,05 = 4,5''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): After the Comma
        self.next_band(4)
        self.write_rows(4, "After the Comma", [
            "After the comma",
            "Tenths, then hundredths",
            "0,7 and 0,07",
            "R0,25 is 25 cents",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Each Digit Has a Seat
        self.next_band(5)
        self.write_rows(5, "Each Digit Has a Seat", [
            "Each digit has a seat",
            "3 units",
            "6 tenths, 8 hundredths",
            "Zeros hold seats",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Count in Small Steps
        self.next_band(6)
        self.write_rows(6, "Count in Small Steps", [
            "Small steps",
            "2,9 then 3,0",
            "0,99 then 1,00",
            "1,0 back to 0,8",
        ], scale=0.9, box=1)

        last = Tex("The comma splits wholes from parts: tenths come first, hundredths second, and ten tenths make a whole.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
