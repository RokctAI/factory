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

# Band-layout whiteboard scene for budget-for-entrepreneurs-day (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-5). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (180/200/190/90/130 of 790 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class BudgetForEntrepreneursDaySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.78, box=None):
        t = Tex(title).scale(1.1).shift(band_shift(k) + UP * 2.4)
        self.play(Write(t))
        self.wait(1.5)
        made = []
        for i, r in enumerate(rows):
            m = Tex(r).scale(scale).shift(band_shift(k) + UP * (1.3 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.3)
            made.append(m)
        if box is not None:
            self.play(Create(SurroundingRectangle(made[box], color=YELLOW)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1)
        self.write_rows(0, "Fixed and variable costs", [
            "Fixed: same whatever the quantity",
            "Table hire, poster, equipment hire",
            "Variable: per unit produced",
            "Ingredients, cups, bags, labels",
        ], box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Cost price and selling price", [
            "Variable cost per unit",
            "Share of fixed cost per unit",
            "Cost price = total cost / units",
            "Selling price = cost price + mark-up",
        ], box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Break-even and the full budget", [
            "Break-even: income = total costs",
            "Units to break even = fixed / (price - variable)",
            "Budget: income, costs, expected profit",
            "Compare actual results afterwards",
        ], box=0)


        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "The muffin shopping list", [
            "Fixed: table R50, posters R30, gas R40",
            "Variable: ingredients R240, cups R40",
            "Total cost R400 for 80 muffins",
            "Cost price R5 each",
        ], box=3)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "How many before we're safe?", [
            "Each muffin: R10 - R3,50 = R6,50",
            "Fixed costs to cover: R120",
            "R120 / R6,50 = about 19 muffins",
            "After 19, every muffin is profit",
        ], box=2)

        self.wait(4)
