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

# Band-layout whiteboard scene for fractions-of-whole-numbers (Part 1 Expert
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


class FractionsOfWholeNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Unit Fractions of Amounts
        self.write_rows(0, "Unit Fractions of Amounts", [
            "Unit fraction: divide by the bottom",
            "1/4 of 36: 36 divided by 4 is 9",
            "1/5 of R150 is R30",
            "1/12 of 60 minutes is 5 minutes",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Other Fractions of Amounts
        self.next_band(1)
        self.write_rows(1, "Other Fractions of Amounts", [
            "Divide by the bottom, times the top",
            "3/4 of 36: one quarter is 9",
            "3/4 of 36 is 27",
            "5/8 of 64 is 40",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Fraction Problems: The Part and the Rest
        self.next_band(2)
        self.write_rows(2, "Fraction Problems: The Part and the Rest", [
            "27 walk, 9 do not",
            "1/4 off R240: R60 off, pay R180",
            "3/4 of an hour is 45 minutes",
            "1/3 of 90 beats 1/2 of 40",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3/4 of 36 is 48''",
            "``3/4 of 36 is 9''",
            "``1/4 off R240: pay R60''",
            "``A half is always more than a third''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Share It Out
        self.next_band(4)
        self.write_rows(4, "Share It Out", [
            "Share into equal groups",
            "1/2 of 48 is 24",
            "1/8 of 64 is 8",
            "Divide by the bottom number",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): One Part, Then More
        self.next_band(5)
        self.write_rows(5, "One Part, Then More", [
            "Find one part first",
            "Then take as many parts as the top",
            "2/3 of 24 is 16",
            "4/5 of 25 is 20",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): The Part or the Rest
        self.next_band(6)
        self.write_rows(6, "The Part or the Rest", [
            "Part or what is left?",
            "R240 minus R60 is R180",
            "1/3 of 24 hours is 8 hours",
            "The parts add up to the whole",
        ], scale=0.9, box=1)

        last = Tex("Divide by the bottom to find one part, multiply by the top, then read the question to see which part it wants.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
