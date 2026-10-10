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

# Band-layout whiteboard scene for multiplying-four-digit-by-three-digit-numbers (Part 1 Expert
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


class MultiplyingFourDigitByThreeDigitNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Breaking Up the Three-Digit Number
        self.write_rows(0, "Breaking Up the Three-Digit Number", [
            "236 = 200 + 30 + 6",
            "1 245 times 6 = 7 470",
            "1 245 times 30 = 37 350",
            "1 245 times 200 = 249 000",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Long Multiplication in Columns
        self.next_band(1)
        self.write_rows(1, "Long Multiplication in Columns", [
            "One row per digit",
            "Tens row: one placeholder 0",
            "Hundreds row: two placeholder 0s",
            "3 408 times 125 = 426 000",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Zeros in the Numbers
        self.next_band(2)
        self.write_rows(2, "Zeros in the Numbers", [
            "304 has no tens: skip that row",
            "2 006 times 4 = 8 024",
            "2 006 times 300 = 601 800",
            "Total: 609 824",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Tens row of 3 408 times 125 is 6 816''",
            "``3 408 times 5 = 15 040''",
            "``No zeros in the hundreds row''",
            "``Rows not lined up''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Three Smaller Sums
        self.next_band(4)
        self.write_rows(4, "Three Smaller Sums", [
            "Three smaller sums",
            "249 000",
            "37 350 and 7 470",
            "293 820 pairs of shoes",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): One Row per Digit
        self.next_band(5)
        self.write_rows(5, "One Row per Digit", [
            "One row per digit",
            "One 0 for tens",
            "Two 0s for hundreds",
            "426 000 books",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Mind the Zeros
        self.next_band(6)
        self.write_rows(6, "Mind the Zeros", [
            "0 tens: skip the row",
            "Keep the placeholders",
            "609 824 seedlings",
            "About 600 000",
        ], scale=0.9, box=2)

        last = Tex("Split the three-digit number, do one row for each part with its placeholder zeros, add the rows and check with an estimate.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
