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

# Band-layout whiteboard scene for rounding-off-to-5-10-100-and-1000 (Part 1 Expert
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


class RoundingOffTo510100And1000Session(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Rounding to the Nearest 10 and 5
        self.write_rows(0, "Rounding to the Nearest 10 and 5", [
            "Look at the units",
            "5 or more: round up",
            "54 687 is about 54 690",
            "Nearest 5: 2 343 is about 2 345",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Rounding to the Nearest 100 and 1 000
        self.next_band(1)
        self.write_rows(1, "Rounding to the Nearest 100 and 1 000", [
            "Nearest 100: look at the tens",
            "Nearest 1 000: look at the hundreds",
            "54 687 is about 54 700 and 55 000",
            "1 449 is about 1 000",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Using Rounding to Estimate
        self.next_band(2)
        self.write_rows(2, "Using Rounding to Estimate", [
            "Round, then add",
            "55 000 + 38 000 = 93 000",
            "Exact: 92 901",
            "Estimate checks the answer",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``54 687 to the nearest 100 is 54 600''",
            "``1 449 to the nearest 1 000 is 2 000''",
            "``54 687 rounds to 55 687''",
            "``2 343 to the nearest 5 is 2 340''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Look Next Door
        self.next_band(4)
        self.write_rows(4, "Look Next Door", [
            "Look next door",
            "5 or more: up",
            "4 or less: down",
            "54 687 is about 54 690",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Bigger Steps
        self.next_band(5)
        self.write_rows(5, "Bigger Steps", [
            "Tens for 100",
            "Hundreds for 1 000",
            "54 700 and 55 000",
            "One digit only",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Round, Then Work
        self.next_band(6)
        self.write_rows(6, "Round, Then Work", [
            "Round first",
            "About 93 000",
            "Exact 92 901",
            "Far off? Check again",
        ], scale=0.9, box=1)

        last = Tex("Find the rounding place, look at the one digit to its right, round up for 5 or more, and use rounding to check your answers.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
