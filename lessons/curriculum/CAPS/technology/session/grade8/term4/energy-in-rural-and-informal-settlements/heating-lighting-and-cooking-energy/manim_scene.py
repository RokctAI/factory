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

# Band-layout whiteboard scene for heating-lighting-and-cooking-energy (Part 1 Expert
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


class SettlementEnergySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Energy Needs in Rural and Informal Settlements: Heating, Lighting and Cooking
        self.write_rows(0, "Energy Needs in Rural and Informal Settlements: Heating, Lighting and Cooking", [
            "Heating, lighting, cooking, plus phones",
            "Rural: grid but cannot afford to cook on it",
            "Settlement: often no legal connection",
            "Fires jump shack to shack; one in eight cook on wood",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): The Energy Options: Wood, Paraffin, Gas, Candles, Solar and Grid Electricity
        self.next_band(1)
        self.write_rows(1, "The Energy Options: Wood, Paraffin, Gas, Candles, Solar and Grid Electricity", [
            "Wood: free, smoky, time, trees",
            "Paraffin: cheap, poison, tips, fumes",
            "Candles: cheap, dim, fires",
            "Gas, solar, grid; homes stack fuels",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Comparing the Options: Cost, Safety, Health and Convenience
        self.next_band(2)
        self.write_rows(2, "Comparing the Options: Cost, Safety, Health and Convenience", [
            "Cost: start-up and running",
            "Safety: fire, poison, shock",
            "Health and convenience",
            "Environment; coal at the station",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Household choices judged as foolish''",
            "``One criterion only''",
            "``Electricity treated as pollution-free''",
            "``Rural homes assumed unconnected''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): What People Need Energy For
        self.next_band(4)
        self.write_rows(4, "What People Need Energy For", [
            "Fourth need: phone charging",
            "Seven million homes connected",
            "Women and children gather wood",
            "Affordability, not wires",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Six Ways to Get It
        self.next_band(5)
        self.write_rows(5, "Six Ways to Get It", [
            "Free Basic Electricity: lights and radio",
            "Stove standard after fires",
            "Cylinder outside",
            "Solar cannot cook",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Weighing Them Up
        self.next_band(6)
        self.write_rows(6, "Weighing Them Up", [
            "Matrix: no perfect column",
            "Cheap ones are dangerous ones",
            "Change the economics",
            "Choices are rational",
        ], scale=0.9, box=1)

        last = Tex("Three needs, six options, five criteria, and the finding that the cheap options are the dangerous ones, so solutions must change the economics.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
