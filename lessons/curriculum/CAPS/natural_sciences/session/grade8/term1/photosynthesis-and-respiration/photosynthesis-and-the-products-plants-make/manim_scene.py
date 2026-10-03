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

# Band-layout whiteboard scene for photosynthesis-and-the-products-plants-make
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex/MathTex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to subtopics.json
# (220/220/240/230/190/190/180 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PhotosynthesisProductsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the word equation
        title = Tex("Photosynthesis: the word equation").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"\text{carbon dioxide} + \text{water} \xrightarrow{\;\text{sunlight, chlorophyll}\;} \text{glucose} + \text{oxygen}").scale(0.85).shift(UP * 1.2)
        l2 = Tex("Raw materials on the LEFT: used up").scale(0.95).shift(UP * 0.2)
        l3 = Tex("Conditions at the ARROW: sunlight and chlorophyll, not used up").scale(0.9).shift(DOWN * 0.7)
        l4 = Tex("CO$_2$ in through stomata; water up the xylem; O$_2$ out").scale(0.9).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): the leaf and the chloroplast
        self.next_band(1)
        b1_title = Tex("The leaf is built for the job").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        rows = [
            r"\text{Broad and flat: more light} \qquad \text{Thin: short path for gases}",
            r"\text{Stomata underneath: CO}_2 \text{ in, O}_2 \text{ out}",
            r"\text{Chloroplast holds chlorophyll: the SITE of photosynthesis}",
            r"\text{Variegated leaf: starch only where it was green}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.85).shift(band_shift(1) + UP * (1.3 - 0.8 * i))
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # --- Band 2 (subtopic_3): the starch test
        self.next_band(2)
        b2_title = Tex("Testing a leaf for starch").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("1. Destarch 48 h in the dark \\quad 2. Light, with one leaf covered").scale(0.85).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex("3. Boil in water: kill, soften \\quad 4. Boil in ethanol: remove green").scale(0.85).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("Ethanol in a WATER BATH, flame off: flammable").scale(0.9).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("5. Warm water \\quad 6. White tile, iodine: blue-black = starch").scale(0.85).shift(band_shift(2) + DOWN * 1.5)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_3): results and conclusion
        self.next_band(3)
        b3_title = Tex("Results").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Leaf in light: blue-black, starch present, photosynthesis occurred").scale(0.85).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("Covered leaf: yellow-brown, no starch, no light = no photosynthesis").scale(0.85).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex("Conclusion: light AND chlorophyll are necessary").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = Tex("Observation alone earns one mark; the 'therefore' earns the rest").scale(0.85).shift(band_shift(3) + DOWN * 1.8)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): what glucose becomes + error museum
        self.next_band(4)
        b4_title = Tex("From glucose to everything else").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Starch: storage (maize, potato) \\quad Cellulose: cell walls (cotton, paper)").scale(0.8).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("Sucrose: transport in phloem (sugar cane) \\quad Oils: seeds (sunflower)").scale(0.8).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex("Protein: glucose compounds + NITRATES from the soil").scale(0.9).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex("``Plants take food from the soil''").scale(0.9).shift(band_shift(4) + DOWN * 1.5)
        for m in (b4_l1, b4_l2, b4_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b4_l4))
        self.play(Create(strike(b4_l4)))
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the plant's kitchen
        self.next_band(5)
        b5_title = Tex("The plant's kitchen").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Ingredients: carbon dioxide from the air, water from the roots").scale(0.85).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Energy: sunlight \\quad Cook: chlorophyll (never eaten)").scale(0.9).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("Out of the kitchen: glucose (food) and oxygen (your next breath)").scale(0.85).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("The only kitchen on Earth that cooks from air and light").scale(0.85).shift(band_shift(5) + DOWN * 1.5)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): the pantry test
        self.next_band(6)
        b6_title = Tex("The pantry test").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Glucose is packed into starch: the pantry").scale(0.95).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("Iodine: tea-brown on nothing, ink-black on starch").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Boil in water, wash out green in ethanol, tile, iodine").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("Ethanol tube stands in hot water, flame OFF").scale(0.95).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): the sugar factory
        self.next_band(7)
        b7_title = Tex("What the plant builds with its sugar").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        rows = [
            r"\text{Starch: the pantry} \qquad \text{Cellulose: the bricks}",
            r"\text{Sucrose: the delivery van} \qquad \text{Oil: the long-life battery}",
            r"\text{Protein: sugar + nitrates from the soil}",
            r"\text{Soil gives water and minerals, never food}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.85).shift(band_shift(7) + UP * (1.3 - 0.75 * i))
            self.play(Write(m))
            self.wait(2.0)
        b7_l5 = Tex("Air + water + light = sugar. Sugar + minerals = a plant.").scale(0.9).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
