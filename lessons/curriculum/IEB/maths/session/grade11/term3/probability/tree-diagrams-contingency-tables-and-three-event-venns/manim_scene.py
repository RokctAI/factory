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

# Band-layout whiteboard scene. One band per teaching beat, add-only lifecycle,
# camera moves down between bands. Covers all seven subtopics of the duo:
# Part 1 Expert (three-event Venns, tree diagrams, contingency tables,
# choosing the tool) then Part 2 Simplifier (eight rooms, the sweet packet
# remembers, the register at the school gate). Band dwell times proportional
# to subtopics.json (235/230/225/225/195/190/195 of 1495 s).

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
        b0_l2 = Tex("3 single-activity, 3 exactly-two, 1 centre, 1 outside").scale(1.05).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_rule = Tex("Start at the CENTRE and build outwards").scale(1.15).shift(DOWN * 1.1)
        self.play(Write(b0_rule))
        self.play(Create(SurroundingRectangle(b0_rule, color=GREEN)))
        self.wait(2)
        b0_l3 = Tex(r"``12 do C and D'' includes the centre: $12 - 4$").scale(1.05).shift(DOWN * 2.2)
        self.play(Write(b0_l3))
        self.wait(3)

        # --- Band 1 (subtopic_1): the 120-learner survey, filled in ---
        self.next_band(1)
        b1_title = Tex("120 learners: choir, drama, chess").scale(1.15).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        vc = band_shift(1) + DOWN * 0.7
        box = Rectangle(width=7.6, height=4.8).move_to(vc)
        cC = Circle(radius=1.5, color=BLUE).move_to(vc + LEFT * 0.85 + UP * 0.55)
        cD = Circle(radius=1.5, color=YELLOW).move_to(vc + RIGHT * 0.85 + UP * 0.55)
        cH = Circle(radius=1.5, color=RED).move_to(vc + DOWN * 0.85)
        lC = Tex("C").scale(1.0).move_to(vc + LEFT * 2.6 + UP * 1.9)
        lD = Tex("D").scale(1.0).move_to(vc + RIGHT * 2.6 + UP * 1.9)
        lH = Tex("Ch").scale(1.0).move_to(vc + RIGHT * 1.7 + DOWN * 2.0)
        self.play(Create(box), Create(cC), Create(cD), Create(cH))
        self.play(Write(lC), Write(lD), Write(lH))
        self.wait(2)
        n_mid = MathTex("4").scale(0.9).move_to(vc + UP * 0.1)
        self.play(Write(n_mid))
        self.wait(2)
        n_cd = MathTex("12").scale(0.9).move_to(vc + UP * 1.0)
        n_ch = MathTex("9").scale(0.9).move_to(vc + LEFT * 0.9 + DOWN * 0.65)
        n_dh = MathTex("7").scale(0.9).move_to(vc + RIGHT * 0.9 + DOWN * 0.65)
        self.play(Write(n_cd), Write(n_ch), Write(n_dh))
        self.wait(2)
        n_c = MathTex("25").scale(0.9).move_to(vc + LEFT * 1.6 + UP * 1.0)
        n_d = MathTex("18").scale(0.9).move_to(vc + RIGHT * 1.6 + UP * 1.0)
        n_h = MathTex("20").scale(0.9).move_to(vc + DOWN * 1.6)
        self.play(Write(n_c), Write(n_d), Write(n_h))
        self.wait(2)
        n_out = MathTex("25").scale(0.9).move_to(vc + RIGHT * 3.3 + DOWN * 2.0)
        b1_sum = MathTex(r"120 - 95 = 25 \text{ outside}").scale(1.0).shift(band_shift(1) + DOWN * 3.6)
        self.play(Write(b1_sum))
        self.play(Write(n_out))
        self.wait(3)

        # --- Band 2 (subtopic_1): reading answers off the diagram ---
        self.next_band(2)
        b2_title = Tex("The diagram answers anything").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1a = Tex("Exactly one activity:").scale(1.05).shift(band_shift(2) + UP * 1.2)
        b2_l1 = MathTex(r"\tfrac{25+18+20}{120} = \tfrac{21}{40}").scale(1.1).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1a))
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2a = Tex("At least two activities:").scale(1.05).shift(band_shift(2) + DOWN * 0.4)
        b2_l2 = MathTex(r"\tfrac{12+9+7+4}{120} = \tfrac{4}{15}").scale(1.1).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l2a))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"P(\text{choir}) = \tfrac{50}{120} = \tfrac{5}{12}").scale(1.1).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the tree — 4 orange, 2 mint, no replacement ---
        self.next_band(3)
        b3_title = Tex("Tree: 4 orange, 2 mint — drawn without replacement").scale(1.05).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        tc = band_shift(3) + DOWN * 0.5
        root = Dot(tc + LEFT * 3.4)
        nO = Dot(tc + LEFT * 0.9 + UP * 1.5)
        nM = Dot(tc + LEFT * 0.9 + DOWN * 1.5)
        e1 = Line(root.get_center(), nO.get_center())
        e2 = Line(root.get_center(), nM.get_center())
        p1 = MathTex(r"\tfrac{4}{6}").scale(0.9).move_to(tc + LEFT * 2.5 + UP * 1.2)
        p2 = MathTex(r"\tfrac{2}{6}").scale(0.9).move_to(tc + LEFT * 2.5 + DOWN * 1.2)
        tO = MathTex("O").scale(0.9).move_to(nO.get_center() + UP * 0.4)
        tM = MathTex("M").scale(0.9).move_to(nM.get_center() + DOWN * 0.4)
        self.play(Create(e1), Create(e2), Create(root), Create(nO), Create(nM))
        self.play(Write(p1), Write(p2), Write(tO), Write(tM))
        self.wait(2)
        note = Tex("After an orange: 3O, 2M left. After a mint: 4O, 1M").scale(0.9).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(note))
        self.wait(2)
        ends = [tc + RIGHT * 1.7 + UP * 2.2, tc + RIGHT * 1.7 + UP * 0.8,
                tc + RIGHT * 1.7 + DOWN * 0.8, tc + RIGHT * 1.7 + DOWN * 2.2]
        e3 = Line(nO.get_center(), ends[0]); e4 = Line(nO.get_center(), ends[1])
        e5 = Line(nM.get_center(), ends[2]); e6 = Line(nM.get_center(), ends[3])
        p3 = MathTex(r"\tfrac{3}{5}").scale(0.8).move_to(tc + RIGHT * 0.3 + UP * 2.15)
        p4 = MathTex(r"\tfrac{2}{5}").scale(0.8).move_to(tc + RIGHT * 0.3 + UP * 0.85)
        p5 = MathTex(r"\tfrac{4}{5}").scale(0.8).move_to(tc + RIGHT * 0.3 + DOWN * 0.85)
        p6 = MathTex(r"\tfrac{1}{5}").scale(0.8).move_to(tc + RIGHT * 0.3 + DOWN * 2.15)
        o1 = MathTex(r"OO").scale(0.85).move_to(ends[0] + RIGHT * 0.6)
        o2 = MathTex(r"OM").scale(0.85).move_to(ends[1] + RIGHT * 0.6)
        o3 = MathTex(r"MO").scale(0.85).move_to(ends[2] + RIGHT * 0.6)
        o4 = MathTex(r"MM").scale(0.85).move_to(ends[3] + RIGHT * 0.6)
        self.play(Create(e3), Create(e4), Create(e5), Create(e6))
        self.play(Write(p3), Write(p4), Write(p5), Write(p6))
        self.play(Write(o1), Write(o2), Write(o3), Write(o4))
        self.wait(3)

        # --- Band 4 (subtopic_2): multiply along, add across, audit to 1 ---
        self.next_band(4)
        b4_title = Tex("Multiply along a path, add between paths").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"P(OO) = \tfrac{4}{6} \times \tfrac{3}{5} = \tfrac{12}{30} = \tfrac{2}{5}").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"P(\text{one of each}) = \tfrac{8}{30} + \tfrac{8}{30} = \tfrac{8}{15}").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"P(MM) = \tfrac{2}{6} \times \tfrac{1}{5} = \tfrac{2}{30}").scale(1.1).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"\text{Audit: } \tfrac{12+8+8+2}{30} = 1").scale(1.1).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_rule = Tex("Paths must total 1 — the tree's receipt").scale(1.05).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_rule))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the contingency table, margins first ---
        self.next_band(5)
        b5_title = Tex("Contingency table: 160 learners").scale(1.15).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_title))
        self.wait(1.5)
        gc = band_shift(5) + DOWN * 0.2
        h1 = Line(gc + LEFT * 3.4 + UP * 1.0, gc + RIGHT * 3.4 + UP * 1.0)
        h2 = Line(gc + LEFT * 3.4 + DOWN * 1.4, gc + RIGHT * 3.4 + DOWN * 1.4)
        v1 = Line(gc + LEFT * 1.7 + UP * 1.8, gc + LEFT * 1.7 + DOWN * 2.2)
        v2 = Line(gc + RIGHT * 1.7 + UP * 1.8, gc + RIGHT * 1.7 + DOWN * 2.2)
        self.play(Create(h1), Create(h2), Create(v1), Create(v2))
        hc = Tex("Cycle").scale(0.9).move_to(gc + LEFT * 0.85 + UP * 1.4)
        hw = Tex("Walk").scale(0.9).move_to(gc + RIGHT * 0.85 + UP * 1.4)
        htot = Tex("Total").scale(0.9).move_to(gc + RIGHT * 2.6 + UP * 1.4)
        rb = Tex("Boys").scale(0.9).move_to(gc + LEFT * 2.6 + UP * 0.4)
        rg = Tex("Girls").scale(0.9).move_to(gc + LEFT * 2.6 + DOWN * 0.7)
        rt = Tex("Total").scale(0.9).move_to(gc + LEFT * 2.6 + DOWN * 1.8)
        self.play(Write(hc), Write(hw), Write(htot), Write(rb), Write(rg), Write(rt))
        self.wait(2)
        c11 = MathTex("24").scale(0.9).move_to(gc + LEFT * 0.85 + UP * 0.4)
        c12 = MathTex("36").scale(0.9).move_to(gc + RIGHT * 0.85 + UP * 0.4)
        c13 = MathTex("60").scale(0.9).move_to(gc + RIGHT * 2.6 + UP * 0.4)
        self.play(Write(c11), Write(c12), Write(c13))
        self.wait(2)
        c21 = MathTex("40").scale(0.9).move_to(gc + LEFT * 0.85 + DOWN * 0.7)
        c22 = MathTex("60").scale(0.9).move_to(gc + RIGHT * 0.85 + DOWN * 0.7)
        c23 = MathTex("100").scale(0.9).move_to(gc + RIGHT * 2.6 + DOWN * 0.7)
        self.play(Write(c21), Write(c22), Write(c23))
        self.wait(2)
        c31 = MathTex("64").scale(0.9).move_to(gc + LEFT * 0.85 + DOWN * 1.8)
        c32 = MathTex("96").scale(0.9).move_to(gc + RIGHT * 0.85 + DOWN * 1.8)
        c33 = MathTex("160").scale(0.9).move_to(gc + RIGHT * 2.6 + DOWN * 1.8)
        self.play(Write(c31), Write(c32), Write(c33))
        self.wait(2)
        b5_l1 = MathTex(r"P(\text{boy who cycles}) = \tfrac{24}{160} = 0{,}15").scale(1.0).shift(band_shift(5) + DOWN * 3.3)
        self.play(Write(b5_l1))
        self.wait(3)

        # --- Band 6 (subtopic_3): the product test for independence ---
        self.next_band(6)
        b6_title = Tex("Is gender independent of transport?").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1a = MathTex(r"P(\text{boy}) = \tfrac{60}{160} = 0{,}375").scale(1.05).shift(band_shift(6) + UP * 1.3)
        b6_l1 = MathTex(r"P(\text{cycle}) = \tfrac{64}{160} = 0{,}4").scale(1.05).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1a))
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"0{,}375 \times 0{,}4 = 0{,}15 = P(\text{boy and cycle})").scale(1.05).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Equal — independent").scale(1.1).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex(r"Rows agree: both cycling rates are $40\%$").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex(r"Tilt to 30 vs 34: $0{,}1875 \neq 0{,}15$ — dependent").scale(1.0).shift(band_shift(6) + DOWN * 2.9)
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

        # --- Band 8 (subtopic_4): mixing tools and rules — wind and the final ---
        self.next_band(8)
        b8_title = Tex("Wind then result: weather is a tree").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"P(\text{windy}) = 0{,}4: \; P(\text{win} \mid \text{windy}) = 0{,}35").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"P(\text{windy and win}) = 0{,}4 \times 0{,}35 = 0{,}14").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = MathTex(r"P(\text{calm and win}) = 0{,}6 \times 0{,}7 = 0{,}42").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = MathTex(r"P(\text{win}) = 0{,}14 + 0{,}42 = 0{,}56").scale(1.1).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): eight rooms, filled from the middle ---
        self.next_band(9)
        b9_title = Tex("Eight rooms, filled from the middle").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("The middle room's number arrives clean: 4 go in").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Shared rooms, loyal rooms, then the stoep").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"120 - 95 = 25 \text{ on the stoep}").scale(1.1).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("``C and D but not Ch'' $= 12$: straight in").scale(1.05).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("``C and D'' includes the heroes: $12 - 4 = 8$").scale(1.05).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_6): the sweet packet remembers ---
        self.next_band(10)
        b10_title = Tex("The sweet packet remembers").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("After an orange goes: 3O, 2M — a different world").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{AND multiplies: } \tfrac{4}{6} \times \tfrac{3}{5} = \tfrac{2}{5}").scale(1.05).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"\text{OR adds: } \tfrac{8}{30} + \tfrac{8}{30} = \tfrac{8}{15}").scale(1.05).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = MathTex(r"\text{Receipt: } \tfrac{12+8+8+2}{30} = 1").scale(1.05).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): the register at the school gate ---
        self.next_band(11)
        b11_title = Tex("The register at the school gate").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex("Margins keep the totals: 60, 100, 64, 96").scale(1.05).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = Tex(r"Boys who cycle: $\tfrac{24}{60} = 40\%$").scale(1.05).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11_l2))
        self.wait(2)
        b11_l3 = Tex(r"Girls who cycle: $\tfrac{40}{100} = 40\%$ — same story").scale(1.05).shift(band_shift(11) + DOWN * 0.7)
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = MathTex(r"0{,}375 \times 0{,}4 = 0{,}15 \;\Rightarrow\; \text{independent}").scale(1.05).shift(band_shift(11) + DOWN * 1.7)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        self.wait(2.5)
        b11_l5 = Tex(r"Tilt the rows ($50\%$ vs $34\%$): dependent").scale(1.05).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11_l5))
        self.wait(4)
