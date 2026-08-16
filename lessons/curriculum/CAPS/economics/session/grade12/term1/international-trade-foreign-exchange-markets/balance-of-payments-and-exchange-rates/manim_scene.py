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
# (Expert 1-4: bands 0-6; Simplifier 5-7: bands 7-9), scene time
# apportioned to subtopics.json (230/245/250/235/190/195/200 of 1545 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BalanceOfPaymentsAndExchangeRatesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md plays (~4-5%).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): why nations trade ---
        title = Tex("Balance of Payments and Exchange Rates").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex(r"Demand side: no country makes everything").scale(1.0).shift(UP * 1.2)
        d2 = Tex(r"Supply side: resources, skills, capital, climate").scale(0.95).shift(UP * 0.4)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.wait(2)
        ab = Tex(r"ABSOLUTE advantage: fewer resources, full stop").scale(0.95).shift(DOWN * 0.5)
        self.play(Write(ab))
        self.wait(2)
        co = Tex(r"COMPARATIVE: lowest OPPORTUNITY COST").scale(1.0).shift(DOWN * 1.4)
        self.play(Write(co))
        self.play(Create(SurroundingRectangle(co, color=GREEN)))
        self.wait(2)
        co2 = Tex(r"— holds even if one side is better at everything").scale(0.95).shift(DOWN * 2.3)
        self.play(Write(co2))
        self.wait(3)

        # --- Band 1 (subtopic_1): the two-country example ---
        self.next_band(1)
        b1_title = Tex("Same resources, two countries").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        t1 = Tex(r"SA: 100 maize OR 50 steel").scale(1.05).shift(band_shift(1) + UP * 1.2)
        t2 = Tex(r"Germany: 120 maize OR 240 steel").scale(1.05).shift(band_shift(1) + UP * 0.4)
        self.play(Write(t1))
        self.wait(2)
        self.play(Write(t2))
        self.wait(2)
        oc1 = Tex(r"1 steel costs SA 2 maize; Germany $\tfrac{1}{2}$ maize").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        oc2 = Tex(r"1 maize costs SA $\tfrac{1}{2}$ steel; Germany 2 steel").scale(0.95).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(oc1))
        self.wait(2.5)
        self.play(Write(oc2))
        self.wait(2.5)
        sp = Tex(r"SA specialises in maize, Germany in steel").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(sp))
        self.wait(2)
        gain = Tex(r"Trade 1 for 1: BOTH consume beyond their PPC").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(gain))
        self.play(Create(SurroundingRectangle(gain, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the current account ---
        self.next_band(2)
        b2_title = Tex("The balance of payments: current account").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        c1 = Tex(r"Merchandise: exports $-$ imports $=$ trade balance").scale(0.95).shift(band_shift(2) + UP * 1.2)
        self.play(Write(c1))
        self.wait(2)
        c2 = Tex(r"Services: a tourist here $=$ service EXPORT").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(c2))
        self.wait(2)
        c3 = Tex(r"Income: dividends, interest; plus transfers").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(c3))
        self.wait(2)
        c4 = Tex(r"SA typically runs a small current deficit:").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        c5 = Tex(r"imports + dividends out $>$ commodity exports").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(c4))
        self.play(Write(c5))
        self.play(Create(SurroundingRectangle(c5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): financing the deficit, IMF ---
        self.next_band(3)
        b3_title = Tex("How the deficit is paid for").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        f1 = Tex(r"Financial account: DIRECT (factories),").scale(1.0).shift(band_shift(3) + UP * 1.2)
        f2 = Tex(r"PORTFOLIO (shares, bonds — hot money),").scale(1.0).shift(band_shift(3) + UP * 0.4)
        f3 = Tex(r"OTHER (loans, deposits)").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(f1))
        self.wait(2)
        self.play(Write(f2))
        self.wait(2)
        self.play(Write(f3))
        self.wait(2)
        bal = Tex(r"Current deficit $\Rightarrow$ financial surplus").scale(1.05).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(bal))
        self.play(Create(SurroundingRectangle(bal, color=GREEN)))
        self.wait(2)
        res = Tex(r"SARB gold + forex reserves: the shock absorber").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(res))
        self.wait(2)
        imf = Tex(r"IMF: 190 members, loans WITH conditions").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(imf))
        self.wait(3)

        # --- Band 4 (subtopic_3): the forex market diagram ---
        self.next_band(4)
        b4_title = Tex("The market that prices the rand").scale(1.15).shift(band_shift(4) + UP * 2.9)
        self.play(Write(b4_title))
        self.wait(1.5)
        o = band_shift(4) + DOWN * 2.9 + LEFT * 5.4
        y_ax = Arrow(o, o + UP * 4.9, buff=0, stroke_width=3)
        x_ax = Arrow(o, o + RIGHT * 7.0, buff=0, stroke_width=3)
        y_lab = Tex(r"R per \$").scale(0.75).shift(o + UP * 4.9 + RIGHT * 0.9)
        x_lab = Tex(r"quantity of \$").scale(0.7).shift(o + RIGHT * 7.0 + DOWN * 0.35)
        self.play(Create(y_ax), Create(x_ax), Write(y_lab), Write(x_lab))
        self.wait(1.5)
        dd = Line(o + RIGHT * 0.6 + UP * 4.2, o + RIGHT * 5.4 + UP * 0.6, color=BLUE)
        dd_lab = MathTex(r"D_{\$}", color=BLUE).scale(0.85).shift(o + RIGHT * 5.9 + UP * 0.6)
        self.play(Create(dd), Write(dd_lab))
        who_d = Tex("importers, travellers,", color=BLUE).scale(0.75).shift(o + RIGHT * 8.6 + UP * 3.6)
        who_d2 = Tex("dollar debts out", color=BLUE).scale(0.75).shift(o + RIGHT * 8.6 + UP * 3.0)
        self.play(Write(who_d), Write(who_d2))
        self.wait(2)
        ss = Line(o + RIGHT * 0.6 + UP * 0.8, o + RIGHT * 5.4 + UP * 4.4, color=GREEN)
        ss_lab = MathTex(r"S_{\$}", color=GREEN).scale(0.85).shift(o + RIGHT * 5.9 + UP * 4.4)
        self.play(Create(ss), Write(ss_lab))
        who_s = Tex("exporters, tourists in,", color=GREEN).scale(0.75).shift(o + RIGHT * 8.6 + UP * 2.0)
        who_s2 = Tex("foreign investors", color=GREEN).scale(0.75).shift(o + RIGHT * 8.6 + UP * 1.4)
        self.play(Write(who_s), Write(who_s2))
        self.wait(2)
        eq = Dot(o + RIGHT * 2.87 + UP * 2.5, color=YELLOW)
        eq_lab = Tex(r"R18/\$").scale(0.8).shift(o + RIGHT * 1.9 + UP * 2.9)
        self.play(Create(eq), Write(eq_lab))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): shifts and the three systems ---
        self.next_band(5)
        b5_title = Tex("Shifts, and who sets the rate").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        s1 = Tex(r"Oil doubles: $D_{\$}$ right $\Rightarrow$ rand DEPRECIATES").scale(0.95).shift(band_shift(5) + UP * 1.2)
        s2 = Tex(r"Commodity boom: $S_{\$}$ right $\Rightarrow$ APPRECIATES").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(s1))
        self.wait(2.5)
        self.play(Write(s2))
        self.wait(2.5)
        wrong = Tex(r"Floating rand ``devalues''").scale(0.95).shift(band_shift(5) + DOWN * 0.5 + LEFT * 3.0)
        self.play(Write(wrong))
        self.play(Create(strike(wrong)))
        vocab = Tex(r"De/revaluation $=$ fixed rates only").scale(0.95).shift(band_shift(5) + DOWN * 0.5 + RIGHT * 3.2)
        self.play(Write(vocab))
        self.wait(2)
        sys1 = Tex(r"FREE-FLOATING: the market — SA's system").scale(0.95).shift(band_shift(5) + DOWN * 1.4)
        sys2 = Tex(r"MANAGED: steered inside a quiet band").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        sys3 = Tex(r"FIXED: set by decree, defended with reserves").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(sys1))
        self.wait(1.5)
        self.play(Write(sys2))
        self.wait(1.5)
        self.play(Write(sys3))
        self.wait(3)

        # --- Band 6 (subtopic_4): correcting a disequilibrium ---
        self.next_band(6)
        b6_title = Tex("Four channels of correction").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        ch1 = Tex(r"1. Exchange rate: depreciate — imported inflation").scale(0.9).shift(band_shift(6) + UP * 1.2)
        ch2 = Tex(r"2. Demand: cool spending — slower growth").scale(0.9).shift(band_shift(6) + UP * 0.4)
        ch3 = Tex(r"3. Controls: tariffs, exchange control — retaliation").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        ch4 = Tex(r"4. Borrow / reserves — conditionality and debt").scale(0.9).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(ch1))
        self.wait(2)
        self.play(Write(ch2))
        self.wait(2)
        self.play(Write(ch3))
        self.wait(2)
        self.play(Write(ch4))
        self.wait(2)
        match = Tex(r"Match the tool to the CAUSE of the gap").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(match))
        self.play(Create(SurroundingRectangle(match, color=GREEN)))
        surp = Tex(r"Surplus: run the toolkit in reverse").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(surp))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the braai exchange ---
        self.next_band(7)
        b7_title = Tex("The braai exchange").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        br1 = Tex(r"Sipho bakes; Anna farms — trade at the fence").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(br1))
        self.wait(2.5)
        br2 = Tex(r"Anna better at BOTH? Count her cost:").scale(1.0).shift(band_shift(7) + UP * 0.4)
        br3 = Tex(r"her baking hour costs 2 chickens;").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        br4 = Tex(r"Sipho's costs almost nothing").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(br2))
        self.wait(2)
        self.play(Write(br3))
        self.wait(2)
        self.play(Write(br4))
        self.wait(2.5)
        rule7 = Tex(r"Do what costs you least; trade for the rest").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(rule7))
        self.play(Create(SurroundingRectangle(rule7, color=GREEN)))
        self.wait(2)
        catch = Tex(r"The catch: Japan will not take rands").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(catch))
        self.wait(3)

        # --- Band 8 (subtopic_6): the two queues ---
        self.next_band(8)
        b8_title = Tex("The rand has a price tag too").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        q1 = Tex(r"BUY-dollar queue: fuel, phones, fees abroad").scale(0.95).shift(band_shift(8) + UP * 1.2)
        q2 = Tex(r"SELL-dollar queue: coal, wine, tourists, bonds").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(q1))
        self.wait(2.5)
        self.play(Write(q2))
        self.wait(2.5)
        q3 = Tex(r"Long buy queue $\Rightarrow$ dollar dearer: rand weakens").scale(0.9).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(q3))
        self.play(Create(SurroundingRectangle(q3, color=GREEN)))
        self.wait(2.5)
        h1 = Tex(r"Oil spike: weakens. Bond inflows: firms.").scale(0.95).shift(band_shift(8) + DOWN * 1.4)
        h2 = Tex(r"Load-shedding scares investors: weakens.").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(h1))
        self.wait(2.5)
        self.play(Write(h2))
        self.wait(2)
        fl = Tex(r"Floating is bumpy but honest; fixed snaps").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(fl))
        self.wait(3)

        # --- Band 9 (subtopic_7): the family notebook ---
        self.next_band(9)
        b9_title = Tex("The family that outspends its earnings").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        n1 = Tex(r"Earn/spend notebook $=$ current account").scale(1.0).shift(band_shift(9) + UP * 1.2)
        n2 = Tex(r"Covering the gap $=$ financial account").scale(1.0).shift(band_shift(9) + UP * 0.4)
        n3 = Tex(r"Tin on the shelf $=$ reserves").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(n1))
        self.wait(2.5)
        self.play(Write(n2))
        self.wait(2.5)
        self.play(Write(n3))
        self.wait(2.5)
        n4 = Tex(r"The uncle with conditions $=$ the IMF").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(n4))
        self.play(Create(SurroundingRectangle(n4, color=GREEN)))
        self.wait(2.5)
        n5 = Tex(r"Four cures: get cheaper, spend less,").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        n6 = Tex(r"block spending, borrow — match cure to disease").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(n5))
        self.play(Write(n6))
        self.wait(4)
