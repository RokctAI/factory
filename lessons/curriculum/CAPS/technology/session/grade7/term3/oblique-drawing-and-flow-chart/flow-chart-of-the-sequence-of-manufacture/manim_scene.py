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

# Band-layout whiteboard scene for flow-chart-of-the-sequence-of-manufacture (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/220/200/100/100/100 of 900 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FlowChartOfManufactureSession(MovingCameraScene):
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
        self.wait(60)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The language of flow charts
        self.write_rows(0, "The language of flow charts", [
            "Oval: start and end",
            "Rectangle: a step with a verb",
            "Diamond: yes or no, two exits",
            "Ruled arrows, no crossing",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Ordering the crane's build
        self.next_band(1)
        self.write_rows(1, "Ordering the crane's build", [
            "Glued parts early: base, mast, arm",
            "Coil, winch, pulley while glue dries",
            "Test magnet; no loops to a fix",
            "Assemble, wire; test the crane",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Drawing and checking
        self.next_band(2)
        self.write_rows(2, "Drawing and checking", [
            "Portrait A4, numbered boxes",
            "Rehearse: who, what, how long",
            "Agenda on making days; tick boxes",
            "Ticked chart is evidence",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Steps written as nouns''",
            "``Diamond with one exit''",
            "``Arm fitted before the mast exists''",
            "``No test until the end''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Four shapes
        self.next_band(4)
        self.write_rows(4, "Four shapes", [
            "Oval, rectangle, diamond, arrow",
            "Same width, few words",
            "Recipes and factory lines",
            "Order jumbled steps in the exam",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): The crane as a recipe
        self.next_band(5)
        self.write_rows(5, "The crane as a recipe", [
            "List first",
            "Slow glue first, coil while drying",
            "Ten clips? No: fix, retest",
            "Lift, move, drop, stand?",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Draw it, walk it
        self.next_band(6)
        self.write_rows(6, "Draw it, walk it", [
            "Start at the top, end at the bottom",
            "Move glue-gun clashes",
            "Add up against four periods",
            "Tick as you build",
        ], scale=0.9, box=2)

        last = Tex("Oval, rectangle, diamond and arrow; steps as instructions in dependency order, tests before assembly, and a rehearsed, ticked chart on making day.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
