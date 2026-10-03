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

# Band-layout whiteboard scene for feeding-relationships (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex/MathTex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (210/240/230/230/190/190/180 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FeedingRelationshipsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): producers
        title = Tex("Feeding relationships").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = Tex("Producer: makes its own food from inorganic substances using sunlight").scale(0.8).shift(UP * 1.2)
        l2 = Tex("Green plants, algae, phytoplankton, some bacteria (autotrophs)").scale(0.85).shift(UP * 0.2)
        l3 = Tex("Only producers bring energy into the living world").scale(0.9).shift(DOWN * 0.7)
        l4 = Tex("``A mushroom is a producer''").scale(0.9).shift(DOWN * 1.7)
        for m in (l1, l2, l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(l4))
        self.play(Create(strike(l4)))
        self.wait(2)

        # --- Band 1 (subtopic_2): consumers
        self.next_band(1)
        b1_title = Tex("Consumers: classified by diet").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        rows = [
            r"\text{Herbivore: plants only. Impala, zebra, locust. Flat ridged molars}",
            r"\text{Carnivore: animals only. Lion, eagle, spider. Canines, shearing teeth}",
            r"\text{Omnivore: both. Baboon, bushpig, human. Mixed teeth}",
            r"\text{Predator hunts; scavenger eats the dead; insectivore eats insects}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.72).shift(band_shift(1) + UP * (1.3 - 0.8 * i))
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # --- Band 2 (subtopic_3): decomposers
        self.next_band(2)
        b2_title = Tex("Decomposers close the loop").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Bacteria and fungi: break dead material into simple substances").scale(0.85).shift(band_shift(2) + UP * 1.3)
        b2_l2 = MathTex(r"\text{dead matter} \rightarrow \text{CO}_2 \text{ to air} + \text{minerals to soil} \rightarrow \text{producers}").scale(0.8).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("Detritivores help: earthworms, millipedes, termites, dung beetles").scale(0.85).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("Compost heap: warm inside because the decomposers respire").scale(0.85).shift(band_shift(2) + DOWN * 1.5)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_3/4): three roles at a carcass + the arrow
        self.next_band(3)
        b3_title = Tex("Three roles at a carcass; one arrow rule").scale(1.1).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Scavenger (vulture) eats flesh: a consumer, NOT a decomposer").scale(0.85).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("Detritivore (maggots, worms) shreds scraps; decomposer finishes").scale(0.85).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"\text{grass} \rightarrow \text{impala} \rightarrow \text{lion}").scale(1.1).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = Tex("Arrow = ``is eaten by'' = energy flows to the eater").scale(0.9).shift(band_shift(3) + DOWN * 1.8)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): other relationships + error museum
        self.next_band(4)
        b4_title = Tex("Partners, and the error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Predator / prey: lion and impala. Parasite / host: tick and cow").scale(0.85).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("Mutualism: oxpecker and giraffe; bee and flower").scale(0.9).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex("``Vultures are decomposers''").scale(0.9).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex("``The arrow points from the lion to the impala''").scale(0.9).shift(band_shift(4) + DOWN * 1.5)
        for m in (b4_l1, b4_l2):
            self.play(Write(m))
            self.wait(2.3)
        for m in (b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the restaurant
        self.next_band(5)
        b5_title = Tex("The kitchen, the eaters and the cleaners").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Kitchen = producers: grass, trees, reeds, algae. Only they can cook").scale(0.8).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Eaters = consumers: plant menu, meat menu, or both").scale(0.9).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("Cleaners = decomposers: bacteria and fungi after closing").scale(0.9).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("A mushroom is a cleaner, not a kitchen").scale(0.95).shift(band_shift(5) + DOWN * 1.5)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): teeth
        self.next_band(6)
        b6_title = Tex("Teeth tell the story").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Flat ridged millstones at the back: herbivore").scale(0.9).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("Long canines, scissor cheek teeth: carnivore").scale(0.9).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Mixed toolkit, like your own mouth: omnivore").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("Diet gives the label, never size: a hippo is a herbivore").scale(0.85).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): nothing is wasted
        self.next_band(7)
        b7_title = Tex("Nothing is wasted").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        rows = [
            r"\text{Decomposers dissolve the dead; minerals to soil, CO}_2 \text{ to air}",
            r"\text{Compost heap: warm, crumbly, months not years}",
            r"\text{Addo dung beetle: clears dung AND fertilises soil}",
            r"\text{Vulture eats, maggots shred, bacteria and fungi finish}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.8).shift(band_shift(7) + UP * (1.3 - 0.75 * i))
            self.play(Write(m))
            self.wait(2.0)
        b7_l5 = Tex("Kitchen cooks, eaters eat, cleaners return it all to the kitchen.").scale(0.85).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
