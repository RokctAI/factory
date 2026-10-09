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

# Band-layout whiteboard scene for budgeting-materials-and-labour (Part 1 Expert
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


class HeadgearBudgetSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Realistic Budget Is and Why the Board Wants One
        self.write_rows(0, "What a Realistic Budget Is and Why the Board Wants One", [
            "Quantities from drawings, rates from market",
            "Complete, realistic, honest",
            "Materials, labour, plant, fees, contingency, VAT",
            "1:100: 600 mm is 60 m",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Costing Materials for the Real Headgear
        self.next_band(1)
        self.write_rows(1, "Costing Materials for the Real Headgear", [
            "Lengths x kg/m = tonnes; show working",
            "Legs: 4 x 62 m x 100 kg/m = 24.8 t",
            "Concrete in cubic metres; sheaves as units",
            "Item, quantity, unit, rate, amount, source",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Costing Labour, Plant and Contingency
        self.next_band(2)
        self.write_rows(2, "Costing Labour, Plant and Contingency", [
            "Labour by trade and time: 2 880 hours",
            "Cranes by the day; fees 8-12 percent",
            "Insurance, site set-up, dust, tests",
            "Contingency 10-15 percent; VAT 15 percent",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Materials only, no labour or plant''",
            "``Rates without sources or dates''",
            "``Quantities guessed, not taken off''",
            "``No contingency''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Counting the Rand
        self.next_band(4)
        self.write_rows(4, "Counting the Rand", [
            "Five columns, every number checkable",
            "Cheapest bid is a warning",
            "Date and source on everything",
            "Model in rand, same format",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Steel by the Tonne
        self.next_band(5)
        self.write_rows(5, "Steel by the Tonne", [
            "Steel by the tonne",
            "Plus 10 percent for bolts and plates",
            "Winder in or out? Say which",
            "Estimate and label it",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): People, Cranes and the Unexpected
        self.next_band(6)
        self.write_rows(6, "People, Cranes and the Unexpected", [
            "People, days, rates",
            "A crane to 60 metres costs by the day",
            "Load tests before anyone rides",
            "Contingency is visible, padding is hidden",
        ], scale=0.9, box=3)

        last = Tex("Take the quantities off the drawing, price them from sourced rates, cost the people and the cranes, add contingency and tax, and show every number's origin.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
