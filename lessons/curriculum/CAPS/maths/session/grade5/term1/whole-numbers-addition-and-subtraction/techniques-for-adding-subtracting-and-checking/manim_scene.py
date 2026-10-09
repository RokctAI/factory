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
        # --- Band 0 (subtopic_1): Breaking Down and Building Up
        self.write_rows(0, "Breaking Down and Building Up", [
            "Split by place, add like parts",
            "23 400 + 15 300 is 38 000 + 700",
            "58 760 minus 23 000, then minus 450",
            "27 650 + 2 350 = 30 000",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Rounding and Compensating
        self.next_band(1)
        self.write_rows(1, "Rounding and Compensating", [
            "Round to a friendly number, then fix",
            "34 567 + 9 998: add 10 000, take off 2",
            "65 432 minus 20 000, then add 3 back",
            "R12 485 + R4 999 is R17 484",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Number Lines and Inverse Checks
        self.next_band(2)
        self.write_rows(2, "Number Lines and Inverse Checks", [
            "Count up on a number line",
            "38 750 to 39 000 is 250",
            "39 000 to 42 000 is 3 000",
            "The answer is 250 + 3 000 = 3 250",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``9 998: add 10 000, then add 2''",
            "``19 997: take 20 000, then take 3 more''",
            "``The answer is where you land''",
            "``Check with the same method''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Split It by Place
        self.next_band(4)
        self.write_rows(4, "Split It by Place", [
            "Thousands with thousands",
            "Hundreds with hundreds",
            "23 400 + 15 300 is 38 700",
            "650 + 350 makes 1 000",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Round, Then Fix
        self.next_band(5)
        self.write_rows(5, "Round, Then Fix", [
            "9 998 is nearly 10 000",
            "Added too much? Take it off",
            "Took too much? Give it back",
            "65 432 minus 19 997 is 45 435",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Jump and Check
        self.next_band(6)
        self.write_rows(6, "Jump and Check", [
            "Jump to a round number",
            "Then jump to the end",
            "Add up the jumps: 3 250",
            "Check: 38 750 + 3 250 = 42 000",
        ], scale=0.9, box=3)

        last = Tex("Split it, round and fix it, or jump it on a number line, and always check with a second technique.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
