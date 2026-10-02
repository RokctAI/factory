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

# Band-layout whiteboard scene for balance-and-disruption-in-ecosystems
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex/MathTex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to subtopics.json
# (230/220/230/230/190/180/190 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BalanceDisruptionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): dynamic balance
        title = Tex("Balance in an ecosystem is dynamic").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"\text{grass} \uparrow \Rightarrow \text{impala} \uparrow \Rightarrow \text{lions} \uparrow \Rightarrow \text{impala} \downarrow \Rightarrow \text{lions} \downarrow \Rightarrow \text{impala} \uparrow").scale(0.75).shift(UP * 1.2)
        l2 = Tex("Predator wave lags the prey wave; neither line reaches zero").scale(0.85).shift(UP * 0.2)
        l3 = Tex("Limiting factors: food, water, space, predators, disease, competition").scale(0.8).shift(DOWN * 0.7)
        l4 = Tex("Carrying capacity: the largest population the area can support long term").scale(0.8).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): natural disruptions
        self.next_band(1)
        b1_title = Tex("Natural disruptions: usually temporary").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        rows = [
            r"\text{Drought: SA about 460 mm/yr vs world 860 mm. Kruger 2015--16}",
            r"\text{Flood: drowns and strips, but deposits silt, fills wetlands}",
            r"\text{Fire: needed in fynbos at the right frequency; harmful too often}",
            r"\text{Disease: rinderpest 1890s. Recovery: months, years, decades}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.75).shift(band_shift(1) + UP * (1.3 - 0.8 * i))
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # --- Band 2 (subtopic_3): human disruptions
        self.next_band(2)
        b2_title = Tex("Human disruptions: larger, faster, often permanent").scale(1.05).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Habitat destruction: ploughing, building, draining, mining (the largest)").scale(0.78).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex("Pollution: sewage and fertiliser (Vaal), acid mine drainage, SO$_2$").scale(0.8).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("Overharvesting: perlemoen, rock lobster, rhino poaching").scale(0.85).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("Overgrazing and dongas; alien species; climate change (Day Zero)").scale(0.8).shift(band_shift(2) + DOWN * 1.5)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(b2_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_3): eutrophication chain
        self.next_band(3)
        b3_title = Tex("Fertiliser to dead fish in four steps").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{nitrates, phosphates} \rightarrow \text{algal bloom}").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"\rightarrow \text{light blocked, plants and algae die}").scale(0.95).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"\rightarrow \text{bacteria decompose, use up oxygen}").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = MathTex(r"\rightarrow \text{fish suffocate: eutrophication}").scale(0.95).shift(band_shift(3) + DOWN * 1.8)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): aliens and the five steps
        self.next_band(4)
        b4_title = Tex("Alien invaders and the five-step case study").scale(1.05).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Alien = introduced. Invasive = spreading and harming").scale(0.9).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("Hyacinth, black wattle, pine, lantana; Working for Water since 1995").scale(0.8).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex("1 name and classify; 2 hit first; 3 hit next; 4 cost to people; 5 response + why").scale(0.72).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex("``Balance means nothing changes''").scale(0.9).shift(band_shift(4) + DOWN * 1.5)
        for m in (b4_l1, b4_l2, b4_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b4_l4))
        self.play(Create(strike(b4_l4)))
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the seesaw
        self.next_band(5)
        b5_title = Tex("The seesaw").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Impala end down, lion end down a year later, round it goes").scale(0.85).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Nobody falls off: a wobble that fixes itself").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("Limits stop it tipping: food, water, space, predators, disease").scale(0.85).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("Too many elephants for the trees: past carrying capacity").scale(0.85).shift(band_shift(5) + DOWN * 1.5)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): the bush fights back
        self.next_band(6)
        b6_title = Tex("When the bush fights back").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Drought: grass dies, herds crash, rain returns, herds recover").scale(0.85).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("Fire: medicine in the right dose, poison in the wrong one").scale(0.9).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Flood leaves mud and fills wetlands; disease knocks and passes").scale(0.85).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("Months for grass, years for drought, decades for forest").scale(0.9).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): the guest who will not leave
        self.next_band(7)
        b7_title = Tex("The guest who will not leave").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        rows = [
            r"\text{Human knocks often do not heal: plough, pour, poach, overgraze}",
            r"\text{Aliens arrive without their enemies and spread unchecked}",
            r"\text{Hyacinth blankets the dam; wattle drinks the river}",
            r"\text{Five steps: name, first hit, next hit, cost, fix and why}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.8).shift(band_shift(7) + UP * (1.3 - 0.75 * i))
            self.play(Write(m))
            self.wait(2.0)
        b7_l5 = Tex("A wobble that heals, a knock that does not, and five steps to read it.").scale(0.85).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
