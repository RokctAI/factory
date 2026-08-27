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
# apportioned to subtopics.json (225/245/250/230/195/195/195 of 1535 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PublicSectorAndLafferCurveSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md plays (~4-5%).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): composition ---
        title = Tex("The Public Sector and the Laffer Curve").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        c1 = Tex(r"NATIONAL: policy, education, health, police").scale(0.95).shift(UP * 1.2)
        c2 = Tex(r"PROVINCIAL: schools and hospitals").scale(0.95).shift(UP * 0.4)
        c3 = Tex(r"LOCAL: water, power lines, refuse, streets").scale(0.95).shift(DOWN * 0.4)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2)
        soe = Tex(r"Outer ring: Eskom, Transnet, SABC, Post Office").scale(0.9).shift(DOWN * 1.4)
        self.play(Write(soe))
        self.play(Create(SurroundingRectangle(soe, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): necessity — failures and roles ---
        self.next_band(1)
        b1_title = Tex("Market failures, matched to state roles").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        p1 = Tex(r"Public goods (non-rival, non-excludable)").scale(0.95).shift(band_shift(1) + UP * 1.2)
        p2 = Tex(r"$\rightarrow$ free-rider $\rightarrow$ state provides").scale(0.95).shift(band_shift(1) + UP * 0.5)
        self.play(Write(p1))
        self.play(Write(p2))
        self.wait(2)
        p3 = Tex(r"Externalities $\rightarrow$ tax harms, fund merit goods").scale(0.9).shift(band_shift(1) + DOWN * 0.3)
        self.play(Write(p3))
        self.wait(2)
        p4 = Tex(r"Monopoly $\rightarrow$ regulate competition").scale(0.95).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(p4))
        self.wait(2)
        p5 = Tex(r"Need-blind incomes $\rightarrow$ redistribute:").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        p6 = Tex(r"progressive tax + grants").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(p5))
        self.play(Write(p6))
        self.play(Create(SurroundingRectangle(p6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): five provisioning problems ---
        self.next_band(2)
        b2_title = Tex("Five reasons providing is hard").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        f1 = Tex(r"1. Accountability: pay-service wire cut").scale(0.95).shift(band_shift(2) + UP * 1.2)
        f2 = Tex(r"2. Efficiency: no profit test, no penalty").scale(0.95).shift(band_shift(2) + UP * 0.4)
        f3 = Tex(r"3. Needs: guessed, not priced").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        f4 = Tex(r"4. Pricing: free floods, full-cost excludes").scale(0.95).shift(band_shift(2) + DOWN * 1.2)
        f5 = Tex(r"5. Parastatals: commercial + social at once").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(f1))
        self.wait(2)
        self.play(Write(f2))
        self.wait(2)
        self.play(Write(f3))
        self.wait(2)
        self.play(Write(f4))
        self.wait(2)
        self.play(Write(f5))
        self.play(Create(SurroundingRectangle(f5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the five objectives ---
        self.next_band(3)
        b3_title = Tex("The five-line scoreboard").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        o1 = Tex(r"Economic growth — real GDP rising").scale(0.95).shift(band_shift(3) + UP * 1.2)
        o2 = Tex(r"Full employment").scale(0.95).shift(band_shift(3) + UP * 0.4)
        o3 = Tex(r"Price stability — 3--6\% target").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        o4 = Tex(r"Exchange-rate stability").scale(0.95).shift(band_shift(3) + DOWN * 1.2)
        o5 = Tex(r"Economic equity — narrowing the gap").scale(0.95).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(o1))
        self.wait(1.5)
        self.play(Write(o2))
        self.wait(1.5)
        self.play(Write(o3))
        self.wait(1.5)
        self.play(Write(o4))
        self.wait(1.5)
        self.play(Write(o5))
        self.play(Create(SurroundingRectangle(o5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the budget ---
        self.next_band(4)
        b4_title = Tex("February's plan: in and out").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        r1 = Tex(r"IN: income tax (largest), VAT 15\%,").scale(0.95).shift(band_shift(4) + UP * 1.2)
        r2 = Tex(r"company tax, excise, customs").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(r1))
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex(r"Direct on income; indirect on spending").scale(0.95).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(r3))
        self.wait(2)
        r4 = Tex(r"OUT: grants, education, health, police —").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        r5 = Tex(r"and debt service, the fastest grower").scale(0.95).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(r4))
        self.play(Write(r5))
        self.wait(2)
        r6 = Tex(r"Deficit $=$ spend $>$ revenue $\rightarrow$ bonds $\rightarrow$ debt").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(r6))
        self.play(Create(SurroundingRectangle(r6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the Laffer curve ---
        self.next_band(5)
        b5_title = Tex("The Laffer curve").scale(1.2).shift(band_shift(5) + UP * 2.9)
        self.play(Write(b5_title))
        self.wait(1.5)
        o = band_shift(5) + DOWN * 2.9 + LEFT * 5.4
        y_ax = Arrow(o, o + UP * 4.8, buff=0, stroke_width=3)
        x_ax = Arrow(o, o + RIGHT * 10.4, buff=0, stroke_width=3)
        y_lab = Tex("revenue").scale(0.75).shift(o + UP * 4.8 + RIGHT * 1.1)
        x_lab = Tex("tax rate: 0 to 100\\%").scale(0.7).shift(o + RIGHT * 9.6 + DOWN * 0.35)
        self.play(Create(y_ax), Create(x_ax))
        self.play(Write(y_lab), Write(x_lab))
        self.wait(1.5)
        # Hump as a chain of Lines: rise to crest, fall back to zero
        h0 = o + RIGHT * 0.4
        h1 = o + RIGHT * 2.2 + UP * 2.4
        h2 = o + RIGHT * 4.6 + UP * 3.8
        h3 = o + RIGHT * 7.0 + UP * 2.4
        h4 = o + RIGHT * 9.0
        hump = VGroup(Line(h0, h1, color=BLUE), Line(h1, h2, color=BLUE),
                      Line(h2, h3, color=BLUE), Line(h3, h4, color=BLUE))
        self.play(Create(hump), run_time=2.5)
        self.wait(1.5)
        z1 = Dot(h0, color=YELLOW)
        z2 = Dot(h4, color=YELLOW)
        zl = Tex("zero at BOTH ends").scale(0.8).shift(o + RIGHT * 8.6 + UP * 1.0)
        self.play(Create(z1), Create(z2), Write(zl))
        self.wait(2)
        crest = Dot(h2, color=RED)
        crest_lab = Tex("the crest: optimum rate", color=RED).scale(0.8).shift(h2 + UP * 0.5)
        self.play(Create(crest), Write(crest_lab))
        self.wait(2)
        read1 = Tex(r"Rising slope: higher rate, more revenue").scale(0.8).shift(o + RIGHT * 2.6 + UP * 4.4)
        read2 = Tex(r"Far slope: higher rate, LESS revenue").scale(0.8).shift(o + RIGHT * 8.0 + UP * 3.6)
        self.play(Write(read1))
        self.wait(1.5)
        self.play(Write(read2))
        self.wait(2)
        cav = Tex(r"Nobody knows where the crest sits").scale(0.85).shift(o + RIGHT * 4.8 + DOWN * 0.4)
        self.play(Write(cav))
        self.play(Create(SurroundingRectangle(cav, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): public sector failure ---
        self.next_band(6)
        b6_title = Tex("When the state itself fails").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        g1 = Tex(r"Causes: skills gaps, apathy, bureaucracy,").scale(0.95).shift(band_shift(6) + UP * 1.2)
        g2 = Tex(r"politics over economics, corruption").scale(0.95).shift(band_shift(6) + UP * 0.5)
        self.play(Write(g1))
        self.play(Write(g2))
        self.wait(2)
        g3 = Tex(r"Effects: misallocation; the poor stranded").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        g4 = Tex(r"while the wealthy buy substitutes;").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        g5 = Tex(r"tax morality and investment erode").scale(0.95).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(g3))
        self.wait(2)
        self.play(Write(g4))
        self.play(Write(g5))
        self.wait(2)
        bal = Tex(r"Markets fail: state exists. States fail: watch it").scale(0.9).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(bal))
        self.play(Create(SurroundingRectangle(bal, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): what the street cannot buy ---
        self.next_band(7)
        b7_title = Tex("What the street cannot buy for itself").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        s1 = Tex(r"Vetkoek, data, haircut: pay and it's yours").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(s1))
        self.wait(2.5)
        s2 = Tex(r"The night patrol: safe for ALL, or for none").scale(0.95).shift(band_shift(7) + UP * 0.4)
        s3 = Tex(r"Everyone waits for everyone — FREE-RIDER").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(s2))
        self.wait(2.5)
        self.play(Write(s3))
        self.play(Create(SurroundingRectangle(s3, color=GREEN)))
        self.wait(2.5)
        s4 = Tex(r"Middle shelf: clinic and school —").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        s5 = Tex(r"benefits overflow the buyer: merit goods").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(s4))
        self.play(Write(s5))
        self.wait(2.5)
        s6 = Tex(r"The grant: need corrected, not a purchase").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(s6))
        self.wait(3)

        # --- Band 8 (subtopic_6): why the tap runs slow ---
        self.next_band(8)
        b8_title = Tex("Why the tap runs slow").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        t1 = Tex(r"Chicken shop: daily election by customers").scale(0.95).shift(band_shift(8) + UP * 1.2)
        t2 = Tex(r"Housing office: no ballot, budget regardless").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(t1))
        self.wait(2.5)
        self.play(Write(t2))
        self.wait(2.5)
        t3 = Tex(r"Needs are guessed: censuses, not prices").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(t3))
        self.wait(2)
        t4 = Tex(r"Stepped tariff: free basics, dear luxury").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(t4))
        self.play(Create(SurroundingRectangle(t4, color=GREEN)))
        self.wait(2.5)
        t5 = Tex(r"Parastatal: serve villages, bleed money;").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        t6 = Tex(r"serve money, villages go dark").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(t5))
        self.play(Write(t6))
        self.wait(3)

        # --- Band 9 (subtopic_7): February's envelope, the hump ---
        self.next_band(9)
        b9_title = Tex("February's envelope, and the crest").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        e1 = Tex(r"IN: payslips, till slips, profits, duties").scale(0.95).shift(band_shift(9) + UP * 1.2)
        e2 = Tex(r"OUT: grants, schools, clinics, police,").scale(0.95).shift(band_shift(9) + UP * 0.4)
        e3 = Tex(r"and INTEREST — watch that line").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(e1))
        self.wait(2)
        self.play(Write(e2))
        self.play(Write(e3))
        self.wait(2.5)
        e4 = Tex(r"Barber taxed at 0\%: nothing. At 100\%: nothing").scale(0.9).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(e4))
        self.wait(2)
        e5 = Tex(r"Between: a crest — past it, squeezing collects less").scale(0.85).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(e5))
        self.play(Create(SurroundingRectangle(e5, color=GREEN)))
        self.wait(2.5)
        e6 = Tex(r"Markets fail; states fail; watch both").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(e6))
        self.wait(4)
