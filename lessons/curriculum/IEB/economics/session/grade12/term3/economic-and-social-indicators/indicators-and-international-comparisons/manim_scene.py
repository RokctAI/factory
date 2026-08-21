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
        title = Tex("Economic and Social Indicators").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        t1 = Tex("LEADING: turn BEFORE the economy —").scale(1.0).shift(UP * 1.4)
        t2 = Tex("building plans, job adverts, factory orders").scale(1.0).shift(UP * 0.7)
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(2.5)
        t3 = Tex("COINCIDENT: move WITH it — retail sales,").scale(1.0).shift(DOWN * 0.2)
        t4 = Tex("industrial production, real GDP").scale(1.0).shift(DOWN * 0.9)
        self.play(Write(t3))
        self.play(Write(t4))
        self.wait(2.5)
        t5 = Tex("LAGGING: confirm AFTER — unemployment,").scale(1.0).shift(DOWN * 1.8)
        t6 = Tex("inventories, insolvencies (never predict)").scale(1.0).shift(DOWN * 2.5)
        self.play(Write(t5))
        self.play(Write(t6))
        self.play(Create(SurroundingRectangle(VGroup(t5, t6), color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): level vs rate, nominal vs real ---
        self.next_band(1)
        b1_title = Tex("Two disciplines before any reading").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("LEVEL $=$ size; RATE $=$ direction").scale(1.1).shift(band_shift(1) + UP * 1.3)
        b1_l2 = Tex("A giant economy can stall; a small one can sprint").scale(0.95).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("NOMINAL inflates with prices — deflate it:").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = MathTex(r"\text{real} \approx \text{nominal} - \text{inflation}").scale(1.1).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = MathTex(r"7{,}5\% - 5{,}5\% = 2{,}0\% \text{ real growth}").scale(1.05).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): production, prices, money ---
        self.next_band(2)
        b2_title = Tex("The economic gauges, part one").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Production: real GDP growth $+$ GDP per capita").scale(1.0).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("GDP $+0{,}9\\%$, population $+1{,}5\\%$ $\\rightarrow$").scale(1.0).shift(band_shift(2) + UP * 0.6)
        b2_l3 = Tex("output per person FALLS in a growing economy").scale(1.0).shift(band_shift(2) + DOWN * 0.1)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Prices: CPI at the till, PPI at the factory gate").scale(1.0).shift(band_shift(2) + DOWN * 1.1)
        b2_l5 = Tex("Money: M1 $\\subset$ M2 $\\subset$ M3 (Bank tracks M3)").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        b2_l6 = Tex("$+$ private credit — fast growth warns of inflation").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): interest, external gauges, labour ---
        self.next_band(3)
        b3_title = Tex("The economic gauges, part two").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Interest: repo (policy), prime (banks' best),").scale(1.0).shift(band_shift(3) + UP * 1.5)
        b3_l2 = MathTex(r"\text{real rate} = \text{nominal} - \text{inflation}").scale(1.0).shift(band_shift(3) + UP * 0.7)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("External: rand, current account, terms of trade").scale(0.97).shift(band_shift(3) + DOWN * 0.2)
        b3_l4 = MathTex(r"\text{ToT} = \frac{\text{export prices}}{\text{import prices}} \times 100").scale(1.0).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex("Labour: strict rate counts searchers only;").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        b3_l6 = Tex("expanded adds the discouraged — the gap is hope lost").scale(0.92).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the social indicators ---
        self.next_band(4)
        b4_title = Tex("Social indicators: measuring the passengers").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Life expectancy: development's summary number —").scale(0.97).shift(band_shift(4) + UP * 1.5)
        b4_l2 = Tex("fell under untreated AIDS, rose $10+$ years with ARVs").scale(0.95).shift(band_shift(4) + UP * 0.8)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Infant mortality: deaths before age 1 per 1 000").scale(0.97).shift(band_shift(4) + DOWN * 0.1)
        b4_l4 = Tex("births — the sharpest poverty gauge").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex("Education: enrolment AND learning outcomes").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        b4_l6 = Tex("Services: water, sanitation, electricity $\\sim$ 9 in 10").scale(0.97).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): HDI and Gini ---
        self.next_band(5)
        b5_title = Tex("Two composite summaries").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("HDI $=$ life expectancy $+$ education $+$ income,").scale(1.0).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("one score from 0 to 1 — lives, not just money").scale(1.0).shift(band_shift(5) + UP * 0.7)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Gini: 0 $=$ everyone equal, 1 $=$ one owns all").scale(1.0).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"\text{South Africa: Gini} \approx 0{,}63\text{--}0{,}65").scale(1.05).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex("Among the highest inequality ever recorded").scale(1.0).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three comparison corrections ---
        self.next_band(6)
        b6_title = Tex("Comparing countries: three corrections").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("1. PER CAPITA: divide by the people —").scale(1.0).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("China's total vs the richer Swiss resident").scale(1.0).shift(band_shift(6) + UP * 0.7)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("2. PPP: price money where it lives — R100 buys").scale(0.97).shift(band_shift(6) + DOWN * 0.2)
        b6_l4 = Tex("a meal in Mthatha, a coffee in London").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("3. COVERAGE: the informal sector, subsistence").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        b6_l6 = Tex("farming, unpaid work — unmeasured, so gaps overstate").scale(0.92).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(VGroup(b6_l5, b6_l6), color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): IMF vs World Bank ---
        self.next_band(7)
        b7_title = Tex("Bretton Woods, 1944: two institutions").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("IMF — the paramedic: surveillance $+$ loans in").scale(1.0).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("balance-of-payments crises, with CONDITIONALITY").scale(0.97).shift(band_shift(7) + UP * 0.7)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("World Bank — the builder: long-term loans for").scale(1.0).shift(band_shift(7) + DOWN * 0.2)
        b7_l4 = Tex("infrastructure, education, health $+$ the data").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("IMF: short-term crisis finance.").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        b7_l6 = Tex("World Bank: long-term development.").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(VGroup(b7_l5, b7_l6), color=GREEN)))
        b7_l7 = Tex("SA drew $\\sim$4,3 billion dollars from the IMF in 2020").scale(0.92).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_l7))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): headlights, speedometer, mirror ---
        self.next_band(8)
        b8_title = Tex("Headlights, speedometer, mirror").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Headlights (leading): building plans, job adverts,").scale(0.97).shift(band_shift(8) + UP * 1.5)
        b8_l2 = Tex("factory orders — promises about next year").scale(1.0).shift(band_shift(8) + UP * 0.8)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Speedometer (coincident): tills, factories, GDP now").scale(0.95).shift(band_shift(8) + DOWN * 0.1)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Mirror (lagging): JOBS — employers retrench late").scale(0.97).shift(band_shift(8) + DOWN * 1.0)
        b8_l5 = Tex("and rehire late, so employment moves LAST").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2)
        b8_l6 = Tex("Size is not speed; rands stretch, kilometres don't").scale(0.97).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): the passengers' report ---
        self.next_band(9)
        b9_title = Tex("The passengers' report").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Eldest: how long do people live? — life expectancy").scale(0.95).shift(band_shift(9) + UP * 1.5)
        b9_l2 = Tex("Mother: do babies reach one? — infant mortality").scale(0.95).shift(band_shift(9) + UP * 0.7)
        b9_l3 = Tex("Learner: in school AND learning? — education").scale(0.95).shift(band_shift(9) + DOWN * 0.1)
        b9_l4 = Tex("Household: tap, toilet, switch? — services").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        for m in (b9_l1, b9_l2, b9_l3, b9_l4):
            self.play(Write(m))
            self.wait(1.6)
        b9_l5 = Tex("HDI: health $+$ school $+$ income out of 1").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        b9_l6 = Tex("Gini: how is the cash SHARED? SA $\\approx 0{,}63$").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): comparing taxis honestly ---
        self.next_band(10)
        b10_title = Tex("Comparing taxis honestly").scale(1.2).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("1. Divide by the heads: R12 000 among 18 is").scale(1.0).shift(band_shift(10) + UP * 1.7)
        b10_l2 = Tex("poorer per person than R5 000 among 3").scale(1.0).shift(band_shift(10) + UP * 1.0)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("2. Price money at home: PPP can lift a poor").scale(1.0).shift(band_shift(10) + UP * 0.1)
        b10_l4 = Tex("country's measured income two or three times").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("3. Respect the unseen meter: informal work").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        b10_l6 = Tex("makes measured gaps wider than real ones").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(2.5)
        b10_l7 = Tex("IMF the paramedic; World Bank the builder").scale(1.0).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l7))
        self.play(Create(SurroundingRectangle(b10_l7, color=GREEN)))
        self.wait(4)
