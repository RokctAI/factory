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

# Band-layout whiteboard scene for the indicators session duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 220/255/245/245/190/190/195 of 1540 s — bands
# 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10 apportioned to match.
# Diagrams hand-built from Arrow/Line/Rectangle/Tex primitives only.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IndicatorsInternationalComparisonsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): indicator types by timing ---
        title = Tex("Economic and Social Indicators").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d0 = Tex("Indicator: a statistic signalling performance").scale(1.05).shift(UP * 1.5)
        self.play(Write(d0))
        self.wait(2)
        l1 = Tex("LEADING — change BEFORE the economy:").scale(1.05).shift(UP * 0.6)
        l1b = Tex("building plans, job adverts, factory orders").scale(1.0).shift(DOWN * 0.1)
        self.play(Write(l1))
        self.play(Write(l1b))
        self.wait(2)
        l2 = Tex("COINCIDENT — move WITH it: production, GDP").scale(1.0).shift(DOWN * 1.0)
        self.play(Write(l2))
        self.wait(2)
        l3 = Tex("LAGGING — confirm AFTER: unemployment,").scale(1.0).shift(DOWN * 1.9)
        l3b = Tex("inventories, insolvencies").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(l3))
        self.play(Write(l3b))
        self.wait(3)

        # --- Band 1 (subtopic_1): level vs rate, nominal vs real ---
        self.next_band(1)
        b1_title = Tex("Two distinctions the exam tests").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("LEVEL = size of GDP; RATE = its direction").scale(1.05).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("Large and shrinking, or small and booming").scale(1.05).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("NOMINAL is inflated by prices; deflate to REAL").scale(1.05).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"\text{Real growth} \approx 8\% - 6\% = 2\%").scale(1.2).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): production, prices, money ---
        self.next_band(2)
        b2_title = Tex("The economic gauges I").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Production: real GDP growth — the headline").scale(1.0).shift(band_shift(2) + UP * 1.5)
        b2_l2 = Tex("GDP grows 1\\%, population 1,5\\%:").scale(1.0).shift(band_shift(2) + UP * 0.7)
        b2_l3 = Tex("output per person is FALLING").scale(1.05).shift(band_shift(2))
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Prices: CPI and PPI — SARB target 3–6\\%").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Money: M1 (coins, notes, demand deposits)").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        b2_l6 = Tex("$\\subset$ M2 (+ short/medium deposits)").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        b2_l7 = Tex("$\\subset$ M3 (+ long-term) — the Bank tracks M3").scale(1.0).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_l5))
        self.wait(1.5)
        self.play(Write(b2_l6))
        self.wait(1.5)
        self.play(Write(b2_l7))
        self.wait(3)

        # --- Band 3 (subtopic_2): interest, external gauges, labour ---
        self.next_band(3)
        b3_title = Tex("The economic gauges II").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Real interest} = \text{nominal} - \text{inflation}").scale(1.05).shift(band_shift(3) + UP * 1.5)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\text{Terms of trade} = \frac{\text{export } P}{\text{import } P} \times 100").scale(0.9).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Improvement = a national raise, no extra ton").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("Unemployment: STRICT = actively searching;").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        b3_l5 = Tex("EXPANDED adds discouraged work-seekers").scale(1.0).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = Tex("Productivity: the only wage rise with no inflation").scale(1.0).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): the social indicators ---
        self.next_band(4)
        b4_title = Tex("The social gauges — the passengers").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Life expectancy: the great summary statistic —").scale(1.0).shift(band_shift(4) + UP * 1.5)
        b4_l2 = Tex("fell in untreated AIDS years, +10 yrs with ARVs").scale(1.0).shift(band_shift(4) + UP * 0.8)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Infant mortality (deaths $<$ 1 yr per 1 000 births):").scale(1.0).shift(band_shift(4))
        b4_l4 = Tex("the most sensitive poverty gauge").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex("Education: enrolment AND learning outcomes").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l5))
        self.wait(2)
        b4_l6 = Tex("Services: water, sanitation, electricity ($\\sim$90\\%),").scale(1.0).shift(band_shift(4) + DOWN * 2.3)
        b4_l7 = Tex("housing; urbanisation — opportunity in towns").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l6))
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_3): HDI and Gini ---
        self.next_band(5)
        b5_title = Tex("Two composite measures").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("HDI (UNDP): life expectancy + education").scale(1.05).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("+ income per person, one score from 0 to 1").scale(1.05).shift(band_shift(5) + UP * 0.6)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Gini: inequality from 0 (all equal)").scale(1.05).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("to 1 (one person owns everything)").scale(1.05).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex("South Africa: Gini $\\approx$ 0,63–0,65 —").scale(1.05).shift(band_shift(5) + DOWN * 2.2)
        b5_l6 = Tex("among the highest ever recorded").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three comparison corrections ---
        self.next_band(6)
        b6_title = Tex("Comparing countries: three corrections").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("1. PER CAPITA — divide by population first:").scale(1.0).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("China's GDP dwarfs Denmark's; Danes are richer").scale(1.0).shift(band_shift(6) + UP * 0.7)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("2. PPP — revalue by what money buys locally;").scale(1.0).shift(band_shift(6) + DOWN * 0.2)
        b6_l4 = Tex("market rates understate poor countries").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("3. COVERAGE — informal sector, unpaid work,").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        b6_l6 = Tex("subsistence farming: measured gaps overstate").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): IMF vs World Bank ---
        self.next_band(7)
        b7_title = Tex("Bretton Woods, 1944: two institutions").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        r1 = Rectangle(width=5.6, height=2.4).shift(band_shift(7) + LEFT * 3.2 + UP * 0.5)
        r1_a = Tex("IMF").scale(1.1).shift(band_shift(7) + LEFT * 3.2 + UP * 1.2)
        r1_b = Tex("surveillance; lends in").scale(0.9).shift(band_shift(7) + LEFT * 3.2 + UP * 0.5)
        r1_c = Tex("BoP crises, with conditions").scale(0.9).shift(band_shift(7) + LEFT * 3.2 + DOWN * 0.1)
        self.play(Create(r1), Write(r1_a))
        self.play(Write(r1_b), Write(r1_c))
        self.wait(2.5)
        r2 = Rectangle(width=5.6, height=2.4).shift(band_shift(7) + RIGHT * 3.2 + UP * 0.5)
        r2_a = Tex("World Bank").scale(1.1).shift(band_shift(7) + RIGHT * 3.2 + UP * 1.2)
        r2_b = Tex("long-term loans for").scale(0.9).shift(band_shift(7) + RIGHT * 3.2 + UP * 0.5)
        r2_c = Tex("development projects").scale(0.9).shift(band_shift(7) + RIGHT * 3.2 + DOWN * 0.1)
        self.play(Create(r2), Write(r2_a))
        self.play(Write(r2_b), Write(r2_c))
        self.wait(2.5)
        b7_l1 = Tex("IMF: short-term crisis finance and stability;").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        b7_l2 = Tex("World Bank: long-term development projects").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(VGroup(b7_l1, b7_l2), color=GREEN)))
        self.wait(2)
        b7_l3 = Tex("SA, 2020: over \\$4 billion from the IMF").scale(1.0).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l3))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): headlights, speedometer, mirror ---
        self.next_band(8)
        b8_title = Tex("The taxi on the N1 at night").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        r1 = Rectangle(width=4.0, height=1.5).shift(band_shift(8) + LEFT * 4.5 + UP * 1.0)
        r1_a = Tex("Headlights").scale(1.0).shift(band_shift(8) + LEFT * 4.5 + UP * 1.3)
        r1_b = Tex("= LEADING").scale(0.9).shift(band_shift(8) + LEFT * 4.5 + UP * 0.7)
        self.play(Create(r1), Write(r1_a), Write(r1_b))
        self.wait(2)
        r2 = Rectangle(width=4.0, height=1.5).shift(band_shift(8) + UP * 1.0)
        r2_a = Tex("Speedometer").scale(1.0).shift(band_shift(8) + UP * 1.3)
        r2_b = Tex("= COINCIDENT").scale(0.9).shift(band_shift(8) + UP * 0.7)
        self.play(Create(r2), Write(r2_a), Write(r2_b))
        self.wait(2)
        r3 = Rectangle(width=4.0, height=1.5).shift(band_shift(8) + RIGHT * 4.5 + UP * 1.0)
        r3_a = Tex("Mirror").scale(1.0).shift(band_shift(8) + RIGHT * 4.5 + UP * 1.3)
        r3_b = Tex("= LAGGING").scale(0.9).shift(band_shift(8) + RIGHT * 4.5 + UP * 0.7)
        self.play(Create(r3), Write(r3_a), Write(r3_b))
        self.wait(2)
        b8_l1 = Tex("Jobs are a MIRROR: bosses retrench late,").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        b8_l2 = Tex("rehire late — unemployment moves LAST").scale(1.0).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Takings up 8\\%, prices up 6\\%: trip only 2\\% longer").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        b8_l4 = Tex("Rands stretch; kilometres do not").scale(1.0).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the passengers' report ---
        self.next_band(9)
        b9_title = Tex("Ask the passengers").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Oldest passenger: how long do people live?").scale(1.0).shift(band_shift(9) + UP * 1.5)
        b9_l2 = Tex("Young mother: do babies see their first birthday?").scale(1.0).shift(band_shift(9) + UP * 0.7)
        b9_l3 = Tex("Schoolchild: in school — and LEARNING?").scale(1.0).shift(band_shift(9) + DOWN * 0.1)
        b9_l4 = Tex("Household: tap, flushing toilet, working lights?").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        for m in (b9_l1, b9_l2, b9_l3, b9_l4):
            self.play(Write(m))
            self.wait(2)
        b9_l5 = Tex("HDI: health + schooling + income, out of 1").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("Gini asks: how is the money SHARED? SA $\\approx$ 0,63").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): comparing taxis honestly ---
        self.next_band(10)
        b10_title = Tex("Comparing taxis honestly").scale(1.2).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("1. Divide by the passengers: R10 000 with 20").scale(1.0).shift(band_shift(10) + UP * 1.5)
        b10_l2 = Tex("aboard is poorer than R6 000 with 4").scale(1.0).shift(band_shift(10) + UP * 0.8)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("2. Ask what money buys where it lives — PPP").scale(1.0).shift(band_shift(10))
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("3. The meter misses the spaza, the gogo,").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        b10_l5 = Tex("the garden — official gaps exaggerate").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex("IMF = paramedic for crises;").scale(1.05).shift(band_shift(10) + DOWN * 2.4)
        b10_l7 = Tex("World Bank = builder for development").scale(1.05).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.play(Create(SurroundingRectangle(b10_l7, color=GREEN)))
        self.wait(4)
