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

# Band-layout whiteboard scene for "Writing Chemical Formulae" (Part 1
# Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe
# mobjects only; write-only reveals; camera moves down band by band. Band
# time apportioned to subtopics.json (230/240/250/270/160/160/160 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class WritingChemicalFormulaeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the one law ---
        title = Tex("Writing Chemical Formulae").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("The one law: total charge must be ZERO").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(2)
        b0_l2 = Tex("metals give electrons: cations $+$").scale(1.0).shift(UP * 0.2)
        b0_l3 = Tex("non-metals take electrons: anions $-$").scale(1.0).shift(DOWN * 0.6)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = MathTex(r"NaCl: \; +1 - 1 = 0 \qquad MgO: \; +2 - 2 = 0").scale(1.0).shift(DOWN * 1.6)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = MathTex(r"MgCl_2: \; +2 -1 -1 = 0").scale(1.05).shift(DOWN * 2.6)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): calcium chloride by crossover ---
        self.next_band(1)
        b1_t = Tex("Calcium chloride, by crossover").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"Ca^{2+} \qquad Cl^{-}").scale(1.2).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        cr1 = Arrow(band_shift(1) + UP * 0.8 + LEFT * 1.0, band_shift(1) + UP * 0.0 + RIGHT * 1.0,
                    buff=0, color=YELLOW)
        cr2 = Arrow(band_shift(1) + UP * 0.8 + RIGHT * 1.0, band_shift(1) + UP * 0.0 + LEFT * 1.0,
                    buff=0, color=YELLOW)
        self.play(Create(cr1), Create(cr2))
        b1_l2 = Tex("cross the SIZES of the charges").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"CaCl_2").scale(1.3).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = MathTex(r"\text{audit: } +2 + 2 \times (-1) = 0").scale(1.0).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the two safety rules ---
        self.next_band(2)
        b2_t = Tex("Safety rules of the crossover").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"Mg^{2+} + O^{2-} \to Mg_2O_2").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.play(Create(strike(b2_l1)))
        self.wait(2)
        b2_l2 = Tex("simplify to the smallest ratio: MgO").scale(1.05).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = MathTex(r"Ca_1Cl_2 \quad \text{(never show a 1)}").scale(1.05).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.play(Create(strike(b2_l3)))
        self.wait(2)
        b2_l4 = Tex("finish every formula with the charge audit").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): ammonium sulphate and the brackets ---
        self.next_band(3)
        b3_t = Tex("Ammonium sulphate: the bracket rule").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"NH_4^{+} \quad \text{and} \quad SO_4^{2-}").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("two ammoniums settle one sulphate").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"(NH_4)_2SO_4").scale(1.25).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = MathTex(r"NH_{42}SO_4 \quad \text{(42 hydrogens!)}").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.play(Create(strike(b3_l4)))
        self.wait(2)
        b3_l5 = Tex("count: 2 N, 8 H, 1 S, 4 O; $+2-2=0$").scale(1.0).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_4): iron(III) oxide ---
        self.next_band(4)
        b4_t = Tex("Iron(III) oxide: the numeral is the charge").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"Fe^{3+} \quad \text{and} \quad O^{2-}").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\text{LCM of 3 and 2 is 6: } 2Fe, \; 3O").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"Fe_2O_3").scale(1.3).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = MathTex(r"\text{audit: } 2(+3) + 3(-2) = 0").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("iron(II) oxide is FeO — a DIFFERENT substance").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): the five-step method ---
        self.next_band(5)
        b5_t = Tex("The five-step method").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("1. name both ions (numerals, -ate endings)").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(1.5)
        b5_l2 = Tex("2. write them WITH their charges").scale(0.95).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l2))
        self.wait(1.5)
        b5_l3 = Tex("3. find the neutral ratio — logic or crossover").scale(0.95).shift(band_shift(5) + DOWN * 0.2)
        self.play(Write(b5_l3))
        self.wait(1.5)
        b5_l4 = Tex("4. simplify, bracket multiplied teams, hide 1s").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l4))
        self.wait(1.5)
        b5_l5 = Tex("5. audit charges and atoms").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2)
        b5_l6 = Tex("a wrong formula cannot be saved by balancing").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): the till must balance ---
        self.next_band(6)
        b6_t = Tex("The till must balance").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("givers: Na 1, Ca 2, Al 3 — left positive").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("takers: Cl 1, O 2, N 3 — left negative").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("calcium hands out two; each chloride").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = MathTex(r"\text{takes one: } CaCl_2, \;\; +2-1-1=0").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2.5)
        b6_l5 = Tex("swap the numbers across, cancel down, no 1s").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_6): the team rides in one taxi ---
        self.next_band(7)
        b7_t = Tex("The team rides in one taxi").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex(r"ammonium NH$_4^+$: five atoms, ONE passenger").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("two groups travelling? brackets are the taxi:").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        b7_l3 = MathTex(r"(NH_4)_2SO_4").scale(1.2).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("outside 2 multiplies everything inside:").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        b7_l5 = Tex("2 N and 8 H; one sulphate rides bracket-free").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_7): the name whispers the charge ---
        self.next_band(8)
        b8_t = Tex("When the name whispers the charge").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("iron(III) means iron handing out three").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"\text{fit into 6: } Fe_2O_3 \;\; \text{— rust}").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2)
        b8_l3 = Tex("iron(II) oxide: FeO, black and different —").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = Tex("``iron is iron'' loses the mark").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("recipe: ions, charges, zero mix, tidy, audit").scale(1.0).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(4)
