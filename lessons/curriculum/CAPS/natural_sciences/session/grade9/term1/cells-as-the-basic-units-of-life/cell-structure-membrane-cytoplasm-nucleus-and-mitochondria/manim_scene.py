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


class CellStructureSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Cell Theory and the Microscope
        title = Tex("The cell theory and the microscope").scale(1.0).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("All living things are made of cells; the cell is the unit of life").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("New cells come only from existing cells").scale(0.9).shift(UP * 0.35)
        b0_l3 = MathTex(r"\text{total magnification} = \text{eyepiece} \times \text{objective} = 10 \times 40 = 400\times").scale(0.75).shift(DOWN * 0.60)
        b0_l4 = MathTex(r"1\ \text{mm} = 1\,000\ \mu\text{m}; \quad \text{cheek cell} \approx 60\ \mu\text{m}").scale(0.75).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Cell Membrane and the Cytoplasm
        self.next_band(1)
        b1_title = Tex("Cell membrane and cytoplasm").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Membrane: thin, flexible, selectively permeable").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Oxygen and glucose diffuse in; carbon dioxide diffuses out").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Cytoplasm: jelly-like, mostly water, site of chemical reactions").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Structure first, then function, joined by 'because'").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The Nucleus and DNA
        self.next_band(2)
        b2_title = Tex("The nucleus and DNA").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Nucleus: control centre, holds the DNA instructions").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Nucleus, chromosomes, DNA, genes").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Human body cell: 46 chromosomes in 23 pairs").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Red blood cell: no nucleus, so no division, about 120 days").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Mitochondria and the Organelles
        self.next_band(3)
        b3_title = Tex("Mitochondria: the powerhouses").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("glucose + oxygen gives carbon dioxide + water + energy").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Energy is RELEASED from glucose, never made").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Muscle cell: thousands of mitochondria; skin cell: few").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Chloroplasts: plant cells only").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Mitochondria and the Organelles
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``The nucleus is the brain'' (no reason given)").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Mitochondria make energy''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("A cell wall drawn on an animal cell").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("Magnification written as 400 percent").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Cell Is a Spaza Shop
        self.next_band(5)
        b5_title = Tex("The cell is a spaza shop").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Security gate = cell membrane").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Shop floor = cytoplasm").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Back office with recipe book = nucleus with DNA").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Generator = mitochondrion").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Smaller Than a Grain of Salt
        self.next_band(6)
        b6_title = Tex("Smaller than a grain of salt").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{salt grain} \approx 300\ \mu\text{m}; \quad \text{cheek cell} \approx 60\ \mu\text{m}").scale(0.75).shift(band_shift(6) + UP * 1.30)
        b6_l2 = MathTex(r"10 \times 4 = 40 \qquad 10 \times 10 = 100 \qquad 10 \times 40 = 400").scale(0.75).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Methylene blue: the nucleus turns dark blue").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Start on the lowest objective, then switch up").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Drawing a Cell for Full Marks
        self.next_band(7)
        b7_title = Tex("Drawing a cell for full marks").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Sharp pencil, clear lines, no shading").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Ruled label lines, no arrowheads, no crossing").scale(0.9).shift(band_shift(7) + UP * 0.50)
        b7_l3 = Tex("Heading with name and magnification: Cheek cell, 400x").scale(0.9).shift(band_shift(7) + DOWN * 0.30)
        b7_l4 = Tex("Labels: cell membrane, cytoplasm, nucleus").scale(0.9).shift(band_shift(7) + DOWN * 1.10)
        b7_l5 = Tex("Gate, floor, office, generator. Name the part, say its job.").scale(0.9).shift(band_shift(7) + DOWN * 1.90)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4, b7_l5):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
