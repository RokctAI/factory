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

# Band-layout whiteboard scene (see AUTHORING spec / quadratics-by-factorisation
# reference). One band per teaching beat, add-only lifecycle, camera moves down
# between bands. Covers all seven subtopics of the duo: Part 1 Expert
# (three-event Venns, tree diagrams, contingency tables, choosing the tool)
# then Part 2 Simplifier (eight rooms, the sweet packet remembers, the register
# at the school gate). Band dwell times proportional to subtopics.json
# (235/230/225/225/195/190/195 of 1495 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ThreeToolsOfProbabilitySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): three-event Venn — the eight regions ---
        title = Tex("Tree Diagrams, Tables and Three-Event Venns").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Three circles cut the rectangle into 8 regions").scale(1.1).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("3 single-code, 3 exactly-two, 1 centre, 1 outside").scale(1.1).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_rule = Tex("Start at the CENTRE and work outwards").scale(1.15).shift(DOWN * 1.1)
        self.play(Write(b0_rule))
        self.play(Create(SurroundingRectangle(b0_rule, color=GREEN)))
        self.wait(2)
        b0_l3 = Tex(r"``15 play S and A'' includes the centre: $15 - 5$").scale(1.05).shift(DOWN * 2.2)
        self.play(Write(b0_l3))
        self.wait(3)

        # --- Band 1 (subtopic_1): the 150-learner survey, filled in ---
        self.next_band(1)
        b1_title = Tex("150 learners: soccer, netball, athletics").scale(1.15).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        vc = band_shift(1) + DOWN * 0.7
        box = Rectangle(width=7.6, height=4.8).move_to(vc)
        cS = Circle(radius=1.5, color=BLUE).move_to(vc + LEFT * 0.85 + UP * 0.55)
        cN = Circle(radius=1.5, color=YELLOW).move_to(vc + RIGHT * 0.85 + UP * 0.55)
        cA = Circle(radius=1.5, color=RED).move_to(vc + DOWN * 0.85)
        lS = Tex("S").scale(1.0).move_to(vc + LEFT * 2.6 + UP * 1.9)
        lN = Tex("N").scale(1.0).move_to(vc + RIGHT * 2.6 + UP * 1.9)
        lA = Tex("A").scale(1.0).move_to(vc + RIGHT * 1.7 + DOWN * 2.0)
        self.play(Create(box), Create(cS), Create(cN), Create(cA))
        self.play(Write(lS), Write(lN), Write(lA))
        self.wait(2)
        n_mid = MathTex("5").scale(0.9).move_to(vc + UP * 0.1)
        self.play(Write(n_mid))
        self.wait(2)
        n_sn = MathTex("10").scale(0.9).move_to(vc + UP * 1.0)
        n_sa = MathTex("15").scale(0.9).move_to(vc + LEFT * 0.9 + DOWN * 0.65)
        n_na = MathTex("8").scale(0.9).move_to(vc + RIGHT * 0.9 + DOWN * 0.65)
        self.play(Write(n_sn), Write(n_sa), Write(n_na))
        self.wait(2)
        n_s = MathTex("30").scale(0.9).move_to(vc + LEFT * 1.6 + UP * 1.0)
        n_n = MathTex("22").scale(0.9).move_to(vc + RIGHT * 1.6 + UP * 1.0)
        n_a = MathTex("25").scale(0.9).move_to(vc + DOWN * 1.6)
        self.play(Write(n_s), Write(n_n), Write(n_a))
        self.wait(2)
        n_out = MathTex("35").scale(0.9).move_to(vc + RIGHT * 3.3 + DOWN * 2.0)
        b1_sum = MathTex(r"150 - 115 = 35 \text{ outside}").scale(1.0).shift(band_shift(1) + DOWN * 3.6)
        self.play(Write(b1_sum))
        self.play(Write(n_out))
        self.wait(3)

        # --- Band 2 (subtopic_1): reading answers off the diagram ---
        self.next_band(2)
        b2_title = Tex("The diagram answers anything").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1a = Tex("Exactly one code:").scale(1.05).shift(band_shift(2) + UP * 1.2)
        b2_l1 = MathTex(r"\tfrac{30+22+25}{150} = \tfrac{77}{150}").scale(1.1).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1a))
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2a = Tex("At least two codes:").scale(1.05).shift(band_shift(2) + DOWN * 0.4)
        b2_l2 = MathTex(r"\tfrac{10+15+8+5}{150} = \tfrac{19}{75}").scale(1.1).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l2a))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"P(\text{soccer}) = \tfrac{60}{150} = \tfrac{2}{5}").scale(1.1).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the tree — 3 red, 2 blue, no replacement ---
        self.next_band(3)
        b3_title = Tex("Tree: 3 red, 2 blue — drawn without replacement").scale(1.1).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        tc = band_shift(3) + DOWN * 0.5
        root = Dot(tc + LEFT * 3.4)
        nR = Dot(tc + LEFT * 0.9 + UP * 1.5)
        nB = Dot(tc + LEFT * 0.9 + DOWN * 1.5)
        e1 = Line(root.get_center(), nR.get_center())
        e2 = Line(root.get_center(), nB.get_center())
        p1 = MathTex(r"\tfrac{3}{5}").scale(0.9).move_to(tc + LEFT * 2.5 + UP * 1.2)
        p2 = MathTex(r"\tfrac{2}{5}").scale(0.9).move_to(tc + LEFT * 2.5 + DOWN * 1.2)
        tR = MathTex("R").scale(0.9).move_to(nR.get_center() + UP * 0.4)
        tB = MathTex("B").scale(0.9).move_to(nB.get_center() + DOWN * 0.4)
        self.play(Create(e1), Create(e2), Create(root), Create(nR), Create(nB))
        self.play(Write(p1), Write(p2), Write(tR), Write(tB))
        self.wait(2)
        note = Tex("After a red: 2R, 2B left. After a blue: 3R, 1B").scale(0.95).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(note))
        self.wait(2)
        ends = [tc + RIGHT * 1.7 + UP * 2.2, tc + RIGHT * 1.7 + UP * 0.8,
                tc + RIGHT * 1.7 + DOWN * 0.8, tc + RIGHT * 1.7 + DOWN * 2.2]
        e3 = Line(nR.get_center(), ends[0]); e4 = Line(nR.get_center(), ends[1])
        e5 = Line(nB.get_center(), ends[2]); e6 = Line(nB.get_center(), ends[3])
        p3 = MathTex(r"\tfrac{2}{4}").scale(0.8).move_to(tc + RIGHT * 0.3 + UP * 2.15)
        p4 = MathTex(r"\tfrac{2}{4}").scale(0.8).move_to(tc + RIGHT * 0.3 + UP * 0.85)
        p5 = MathTex(r"\tfrac{3}{4}").scale(0.8).move_to(tc + RIGHT * 0.3 + DOWN * 0.85)
        p6 = MathTex(r"\tfrac{1}{4}").scale(0.8).move_to(tc + RIGHT * 0.3 + DOWN * 2.15)
        o1 = MathTex(r"RR").scale(0.85).move_to(ends[0] + RIGHT * 0.6)
        o2 = MathTex(r"RB").scale(0.85).move_to(ends[1] + RIGHT * 0.6)
        o3 = MathTex(r"BR").scale(0.85).move_to(ends[2] + RIGHT * 0.6)
        o4 = MathTex(r"BB").scale(0.85).move_to(ends[3] + RIGHT * 0.6)
        self.play(Create(e3), Create(e4), Create(e5), Create(e6))
        self.play(Write(p3), Write(p4), Write(p5), Write(p6))
        self.play(Write(o1), Write(o2), Write(o3), Write(o4))
        self.wait(3)

        # --- Band 4 (subtopic_2): multiply along, add across, audit to 1 ---
        self.next_band(4)
        b4_title = Tex("Multiply along a path, add between paths").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"P(RR) = \tfrac{3}{5} \times \tfrac{2}{4} = \tfrac{6}{20} = \tfrac{3}{10}").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"P(\text{one of each}) = \tfrac{6}{20} + \tfrac{6}{20} = \tfrac{3}{5}").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"P(BB) = \tfrac{2}{5} \times \tfrac{1}{4} = \tfrac{2}{20}").scale(1.1).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"\text{Audit: } \tfrac{6+6+6+2}{20} = 1").scale(1.1).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_rule = Tex("Paths must total 1 — the tree's receipt").scale(1.05).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_rule))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the contingency table, margins first ---
        self.next_band(5)
        b5_title = Tex("Contingency table: 200 learners").scale(1.15).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_title))
        self.wait(1.5)
        gc = band_shift(5) + DOWN * 0.2
        h1 = Line(gc + LEFT * 3.4 + UP * 1.0, gc + RIGHT * 3.4 + UP * 1.0)
        h2 = Line(gc + LEFT * 3.4 + DOWN * 1.4, gc + RIGHT * 3.4 + DOWN * 1.4)
        v1 = Line(gc + LEFT * 1.7 + UP * 1.8, gc + LEFT * 1.7 + DOWN * 2.2)
        v2 = Line(gc + RIGHT * 1.7 + UP * 1.8, gc + RIGHT * 1.7 + DOWN * 2.2)
        self.play(Create(h1), Create(h2), Create(v1), Create(v2))
        hw = Tex("Walk").scale(0.9).move_to(gc + LEFT * 0.85 + UP * 1.4)
        ht = Tex("Taxi").scale(0.9).move_to(gc + RIGHT * 0.85 + UP * 1.4)
        htot = Tex("Total").scale(0.9).move_to(gc + RIGHT * 2.6 + UP * 1.4)
        rb = Tex("Boys").scale(0.9).move_to(gc + LEFT * 2.6 + UP * 0.4)
        rg = Tex("Girls").scale(0.9).move_to(gc + LEFT * 2.6 + DOWN * 0.7)
        rt = Tex("Total").scale(0.9).move_to(gc + LEFT * 2.6 + DOWN * 1.8)
        self.play(Write(hw), Write(ht), Write(htot), Write(rb), Write(rg), Write(rt))
        self.wait(2)
        c11 = MathTex("30").scale(0.9).move_to(gc + LEFT * 0.85 + UP * 0.4)
        c12 = MathTex("50").scale(0.9).move_to(gc + RIGHT * 0.85 + UP * 0.4)
        c13 = MathTex("80").scale(0.9).move_to(gc + RIGHT * 2.6 + UP * 0.4)
        self.play(Write(c11), Write(c12), Write(c13))
        self.wait(2)
        c21 = MathTex("45").scale(0.9).move_to(gc + LEFT * 0.85 + DOWN * 0.7)
        c22 = MathTex("75").scale(0.9).move_to(gc + RIGHT * 0.85 + DOWN * 0.7)
        c23 = MathTex("120").scale(0.9).move_to(gc + RIGHT * 2.6 + DOWN * 0.7)
        self.play(Write(c21), Write(c22), Write(c23))
        self.wait(2)
        c31 = MathTex("75").scale(0.9).move_to(gc + LEFT * 0.85 + DOWN * 1.8)
        c32 = MathTex("125").scale(0.9).move_to(gc + RIGHT * 0.85 + DOWN * 1.8)
        c33 = MathTex("200").scale(0.9).move_to(gc + RIGHT * 2.6 + DOWN * 1.8)
        self.play(Write(c31), Write(c32), Write(c33))
        self.wait(2)
        b5_l1 = MathTex(r"P(\text{boy who walks}) = \tfrac{30}{200} = 0{,}15").scale(1.0).shift(band_shift(5) + DOWN * 3.3)
        self.play(Write(b5_l1))
        self.wait(3)

        # --- Band 6 (subtopic_3): the product test for independence ---
        self.next_band(6)
        b6_title = Tex("Is gender independent of transport?").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1a = MathTex(r"P(\text{boy}) = \tfrac{80}{200} = 0{,}4").scale(1.05).shift(band_shift(6) + UP * 1.3)
        b6_l1 = MathTex(r"P(\text{walk}) = \tfrac{75}{200} = 0{,}375").scale(1.05).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1a))
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"0{,}4 \times 0{,}375 = 0{,}15 = P(\text{boy and walk})").scale(1.05).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Equal — independent").scale(1.1).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex(r"Rows agree: both walk rates are $37{,}5\%$").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex(r"Tilt to 40 vs 35: $0{,}2 \neq 0{,}15$ — dependent").scale(1.0).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): choosing the tool from the wording ---
        self.next_band(7)
        b7_title = Tex("Choose the tool from the wording").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("``or, and, only, neither'' $\\Rightarrow$ Venn diagram").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("``first, then, without replacement'' $\\Rightarrow$ tree").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Two characteristics tabulated $\\Rightarrow$ table").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("``independent'' $\\Rightarrow$ run the product test").scale(1.05).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Finish with the sentence, numbers included").scale(1.05).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # --- Band 8 (subtopic_4): mixing tools and rules — rain and the match ---
        self.next_band(8)
        b8_title = Tex("Rain then result: weather is a tree").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"P(\text{rain}) = 0{,}3: \; P(\text{win} \mid \text{rain}) = 0{,}4").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"P(\text{rain and win}) = 0{,}3 \times 0{,}4 = 0{,}12").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = MathTex(r"P(\text{dry and win}) = 0{,}7 \times 0{,}65 = 0{,}455").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = MathTex(r"P(\text{win}) = 0{,}12 + 0{,}455 = 0{,}575").scale(1.1).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): eight rooms, filled from the middle ---
        self.next_band(9)
        b9_title = Tex("Eight rooms, filled from the middle").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("The middle room's number arrives clean: 5 go in").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Shared rooms, loyal rooms, then the stoep").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"150 - 115 = 35 \text{ on the stoep}").scale(1.1).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("``S and A but not N'' $= 15$: straight in").scale(1.05).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("``S and A'' includes the heroes: $15 - 5 = 10$").scale(1.05).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_6): the sweet packet remembers ---
        self.next_band(10)
        b10_title = Tex("The sweet packet remembers").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("After a red goes: 2R, 2B — a different world").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{AND multiplies: } \tfrac{3}{5} \times \tfrac{2}{4} = \tfrac{3}{10}").scale(1.05).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"\text{OR adds: } \tfrac{6}{20} + \tfrac{6}{20} = \tfrac{3}{5}").scale(1.05).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = MathTex(r"\text{Receipt: } \tfrac{6+6+6+2}{20} = 1").scale(1.05).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): the register at the school gate ---
        self.next_band(11)
        b11_title = Tex("The register at the school gate").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex("Margins keep the totals: 80, 120, 75, 125").scale(1.05).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = Tex(r"Boys who walk: $\tfrac{30}{80} = 37{,}5\%$").scale(1.05).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11_l2))
        self.wait(2)
        b11_l3 = Tex(r"Girls who walk: $\tfrac{45}{120} = 37{,}5\%$ — same story").scale(1.05).shift(band_shift(11) + DOWN * 0.7)
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = MathTex(r"0{,}4 \times 0{,}375 = 0{,}15 \;\Rightarrow\; \text{independent}").scale(1.05).shift(band_shift(11) + DOWN * 1.7)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        self.wait(2.5)
        b11_l5 = Tex(r"Tilt the rows ($50\%$ vs $29\%$): dependent").scale(1.05).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11_l5))
        self.wait(4)
