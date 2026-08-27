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

# Band-layout whiteboard scene for the macro revision-essentials duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 250/240/240/250/195/195/190 of 1560 s — bands
# 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10 apportioned to match.
# Circular-flow, Laffer and forex sketches hand-built from
# Arrow/Line/Dot/Rectangle/Tex primitives only.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def axes(origin, w, h, xlab, ylab):
    xa = Arrow(origin, origin + RIGHT * w, buff=0, stroke_width=3)
    ya = Arrow(origin, origin + UP * h, buff=0, stroke_width=3)
    xl = Tex(xlab).scale(0.9).next_to(origin + RIGHT * w, DOWN, buff=0.2)
    yl = Tex(ylab).scale(0.9).next_to(origin + UP * h, RIGHT, buff=0.15)
    return VGroup(xa, ya, xl, yl)


def chain(origin, pts, color=WHITE, sw=5):
    g = VGroup()
    for a, b in zip(pts[:-1], pts[1:]):
        g.add(Line(origin + RIGHT * a[0] + UP * a[1],
                   origin + RIGHT * b[0] + UP * b[1],
                   color=color, stroke_width=sw))
    return g


class MacroEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # --- Band 0 (subtopic_1): the circular flow ---
        title = Tex("Macro Essentials — one sweep").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        hh = Rectangle(width=3.0, height=1.1).shift(LEFT * 4.2 + UP * 0.6)
        hh_t = Tex("Households").scale(0.85).move_to(hh)
        bb = Rectangle(width=3.0, height=1.1).shift(RIGHT * 4.2 + UP * 0.6)
        bb_t = Tex("Businesses").scale(0.85).move_to(bb)
        st = Rectangle(width=2.6, height=1.0).shift(UP * 2.4)
        st_t = Tex("State").scale(0.85).move_to(st)
        ff = Rectangle(width=3.2, height=1.0).shift(DOWN * 2.0)
        ff_t = Tex("Foreign sector").scale(0.8).move_to(ff)
        self.play(Create(hh), Write(hh_t), Create(bb), Write(bb_t))
        self.play(Create(st), Write(st_t), Create(ff), Write(ff_t))
        self.wait(1.5)
        a1 = Arrow(LEFT * 2.6 + UP * 0.9, RIGHT * 2.6 + UP * 0.9, buff=0, color=YELLOW, stroke_width=4)
        a1_t = Tex("labour $\\rightarrow$ wages").scale(0.75).next_to(a1, UP, buff=0.1)
        a2 = Arrow(RIGHT * 2.6 + UP * 0.2, LEFT * 2.6 + UP * 0.2, buff=0, color=GREEN, stroke_width=4)
        a2_t = Tex("goods $\\leftarrow$ spending").scale(0.75).next_to(a2, DOWN, buff=0.1)
        self.play(Create(a1), Write(a1_t))
        self.play(Create(a2), Write(a2_t))
        self.wait(2)
        eq1 = Tex("Leakages: S $+$ T $+$ M").scale(0.95).shift(DOWN * 3.0 + LEFT * 3.2)
        eq2 = Tex("Injections: I $+$ G $+$ X").scale(0.95).shift(DOWN * 3.0 + RIGHT * 3.2)
        self.play(Write(eq1), Write(eq2))
        self.wait(3)

        # --- Band 1 (subtopic_1): multiplier and cycles ---
        self.next_band(1)
        b1_title = Tex("The multiplier, then the cycle").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_f1 = MathTex(r"\text{Multiplier} = \frac{1}{1 - mpc} = \frac{1}{0{,}25} = 4").scale(1.05).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_f1))
        self.play(Create(SurroundingRectangle(b1_f1, color=GREEN)))
        self.wait(2.5)
        b1_l1 = Tex("R5 billion invested $\\Rightarrow$ R20 billion of income").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Cycle: recovery, prosperity, recession,").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        b1_l3 = Tex("depression — around a rising trend").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Monetarists: EXOGENOUS shocks, markets heal").scale(0.95).shift(band_shift(1) + DOWN * 2.3)
        b1_l5 = Tex("Keynesians: ENDOGENOUS moods, state must act").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): objectives and the budget ---
        self.next_band(2)
        b2_title = Tex("The public sector and the budget").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Five objectives: growth, jobs, stable prices,").scale(1.0).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("external balance, equity").scale(1.0).shift(band_shift(2) + UP * 0.7)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("Revenue: personal income tax, VAT, company tax").scale(0.95).shift(band_shift(2) + DOWN * 0.2)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("Three-year plan $=$ the rolling framework;").scale(0.95).shift(band_shift(2) + DOWN * 1.1)
        b2_l5 = Tex("October statement $=$ the mid-year update").scale(0.95).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(2)
        b2_l6 = Tex("Debt watched as a share of GDP").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the Laffer curve ---
        self.next_band(3)
        b3_title = Tex("The Laffer curve, told in words").scale(1.15).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        o = band_shift(3) + LEFT * 5.4 + DOWN * 2.2
        ax = axes(o, 9.6, 4.2, "tax rate", "revenue")
        self.play(Create(ax))
        laffer = chain(o, [(0.4, 0.2), (2.4, 2.4), (4.6, 3.6), (6.8, 2.6), (9.0, 0.3)],
                       color=YELLOW)
        self.play(Create(laffer), run_time=2)
        opt = DashedLine(o + RIGHT * 4.6, o + RIGHT * 4.6 + UP * 3.6, stroke_width=3)
        opt_lab = Tex("optimal rate").scale(0.85).next_to(o + RIGHT * 4.6, DOWN, buff=0.15)
        self.play(Create(opt), Write(opt_lab))
        self.wait(2)
        b3_l1 = Tex("Zero at 0\\% and at 100\\% — beyond the peak,").scale(0.95).shift(band_shift(3) + RIGHT * 2.6 + UP * 1.6)
        b3_l2 = Tex("CUTTING the rate raises MORE revenue").scale(0.95).shift(band_shift(3) + RIGHT * 2.6 + UP * 0.9)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Public failure: bureaucracy, interference,").scale(0.9).shift(band_shift(3) + DOWN * 3.1 + LEFT * 2.4)
        b3_l4 = Tex("special interests").scale(0.9).shift(band_shift(3) + DOWN * 3.1 + RIGHT * 3.6)
        self.play(Write(b3_l3), Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): the rand's market ---
        self.next_band(4)
        b4_title = Tex("The market for foreign currency").scale(1.15).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        o2 = band_shift(4) + LEFT * 5.4 + DOWN * 2.4
        ax2 = axes(o2, 9.6, 4.4, "quantity of foreign currency", "rand price")
        self.play(Create(ax2))
        dd = Line(o2 + RIGHT * 0.8 + UP * 4.0, o2 + RIGHT * 8.6 + UP * 0.6, color=BLUE, stroke_width=4)
        dd_lab = Tex("D: importers, travellers out").scale(0.8).next_to(o2 + RIGHT * 8.6 + UP * 0.6, RIGHT, buff=0.15)
        ss = Line(o2 + RIGHT * 0.8 + UP * 0.6, o2 + RIGHT * 8.6 + UP * 4.0, color=YELLOW, stroke_width=4)
        ss_lab = Tex("S: exporters, tourists in").scale(0.8).next_to(o2 + RIGHT * 8.6 + UP * 4.0, RIGHT, buff=0.15)
        self.play(Create(dd), Write(dd_lab))
        self.play(Create(ss), Write(ss_lab))
        self.wait(1.5)
        eq_dot = Dot(o2 + RIGHT * 4.7 + UP * 2.3, color=RED)
        eq_lab = Tex("rate set here").scale(0.85).next_to(o2 + RIGHT * 4.7 + UP * 2.3, UP, buff=0.15)
        self.play(Create(eq_dot), Write(eq_lab))
        self.wait(2)
        b4_l1 = Tex("More imports $\\Rightarrow$ D right $\\Rightarrow$ rand DEPRECIATES").scale(0.9).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l1))
        self.wait(3)

        # --- Band 5 (subtopic_3): the accounts and terms of trade ---
        self.next_band(5)
        b5_title = Tex("Three accounts, and the terms of trade").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Current: goods, services, income flows").scale(1.0).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("Capital transfer: small, quiet gifts").scale(1.0).shift(band_shift(5) + UP * 0.7)
        b5_l3 = Tex("Financial: direct, portfolio, reserves").scale(1.0).shift(band_shift(5))
        for m in (b5_l1, b5_l2, b5_l3):
            self.play(Write(m))
            self.wait(1.8)
        b5_l4 = Tex("Retailer bought $\\rightarrow$ direct; shares $\\rightarrow$ portfolio").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_f1 = MathTex(r"\text{Terms of trade} = \frac{\text{export price index}}{\text{import price index}} \times 100").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_f1))
        self.play(Create(SurroundingRectangle(b5_f1, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex("Rising ratio: each export ton buys more imports").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): trade policy and growth ---
        self.next_band(6)
        b6_title = Tex("Trade policy, growth and development").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Export promotion: incentives outward —").scale(0.95).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("risk: firms that never stand alone").scale(0.95).shift(band_shift(6) + UP * 0.7)
        b6_l3 = Tex("Import substitution: tariffs shelter home —").scale(0.95).shift(band_shift(6))
        b6_l4 = Tex("risk: expensive, slow producers").scale(0.95).shift(band_shift(6) + DOWN * 0.7)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(1.6)
        b6_l5 = Tex("GROWTH: real GDP rises").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        b6_l6 = Tex("DEVELOPMENT: lives widen — standards, choices").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): plans and indicators ---
        self.next_band(7)
        b7_title = Tex("The plans in order, and the indicators").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Rebuild $\\rightarrow$ stabilise $\\rightarrow$ unblock $\\rightarrow$").scale(1.0).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("employ $\\rightarrow$ plan long, to 2030").scale(1.0).shift(band_shift(7) + UP * 0.7)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Zones and corridors: industry moved to people").scale(0.95).shift(band_shift(7) + DOWN * 0.2)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Economic indicators: prices, jobs, rates, money").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        b7_l5 = Tex("Social indicators: life expectancy, water,").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        b7_l6 = Tex("schooling, housing").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        for m in (b7_l4, b7_l5, b7_l6):
            self.play(Write(m))
            self.wait(1.6)
        b7_l7 = Tex("Sort them fast — the split is a standing question").scale(0.95).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_l7))
        self.play(Create(SurroundingRectangle(b7_l7, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_5): the taxi route ---
        self.next_band(8)
        b8_title = Tex("The economy as one big taxi route").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        c = Circle(radius=1.7, color=YELLOW, stroke_width=5).shift(band_shift(8) + LEFT * 3.4 + DOWN * 0.4)
        taxi = Dot(band_shift(8) + LEFT * 3.4 + UP * 1.3, color=RED)
        self.play(Create(c))
        self.play(Create(taxi))
        self.wait(1)
        off = Arrow(band_shift(8) + LEFT * 1.7 + DOWN * 0.4, band_shift(8) + LEFT * 0.2 + DOWN * 0.4,
                    buff=0, color=BLUE, stroke_width=4)
        off_t = Tex("off: S, T, M").scale(0.85).next_to(off, DOWN, buff=0.1)
        on = Arrow(band_shift(8) + LEFT * 6.6 + DOWN * 0.4, band_shift(8) + LEFT * 5.1 + DOWN * 0.4,
                   buff=0, color=GREEN, stroke_width=4)
        on_t = Tex("on: I, G, X").scale(0.85).next_to(on, DOWN, buff=0.1)
        self.play(Create(off), Write(off_t))
        self.play(Create(on), Write(on_t))
        self.wait(2)
        b8_l1 = Tex("Steady route: off $=$ on").scale(0.95).shift(band_shift(8) + RIGHT * 3.2 + UP * 1.0)
        b8_l2 = Tex("Depot: R8m, spend 75c per rand").scale(0.9).shift(band_shift(8) + RIGHT * 3.2 + UP * 0.2)
        b8_l3 = MathTex(r"\frac{1}{0{,}25} = 4 \Rightarrow \text{R32m}").scale(1.0).shift(band_shift(8) + RIGHT * 3.2 + DOWN * 0.8)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Busy season, peak, quiet months, trough").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the purse and the stall ---
        self.next_band(9)
        b9_title = Tex("The nation's purse, the rand's stall").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(1.5)
        b9_l1 = Tex("In: income tax, VAT, company tax").scale(1.0).shift(band_shift(9) + UP * 1.4)
        b9_l2 = Tex("Out: schools, grants, clinics — and interest").scale(1.0).shift(band_shift(9) + UP * 0.7)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Tuckshop truth: free $=$ empty till,").scale(1.0).shift(band_shift(9) + DOWN * 0.2)
        b9_l4 = Tex("unpayable $=$ empty till — best rate between").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Rand's stall: buyers crowd $\\Rightarrow$ rand weakens;").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        b9_l6 = Tex("weak rand: exports and tourism win,").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        b9_l7 = Tex("petrol and medicine bite — hold both sides").scale(0.95).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.play(Create(SurroundingRectangle(b9_l7, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the pie and the report card ---
        self.next_band(10)
        b10_title = Tex("Growing the pie, reading the card").scale(1.15).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(1.5)
        b10_l1 = Tex("School shoes: levy keeps the cobbler,").scale(0.95).shift(band_shift(10) + UP * 1.4)
        b10_l2 = Tex("every family pays more — balance the mix").scale(0.95).shift(band_shift(10) + UP * 0.7)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("Bigger pie $\\ne$ more people eating:").scale(1.0).shift(band_shift(10) + DOWN * 0.2)
        b10_l4 = Tex("growth without development").scale(1.0).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Report card: prices, jobs, wellbeing —").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        b10_l6 = Tex("never judge one column alone").scale(0.95).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(2)
        b10_l7 = Tex("The skeleton never changes — only the numbers do").scale(0.95).shift(band_shift(10) + DOWN * 3.2)
        self.play(Write(b10_l7))
        self.wait(4)
