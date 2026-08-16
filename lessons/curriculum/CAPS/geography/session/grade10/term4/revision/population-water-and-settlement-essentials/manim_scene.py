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

# Band-layout whiteboard scene for the revision session "Population, Water
# and Settlement Essentials" (Part 1 — Expert subtopics 1-4, Part 2 —
# Simplifier 5-7). Exporter-safe primitives only; the density and natural-
# increase calculations are written line by line in MathTex with green boxed
# answers. Add-only lifecycle; camera moves down band by band. Band time
# apportioned to subtopics.json (250/250/245/255/185/190/195 of 1570 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class Grade10HumanRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): distribution vs density ---
        title = Tex("Population, Water and Settlement").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Distribution: WHERE the people are (pattern)").scale(1.0).shift(UP * 1.0)
        d2 = Tex("Density: HOW MANY per unit area").scale(1.0).shift(UP * 0.2)
        self.play(Write(d1))
        self.wait(1.5)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"\frac{2\,000\,000}{40\,000 \text{ km}^2} = 50 \text{ per km}^2").scale(0.99).shift(DOWN * 1.0)
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(2.5)
        d4 = Tex("Trap: density is an AVERAGE —").scale(0.95).shift(DOWN * 2.1)
        d5 = Tex("Egypt looks moderate, lives on the Nile").scale(0.95).shift(DOWN * 2.9)
        self.play(Write(d4))
        self.play(Write(d5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the world and SA patterns ---
        self.next_band(1)
        b1_title = Tex("The pattern and its reasons").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        w1 = Tex("9 of 10 live north of the equator;").scale(0.95).shift(band_shift(1) + UP * 1.2)
        w2 = Tex("empty = too dry, cold, high or forested").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(w1))
        self.play(Write(w2))
        self.wait(2.5)
        w3 = Tex("SA: people thicken eastward with the rain").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(w3))
        self.wait(2)
        w4 = Tex("Gauteng: smallest province, a quarter of us —").scale(0.95).shift(band_shift(1) + DOWN * 1.4)
        w5 = Tex("GOLD (1886) overrode the physical factors").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(w4))
        self.play(Write(w5))
        self.play(Create(SurroundingRectangle(w5, color=GREEN)))
        self.wait(2)
        w6 = Tex("Northern Cape: largest, $\\approx 2$ per km$^2$").scale(0.95).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(w6))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the vital rates ---
        self.next_band(2)
        b2_title = Tex("Growth: the vital rates").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        v1 = Tex("Births and deaths per 1 000 per year").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(v1))
        self.wait(2)
        v2 = MathTex(r"30 - 10 = 20 \text{ per thousand} = 2\%").scale(1.1).shift(band_shift(2) + UP * 0.2)
        self.play(Write(v2))
        self.play(Create(SurroundingRectangle(v2, color=GREEN)))
        self.wait(2.5)
        v3 = Tex("Fertility: 2,1 = replacement level").scale(0.95).shift(band_shift(2) + DOWN * 0.8)
        v4 = Tex("Infant mortality: the most sensitive indicator").scale(0.95).shift(band_shift(2) + DOWN * 1.6)
        v5 = Tex("Life expectancy: average years for a newborn").scale(0.95).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(v3))
        self.wait(1.5)
        self.play(Write(v4))
        self.wait(1.5)
        self.play(Write(v5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): transition model and the pyramid ---
        self.next_band(3)
        b3_title = Tex("Transition and the pyramid").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        s1 = Tex("1: both high. 2: deaths fall — explosion.").scale(0.9).shift(band_shift(3) + UP * 1.2)
        s2 = Tex("3: births follow. 4: both low. 5: shrinking").scale(0.9).shift(band_shift(3) + UP * 0.4)
        self.play(Write(s1))
        self.play(Write(s2))
        self.wait(2.5)
        s3 = Tex("Overpopulation: people vs resources,").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        s4 = Tex("a relationship, never a raw count").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(s3))
        self.play(Write(s4))
        self.play(Create(SurroundingRectangle(s4, color=GREEN)))
        self.wait(2.5)
        s5 = Tex("Pyramid: read base, sides, top —").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        s6 = Tex("births, survival, old age; SA transitional,").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        s7 = Tex("with the HIV notch in the young-adult bars").scale(0.95).shift(band_shift(3) + DOWN * 3.7)
        self.play(Write(s5))
        self.play(Write(s6))
        self.play(Write(s7))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): migration vocabulary and push-pull ---
        self.next_band(4)
        b4_title = Tex("People on the move").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        m1 = Tex("Emigrant leaves, immigrant enters;").scale(0.95).shift(band_shift(4) + UP * 1.2)
        m2 = Tex("internal vs international; voluntary vs forced").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(m1))
        self.play(Write(m2))
        self.wait(2.5)
        m3 = Tex("Push: unemployment, drought, conflict").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        m4 = Tex("Pull: jobs, schools, city lights").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(m3))
        self.wait(1.5)
        self.play(Write(m4))
        self.wait(2)
        m5 = Tex("Eastern Cape and Limpopo $\\to$ Gauteng;").scale(0.95).shift(band_shift(4) + DOWN * 2.2)
        m6 = Tex("Zimbabwe, Mozambique, Lesotho $\\to$ SA").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(m5))
        self.play(Write(m6))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): urbanisation and informal settlement ---
        self.next_band(5)
        b5_title = Tex("Urbanisation and the leftover land").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        u1 = Tex("Urbanisation: rising PERCENTAGE in towns —").scale(0.95).shift(band_shift(5) + UP * 1.2)
        u2 = Tex("SA past two-thirds urban and climbing").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(u1))
        self.play(Write(u2))
        self.wait(2.5)
        u3 = Tex("Informal settlements: self-built homes on").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        u4 = Tex("steep slopes, floodplains, land beside industry").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(u3))
        self.play(Write(u4))
        self.wait(2.5)
        u5 = Tex("Answer = upgrading, not demolition:").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        u6 = Tex("water, sanitation, electricity, tenure").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(u5))
        self.play(Write(u6))
        self.play(Create(SurroundingRectangle(u6, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): water in a dry country ---
        self.next_band(6)
        b6_title = Tex("Water in a dry country").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        q1 = Tex("SA rainfall $\\approx 464$ mm vs world $\\approx 860$ mm").scale(0.95).shift(band_shift(6) + UP * 1.2)
        self.play(Write(q1))
        self.play(Create(SurroundingRectangle(q1, color=GREEN)))
        self.wait(2.5)
        q2 = Tex("Two-thirds of the country under 500 mm").scale(0.95).shift(band_shift(6) + UP * 0.2)
        self.play(Write(q2))
        self.wait(2)
        q3 = Tex("Answers: dams (Gariep, Vaal), transfers").scale(0.95).shift(band_shift(6) + DOWN * 0.7)
        q4 = Tex("(Lesotho Highlands $\\to$ Gauteng), boreholes").scale(0.95).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(q3))
        self.play(Write(q4))
        self.wait(2.5)
        q5 = Tex("Yet it floods: cut-off lows on primed catchments;").scale(0.9).shift(band_shift(6) + DOWN * 2.4)
        q6 = Tex("urban seal + floodplain settlement = disaster").scale(0.9).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(q5))
        self.play(Write(q6))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): hydrograph signatures and management ---
        self.next_band(7)
        b7_title = Tex("Hydrograph signatures and management").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        r1 = Tex("Sealed catchment: short lag, high narrow peak").scale(0.95).shift(band_shift(7) + UP * 1.2)
        r2 = Tex("Vegetated: long lag, low broad peak").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex("Laingsburg 1981 flash; KZN 2022 regional").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(r3))
        self.wait(2)
        r4 = Tex("Free basic water: 6 000 litres per household").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        r5 = Tex("per month; two-thirds of water to agriculture;").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        r6 = Tex("Day Zero 2018: management is not optional").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(r4))
        self.wait(2)
        self.play(Write(r5))
        self.play(Write(r6))
        self.play(Create(SurroundingRectangle(r6, color=GREEN)))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the party in the kitchen ---
        self.next_band(8)
        b8_title = Tex("The party in the kitchen").scale(1.2).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        p1 = Tex("People drift to food, drinks and friends:").scale(0.95).shift(band_shift(8) + UP * 1.3)
        p2 = Tex("that drift IS distribution").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(p1))
        self.play(Write(p2))
        self.wait(2.5)
        p3 = Tex("Density = people $\\div$ space").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(p3))
        self.play(Create(SurroundingRectangle(p3, color=GREEN)))
        self.wait(2)
        p4 = Tex("Gauteng is the kitchen (jobs since 1886);").scale(0.95).shift(band_shift(8) + DOWN * 1.4)
        p5 = Tex("Northern Cape the cold stoep, near-empty").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(p4))
        self.play(Write(p5))
        self.wait(2.5)
        p6 = Tex("Averages lie smoothly — ask how people spread").scale(0.9).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(p6))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): the stadium photograph ---
        self.next_band(9)
        b9_title = Tex("The stadium photograph").scale(1.2).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        g1 = Tex("Three glances: the bottom row (births),").scale(0.95).shift(band_shift(9) + UP * 1.3)
        g2 = Tex("the slope (survival), the top (old age)").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(g1))
        self.play(Write(g2))
        self.wait(2.5)
        g3 = Tex("Triangle = young, poor, fast-growing;").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        g4 = Tex("column = rich, slow, ageing").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(g3))
        self.play(Write(g4))
        self.wait(2.5)
        g5 = Tex("SA in between: base near two children,").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        g6 = Tex("HIV notch, then treatment turned it up").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(g5))
        self.play(Write(g6))
        self.wait(2)
        g7 = Tex("Overpopulation: can the kitchens feed them?").scale(0.95).shift(band_shift(9) + DOWN * 3.6)
        self.play(Write(g7))
        self.wait(2.5)

        # --- Band 10 (subtopic_7): the bucket with a hole ---
        self.next_band(10)
        b10_title = Tex("The bucket with a hole").scale(1.2).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        k1 = Tex("Small (half the world's rain), fills unevenly,").scale(0.9).shift(band_shift(10) + UP * 1.3)
        k2 = Tex("and leaks — a third lost in broken pipes").scale(0.9).shift(band_shift(10) + UP * 0.5)
        self.play(Write(k1))
        self.play(Write(k2))
        self.wait(2.5)
        k3 = Tex("Responses: engineering (dams, Lesotho scheme,").scale(0.9).shift(band_shift(10) + DOWN * 0.4)
        k4 = Tex("boreholes), fairness (6 000 free litres),").scale(0.9).shift(band_shift(10) + DOWN * 1.2)
        k5 = Tex("behaviour (drip irrigation beats short showers)").scale(0.9).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(k3))
        self.play(Write(k4))
        self.wait(2)
        self.play(Write(k5))
        self.wait(2.5)
        k6 = Tex("One chain: moved for work, settled on leftover").scale(0.9).shift(band_shift(10) + DOWN * 2.9)
        k7 = Tex("land — and the leftover land was the water's own").scale(0.9).shift(band_shift(10) + DOWN * 3.6)
        self.play(Write(k6))
        self.play(Write(k7))
        self.play(Create(SurroundingRectangle(k7, color=GREEN)))
        self.wait(3)
