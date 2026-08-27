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

# Band-layout whiteboard scene for "Free Basic Water and Sustainable Water
# Use" (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier 5-7). Exporter-
# safe primitives only: the Lesotho transfer is a Line cross-section with a
# gravity Arrow, and the five purification gates are a Rectangle+Arrow chain.
# Add-only lifecycle; camera moves down band by band.
# Band time apportioned to subtopics.json (235/245/250/230/190/185/165
# of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class FreeBasicWaterSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the legal spine ---
        title = Tex("Free Basic Water and Sustainable Use").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l1 = Tex("Section 27: the right of access to sufficient water").scale(0.95).shift(UP * 1.1)
        self.play(Write(l1))
        self.wait(2)
        l2 = Tex("National Water Act 1998: water held in public trust;").scale(0.9).shift(UP * 0.2)
        l3 = Tex("the RESERVE set aside first — people and rivers").scale(0.9).shift(DOWN * 0.6)
        self.play(Write(l2))
        self.play(Write(l3))
        self.play(Create(SurroundingRectangle(l3, color=GREEN)))
        self.wait(2.5)
        l4 = Tex("Free basic water (2001): the right becomes a number").scale(0.9).shift(DOWN * 1.6)
        self.play(Write(l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the six kilolitres and the tariff ---
        self.next_band(1)
        b1_title = Tex("The allowance and the bill").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        a1 = MathTex(r"25 \tfrac{\ell}{\text{person day}} \times 8 \times 30 \approx 6\,000\ \ell/\text{month}").scale(0.95).shift(band_shift(1) + UP * 1.3)
        self.play(Write(a1))
        self.play(Create(SurroundingRectangle(a1, color=GREEN)))
        self.wait(2.5)
        a2 = Tex("Within 200 m of the home; a floor, not comfort").scale(0.9).shift(band_shift(1) + UP * 0.3)
        a3 = Tex("(suburban use $\\approx 150\\ \\ell$ per person per day)").scale(0.85).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(a2))
        self.play(Write(a3))
        self.wait(2.5)
        a4 = Tex("Rising block tariff: first block free,").scale(0.9).shift(band_shift(1) + DOWN * 1.5)
        a5 = Tex("each further block dearer — the irrigated lawn").scale(0.9).shift(band_shift(1) + DOWN * 2.3)
        a6 = Tex("helps pay for the village standpipe").scale(0.9).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(a4))
        self.play(Write(a5))
        self.play(Write(a6))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): rural challenges ---
        self.next_band(2)
        b2_title = Tex("Rural delivery: distance and decay").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        r1 = Tex("Scattered settlements: every km of pipe").scale(0.9).shift(band_shift(2) + UP * 1.4)
        r2 = Tex("serves a handful of households").scale(0.9).shift(band_shift(2) + UP * 0.7)
        self.play(Write(r1))
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex("Fragile sources: small dams, springs, boreholes").scale(0.9).shift(band_shift(2) + DOWN * 0.2)
        r4 = Tex("Maintenance trap: built on grants, breaks unrepaired").scale(0.85).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(r3))
        self.play(Write(r4))
        self.wait(2.5)
        r5 = Tex("Women and girls carry the failure;").scale(0.9).shift(band_shift(2) + DOWN * 2.0)
        r6 = Tex("shared water brings cholera back").scale(0.9).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(r5))
        self.play(Write(r6))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): urban challenges ---
        self.next_band(3)
        b3_title = Tex("Urban delivery: speed, money, leaks").scale(1.1).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        u1 = Tex("People arrive faster than pipes:").scale(0.9).shift(band_shift(3) + UP * 1.4)
        u2 = Tex("informal settlements on unserviced land").scale(0.9).shift(band_shift(3) + UP * 0.7)
        self.play(Write(u1))
        self.play(Write(u2))
        self.wait(2)
        u3 = Tex("Unemployment: revenue fails, disputes flare").scale(0.9).shift(band_shift(3) + DOWN * 0.2)
        self.play(Write(u3))
        self.wait(2)
        u4 = Tex("Non-revenue water: a third or more lost —").scale(0.9).shift(band_shift(3) + DOWN * 1.1)
        u5 = Tex("treat three litres to sell two").scale(0.9).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(u4))
        self.play(Write(u5))
        self.play(Create(SurroundingRectangle(u5, color=GREEN)))
        self.wait(2)
        u6 = Tex("Beneath both: municipalities short of money,").scale(0.9).shift(band_shift(3) + DOWN * 2.8)
        u7 = Tex("skills and maintenance discipline").scale(0.9).shift(band_shift(3) + DOWN * 3.5)
        self.play(Write(u6))
        self.play(Write(u7))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): transfers — gravity vs pumping ---
        self.next_band(4)
        b4_title = Tex("Inter-basin transfers").scale(1.15).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_title))
        self.wait(1.5)
        # cross-section: Lesotho highlands (high, right) down to Gauteng (left)
        p_gau = band_shift(4) + LEFT * 5.0 + DOWN * 0.6
        p_mid = band_shift(4) + LEFT * 0.6 + UP * 0.4
        p_les = band_shift(4) + RIGHT * 3.4 + UP * 1.8
        prof1 = Line(p_gau, p_mid, stroke_width=5)
        prof2 = Line(p_mid, p_les, stroke_width=5)
        self.play(Create(prof1), Create(prof2))
        dam = Dot(p_les, color=BLUE)
        dam_lab = Tex("Katse, Mohale, Polihali").scale(0.75).shift(p_les + UP * 0.6 + LEFT * 0.4)
        gau_lab = Tex("Gauteng / Vaal system").scale(0.75).shift(p_gau + UP * 0.6 + RIGHT * 0.4)
        self.play(FadeIn(dam), Write(dam_lab), Write(gau_lab))
        flow = Arrow(p_les + DOWN * 0.15 + LEFT * 0.3, p_gau + UP * 0.25 + RIGHT * 0.5,
                     buff=0, color=BLUE, stroke_width=5)
        flow_lab = Tex("downhill all the way — gravity is free").scale(0.8).shift(band_shift(4) + LEFT * 0.6 + DOWN * 1.1)
        self.play(Create(flow), Write(flow_lab))
        self.wait(2.5)
        t1 = Tex("Lesotho earns royalties and power; Gauteng drinks").scale(0.85).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(t1))
        self.wait(2)
        t2 = Tex("Tugela-Vaal fights gravity: pumped up the").scale(0.85).shift(band_shift(4) + DOWN * 2.7)
        t3 = Tex("escarpment to Sterkfontein — the drought reserve").scale(0.85).shift(band_shift(4) + DOWN * 3.4)
        self.play(Write(t2))
        self.play(Write(t3))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): dams and the five purification gates ---
        self.next_band(5)
        b5_title = Tex("Dams, and the five gates").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        d1 = Tex("Gariep, Vanderkloof, Vaal Dam: hold the summer").scale(0.9).shift(band_shift(5) + UP * 1.5)
        d2 = Tex("for the winter, paying the evaporation tax").scale(0.9).shift(band_shift(5) + UP * 0.8)
        self.play(Write(d1))
        self.play(Write(d2))
        self.wait(2)
        steps = ["1 screen", "2 coagulate", "3 settle", "4 filter", "5 chlorinate"]
        xs = [-5.0, -2.5, 0.0, 2.5, 5.0]
        prev = None
        for x, s in zip(xs, steps):
            box = Rectangle(width=2.2, height=0.9).shift(band_shift(5) + RIGHT * x + DOWN * 0.4)
            lab = Tex(s).scale(0.7).shift(band_shift(5) + RIGHT * x + DOWN * 0.4)
            self.play(Create(box), Write(lab), run_time=0.7)
            if prev is not None:
                ar = Arrow(band_shift(5) + RIGHT * (prev + 1.1) + DOWN * 0.4,
                           band_shift(5) + RIGHT * (x - 1.1) + DOWN * 0.4,
                           buff=0, stroke_width=4, color=BLUE)
                self.play(Create(ar), run_time=0.4)
            prev = x
        self.wait(2)
        d3 = Tex("Dosed aluminium sulphate binds fine dirt into flocs;").scale(0.85).shift(band_shift(5) + DOWN * 1.7)
        d4 = Tex("chlorine (or ozone, UV) ends the microbes").scale(0.85).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(d3))
        self.play(Write(d4))
        self.wait(2)
        d5 = Tex("Blue Drop audits drinking water; Green Drop, sewage").scale(0.85).shift(band_shift(5) + DOWN * 3.3)
        self.play(Write(d5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the state's list ---
        self.next_band(6)
        b6_title = Tex("Sustainability: the state's half").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        g1 = Tex("Stop the bleeding: pipes, meters, pressure").scale(0.9).shift(band_shift(6) + UP * 1.4)
        g2 = Tex("Defend quality: sewage works, acid mine drainage").scale(0.9).shift(band_shift(6) + UP * 0.6)
        g3 = Tex("Working for Water: jobs that free rivers").scale(0.9).shift(band_shift(6) + DOWN * 0.2)
        g4 = Tex("Price for restraint: blocks and restrictions").scale(0.9).shift(band_shift(6) + DOWN * 1.0)
        g5 = Tex("Diversify: desalination, reused wastewater").scale(0.9).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(g1))
        self.wait(1.5)
        self.play(Write(g2))
        self.wait(1.5)
        self.play(Write(g3))
        self.wait(1.5)
        self.play(Write(g4))
        self.wait(1.5)
        self.play(Write(g5))
        self.play(Create(SurroundingRectangle(g3, color=GREEN)))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): the citizen's list, and two cities ---
        self.next_band(7)
        b7_title = Tex("The citizen's half").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        c1 = Tex("Mend the drip; shower short; close the tap;").scale(0.9).shift(band_shift(7) + UP * 1.4)
        c2 = Tex("tank the rain; greywater to the garden;").scale(0.9).shift(band_shift(7) + UP * 0.6)
        c3 = Tex("indigenous plants; water at dusk; report leaks").scale(0.9).shift(band_shift(7) + DOWN * 0.2)
        self.play(Write(c1))
        self.play(Write(c2))
        self.play(Write(c3))
        self.wait(2.5)
        c4 = Tex("Cape Town 2018: use roughly halved, taps stayed open").scale(0.85).shift(band_shift(7) + DOWN * 1.2)
        c5 = Tex("Nelson Mandela Bay 2022: late savings,").scale(0.85).shift(band_shift(7) + DOWN * 2.0)
        c6 = Tex("unfixed leaks — a crisis stretched over years").scale(0.85).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(c4))
        self.wait(2)
        self.play(Write(c5))
        self.play(Write(c6))
        self.play(Create(SurroundingRectangle(c4, color=GREEN)))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the first six thousand litres ---
        self.next_band(8)
        b8_title = Tex("The first six thousand litres").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        s1 = Tex("25 litres = two ten-litre buckets and a kettle,").scale(0.9).shift(band_shift(8) + UP * 1.3)
        s2 = Tex("per person, per day — every sip, meal and wash").scale(0.9).shift(band_shift(8) + UP * 0.5)
        self.play(Write(s1))
        self.play(Write(s2))
        self.wait(2.5)
        s3 = Tex("A staircase of prices: cheap bottom steps,").scale(0.9).shift(band_shift(8) + DOWN * 0.4)
        s4 = Tex("stinging top steps that fund the free water").scale(0.9).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(s3))
        self.play(Write(s4))
        self.wait(2.5)
        s5 = Tex("Access is a paper word: the promise is policy,").scale(0.9).shift(band_shift(8) + DOWN * 2.1)
        s6 = Tex("the truth is buckets, queues and repairs").scale(0.9).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(s5))
        self.play(Write(s6))
        self.play(Create(SurroundingRectangle(s6, color=GREEN)))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): moving a river over a mountain ---
        self.next_band(9)
        b9_title = Tex("Moving a river over a mountain").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        m1 = Tex("Gauteng: built where the gold was,").scale(0.95).shift(band_shift(9) + UP * 1.3)
        m2 = Tex("not where the water is").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(m1))
        self.play(Write(m2))
        self.wait(2.5)
        m3 = Tex("Lesotho: heavy rain, higher ground —").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        m4 = Tex("dam it, tunnel it, let gravity deliver").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(m3))
        self.play(Write(m4))
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(2.5)
        m5 = Tex("Downhill water is cheap; pumped water is precious —").scale(0.85).shift(band_shift(9) + DOWN * 2.1)
        m6 = Tex("five gates: screen, clump, settle, filter, chlorinate").scale(0.85).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(m5))
        self.play(Write(m6))
        self.wait(2.5)

        # --- Band 10 (subtopic_7): the city that counted its days ---
        self.next_band(10)
        b10_title = Tex("The city that counted its days").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        z1 = Tex("Day Zero, 2018: the date the taps would shut").scale(0.9).shift(band_shift(10) + UP * 1.3)
        self.play(Write(z1))
        self.wait(2)
        z2 = Tex("Cape Town halved its use — buckets, tanks,").scale(0.9).shift(band_shift(10) + UP * 0.4)
        z3 = Tex("greywater, brown lawns, weekly dam levels").scale(0.9).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(z2))
        self.play(Write(z3))
        self.wait(2.5)
        z4 = Tex("The cheapest new dam is the water").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        z5 = Tex("a city stops wasting").scale(0.95).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(z4))
        self.play(Write(z5))
        self.play(Create(SurroundingRectangle(z5, color=GREEN)))
        self.wait(2)
        z6 = Tex("Neither half works alone: citizens and pipes,").scale(0.9).shift(band_shift(10) + DOWN * 3.0)
        z7 = Tex("habits and maintenance, together").scale(0.9).shift(band_shift(10) + DOWN * 3.7)
        self.play(Write(z6))
        self.play(Write(z7))
        self.wait(3)
