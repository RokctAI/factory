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

# Band-layout whiteboard scene for the session duo "Growth, Inequality and
# Redistribution" (Grade 11, Term 3). One band per teaching step; the camera
# moves down and nothing is removed. Exporter-safe mobjects only; the Lorenz
# curve is hand-built from Lines inside a Rectangle frame. Band time
# apportioned to subtopics.json (235/255/245/255/195/205/200 of 1590 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GrowthInequalityRedistributionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the two corrections ---
        title = Tex("Growth, Inequality and Redistribution").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        g1 = Tex(r"Growth: \% change in REAL GDP, year on year").scale(1.05).shift(UP * 1.1)
        self.play(Write(g1))
        self.wait(2)
        g2 = Tex(r"Correction 1 — real: nominal up 7\% at 6\% inflation").scale(0.95).shift(UP * 0.2)
        g2b = Tex(r"$=$ roughly 1\% of genuine extra output").scale(0.95).shift(DOWN * 0.6)
        self.play(Write(g2))
        self.wait(2)
        self.play(Write(g2b))
        self.wait(2.5)
        g3 = MathTex(r"\text{Correction 2: per capita} = \text{real output} \div \text{population}").scale(0.9).shift(DOWN * 1.6)
        self.play(Write(g3))
        self.wait(2)
        g4 = Tex("Average lives improve only when output outruns the people").scale(0.85).shift(DOWN * 2.6)
        self.play(Write(g4))
        self.play(Create(SurroundingRectangle(g4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): South Africa's decade ---
        self.next_band(1)
        b1_title = Tex("The decade that defines the debate").scale(1.1).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        r1 = Tex(r"Real GDP growth: about 1\% a year").scale(1.05).shift(band_shift(1) + UP * 1.3)
        r2 = Tex(r"Population growth: about 1{,}5\% a year").scale(1.05).shift(band_shift(1) + UP * 0.4)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex("Output grew; output per person fell — slowly poorer").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(r3))
        self.play(Create(SurroundingRectangle(r3, color=GREEN)))
        self.wait(2.5)
        r4 = Tex(r"Compounding: 1\% doubles in $\approx$70 years,").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        r5 = Tex(r"5\% in $\approx$14 — the whole case for growth targets").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(r4))
        self.play(Write(r5))
        self.wait(2.5)
        r6 = Tex("Growth funds jobs, incomes and the whole tax base").scale(0.9).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(r6))
        self.wait(3)

        # --- Band 2 (subtopic_2): the Lorenz curve, constructed ---
        self.next_band(2)
        b2_title = Tex("The Lorenz curve").scale(1.2).shift(band_shift(2) + UP * 2.9)
        self.play(Write(b2_title))
        self.wait(1.5)
        org = band_shift(2) + LEFT * 4.6 + DOWN * 2.6
        # Square frame: cumulative population along the bottom, income up.
        frame_sq = Rectangle(width=4.8, height=4.8).move_to(org + RIGHT * 2.4 + UP * 2.4)
        xlab = Tex(r"cumulative \% of people").scale(0.65).move_to(org + RIGHT * 2.4 + DOWN * 0.4)
        ylab = Tex(r"cumulative \% of income").scale(0.6).move_to(org + LEFT * 1.0 + UP * 2.4)
        self.play(Create(frame_sq), Write(xlab), Write(ylab))
        self.wait(1.5)
        diag = Line(org, org + RIGHT * 4.8 + UP * 4.8, stroke_width=4, color=BLUE)
        diag_lab = Tex("line of perfect equality").scale(0.6).move_to(org + RIGHT * 1.5 + UP * 2.8)
        self.play(Create(diag), Write(diag_lab))
        self.wait(2)
        lz1 = Line(org, org + RIGHT * 2.88 + UP * 0.48, stroke_width=5)
        lz2 = Line(org + RIGHT * 2.88 + UP * 0.48, org + RIGHT * 4.1 + UP * 1.7, stroke_width=5)
        lz3 = Line(org + RIGHT * 4.1 + UP * 1.7, org + RIGHT * 4.8 + UP * 4.8, stroke_width=5)
        lz_lab = Tex("actual sharing").scale(0.65).move_to(org + RIGHT * 4.0 + UP * 0.6)
        self.play(Create(lz1))
        self.play(Create(lz2))
        self.play(Create(lz3), Write(lz_lab))
        self.wait(2)
        pt = Dot(org + RIGHT * 2.88 + UP * 0.48)
        pt_lab = Tex(r"SA: poorest 60\% hold $\approx$10\% of income").scale(0.7).move_to(band_shift(2) + RIGHT * 3.6 + DOWN * 0.9)
        self.play(Create(pt), Write(pt_lab))
        self.wait(2.5)
        sag = Tex("The deeper the droop, the worse the inequality").scale(0.8).move_to(band_shift(2) + RIGHT * 3.6 + DOWN * 1.8)
        self.play(Write(sag))
        self.play(Create(SurroundingRectangle(sag, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the Gini; income vs wealth ---
        self.next_band(3)
        b3_title = Tex("The Gini: the droop as one number").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        n1 = MathTex(r"\text{Gini} = \frac{\text{area between diagonal and curve}}{\text{area under diagonal}}").scale(0.9).shift(band_shift(3) + UP * 1.2)
        self.play(Write(n1))
        self.wait(2.5)
        n2 = Tex(r"Perfect equality: 0. \; One person holds all: 1.").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(n2))
        self.wait(2)
        n3 = Tex(r"Nordics $\approx 0{,}25$--$0{,}3$; \; South Africa $\approx 0{,}63$").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(n3))
        self.play(Create(SurroundingRectangle(n3, color=GREEN)))
        self.wait(2.5)
        n4 = Tex("Income is a flow; wealth is a stock, built over generations").scale(0.85).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(n4))
        self.wait(2)
        n5 = Tex(r"Top 10\% hold over 80\% of wealth — history as a stock").scale(0.85).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(n5))
        self.wait(3)

        # --- Band 4 (subtopic_3): tax and grants ---
        self.next_band(4)
        b4_title = Tex("Redistribution: methods 1 and 2").scale(1.15).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        m1 = Tex("Progressive: a bigger PERCENTAGE from higher earners").scale(0.9).shift(band_shift(4) + UP * 1.3)
        m2 = Tex(r"SA staircase: 18\% up to 45\% on the top slice").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(m1))
        self.wait(2)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex("VAT bites the poor hardest — staples zero-rated").scale(0.9).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(m3))
        self.wait(2.5)
        m4 = Tex(r"Grants: $\approx$28 million people paid monthly").scale(0.95).shift(band_shift(4) + DOWN * 1.4)
        m5 = Tex(r"Older persons R2\,000$+$; child support R500$+$").scale(0.95).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(m4))
        self.wait(2)
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex("The fastest route to the poorest households").scale(0.9).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(m6))
        self.wait(3)

        # --- Band 5 (subtopic_3): in kind, assets, and the tension ---
        self.next_band(5)
        b5_title = Tex("Methods 3 and 4 — then the tension").scale(1.15).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        v1 = Tex("In kind: free basic water and electricity, no-fee").scale(0.95).shift(band_shift(5) + UP * 1.3)
        v1b = Tex("schools, feeding schemes, clinics, state housing").scale(0.95).shift(band_shift(5) + UP * 0.5)
        self.play(Write(v1))
        self.play(Write(v1b))
        self.wait(2.5)
        v2 = Tex("Labour and assets: minimum wage, empowerment,").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        v2b = Tex("land reform, skills — tomorrow's earning power").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(v2))
        self.play(Write(v2b))
        self.wait(2.5)
        v3 = Tex("Growth and redistribution: complements, not substitutes").scale(0.9).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(v3))
        self.play(Create(SurroundingRectangle(v3, color=GREEN)))
        self.wait(2)
        v4 = Tex("Growth pays for sharing; sharing builds skills and demand").scale(0.85).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(v4))
        self.wait(3)

        # --- Band 6 (subtopic_4): growth sources vs SA padlocks ---
        self.next_band(6)
        b6_title = Tex("Where growth comes from — and our padlocks").scale(1.0).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        w1 = Tex("Sources: capital from savings; capable labour;").scale(0.9).shift(band_shift(6) + UP * 1.4)
        w2 = Tex("better technology; trade; a climate worth the risk").scale(0.9).shift(band_shift(6) + UP * 0.6)
        self.play(Write(w1))
        self.play(Write(w2))
        self.wait(2.5)
        w3 = Tex("Padlock: load shedding, freight rail below capacity").scale(0.9).shift(band_shift(6) + DOWN * 0.3)
        w4 = Tex(r"Padlock: skills mismatch — vacancies beside 30\%$+$ jobless").scale(0.85).shift(band_shift(6) + DOWN * 1.1)
        w5 = Tex("Padlock: thin savings; uncertainty scares foreign capital").scale(0.85).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(w3))
        self.wait(2)
        self.play(Write(w4))
        self.wait(2)
        self.play(Write(w5))
        self.wait(2)
        w6 = Tex("Each constraint is a growth method with a padlock on it").scale(0.9).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(w6))
        self.play(Create(SurroundingRectangle(w6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): standard of living and the HDI ---
        self.next_band(7)
        b7_title = Tex("Standard of living: what GDP cannot see").scale(1.05).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        s1 = Tex("Silent on distribution — averages hide the queue").scale(0.95).shift(band_shift(7) + UP * 1.3)
        s2 = Tex("Omits unpaid and informal work").scale(0.95).shift(band_shift(7) + UP * 0.4)
        s3 = Tex("Pollution counted as gain, damage as nothing").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        s4 = Tex("Money measured; health and learning ignored").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        for m in (s1, s2, s3, s4):
            self.play(Write(m))
            self.wait(1.8)
        s5 = Tex("HDI: income $+$ life expectancy $+$ education").scale(0.95).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(s5))
        self.play(Create(SurroundingRectangle(s5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the potjie and the two tricks ---
        self.next_band(8)
        b8_title = Tex("The potjie at the braai").scale(1.2).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        p1 = Tex("Growth: MORE FOOD in this year's pot").scale(1.0).shift(band_shift(8) + UP * 1.3)
        self.play(Write(p1))
        self.wait(2)
        p2 = Tex(r"Price trick: same food, higher price tags — ``growth''").scale(0.85).shift(band_shift(8) + UP * 0.4)
        self.play(Write(p2))
        self.play(Create(strike(p2)))
        self.wait(1.5)
        p3 = Tex(r"Real growth: value the pot at last year's prices").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(p3))
        self.wait(2)
        p4 = Tex(r"Headcount trick: pot up 2\%, crowd up 3\% — smaller plates").scale(0.85).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(p4))
        self.wait(2)
        p5 = Tex(r"SA: pot $\approx 1\%$, crowd $\approx 1{,}5\%$ — plates shrinking").scale(0.85).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(p5))
        self.play(Create(SurroundingRectangle(p5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): walking the queue ---
        self.next_band(9)
        b9_title = Tex("Walking the queue: 100 people, 100 coins").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        q1 = Tex("Equal sharing: one coin per step, all the way").scale(0.95).shift(band_shift(9) + UP * 1.3)
        self.play(Write(q1))
        self.wait(2)
        q2 = Tex("Real walk: 20 people passed — 2 or 3 coins counted").scale(0.95).shift(band_shift(9) + UP * 0.4)
        q3 = Tex("Person 60 — the count has crawled to about 10").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        q4 = Tex("Final 10 people — roughly 65 coins between them").scale(0.95).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(q2))
        self.wait(2)
        self.play(Write(q3))
        self.wait(2)
        self.play(Write(q4))
        self.wait(2)
        q5 = Tex(r"Crawl then avalanche $=$ the Lorenz droop: Gini $\approx 0{,}63$").scale(0.85).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(q5))
        self.play(Create(SurroundingRectangle(q5, color=GREEN)))
        self.wait(2)
        q6 = Tex("The wealth queue is worse: stocks store history").scale(0.85).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(q6))
        self.wait(3)

        # --- Band 10 (subtopic_7): the four moves and the tension ---
        self.next_band(10)
        b10_title = Tex("Four ways to move the coins").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        u1 = Tex(r"1. Staircase tax: up to 45c in the rand; staples VAT-free").scale(0.8).shift(band_shift(10) + UP * 1.4)
        u2 = Tex(r"2. Coins into empty pockets: grants to $\approx$28 million").scale(0.8).shift(band_shift(10) + UP * 0.6)
        u3 = Tex("3. Things, not coins: free water, no-fee schools, clinics").scale(0.8).shift(band_shift(10) + DOWN * 0.2)
        u4 = Tex("4. Tomorrow's coins: minimum wage, land, above all skills").scale(0.8).shift(band_shift(10) + DOWN * 1.0)
        for m in (u1, u2, u3, u4):
            self.play(Write(m))
            self.wait(1.8)
        u5 = Tex("Tax the cooks too hard and the cooking stops;").scale(0.85).shift(band_shift(10) + DOWN * 1.8)
        u6 = Tex("starve the queue and the pot stops growing").scale(0.85).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(u5))
        self.play(Write(u6))
        self.wait(2)
        u7 = Tex("Each feeds the other — keep both moving at once").scale(0.9).shift(band_shift(10) + DOWN * 3.05)
        self.play(Write(u7))
        self.play(Create(SurroundingRectangle(u7, color=GREEN)))
        self.wait(4)
