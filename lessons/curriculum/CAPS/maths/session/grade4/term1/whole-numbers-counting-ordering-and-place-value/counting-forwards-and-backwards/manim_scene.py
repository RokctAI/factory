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

# Band-layout whiteboard scene for counting-forwards-and-backwards (Part 1 Expert
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


class CountingForwardsAndBackwardsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Counting in Steps from Any Start
        self.write_rows(0, "Counting in Steps from Any Start", [
            "Add the same number every time",
            "25s end in 25, 50, 75, 00",
            "3s repeat every ten numbers",
            "10s keep the units digit",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Counting Backwards
        self.next_band(1)
        self.write_rows(1, "Counting Backwards", [
            "Subtract the same number each time",
            "3 050 back 100 gives 2 950",
            "Back in 2s from odd stays odd",
            "Check by counting forwards",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Finding the Rule and the Missing Numbers
        self.next_band(2)
        self.write_rows(2, "Finding the Rule and the Missing Numbers", [
            "Step is the gap between neighbours",
            "Check the step on a second pair",
            "1 325 plus 25 fills the gap: 1 350",
            "Up or down? Ask first",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``After 75 comes 90''",
            "``3 050 back 100 is 3 950''",
            "``One pair is enough''",
            "``Sequences always go up''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Jumping in Steps
        self.next_band(4)
        self.write_rows(4, "Jumping in Steps", [
            "Every jump the same size",
            "25, 50, 75, 100, 125, 150",
            "9 900 plus 100 is 10 000",
            "Start from any number",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Going Backwards Too
        self.next_band(5)
        self.write_rows(5, "Going Backwards Too", [
            "Same jump, other direction",
            "1 000, 950, 900, 850, 800",
            "3 050 back 100 is 2 950",
            "Count forwards to check",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Fill the Gap
        self.next_band(6)
        self.write_rows(6, "Fill the Gap", [
            "Find the jump first",
            "Check it on another pair",
            "Going up or going down?",
            "Then fill the gap",
        ], scale=0.9, box=0)

        last = Tex("Same jump every time, forwards or back: find the step, check it, fill the gap.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
