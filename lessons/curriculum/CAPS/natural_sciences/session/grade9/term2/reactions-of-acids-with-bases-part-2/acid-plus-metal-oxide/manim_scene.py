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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AcidMetalOxideSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The General Reaction: Acid + Metal Oxide → Salt + Water
        title = Tex("The general reaction").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("acid + metal oxide gives salt + water").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Metal oxides are bases").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("No gas, no fizzing").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Insoluble in water, but reacts with acid").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Balanced Examples
        self.next_band(1)
        b1_title = Tex("Balanced examples").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\mathrm{CuO + H_2SO_4 \rightarrow CuSO_4 + H_2O}").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = MathTex(r"\mathrm{MgO + 2HCl \rightarrow MgCl_2 + H_2O}").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = MathTex(r"\mathrm{Fe_2O_3 + 6HCl \rightarrow 2FeCl_3 + 3H_2O}").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("2+ metal oxides: 2HCl or 1 H2SO4").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Preparing Copper Sulfate Crystals
        self.next_band(2)
        b2_title = Tex("Copper sulfate crystals").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Warm the acid; add CuO in excess").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Filter off the excess").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Evaporate partly; cool slowly").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Do not boil dry").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Industrial Uses and the Error Museum
        self.next_band(3)
        b3_title = Tex("Uses").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Pickling: acid removes rust from steel").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Copper sulfate: fungicide for vineyards").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Ores dissolved in sulfuric acid").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Then galvanise or paint the clean steel").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Industrial Uses and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Salt + hydrogen''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``It fizzes''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``MgO + HCl is balanced''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Boil it dry for crystals''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Vanishing Black Powder
        self.next_band(5)
        b5_title = Tex("The vanishing black powder").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("In water: stays black").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("In warm acid: vanishes, turns blue").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Copper sulfate is the blue").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Metal first, acid part second").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Balancing Workout
        self.next_band(6)
        b6_title = Tex("A balancing workout").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("CuO: already balanced").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("MgO: needs 2HCl").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Rust: 6HCl, 2FeCl3, 3H2O").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Count every element").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The Crystal Recipe
        self.next_band(7)
        b7_title = Tex("The crystal recipe").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Add oxide until some is left over").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Filter").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Evaporate, then cool slowly").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Blue crystals").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l1, color=YELLOW)))
        self.wait(4)
