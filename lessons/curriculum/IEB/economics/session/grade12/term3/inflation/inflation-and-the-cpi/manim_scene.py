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

# Band-layout whiteboard scene for the inflation-and-the-CPI session duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 225/245/235/255/190/185/195 of 1530 s — bands
# 0-1 / 2-4 / 5 / 6-7 / 8 / 9 / 10 apportioned to match.
# AS-AD sketches hand-built from Arrow/Line/Tex primitives only.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def axes(origin, w, h, xlab, ylab):
    xa = Arrow(origin, origin + RIGHT * w, buff=0, stroke_width=3)
    ya = Arrow(origin, origin + UP * h, buff=0, stroke_width=3)
    xl = Tex(xlab).scale(0.9).next_to(origin + RIGHT * w, DOWN, buff=0.2)
    yl = Tex(ylab).scale(0.9).next_to(origin + UP * h, LEFT, buff=0.2)
    return VGroup(xa, ya, xl, yl)


def chain(origin, pts, color=WHITE, sw=5):
    g = VGroup()
    for a, b in zip(pts[:-1], pts[1:]):
        g.add(Line(origin + RIGHT * a[0] + UP * a[1],
                   origin + RIGHT * b[0] + UP * b[1],
                   color=color, stroke_width=sw))
    return g


