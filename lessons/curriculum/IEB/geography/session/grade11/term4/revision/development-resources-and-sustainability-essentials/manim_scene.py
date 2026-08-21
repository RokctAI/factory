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

# Band-layout whiteboard scene for the IEB revision session "Development,
# Resources and Sustainability Essentials" (grade 11, term 4). Seven subtopics
# of the duo: Part 1 Expert (subtopics 1-4), Part 2 Simplifier (subtopics 5-7).
# Band time apportioned to subtopics.json (255/255/260/250/195/195/195 of
# 1605 s). Exporter-safe primitives only; diagrams (indicator table, trade
# arrows, energy chain, the year's circle) hand-built from
# Line/Arrow/Dot/Circle/Rectangle/Tex element by element.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class DevelopmentResourcesSustainabilitySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): measuring development
        title = Tex("Development, Resources, Sustainability").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Growth $=$ more output. Development $=$ better lives.").scale(0.85).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(2.5)
        b0_l2 = Tex(r"GDP: made inside. GNI: earned anywhere.").scale(0.9).shift(UP * 0.4)
        b0_l3 = Tex(r"Both per capita — but averages hide the split").scale(0.9).shift(DOWN * 0.4)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex(r"Gini 0 $\to$ 1: SA among the world's highest").scale(0.9).shift(DOWN * 1.3)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex(r"HDI: long life $+$ knowledge $+$ living standard,").scale(0.85).shift(DOWN * 2.2)
        b0_l6 = Tex(r"scored 0 to 1 — money turned INTO lives").scale(0.85).shift(DOWN * 2.9)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): core-periphery and Rostow
        self.next_band(1)
        b1_title = Tex("Core-periphery and Rostow").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        # Core dot with arrows in (investment) and out (goods), periphery ring.
        core = Dot(band_shift(1) + UP * 0.6, color=YELLOW)
        core_lab = Tex("core: Gauteng").scale(0.8).shift(band_shift(1) + UP * 1.2)
        ring = Circle(radius=2.2).shift(band_shift(1) + UP * 0.6)
        ring_lab = Tex("periphery: former homelands").scale(0.75).shift(band_shift(1) + DOWN * 1.9)
        in_ar = Arrow(band_shift(1) + UP * 0.6 + LEFT * 2.1, band_shift(1) + UP * 0.6 + LEFT * 0.2, color=GREEN)
        in_lab = Tex("labour, materials").scale(0.65).shift(band_shift(1) + UP * 0.1 + LEFT * 2.6)
        out_ar = Arrow(band_shift(1) + UP * 0.6 + RIGHT * 0.2, band_shift(1) + UP * 0.6 + RIGHT * 2.1, color=BLUE)
        out_lab = Tex("remittances").scale(0.65).shift(band_shift(1) + UP * 0.1 + RIGHT * 2.6)
        self.play(Create(core), Write(core_lab))
        self.play(Create(ring), Write(ring_lab))
        self.play(Create(in_ar), Write(in_lab))
        self.play(Create(out_ar), Write(out_lab))
        self.wait(2)
        b1_l1 = Tex(r"Scales: world, country, city").scale(0.85).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"Rostow: 5 stages — quote the critics:").scale(0.85).shift(band_shift(1) + DOWN * 3.3)
        b1_l3 = Tex(r"one staircase, colonial history ignored").scale(0.85).shift(band_shift(1) + DOWN * 4.0)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(3)

        # --- Band 2 (subtopic_2): the trade rules
        self.next_band(2)
        b2_title = Tex("The rules of the game").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Periphery sells raw, buys finished —").scale(0.9).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex(r"terms of trade slide against the raw seller").scale(0.9).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex(r"Escape: beneficiation — sell the jewellery,").scale(0.9).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex(r"not the gold; climb the value chain").scale(0.9).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)
        b2_l5 = Tex(r"Free trade against protectionism: tariffs,").scale(0.9).shift(band_shift(2) + DOWN * 2.0)
        b2_l6 = Tex(r"quotas, subsidies — rich farmers subsidised").scale(0.9).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(2.5)
        b2_l7 = Tex(r"Globalisation: ladders up, shocks in; BRICS, AfCFTA").scale(0.8).shift(band_shift(2) + DOWN * 3.5)
        self.play(Write(b2_l7))
        self.wait(3)

        # --- Band 3 (subtopic_2): aid, argued both ways
        self.next_band(3)
        b3_title = Tex("Aid, argued both ways").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Types: emergency, development, technical;").scale(0.9).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"multilateral vs bilateral; tied $=$ strings").scale(0.9).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_mid = Line(band_shift(3) + UP * 0.0, band_shift(3) + DOWN * 2.4)
        self.play(Create(b3_mid))
        b3_fh = Tex("For", color=GREEN).scale(0.95).shift(band_shift(3) + DOWN * 0.3 + LEFT * 3.2)
        b3_ah = Tex("Against", color=RED).scale(0.95).shift(band_shift(3) + DOWN * 0.3 + RIGHT * 3.2)
        self.play(Write(b3_fh), Write(b3_ah))
        b3_f1 = Tex(r"saves lives; builds\\ clinics, schools").scale(0.8).shift(band_shift(3) + DOWN * 1.2 + LEFT * 3.2)
        b3_a1 = Tex(r"dependency;\\ corruption leaks").scale(0.8).shift(band_shift(3) + DOWN * 1.2 + RIGHT * 3.2)
        self.play(Write(b3_f1))
        self.play(Write(b3_a1))
        self.wait(2)
        b3_f2 = Tex(r"skills; vaccination\\ transformed societies").scale(0.8).shift(band_shift(3) + DOWN * 2.2 + LEFT * 3.2)
        b3_a2 = Tex(r"tied aid serves donor;\\ the 80s debt trap").scale(0.8).shift(band_shift(3) + DOWN * 2.2 + RIGHT * 3.2)
        self.play(Write(b3_f2))
        self.play(Write(b3_a2))
        self.wait(2.5)
        b3_l3 = Tex(r"Verdict: build capacity; fair trade beats charity").scale(0.85).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): conventional energy
        self.next_band(4)
        b4_title = Tex("Conventional energy").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Coal $>$ 4/5 of generation; stations on the seams").scale(0.85).shift(band_shift(4) + UP * 1.3)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex(r"mill $\to$ burn $\to$ steam $\to$ turbine $\to$ generator").scale(0.85).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex(r"For: cheap, local, jobs, baseload. Against: CO$_2$,").scale(0.85).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex(r"Highveld air, water, scars, acid mine drainage").scale(0.85).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex(r"Koeberg: steady, low-carbon; dear, slow, waste").scale(0.85).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l5))
        self.wait(2)
        b4_l6 = Tex(r"Hydro small — weak rivers; Cahora Bassa imports;").scale(0.8).shift(band_shift(4) + DOWN * 2.8)
        b4_l7 = Tex(r"pumped storage $=$ battery, not source").scale(0.85).shift(band_shift(4) + DOWN * 3.5)
        self.play(Write(b4_l6))
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_3): non-conventional energy
        self.next_band(5)
        b5_title = Tex("Non-conventional energy").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Northern Cape sun: world-class — PV farms,").scale(0.9).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex(r"mirror fields banking heat in molten salt").scale(0.9).shift(band_shift(5) + UP * 0.6)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Cape coasts: turbine farms, Kouga to West Coast").scale(0.85).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex(r"Auction rounds drove prices below new coal").scale(0.9).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)
        b5_l5 = Tex(r"But: intermittency — storage, backup, grid;").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        b5_l6 = Tex(r"and a JUST transition for the coal towns").scale(0.9).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): the erosion ladder
        self.next_band(6)
        b6_title = Tex("Soil: the erosion ladder").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Centuries to form; storms to lose — non-renewable").scale(0.85).shift(band_shift(6) + UP * 1.3)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex(r"bare $\to$ splash $\to$ sheet $\to$ rill $\to$ donga").scale(0.9).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex(r"12\% arable, 3\% high-potential; losses in the").scale(0.85).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex(r"hundreds of millions of tonnes a year").scale(0.85).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex(r"Remedies: cover, contour, terrace, rotate,").scale(0.85).shift(band_shift(6) + DOWN * 2.0)
        b6_l6 = Tex(r"carrying capacity, gabions in the dongas").scale(0.85).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): sustainability and the circle
        self.next_band(7)
        b7_title = Tex("Sustainability and the circle").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Present needs met without compromising").scale(0.9).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex(r"future generations — word for word").scale(0.9).shift(band_shift(7) + UP * 0.6)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        # The year's circle: four dots joined in a ring with arrows.
        d1 = Dot(band_shift(7) + DOWN * 0.6 + LEFT * 3.0)
        d1_lab = Tex("development").scale(0.7).shift(band_shift(7) + DOWN * 0.1 + LEFT * 3.0)
        d2 = Dot(band_shift(7) + DOWN * 0.6 + RIGHT * 3.0)
        d2_lab = Tex("energy").scale(0.7).shift(band_shift(7) + DOWN * 0.1 + RIGHT * 3.0)
        d3 = Dot(band_shift(7) + DOWN * 2.6 + RIGHT * 3.0)
        d3_lab = Tex("climate").scale(0.7).shift(band_shift(7) + DOWN * 3.1 + RIGHT * 3.0)
        d4 = Dot(band_shift(7) + DOWN * 2.6 + LEFT * 3.0)
        d4_lab = Tex("soil").scale(0.7).shift(band_shift(7) + DOWN * 3.1 + LEFT * 3.0)
        self.play(Create(d1), Write(d1_lab))
        self.play(Create(d2), Write(d2_lab))
        self.play(Create(d3), Write(d3_lab))
        self.play(Create(d4), Write(d4_lab))
        a12 = Arrow(d1.get_center(), d2.get_center(), buff=0.15)
        a23 = Arrow(d2.get_center(), d3.get_center(), buff=0.15)
        a34 = Arrow(d3.get_center(), d4.get_center(), buff=0.15)
        a41 = Arrow(d4.get_center(), d1.get_center(), buff=0.15)
        self.play(Create(a12))
        self.play(Create(a23))
        self.play(Create(a34))
        self.play(Create(a41))
        self.wait(2)
        b7_l3 = Tex(r"Walk the circle $=$ doing geography").scale(0.9).shift(band_shift(7) + DOWN * 3.9)
        self.play(Write(b7_l3))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the scoreboard and the rigged shop
        self.next_band(8)
        b8_title = Tex("The scoreboard and the rigged shop").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Fix 1: per person. Fix 2: the spread — Gini.").scale(0.85).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"Fix 3: follow money into lives — HDI").scale(0.85).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex(r"The shop: sell raw, buy finished —").scale(0.9).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex(r"your trolley buys less every year").scale(0.9).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex(r"Escape: start MAKING — beneficiation").scale(0.9).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex(r"Charity counter: bakeries beat bread").scale(0.9).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the braai fire and the free fuels
        self.next_band(9)
        b9_title = Tex("The braai fire and the two free fuels").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"The fire: coal on the Highveld seams —").scale(0.9).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex(r"steady baseload; smoke, water, acid bills").scale(0.9).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex(r"Free fuels: Upington mirrors and molten salt;").scale(0.85).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex(r"Cape turbine forests — cheaper than new coal").scale(0.85).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex(r"But they take days off: keep an ember steady,").scale(0.85).shift(band_shift(9) + DOWN * 2.0)
        b9_l6 = Tex(r"build water batteries, thicken the wires").scale(0.85).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(2.5)
        b9_l7 = Tex(r"And carry the coal towns: the JUST transition").scale(0.85).shift(band_shift(9) + DOWN * 3.5)
        self.play(Write(b9_l7))
        self.play(Create(SurroundingRectangle(b9_l7, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): living off the interest
        self.next_band(10)
        b10_title = Tex("Living off the interest").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Topsoil: teaspoon deposits, bucket withdrawals").scale(0.9).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.play(Create(SurroundingRectangle(b10_l1, color=GREEN)))
        self.wait(2.5)
        b10_l2 = Tex(r"Soil $=$ capital, harvest $=$ interest;").scale(0.9).shift(band_shift(10) + UP * 0.3)
        b10_l3 = Tex(r"coal $=$ capital burning; sun and wind $=$ interest").scale(0.85).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"The circle: development $\to$ energy $\to$ climate").scale(0.85).shift(band_shift(10) + DOWN * 1.3)
        b10_l5 = Tex(r"$\to$ storms $\to$ soil $\to$ back to development").scale(0.85).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex(r"Definition word-perfect; responsibilities:").scale(0.85).shift(band_shift(10) + DOWN * 2.8)
        b10_l7 = Tex(r"government, business, you").scale(0.9).shift(band_shift(10) + DOWN * 3.5)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.play(Create(SurroundingRectangle(b10_l7, color=GREEN)))
        self.wait(4)
