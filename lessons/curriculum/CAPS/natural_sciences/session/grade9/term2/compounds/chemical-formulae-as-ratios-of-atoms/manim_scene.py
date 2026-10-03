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


class ChemicalFormulaeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Elements, Compounds and Molecules
        title = Tex("Elements, compounds, molecules").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Element: one kind of atom, e.g. Fe, O2").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Compound: elements chemically combined in a fixed ratio").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("New properties: sodium + chlorine give table salt").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Molecule: atoms bonded together; NaCl is a lattice").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Reading a Chemical Formula
        self.next_band(1)
        b1_title = Tex("Reading a formula").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("A subscript belongs to the symbol before it").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("H2O: 2 H, 1 O.   CO2: 1 C, 2 O").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Ca(OH)2: 1 Ca, 2 O, 2 H").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Al2(SO4)3: 2 Al, 3 S, 12 O").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Formulae as Fixed Ratios
        self.next_band(2)
        b2_title = Tex("Formulae as fixed ratios").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("H2O: 2 to 1;  CO2: 1 to 2").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Fe2O3: 2 to 3;  NaCl: 1 to 1").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Law of constant composition: always the same ratio").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("H2O is water; H2O2 is hydrogen peroxide").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Counting Atoms in Formulae and the Error Museum
        self.next_band(3)
        b3_title = Tex("Counting atoms").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\mathrm{H_2SO_4}: 2 + 1 + 4 = 7").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = MathTex(r"\mathrm{CaCO_3}: 1 + 1 + 3 = 5").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = MathTex(r"\mathrm{C_6H_{12}O_6}: 6 + 12 + 6 = 24").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Glucose: 3 elements, 24 atoms").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Counting Atoms in Formulae and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``O2 is a compound''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Ca(OH)2 has one hydrogen atom''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``CO2 has two carbon atoms''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Change H2O to H2O2 to balance''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Recipes in Letters and Numbers
        self.next_band(5)
        b5_title = Tex("Recipes in letters and numbers").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Symbols: which ingredients").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Little numbers: how many of each").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Compound: nothing like its ingredients").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("O2 is an element: two atoms, one kind").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Little Number Belongs to the Letter Before It
        self.next_band(6)
        b6_title = Tex("Whose number is it?").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("The little number belongs to the letter before it").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("No number means one").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Brackets are packets: multiply everything inside").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Read aloud: element, then number").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Same Letters, Different Recipe
        self.next_band(7)
        b7_title = Tex("Same letters, different recipe").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Water is always 2 to 1").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("H2O water; H2O2 hydrogen peroxide").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("CO2 breathed out; CO deadly").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Never change a subscript").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
