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


class SpecialisedCellsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Unicellular and Multicellular Organisms
        title = Tex("Unicellular and multicellular").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Unicellular: one cell does every life process (Amoeba, bacteria, yeast)").scale(0.75).shift(UP * 1.30)
        b0_l2 = Tex("Multicellular: division of labour, about 30 trillion human cells").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Volume grows faster than surface: cells must stay small").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Cells can be replaced: skin, blood, gut lining").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Cells Adapted to Their Functions
        self.next_band(1)
        b1_title = Tex("Cells adapted to their functions").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Red blood cell: no nucleus, dented disc, full of haemoglobin").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Muscle cell: long, sliding fibres, many mitochondria").scale(0.9).shift(band_shift(1) + UP * 0.50)
        b1_l3 = Tex("Nerve cell: long axon carries messages far and fast").scale(0.9).shift(band_shift(1) + DOWN * 0.30)
        b1_l4 = Tex("Root hair cell: long extension, large surface for absorption").scale(0.9).shift(band_shift(1) + DOWN * 1.10)
        b1_l5 = Tex("Feature, then function: 'which allows'").scale(0.9).shift(band_shift(1) + DOWN * 1.90)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4, b1_l5):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l5, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Cells, Tissues, Organs and Systems
        self.next_band(2)
        b2_title = Tex("Cells, tissues, organs, systems").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Tissue: similar cells, same function (muscle tissue)").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Organ: different tissues together (the heart)").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("System: organs together (circulatory system)").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("cell, tissue, organ, system, organism").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Stem Cells and the Error Museum
        self.next_band(3)
        b3_title = Tex("Stem cells").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Unspecialised; divides; becomes specialised cells").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Found in embryos and adult bone marrow").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Every cell keeps all 46 chromosomes: different genes active").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Bone marrow transplant: new blood-forming cells").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Stem Cells and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``An organ is a big tissue''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``A tissue is a mix of different cells''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Red blood cells have a nucleus''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Specialised cells have lost DNA''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A One-Person Shop and a Big Company
        self.next_band(5)
        b5_title = Tex("One-person shop and a big company").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("One-person shop = unicellular: every job, one cell").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Big company = multicellular: one job per worker").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("A cell lives through its skin: stay small").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Workers get replaced: wounds heal").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Shaped for the Job
        self.next_band(6)
        b6_title = Tex("Shaped for the job").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Red blood cell: sucked-thin sweet, no nucleus").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Muscle cell: rubber band full of generators").scale(0.9).shift(band_shift(6) + UP * 0.50)
        b6_l3 = Tex("Nerve cell: a wire up to a metre long").scale(0.9).shift(band_shift(6) + DOWN * 0.30)
        b6_l4 = Tex("Root hair: a long finger into the soil").scale(0.9).shift(band_shift(6) + DOWN * 1.10)
        b6_l5 = Tex("This cell has ..., which allows it to ...").scale(0.9).shift(band_shift(6) + DOWN * 1.90)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4, b6_l5):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l5, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): From Brick to Building
        self.next_band(7)
        b7_title = Tex("From brick to building").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Brick = cell; wall = tissue; room = organ").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("House = system; street = organism").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Blank brick = stem cell (bone marrow, embryo)").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Same 46 chromosomes in every brick").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l2, color=YELLOW)))
        self.wait(4)
