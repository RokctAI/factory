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

# Band-layout whiteboard scene for levels-of-ecology-and-ecosystem-components
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex/MathTex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to subtopics.json
# (230/220/220/240/190/190/180 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EcologyLevelsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the six levels
        title = Tex("Ecology: the levels of study").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"\text{organism} \subset \text{population} \subset \text{community} \subset \text{ecosystem} \subset \text{biome} \subset \text{biosphere}").scale(0.75).shift(UP * 1.2)
        l2 = Tex("Population: same species, same place, same time").scale(0.9).shift(UP * 0.2)
        l3 = Tex("Community: all populations (living only)").scale(0.9).shift(DOWN * 0.7)
        l4 = Tex("Ecosystem: community + non-living environment + interactions").scale(0.85).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): biotic and abiotic
        self.next_band(1)
        b1_title = Tex("Biotic and abiotic").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        rows = [
            r"\text{Biotic: alive or once alive: plants, animals, fungi, bacteria, dung, dead leaves}",
            r"\text{Abiotic: never alive: sunlight, temperature, water, air, soil, rock}",
            r"\text{Abiotic shapes biotic: 400 mm rain line, grassland vs Karoo}",
            r"\text{Biotic shapes abiotic: shade, roots hold soil, termites aerate}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.72).shift(band_shift(1) + UP * (1.3 - 0.8 * i))
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # --- Band 2 (subtopic_2): the two-column sort
        self.next_band(2)
        b2_title = Tex("Sorting a dam").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Biotic: fish, reeds, frogs, algae, bacteria, the dead fish").scale(0.9).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex("Abiotic: water, sunlight, temperature, mud, rock, dissolved oxygen").scale(0.85).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("Rule: if it was ever part of an organism, it is biotic").scale(0.9).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("``A dead leaf is abiotic''").scale(0.9).shift(band_shift(2) + DOWN * 1.5)
        for m in (b2_l1, b2_l2, b2_l3):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Write(b2_l4))
        self.play(Create(strike(b2_l4)))
        self.wait(2)

        # --- Band 3 (subtopic_3): habitats
        self.next_band(3)
        b3_title = Tex("Habitat: where an organism lives").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Supplies food, water, shelter, space, conditions").scale(0.9).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("Dassie: rocky koppie. Barbel: muddy bottom. Leopard: riverine bush").scale(0.8).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex("Describe by PHYSICAL features, not by the neighbours").scale(0.9).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = Tex("Habitat (the house) vs ecosystem (the suburb) vs range (the map)").scale(0.8).shift(band_shift(3) + DOWN * 1.8)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): adapting to change
        self.next_band(4)
        b4_title = Tex("Adapting to change").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Daily: nocturnal geckos, bat-eared fox; stomata close at midday").scale(0.8).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("Seasonal: swallows migrate; bats hibernate; bullfrog aestivates").scale(0.8).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex("Marula drops leaves in the dry season: less water lost").scale(0.85).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex("Marks: the change, the response, how it helps survival").scale(0.9).shift(band_shift(4) + DOWN * 1.5)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b4_l4, color=YELLOW)))
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): nesting boxes
        self.next_band(5)
        b5_title = Tex("From one buck to the whole planet").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("One impala: organism. Its herd and kind: population").scale(0.9).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Everything alive there: community").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("Plus sun, rain, soil, air: ecosystem").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("Climate region: biome. Whole living planet: biosphere").scale(0.9).shift(band_shift(5) + DOWN * 1.5)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): actors and stage
        self.next_band(6)
        b6_title = Tex("Actors and the stage").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Actors = biotic: plants, animals, fungi, bacteria, dung, bones").scale(0.85).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("Stage = abiotic: sun, rain, soil, wind, rock, heat").scale(0.9).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Stage decides who acts: rain makes forest, dry makes Karoo").scale(0.85).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("Actors rebuild the stage: shade, roots, termites, elephants").scale(0.85).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): home and the seasons
        self.next_band(7)
        b7_title = Tex("Home and the seasons").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        rows = [
            r"\text{Habitat = home, described by what the place is like}",
            r"\text{Hide (nocturnal), leave (migrate), sleep (hibernate, aestivate)}",
            r"\text{Bodies built for it: leaf drop, bulbs, fat, thick coats}",
            r"\text{Always finish: how does it help survival?}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.85).shift(band_shift(7) + UP * (1.3 - 0.75 * i))
            self.play(Write(m))
            self.wait(2.0)
        b7_l5 = Tex("Six boxes. Two columns. Home, change, response, benefit.").scale(0.9).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
