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

# Band-layout whiteboard scene for flow-diagrams-tables-and-number-sentences (Part 1 Expert
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


class FlowDiagramsTablesAndNumberSentencesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Flow Diagrams with Many Inputs
        self.write_rows(0, "Flow Diagrams with Many Inputs", [
            "Times 6: 1, 2, 3 give 6, 12, 18",
            "Times 6, then plus 5",
            "3 vetkoek: 18, then R23",
            "R47: minus 5 is 42, divided by 6 is 7",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Input and Output Tables
        self.next_band(1)
        self.write_rows(1, "Input and Output Tables", [
            "Inputs: 1, 2, 3, 4, 10",
            "Outputs: R11, R17, R23, R29, R65",
            "Inputs up 2, outputs up 6",
            "Rule: times 3, then plus 1",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Words, Diagrams, Tables and Number Sentences
        self.next_band(2)
        self.write_rows(2, "Words, Diagrams, Tables and Number Sentences", [
            "Words: times 6, then add 5",
            "Flow: times 6 box, plus 5 box",
            "4 times 6 plus 5 equals 29",
            "6 times a number plus 5 is 35: 5",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``R29 plus R6 for 10 vetkoek''",
            "``Forgetting the plus 5 box''",
            "``Output jump 6, so times 6''",
            "``47 divided by 6 first''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Many Numbers Through One Machine
        self.next_band(4)
        self.write_rows(4, "Many Numbers Through One Machine", [
            "Many numbers, one machine",
            "1, 2, 3 give R6, R12, R18",
            "Delivered: times 6, plus 5",
            "R47 means 7 vetkoek",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Read the Table
        self.next_band(5)
        self.write_rows(5, "Read the Table", [
            "Top row: inputs",
            "Bottom row: outputs",
            "For 10, use the rule: R65",
            "Compare jumps, fix the start",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Four Ways, One Rule
        self.next_band(6)
        self.write_rows(6, "Four Ways, One Rule", [
            "Four ways, one rule",
            "Words, flow, table, sentence",
            "4 vetkoek: R29",
            "Test every column",
        ], scale=0.9, box=1)

        last = Tex("Put each input through the rule, compare the jumps to find a rule, and test every column before you trust it.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
