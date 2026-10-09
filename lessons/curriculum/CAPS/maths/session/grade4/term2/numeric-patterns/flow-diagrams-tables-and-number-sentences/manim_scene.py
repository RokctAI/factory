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
        # --- Band 0 (subtopic_1): Tables from Rules
        self.write_rows(0, "Tables from Rules", [
            "Vetkoek: times 6",
            "Taxi: times 12 then plus 5",
            "Input 3: 36 plus 5 is 41",
            "Pocket money week 10: 250",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Rules from Tables and Missing Values
        self.next_band(1)
        self.write_rows(1, "Rules from Tables and Missing Values", [
            "Outputs step by 12: times 12",
            "Fix the start: plus 5",
            "Missing input: run backwards",
            "Undo the last step first",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Four Descriptions, One Rule
        self.next_band(2)
        self.write_rows(2, "Four Descriptions, One Rule", [
            "Words, diagram, table, sentence",
            "12 times box plus 5 equals fare",
            "17 times box fails at input 2",
            "Pick the form for the job",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Undo the first step first''",
            "``Output step is always the multiplier''",
            "``Fits one row, fits the rule''",
            "``Add on to the previous row''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Fill the Table
        self.next_band(4)
        self.write_rows(4, "Fill the Table", [
            "Inputs and outputs side by side",
            "Times 6: 6, 12, 18, 24, 30",
            "Taxi input 3: 41",
            "Input 20: 120",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Find the Rule, Find the Gap
        self.next_band(5)
        self.write_rows(5, "Find the Rule, Find the Gap", [
            "Steps of 12: times 12",
            "Then plus 5",
            "42 divided by 6 is 7",
            "65: minus 5, then divide by 12",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Same Rule, Four Outfits
        self.next_band(6)
        self.write_rows(6, "Same Rule, Four Outfits", [
            "Words",
            "Flow diagram",
            "Table",
            "Number sentence",
        ], scale=0.9, box=3)

        last = Tex("Fill the table from the rule, find the rule from the table, run it backwards, and check all four forms agree.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
