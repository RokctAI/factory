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

# Band-layout whiteboard scene for cost-appearance-and-choosing-materials (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/150/160/120/120/120 of 820 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CostAppearanceAndChoosingMaterialsSession(MovingCameraScene):
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Cost and availability
        self.write_rows(0, "Cost and availability", [
            "Cost: rarity, processing energy, transport, demand",
            "Copper not gold; aluminium cables beat theft",
            "Recycled aluminium: about 5\\% of the energy",
            "Judge cost over the whole life",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Colour, texture, appearance
        self.next_band(1)
        self.write_rows(1, "Colour, texture, appearance", [
            "Colour can work: white roofs, safety vests, wire codes",
            "Smooth: easy to clean; rough: grip; soft: comfort",
            "Culture and taste: Ndebele paint, beadwork, shweshwe",
            "Coatings balance looks and properties",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Weighing up a choice
        self.next_band(2)
        self.write_rows(2, "Weighing up a choice", [
            "Thatch: cheap locally, insulates, quiet; burns",
            "Iron sheets: cheap, fireproof, rain tanks; hot, noisy",
            "Tiles: durable, fireproof; heavy, costly",
            "Name needs, compare, explain trade-offs, justify",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The strongest material is always best''",
            "``The cheapest material is always best value''",
            "``Colour and texture do not matter''",
            "``There is only one right answer''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.78).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Can we afford it?
        self.next_band(4)
        self.write_rows(4, "Can we afford it?", [
            "Gold: brilliant but too pricey; use copper",
            "Recycling aluminium saves energy and money",
            "Local materials: often cheapest",
            "Think long-term",
        ], scale=0.88, box=1)

        # --- Band 5 (subtopic_5): Looks and feel
        self.next_band(5)
        self.write_rows(5, "Looks and feel", [
            "White roof: cooler; orange vest: seen",
            "Smooth: easy to clean; rough: grip; soft: comfy",
            "Ndebele patterns, beadwork, shweshwe",
            "Paint steel: looks good and stops rust",
        ], scale=0.82, box=0)

        # --- Band 6 (subtopic_6): The roof decision
        self.next_band(6)
        self.write_rows(6, "The roof decision", [
            "Thatch: cheap, cool, quiet; fire risk",
            "Iron: cheap, fireproof, rain tanks; hot and noisy",
            "Tiles: durable, fireproof; heavy, costly",
            "No single right answer: give reasons",
        ], scale=0.82, box=3)

        last = Tex("Properties first, then cost, looks, feel and what is available.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
