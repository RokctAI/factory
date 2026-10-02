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

# Band-layout whiteboard scene for energy-flow-in-food-chains-and-food-webs
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex/MathTex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to subtopics.json
# (210/210/240/250/190/190/180 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EnergyFlowSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): food chains
        title = Tex("Food chains: energy on the move").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"\text{grass} \rightarrow \text{impala} \rightarrow \text{lion}").scale(1.1).shift(UP * 1.2)
        l2 = MathTex(r"\text{phytoplankton} \rightarrow \text{zooplankton} \rightarrow \text{sardine} \rightarrow \text{gannet}").scale(0.85).shift(UP * 0.2)
        l3 = Tex("Arrow = direction of energy flow = ``is eaten by''").scale(0.9).shift(DOWN * 0.7)
        l4 = Tex("Always starts with a producer; decomposers act on every link").scale(0.85).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): trophic levels
        self.next_band(1)
        b1_title = Tex("Trophic levels").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        rows = [
            r"\text{Level 1: producer (grass)}",
            r"\text{Level 2: primary consumer, herbivore (impala)}",
            r"\text{Level 3: secondary consumer, carnivore (lion)}",
            r"\text{Level 4: tertiary consumer (eagle eating a snake)}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.85).shift(band_shift(1) + UP * (1.3 - 0.8 * i))
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # --- Band 2 (subtopic_3): food webs
        self.next_band(2)
        b2_title = Tex("Food webs: all the chains at once").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{grass} \rightarrow \text{locust} \rightarrow \text{lizard} \rightarrow \text{eagle}").scale(0.9).shift(band_shift(2) + UP * 1.3)
        b2_l2 = MathTex(r"\text{grass} \rightarrow \text{zebra} \rightarrow \text{lion} \qquad \text{locust} \rightarrow \text{jackal}").scale(0.9).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("Remove jackals: locusts up, grass down, grazers hungry").scale(0.9).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("Answer with arrows: ``X increases because fewer are eaten by Y''").scale(0.8).shift(band_shift(2) + DOWN * 1.5)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): the ten percent rule
        self.next_band(3)
        b3_title = Tex("Energy loss: the ten percent rule").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"10\,000\ \text{kJ (grass)} \rightarrow 1000\ \text{kJ (impala)} \rightarrow 100\ \text{kJ (lion)} \rightarrow 10\ \text{kJ}").scale(0.8).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("Lost: not eaten, not digested (dung), RESPIRATION as heat, urine").scale(0.8).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex("Only energy in new tissue passes on").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = Tex("So chains are short and the shape is a pyramid").scale(0.9).shift(band_shift(3) + DOWN * 1.8)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{lion} \rightarrow \text{impala} \rightarrow \text{grass}").scale(0.95).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("``The Sun is the first organism''").scale(0.9).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex("``The energy disappears''").scale(0.9).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex("``The herbivore is at trophic level 1''").scale(0.9).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the relay
        self.next_band(5)
        b5_title = Tex("Follow the sandwich: a relay race").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Baton = energy. Sun passes it to the grass, grass to impala, impala to lion").scale(0.8).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Arrow points to whoever RECEIVES the baton").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("First runner is always green: the producer").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("Herbivore runs second, so it is at level two").scale(0.95).shift(band_shift(5) + DOWN * 1.5)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): the spider's web
        self.next_band(6)
        b6_title = Tex("One menu, many links").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Nobody eats one thing: draw every chain together = a web").scale(0.85).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("Pull one strand and the whole web shivers").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("No jackals: more locusts, less grass, hungry grazers").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("Variety is safety; a one-food animal is in trouble").scale(0.9).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): the leaky bucket
        self.next_band(7)
        b7_title = Tex("The leaky bucket").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        rows = [
            r"\text{Grass bucket 10\,000. Impala bucket 1000. Lion bucket 100.}",
            r"\text{Four holes: not eaten, dung, heat from respiration, urine}",
            r"\text{Energy never destroyed: it ends as heat nobody can eat}",
            r"\text{Maize as pap feeds ten times more than maize as beef}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.8).shift(band_shift(7) + UP * (1.3 - 0.75 * i))
            self.play(Write(m))
            self.wait(2.0)
        b7_l5 = Tex("Ten percent per step. Short chains. Few lions. A pyramid.").scale(0.9).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
