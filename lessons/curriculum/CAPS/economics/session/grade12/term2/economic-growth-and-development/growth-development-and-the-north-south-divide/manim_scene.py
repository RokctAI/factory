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
# (Expert 1-4: bands 0-7; Simplifier 5-7: bands 8-10), scene time
# apportioned to subtopics.json (235/235/240/265/195/200/210 of 1580 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GrowthDevelopmentNorthSouthSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md plays (~4-5%).
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): two different questions ---
        title = Tex("Growth, Development, North and South").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        g1 = Tex(r"GROWTH: annual \% change in REAL GDP").scale(1.05).shift(UP * 1.2)
        self.play(Write(g1))
        self.wait(2)
        g2 = Tex(r"Population grows $\approx$ 1,5\% a year:").scale(1.0).shift(UP * 0.3)
        g3 = Tex(r"growth below that $=$ poorer per person").scale(1.0).shift(DOWN * 0.5)
        self.play(Write(g2))
        self.play(Write(g3))
        self.play(Create(SurroundingRectangle(g3, color=GREEN)))
        self.wait(2.5)
        d1 = Tex(r"DEVELOPMENT: quality of life rising —").scale(1.0).shift(DOWN * 1.5)
        d2 = Tex(r"health, education, housing, security, choice").scale(0.95).shift(DOWN * 2.3)
        self.play(Write(d1))
        self.play(Write(d2))
        self.wait(3)

        # --- Band 1 (subtopic_1): HDI and the partings ---
        self.next_band(1)
        b1_title = Tex("The HDI, and when the two part company").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        h1 = Tex(r"HDI averages three dimensions:").scale(1.0).shift(band_shift(1) + UP * 1.2)
        h2 = Tex(r"long healthy life, knowledge, decent living").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(h1))
        self.play(Write(h2))
        self.play(Create(SurroundingRectangle(h2, color=GREEN)))
        self.wait(2.5)
        p1 = Tex(r"Growth WITHOUT development:").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        p2 = Tex(r"the resource-enclave pattern").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(p1))
        self.play(Write(p2))
        self.wait(2.5)
        p3 = Tex(r"Development without growth: Cuba's health;").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        p4 = Tex(r"SA's post-2004 HDI rise on grants, housing").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(p3))
        self.play(Write(p4))
        self.wait(3)

        # --- Band 2 (subtopic_2): demand-side instruments ---
        self.next_band(2)
        b2_title = Tex("Demand side: raise spending").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        i1 = Tex(r"Fiscal: infrastructure, public jobs, grants").scale(1.0).shift(band_shift(2) + UP * 1.2)
        i2 = Tex(r"— the poor's high MPC makes grants fuel").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(i1))
        self.play(Write(i2))
        self.wait(2.5)
        i3 = Tex(r"Monetary: lower rates, easier credit").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        i4 = Tex(r"Plus export demand via trade deals").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(i3))
        self.wait(2)
        self.play(Write(i4))
        self.wait(2)
        case = Tex(r"Case for: mass unemployment $=$ spare capacity,").scale(0.9).shift(band_shift(2) + DOWN * 2.1)
        case2 = Tex(r"so the multiplier delivers jobs, not prices").scale(0.9).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(case))
        self.play(Write(case2))
        self.wait(3)

        # --- Band 3 (subtopic_2): the four walls ---
        self.next_band(3)
        b3_title = Tex("The four South African walls").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        w1 = Tex(r"1. INFLATION: supply-bound spending lifts prices").scale(0.9).shift(band_shift(3) + UP * 1.2)
        w2 = Tex(r"2. IMPORTS: high MPM $\Rightarrow$ small multiplier").scale(0.95).shift(band_shift(3) + UP * 0.4)
        w3 = Tex(r"3. DEBT: service costs crowd social spending").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        w4 = Tex(r"4. STRUCTURE: demand trains no electrician").scale(0.95).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(w1))
        self.wait(2)
        self.play(Write(w2))
        self.wait(2)
        self.play(Write(w3))
        self.wait(2)
        self.play(Write(w4))
        self.wait(2)
        sm = Tex(r"Demand buys relief, not transformation").scale(1.0).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(sm))
        self.play(Create(SurroundingRectangle(sm, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): supply side shifts the PPC ---
        self.next_band(4)
        b4_title = Tex("Supply side: build capacity").scale(1.2).shift(band_shift(4) + UP * 2.9)
        self.play(Write(b4_title))
        self.wait(1.5)
        # Small PPC diagram, lower left
        o = band_shift(4) + DOWN * 2.9 + LEFT * 5.6
        y_ax = Arrow(o, o + UP * 4.0, buff=0, stroke_width=3)
        x_ax = Arrow(o, o + RIGHT * 4.6, buff=0, stroke_width=3)
        self.play(Create(y_ax), Create(x_ax))
        ppc1 = VGroup(Line(o + UP * 3.0, o + RIGHT * 1.8 + UP * 2.4, color=BLUE),
                      Line(o + RIGHT * 1.8 + UP * 2.4, o + RIGHT * 3.0, color=BLUE))
        ppc1_lab = Tex("PPC", color=BLUE).scale(0.75).shift(o + RIGHT * 3.0 + DOWN * 0.4)
        self.play(Create(ppc1), Write(ppc1_lab))
        self.wait(1.5)
        ppc2 = VGroup(Line(o + UP * 3.7, o + RIGHT * 2.3 + UP * 3.0, color=GREEN),
                      Line(o + RIGHT * 2.3 + UP * 3.0, o + RIGHT * 3.9, color=GREEN))
        ppc2_lab = MathTex(r"PPC_2", color=GREEN).scale(0.75).shift(o + RIGHT * 3.9 + DOWN * 0.4)
        outw = Arrow(o + RIGHT * 1.6 + UP * 1.7, o + RIGHT * 2.4 + UP * 2.3, buff=0, color=YELLOW)
        self.play(Create(ppc2), Write(ppc2_lab), Create(outw))
        self.wait(2)
        s1 = Tex(r"Costs: power, ports, less red tape").scale(0.9).shift(band_shift(4) + UP * 1.7 + RIGHT * 2.9)
        s2 = Tex(r"Human capital: schools, TVET, health").scale(0.9).shift(band_shift(4) + UP * 0.9 + RIGHT * 2.9)
        s3 = Tex(r"Capital and technology: R\&D, incentives").scale(0.9).shift(band_shift(4) + UP * 0.1 + RIGHT * 2.9)
        s4 = Tex(r"Efficient markets: competition, finance").scale(0.9).shift(band_shift(4) + DOWN * 0.7 + RIGHT * 2.9)
        s5 = Tex(r"Incentives: tax structure, policy certainty").scale(0.9).shift(band_shift(4) + DOWN * 1.5 + RIGHT * 2.9)
        self.play(Write(s1))
        self.wait(1.5)
        self.play(Write(s2))
        self.wait(1.5)
        self.play(Write(s3))
        self.wait(1.5)
        self.play(Write(s4))
        self.wait(1.5)
        self.play(Write(s5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): evaluation and sequencing ---
        self.next_band(5)
        b5_title = Tex("Evaluate the two approaches").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        e1 = Tex(r"For: only capacity growth is durable —").scale(1.0).shift(band_shift(5) + UP * 1.2)
        e2 = Tex(r"it raises the trend line itself").scale(1.0).shift(band_shift(5) + UP * 0.5)
        self.play(Write(e1))
        self.play(Write(e2))
        self.wait(2.5)
        e3 = Tex(r"Against: SLOW, regressive in the short run,").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        e4 = Tex(r"and it depends on state capacity").scale(0.95).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(e3))
        self.play(Write(e4))
        self.wait(2.5)
        wrong = Tex(r"Choose one side").scale(1.0).shift(band_shift(5) + DOWN * 2.0 + LEFT * 3.4)
        self.play(Write(wrong))
        self.play(Create(strike(wrong)))
        seq = Tex(r"Sequencing: demand holds the present,").scale(0.95).shift(band_shift(5) + DOWN * 2.0 + RIGHT * 2.6)
        seq2 = Tex(r"supply decides the future — do both in proportion").scale(0.9).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(seq))
        self.play(Write(seq2))
        self.play(Create(SurroundingRectangle(seq2, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): South Africa's endeavours ---
        self.next_band(6)
        b6_title = Tex("South Africa's four plans").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        r1 = Tex(r"RDP 1994: basic needs — demand in spirit").scale(0.95).shift(band_shift(6) + UP * 1.2)
        r2 = Tex(r"GEAR 1996: discipline, deficit cut — supply swing").scale(0.9).shift(band_shift(6) + UP * 0.4)
        r3 = Tex(r"ASGISA 2006: binding constraints named").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        r4 = Tex(r"NDP 2012: aim 2030 — poverty, inequality").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2)
        self.play(Write(r3))
        self.wait(2)
        self.play(Write(r4))
        self.wait(2)
        v1 = Tex(r"Verdict: stability + social wage achieved;").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        v2 = Tex(r"the plans diagnosed; delivery lagged").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(v1))
        self.play(Write(v2))
        self.play(Create(SurroundingRectangle(v2, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the north-south divide ---
        self.next_band(7)
        b7_title = Tex("The north-south divide").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        n1 = Tex(r"North: manufactures, capital, rule-setting").scale(0.95).shift(band_shift(7) + UP * 1.2)
        n2 = Tex(r"South: commodities, debt, aid with conditions").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(n1))
        self.wait(2)
        self.play(Write(n2))
        self.wait(2)
        m1 = Tex(r"Gap-keepers: terms of trade, debt service,").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        m2 = Tex(r"tariffs on processed goods, brain drain").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(m1))
        self.play(Write(m2))
        self.play(Create(SurroundingRectangle(m2, color=GREEN)))
        self.wait(2.5)
        c1 = Tex(r"Counter-moves: China, India, Brazil; BRICS;").scale(0.9).shift(band_shift(7) + DOWN * 2.1)
        c2 = Tex(r"AfCFTA; remittances running north to south").scale(0.9).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(c1))
        self.play(Write(c2))
        self.wait(2)
        c3 = Tex(r"SA sits astride the line — the dual anchor").scale(0.95).shift(band_shift(7) + DOWN * 3.4)
        self.play(Write(c3))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the payslip and the report card ---
        self.next_band(8)
        b8_title = Tex("The payslip and the report card").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        f1 = Tex(r"Family 1: income up, life not — money up").scale(0.95).shift(band_shift(8) + UP * 1.2)
        f2 = Tex(r"Family 2: income flat, lives moving").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(f1))
        self.wait(2.5)
        self.play(Write(f2))
        self.wait(2.5)
        f3 = Tex(r"Growth $=$ the payslip: strip inflation,").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        f4 = Tex(r"then divide by the mouths").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(f3))
        self.play(Write(f4))
        self.play(Create(SurroundingRectangle(f4, color=GREEN)))
        self.wait(2.5)
        f5 = Tex(r"Development $=$ the report card: the HDI —").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        f6 = Tex(r"live long, learn, afford a decent life").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(f5))
        self.play(Write(f6))
        self.wait(2.5)
        f7 = Tex(r"SA: middling payslip, better report card").scale(0.95).shift(band_shift(8) + DOWN * 3.4)
        self.play(Write(f7))
        self.wait(3)

        # --- Band 9 (subtopic_6): feed the fire or build the stove ---
        self.next_band(9)
        b9_title = Tex("Feed the fire or build the stove").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        fire = Tex(r"Fire: money in pockets, spent and respent").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(fire))
        self.wait(2.5)
        lim = Tex(r"Four limits: full pots lift prices; far-away").scale(0.95).shift(band_shift(9) + UP * 0.4)
        lim2 = Tex(r"shops; the lender at the door; no wired stove").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(lim))
        self.play(Write(lim2))
        self.wait(2.5)
        stove = Tex(r"Stove: wire the house, fix the van,").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        stove2 = Tex(r"school to matric — slow, but cooks forever").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(stove))
        self.play(Write(stove2))
        self.wait(2.5)
        prop = Tex(r"Feed the fire through the present;").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        prop2 = Tex(r"never stop building the stove").scale(0.95).shift(band_shift(9) + DOWN * 3.4)
        self.play(Write(prop))
        self.play(Write(prop2))
        self.play(Create(SurroundingRectangle(prop2, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): the street and the suburb ---
        self.next_band(10)
        b10_title = Tex("The street and the suburb").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        st1 = Tex(r"Suburb inherits working systems; the street").scale(0.95).shift(band_shift(10) + UP * 1.2)
        st2 = Tex(r"supplies fruit, ore — and its cleverest children").scale(0.9).shift(band_shift(10) + UP * 0.4)
        self.play(Write(st1))
        self.play(Write(st2))
        self.wait(2.5)
        st3 = Tex(r"Raw goods enter free; manufactures pay").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        st4 = Tex(r"at the gate — the gap keeps itself open").scale(0.95).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(st3))
        self.play(Write(st4))
        self.wait(2.5)
        st5 = Tex(r"Redrawn map: east Asia's stoves, AfCFTA,").scale(0.9).shift(band_shift(10) + DOWN * 1.9)
        st6 = Tex(r"remittances outweighing aid").scale(0.95).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(st5))
        self.play(Write(st6))
        self.wait(2.5)
        fin = Tex(r"Growth to afford the future; development").scale(0.9).shift(band_shift(10) + DOWN * 3.1)
        fin2 = Tex(r"so everyone arrives there").scale(0.95).shift(band_shift(10) + DOWN * 3.7)
        self.play(Write(fin))
        self.play(Write(fin2))
        self.play(Create(SurroundingRectangle(fin2, color=GREEN)))
        self.wait(4)
