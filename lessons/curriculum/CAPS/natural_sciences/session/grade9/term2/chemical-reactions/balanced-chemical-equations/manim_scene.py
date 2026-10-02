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


class BalancedEquationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Why Equations Must Be Balanced
        title = Tex("Why balance?").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Atoms are never created or destroyed").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("H2 + O2 gives H2O: one O missing").scale(0.9).shift(UP * 0.35)
        b0_l3 = MathTex(r"\mathrm{2H_2 + O_2 \rightarrow 2H_2O}").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Change coefficients only").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): A Step-by-Step Balancing Method
        self.next_band(1)
        b1_title = Tex("The method").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Word equation, then correct formulae").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Stocktake table: element, left, right").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("One element at a time; O and H last; recount").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = MathTex(r"\mathrm{CH_4 + 2O_2 \rightarrow CO_2 + 2H_2O}").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Balancing Harder Equations
        self.next_band(2)
        b2_title = Tex("Harder equations").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("O in 2s and 3s: use 6").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = MathTex(r"\mathrm{4Fe + 3O_2 \rightarrow 2Fe_2O_3}").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = MathTex(r"\mathrm{C_3H_8 + 5O_2 \rightarrow 3CO_2 + 4H_2O}").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = MathTex(r"\mathrm{2H_2O_2 \rightarrow 2H_2O + O_2}").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Checking, Presenting and the Error Museum
        self.next_band(3)
        b3_title = Tex("Check and present").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("State symbols: (s), (l), (g), (aq)").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = MathTex(r"\mathrm{2Na + Cl_2 \rightarrow 2NaCl}").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("4H2 + 2O2 gives 4H2O: divide by 2").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Smallest whole numbers").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Checking, Presenting and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Change H2O to H2O2''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Oxygen gas is O''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``A number inside the formula''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``No need to recount''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Fair Trade
        self.next_band(5)
        b5_title = Tex("A fair trade").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Everything on the left turns up on the right").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Count each kind of atom").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Big numbers change; little numbers are locked").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Hydrogen and oxygen: 2 to 1").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Recipe for Balancing
        self.next_band(6)
        b6_title = Tex("The recipe").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Words, formulae, table").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Fix one element at a time").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Oxygen and hydrogen last").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Recount after every change").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Trickier Ones and Final Checks
        self.next_band(7)
        b7_title = Tex("Trickier ones, final checks").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Formulae right: O2, H2, N2, Cl2").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Every element matches").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Smallest whole numbers").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Then hand it in").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l2, color=YELLOW)))
        self.wait(4)
