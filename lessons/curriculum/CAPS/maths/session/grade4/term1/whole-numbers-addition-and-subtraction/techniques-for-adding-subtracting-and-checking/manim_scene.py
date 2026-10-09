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

# Band-layout whiteboard scene for techniques-for-adding-subtracting-and-checking (Part 1 Expert
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


class TechniquesForAddingSubtractingAndCheckingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Estimate First, Then Break Down
        self.write_rows(0, "Estimate First, Then Break Down", [
            "Estimate first: about R1 600",
            "Break into 1 000, 200, 40, 8",
            "1 248 plus 397 is 1 645",
            "Build up: 25, 100, 650 gives 775",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Number Lines and Rounding with Compensation
        self.next_band(1)
        self.write_rows(1, "Number Lines and Rounding with Compensation", [
            "Jump 300, 90, 7 on the line",
            "397 is 400 minus 3",
            "1 648 minus 3 is 1 645",
            "Took away 25 too many? Add 25",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Inverse Operations as a Check
        self.next_band(2)
        self.write_rows(2, "Inverse Operations as a Check", [
            "Addition and subtraction undo each other",
            "2 000 minus 1 395 is 605",
            "Check with a different technique",
            "Disagree? Estimate to decide",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``No need to estimate''",
            "``750 minus 25 for the fix''",
            "``Check with the same method''",
            "``Disagree? Pick one at random''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Guess, Then Break It Up
        self.next_band(4)
        self.write_rows(4, "Guess, Then Break It Up", [
            "Guess first: about 1 600",
            "Break into place-value parts",
            "1 000, 500, 130, 15 make 1 645",
            "Build up the jumps: 775",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Round It, Then Fix It
        self.next_band(5)
        self.write_rows(5, "Round It, Then Fix It", [
            "397 is 400 minus 3",
            "1 648 take off 3 is 1 645",
            "1 875 is 1 900 minus 25",
            "750 add back 25 is 775",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Check It the Other Way
        self.next_band(6)
        self.write_rows(6, "Check It the Other Way", [
            "Plus and minus undo each other",
            "1 645 minus 397 is 1 248",
            "1 395 plus 605 is 2 000",
            "Two techniques every time",
        ], scale=0.9, box=3)

        last = Tex("Estimate, break down or round and fix, then check the other way round.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
