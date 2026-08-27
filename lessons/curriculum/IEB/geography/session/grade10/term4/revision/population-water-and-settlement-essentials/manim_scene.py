# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
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

# Band-layout whiteboard scene for the Grade 10 human-geography revision
# session "Population, Water and Settlement Essentials" (Part 1 — Expert
# subtopics 1-4, Part 2 — Simplifier 5-7). Exporter-safe primitives only:
# the pyramid archetypes are Rectangle bar stacks, and the hydrograph
# signatures are Line chains. Add-only lifecycle; camera moves down band by
# band. Band time apportioned to subtopics.json
# (250/250/245/255/185/190/195 of 1570 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class Grade10HumanRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): distribution vs density ---
        title = Tex("Population, Water and Settlement").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Distribution: WHERE the pattern lies").scale(0.95).shift(UP * 1.0)
        d2 = Tex("Density: HOW MANY per square kilometre").scale(0.95).shift(UP * 0.2)
        self.play(Write(d1))
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"3\,000\,000 \div 25\,000 = 120 \text{ per km}^2").scale(1.0).shift(DOWN * 0.9)
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(2)
        d4 = Tex("Averages hide the crush: Australia looks empty,").scale(0.85).shift(DOWN * 2.0)
        d5 = Tex("yet its people queue on two coastal fringes").scale(0.85).shift(DOWN * 2.8)
        self.play(Write(d4))
        self.play(Write(d5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the world and SA patterns ---
        self.next_band(1)
        b1_title = Tex("Why people are where they are").scale(1.1).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        w1 = Tex("Empty: too dry, too cold, too high, too forested").scale(0.85).shift(band_shift(1) + UP * 1.4)
        self.play(Write(w1))
        self.wait(2)
        w2 = Tex("Physical: water, climate, soil, relief, resources").scale(0.85).shift(band_shift(1) + UP * 0.5)
        w3 = Tex("Human: work, transport, trade, history, politics").scale(0.85).shift(band_shift(1) + DOWN * 0.3)
        self.play(Write(w2))
        self.play(Write(w3))
        self.wait(2)
        w4 = Tex("Gauteng: a quarter of the nation on dry ground —").scale(0.85).shift(band_shift(1) + DOWN * 1.3)
        w5 = Tex("gold (1886) overruled the rain").scale(0.85).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(w4))
        self.play(Write(w5))
        self.play(Create(SurroundingRectangle(w5, color=GREEN)))
        self.wait(2)
        w6 = Tex("Northern Cape: $\\approx 2$ per km$^2$; coasts on trade").scale(0.85).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(w6))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the vital rates ---
        self.next_band(2)
        b2_title = Tex("The vital rates").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        v1 = Tex("Births and deaths per 1 000 per year").scale(0.9).shift(band_shift(2) + UP * 1.4)
        self.play(Write(v1))
        self.wait(1.5)
        v2 = MathTex(r"24 - 9 = 15 \text{ per } 1000 = 1.5\% \text{ growth}").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(v2))
        self.play(Create(SurroundingRectangle(v2, color=GREEN)))
        self.wait(2.5)
        v3 = Tex("Natural increase ignores migration").scale(0.9).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(v3))
        self.wait(2)
        v4 = Tex("Fertility ($\\approx 2.1$ = replacement), infant").scale(0.85).shift(band_shift(2) + DOWN * 1.5)
        v5 = Tex("mortality (the honest indicator), life expectancy").scale(0.85).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(v4))
        self.play(Write(v5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): transition model and the pyramid ---
        self.next_band(3)
        b3_title = Tex("Transition, and the pyramid").scale(1.1).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_title))
        self.wait(1.5)
        t1 = Tex("Stages: high-high $\\to$ deaths fall (explosion) $\\to$").scale(0.8).shift(band_shift(3) + UP * 1.6)
        t2 = Tex("births follow $\\to$ low-low $\\to$ shrinking (Japan)").scale(0.8).shift(band_shift(3) + UP * 0.9)
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(2.5)
        # wedge: wide-base bar stack (left) and block: straight stack (right)
        for i, w in enumerate([3.6, 2.8, 2.0, 1.3, 0.7]):
            bar = Rectangle(width=w, height=0.45).shift(band_shift(3) + LEFT * 3.2 + DOWN * (1.9 - i * 0.5))
            self.play(Create(bar), run_time=0.35)
        wedge_lab = Tex("wedge: young, growing").scale(0.7).shift(band_shift(3) + LEFT * 3.2 + DOWN * 2.7)
        self.play(Write(wedge_lab))
        for i, w in enumerate([2.0, 2.0, 1.95, 1.9, 1.6]):
            bar = Rectangle(width=w, height=0.45).shift(band_shift(3) + RIGHT * 3.2 + DOWN * (1.9 - i * 0.5))
            self.play(Create(bar), run_time=0.35)
        block_lab = Tex("block: wealthy, ageing").scale(0.7).shift(band_shift(3) + RIGHT * 3.2 + DOWN * 2.7)
        self.play(Write(block_lab))
        self.wait(2)
        t3 = Tex("SA: between the shapes, HIV scar, treatment recovery").scale(0.8).shift(band_shift(3) + DOWN * 3.5)
        self.play(Write(t3))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): migration vocabulary and push-pull ---
        self.next_band(4)
        b4_title = Tex("Migration: the pairs").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        m1 = Tex("Emigrant leaves / immigrant arrives;").scale(0.9).shift(band_shift(4) + UP * 1.4)
        m2 = Tex("international / internal; voluntary / forced").scale(0.9).shift(band_shift(4) + UP * 0.6)
        self.play(Write(m1))
        self.play(Write(m2))
        self.wait(2.5)
        push = Tex("PUSH: no work, drought, failing services").scale(0.85).shift(band_shift(4) + DOWN * 0.4)
        pull = Tex("PULL: wages, schools, clinics, city lights").scale(0.85).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(push))
        self.play(Write(pull))
        self.wait(2)
        m3 = Tex("Eastern Cape and Limpopo $\\to$ Gauteng and the metros;").scale(0.8).shift(band_shift(4) + DOWN * 2.1)
        m4 = Tex("the region's magnet: Zimbabwe, Mozambique, Lesotho").scale(0.8).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m3))
        self.play(Write(m4))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): urbanisation and informal settlement ---
        self.next_band(5)
        b5_title = Tex("Urbanisation and the backlog").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        u1 = Tex("Urbanisation: a rising SHARE in towns —").scale(0.9).shift(band_shift(5) + UP * 1.4)
        u2 = Tex("South Africa past two thirds and climbing").scale(0.9).shift(band_shift(5) + UP * 0.6)
        self.play(Write(u1))
        self.play(Write(u2))
        self.wait(2)
        u3 = Tex("Arrivals outpace delivery: informal settlements").scale(0.85).shift(band_shift(5) + DOWN * 0.3)
        u4 = Tex("on the land nobody claimed — slopes, margins,").scale(0.85).shift(band_shift(5) + DOWN * 1.1)
        u5 = Tex("floodplains — within reach of work").scale(0.85).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(u3))
        self.play(Write(u4))
        self.play(Write(u5))
        self.wait(2.5)
        u6 = Tex("Response: upgrade in place, not remove").scale(0.9).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(u6))
        self.play(Create(SurroundingRectangle(u6, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): water in a dry country ---
        self.next_band(6)
        b6_title = Tex("Water in a dry country").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        q1 = MathTex(r"465 \text{ mm vs } 860 \text{ mm}; \quad \approx 9\% \text{ runoff}").scale(0.95).shift(band_shift(6) + UP * 1.4)
        self.play(Write(q1))
        self.play(Create(SurroundingRectangle(q1, color=GREEN)))
        self.wait(2.5)
        q2 = Tex("Orange west with Lesotho's water; Vaal for Gauteng;").scale(0.8).shift(band_shift(6) + UP * 0.3)
        q3 = Tex("500+ dams; Lesotho Highlands transfer; boreholes").scale(0.8).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(q2))
        self.play(Write(q3))
        self.wait(2.5)
        q4 = Tex("Floods, physical: storms, cut-off lows, cyclones").scale(0.8).shift(band_shift(6) + DOWN * 1.5)
        q5 = Tex("Floods, human: sealed cities, lost wetlands,").scale(0.8).shift(band_shift(6) + DOWN * 2.3)
        q6 = Tex("homes on the floodplain").scale(0.8).shift(band_shift(6) + DOWN * 3.1)
        self.play(Write(q4))
        self.play(Write(q5))
        self.play(Write(q6))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): hydrograph signatures and management ---
        self.next_band(7)
        b7_title = Tex("Two signatures, one management list").scale(1.05).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_title))
        self.wait(1.5)
        o7 = band_shift(7) + LEFT * 4.8 + DOWN * 1.2
        x7 = Arrow(o7, o7 + RIGHT * 9.2, buff=0, stroke_width=4)
        y7 = Arrow(o7, o7 + UP * 3.2, buff=0, stroke_width=4)
        self.play(Create(x7), Create(y7))
        s1 = Line(o7 + UP * 0.3, o7 + RIGHT * 1.2 + UP * 0.35, color=RED, stroke_width=5)
        s2 = Line(o7 + RIGHT * 1.2 + UP * 0.35, o7 + RIGHT * 2.0 + UP * 2.8, color=RED, stroke_width=5)
        s3 = Line(o7 + RIGHT * 2.0 + UP * 2.8, o7 + RIGHT * 3.1 + UP * 0.5, color=RED, stroke_width=5)
        sealed_lab = Tex("sealed: short lag, tall peak").scale(0.7).shift(o7 + RIGHT * 3.2 + UP * 3.0)
        self.play(Create(s1), Create(s2), Create(s3), Write(sealed_lab))
        g1 = Line(o7 + UP * 0.4, o7 + RIGHT * 2.6 + UP * 0.6, color=GREEN, stroke_width=5)
        g2 = Line(o7 + RIGHT * 2.6 + UP * 0.6, o7 + RIGHT * 4.8 + UP * 1.4, color=GREEN, stroke_width=5)
        g3 = Line(o7 + RIGHT * 4.8 + UP * 1.4, o7 + RIGHT * 8.6 + UP * 0.5, color=GREEN, stroke_width=5)
        veg_lab = Tex("vegetated: long lag, low peak").scale(0.7).shift(o7 + RIGHT * 6.6 + UP * 2.2)
        self.play(Create(g1), Create(g2), Create(g3), Write(veg_lab))
        self.wait(2.5)
        j1 = Tex("Jukskei 2022 in minutes; Natal 1987 over days").scale(0.8).shift(band_shift(7) + DOWN * 2.4)
        j2 = Tex("6 000 free litres; irrigation $\\approx 60\\%$; Day Zero beaten").scale(0.8).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(j1))
        self.play(Write(j2))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the tuckshop at first break ---
        self.next_band(8)
        b8_title = Tex("The tuckshop at first break").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        p1 = Tex("The school arranges itself: crush at the counter,").scale(0.85).shift(band_shift(8) + UP * 1.3)
        p2 = Tex("groups in the quad, nobody on the far field").scale(0.85).shift(band_shift(8) + UP * 0.5)
        self.play(Write(p1))
        self.play(Write(p2))
        self.wait(2.5)
        p3 = Tex("Tuckshop = Gauteng (work since 1886);").scale(0.9).shift(band_shift(8) + DOWN * 0.4)
        p4 = Tex("far field = Northern Cape ($\\approx 2$ per km$^2$)").scale(0.9).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(p3))
        self.play(Write(p4))
        self.play(Create(SurroundingRectangle(p3, color=GREEN)))
        self.wait(2.5)
        p5 = Tex("Density = people $\\div$ space; the average").scale(0.9).shift(band_shift(8) + DOWN * 2.1)
        p6 = Tex("never shows the crush at the counter").scale(0.9).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(p5))
        self.play(Write(p6))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): the choir on the steps ---
        self.next_band(9)
        b9_title = Tex("The choir on the steps").scale(1.15).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        c1 = Tex("Three looks: the front row (births),").scale(0.9).shift(band_shift(9) + UP * 1.3)
        c2 = Tex("how fast rows thin (survival), the back (old age)").scale(0.9).shift(band_shift(9) + UP * 0.5)
        self.play(Write(c1))
        self.play(Write(c2))
        self.wait(2.5)
        c3 = Tex("Wedge = young and growing; block = rich and ageing").scale(0.85).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(c3))
        self.play(Create(SurroundingRectangle(c3, color=GREEN)))
        self.wait(2)
        c4 = Tex("SA mid-journey: near-two-child families,").scale(0.9).shift(band_shift(9) + DOWN * 1.4)
        c5 = Tex("the HIV notch, the treatment recovery").scale(0.9).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(c4))
        self.play(Write(c5))
        self.wait(2)
        c6 = Tex("Overpopulation: people vs resources, never a count").scale(0.85).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(c6))
        self.wait(2.5)

        # --- Band 10 (subtopic_7): the leaking Jojo tank ---
        self.next_band(10)
        b10_title = Tex("The leaking Jojo tank").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        k1 = Tex("Small tank, unpredictable filling, a leaking third").scale(0.9).shift(band_shift(10) + UP * 1.3)
        self.play(Write(k1))
        self.wait(2)
        k2 = Tex("Answers: dams and transfers; 6 000 free litres;").scale(0.85).shift(band_shift(10) + UP * 0.4)
        k3 = Tex("farm efficiency first, household habits always").scale(0.85).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(k2))
        self.play(Write(k3))
        self.wait(2.5)
        k4 = Tex("The overflow finds the floodplain settlers:").scale(0.9).shift(band_shift(10) + DOWN * 1.3)
        k5 = Tex("sealed city, lost wetlands, short lag, high peak").scale(0.85).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(k4))
        self.play(Write(k5))
        self.wait(2.5)
        k6 = Tex("People moved for work, settled on leftover land,").scale(0.85).shift(band_shift(10) + DOWN * 3.0)
        k7 = Tex("and the leftover land belonged to the water").scale(0.85).shift(band_shift(10) + DOWN * 3.7)
        self.play(Write(k6))
        self.play(Write(k7))
        self.play(Create(SurroundingRectangle(k7, color=GREEN)))
        self.wait(3)
