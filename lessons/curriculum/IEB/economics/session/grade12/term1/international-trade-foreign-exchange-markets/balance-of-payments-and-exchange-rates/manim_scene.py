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
        title = Tex("Balance of Payments and Exchange Rates").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex(r"Demand side: no country makes everything").scale(1.0).shift(UP * 1.2)
        d2 = Tex(r"Supply side: resources, skills, capital,").scale(1.0).shift(UP * 0.4)
        d3 = Tex(r"technology and climate differ").scale(1.0).shift(DOWN * 0.3)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.play(Write(d3))
        self.wait(2)
        sp = Tex(r"Specialise where endowments favour;").scale(1.0).shift(DOWN * 1.3)
        sp2 = Tex(r"trade for the rest — both consume more").scale(1.0).shift(DOWN * 2.0)
        self.play(Write(sp))
        self.play(Write(sp2))
        self.play(Create(SurroundingRectangle(sp2, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the two-country example ---
        self.next_band(1)
        b1_title = Tex("Citrus against electronics").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        t1 = Tex(r"SA: 80 citrus OR 20 electronics").scale(1.0).shift(band_shift(1) + UP * 1.2)
        t2 = Tex(r"Korea: 100 citrus OR 200 electronics").scale(1.0).shift(band_shift(1) + UP * 0.5)
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(2)
        t3 = Tex(r"Korea absolutely better at BOTH").scale(1.0).shift(band_shift(1) + DOWN * 0.3)
        self.play(Write(t3))
        self.wait(2)
        oc1 = Tex(r"1 electronics costs SA 4 citrus; Korea $\tfrac{1}{2}$").scale(0.95).shift(band_shift(1) + DOWN * 1.1)
        oc2 = Tex(r"1 citrus costs Korea 2 electronics; SA $\tfrac{1}{4}$").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(oc1))
        self.wait(2)
        self.play(Write(oc2))
        self.wait(2)
        res = Tex(r"Least sacrifice: SA citrus, Korea electronics").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(res))
        self.play(Create(SurroundingRectangle(res, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the current account ---
        self.next_band(2)
        b2_title = Tex("The current account: trade and income NOW").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        c1 = Tex(r"Merchandise: minerals, vehicles, fruit out;").scale(0.95).shift(band_shift(2) + UP * 1.2)
        c2 = Tex(r"oil, machinery, electronics in — TRADE BALANCE").scale(0.9).shift(band_shift(2) + UP * 0.5)
        self.play(Write(c1))
        self.play(Write(c2))
        self.wait(2)
        c3 = Tex(r"Services: freight, tourism —").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        c4 = Tex(r"a visitor's spending is a service EXPORT").scale(0.95).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(c3))
        self.play(Write(c4))
        self.wait(2)
        c5 = Tex(r"Income: dividends, interest; plus transfers").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(c5))
        self.wait(2)
        c6 = Tex(r"SA usually runs a modest current deficit").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(c6))
        self.play(Create(SurroundingRectangle(c6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): financing the deficit, IMF ---
        self.next_band(3)
        b3_title = Tex("Financing the gap").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        f1 = Tex(r"Financial account: DIRECT (factories),").scale(0.95).shift(band_shift(3) + UP * 1.2)
        f2 = Tex(r"PORTFOLIO (shares, bonds — hot money),").scale(0.95).shift(band_shift(3) + UP * 0.5)
        f3 = Tex(r"OTHER (loans and deposits)").scale(0.95).shift(band_shift(3) + DOWN * 0.2)
        self.play(Write(f1))
        self.wait(2)
        self.play(Write(f2))
        self.wait(2)
        self.play(Write(f3))
        self.wait(2)
        f4 = Tex(r"Current deficit $\Rightarrow$ financial surplus").scale(1.0).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(f4))
        self.play(Create(SurroundingRectangle(f4, color=GREEN)))
        self.wait(2)
        f5 = Tex(r"Reserves: the shock absorber that balances all").scale(0.9).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(f5))
        self.wait(2)
        f6 = Tex(r"IMF: 190 members, loans WITH conditions").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(f6))
        self.wait(3)

        # --- Band 4 (subtopic_3): the forex market diagram ---
        self.next_band(4)
        b4_title = Tex("The market that prices the rand").scale(1.15).shift(band_shift(4) + UP * 2.9)
        self.play(Write(b4_title))
        self.wait(1.5)
        o = band_shift(4) + DOWN * 2.9 + LEFT * 5.4
        y_ax = Arrow(o, o + UP * 4.8, buff=0, stroke_width=3)
        x_ax = Arrow(o, o + RIGHT * 10.4, buff=0, stroke_width=3)
        y_lab = Tex("R per \\$").scale(0.75).shift(o + UP * 4.8 + RIGHT * 1.0)
        x_lab = Tex("quantity of dollars").scale(0.7).shift(o + RIGHT * 9.8 + DOWN * 0.35)
        self.play(Create(y_ax), Create(x_ax))
        self.play(Write(y_lab), Write(x_lab))
        self.wait(1.5)
        dd = Line(o + RIGHT * 0.8 + UP * 4.2, o + RIGHT * 8.6 + UP * 0.6, color=BLUE)
        dd_lab = Tex("D: importers, travellers,", color=BLUE).scale(0.7).shift(o + RIGHT * 8.6 + UP * 1.6)
        dd_lab2 = Tex("dollar debtors", color=BLUE).scale(0.7).shift(o + RIGHT * 8.6 + UP * 1.1)
        self.play(Create(dd), Write(dd_lab), Write(dd_lab2))
        self.wait(2)
        ss = Line(o + RIGHT * 0.8 + UP * 0.6, o + RIGHT * 8.6 + UP * 4.2, color=GREEN)
        ss_lab = Tex("S: exporters, tourists,", color=GREEN).scale(0.7).shift(o + RIGHT * 8.6 + UP * 3.6)
        ss_lab2 = Tex("investors coming in", color=GREEN).scale(0.7).shift(o + RIGHT * 8.6 + UP * 3.1)
        self.play(Create(ss), Write(ss_lab), Write(ss_lab2))
        self.wait(2)
        eq = Dot(o + RIGHT * 4.7 + UP * 2.4, color=YELLOW)
        eq_lab = Tex("today's rate, say R19/\\$").scale(0.75).shift(o + RIGHT * 4.7 + UP * 3.1)
        self.play(Create(eq), Write(eq_lab))
        self.play(Create(SurroundingRectangle(eq_lab, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): shifts and the three systems ---
        self.next_band(5)
        b5_title = Tex("Shifts, and who sets the price").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        s1 = Tex(r"Wheat imports up: D right — rand DEPRECIATES").scale(0.9).shift(band_shift(5) + UP * 1.2)
        s2 = Tex(r"Citrus boom or bond inflows: S right —").scale(0.9).shift(band_shift(5) + UP * 0.5)
        s3 = Tex(r"rand APPRECIATES").scale(0.95).shift(band_shift(5) + DOWN * 0.2)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.play(Write(s3))
        self.wait(2)
        wr = Tex(r"Floating market moves $=$ devaluation").scale(0.9).shift(band_shift(5) + DOWN * 1.1 + LEFT * 2.4)
        self.play(Write(wr))
        self.play(Create(strike(wr)))
        rt = Tex(r"De/revaluation: fixed-rate resets only").scale(0.9).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(rt))
        self.wait(2)
        sys = Tex(r"Free float (SA), managed float, fixed peg").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(sys))
        self.play(Create(SurroundingRectangle(sys, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): correcting a disequilibrium ---
        self.next_band(6)
        b6_title = Tex("Four channels of correction").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        ch1 = Tex(r"1. Exchange rate slides — cost: imported inflation").scale(0.9).shift(band_shift(6) + UP * 1.2)
        ch2 = Tex(r"2. Demand restraint — cost: growth and jobs").scale(0.9).shift(band_shift(6) + UP * 0.4)
        ch3 = Tex(r"3. Direct controls — cost: retaliation, evasion").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        ch4 = Tex(r"4. Borrow and reserves — cost: debt, conditions").scale(0.9).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(ch1))
        self.wait(2)
        self.play(Write(ch2))
        self.wait(2)
        self.play(Write(ch3))
        self.wait(2)
        self.play(Write(ch4))
        self.wait(2)
        sur = Tex(r"Surplus: run the toolkit in reverse").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(sur))
        self.wait(1.5)
        match = Tex(r"Match the tool to the CAUSE").scale(1.0).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(match))
        self.play(Create(SurroundingRectangle(match, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the braai exchange ---
        self.next_band(7)
        b7_title = Tex("The braai exchange").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        g1 = Tex(r"Karabo grows; Elsa bakes; both eat better").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(g1))
        self.wait(2.5)
        g2 = Tex(r"Even if Elsa is better at BOTH:").scale(0.95).shift(band_shift(7) + UP * 0.4)
        g3 = Tex(r"her garden hour costs 2 loaves;").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        g4 = Tex(r"Karabo's costs almost nothing").scale(0.95).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(g2))
        self.wait(2)
        self.play(Write(g3))
        self.play(Write(g4))
        self.wait(2.5)
        g5 = Tex(r"Do what costs YOU least; trade for the rest").scale(0.95).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(g5))
        self.play(Create(SurroundingRectangle(g5, color=GREEN)))
        self.wait(2)
        g6 = Tex(r"Snag at the gate: whose money settles the deal?").scale(0.9).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(g6))
        self.wait(3)

        # --- Band 8 (subtopic_6): the two queues ---
        self.next_band(8)
        b8_title = Tex("Two queues price the rand").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        q1 = Tex(r"BUY dollars: fuel importer, phone chain,").scale(0.95).shift(band_shift(8) + UP * 1.2)
        q2 = Tex(r"foreign fees, funds going abroad").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(q1))
        self.play(Write(q2))
        self.wait(2.5)
        q3 = Tex(r"SELL dollars: coal and citrus exporters,").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        q4 = Tex(r"arriving tourists, bond buyers").scale(0.95).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(q3))
        self.play(Write(q4))
        self.wait(2.5)
        q5 = Tex(r"Long buy queue: rand weakens; reversed: firms").scale(0.9).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(q5))
        self.play(Create(SurroundingRectangle(q5, color=GREEN)))
        self.wait(2)
        q6 = Tex(r"Drought, downgrade, harvest, rate rise — all queues").scale(0.85).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(q6))
        self.wait(3)

        # --- Band 9 (subtopic_7): the family exercise book ---
        self.next_band(9)
        b9_title = Tex("The family that outspends its earnings").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        n1 = Tex(r"Exercise book $=$ current account").scale(0.95).shift(band_shift(9) + UP * 1.2)
        n2 = Tex(r"Covering page $=$ financial account").scale(0.95).shift(band_shift(9) + UP * 0.4)
        n3 = Tex(r"Envelope behind the cupboard $=$ reserves").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(n1))
        self.wait(2)
        self.play(Write(n2))
        self.wait(2)
        self.play(Write(n3))
        self.wait(2)
        n4 = Tex(r"The relative with conditions $=$ the IMF").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(n4))
        self.wait(2)
        n5 = Tex(r"Cures: cheaper prices, tighter belt,").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        n6 = Tex(r"blocked spending, borrowed time").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(n5))
        self.play(Write(n6))
        self.play(Create(SurroundingRectangle(n6, color=GREEN)))
        self.wait(4)
