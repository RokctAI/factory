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


class PlantAnimalCellSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Cell Wall
        title = Tex("The cell wall").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Cellulose wall outside the membrane: support and shape").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Fully permeable: does NOT control entry (the membrane does)").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Onion cells: rectangular bricks in rows").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Animal cells: membrane only, irregular shape").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Large Permanent Vacuole
        self.next_band(1)
        b1_title = Tex("The large permanent vacuole").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Cell sap: water, sugars, salts, pigments").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Full vacuole: turgid, firm; shrunken vacuole: flaccid, wilted").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Pushes the nucleus to the edge of the cell").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Animal cells: small temporary vacuoles or none").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Chloroplasts and Photosynthesis
        self.next_band(2)
        b2_title = Tex("Chloroplasts and photosynthesis").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Chlorophyll absorbs light; leaves look green").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("carbon dioxide + water gives glucose + oxygen (sunlight)").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Green parts only: roots and onion bulbs have NONE").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Both cell types keep mitochondria: all living cells respire").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): The Comparison Table and the Error Museum
        self.next_band(3)
        b3_title = Tex("The comparison table").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Both: membrane, cytoplasm, nucleus, mitochondria").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Plant only: cell wall, large vacuole, chloroplasts").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Plant: box shape, nucleus at edge; animal: round, nucleus central").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Write a word in every box: 'none' earns the mark").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): The Comparison Table and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``The cell wall controls what enters''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Plant cells have no mitochondria''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``All plant cells have chloroplasts''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("A plant cell drawn as a circle").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Brick House and a Tent
        self.next_band(5)
        b5_title = Tex("A brick house and a tent").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Brick walls = cell wall (cellulose)").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Door = cell membrane, in both").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Tent = animal cell: flexible, no bricks").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Bricks have gaps: the door still chooses").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Water Balloon Inside
        self.next_band(6)
        b6_title = Tex("The water balloon inside").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Big balloon = large permanent vacuole of cell sap").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Full: turgid and firm. Empty: flaccid and wilted.").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Limp lettuce + cold water = crisp again").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Red cabbage colour lives in the sap").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The Green Solar Panels
        self.next_band(7)
        b7_title = Tex("The green solar panels").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Chloroplasts: chlorophyll + sunlight make glucose and oxygen").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Only green parts: no panels on roots or onion bulbs").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Panels do not replace the generator: plants also respire").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Plant stands still: bricks, balloon, panels. Animal eats: none.").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
