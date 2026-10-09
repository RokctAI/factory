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

# Band-layout whiteboard scene for flow-diagrams-and-rules-for-geometric-patterns (Part 1 Expert
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


class FlowDiagramsAndRulesForGeometricPatternsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Inputs, Rules and Outputs
        self.write_rows(0, "Inputs, Rules and Outputs", [
            "Input, rule, output",
            "Times 3 then plus 1: input 3 gives 10",
            "Backwards: 31 minus 1, divided by 3 is 10",
            "Order of boxes matters",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Finding the Rule
        self.next_band(1)
        self.write_rows(1, "Finding the Rule", [
            "Differences give the multiplier",
            "Outputs 5, 9, 13, 17: times 4 then plus 1",
            "Outputs 2, 5, 8, 11: times 3 minus 1",
            "Test the rule on every pair",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Same Rule, Three Ways
        self.next_band(2)
        self.write_rows(2, "Same Rule, Three Ways", [
            "Words, diagram, number sentence",
            "3 times box plus 1 equals sticks",
            "Plus 1 then times 3 is different",
            "Test equivalence with inputs",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Do the boxes in any order''",
            "``Find inputs by going forwards''",
            "``One pair fixes the rule''",
            "``Agree once means equivalent''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): The Number Machine
        self.next_band(4)
        self.write_rows(4, "The Number Machine", [
            "In, rule, out",
            "Input 7: 21 then 22",
            "Backwards: 31, 30, 10",
            "Follow the boxes in order",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Find the Rule
        self.next_band(5)
        self.write_rows(5, "Find the Rule", [
            "Jumps give the times",
            "Then fix with plus or minus",
            "5, 9, 13, 17: times 4 plus 1",
            "Test every pair",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Three Ways to Say It
        self.next_band(6)
        self.write_rows(6, "Three Ways to Say It", [
            "Words",
            "Flow diagram",
            "Number sentence",
            "Test with a number",
        ], scale=0.9, box=3)

        last = Tex("Input, rule, output: run it forwards, run it backwards, and test that two rules agree on every number.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
