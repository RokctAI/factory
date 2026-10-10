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
        # --- Band 0 (subtopic_1): From Picture to Flow Diagram
        self.write_rows(0, "From Picture to Flow Diagram", [
            "1 table: 4 seats",
            "2 tables: 6 seats",
            "Tables, times 2, plus 2, seats",
            "Hexagons: times 5, plus 1",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Working Backwards to the Input
        self.next_band(1)
        self.write_rows(1, "Working Backwards to the Input", [
            "Undo the last step first",
            "62 guests: 62 minus 2 = 60",
            "60 divided by 2 = 30 tables",
            "101 matches: 20 hexagons",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Words, Tables, Diagrams and Number Sentences
        self.next_band(2)
        self.write_rows(2, "Words, Tables, Diagrams and Number Sentences", [
            "Words, diagram, table, sentence",
            "5 times 2 + 2 = 12",
            "Double, then add 2",
            "Add 1, then double: same seats",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``2 tables seat 8''",
            "``62 divided by 2, minus 2 = 29 tables''",
            "``10 hexagons need 60 matches''",
            "``Testing only one input''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Picture to Machine
        self.next_band(4)
        self.write_rows(4, "Picture to Machine", [
            "Picture to machine",
            "2 seats per table",
            "2 at the ends",
            "Times 2, plus 2",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): How Many Shapes
        self.next_band(5)
        self.write_rows(5, "How Many Shapes", [
            "How many shapes?",
            "Minus 2",
            "Divide by 2",
            "30 tables",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Four Ways, One Pattern
        self.next_band(6)
        self.write_rows(6, "Four Ways, One Pattern", [
            "One pattern, four ways",
            "Same inputs",
            "Same outputs",
            "Equivalent",
        ], scale=0.9, box=3)

        last = Tex("Let the picture show you the rule, run the flow diagram forwards for outputs and backwards for inputs, and test every picture.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
