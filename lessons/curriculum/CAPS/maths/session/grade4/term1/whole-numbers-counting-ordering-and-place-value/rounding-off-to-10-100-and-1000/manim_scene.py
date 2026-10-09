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

# Band-layout whiteboard scene for rounding-off-to-10-100-and-1000 (Part 1 Expert
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


class RoundingOffTo10100And1000Session(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Rounding to the Nearest 10
        self.write_rows(0, "Rounding to the Nearest 10", [
            "Between two tens: which is closer?",
            "Units 0 to 4 down, 5 to 9 up",
            "3 468 rounds to 3 470",
            "2 396 rounds to 2 400",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Rounding to the Nearest 100 and 1 000
        self.next_band(1)
        self.write_rows(1, "Rounding to the Nearest 100 and 1 000", [
            "Nearest 100: look at the tens digit",
            "Nearest 1 000: look at the hundreds digit",
            "3 468 gives 3 500 and 3 000",
            "Round the original in one step",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Rounding to Estimate
        self.next_band(2)
        self.write_rows(2, "Rounding to Estimate", [
            "Round first, then estimate",
            "3 500 plus 2 800 is about 6 300",
            "R1 300 times 4 is about R5 200",
            "Round to match the need",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Nearest 100: look at the units''",
            "``Round in stages''",
            "``A 5 rounds down''",
            "``One rounded answer fits all''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Up or Down to the Nearest 10
        self.next_band(4)
        self.write_rows(4, "Up or Down to the Nearest 10", [
            "Find the two tens either side",
            "Units 0 to 4: down",
            "Units 5 to 9: up",
            "3 468 is about 3 470",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Nearest 100 and Nearest 1 000
        self.next_band(5)
        self.write_rows(5, "Nearest 100 and Nearest 1 000", [
            "Nearest 100: look at the tens",
            "Nearest 1 000: look at the hundreds",
            "3 468 is about 3 500",
            "3 468 is about 3 000",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Guess Before You Work It Out
        self.next_band(6)
        self.write_rows(6, "Guess Before You Work It Out", [
            "Round first, guess the answer",
            "3 500 plus 2 800 is about 6 300",
            "Check the exact answer against it",
            "Round to match the need",
        ], scale=0.9, box=2)

        last = Tex("Look one digit to the right: 0 to 4 down, 5 to 9 up, then estimate before you calculate.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
