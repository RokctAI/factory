# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band layout: content lives in sequential one-frame-tall bands down a long
# virtual canvas; the camera moves, nothing is ever removed. Exporter-safe
# vocabulary only (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/VGroup) and
# write-only reveals — no Transform/FadeOut/sub-part indexing.
#
# Mirrors script.md across the seven subtopics of the duo
# (Expert 1-4: bands 0-7; Simplifier 5-7: bands 8-10), scene time
# apportioned to subtopics.json (240/245/250/250/195/200/200 of 1580 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MarketsAndMacroeconomyEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md audio plays (~4-5%).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): three questions, three systems ---
        title = Tex("Markets and Macroeconomy Essentials").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        q3 = Tex(r"WHAT to produce? \; HOW? \; FOR WHOM?").scale(1.15).shift(UP * 1.3)
        self.play(Write(q3))
        self.wait(2)
        s1 = Tex(r"Free market: prices answer").scale(1.1).shift(UP * 0.4)
        s2 = Tex(r"Planned: the state answers").scale(1.1).shift(DOWN * 0.4)
        s3 = Tex(r"Every real economy is MIXED").scale(1.1).shift(DOWN * 1.2)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.wait(2)
        self.play(Write(s3))
        self.wait(2)
        s4 = Tex(r"SA: mixed AND dualistic — two economies").scale(1.1).shift(DOWN * 2.2)
        self.play(Write(s4))
        self.play(Create(SurroundingRectangle(s4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): four factors and their rewards ---
        self.next_band(1)
        b1_title = Tex("The four factors and their rewards").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        f1 = Tex(r"Natural resources $\rightarrow$ RENT").scale(1.1).shift(band_shift(1) + UP * 1.1)
        f2 = Tex(r"Labour $\rightarrow$ WAGES (human capital)").scale(1.1).shift(band_shift(1) + UP * 0.3)
        f3 = Tex(r"Capital $\rightarrow$ INTEREST").scale(1.1).shift(band_shift(1) + DOWN * 0.5)
        f4 = Tex(r"Entrepreneurship $\rightarrow$ PROFIT").scale(1.1).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(f1))
        self.wait(1.5)
        self.play(Write(f2))
        self.wait(1.5)
        self.play(Write(f3))
        self.wait(1.5)
        wrong = Tex(r"Capital $=$ money itself").scale(1.0).shift(band_shift(1) + DOWN * 2.1 + LEFT * 3.2)
        self.play(Write(wrong))
        self.play(Create(strike(wrong)))
        self.wait(1.5)
        self.play(Write(f4))
        self.wait(1.5)
        resid = Tex(r"Profit $=$ the RESIDUAL — reward for risk").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(resid))
        self.play(Create(SurroundingRectangle(resid, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): three methods, one GDP ---
        self.next_band(2)
        b2_title = Tex("One economy, three measurements").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        m1 = Tex(r"Production: sum of value added (GVA)").scale(1.05).shift(band_shift(2) + UP * 1.1)
        m2 = Tex(r"Income: wages + rent + interest + profit").scale(1.05).shift(band_shift(2) + UP * 0.3)
        m3 = MathTex(r"\text{Expenditure: } C + I + G + (X - M)").scale(1.1).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(m1))
        self.wait(2)
        self.play(Write(m2))
        self.wait(2)
        self.play(Write(m3))
        self.play(Create(SurroundingRectangle(m3, color=GREEN)))
        self.wait(2)
        gwrong = Tex(r"G includes social grants").scale(1.0).shift(band_shift(2) + DOWN * 1.6 + LEFT * 2.8)
        self.play(Write(gwrong))
        self.play(Create(strike(gwrong)))
        gright = Tex(r"G $=$ consumption: nurses, teachers").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(gright))
        self.wait(2)
        gni = Tex(r"GNI $=$ GDP $+$ income from abroad $-$ outflow").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(gni))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): sectors and infrastructure ---
        self.next_band(3)
        b3_title = Tex("Sectors and infrastructure").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        # Three sector boxes chained with arrows
        box1 = Rectangle(width=3.4, height=1.0).shift(band_shift(3) + UP * 1.0 + LEFT * 4.2)
        box2 = Rectangle(width=3.4, height=1.0).shift(band_shift(3) + UP * 1.0)
        box3 = Rectangle(width=3.4, height=1.0).shift(band_shift(3) + UP * 1.0 + RIGHT * 4.2)
        t1 = Tex("PRIMARY: takes").scale(0.8).shift(band_shift(3) + UP * 1.0 + LEFT * 4.2)
        t2 = Tex("SECONDARY: transforms").scale(0.7).shift(band_shift(3) + UP * 1.0)
        t3 = Tex("TERTIARY: serves").scale(0.8).shift(band_shift(3) + UP * 1.0 + RIGHT * 4.2)
        a12 = Arrow(band_shift(3) + UP * 1.0 + LEFT * 2.5, band_shift(3) + UP * 1.0 + LEFT * 1.7, buff=0)
        a23 = Arrow(band_shift(3) + UP * 1.0 + RIGHT * 1.7, band_shift(3) + UP * 1.0 + RIGHT * 2.5, buff=0)
        self.play(Create(box1), Write(t1))
        self.wait(1.5)
        self.play(Create(a12), Create(box2), Write(t2))
        self.wait(1.5)
        self.play(Create(a23), Create(box3), Write(t3))
        self.wait(2)
        chain = Tex(r"Chains: iron ore $\rightarrow$ steel $\rightarrow$ construction").scale(1.0).shift(band_shift(3) + DOWN * 0.1)
        self.play(Write(chain))
        self.wait(2)
        shift_line = Tex(r"Tertiary now $\approx$ two-thirds of GDP").scale(1.05).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(shift_line))
        self.wait(2)
        infra = Tex(r"Infrastructure $=$ the skeleton: power, transport").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(infra))
        self.wait(1.5)
        gate = Tex(r"Load-shedding: every sector limps").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(gate))
        self.play(Create(SurroundingRectangle(gate, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): PED and the two curve shapes ---
        self.next_band(4)
        b4_title = Tex("Price elasticity of demand").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        ped = MathTex(r"PED = \frac{\%\Delta Q_d}{\%\Delta P}").scale(1.15).shift(band_shift(4) + UP * 1.0)
        self.play(Write(ped))
        self.wait(2)
        cats = Tex(r"$>1$ elastic, $<1$ inelastic, $=1$ unitary").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(cats))
        self.wait(2)
        # Hand-built axes: P vertical, Q horizontal
        origin = band_shift(4) + DOWN * 2.9 + LEFT * 5.0
        y_ax = Arrow(origin, origin + UP * 2.4, buff=0, stroke_width=3)
        x_ax = Arrow(origin, origin + RIGHT * 5.2, buff=0, stroke_width=3)
        p_lab = Tex("P").scale(0.9).shift(origin + UP * 2.4 + LEFT * 0.35)
        q_lab = Tex("Q").scale(0.9).shift(origin + RIGHT * 5.2 + DOWN * 0.35)
        self.play(Create(y_ax), Create(x_ax))
        self.play(Write(p_lab), Write(q_lab))
        self.wait(1)
        # Elastic: flat demand curve (two chained segments)
        el1 = Line(origin + UP * 1.6 + RIGHT * 0.5, origin + UP * 1.2 + RIGHT * 2.6, color=BLUE)
        el2 = Line(origin + UP * 1.2 + RIGHT * 2.6, origin + UP * 0.8 + RIGHT * 4.7, color=BLUE)
        el_lab = Tex("elastic: flat", color=BLUE).scale(0.85).shift(origin + UP * 1.7 + RIGHT * 3.9)
        self.play(Create(el1), Create(el2))
        self.play(Write(el_lab))
        self.wait(1.5)
        # Inelastic: steep demand curve
        in1 = Line(origin + UP * 2.2 + RIGHT * 1.3, origin + UP * 1.1 + RIGHT * 1.7, color=ORANGE)
        in2 = Line(origin + UP * 1.1 + RIGHT * 1.7, origin + RIGHT * 2.1 + UP * 0.15, color=ORANGE)
        in_lab = Tex("inelastic: steep", color=ORANGE).scale(0.85).shift(origin + UP * 2.3 + RIGHT * 3.3)
        self.play(Create(in1), Create(in2))
        self.play(Write(in_lab))
        self.wait(2)
        det = Tex(r"Determinants: substitutes, necessity, time").scale(0.95).shift(band_shift(4) + DOWN * 0.8 + RIGHT * 2.0)
        self.play(Write(det))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): revenue payoff, costs, MR = MC ---
        self.next_band(5)
        b5_title = Tex(r"Revenue, costs and the profit rule").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        tr = MathTex(r"TR = P \times Q").scale(1.15).shift(band_shift(5) + UP * 1.2)
        self.play(Write(tr))
        self.wait(1.5)
        r1 = Tex(r"Inelastic: raise P $\Rightarrow$ TR rises (bread)").scale(1.0).shift(band_shift(5) + UP * 0.4)
        r2 = Tex(r"Elastic: raise P $\Rightarrow$ TR falls; a CUT can raise it").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2)
        c1 = Tex(r"Fixed costs: owed at zero output (rent)").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        c2 = Tex(r"Price taker: $MR = P$").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(1.5)
        rule = MathTex(r"\text{Stop where } MR = MC").scale(1.15).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(rule))
        self.play(Create(SurroundingRectangle(rule, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): connected markets ---
        self.next_band(6)
        b6_title = Tex("Connected markets").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        sub = Tex(r"Substitutes: beef P up $\Rightarrow$ chicken D right").scale(1.0).shift(band_shift(6) + UP * 1.2)
        comp = Tex(r"Complements: petrol P up $\Rightarrow$ car D left").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(sub))
        self.wait(2)
        self.play(Write(comp))
        self.wait(2)
        # Mini diagram: demand shift right for chicken
        o6 = band_shift(6) + DOWN * 2.9 + LEFT * 5.6
        y6 = Arrow(o6, o6 + UP * 2.3, buff=0, stroke_width=3)
        x6 = Arrow(o6, o6 + RIGHT * 4.0, buff=0, stroke_width=3)
        p6 = Tex("P").scale(0.8).shift(o6 + UP * 2.3 + LEFT * 0.3)
        q6 = Tex("Q").scale(0.8).shift(o6 + RIGHT * 4.0 + DOWN * 0.3)
        d_old = Line(o6 + UP * 1.9 + RIGHT * 0.4, o6 + UP * 0.3 + RIGHT * 2.2, color=BLUE)
        d_new = Line(o6 + UP * 1.9 + RIGHT * 1.5, o6 + UP * 0.3 + RIGHT * 3.3, color=GREEN)
        d_lab = MathTex(r"D", color=BLUE).scale(0.8).shift(o6 + UP * 0.15 + RIGHT * 2.5)
        d2_lab = MathTex(r"D_2", color=GREEN).scale(0.8).shift(o6 + UP * 0.15 + RIGHT * 3.7)
        sh = Arrow(o6 + UP * 1.3 + RIGHT * 1.3, o6 + UP * 1.3 + RIGHT * 2.4, buff=0, color=YELLOW)
        self.play(Create(y6), Create(x6), Write(p6), Write(q6))
        self.play(Create(d_old), Write(d_lab))
        self.wait(1.5)
        self.play(Create(d_new), Write(d2_lab), Create(sh))
        self.wait(2)
        mech = Tex(r"The CURVE shifts — say the mechanism").scale(0.95).shift(band_shift(6) + DOWN * 0.7 + RIGHT * 2.6)
        self.play(Write(mech))
        self.wait(1.5)
        loop = Tex(r"Labour demand is DERIVED from products").scale(0.95).shift(band_shift(6) + DOWN * 1.6 + RIGHT * 2.6)
        self.play(Write(loop))
        self.wait(1.5)
        structs = Tex(r"Count sellers: many, many varied, few, one").scale(0.9).shift(band_shift(6) + DOWN * 2.5 + RIGHT * 2.6)
        self.play(Write(structs))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): the two policy steering wheels ---
        self.next_band(7)
        b7_title = Tex("The two policy steering wheels").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        mon = Tex(r"MONETARY: SARB, repo rate").scale(1.05).shift(band_shift(7) + UP * 1.2 + LEFT * 3.2)
        fis = Tex(r"FISCAL: budget — G and taxes").scale(1.05).shift(band_shift(7) + UP * 1.2 + RIGHT * 3.2)
        self.play(Write(mon))
        self.play(Write(fis))
        self.wait(2)
        chain7 = Tex(r"Repo up $\Rightarrow$ prime up $\Rightarrow$ borrowing falls").scale(0.93).shift(band_shift(7) + UP * 0.3)
        chain7b = Tex(r"$\Rightarrow$ demand cools $\Rightarrow$ inflation eases").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(chain7))
        self.wait(2)
        self.play(Write(chain7b))
        self.wait(2)
        target = Tex(r"Inflation target: 3\% to 6\%").scale(1.1).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(target))
        self.play(Create(SurroundingRectangle(target, color=GREEN)))
        self.wait(2)
        speed = Tex(r"Repo moves in an afternoon; budgets yearly").scale(0.95).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(speed))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): three kitchens, four pay packets ---
        self.next_band(8)
        b8_title = Tex("Three kitchens and four pay packets").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        k1 = Tex(r"Kitchen 1: the till decides — free market").scale(1.0).shift(band_shift(8) + UP * 1.2)
        k2 = Tex(r"Kitchen 2: head office faxes the menu — planned").scale(0.95).shift(band_shift(8) + UP * 0.4)
        k3 = Tex(r"Kitchen 3: till + inspector — mixed (ours)").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(k1))
        self.wait(2.5)
        self.play(Write(k2))
        self.wait(2.5)
        self.play(Write(k3))
        self.wait(2.5)
        pk = Tex(r"Land: rent; hands: wages; stove: interest").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(pk))
        self.wait(2.5)
        pk2 = Tex(r"Owner: PROFIT — the leftovers, can be empty").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(pk2))
        self.play(Create(SurroundingRectangle(pk2, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): rubber bands, planks, the next plate ---
        self.next_band(9)
        b9_title = Tex("Rubber bands, planks and the next plate").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        rb = Tex(r"Cooldrink up R3: you switch — RUBBER BAND").scale(1.0).shift(band_shift(9) + UP * 1.2)
        pl = Tex(r"Bread up R3: you still buy — PLANK").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(rb))
        self.wait(2.5)
        self.play(Write(pl))
        self.wait(2.5)
        till = Tex(r"Raise a plank's price: till fills").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        till2 = Tex(r"Raise a rubber band's price: till empties").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(till))
        self.wait(2.5)
        self.play(Write(till2))
        self.wait(2.5)
        plate = Tex(r"Kota stand, R30 a plate: cook while the").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        plate2 = Tex(r"next plate costs less than R30 — MR $=$ MC").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(plate))
        self.play(Write(plate2))
        self.play(Create(SurroundingRectangle(plate2, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): the till slip and the two drivers ---
        self.next_band(10)
        b10_title = Tex("The till slip and the two drivers").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        add = Tex(r"One slip, three adding machines:").scale(1.0).shift(band_shift(10) + UP * 1.2)
        add2 = Tex(r"what was ADDED, EARNED, SPENT — one answer").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(add))
        self.wait(2)
        self.play(Write(add2))
        self.wait(2.5)
        dept = Tex(r"Ground, factory, counter — counter $\approx \tfrac{2}{3}$").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(dept))
        self.wait(2.5)
        d1 = Tex(r"Driver 1: SARB, repo pedal, 3--6\% target").scale(1.0).shift(band_shift(10) + DOWN * 1.4)
        d2 = Tex(r"Driver 2: Treasury, budget ship, spend + tax").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(d1))
        self.wait(2.5)
        self.play(Write(d2))
        self.wait(2)
        final = Tex(r"Fast pedal, slow ship — same economy").scale(1.05).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(final))
        self.play(Create(SurroundingRectangle(final, color=GREEN)))
        self.wait(4)
