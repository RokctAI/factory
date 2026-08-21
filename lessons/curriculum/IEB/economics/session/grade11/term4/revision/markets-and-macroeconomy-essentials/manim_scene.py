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

# Band-layout whiteboard scene for the revision session duo "Markets and
# Macroeconomy Essentials" (Grade 11, Term 4, IEB catalogue). Content lives
# in sequential one-frame-tall bands down a long canvas; the camera moves
# down and nothing is removed. Exporter-safe mobjects only; demand curves
# hand-built from Lines. Band time apportioned to subtopics.json
# (240/245/250/250/195/200/200 of 1580 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class MarketsAndMacroeconomyEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): three questions, three systems ---
        title = Tex("Economic Systems and the Four Factors").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        q1 = Tex("WHAT to produce? HOW? FOR WHOM?").scale(0.95).shift(UP * 1.5)
        self.play(Write(q1))
        self.play(Create(SurroundingRectangle(q1, color=GREEN)))
        self.wait(2)
        s1 = Tex("Free market: prices answer — efficient, unequal").scale(0.85).shift(UP * 0.5)
        s2 = Tex("Planned: officials answer — fair on paper,").scale(0.85).shift(DOWN * 0.4)
        s2b = Tex("blind without price signals").scale(0.85).shift(DOWN * 1.1)
        s3 = Tex("Mixed: markets + state — every real economy").scale(0.85).shift(DOWN * 2.0)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.play(Write(s2b))
        self.wait(2)
        self.play(Write(s3))
        self.wait(2)
        s4 = Tex("South Africa: mixed AND dualistic — two economies, one flag").scale(0.75).shift(DOWN * 2.9)
        self.play(Write(s4))
        self.wait(3)

        # --- Band 1 (subtopic_1): four factors and their rewards ---
        self.next_band(1)
        b1_title = Tex("Four factors, four rewards").scale(1.1).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        f1 = Tex(r"Natural resources $\to$ RENT").scale(0.9).shift(band_shift(1) + UP * 1.4)
        f2 = Tex(r"Labour $\to$ WAGES (human capital raises them)").scale(0.9).shift(band_shift(1) + UP * 0.55)
        f3 = Tex(r"Capital $\to$ INTEREST (machines, not money)").scale(0.9).shift(band_shift(1) + DOWN * 0.3)
        f4 = Tex(r"Entrepreneurship $\to$ PROFIT").scale(0.9).shift(band_shift(1) + DOWN * 1.15)
        for m in (f1, f2, f3, f4):
            self.play(Write(m))
            self.wait(1.8)
        f5 = Tex("Profit is the RESIDUAL: what remains after the").scale(0.85).shift(band_shift(1) + DOWN * 2.05)
        f5b = Tex("other three are paid — the price of risk").scale(0.85).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(f5))
        self.play(Write(f5b))
        self.play(Create(SurroundingRectangle(VGroup(f5, f5b), color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): three methods, one GDP ---
        self.next_band(2)
        b2_title = Tex("Three tape measures, one reading").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        m1 = Tex("Production: value added by every industry").scale(0.85).shift(band_shift(2) + UP * 1.4)
        m2 = Tex("Income: wages + rent + interest + profit").scale(0.85).shift(band_shift(2) + UP * 0.55)
        m3 = Tex(r"Expenditure: C + I + G + (X $-$ M)").scale(0.9).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(m1))
        self.wait(2)
        self.play(Write(m2))
        self.wait(2)
        self.play(Write(m3))
        self.play(Create(SurroundingRectangle(m3, color=GREEN)))
        self.wait(2.5)
        m4 = Tex("G = nurses' salaries, NOT grants;").scale(0.85).shift(band_shift(2) + DOWN * 1.2)
        m4b = Tex("I = fixed capital formation, tomorrow's capacity").scale(0.85).shift(band_shift(2) + DOWN * 1.95)
        self.play(Write(m4))
        self.play(Write(m4b))
        self.wait(2.5)
        m5 = Tex("GNI: GDP + residents' foreign earnings $-$ foreigners' local").scale(0.75).shift(band_shift(2) + DOWN * 2.85)
        self.play(Write(m5))
        self.wait(3)

        # --- Band 3 (subtopic_2): sectors and infrastructure ---
        self.next_band(3)
        b3_title = Tex("Sectors, chains and the skeleton").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        c1 = Tex("Primary draws; secondary transforms; tertiary serves").scale(0.85).shift(band_shift(3) + UP * 1.4)
        self.play(Write(c1))
        self.wait(2)
        c2 = Tex("The arc: primary shrinks, manufacturing drifts,").scale(0.85).shift(band_shift(3) + UP * 0.5)
        c2b = Tex("services near two-thirds of GDP").scale(0.85).shift(band_shift(3) + DOWN * 0.25)
        self.play(Write(c2))
        self.play(Write(c2b))
        self.wait(2.5)
        c3 = Tex(r"Chains: ore $\to$ steel $\to$ bridge — failure travels").scale(0.85).shift(band_shift(3) + DOWN * 1.15)
        self.play(Write(c3))
        self.wait(2)
        c4 = Tex("Infrastructure = engine and gate: load-shedding cut").scale(0.8).shift(band_shift(3) + DOWN * 2.05)
        c4b = Tex("production; missing services lock households out").scale(0.8).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(c4))
        self.play(Write(c4b))
        self.play(Create(SurroundingRectangle(VGroup(c4, c4b), color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): PED and the two curve shapes ---
        self.next_band(4)
        b4_title = Tex("Elasticity: the stretch test").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        e1 = Tex(r"PED = \%$\Delta$Q $\div$ \%$\Delta$P").scale(0.95).shift(band_shift(4) + UP * 1.4)
        self.play(Write(e1))
        self.play(Create(SurroundingRectangle(e1, color=GREEN)))
        self.wait(2.5)
        ax1 = Line(band_shift(4) + LEFT * 5.5 + DOWN * 2.4, band_shift(4) + LEFT * 5.5 + UP * 0.4)
        ax2 = Line(band_shift(4) + LEFT * 5.5 + DOWN * 2.4, band_shift(4) + LEFT * 0.5 + DOWN * 2.4)
        flat = Line(band_shift(4) + LEFT * 5.2 + DOWN * 0.4, band_shift(4) + LEFT * 0.9 + DOWN * 1.6, color=BLUE)
        self.play(Create(ax1), Create(ax2))
        self.play(Create(flat))
        e2 = Tex("Elastic: flatter — price nudges, quantity flees").scale(0.7).shift(band_shift(4) + LEFT * 3.0 + UP * 0.35)
        self.play(Write(e2))
        self.wait(2)
        ax3 = Line(band_shift(4) + RIGHT * 0.8 + DOWN * 2.4, band_shift(4) + RIGHT * 0.8 + UP * 0.4)
        ax4 = Line(band_shift(4) + RIGHT * 0.8 + DOWN * 2.4, band_shift(4) + RIGHT * 5.8 + DOWN * 2.4)
        steep = Line(band_shift(4) + RIGHT * 2.6 + UP * 0.3, band_shift(4) + RIGHT * 3.6 + DOWN * 2.2, color=RED)
        self.play(Create(ax3), Create(ax4))
        self.play(Create(steep))
        e3 = Tex("Inelastic: steeper — price climbs, quantity holds").scale(0.7).shift(band_shift(4) + RIGHT * 3.3 + UP * 0.35)
        self.play(Write(e3))
        self.wait(2)
        e4 = Tex("Determinants: substitutes, necessity, budget share, time").scale(0.75).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(e4))
        self.wait(3)

        # --- Band 5 (subtopic_3): revenue payoff, costs, MR = MC ---
        self.next_band(5)
        b5_title = Tex("Revenue, costs and the stopping rule").scale(1.1).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        r1 = Tex(r"Inelastic: price UP $\to$ revenue UP").scale(0.9).shift(band_shift(5) + UP * 1.4)
        r2 = Tex(r"Elastic: price UP $\to$ revenue DOWN (cut can fill the till)").scale(0.8).shift(band_shift(5) + UP * 0.55)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2.5)
        r3 = Tex("Fixed costs stand still; variable costs climb per unit").scale(0.8).shift(band_shift(5) + DOWN * 0.35)
        self.play(Write(r3))
        self.wait(2)
        r4 = Tex("Price taker: MR = price on every unit").scale(0.85).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(r4))
        self.wait(2)
        r5 = Tex("Expand while MR exceeds MC; stop where MR = MC").scale(0.9).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(r5))
        self.play(Create(SurroundingRectangle(r5, color=GREEN)))
        self.wait(2)
        r6 = Tex("Profit = total revenue $-$ total cost at that output").scale(0.8).shift(band_shift(5) + DOWN * 2.95)
        self.play(Write(r6))
        self.wait(3)

        # --- Band 6 (subtopic_4): connected markets ---
        self.next_band(6)
        b6_title = Tex("Markets that talk to each other").scale(1.1).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        k1 = Tex(r"Substitutes: butter price up $\to$ margarine demand").scale(0.8).shift(band_shift(6) + UP * 1.4)
        k1b = Tex("SHIFTS right").scale(0.85).shift(band_shift(6) + UP * 0.65)
        self.play(Write(k1))
        self.play(Write(k1b))
        self.wait(2.5)
        k2 = Tex(r"Complements: meat price up $\to$ charcoal demand eases left").scale(0.75).shift(band_shift(6) + DOWN * 0.2)
        self.play(Write(k2))
        self.wait(2)
        k3 = Tex("Derived demand: the welder is hired because").scale(0.8).shift(band_shift(6) + DOWN * 1.05)
        k3b = Tex("someone buys what welding builds").scale(0.8).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(k3))
        self.play(Write(k3b))
        self.play(Create(SurroundingRectangle(VGroup(k3, k3b), color=GREEN)))
        self.wait(2.5)
        k4 = Tex("Count the sellers: many / many-differentiated / few / one").scale(0.75).shift(band_shift(6) + DOWN * 2.75)
        self.play(Write(k4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the two policy steering wheels ---
        self.next_band(7)
        b7_title = Tex("Two steering wheels").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        w1 = Tex("Monetary: Reserve Bank, repo rate,").scale(0.85).shift(band_shift(7) + UP * 1.4)
        w1b = Tex(r"inflation target 3--6\%").scale(0.85).shift(band_shift(7) + UP * 0.65)
        self.play(Write(w1))
        self.play(Write(w1b))
        self.wait(2.5)
        w2 = Tex(r"Repo up $\to$ prime up $\to$ borrowing cools $\to$ inflation eases").scale(0.75).shift(band_shift(7) + DOWN * 0.2)
        self.play(Write(w2))
        self.wait(2)
        w3 = Tex("Fiscal: elected treasury, spending and taxation,").scale(0.8).shift(band_shift(7) + DOWN * 1.05)
        w3b = Tex("deficit borrowed, debt's interest bill crowds the budget").scale(0.75).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(w3))
        self.play(Write(w3b))
        self.wait(2.5)
        w4 = Tex("Compare: driver, lever, speed, target — then the mix").scale(0.8).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(w4))
        self.play(Create(SurroundingRectangle(w4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): three kitchens, four envelopes ---
        self.next_band(8)
        b8_title = Tex("Three kitchens, four envelopes").scale(1.1).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        n1 = Tex("Kitchen 1: the queue decides — quick, merciless").scale(0.85).shift(band_shift(8) + UP * 1.4)
        n2 = Tex("Kitchen 2: head office decides — soup floods, bread runs out").scale(0.75).shift(band_shift(8) + UP * 0.55)
        n3 = Tex("Kitchen 3: queue + inspector + soup pot = mixed").scale(0.8).shift(band_shift(8) + DOWN * 0.3)
        for m in (n1, n2, n3):
            self.play(Write(m))
            self.wait(1.9)
        n4 = Tex("SA: restaurant strip AND paraffin stove — dualistic").scale(0.8).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(n4))
        self.wait(2)
        n5 = Tex("Envelopes: rent, wages, interest — and profit,").scale(0.8).shift(band_shift(8) + DOWN * 2.1)
        n5b = Tex("the leftover that can be empty: the price of risk").scale(0.8).shift(band_shift(8) + DOWN * 2.85)
        self.play(Write(n5))
        self.play(Write(n5b))
        self.play(Create(SurroundingRectangle(n5b, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): rubber bands, planks, the next vetkoek ---
        self.next_band(9)
        b9_title = Tex("Rubber bands, planks, the next vetkoek").scale(1.05).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        v1 = Tex("Chips: rivals on the shelf — you bounce (elastic)").scale(0.85).shift(band_shift(9) + UP * 1.4)
        v2 = Tex("Taxi fare: no substitute — you pay (inelastic)").scale(0.85).shift(band_shift(9) + UP * 0.55)
        self.play(Write(v1))
        self.wait(2)
        self.play(Write(v2))
        self.wait(2)
        v3 = Tex("Plank price up: till swells. Rubber band up: till shrinks").scale(0.8).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(v3))
        self.play(Create(SurroundingRectangle(v3, color=GREEN)))
        self.wait(2.5)
        v4 = Tex("The stall: stand fee fixed; flour, oil, mince variable").scale(0.8).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(v4))
        self.wait(2)
        v5 = Tex("At R15 each: fry while the next one costs less than 15;").scale(0.8).shift(band_shift(9) + DOWN * 2.1)
        v5b = Tex("stop when it costs more — MR = MC in vetkoek").scale(0.8).shift(band_shift(9) + DOWN * 2.85)
        self.play(Write(v5))
        self.play(Write(v5b))
        self.wait(3)

        # --- Band 10 (subtopic_7): the till slip and the two drivers ---
        self.next_band(10)
        b10_title = Tex("The till slip and the two drivers").scale(1.1).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        t1 = Tex("Add the slip three ways — added, earned, spent —").scale(0.8).shift(band_shift(10) + UP * 1.4)
        t1b = Tex("final goods only, one total").scale(0.85).shift(band_shift(10) + UP * 0.65)
        self.play(Write(t1))
        self.play(Write(t1b))
        self.wait(2.5)
        t2 = Tex("Departments: earth, works, counter — counter near two-thirds").scale(0.7).shift(band_shift(10) + DOWN * 0.2)
        self.play(Write(t2))
        self.wait(2)
        t3 = Tex("Driver one: repo pedal, weeks, inflation 3 to 6").scale(0.8).shift(band_shift(10) + DOWN * 1.05)
        self.play(Write(t3))
        self.wait(2)
        t4 = Tex("Driver two: budget ship, yearly, spend and tax —").scale(0.8).shift(band_shift(10) + DOWN * 1.9)
        t4b = Tex("the borrowed gap grows an interest bill").scale(0.8).shift(band_shift(10) + DOWN * 2.65)
        self.play(Write(t4))
        self.play(Write(t4b))
        self.wait(2.5)
        t5 = Tex("Quick pedal, slow ship, one economy").scale(0.9).shift(band_shift(10) + DOWN * 3.5)
        self.play(Write(t5))
        self.play(Create(SurroundingRectangle(t5, color=GREEN)))
        self.wait(4)
