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

# Band-layout whiteboard scene for the Paper 1 revision-essentials duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 250/240/240/250/195/195/190 of 1560 s — bands
# 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10 apportioned to match.
# Circular-flow, Laffer and forex sketches hand-built from
# Arrow/Line/Dot/Rectangle/Tex primitives only.

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
    yl = Tex(ylab).scale(0.9).next_to(origin + UP * h, RIGHT, buff=0.15)
    return VGroup(xa, ya, xl, yl)


def chain(origin, pts, color=WHITE, sw=5):
    g = VGroup()
    for a, b in zip(pts[:-1], pts[1:]):
        g.add(Line(origin + RIGHT * a[0] + UP * a[1],
                   origin + RIGHT * b[0] + UP * b[1],
                   color=color, stroke_width=sw))
    return g


class PaperOneMacroEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # --- Band 0 (subtopic_1): the open circular flow ---
        title = Tex("Paper 1 Essentials: Macro and Pursuits").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        hh = Rectangle(width=3.6, height=1.3).shift(LEFT * 4.4 + UP * 0.7)
        hh_lab = Tex("Households").scale(1.0).shift(LEFT * 4.4 + UP * 0.7)
        bs = Rectangle(width=3.6, height=1.3).shift(RIGHT * 4.4 + UP * 0.7)
        bs_lab = Tex("Businesses").scale(1.0).shift(RIGHT * 4.4 + UP * 0.7)
        self.play(Create(hh), Write(hh_lab))
        self.play(Create(bs), Write(bs_lab))
        self.wait(1.5)
        top_ar = Arrow(LEFT * 2.5 + UP * 1.2, RIGHT * 2.5 + UP * 1.2, buff=0, stroke_width=4, color=BLUE)
        top_lab = Tex("real flow: labour, goods").scale(0.85).shift(UP * 1.7)
        bot_ar = Arrow(RIGHT * 2.5 + UP * 0.2, LEFT * 2.5 + UP * 0.2, buff=0, stroke_width=4, color=YELLOW)
        bot_lab = Tex("money flow: wages, spending").scale(0.85).shift(DOWN * 0.3)
        self.play(Create(top_ar), Write(top_lab))
        self.play(Create(bot_ar), Write(bot_lab))
        self.wait(2)
        st = Rectangle(width=3.2, height=1.2).shift(LEFT * 4.4 + DOWN * 1.8)
        st_lab = Tex("State").scale(1.0).shift(LEFT * 4.4 + DOWN * 1.8)
        fo = Rectangle(width=3.2, height=1.2).shift(RIGHT * 4.4 + DOWN * 1.8)
        fo_lab = Tex("Foreign sector").scale(0.9).shift(RIGHT * 4.4 + DOWN * 1.8)
        st_ar = Arrow(LEFT * 4.4 + DOWN * 1.2, LEFT * 4.4 + UP * 0.05, buff=0, stroke_width=3)
        fo_ar = Arrow(RIGHT * 4.4 + DOWN * 1.2, RIGHT * 4.4 + UP * 0.05, buff=0, stroke_width=3)
        self.play(Create(st), Write(st_lab), Create(st_ar))
        self.play(Create(fo), Write(fo_lab), Create(fo_ar))
        self.wait(2)
        note = Tex("Taxes and services; exports and imports —").scale(0.95).shift(DOWN * 2.7)
        note2 = Tex("the financial sector turns savings into investment").scale(0.95).shift(DOWN * 3.3)
        self.play(Write(note))
        self.play(Write(note2))
        self.wait(3)

        # --- Band 1 (subtopic_1): equalities, multiplier, cycles ---
        self.next_band(1)
        b1_title = Tex("The equalities and the multiplier").scale(1.15).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"L = S + T + M, \quad J = I + G + X").scale(1.1).shift(band_shift(1) + UP * 1.7)
        b1_l2 = MathTex(r"Y = C + I + G + (X - M)").scale(1.1).shift(band_shift(1) + UP * 0.8)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = MathTex(r"\text{Multiplier} = \frac{1}{1 - mpc} = \frac{1}{mps}").scale(1.05).shift(band_shift(1) + DOWN * 0.2)
        b1_l4 = MathTex(r"mpc = 0{,}6: \;\; \frac{1}{0{,}4} = 2{,}5").scale(1.05).shift(band_shift(1) + DOWN * 1.1)
        b1_l5 = MathTex(r"\text{R}10\text{ bn} \times 2{,}5 = \text{R}25\text{ bn}").scale(1.05).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(2)
        b1_l6 = Tex("Cycles: monetarists blame outside shocks;").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        b1_l7 = Tex("Keynesians see causes inside — intervene").scale(0.95).shift(band_shift(1) + DOWN * 3.4)
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.wait(3)

        # --- Band 2 (subtopic_2): public sector and the budget ---
        self.next_band(2)
        b2_title = Tex("The public sector and the budget").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Five objectives: growth, full employment, price").scale(1.0).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("stability, external stability, equity").scale(1.0).shift(band_shift(2) + UP * 0.7)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("MTEF: rolling 3-year spending plan;").scale(1.0).shift(band_shift(2) + DOWN * 0.2)
        b2_l4 = Tex("MTBPS: the October mini-budget update").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(VGroup(b2_l3, b2_l4), color=GREEN)))
        self.wait(2.5)
        b2_l5 = Tex("Revenue: personal income tax, VAT, company tax").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        b2_l6 = Tex("Watch public debt as a percentage of GDP").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): the Laffer curve and public failure ---
        self.next_band(3)
        b3_title = Tex("The Laffer curve, and public failure").scale(1.15).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        o = band_shift(3) + LEFT * 5.6 + DOWN * 1.8
        ax = axes(o, 5.4, 3.6, "tax rate", "revenue")
        self.play(Create(ax))
        laf = chain(o, [(0.3, 0.2), (1.4, 1.9), (2.6, 2.9), (3.8, 2.0), (4.9, 0.3)], color=YELLOW)
        self.play(Create(laf), run_time=1.5)
        opt = DashedLine(o + RIGHT * 2.6, o + RIGHT * 2.6 + UP * 2.9, stroke_width=3)
        opt_lab = Tex("optimal").scale(0.85).next_to(o + RIGHT * 2.6, DOWN, buff=0.15)
        self.play(Create(opt), Write(opt_lab))
        self.wait(2)
        b3_l1 = Tex("Zero at 0\\% and at 100\\%;").scale(0.95).shift(band_shift(3) + RIGHT * 3.4 + UP * 1.2)
        b3_l2 = Tex("beyond the peak, cutting").scale(0.95).shift(band_shift(3) + RIGHT * 3.4 + UP * 0.4)
        b3_l3 = Tex("rates RAISES revenue").scale(0.95).shift(band_shift(3) + RIGHT * 3.4 + DOWN * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Public failure: bureaucracy, political interference,").scale(0.95).shift(band_shift(3) + DOWN * 2.5)
        b3_l5 = Tex("weak management, special interests").scale(0.95).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the balance of payments ---
        self.next_band(4)
        b4_title = Tex("Balance of payments: three accounts").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Current: goods, net gold, services, income").scale(1.0).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("Capital transfer: small and quiet").scale(1.0).shift(band_shift(4) + UP * 0.6)
        b4_l3 = Tex("Financial: direct, portfolio, reserves").scale(1.0).shift(band_shift(4) + DOWN * 0.2)
        for m in (b4_l1, b4_l2, b4_l3):
            self.play(Write(m))
            self.wait(1.8)
        b4_l4 = Tex("Foreign firm buys a bank $\\rightarrow$ direct investment;").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        b4_l5 = Tex("foreigner buys JSE shares $\\rightarrow$ portfolio").scale(0.95).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2.5)
        b4_l6 = Tex("Deficit fixes: raise rates, promote exports,").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        b4_l7 = Tex("substitute imports, let the rand adjust").scale(1.0).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l6))
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_3): the market for dollars ---
        self.next_band(5)
        b5_title = Tex("The market for dollars").scale(1.15).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_title))
        self.wait(1.5)
        o2 = band_shift(5) + LEFT * 5.4 + DOWN * 2.2
        ax2 = axes(o2, 5.6, 4.0, "Q dollars", "R per \\$")
        self.play(Create(ax2))
        dd = chain(o2, [(0.5, 3.4), (2.4, 2.0), (4.4, 0.9)], color=BLUE)
        dd_lab = Tex("D: importers").scale(0.8).next_to(o2 + RIGHT * 4.4 + UP * 0.9, RIGHT, buff=0.1)
        ss = chain(o2, [(0.5, 0.8), (2.4, 2.0), (4.4, 3.3)], color=YELLOW)
        ss_lab = Tex("S: exporters").scale(0.8).next_to(o2 + RIGHT * 4.4 + UP * 3.3, RIGHT, buff=0.1)
        self.play(Create(dd), Write(dd_lab))
        self.play(Create(ss), Write(ss_lab))
        e_dot = Dot(o2 + RIGHT * 2.4 + UP * 2.0, color=GREEN)
        self.play(Create(e_dot))
        self.wait(2)
        b5_l1 = Tex("More imports: D right, dollar").scale(0.95).shift(band_shift(5) + RIGHT * 3.6 + UP * 1.4)
        b5_l2 = Tex("dearer — rand DEPRECIATES").scale(0.95).shift(band_shift(5) + RIGHT * 3.6 + UP * 0.6)
        b5_l3 = Tex("Export surge: S right —").scale(0.95).shift(band_shift(5) + RIGHT * 3.6 + DOWN * 0.3)
        b5_l4 = Tex("rand APPRECIATES").scale(0.95).shift(band_shift(5) + RIGHT * 3.6 + DOWN * 1.1)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(1.6)
        b5_l5 = MathTex(r"\text{Terms of trade} = \frac{\text{export index}}{\text{import index}} \times 100").scale(0.81).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the trade-policy debate ---
        self.next_band(6)
        b6_title = Tex("Trade policy: promote or protect?").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Export promotion: incentives push firms out —").scale(1.0).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("danger: subsidised firms that never compete").scale(1.0).shift(band_shift(6) + UP * 0.7)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Import substitution: tariffs shelter home firms —").scale(1.0).shift(band_shift(6) + DOWN * 0.2)
        b6_l4 = Tex("danger: inefficiency and higher prices").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("For protection: infants, jobs, dumping;").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        b6_l6 = Tex("for free trade: specialisation, scale, choice").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(2)
        b6_l7 = Tex("Answer: a desirable mix — WTO, SACU, SADC, BRICS").scale(0.95).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6_l7))
        self.play(Create(SurroundingRectangle(b6_l7, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): growth, plans and indicators ---
        self.next_band(7)
        b7_title = Tex("Growth, the plans, the indicators").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("GROWTH: real GDP rises. DEVELOPMENT:").scale(1.0).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("living standards and choices improve").scale(1.0).shift(band_shift(7) + UP * 0.7)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(VGroup(b7_l1, b7_l2), color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("The alphabet in order: RDP $\\rightarrow$ GEAR $\\rightarrow$").scale(1.0).shift(band_shift(7) + DOWN * 0.3)
        b7_l4 = Tex("AsgiSA/JIPSA $\\rightarrow$ New Growth Path $\\rightarrow$ NDP 2030").scale(0.95).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Economic indicators: CPI, PPI, exchange rate,").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        b7_l6 = Tex("unemployment, productivity, repo, M1–M3;").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        b7_l7 = Tex("social: life expectancy, water, education").scale(1.0).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.play(Write(b7_l7))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the taxi route ---
        self.next_band(8)
        b8_title = Tex("Round and round: one big taxi route").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Money circles like the taxi: labour out, wages").scale(1.0).shift(band_shift(8) + UP * 1.5)
        b8_l2 = Tex("back, spending round again").scale(1.0).shift(band_shift(8) + UP * 0.8)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Passengers off — savings, taxes, imports: LEAKS").scale(1.0).shift(band_shift(8))
        b8_l4 = Tex("Passengers on — investment, G, exports: INJECTIONS").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = MathTex(r"\text{spend } 60\text{c of each rand: } \frac{1}{0{,}4} = 2{,}5").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2.5)
        b8_l6 = Tex("Cycle: busy season, peak, quiet season, trough —").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        b8_l7 = Tex("potholes from outside, or the passengers' moods?").scale(0.95).shift(band_shift(8) + DOWN * 3.2)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): the purse and the price of the rand ---
        self.next_band(9)
        b9_title = Tex("The nation's purse, the price of the rand").scale(1.1).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Purse in: income tax, VAT, company tax;").scale(1.0).shift(band_shift(9) + UP * 1.5)
        b9_l2 = Tex("out: grants, schools, health — and debt interest").scale(1.0).shift(band_shift(9) + UP * 0.8)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Lemonade truth: price at nothing, earn nothing;").scale(1.0).shift(band_shift(9))
        b9_l4 = Tex("too high, earn nothing — the Laffer curve").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("The rand is a price: importers buy dollars,").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        b9_l6 = Tex("exporters bring them; scarce dollars = weak rand").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(2)
        b9_l7 = Tex("Weak rand: exports boom, petrol hurts — say both").scale(0.95).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9_l7))
        self.play(Create(SurroundingRectangle(b9_l7, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the bakery, the pie, the report card ---
        self.next_band(10)
        b10_title = Tex("The bakery, the pie, the report card").scale(1.15).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Protect the local bakery: jobs stay, bread costs").scale(1.0).shift(band_shift(10) + UP * 1.5)
        b10_l2 = Tex("more; open the road: cheaper bread, baker must").scale(1.0).shift(band_shift(10) + UP * 0.8)
        b10_l3 = Tex("compete — the answer is balance").scale(1.0).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(3)
        b10_l4 = Tex("Bigger pie (growth) is not more people eating").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        b10_l5 = Tex("(development) — plans from RDP to NDP try both").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex("Indicators are the report card — never read").scale(1.0).shift(band_shift(10) + DOWN * 2.4)
        b10_l7 = Tex("one column alone; look for the pattern").scale(1.0).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.play(Create(SurroundingRectangle(b10_l7, color=GREEN)))
        self.wait(4)
