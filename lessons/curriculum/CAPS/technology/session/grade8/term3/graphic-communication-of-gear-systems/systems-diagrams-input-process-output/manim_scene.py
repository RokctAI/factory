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

# Band-layout whiteboard scene for systems-diagrams-input-process-output (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/160/120/110/90 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SystemsDiagramsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Systems Thinking: Input, Process, Output
        self.write_rows(0, "Systems Thinking: Input, Process, Output", [
            "Input, process, output",
            "Ruled boxes, arrows with numbers, a title",
            "Gear drawing: how; systems diagram: what",
            "Skeleton of the flow chart",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Systems Diagram for a Gear System With MA 4:1
        self.next_band(1)
        self.write_rows(1, "Systems Diagram for a Gear System With MA 4:1", [
            "In: 12T, 400 rpm, weak, clockwise",
            "Process: 12T to 48T, 4:1, MA 4, flips",
            "Out: 100 rpm, four times torque, anticlockwise",
            "Two stages: 200 rpm between",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Systems Diagram for a Train Whose Output Is Faster
        self.next_band(2)
        self.write_rows(2, "Systems Diagram for a Train Whose Output Is Faster", [
            "In: 48T, 100 rpm, strong",
            "Process: 1:4, MA 0.25",
            "Out: 400 rpm, quarter torque",
            "Full chain: battery to cage, brake aside",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Gears in the input box''",
            "``Output speed multiplied for a reducer''",
            "``Direction left off''",
            "``Flow chart disagrees with the drawing''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Boxes and Arrows
        self.next_band(4)
        self.write_rows(4, "Boxes and Arrows", [
            "What goes in, what happens, what comes out",
            "Numbers on every arrow",
            "Say the job in the title",
            "Board reads this first",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Slow Strong Box
        self.next_band(5)
        self.write_rows(5, "Slow Strong Box", [
            "Fast weak in, slow strong out",
            "Divide speed, multiply torque",
            "Flip at each mesh",
            "Add battery before, cage after",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Fast Weak Box
        self.next_band(6)
        self.write_rows(6, "Fast Weak Box", [
            "Strong in, fast out: hand drill",
            "Same gears, swapped driver",
            "Ratio from teeth, then speed and torque",
            "Numbers must match the drawing",
        ], scale=0.9, box=1)

        last = Tex("Input, process, output with numbers on the arrows: divide speed, multiply torque, flip direction, and chain the whole winder for the board.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
