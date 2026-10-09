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

# Band-layout whiteboard scene for design-brief-for-the-crane (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/170/230/100/100/100 of 890 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DesignBriefForTheCraneSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): From scenario to brief
        self.write_rows(0, "From scenario to brief", [
            "Need: sort steel from mixed scrap",
            "What, who for, what it must do",
            "Ferrous, electromagnet, release",
            "Leave height and materials open",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Specifications
        self.next_band(1)
        self.write_rows(1, "Specifications", [
            "Measurable: ruler, stopwatch, count",
            "Lift ten clips; release in one second",
            "Raise 150 mm; move 200 mm",
            "No copper; bulb on when magnet on",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Constraints
        self.next_band(2)
        self.write_rows(2, "Constraints", [
            "Card, string, nail, wire, cells",
            "A4 base; under 400 mm; four periods",
            "No mains; always a switch",
            "About the maker, not the crane",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Make a crane''",
            "``Must be strong''",
            "``Specs and constraints in one list''",
            "``Tall yellow crane with pivoting arm''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Writing the brief
        self.next_band(4)
        self.write_rows(4, "Writing the brief", [
            "One or two sentences",
            "What? Who for? What must it do?",
            "Every word from the investigation",
            "Do not fix the design yet",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Specifications you can test
        self.next_band(5)
        self.write_rows(5, "Specifications you can test", [
            "A number and an instrument",
            "Sorting and releasing first",
            "Must be strong is a wish",
            "Four to six are enough",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Constraints you must obey
        self.next_band(6)
        self.write_rows(6, "Constraints you must obey", [
            "Materials, size, time, cost, safety",
            "Is it about the crane or about me?",
            "Two columns, never mixed",
            "Limits make it a real problem",
        ], scale=0.9, box=1)

        last = Tex("A brief says what, who for and what it must do; specifications are testable; constraints are the limits on the maker.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
