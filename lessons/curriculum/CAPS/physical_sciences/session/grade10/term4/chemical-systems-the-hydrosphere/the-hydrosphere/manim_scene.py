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

# Band-layout whiteboard scene for "The Hydrosphere" (Part 1 — Expert:
# subtopics 1-4; Part 2 — Simplifier: subtopics 5-7). Exporter-safe mobjects
# only; the water-proportions bar chart is hand-built from Rectangles.
# Add-only lifecycle, one band per teaching beat. Band time apportioned to
# subtopics.json (230/240/250/260/180/200/210 of 1570 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TheHydrosphereSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(15)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): what the hydrosphere contains ---
        title = Tex("The Hydrosphere").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("ALL the Earth's water, in three states").scale(1.1).shift(UP * 1.0)
        self.play(Write(d1))
        self.wait(2)
        d2 = Tex("Liquid: oceans, rivers, lakes, GROUNDWATER").scale(1.0).shift(UP * 0.0)
        self.play(Write(d2))
        self.wait(2)
        d3 = Tex("Frozen: ice sheets, glaciers, permafrost").scale(1.0).shift(DOWN * 0.9)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex("Vapour: the invisible gas in the atmosphere").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(d4))
        self.wait(2)
        d5 = Tex("A reservoir SYSTEM — the store, not the moving").scale(0.95).shift(DOWN * 2.8)
        self.play(Write(d5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the proportions, as bars ---
        self.next_band(1)
        b1t = Tex("Where the water sits").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1t))
        self.wait(1.5)
        base_y = band_shift(1) + DOWN * 1.8
        floor = Line(base_y + LEFT * 5.0, base_y + RIGHT * 5.0, stroke_width=4)
        self.play(Create(floor))
        bar1 = Rectangle(width=1.8, height=3.4, color=BLUE).move_to(base_y + LEFT * 3.0 + UP * 1.7)
        l1a = Tex("ocean 97\\%").scale(0.9).move_to(base_y + LEFT * 3.0 + DOWN * 0.5)
        self.play(Create(bar1), Write(l1a))
        self.wait(2)
        bar2 = Rectangle(width=1.8, height=0.35, color=WHITE).move_to(base_y + UP * 0.175)
        l2a = Tex("ice sheets").scale(0.9).move_to(base_y + DOWN * 0.5)
        self.play(Create(bar2), Write(l2a))
        self.wait(2)
        bar3 = Rectangle(width=1.8, height=0.12, color=GREEN).move_to(base_y + RIGHT * 3.0 + UP * 0.06)
        l3a = Tex("reachable fresh").scale(0.85).move_to(base_y + RIGHT * 3.0 + DOWN * 0.5)
        self.play(Create(bar3), Write(l3a))
        self.wait(2)
        b1a = Tex("Under 1\\% is fresh, liquid and reachable").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1a))
        self.play(Create(SurroundingRectangle(b1a, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): into the atmosphere ---
        self.next_band(2)
        b2t = Tex("One water, four spheres").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("Into the AIR: sun drives evaporation").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2a))
        self.wait(2)
        b2b = Tex("Cooling drives condensation $\\to$ clouds").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2b))
        self.wait(2)
        b2c = Tex("Rain, snow, hail return it").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2c))
        self.wait(2)
        b2d = Tex("Warming sends water up; cooling brings it down").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2d))
        self.play(Create(SurroundingRectangle(b2d, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): rock and life ---
        self.next_band(3)
        b3t = Tex("Into the rocks, into the living").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("Rain soaks in $\\to$ groundwater in the pores").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3a))
        self.wait(2)
        b3b = Tex("The polar solvent DISSOLVES minerals as ions").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3b))
        self.wait(2)
        b3c = Tex("...and DEPOSITS them — dripstone caves").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3c))
        self.wait(2)
        b3d = Tex("Your body: roughly 60\\% water").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3d))
        self.wait(2)
        b3e = Tex("Plants exhale vapour: transpiration").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3e))
        self.wait(3)

        # --- Band 4 (subtopic_3): why dam a river ---
        self.next_band(4)
        b4t = Tex("Dams: the case for the wall").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("Rain is seasonal; thirst is constant").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4a))
        self.wait(2)
        b4b = Tex("Store the wet season for the dry one").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4b))
        self.wait(2)
        b4c = Tex("Drinking water, irrigation, hydroelectric power").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4c))
        self.wait(2)
        b4d = Tex("Gariep: largest store; Vaal: Gauteng's taps").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4d))
        self.wait(3)

        # --- Band 5 (subtopic_3): the costs, and how to study them ---
        self.next_band(5)
        b5t = Tex("The price of stored water").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("Upstream: the valley drowns; people moved").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5a))
        self.wait(2)
        b5b = Tex("Downstream: floods flattened, fish blocked").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5b))
        self.wait(2)
        b5c = Tex("Sediment trapped: reservoir fills, plains starve").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5c))
        self.wait(2.5)
        b5d = Tex("Still water: more weeds, more mosquitoes").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5d))
        self.wait(2)
        b5e = Tex("Study it: interviews, literature, above vs below").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5e))
        self.wait(3)

        # --- Band 6 (subtopic_4): testing water ---
        self.next_band(6)
        b6t = Tex("Testing a water sample").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("pH first: 0 — acid, 7 — neutral, 14 — alkali").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.wait(2)
        b6b = Tex("HNO$_3$ then AgNO$_3$: white $\\to$ Cl$^-$").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6b))
        self.wait(2)
        b6c = Tex("HNO$_3$ then Ba(NO$_3$)$_2$: stays white $\\to$ SO$_4^{2-}$").scale(0.95).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6c))
        self.wait(2)
        b6d = Tex("Fizz under acid: carbonate").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6d))
        self.wait(2)
        b6e = Tex("Nitrates/nitrites: fertiliser or sewage warning").scale(0.95).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6e))
        self.play(Create(SurroundingRectangle(b6e, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): purifying water ---
        self.next_band(7)
        b7t = Tex("Purifying: three stages in order").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("1. SEDIMENTATION: let grit settle").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.wait(2)
        b7b = Tex("2. FILTRATION: sand and gravel beds").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7b))
        self.wait(2)
        b7c = Tex("3. DISINFECTION: chlorine — or boil 1 minute").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("Filters catch particles, never microbes").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7d))
        self.wait(2)
        b7e = Tex("Dissolved ions survive filter AND flame").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7e))
        self.play(Create(SurroundingRectangle(b7e, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the bucket planet ---
        self.next_band(8)
        b8t = Tex("The bucket planet").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("All Earth's water in one 10-litre bucket:").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex("About 9,5 litres: salty sea water").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("Most of the rest: locked in ice").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex("Left to share: a few teaspoons").scale(1.1).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8d))
        self.play(Create(SurroundingRectangle(b8d, color=GREEN)))
        self.wait(2)
        b8e = Tex("Groundwater: the sponge a borehole drinks from").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8e))
        self.wait(3)

        # --- Band 9 (subtopic_6): the longest round trip ---
        self.next_band(9)
        b9t = Tex("The longest round trip").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Sea $\\to$ vapour $\\to$ cloud $\\to$ rain on a mountain").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = Tex("Soaks in — dissolves the rock as it creeps").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("Tree drinks it, exhales it: transpiration").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9c))
        self.wait(2)
        b9d = Tex("Girl drinks it: cell chemistry in solution").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9d))
        self.wait(2)
        b9e = Tex("Rivers deliver salt; evaporation leaves it: salty sea").scale(0.9).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9e))
        self.play(Create(SurroundingRectangle(b9e, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): two banks of opinions ---
        self.next_band(10)
        b10t = Tex("The river with two banks of opinions").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("For: banks the flood for the drought").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2)
        b10b = Tex("Against: drowned valleys, tamed river, lost silt").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10b))
        self.wait(2.5)
        b10c = Tex("`Is a dam good or bad?'").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10c))
        self.play(Create(strike(b10c)))
        self.wait(2)
        b10d = Tex("Ask: who gains, who loses, what can soften it").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10d))
        self.play(Create(SurroundingRectangle(b10d, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): the chemist's checkpoint ---
        self.next_band(11)
        b11t = Tex("The chemist's checkpoint").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11t))
        self.wait(2)
        b11a = Tex("Settle it $\\to$ filter it $\\to$ chlorinate or boil").scale(1.0).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11a))
        self.wait(2.5)
        b11b = Tex("Filtering catches particles, never microbes").scale(1.0).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11b))
        self.wait(2)
        b11c = Tex("Boiling kills microbes, never removes salt").scale(1.0).shift(band_shift(11) + DOWN * 0.7)
        self.play(Write(b11c))
        self.wait(2)
        b11d = Tex("The teaspoons are precious — keep them safe").scale(1.0).shift(band_shift(11) + DOWN * 1.7)
        self.play(Write(b11d))
        self.play(Create(SurroundingRectangle(b11d, color=GREEN)))
        self.wait(4)
