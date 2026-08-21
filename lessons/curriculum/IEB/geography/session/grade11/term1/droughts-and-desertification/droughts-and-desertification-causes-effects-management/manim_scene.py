# Copyright (c) 2026 RokctAI
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from manim import *

# Band-layout whiteboard scene for the IEB Grade 11 Geography session duo
# "Droughts and Desertification: Causes, Effects, Management". One band per
# teaching beat; the camera moves down to fresh space and nothing is ever
# removed. Exporter-safe primitives only: the four deepening drought stages
# are drawn as a descending staircase of labels.
# Subtopic time shares follow subtopics.json:
# 220/230/235/240/185/185/210 of 1505 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DroughtsDesertificationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): drought defined against the local normal ---
        title = Tex("Droughts and Desertification").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("Drought: rainfall well below the").scale(1.1).shift(UP * 1.0)
        s0_l2 = Tex("LOCAL normal — not merely low rain").scale(1.1).shift(UP * 0.1)
        self.play(Write(s0_l1))
        self.play(Write(s0_l2))
        self.play(Create(SurroundingRectangle(s0_l2, color=GREEN)))
        self.wait(2.5)
        s0_l3 = Tex("Springbok thrives on $\\approx 200$ mm;").scale(1.0).shift(DOWN * 1.0)
        s0_l4 = Tex("the same total would break Mbombela").scale(1.0).shift(DOWN * 1.9)
        self.play(Write(s0_l3))
        self.wait(2)
        self.play(Write(s0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the four deepening stages + causes ---
        self.next_band(1)
        b1_title = Tex("Four stages, always in order").scale(1.2).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        # descending staircase of stages
        st1 = Tex("1 METEOROLOGICAL: rain fails").scale(0.95).shift(band_shift(1) + LEFT * 1.8 + UP * 1.5)
        st2 = Tex("2 AGRICULTURAL: soil moisture fails").scale(0.95).shift(band_shift(1) + LEFT * 0.9 + UP * 0.6)
        st3 = Tex("3 HYDROLOGICAL: rivers, dams fail").scale(0.95).shift(band_shift(1) + RIGHT * 0.0 + DOWN * 0.3)
        st4 = Tex("4 SOCIO-ECONOMIC: lives fail").scale(0.95).shift(band_shift(1) + RIGHT * 0.9 + DOWN * 1.2)
        self.play(Write(st1))
        self.wait(2)
        self.play(Write(st2))
        self.wait(2)
        self.play(Write(st3))
        self.wait(2)
        self.play(Write(st4))
        self.play(Create(SurroundingRectangle(st4, color=GREEN)))
        self.wait(2)
        b1_l1 = Tex("Causes: subsiding belt, stalling ITCZ,").scale(0.9).shift(band_shift(1) + DOWN * 2.2)
        b1_l2 = Tex("El Ni\\~no 2023-24, climate change, demand").scale(0.9).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(3)

        # --- Band 2 (subtopic_2): desertification and its causal chain ---
        self.next_band(2)
        b2_title = Tex("Desertification: land degradation").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Not a desert marching — land dying in patches").scale(0.9).shift(band_shift(2) + UP * 1.4)
        self.play(Write(b2_l1))
        self.wait(2)
        c1 = Tex("OVERGRAZING").scale(0.9).shift(band_shift(2) + LEFT * 3.4 + UP * 0.4)
        c2 = Tex("OVER-CULTIVATION").scale(0.9).shift(band_shift(2) + RIGHT * 2.6 + UP * 0.4)
        c3 = Tex("DEFORESTATION").scale(0.9).shift(band_shift(2) + LEFT * 3.2 + DOWN * 0.5)
        c4 = Tex("SALINISATION").scale(0.9).shift(band_shift(2) + RIGHT * 2.8 + DOWN * 0.5)
        self.play(Write(c1))
        self.wait(1.5)
        self.play(Write(c2))
        self.wait(1.5)
        self.play(Write(c3))
        self.wait(1.5)
        self.play(Write(c4))
        self.wait(1.5)
        c5 = Tex("POPULATION PRESSURE beneath all four").scale(0.95).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(c5))
        self.play(Create(SurroundingRectangle(c5, color=GREEN)))
        self.wait(2)
        b2_l2 = Tex("Sahel; Karoo margins; old Eastern Cape reserves").scale(0.85).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l2))
        self.wait(3)

        # --- Band 3 (subtopic_2): the feedback loop ---
        self.next_band(3)
        b3_title = Tex("The spiral with no brakes").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        # loop of four steps joined by arrows
        p1 = Tex("bare soil crusts").scale(0.9).shift(band_shift(3) + UP * 1.2)
        p2 = Tex("rain sheets off: dongas").scale(0.9).shift(band_shift(3) + RIGHT * 3.2 + UP * 0.0)
        p3 = Tex("topsoil lost").scale(0.9).shift(band_shift(3) + DOWN * 1.2)
        p4 = Tex("less cover regrows").scale(0.9).shift(band_shift(3) + LEFT * 3.2 + UP * 0.0)
        a12 = Arrow(RIGHT * 1.1 + UP * 1.0, RIGHT * 2.6 + UP * 0.3, color=YELLOW, buff=0).shift(band_shift(3))
        a23 = Arrow(RIGHT * 2.6 + DOWN * 0.3, RIGHT * 1.1 + DOWN * 1.0, color=YELLOW, buff=0).shift(band_shift(3))
        a34 = Arrow(LEFT * 1.1 + DOWN * 1.0, LEFT * 2.6 + DOWN * 0.3, color=YELLOW, buff=0).shift(band_shift(3))
        a41 = Arrow(LEFT * 2.6 + UP * 0.3, LEFT * 1.1 + UP * 1.0, color=YELLOW, buff=0).shift(band_shift(3))
        self.play(Write(p1))
        self.play(Create(a12), Write(p2))
        self.wait(2)
        self.play(Create(a23), Write(p3))
        self.wait(2)
        self.play(Create(a34), Write(p4))
        self.wait(2)
        self.play(Create(a41))
        self.wait(2)
        b3_l1 = Tex("Positive feedback: each round bares more ground").scale(0.9).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): effects on environment and people ---
        self.next_band(4)
        b4_title = Tex("The costs cascade").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Vegetation $\\rightarrow$ habitats $\\rightarrow$ biodiversity").scale(0.95).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("Soil: a thousand years lost in a season").scale(0.95).shift(band_shift(4) + UP * 0.5)
        b4_l3 = Tex("Water: rivers to sand, dams to dead storage").scale(0.95).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("People: food security, jobs, health,").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        b4_l5 = Tex("drought migration, conflict over water").scale(0.95).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2)
        b4_l6 = Tex("2023-24: regional disaster declarations").scale(0.9).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): Nelson Mandela Bay, the numbers ---
        self.next_band(5)
        b5_title = Tex("Case study: Nelson Mandela Bay").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        # dam gauge falling to one tenth
        gauge = Line(LEFT * 4.6 + DOWN * 1.8, LEFT * 4.6 + UP * 1.6, color=WHITE).shift(band_shift(5))
        level = Dot(LEFT * 4.6 + DOWN * 1.45).shift(band_shift(5))
        g_lab = Tex("2022: dams near one-tenth").scale(0.9).shift(band_shift(5) + LEFT * 1.4 + DOWN * 1.5)
        self.play(Create(gauge), Create(level))
        self.play(Write(g_lab))
        self.wait(2)
        b5_l1 = Tex("Rains missed the catchments from 2015").scale(0.95).shift(band_shift(5) + UP * 1.3 + RIGHT * 0.6)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Pressure down, leaks chased, boreholes,").scale(0.95).shift(band_shift(5) + UP * 0.4 + RIGHT * 0.6)
        b5_l3 = Tex("Nooitgedagt: Orange River water in").scale(0.95).shift(band_shift(5) + DOWN * 0.4 + RIGHT * 0.6)
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex("Target: 50 litres per person per day").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three management families ---
        self.next_band(6)
        b6_title = Tex("Three families of management").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        f1 = Tex("1 SEE IT COMING: satellites, GIS,").scale(0.95).shift(band_shift(6) + UP * 1.3)
        f1b = Tex("destock early, hardy crops, fodder banks").scale(0.95).shift(band_shift(6) + UP * 0.5)
        self.play(Write(f1))
        self.play(Write(f1b))
        self.wait(2.5)
        f2 = Tex("2 SPEND LESS: drip lines, night watering,").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        f2b = Tex("mulch, leaks fixed, tariffs, rain tanks").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(f2))
        self.play(Write(f2b))
        self.wait(2.5)
        f3 = Tex("3 HEAL THE LAND: rest camps, contour").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        f3b = Tex("ploughing, check dams, windbreaks").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(f3))
        self.play(Write(f3b))
        self.wait(3)

        # --- Band 7 (subtopic_4): the named programmes ---
        self.next_band(7)
        b7_title = Tex("Named programmes carry marks").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("WORKING FOR WATER: alien trees out,").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("streamflow back, rural jobs created").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("LANDCARE: communal land rehabilitated").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("GREAT GREEN WALL: thousands of village").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        b7_l5 = Tex("projects, Senegal to Djibouti").scale(1.0).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the prepaid data bundle ---
        self.next_band(8)
        b8_title = Tex("The prepaid data bundle").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Rain = the monthly bundle a place loads").scale(0.95).shift(band_shift(8) + UP * 1.3)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Drought = YOUR bundle loading far short").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2)
        b8_l3 = Tex("bundle $\\rightarrow$ apps $\\rightarrow$ reserves $\\rightarrow$ life").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("= rain, soil, dams, society — in order").scale(0.95).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Loads lighter: stalled belt, El Ni\\~no,").scale(0.9).shift(band_shift(8) + DOWN * 2.3)
        b8_l6 = Tex("climate change — and harder spending").scale(0.9).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): how to make a desert ---
        self.next_band(9)
        b9_title = Tex("How to make a desert").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Recipe: too many hooves, tired lands,").scale(0.95).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex("felled trees, salty irrigation").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("The goalmouth: trampled bare, baked hard,").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex("rain sheets off, wind lifts the dust").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Scaled up: dongas bleeding topsoil away").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("The damage feeds itself — patch by patch").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): Gqeberha and the empty dams ---
        self.next_band(10)
        b10_title = Tex("Gqeberha and the empty dams").scale(1.15).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Seven missed seasons; 2022: near one-tenth").scale(0.95).shift(band_shift(10) + UP * 1.4)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("Fought on every front: pressure, leaks,").scale(0.95).shift(band_shift(10) + UP * 0.6)
        b10_l3 = Tex("boreholes, Orange River water, 50 litres").scale(0.95).shift(band_shift(10) + DOWN * 0.2)
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("Taps held until the 2023 rains").scale(1.0).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("Three moves: see it coming, spend less,").scale(0.95).shift(band_shift(10) + DOWN * 2.0)
        b10_l6 = Tex("heal the land — with the named programmes").scale(0.95).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(4)
