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

# Band-layout whiteboard scene for commercial-farming (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/190/170/110/110/110 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CommercialFarmingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What Commercial Farming Is
        self.write_rows(0, "What Commercial Farming Is", [
            "Farming to sell for a profit",
            "Profit: income minus costs",
            "Large farms that specialise",
            "Exports: citrus, grapes, wool",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Machines, Workers and Water
        self.next_band(1)
        self.write_rows(1, "Machines, Workers and Water", [
            "Tractors, planters, harvesters",
            "Many paid workers",
            "Irrigation: pipes and sprinklers",
            "Loans and insurance",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): From Farm to Market
        self.next_band(2)
        self.write_rows(2, "From Farm to Market", [
            "Silos store the grain",
            "Mills make maize meal",
            "Fruit packed and cooled",
            "Ships to other countries",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Grown mainly for the family''",
            "``Profit is all the money''",
            "``Commercial farms only grow crops''",
            "``All products stay in South Africa''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Farming to Sell
        self.next_band(4)
        self.write_rows(4, "Farming to Sell", [
            "Sell for profit",
            "Big farms",
            "Specialise",
            "Export",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Big Machines
        self.next_band(5)
        self.write_rows(5, "Big Machines", [
            "Tractors",
            "Harvesters",
            "Workers",
            "Irrigation",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): To the Shops
        self.next_band(6)
        self.write_rows(6, "To the Shops", [
            "Silos",
            "Mills",
            "Markets",
            "Ships",
        ], scale=0.9, box=0)

        last = Tex("Commercial farmers grow crops and raise animals on large farms to sell for a profit.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
