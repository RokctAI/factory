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

# Band-layout whiteboard scene for the session duo "Economic Development and
# Developing Countries" (Grade 11, Term 3). One band per teaching step; the
# camera moves down and nothing is removed. Exporter-safe mobjects only; the
# HDI blocks and the plans timeline are hand-built from Rectangles, Lines,
# Dots and Tex. Band time apportioned to subtopics.json
# (235/255/250/245/200/205/210 of 1600 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EconomicDevelopmentSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): growth vs development ---
        title = Tex("Economic Development vs Economic Growth").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        g1 = Tex("Growth: a QUANTITY statement — real GDP rose").scale(1.05).shift(UP * 1.1)
        g2 = Tex("Development: a QUALITY statement — lives improved").scale(1.01).shift(UP * 0.2)
        self.play(Write(g1))
        self.wait(2)
        self.play(Write(g2))
        self.wait(2.5)
        g3 = Tex("Oil-rich, unschooled, unwell: growth WITHOUT development").scale(0.9).shift(DOWN * 0.8)
        self.play(Write(g3))
        self.wait(2)
        g4 = Tex("Modest growth, big gains in schooling and health:").scale(0.95).shift(DOWN * 1.7)
        g5 = Tex("development racing ahead of growth").scale(0.95).shift(DOWN * 2.5)
        self.play(Write(g4))
        self.play(Write(g5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the HDI and the poverty measures ---
        self.next_band(1)
        b1_title = Tex("Human Development Index: three dimensions").scale(1.1).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        box1 = Rectangle(width=3.6, height=1.2).shift(band_shift(1) + LEFT * 4.2 + UP * 1.1)
        lab1 = Tex("Income: GNI per capita").scale(0.7).move_to(box1.get_center())
        box2 = Rectangle(width=3.6, height=1.2).shift(band_shift(1) + UP * 1.1)
        lab2 = Tex("Health: life expectancy").scale(0.7).move_to(box2.get_center())
        box3 = Rectangle(width=3.6, height=1.2).shift(band_shift(1) + RIGHT * 4.2 + UP * 1.1)
        lab3 = Tex("Education: schooling").scale(0.7).move_to(box3.get_center())
        self.play(Create(box1), Write(lab1))
        self.play(Create(box2), Write(lab2))
        self.play(Create(box3), Write(lab3))
        self.wait(2)
        h1 = Tex("One score per country, between 0 and 1").scale(1.0).shift(band_shift(1) + UP * 0.1)
        self.play(Write(h1))
        self.wait(2)
        h2 = Tex("SA: richer than we are healthy or educated").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(h2))
        self.play(Create(SurroundingRectangle(h2, color=GREEN)))
        self.wait(2.5)
        h3 = Tex("Absolute poverty: below a fixed line (food poverty line)").scale(0.85).shift(band_shift(1) + DOWN * 1.7)
        h4 = Tex("Relative: far below your society; multidimensional: services").scale(0.8).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(h3))
        self.wait(2)
        self.play(Write(h4))
        self.wait(3)

        # --- Band 2 (subtopic_2): six signs, first three ---
        self.next_band(2)
        b2_title = Tex("Six signs of developing countries (1--3)").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        s1 = Tex("1. Low standard of living — SA twist: the SPREAD").scale(0.95).shift(band_shift(2) + UP * 1.3)
        self.play(Write(s1))
        self.wait(2.5)
        s2 = Tex("2. Low productivity: few tools, little training").scale(0.95).shift(band_shift(2) + UP * 0.4)
        s2b = Tex(r"low pay $\to$ low saving $\to$ no tools: vicious circle").scale(0.9).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(s2))
        self.wait(2)
        self.play(Write(s2b))
        self.wait(2.5)
        s3 = Tex(r"3. High population growth, heavy dependency burden").scale(0.95).shift(band_shift(2) + DOWN * 1.5)
        s3b = Tex(r"SA: $\approx 1{,}5\%$ growth — still ahead of GDP growth").scale(0.9).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(s3))
        self.wait(2)
        self.play(Write(s3b))
        self.wait(3)

        # --- Band 3 (subtopic_2): six signs, last three + the checklist ---
        self.next_band(3)
        b3_title = Tex("Six signs (4--6), and how to use them").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        t1 = Tex(r"4. Unemployment: SA extreme — 30\%$+$, 40\%$+$ expanded").scale(0.9).shift(band_shift(3) + UP * 1.3)
        self.play(Write(t1))
        self.wait(2.5)
        t2 = Tex("5. Primary-sector dependence: raw exports, swinging prices").scale(0.85).shift(band_shift(3) + UP * 0.4)
        t2b = Tex("SA half-fits: services dominate, exports lean on minerals").scale(0.85).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(t2))
        self.wait(2)
        self.play(Write(t2b))
        self.wait(2)
        t3 = Tex("6. Deficient infrastructure and incomplete markets").scale(0.9).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(t3))
        self.wait(2)
        t4 = Tex("Diagnose: fits, does not fit, or fits WITH A TWIST").scale(0.95).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(t4))
        self.play(Create(SurroundingRectangle(t4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): three strategic choices ---
        self.next_band(4)
        b4_title = Tex("Development strategies: three big choices").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        c1 = Tex("1. Who leads: the STATE or the MARKET?").scale(1.0).shift(band_shift(4) + UP * 1.3)
        c1b = Tex("Every success story mixes the two").scale(0.9).shift(band_shift(4) + UP * 0.5)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c1b))
        self.wait(2)
        c2 = Tex("2. Which direction: INWARD (import substitution)").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        c2b = Tex("or OUTWARD (exports — the East Asian route)").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(c2))
        self.play(Write(c2b))
        self.wait(2.5)
        c3 = Tex("3. The engine: THINGS (big push) or PEOPLE?").scale(0.95).shift(band_shift(4) + DOWN * 2.1)
        c3b = Tex("No country developed with people unschooled and unwell").scale(0.85).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(c3))
        self.wait(2)
        self.play(Write(c3b))
        self.wait(3)

        # --- Band 5 (subtopic_3): South Africa's succession of plans ---
        self.next_band(5)
        b5_title = Tex("South Africa's plans since 1994").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        tl = Line(band_shift(5) + LEFT * 5.2 + UP * 1.4, band_shift(5) + RIGHT * 5.2 + UP * 1.4, stroke_width=4)
        dot1 = Dot(band_shift(5) + LEFT * 3.8 + UP * 1.4)
        dot2 = Dot(band_shift(5) + UP * 1.4)
        dot3 = Dot(band_shift(5) + RIGHT * 3.8 + UP * 1.4)
        l1 = Tex("RDP: basic needs").scale(0.75).move_to(band_shift(5) + LEFT * 3.8 + UP * 2.0)
        l2 = Tex("GEAR 1996: stabilise").scale(0.75).move_to(band_shift(5) + UP * 2.0)
        l3 = Tex("NDP 2030").scale(0.75).move_to(band_shift(5) + RIGHT * 3.8 + UP * 2.0)
        self.play(Create(tl))
        self.play(Create(dot1), Write(l1))
        self.wait(1.5)
        self.play(Create(dot2), Write(l2))
        self.wait(1.5)
        self.play(Create(dot3), Write(l3))
        self.wait(2)
        p1 = Tex("RDP: houses, water, electricity, clinics — delivered directly").scale(0.8).shift(band_shift(5) + UP * 0.5)
        p2 = Tex("GEAR: debt and inflation steadied; jobs lagged").scale(0.85).shift(band_shift(5) + DOWN * 0.3)
        p3 = Tex("NDP 2030: end income poverty, single-digit unemployment").scale(0.8).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(p1))
        self.wait(2)
        self.play(Write(p2))
        self.wait(2)
        self.play(Write(p3))
        self.wait(2)
        p4 = Tex("Instruments: EPWP, special economic zones, social grants").scale(0.8).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(p4))
        self.wait(2)
        p5 = Tex("A plan is a strategy; development is a delivery record").scale(0.85).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(p5))
        self.play(Create(SurroundingRectangle(p5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): IKS contributions ---
        self.next_band(6)
        b6_title = Tex("Indigenous Knowledge Systems: from within").scale(1.1).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        k1 = Tex("Finance: stokvels move tens of billions a year;").scale(0.9).shift(band_shift(6) + UP * 1.3)
        k1b = Tex("burial societies insure millions").scale(0.9).shift(band_shift(6) + UP * 0.5)
        self.play(Write(k1))
        self.play(Write(k1b))
        self.wait(2.5)
        k2 = Tex("Agriculture: sorghum, millet, intercropping — drought-wise").scale(0.85).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(k2))
        self.wait(2)
        k3 = Tex("Medicine: healers recognised by law; plant value").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(k3))
        self.wait(2)
        k4 = Tex("Development that ignores what people trust tends to FAIL").scale(0.85).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(k4))
        self.play(Create(SurroundingRectangle(k4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): protection — hoodia and biopiracy ---
        self.next_band(7)
        b7_title = Tex("Protecting IKS: the hoodia case").scale(1.15).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        q1 = Tex("San hoodia knowledge patented without consent or payment").scale(0.85).shift(band_shift(7) + UP * 1.3)
        self.play(Write(q1))
        self.wait(2.5)
        q2 = Tex("BIOPIRACY: profiting from indigenous knowledge").scale(0.95).shift(band_shift(7) + UP * 0.4)
        q2b = Tex("without consent or compensation").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(q2))
        self.play(Write(q2b))
        self.wait(2.5)
        q3 = Tex("Answer: IKS law, benefit-sharing, recorded knowledge").scale(0.9).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(q3))
        self.wait(2)
        q4 = Tex("Rooibos: Khoi and San now earn a recognised share").scale(0.9).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(q4))
        self.wait(2)
        q5 = Tex("Neither museum piece nor replacement: a development asset").scale(0.8).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(q5))
        self.play(Create(SurroundingRectangle(q5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): taller or better? ---
        self.next_band(8)
        b8_title = Tex("Taller or better? The tape measure test").scale(1.1).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        m1 = Tex("Growth: the tape measure against the door frame").scale(0.95).shift(band_shift(8) + UP * 1.3)
        m2 = Tex("Development: everything the tape cannot see").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(m1))
        self.wait(2)
        self.play(Write(m2))
        self.wait(2.5)
        m3 = Tex("New mall, dry taps, sixty to a class: grew, not developed").scale(0.85).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(m3))
        self.wait(2.5)
        m4 = Tex("HDI: money $+$ health $+$ learning, one score 0 to 1").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(m4))
        self.wait(2)
        m5 = Tex("SA: richer than we are healthy or educated").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(m5))
        self.play(Create(SurroundingRectangle(m5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): six signs walked down one street ---
        self.next_band(9)
        b9_title = Tex("The six signs, walked down one street").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        w1 = Tex("1. Meals that stretch — and the suburb twenty minutes away").scale(0.8).shift(band_shift(9) + UP * 1.4)
        w2 = Tex("2. A spade next to a machine: under-equipped, not lazy").scale(0.8).shift(band_shift(9) + UP * 0.6)
        w3 = Tex("3. One pay packet, many mouths: nothing left to invest").scale(0.8).shift(band_shift(9) + DOWN * 0.2)
        w4 = Tex("4. Certificates with nowhere to go: three, four in ten").scale(0.8).shift(band_shift(9) + DOWN * 1.0)
        w5 = Tex("5. Selling raw ore, buying back phones made from it").scale(0.8).shift(band_shift(9) + DOWN * 1.8)
        w6 = Tex("6. Power that cuts, trains that never come, loans refused").scale(0.8).shift(band_shift(9) + DOWN * 2.6)
        for m in (w1, w2, w3, w4, w5, w6):
            self.play(Write(m))
            self.wait(1.8)
        self.play(Create(SurroundingRectangle(VGroup(w1, w6), color=GREEN, buff=0.25)))
        self.wait(3)

        # --- Band 10 (subtopic_7): plans on paper, roots in the ground ---
        self.next_band(10)
        b10_title = Tex("Plans on paper, roots in the ground").scale(1.1).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        n1 = Tex(r"RDP built basics $\to$ GEAR steadied money $\to$ NDP 2030").scale(0.85).shift(band_shift(10) + UP * 1.4)
        self.play(Write(n1))
        self.wait(2.5)
        n2 = Tex("Report card: services delivered, floor held;").scale(0.9).shift(band_shift(10) + UP * 0.5)
        n2b = Tex("growth and jobs repeatedly missed").scale(0.9).shift(band_shift(10) + DOWN * 0.3)
        self.play(Write(n2))
        self.play(Write(n2b))
        self.wait(2.5)
        n3 = Tex("The stokvel turns neighbours into a bank — trust as").scale(0.85).shift(band_shift(10) + DOWN * 1.2)
        n3b = Tex("infrastructure; sorghum where the grandmothers knew").scale(0.85).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(n3))
        self.play(Write(n3b))
        self.wait(2.5)
        n4 = Tex("Guard the roots: hoodia, biopiracy, benefit-sharing").scale(0.9).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(n4))
        self.play(Create(SurroundingRectangle(n4, color=GREEN)))
        self.wait(4)