class InflationAndTheCPISession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the definition's three tests ---
        title = Tex("Inflation and the CPI").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Inflation: a SUSTAINED, significant rise in").scale(1.1).shift(UP * 1.4)
        d2 = Tex("the GENERAL price level OVER TIME").scale(1.1).shift(UP * 0.6)
        self.play(Write(d1))
        self.play(Write(d2))
        self.play(Create(SurroundingRectangle(VGroup(d1, d2), color=GREEN)))
        self.wait(2.5)
        d3 = Tex("Sustained: one fuel-levy jump is not inflation").scale(1.0).shift(DOWN * 0.5)
        d4 = Tex("General: dearer shoes alone is relative, not inflation").scale(0.92).shift(DOWN * 1.3)
        self.play(Write(d3))
        self.wait(2)
        self.play(Write(d4))
        self.wait(2)
        d5 = Tex("Deflation: general level falls; disinflation:").scale(1.0).shift(DOWN * 2.2)
        d6 = Tex("still rising, just slower (8\\% $\\rightarrow$ 5\\%)").scale(1.0).shift(DOWN * 2.9)
        self.play(Write(d5))
        self.play(Write(d6))
        self.wait(3)

        # --- Band 1 (subtopic_1): building the basket ---
        self.next_band(1)
        b1_title = Tex("Stats SA assembles the CPI in four stages").scale(1.1).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("1. Survey households $\\rightarrow$ the BASKET").scale(1.0).shift(band_shift(1) + UP * 1.5)
        b1_l2 = Tex("2. WEIGHT each item: housing $\\sim\\tfrac{1}{4}$,").scale(1.0).shift(band_shift(1) + UP * 0.7)
        b1_l3 = Tex("food under $\\tfrac{1}{5}$, transport $\\sim\\tfrac{1}{7}$").scale(1.0).shift(band_shift(1))
        b1_l4 = Tex("3. Record tens of thousands of prices monthly").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l5 = Tex("4. Weighted average $\\rightarrow$ index, base year $=$ 100").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4, b1_l5):
            self.play(Write(m))
            self.wait(1.8)
        b1_l6 = Tex("Headline CPI: all items. Core: strips food, fuel,").scale(0.95).shift(band_shift(1) + DOWN * 2.5)
        b1_l7 = Tex("energy. PPI: factory gate — tomorrow's CPI early").scale(0.95).shift(band_shift(1) + DOWN * 3.2)
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.wait(3)

        # --- Band 2 (subtopic_2): constructing the index ---
        self.next_band(2)
        b2_title = Tex("Calculation 1: building the index").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Base year: basket costs R5 000, index $=$ 100").scale(1.05).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("Three years later: same basket costs R5 400").scale(1.05).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\text{Index} = \frac{5\,400}{5\,000} \times 100 = 108{,}0").scale(1.15).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Not a price, not a percentage — a ratio:").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        b2_l5 = Tex("what cost R100 in the base year costs R108 now").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the inflation rate and the traps ---
        self.next_band(3)
        b3_title = Tex("Calculation 2: the inflation rate").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Rate} = \frac{\text{new} - \text{old}}{\text{old}} \times 100").scale(1.1).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"\frac{114{,}5 - 108{,}0}{108{,}0} \times 100 = 6{,}02\%").scale(1.1).shift(band_shift(3) + UP * 0.1)
        b3_l3 = MathTex(r"\approx 6{,}0\%").scale(1.15).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex("Trap: 6,5 index points is NOT 6,5 percent").scale(1.05).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.play(Create(strike(b3_l4)))
        self.wait(2)
        b3_l5 = Tex("Divide by the OLD index, never the new").scale(1.05).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_2): weighted basket, reverse, real values ---
        self.next_band(4)
        b4_title = Tex("Weights, reverse gear, and real values").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Food 40\\% rose 12\\%; transport 35\\% rose 4\\%;").scale(1.0).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("education 25\\% rose 8\\%").scale(1.0).shift(band_shift(4) + UP * 0.7)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"0{,}4(12) + 0{,}35(4) + 0{,}25(8) = 8{,}2\%").scale(1.1).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = MathTex(r"\text{Reverse: } 105{,}0 \times 1{,}08 = 113{,}4").scale(1.05).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex("Salary $+5\\%$ under $7\\%$ inflation:").scale(1.05).shift(band_shift(4) + DOWN * 2.3)
        b4_l6 = MathTex(r"\text{real change} \approx 5\% - 7\% = -2\%").scale(1.05).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): demand-pull vs cost-push ---
        self.next_band(5)
        b5_title = Tex("Two kinds, two curve stories").scale(1.15).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_title))
        self.wait(1.5)
        o1 = band_shift(5) + LEFT * 5.6 + DOWN * 2.4
        ax1 = axes(o1, 4.4, 3.6, "Q", "P")
        lab1 = Tex("Demand-pull").scale(0.95).shift(band_shift(5) + LEFT * 3.4 + UP * 1.7)
        self.play(Create(ax1), Write(lab1))
        as1 = chain(o1, [(0.5, 0.7), (2.1, 1.8), (3.7, 2.9)], color=YELLOW)
        as1_lab = Tex("AS").scale(0.85).next_to(o1 + RIGHT * 3.7 + UP * 2.9, RIGHT, buff=0.1)
        ad1 = chain(o1, [(0.5, 2.9), (2.1, 1.8), (3.7, 0.7)], color=BLUE)
        ad1_lab = Tex("AD$_1$").scale(0.85).next_to(o1 + RIGHT * 3.7 + UP * 0.7, RIGHT, buff=0.1)
        self.play(Create(as1), Write(as1_lab))
        self.play(Create(ad1), Write(ad1_lab))
        self.wait(1.5)
        ad2 = chain(o1, [(1.3, 3.4), (2.9, 2.3), (4.3, 1.4)], color=BLUE)
        ad2_lab = Tex("AD$_2$").scale(0.85).next_to(o1 + RIGHT * 4.3 + UP * 1.4, RIGHT, buff=0.1)
        sh1 = Arrow(o1 + RIGHT * 1.6 + UP * 2.6, o1 + RIGHT * 2.5 + UP * 2.9, buff=0, stroke_width=4, color=GREEN)
        self.play(Create(ad2), Write(ad2_lab), Create(sh1))
        p_up1 = Tex("P up, Q up").scale(0.9).shift(band_shift(5) + LEFT * 3.4 + DOWN * 3.0)
        self.play(Write(p_up1))
        self.wait(2)
        o2 = band_shift(5) + RIGHT * 1.0 + DOWN * 2.4
        ax2 = axes(o2, 4.4, 3.6, "Q", "P")
        lab2 = Tex("Cost-push").scale(0.95).shift(band_shift(5) + RIGHT * 3.2 + UP * 1.7)
        self.play(Create(ax2), Write(lab2))
        as2 = chain(o2, [(0.5, 0.7), (2.1, 1.8), (3.7, 2.9)], color=YELLOW)
        as2_lab = Tex("AS$_1$").scale(0.85).next_to(o2 + RIGHT * 3.7 + UP * 2.9, RIGHT, buff=0.1)
        ad3 = chain(o2, [(0.5, 2.9), (2.1, 1.8), (3.7, 0.7)], color=BLUE)
        self.play(Create(as2), Write(as2_lab))
        self.play(Create(ad3))
        self.wait(1.5)
        as3 = chain(o2, [(0.2, 1.4), (1.6, 2.5), (2.9, 3.5)], color=YELLOW)
        as3_lab = Tex("AS$_2$").scale(0.85).next_to(o2 + RIGHT * 2.9 + UP * 3.5, RIGHT, buff=0.1)
        sh2 = Arrow(o2 + RIGHT * 2.9 + UP * 2.2, o2 + RIGHT * 2.1 + UP * 2.6, buff=0, stroke_width=4, color=RED)
        self.play(Create(as3), Write(as3_lab), Create(sh2))
        p_up2 = Tex("P up, Q DOWN: stagflation").scale(0.9).shift(band_shift(5) + RIGHT * 3.2 + DOWN * 3.0)
        self.play(Write(p_up2))
        self.play(Create(SurroundingRectangle(p_up2, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the redistribution ---
        self.next_band(6)
        b6_title = Tex("Consequences: wealth moved without permission").scale(1.05).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Creditors lose to debtors: loans repaid").scale(1.0).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("in rands that buy less").scale(1.0).shift(band_shift(6) + UP * 0.7)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Fixed incomes stretch thinner; savers lose when").scale(0.97).shift(band_shift(6) + DOWN * 0.1)
        b6_l4 = MathTex(r"\text{real rate} = \text{nominal} - \text{inflation} < 0").scale(1.05).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Uncertainty delays investment; exports lose").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        b6_l6 = Tex("their edge; bracket creep — an unvoted tax;").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        b6_l7 = Tex("expectations of 7\\% write contracts at 7\\%").scale(1.0).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.wait(3)

        # --- Band 7 (subtopic_4): the fight — targeting and its limits ---
        self.next_band(7)
        b7_title = Tex("The fight: inflation targeting since 2000").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("SARB must hold CPI inflation inside 3–6\\%").scale(1.05).shift(band_shift(7) + UP * 1.4)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(2.5)
        b7_l2 = Tex("Instrument: the repo rate — lift it, prime").scale(1.0).shift(band_shift(7) + UP * 0.4)
        b7_l3 = Tex("follows, borrowing slows, demand cools").scale(1.0).shift(band_shift(7) + DOWN * 0.3)
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("Limit: the repo works on DEMAND — it cannot").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        b7_l5 = Tex("lower a tariff, a fuel shock or a drought").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(2.5)
        b7_l6 = Tex("Wage and price controls tend to fail:").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l6))
        self.play(Create(strike(b7_l6)))
        b7_l7 = Tex("shortages and black markets grow under the freeze").scale(0.95).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l7))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the trolley that tells the truth ---
        self.next_band(8)
        b8_title = Tex("The trolley that tells the truth").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("One trolley for the whole country: maize meal,").scale(1.0).shift(band_shift(8) + UP * 1.5)
        b8_l2 = Tex("taxi fare, data, rent, a burial-society premium").scale(1.0).shift(band_shift(8) + UP * 0.8)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{R}5\,000 \to 100; \quad \frac{5\,400}{5\,000} \times 100 = 108").scale(0.97).shift(band_shift(8) + DOWN * 0.2)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = MathTex(r"108 \to 114{,}5: \;\; \frac{6{,}5}{108} \times 100 \approx 6\%").scale(1.05).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2.5)
        b8_l5 = Tex("One trolley, priced twice, compared —").scale(1.0).shift(band_shift(8) + DOWN * 2.3)
        b8_l6 = Tex("and no real family's trolley is the average one").scale(1.0).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): two fires, two hoses ---
        self.next_band(9)
        b9_title = Tex("Two fires, two hoses").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Fire 1 — at the till: money flowing, shelves").scale(1.0).shift(band_shift(9) + UP * 1.5)
        b9_l2 = Tex("emptying — DEMAND-PULL (spot the busy shop)").scale(1.0).shift(band_shift(9) + UP * 0.8)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Fire 2 — at the loading bay: weak rand, diesel,").scale(1.0).shift(band_shift(9))
        b9_l4 = Tex("tariffs, drought — COST-PUSH (quiet shop)").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("The repo hose reaches only the FIRST fire:").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        b9_l6 = Tex("diesel stays dear when bond repayments rise").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(2)
        b9_l7 = Tex("Repo fights demand-pull well, cost-push badly").scale(1.0).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9_l7))
        self.play(Create(SurroundingRectangle(b9_l7, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): winners and losers ---
        self.next_band(10)
        b10_title = Tex("Who wins and who loses when prices run").scale(1.15).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Losers: the pensioner's fixed envelope, the saver").scale(1.0).shift(band_shift(10) + UP * 1.7)
        b10_l2 = Tex("at 5\\% under 7\\% inflation (real return $-2\\%$),").scale(1.0).shift(band_shift(10) + UP * 1.0)
        b10_l3 = Tex("the worker with no union, the bracket-creep payer").scale(0.97).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(3)
        b10_l4 = Tex("Winners: borrowers repay in lighter rands —").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        b10_l5 = Tex("including government; holders of property and shares").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex("The 3–6\\% band: not zero, and never Zimbabwe").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        b10_l7 = Tex("2008 — low and steady, so families can plan").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.play(Create(SurroundingRectangle(b10_l7, color=GREEN)))
        self.wait(4)
