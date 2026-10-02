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


class SubscriptsCoefficientsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Subscripts and Coefficients
        title = Tex("Subscript and coefficient").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Subscript: atoms in one particle; part of the formula").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Coefficient: number of particles; in front").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("2 H2O: two molecules, each with 2 H and 1 O").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Change coefficients only; never subscripts").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Counting Atoms in an Equation
        self.next_band(1)
        b1_title = Tex("Counting atoms").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"2\,\mathrm{H_2O}:\ 2 \times 2 = 4 \ \mathrm{H}").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = MathTex(r"3\,\mathrm{CO_2}:\ 3 \times 2 = 6 \ \mathrm{O}").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = MathTex(r"\mathrm{N_2 + 3H_2 \rightarrow 2NH_3}").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("H: 3 x 2 gives 6 on the left; 2 x 3 gives 6 on the right").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Conservation of Atoms and Mass
        self.next_band(2)
        b2_title = Tex("Conservation of mass").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Atoms rearranged; none created or destroyed").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Closed system: mass of products equals mass of reactants").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = MathTex(r"2{,}4 + 1{,}6 = 4{,}0 \ \mathrm{g}").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Open crucible gains mass: oxygen joins from the air").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Checking Whether an Equation Is Balanced and the Error Museum
        self.next_band(3)
        b3_title = Tex("Is it balanced?").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("H2 + O2 gives H2O: O is 2 and 1, not balanced").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("2H2 + O2 gives 2H2O: H 4 and 4, O 2 and 2").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("2Mg + O2 gives 2MgO: balanced").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Never fix it by writing H2O2").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Checking Whether an Equation Is Balanced and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``The 2 in H2O and in 2H2O mean the same''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``2H2O has three hydrogen atoms''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Change a subscript to balance''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Burning destroys mass''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Little Numbers and Big Numbers
        self.next_band(5)
        b5_title = Tex("Little numbers, big numbers").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Little number: what one particle is").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Big number: how many particles").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Three loaves; a loaf is still a loaf").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Change big numbers only").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Stocktake
        self.next_band(6)
        b6_title = Tex("The stocktake").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Big number times little number").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Add an element's atoms across one side").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Table: element, left, right").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Every row must match").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Nothing Is Lost, Nothing Is Gained
        self.next_band(7)
        b7_title = Tex("Nothing lost, nothing gained").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Log: gases escape up the chimney").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Magnesium: oxygen joins from the air").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Sealed box: the scale does not move").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = MathTex(r"16 + 64 = 80; \ 80 - 44 = 36 \ \mathrm{g}").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
