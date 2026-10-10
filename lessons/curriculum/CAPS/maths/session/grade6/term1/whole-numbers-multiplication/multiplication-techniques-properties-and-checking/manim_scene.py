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

# Band-layout whiteboard scene for multiplication-techniques-properties-and-checking (Part 1 Expert
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


class MultiplicationTechniquesPropertiesAndCheckingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Doubling and Halving
        self.write_rows(0, "Doubling and Halving", [
            "Double one, halve the other",
            "25 times 48 = 50 times 24",
            "= 100 times 12 = 1 200",
            "Times 4: double twice",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Properties of Multiplication, Including 1
        self.next_band(1)
        self.write_rows(1, "Properties of Multiplication, Including 1", [
            "Swap and regroup: 4 times 25 = 100",
            "4 times 37 times 25 = 3 700",
            "7 times 1 999 = 14 000 minus 7 = 13 993",
            "Times 1: same. Times 0: zero.",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Estimating and Checking with Division
        self.next_band(2)
        self.write_rows(2, "Estimating and Checking with Division", [
            "Estimate: 236 times 20 is about 4 720",
            "Inverse: 6 000 divided by 48 = 125",
            "294 times 8 = 2 352",
            "Calculator only to check",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``25 times 48 = 50 times 96''",
            "``4 875 times 1 = 4 876''",
            "``4 875 times 0 = 4 875''",
            "``7 times 1 999 = 14 007''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Double One, Halve the Other
        self.next_band(4)
        self.write_rows(4, "Double One, Halve the Other", [
            "Double and halve",
            "50 times 24",
            "100 times 12",
            "1 200 rolls",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Rules That Help
        self.next_band(5)
        self.write_rows(5, "Rules That Help", [
            "Swap the order",
            "Group to make 100",
            "Times 1: no change",
            "Times 0: zero",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Undo It with Division
        self.next_band(6)
        self.write_rows(6, "Undo It with Division", [
            "Estimate first",
            "Undo with division",
            "6 000 divided by 125 = 48",
            "Calculator to check",
        ], scale=0.9, box=1)

        last = Tex("Make numbers friendly by doubling and halving or regrouping, remember that times 1 keeps a number and times 0 gives 0, and check with division.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
