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

# Band-layout whiteboard scene for dividing-two-and-three-digit-numbers (Part 1 Expert
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


class DividingTwoAndThreeDigitNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Two Faces of Division
        self.write_rows(0, "Two Faces of Division", [
            "Sharing: 84 sweets among 4",
            "Grouping: 96 in rows of 8",
            "Which number times 4 is 84? 21",
            "Dividend first, divisor second",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Dividing a Two-Digit Number
        self.next_band(1)
        self.write_rows(1, "Dividing a Two-Digit Number", [
            "84 is 80 plus 4: 20 plus 1 is 21",
            "96 is 80 plus 16: 10 plus 2 is 12",
            "85 divided by 4 is 21 remainder 1",
            "Remainder smaller than the divisor",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Dividing a Three-Digit Number by Chunking
        self.next_band(2)
        self.write_rows(2, "Dividing a Three-Digit Number by Chunking", [
            "372 divided by 6: take 300, 60, 12",
            "Chunks 50, 10, 2 make 62",
            "375 divided by 6 is 62 remainder 3",
            "Estimate: a little more than 60",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``4 divided by 84 is 21''",
            "``20 remainder 5 for 85 divided by 4''",
            "``96 is 90 plus 6 for dividing by 8''",
            "``Chunks need no adding''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Share It or Group It
        self.next_band(4)
        self.write_rows(4, "Share It or Group It", [
            "Sharing: how many each",
            "Grouping: how many groups",
            "Which number times 4 is 84?",
            "Whole amount first",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Break It into Pieces
        self.next_band(5)
        self.write_rows(5, "Break It into Pieces", [
            "84: 80 and 4",
            "20 plus 1 is 21",
            "96: 80 and 16",
            "85 divided by 4: 21 remainder 1",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Big Numbers in Chunks
        self.next_band(6)
        self.write_rows(6, "Big Numbers in Chunks", [
            "Take 300: 72 left",
            "Take 60: 12 left",
            "Take 12: 0 left",
            "50 plus 10 plus 2 is 62",
        ], scale=0.9, box=3)

        last = Tex("Divide by asking how many times it fits: break into pieces, chunk big numbers, keep the remainder small.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
