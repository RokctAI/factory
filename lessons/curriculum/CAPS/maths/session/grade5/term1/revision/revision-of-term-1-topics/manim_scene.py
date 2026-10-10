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

# Band-layout whiteboard scene for revision-of-term-1-topics (Part 1 Expert
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


class RevisionOfTerm1TopicsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Numbers: Place Value, Ordering and Rounding
        self.write_rows(0, "Numbers: Place Value, Ordering and Rounding", [
            "148 365: the 4 is worth 40 000",
            "153 840 is bigger than 148 365",
            "148 365 rounds to 148 400",
            "Nearest 1 000: 148 000",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Number Sentences, Adding and Subtracting
        self.next_band(1)
        self.write_rows(1, "Number Sentences, Adding and Subtracting", [
            "12 476 + 9 858 = 22 334",
            "153 840 minus 148 365 is 5 475",
            "Check: 148 365 + 5 475 = 153 840",
            "(25 times 4) times 13 is 1 300",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Multiplying, Factors, Ratio and Rate
        self.next_band(2)
        self.write_rows(2, "Multiplying, Factors, Ratio and Rate", [
            "24 times 135 is 2 700 + 540 = 3 240",
            "Factors of 36 come in pairs",
            "Every 15 and every 20: together at 60",
            "1 syrup to 5 water: 4 to 20",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``99 999 beats 100 000''",
            "``2 449 to 2 450 to 2 500''",
            "``Smaller from bigger in every column''",
            "``1 to 5 becomes 4 to 8''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): The Takings Board
        self.next_band(4)
        self.write_rows(4, "The Takings Board", [
            "Seats: the 4 is worth 40 000",
            "Compare from the left",
            "Nearest 100: look at the tens",
            "148 365 is about 148 400",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): At the Gate and the Till
        self.next_band(5)
        self.write_rows(5, "At the Gate and the Till", [
            "Line up, carry, exchange",
            "22 334 visitors",
            "R5 475 more this year",
            "Add back to check",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): At the Stalls
        self.next_band(6)
        self.write_rows(6, "At the Stalls", [
            "24 stalls at R135: R3 240",
            "Factors in pairs, multiples go up",
            "Ratio: multiply both parts",
            "Rate: per means for each",
        ], scale=0.9, box=0)

        last = Tex("Place value, sentences, columns, multiplying and checks: every Term 1 tool, used every time.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
