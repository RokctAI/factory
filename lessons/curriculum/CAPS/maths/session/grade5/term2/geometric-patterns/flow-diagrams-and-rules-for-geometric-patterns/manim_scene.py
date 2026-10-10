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
        # --- Band 0 (subtopic_1): Flow Diagrams: Input, Rule, Output
        self.write_rows(0, "Flow Diagrams: Input, Rule, Output", [
            "1 table: 6 chairs, 2 tables: 10",
            "Rule: times 4, then plus 2",
            "Input 5: 20, then 22",
            "Inputs 6, 7, 8 give 26, 30, 34",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Finding Inputs and Rules
        self.next_band(1)
        self.write_rows(1, "Finding Inputs and Rules", [
            "Output 30: minus 2 is 28",
            "28 divided by 4 is 7 tables",
            "Inputs 1, 2, 3 give 5, 8, 11",
            "Rule: times 3, then plus 2",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): One Rule, Three Ways
        self.next_band(2)
        self.write_rows(2, "One Rule, Three Ways", [
            "Words: times 4, then add 2",
            "Flow diagram: times 4 box, plus 2 box",
            "Number sentence: 5 times 4 plus 2 is 22",
            "Plus 2 first gives 28: different",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Adding first: 28 chairs, not 22''",
            "``Dividing 30 by 4 first''",
            "``Times 6 for 3 tables: 18, not 14''",
            "``Times 5 fits input 1 only''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Number In, Number Out
        self.next_band(4)
        self.write_rows(4, "Number In, Number Out", [
            "Number in, number out",
            "Times 4, then plus 2",
            "Input 5 gives 22",
            "Input 3 gives 14",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Run It Backwards
        self.next_band(5)
        self.write_rows(5, "Run It Backwards", [
            "Undo the last box first",
            "30 minus 2 is 28",
            "28 divided by 4 is 7",
            "Check forwards: 7 gives 30",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Same Rule, Different Clothes
        self.next_band(6)
        self.write_rows(6, "Same Rule, Different Clothes", [
            "Words, flow diagram, sentence",
            "All give 22 for input 5",
            "Order of the boxes matters",
            "Test with the same inputs",
        ], scale=0.9, box=1)

        last = Tex("Follow the arrows to find an output, undo the boxes in reverse to find an input, and test every rule with the same inputs.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
