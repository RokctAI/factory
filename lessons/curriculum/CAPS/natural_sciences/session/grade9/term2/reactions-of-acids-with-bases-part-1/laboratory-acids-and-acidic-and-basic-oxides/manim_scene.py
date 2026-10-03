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


class LabAcidsOxidesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Hydrochloric Acid and Sulfuric Acid
        title = Tex("Two laboratory acids").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Hydrochloric acid, HCl: fumes when concentrated").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Sulfuric acid, H2SO4: oily, dehydrating").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Both strong; always add acid to water").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = MathTex(r"\mathrm{Mg + 2HCl \rightarrow MgCl_2 + H_2}").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Uses of Hydrochloric and Sulfuric Acid
        self.next_band(1)
        b1_title = Tex("Uses").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("HCl: stomach, pool acid, cleaning steel").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("H2SO4: fertilisers, car batteries").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("H2SO4: mining and refining").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Sulfur from Secunda becomes acid").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Acidic and Basic Compounds
        self.next_band(2)
        b2_title = Tex("Acidic and basic").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\mathrm{SO_2 + H_2O \rightarrow H_2SO_3}").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = MathTex(r"\mathrm{CaO + H_2O \rightarrow Ca(OH)_2}").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Bases: metal oxides, hydroxides, carbonates").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = MathTex(r"\mathrm{CaCO_3 + 2HCl \rightarrow CaCl_2 + H_2O + CO_2}").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Classifying in Practice and the Error Museum
        self.next_band(3)
        b3_title = Tex("Classifying").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Acidic: SO2, CO2, H2SO4, HCl").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Basic: MgO, KOH, CaCO3, Na2O").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = MathTex(r"\mathrm{Ca(OH)_2 + CO_2 \rightarrow CaCO_3 + H_2O}").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Opposites react").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Classifying in Practice and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``No smell means safe''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Carbonates are acids''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Insoluble oxides are not bases''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``All oxides are acidic''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Two Famous Acids
        self.next_band(5)
        b5_title = Tex("Two famous acids").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("HCl: stomach and pool acid").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("H2SO4: car battery and fertiliser").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Sugar turns to black carbon").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Acid into water, never water into acid").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Acid Makers and Base Makers
        self.next_band(6)
        b6_title = Tex("Acid makers, base makers").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Non-metals make acids").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Metals make bases").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Oxides, hydroxides, carbonates").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Carbonates fizz").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The Formula Cheat Sheet
        self.next_band(7)
        b7_title = Tex("Formula cheat sheet").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("H in front: acid").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Non-metal with oxygen: acidic").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Metal with O, OH or CO3: base").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Limewater turns milky").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
