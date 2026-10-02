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


class PeriodicTableReviewSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Elements, Symbols and Names
        title = Tex("Elements and symbols").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("118 elements; symbol: capital first, small second").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Co is cobalt; CO is carbon monoxide").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Latin: Na sodium, K potassium, Fe iron, Cu copper").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Ag silver, Au gold, Pb lead, Hg mercury").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Groups and Periods
        self.next_band(1)
        b1_title = Tex("Groups and periods").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("18 groups (columns): similar properties").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("7 periods (rows): metal to non-metal across").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Group 1 alkali metals; Group 2 alkaline earth metals").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Group 17 halogens; Group 18 noble gases").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Metals, Non-metals and Semi-metals
        self.next_band(2)
        b2_title = Tex("Metals, non-metals, semi-metals").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Metals (left): shiny, conduct, malleable, ductile").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Non-metals (right): dull, poor conductors, brittle").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Semi-metals on the staircase: B, Si, Ge, As, Sb, Te").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Hydrogen is a non-metal; mercury is a liquid metal").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Atomic Number, Mass Number and the Error Museum
        self.next_band(3)
        b3_title = Tex("Atomic number and mass number").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Z: protons. A: protons + neutrons.").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Neutral atom: electrons equal protons").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Na: Z 11, A 23; neutrons 23 - 11 gives 12").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Fe: Z 26, A 56; neutrons 56 - 26 gives 30").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Atomic Number, Mass Number and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Co and CO mean the same''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Atomic number counts protons and neutrons''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Same period, similar properties''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Hydrogen is a metal''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Street Map of the Elements
        self.next_band(5)
        b5_title = Tex("A street map of the elements").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Gates: symbols, some in Latin").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Streets down: groups, families alike").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Roads across: periods, metal to non-metal").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Street 18: the quiet noble gases").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Reading One Block
        self.next_band(6)
        b6_title = Tex("Reading one block").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Left of the staircase: metals").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Right of the staircase: non-metals").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("On the staircase: semi-metals such as silicon").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Check with properties: shiny, conducts, bends").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Counting What Is Inside an Atom
        self.next_band(7)
        b7_title = Tex("Counting inside an atom").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Protons: the atomic number").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Electrons: same as protons").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Neutrons: mass number minus atomic number").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Al: 13 protons, 13 electrons, 14 neutrons").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
