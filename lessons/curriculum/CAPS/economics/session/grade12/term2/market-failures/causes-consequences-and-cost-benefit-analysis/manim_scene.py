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

# Band layout: one frame-tall bands down a long canvas; camera moves down,
# nothing is removed. Exporter-safe mobjects only (Tex/MathTex/Line/Arrow/
# Dot/Circle/Rectangle/VGroup); write-only reveals — no Transform/FadeOut.
#
# Mirrors script.md across the seven subtopics of the duo
# (Expert 1-4: bands 0-7; Simplifier 5-7: bands 8-10), scene time
# apportioned to subtopics.json (235/255/245/240/195/190/210 of 1570 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MarketFailuresSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md plays (~4-5%).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the definition, causes 1-3 ---
        title = Tex("Market Failure and Cost-Benefit Analysis").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        wrong = Tex(r"Failure $=$ high prices, greedy firms").scale(0.95).shift(UP * 1.3 + LEFT * 2.4)
        self.play(Write(wrong))
        self.play(Create(strike(wrong)))
        self.wait(1.5)
        defn = Tex(r"Failure $=$ the QUANTITIES are wrong").scale(1.05).shift(UP * 0.4)
        self.play(Write(defn))
        self.play(Create(SurroundingRectangle(defn, color=GREEN)))
        self.wait(2.5)
        c1 = Tex(r"1. Externalities: costs land on third parties").scale(0.95).shift(DOWN * 0.6)
        c2 = Tex(r"2. Missing markets: public and merit goods").scale(0.95).shift(DOWN * 1.4)
        c3 = Tex(r"3. Imperfect competition: $P > MC$, output cut").scale(0.95).shift(DOWN * 2.2)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): causes 4-6 ---
        self.next_band(1)
        b1_title = Tex("Causes, continued").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        c4 = Tex(r"4. Imperfect information: wrong facts,").scale(0.95).shift(band_shift(1) + UP * 1.2)
        c4b = Tex(r"wrong quantities").scale(0.95).shift(band_shift(1) + UP * 0.5)
        c5 = Tex(r"5. Immobile factors: the dying coal town —").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        c5b = Tex(r"structural unemployment").scale(0.95).shift(band_shift(1) + DOWN * 1.1)
        c6 = Tex(r"6. Inequality: rand votes pull resources").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        c6b = Tex(r"to luxuries while unbacked needs go unmet").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(c4))
        self.play(Write(c4b))
        self.wait(2)
        self.play(Write(c5))
        self.play(Write(c5b))
        self.wait(2)
        self.play(Write(c6))
        self.play(Write(c6b))
        self.wait(2)
        eq = Tex(r"Efficiency and equity are different tests").scale(0.95).shift(band_shift(1) + DOWN * 3.4)
        self.play(Write(eq))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): negative production externality ---
        self.next_band(2)
        b2_title = Tex("The mill on the Vaal: MSC above MPC").scale(1.1).shift(band_shift(2) + UP * 2.9)
        self.play(Write(b2_title))
        self.wait(1.5)
        voc = Tex(r"Social cost $=$ private $+$ external").scale(0.9).shift(band_shift(2) + UP * 2.1 + RIGHT * 3.2)
        self.play(Write(voc))
        self.wait(2)
        o = band_shift(2) + DOWN * 2.9 + LEFT * 5.6
        y_ax = Arrow(o, o + UP * 4.7, buff=0, stroke_width=3)
        x_ax = Arrow(o, o + RIGHT * 7.2, buff=0, stroke_width=3)
        p_lab = Tex("P").scale(0.8).shift(o + UP * 4.7 + LEFT * 0.35)
        q_lab = Tex("Q").scale(0.8).shift(o + RIGHT * 7.2 + DOWN * 0.35)
        self.play(Create(y_ax), Create(x_ax), Write(p_lab), Write(q_lab))
        dd = Line(o + RIGHT * 0.5 + UP * 4.2, o + RIGHT * 5.6 + UP * 0.6, color=BLUE)
        dd_lab = Tex("D", color=BLUE).scale(0.8).shift(o + RIGHT * 5.9 + UP * 0.4)
        self.play(Create(dd), Write(dd_lab))
        mpc = Line(o + RIGHT * 0.5 + UP * 0.6, o + RIGHT * 5.6 + UP * 3.9, color=GREEN)
        mpc_lab = Tex("MPC", color=GREEN).scale(0.75).shift(o + RIGHT * 6.2 + UP * 3.9)
        self.play(Create(mpc), Write(mpc_lab))
        self.wait(1.5)
        msc = Line(o + RIGHT * 0.5 + UP * 1.4, o + RIGHT * 5.0 + UP * 4.3, color=ORANGE)
        msc_lab = Tex("MSC", color=ORANGE).scale(0.75).shift(o + RIGHT * 5.6 + UP * 4.4)
        gap = Arrow(o + RIGHT * 4.6 + UP * 3.25, o + RIGHT * 4.6 + UP * 4.05, buff=0, color=RED)
        gap_lab = Tex("external cost", color=RED).scale(0.65).shift(o + RIGHT * 6.3 + UP * 3.4)
        self.play(Create(msc), Write(msc_lab))
        self.play(Create(gap), Write(gap_lab))
        self.wait(2)
        mkt = Dot(o + RIGHT * 3.16 + UP * 2.32, color=YELLOW)
        mkt_lab = MathTex(r"Q_m").scale(0.7).shift(o + RIGHT * 3.16 + DOWN * 0.35)
        d1 = DashedLine(o + RIGHT * 3.16 + UP * 2.32, o + RIGHT * 3.16, color=GREY)
        self.play(Create(mkt), Create(d1), Write(mkt_lab))
        soc = Dot(o + RIGHT * 2.57 + UP * 2.74, color=RED)
        soc_lab = MathTex(r"Q^{*}").scale(0.7).shift(o + RIGHT * 2.45 + DOWN * 0.35)
        d2 = DashedLine(o + RIGHT * 2.57 + UP * 2.74, o + RIGHT * 2.57, color=GREY)
        self.play(Create(soc), Create(d2), Write(soc_lab))
        self.wait(2)
        over = Tex(r"$Q_m > Q^{*}$: over-produced, under-priced").scale(0.85).shift(o + RIGHT * 9.6 + UP * 2.3)
        self.play(Write(over))
        self.play(Create(SurroundingRectangle(over, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): positive consumption externality ---
        self.next_band(3)
        b3_title = Tex("Vaccination: MSB above private demand").scale(1.1).shift(band_shift(3) + UP * 2.9)
        self.play(Write(b3_title))
        self.wait(1.5)
        o3 = band_shift(3) + DOWN * 2.9 + LEFT * 5.6
        y3 = Arrow(o3, o3 + UP * 4.7, buff=0, stroke_width=3)
        x3 = Arrow(o3, o3 + RIGHT * 7.2, buff=0, stroke_width=3)
        p3 = Tex("P").scale(0.8).shift(o3 + UP * 4.7 + LEFT * 0.35)
        q3 = Tex("Q").scale(0.8).shift(o3 + RIGHT * 7.2 + DOWN * 0.35)
        self.play(Create(y3), Create(x3), Write(p3), Write(q3))
        ss = Line(o3 + RIGHT * 0.5 + UP * 0.6, o3 + RIGHT * 5.6 + UP * 3.9, color=GREEN)
        ss_lab = Tex("S", color=GREEN).scale(0.8).shift(o3 + RIGHT * 6.0 + UP * 3.9)
        self.play(Create(ss), Write(ss_lab))
        dp = Line(o3 + RIGHT * 0.5 + UP * 3.8, o3 + RIGHT * 5.0 + UP * 0.5, color=BLUE)
        dp_lab = Tex("D private", color=BLUE).scale(0.7).shift(o3 + RIGHT * 5.9 + UP * 0.4)
        self.play(Create(dp), Write(dp_lab))
        self.wait(1.5)
        msb = Line(o3 + RIGHT * 0.9 + UP * 4.3, o3 + RIGHT * 5.4 + UP * 1.0, color=ORANGE)
        msb_lab = Tex("MSB", color=ORANGE).scale(0.75).shift(o3 + RIGHT * 5.9 + UP * 1.2)
        self.play(Create(msb), Write(msb_lab))
        self.wait(2)
        m3 = Dot(o3 + RIGHT * 2.82 + UP * 2.10, color=YELLOW)
        m3_lab = MathTex(r"Q_m").scale(0.7).shift(o3 + RIGHT * 2.7 + DOWN * 0.35)
        s3 = Dot(o3 + RIGHT * 3.39 + UP * 2.47, color=RED)
        s3_lab = MathTex(r"Q^{*}").scale(0.7).shift(o3 + RIGHT * 3.5 + DOWN * 0.35)
        self.play(Create(m3), Write(m3_lab))
        self.play(Create(s3), Write(s3_lab))
        self.wait(2)
        under = Tex(r"$Q_m < Q^{*}$: under-produced").scale(0.85).shift(o3 + RIGHT * 9.6 + UP * 3.3)
        self.play(Write(under))
        self.play(Create(SurroundingRectangle(under, color=GREEN)))
        self.wait(2)
        rule = Tex(r"External costs: too much; external").scale(0.85).shift(o3 + RIGHT * 9.6 + UP * 2.2)
        rule2 = Tex(r"benefits: too little — the price lies").scale(0.85).shift(o3 + RIGHT * 9.6 + UP * 1.5)
        self.play(Write(rule))
        self.play(Write(rule2))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): consequences, taxes and subsidies ---
        self.next_band(4)
        b4_title = Tex("Consequences, and the first tools").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        k1 = Tex(r"Misallocation, degraded environment,").scale(0.95).shift(band_shift(4) + UP * 1.2)
        k2 = Tex(r"missing goods, compounded inequality").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(k1))
        self.play(Write(k2))
        self.wait(2.5)
        tx = Tex(r"TAX the external cost: carbon tax, fuel levy,").scale(0.9).shift(band_shift(4) + DOWN * 0.4)
        tx2 = Tex(r"sin taxes, sugar levy — MPC lifts onto MSC").scale(0.9).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(tx))
        self.play(Write(tx2))
        self.play(Create(SurroundingRectangle(tx2, color=GREEN)))
        self.wait(2.5)
        sb = Tex(r"SUBSIDISE the external benefit: no-fee").scale(0.9).shift(band_shift(4) + DOWN * 2.0)
        sb2 = Tex(r"schools, free clinics, housing subsidies").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(sb))
        self.play(Write(sb2))
        self.wait(3)

        # --- Band 5 (subtopic_3): provision, regulation, prices ---
        self.next_band(5)
        b5_title = Tex("The rest of the toolkit").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        pr1 = Tex(r"Direct provision: defence, streetlights, courts").scale(0.9).shift(band_shift(5) + UP * 1.2)
        pr2 = Tex(r"Regulation: emission rules, labels, zoning").scale(0.9).shift(band_shift(5) + UP * 0.4)
        self.play(Write(pr1))
        self.wait(2)
        self.play(Write(pr2))
        self.wait(2)
        pr3 = Tex(r"Max price below equilibrium $\Rightarrow$ shortages;").scale(0.9).shift(band_shift(5) + DOWN * 0.5)
        pr4 = Tex(r"min wage above $\Rightarrow$ surplus risk").scale(0.9).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(pr3))
        self.play(Write(pr4))
        self.wait(2.5)
        pr5 = Tex(r"Redistribution: progressive tax and grants").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(pr5))
        self.wait(2)
        ev = Tex(r"Imperfect tools in imperfect hands —").scale(0.9).shift(band_shift(5) + DOWN * 2.8)
        ev2 = Tex(r"each intervention needs its own case").scale(0.9).shift(band_shift(5) + DOWN * 3.4)
        self.play(Write(ev))
        self.play(Write(ev2))
        self.play(Create(SurroundingRectangle(ev2, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): CBA in five steps ---
        self.next_band(6)
        b6_title = Tex("Cost-benefit analysis: five steps").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        s1 = Tex(r"1. List ALL costs — flooded farmland too").scale(0.95).shift(band_shift(6) + UP * 1.2)
        s2 = Tex(r"2. List ALL benefits — floods prevented too").scale(0.95).shift(band_shift(6) + UP * 0.4)
        s3_ = Tex(r"3. Value the unpriced: time at the wage rate").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        s4_ = Tex(r"4. DISCOUNT future rands to the present").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        s5_ = Tex(r"5. Proceed if social benefit $>$ social cost").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.wait(2)
        self.play(Write(s3_))
        self.wait(2)
        self.play(Write(s4_))
        self.wait(2)
        self.play(Write(s5_))
        self.play(Create(SurroundingRectangle(s5_, color=GREEN)))
        self.wait(2)
        why = Tex(r"It internalises on paper what markets ignore").scale(0.9).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(why))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): the four limits ---
        self.next_band(7)
        b7_title = Tex("The four limits of CBA").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        L1 = Tex(r"1. Valuing the unpriceable is contestable").scale(0.95).shift(band_shift(7) + UP * 1.2)
        L2 = Tex(r"2. The discount rate is a moral choice —").scale(0.95).shift(band_shift(7) + UP * 0.4)
        L2b = Tex(r"a high rate silences future generations").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        L3 = Tex(r"3. Optimism bias: champions overstate").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        L4 = Tex(r"4. It sums rands without asking WHOSE").scale(0.95).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(L1))
        self.wait(2)
        self.play(Write(L2))
        self.play(Write(L2b))
        self.wait(2)
        self.play(Write(L3))
        self.wait(2)
        self.play(Write(L4))
        self.wait(2)
        hon = Tex(r"Honest: arithmetic disciplines politics;").scale(0.9).shift(band_shift(7) + DOWN * 2.7)
        hon2 = Tex(r"cynical: politics dressed in arithmetic").scale(0.9).shift(band_shift(7) + DOWN * 3.4)
        self.play(Write(hon))
        self.play(Write(hon2))
        self.play(Create(SurroundingRectangle(hon2, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the bill nobody sends ---
        self.next_band(8)
        b8_title = Tex("The bill nobody sends").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        ch1 = Tex(r"Chicken: R40 at the till — but the village").scale(0.95).shift(band_shift(8) + UP * 1.2)
        ch2 = Tex(r"pays R5 in paraffin, taxis, lost spinach").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(ch1))
        self.play(Write(ch2))
        self.wait(2.5)
        ch3 = MathTex(r"\text{True cost} = 40 + 5 = R45").scale(1.1).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(ch3))
        self.play(Create(SurroundingRectangle(ch3, color=GREEN)))
        self.wait(2.5)
        ch4 = Tex(r"Looks R5 cheap $\Rightarrow$ people buy MORE —").scale(0.95).shift(band_shift(8) + DOWN * 1.4)
        ch5 = Tex(r"over-production from a missing bill").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(ch4))
        self.play(Write(ch5))
        self.wait(2.5)
        ch6 = Tex(r"Mirror: evening classes worth more than R50,").scale(0.9).shift(band_shift(8) + DOWN * 2.9)
        ch7 = Tex(r"so too few enrol — a missing thank-you").scale(0.9).shift(band_shift(8) + DOWN * 3.5)
        self.play(Write(ch6))
        self.play(Write(ch7))
        self.wait(3)

        # --- Band 9 (subtopic_6): fixing the price ---
        self.next_band(9)
        b9_title = Tex("Fix the price until it tells the truth").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        fx1 = Tex(r"Send the bill: R5 levy per chicken —").scale(0.95).shift(band_shift(9) + UP * 1.2)
        fx2 = Tex(r"the carbon tax and tobacco excise logic").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(fx1))
        self.play(Write(fx2))
        self.wait(2.5)
        fx3 = Tex(r"Send the thank-you: classes down to R20 —").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        fx4 = Tex(r"no-fee schools, free clinics").scale(0.95).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(fx3))
        self.play(Write(fx4))
        self.wait(2.5)
        fx5 = Tex(r"No bill possible: buy it outright (streetlight);").scale(0.9).shift(band_shift(9) + DOWN * 1.9)
        fx6 = Tex(r"too grave to tax: rule it — poison has no price").scale(0.9).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(fx5))
        self.play(Write(fx6))
        self.wait(2.5)
        fx7 = Tex(r"Good policy: choose the smaller failure").scale(0.95).shift(band_shift(9) + DOWN * 3.4)
        self.play(Write(fx7))
        self.play(Create(SurroundingRectangle(fx7, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): should the dam be built? ---
        self.next_band(10)
        b10_title = Tex("Should the dam be built?").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        da1 = Tex(r"Costs: concrete, 80 households moved,").scale(0.95).shift(band_shift(10) + UP * 1.2)
        da2 = Tex(r"fields, fish, the free-working wetland").scale(0.95).shift(band_shift(10) + UP * 0.5)
        self.play(Write(da1))
        self.play(Write(da2))
        self.wait(2.5)
        da3 = Tex(r"Benefits: power, floods stopped, jobs,").scale(0.95).shift(band_shift(10) + DOWN * 0.3)
        da4 = Tex(r"cold-chain clinics — value them all").scale(0.95).shift(band_shift(10) + DOWN * 1.0)
        self.play(Write(da3))
        self.play(Write(da4))
        self.wait(2.5)
        da5 = Tex(r"Shrink future rands, then compare;").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        da6 = Tex(r"rank rivals by benefit per rand").scale(0.95).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(da5))
        self.play(Write(da6))
        self.play(Create(SurroundingRectangle(da6, color=GREEN)))
        self.wait(2.5)
        da7 = Tex(r"Ask about the losers before signing").scale(0.95).shift(band_shift(10) + DOWN * 3.4)
        self.play(Write(da7))
        self.wait(4)
