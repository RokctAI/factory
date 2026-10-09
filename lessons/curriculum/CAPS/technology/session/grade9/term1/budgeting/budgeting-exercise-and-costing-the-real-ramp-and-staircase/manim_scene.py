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

# Band-layout whiteboard scene for budgeting-exercise-and-costing-the-real-ramp-and-staircase (Part 1 Expert
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


class BudgetingExerciseAndCostingTheRealRampAndStaircaseSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): From Estimate to Budget: Headings, Lines and Totals
        self.write_rows(0, "From Estimate to Budget: Headings, Lines and Totals", [
            "Materials, labour, transport, allowances, total",
            "Line = qty x sourced price, with working",
            "Exercise: one step = 0.045 m3",
            "Round UP to units sold: 23 bags, 4 lengths",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Costing the Real Ramp and Staircase Line by Line
        self.next_band(1)
        self.write_rows(1, "Costing the Real Ramp and Staircase Line by Line", [
            "Concrete ~2.3 m3: 17 bags, 1.5 sand, 1.5 stone",
            "Fill 2.6 m3 hardcore; mesh 2 sheets",
            "Rails 19 + posts 14 = 33 m tube, or quote",
            "3 crew x 8 days; deliveries; +10\\% +10\\%",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Checking, Trimming and Presenting the Tender Price
        self.next_band(2)
        self.write_rows(2, "Checking, Trimming and Presenting the Tender Price", [
            "Check: arithmetic, sense, proportion",
            "Materials largest for concrete work",
            "Save by layout, not by gradient",
            "Page: totals, date, exclusions",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Total with no lines''",
            "``Rounded down to look cheap''",
            "``Contingency cut to win''",
            "``Quantities not from the drawing''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Budget Is an Estimate with Rules
        self.next_band(4)
        self.write_rows(4, "A Budget Is an Estimate with Rules", [
            "Estimate with rules",
            "What, how many, price, source",
            "Practise on one step",
            "Round up, never down",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Concrete, Steel, People and Trips
        self.next_band(5)
        self.write_rows(5, "Concrete, Steel, People and Trips", [
            "17 bags for the concrete",
            "33 metres of tube",
            "Three people, eight days",
            "Ten percent, twice",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Does the Number Make Sense?
        self.next_band(6)
        self.write_rows(6, "Does the Number Make Sense?", [
            "Redo the maths",
            "Compare with town",
            "Never cut the ramp or the contingency",
            "Be ready for three questions",
        ], scale=0.9, box=2)

        last = Tex("Quantities from the drawing, prices from named sources, rounded up, with waste and contingency, checked three ways: a tender price with nothing hidden.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
