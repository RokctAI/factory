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
# apportioned to subtopics.json (215/230/245/225/185/185/190 of 1475 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FourSectorCircularFlowSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md plays (~4-5%).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): closed, open, four participants ---
        title = Tex("The Four-Sector Circular Flow").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        c1 = Tex(r"CLOSED: households + businesses (+ government)").scale(0.95).shift(UP * 1.2)
        c2 = Tex(r"OPEN: add the foreign sector — SA is open").scale(1.0).shift(UP * 0.4)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        p1 = Tex(r"Four participants: households, businesses,").scale(1.0).shift(DOWN * 0.5)
        p2 = Tex(r"government, foreign sector").scale(1.05).shift(DOWN * 1.3)
        self.play(Write(p1))
        self.play(Write(p2))
        self.wait(2)
        mk = Tex(r"Four markets: factor, product,").scale(1.0).shift(DOWN * 2.2)
        mk2 = Tex(r"financial, foreign exchange").scale(1.0).shift(DOWN * 2.9)
        self.play(Write(mk))
        self.play(Write(mk2))
        self.wait(3)

        # --- Band 1 (subtopic_1): the diagram, real vs money flow ---
        self.next_band(1)
        b1_title = Tex("Two currents close the loop").scale(1.15).shift(band_shift(1) + UP * 2.9)
        self.play(Write(b1_title))
        self.wait(1.5)
        hh = Rectangle(width=3.4, height=1.1).shift(band_shift(1) + LEFT * 4.6 + UP * 0.3)
        hh_lab = Tex("HOUSEHOLDS").scale(0.8).shift(band_shift(1) + LEFT * 4.6 + UP * 0.3)
        bs = Rectangle(width=3.4, height=1.1).shift(band_shift(1) + RIGHT * 4.6 + UP * 0.3)
        bs_lab = Tex("BUSINESSES").scale(0.8).shift(band_shift(1) + RIGHT * 4.6 + UP * 0.3)
        self.play(Create(hh), Write(hh_lab))
        self.play(Create(bs), Write(bs_lab))
        self.wait(1.5)
        gov = Rectangle(width=3.6, height=1.0).shift(band_shift(1) + UP * 2.0)
        gov_lab = Tex("GOVERNMENT").scale(0.75).shift(band_shift(1) + UP * 2.0)
        fs = Rectangle(width=3.6, height=1.0).shift(band_shift(1) + DOWN * 1.6)
        fs_lab = Tex("FOREIGN SECTOR").scale(0.7).shift(band_shift(1) + DOWN * 1.6)
        self.play(Create(gov), Write(gov_lab))
        self.play(Create(fs), Write(fs_lab))
        self.wait(1.5)
        real = Arrow(band_shift(1) + LEFT * 2.8 + UP * 0.7, band_shift(1) + RIGHT * 2.8 + UP * 0.7,
                     buff=0, color=BLUE)
        real_lab = Tex("real flow: work and goods", color=BLUE).scale(0.75).shift(band_shift(1) + UP * 1.15)
        money = Arrow(band_shift(1) + RIGHT * 2.8 + DOWN * 0.15, band_shift(1) + LEFT * 2.8 + DOWN * 0.15,
                      buff=0, color=GREEN)
        money_lab = Tex("money flow: income and spending", color=GREEN).scale(0.75).shift(band_shift(1) + DOWN * 0.55)
        self.play(Create(real), Write(real_lab))
        self.wait(2)
        self.play(Create(money), Write(money_lab))
        self.wait(2)
        wrong = Tex(r"Money and goods share a ring").scale(0.95).shift(band_shift(1) + DOWN * 2.5 + LEFT * 3.0)
        self.play(Write(wrong))
        self.play(Create(strike(wrong)))
        self.wait(1.5)
        rule = Tex(r"Things one ring; rands the other").scale(0.95).shift(band_shift(1) + DOWN * 2.5 + RIGHT * 3.3)
        self.play(Write(rule))
        self.play(Create(SurroundingRectangle(rule, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): leakages, injections, the condition ---
        self.next_band(2)
        b2_title = Tex("Leakages out, injections in").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        lk = Tex(r"Leakages: S (saving), T (tax), M (imports)").scale(1.0).shift(band_shift(2) + UP * 1.2)
        inj = Tex(r"Injections: I (investment), G, X (exports)").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(lk))
        self.wait(2)
        self.play(Write(inj))
        self.wait(2)
        pair = Tex(r"Three doors: S--I, T--G, M--X").scale(1.05).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(pair))
        self.wait(2)
        cond = MathTex(r"S + T + M = I + G + X").scale(1.3).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(cond))
        self.play(Create(SurroundingRectangle(cond, color=GREEN)))
        self.wait(2)
        trap = Tex(r"Every pair balances alone").scale(1.0).shift(band_shift(2) + DOWN * 2.5 + LEFT * 2.8)
        self.play(Write(trap))
        self.play(Create(strike(trap)))
        tot = Tex(r"Only the TOTALS must").scale(1.0).shift(band_shift(2) + DOWN * 2.5 + RIGHT * 3.6)
        self.play(Write(tot))
        self.wait(3)

        # --- Band 3 (subtopic_2): the worked balance ---
        self.next_band(3)
        b3_title = Tex("Test it, in R billions").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        w1 = MathTex(r"S + T + M = 250 + 550 + 300 = 1\,100").scale(1.1).shift(band_shift(3) + UP * 1.1)
        w2 = MathTex(r"I + G + X = 300 + 500 + 300 = 1\,100").scale(1.1).shift(band_shift(3) + UP * 0.2)
        self.play(Write(w1))
        self.wait(2.5)
        self.play(Write(w2))
        self.wait(2.5)
        w3 = Tex(r"Totals agree — national income holds steady").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(w3))
        self.play(Create(SurroundingRectangle(w3, color=GREEN)))
        self.wait(2)
        w4 = MathTex(r"\text{Same fact: } Y = C + I + G + (X - M)").scale(1.05).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(w4))
        self.wait(2)
        w5 = Tex(r"Spent $=$ earned $=$ produced").scale(1.05).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(w5))
        self.wait(3)

        # --- Band 4 (subtopic_3): three methods, market to factor cost ---
        self.next_band(4)
        b4_title = Tex("One river, three bridges").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        m1 = Tex(r"Production: value ADDED, never turnover").scale(1.0).shift(band_shift(4) + UP * 1.2)
        m2 = Tex(r"Income: what the factors were paid").scale(1.0).shift(band_shift(4) + UP * 0.5)
        m3 = MathTex(r"\text{Expenditure: } C + I + G + (X - M)").scale(1.0).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(m1))
        self.wait(2)
        self.play(Write(m2))
        self.wait(1.5)
        self.play(Write(m3))
        self.wait(2)
        conv = Tex(r"Factor cost $=$ market prices $-$ taxes $+$ subsidies").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(conv))
        self.wait(2)
        calc = MathTex(r"7\,000 - 800 + 120 = R6\,320\text{ bn}").scale(1.1).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(calc))
        self.play(Create(SurroundingRectangle(calc, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): GNI, real, per capita ---
        self.next_band(5)
        b5_title = Tex("Domestic to national, nominal to real").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        g1 = Tex(r"GNI: add income received, subtract income paid").scale(0.95).shift(band_shift(5) + UP * 1.2)
        g2 = MathTex(r"7\,000 + 90 - 260 = R6\,830\text{ bn}").scale(1.1).shift(band_shift(5) + UP * 0.3)
        self.play(Write(g1))
        self.wait(2)
        self.play(Write(g2))
        self.wait(2)
        g3 = Tex(r"More foreign capital works here: GNI $<$ GDP").scale(0.95).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(g3))
        self.wait(2)
        r1 = MathTex(r"\text{Real} = 7\,000 \times \tfrac{100}{125} = R5\,600\text{ bn}").scale(1.05).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(r1))
        self.play(Create(SurroundingRectangle(r1, color=GREEN)))
        self.wait(2)
        r2 = Tex(r"$\div$ 63 m people $\approx$ R89\,000 per person").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(r2))
        self.wait(3)

        # --- Band 6 (subtopic_4): leakages exceed injections ---
        self.next_band(6)
        b6_title = Tex("Disequilibrium: the drains win").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        d1 = MathTex(r"X: 300 \rightarrow 240 \;\Rightarrow\; 1\,040 < 1\,100").scale(1.05).shift(band_shift(6) + UP * 1.2)
        self.play(Write(d1))
        self.wait(2)
        d2 = Tex(r"Stock piles up $\rightarrow$ output cut $\rightarrow$ retrench").scale(0.95).shift(band_shift(6) + UP * 0.3)
        d3 = Tex(r"$\rightarrow$ incomes fall $\rightarrow$ S, T, M shrink").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(d2))
        self.wait(2)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex(r"Balance returns at LOWER income,").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        d5 = Tex(r"more unemployment — a downswing").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(d4))
        self.play(Write(d5))
        self.play(Create(SurroundingRectangle(d5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): injections win, capacity, policy ---
        self.next_band(7)
        b7_title = Tex("The taps win — and the policy doorway").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        u1 = Tex(r"Stocks run down $\rightarrow$ output, jobs, incomes rise").scale(0.9).shift(band_shift(7) + UP * 1.2)
        self.play(Write(u1))
        self.wait(2)
        u2 = Tex(r"Idle capacity: more output and jobs").scale(1.0).shift(band_shift(7) + UP * 0.4)
        u3 = Tex(r"Near capacity: mainly INFLATION").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(u2))
        self.wait(2)
        self.play(Write(u3))
        self.wait(2)
        u4 = Tex(r"Self-correcting in direction, not in outcome").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(u4))
        self.wait(2)
        u5 = Tex(r"Fiscal: G, T; monetary: S, I; trade: X, M").scale(1.0).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(u5))
        self.play(Create(SurroundingRectangle(u5, color=GREEN)))
        u6 = Tex(r"A rand injected lifts Y by more — the multiplier").scale(0.9).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(u6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): month-end in the factory town ---
        self.next_band(8)
        b8_title = Tex("Month-end money goes around").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        s1 = Tex(r"Families supply WORK;").scale(1.05).shift(band_shift(8) + UP * 1.2)
        s2 = Tex(r"the factory returns MONEY").scale(1.05).shift(band_shift(8) + UP * 0.5)
        self.play(Write(s1))
        self.play(Write(s2))
        self.wait(2.5)
        s3 = Tex(r"Two rings, opposite directions:").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        s4 = Tex(r"one carries things, one carries rands").scale(1.0).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(s3))
        self.play(Write(s4))
        self.wait(2.5)
        s5 = Tex(r"Money is not consumed — it circulates").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(s5))
        self.play(Create(SurroundingRectangle(s5, color=GREEN)))
        self.wait(2.5)
        s6 = Tex(r"Four players, four meeting places").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(s6))
        self.wait(3)

        # --- Band 9 (subtopic_6): taps and drains ---
        self.next_band(9)
        b9_title = Tex("Taps and drains").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        # Water-tank diagram: rectangle tank, tap arrows in, drain arrows out
        tank = Rectangle(width=5.0, height=1.8).shift(band_shift(9) + UP * 0.4)
        level = Tex("level $=$ national income").scale(0.8).shift(band_shift(9) + UP * 0.4)
        self.play(Create(tank), Write(level))
        self.wait(1.5)
        tap1 = Arrow(band_shift(9) + UP * 2.0 + LEFT * 1.6, band_shift(9) + UP * 1.35 + LEFT * 1.6, buff=0, color=GREEN)
        tap2 = Arrow(band_shift(9) + UP * 2.0, band_shift(9) + UP * 1.35, buff=0, color=GREEN)
        tap3 = Arrow(band_shift(9) + UP * 2.0 + RIGHT * 1.6, band_shift(9) + UP * 1.35 + RIGHT * 1.6, buff=0, color=GREEN)
        taps_lab = Tex("taps in: I, G, X", color=GREEN).scale(0.85).shift(band_shift(9) + UP * 1.7 + RIGHT * 4.3)
        self.play(Create(tap1), Create(tap2), Create(tap3), Write(taps_lab))
        self.wait(2)
        dr1 = Arrow(band_shift(9) + DOWN * 0.5 + LEFT * 1.6, band_shift(9) + DOWN * 1.15 + LEFT * 1.6, buff=0, color=RED)
        dr2 = Arrow(band_shift(9) + DOWN * 0.5, band_shift(9) + DOWN * 1.15, buff=0, color=RED)
        dr3 = Arrow(band_shift(9) + DOWN * 0.5 + RIGHT * 1.6, band_shift(9) + DOWN * 1.15 + RIGHT * 1.6, buff=0, color=RED)
        dr_lab = Tex("drains out: S, T, M", color=RED).scale(0.85).shift(band_shift(9) + DOWN * 0.9 + RIGHT * 4.3)
        self.play(Create(dr1), Create(dr2), Create(dr3), Write(dr_lab))
        self.wait(2)
        rule9 = Tex(r"Steady when taps TOGETHER match drains").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(rule9))
        self.wait(2)
        num9 = MathTex(r"250+550+300 = 300+500+300 = 1\,100").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(num9))
        self.play(Create(SurroundingRectangle(num9, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): when the bucket won't sit still ---
        self.next_band(10)
        b10_title = Tex("When the bucket won't sit still").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        f1 = MathTex(r"\text{Exports } 300 \rightarrow 240: \text{ the level falls}").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(f1))
        self.wait(2)
        f2 = Tex(r"Jeans stack up $\rightarrow$ shift dropped $\rightarrow$ thinner").scale(0.95).shift(band_shift(10) + UP * 0.4)
        f3 = Tex(r"payslips $\rightarrow$ less at the shop, each turn smaller").scale(0.9).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(f2))
        self.play(Write(f3))
        self.wait(2.5)
        f4 = Tex(r"It settles — LOWER. Balanced $\neq$ well").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(f4))
        self.play(Create(SurroundingRectangle(f4, color=GREEN)))
        self.wait(2.5)
        f5 = Tex(r"Machines already flat out: money bids up prices").scale(0.9).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(f5))
        self.wait(2)
        f6 = Tex(r"Every headline is a tap or a drain").scale(1.0).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(f6))
        self.wait(4)
