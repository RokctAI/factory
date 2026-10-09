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

# Band-layout whiteboard scene for tools-materials-and-construction-steps (Part 1 Expert
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


class ConstructionPlanningSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Listing Tools and Materials From the Parts List
        self.write_rows(0, "Listing Tools and Materials From the Parts List", [
            "Materials grouped from the parts list, plus spare",
            "Tools from each operation",
            "Spring balance, stopwatch, masses, eye protection",
            "Checked against the store and the drawing",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Logical Construction Steps: Sequence and Dependencies
        self.next_band(1)
        self.write_rows(1, "Logical Construction Steps: Sequence and Dependencies", [
            "What must already exist?",
            "Cut, base, gear plate, faces flat, stand, join",
            "Tower to base, back-leg, sheave, winder, brake",
            "Parallel: cutting, drilling, cage; use glue time",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): The Flow Chart and the Build Timetable
        self.next_band(2)
        self.write_rows(2, "The Flow Chart and the Build Timetable", [
            "Rounded start/end, rectangles, diamonds",
            "Gears free? Square? Lifts 300 g?",
            "15-minute blocks, names across, glue before break",
            "List, sequence, chart, timetable agree",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Materials list from memory''",
            "``Sheave fitted before the tower is square''",
            "``No decision diamonds''",
            "``Timetable with no slack''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): What You Need Before You Start
        self.next_band(4)
        self.write_rows(4, "What You Need Before You Start", [
            "Shopping list from the drawing",
            "Tools for every job",
            "A bit spare on every line",
            "Fix gaps today, not build day",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Base Before Tower, Tower Before Sheave
        self.next_band(5)
        self.write_rows(5, "Base Before Tower, Tower Before Sheave", [
            "Faces flat, then stand them",
            "Nothing on top of what is not built",
            "Who can work at the same time?",
            "Glue sets while others cut",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Boxes, Arrows and a Clock
        self.next_band(6)
        self.write_rows(6, "Boxes, Arrows and a Clock", [
            "Boxes in order, arrows between",
            "Diamond at every test with a no branch",
            "Names and times",
            "Thirty minutes spare",
        ], scale=0.9, box=2)

        last = Tex("List materials and tools from the drawing, order the steps by what must exist first, chart them with tests built in, and timetable people with slack.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
