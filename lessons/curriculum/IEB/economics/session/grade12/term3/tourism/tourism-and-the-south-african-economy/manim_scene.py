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

# Band-layout whiteboard scene for the tourism session duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 225/230/245/250/185/195/195 of 1525 s — bands
# 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10 apportioned to match.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TourismSouthAfricanEconomySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): what counts as a tourist ---
        title = Tex("Tourism and the South African Economy").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Tourist (UNWTO): outside the usual environment,").scale(0.97).shift(UP * 1.3)
        d2 = Tex("under a year, not paid at the destination").scale(1.0).shift(UP * 0.6)
        self.play(Write(d1))
        self.play(Write(d2))
        self.play(Create(SurroundingRectangle(VGroup(d1, d2), color=GREEN)))
        self.wait(2.5)
        d3 = Tex("Each clause excludes something: commuting,").scale(1.0).shift(DOWN * 0.4)
        d4 = Tex("migration, taking a job there").scale(1.0).shift(DOWN * 1.1)
        self.play(Write(d3))
        self.play(Write(d4))
        self.wait(2.5)
        d5 = Tex("Overnight $=$ tourist; same-day $=$ day visitor").scale(1.0).shift(DOWN * 2.1)
        d6 = Tex("(counted, but spends a fraction)").scale(0.95).shift(DOWN * 2.8)
        self.play(Write(d5))
        self.play(Write(d6))
        self.wait(3)

        # --- Band 1 (subtopic_1): the three flows ---
        self.next_band(1)
        b1_title = Tex("Three flows, one trade logic").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("DOMESTIC: Pretoria family to Ballito —").scale(1.0).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("rands circulate at home, no new money in").scale(1.0).shift(band_shift(1) + UP * 0.7)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("INBOUND: foreign visitors here $=$ an EXPORT,").scale(1.0).shift(band_shift(1) + DOWN * 0.2)
        b1_l4 = Tex("foreign exchange earned inside our borders").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l5 = Tex("OUTBOUND: residents abroad $=$ an import").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        b1_l6 = Tex("Balance in surplus; purposes: leisure, MICE, VFR").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): why tourism has grown ---
        self.next_band(2)
        b2_title = Tex("From millions to a billion trips").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Demand: rising incomes, paid leave, long").scale(1.0).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("retirements, Asia's new middle classes").scale(1.0).shift(band_shift(2) + UP * 0.7)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("Supply: jets and budget airlines collapsed the").scale(1.0).shift(band_shift(2) + DOWN * 0.2)
        b2_l4 = Tex("price of distance; the internet, of knowing").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = Tex("A year's wages $\\rightarrow$ a week's wages per flight").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): enablers and fragility ---
        self.next_band(3)
        b3_title = Tex("Enablers — and the fragile floor").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Tourism follows safety: peace, open borders,").scale(1.0).shift(band_shift(3) + UP * 1.4)
        b3_l2 = Tex("easy visas, convertible currencies").scale(1.0).shift(band_shift(3) + UP * 0.7)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("1994: apartheid and sanctions end — SA becomes").scale(0.97).shift(band_shift(3) + DOWN * 0.2)
        b3_l4 = Tex("a fastest-growing destination within a decade").scale(0.97).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)
        b3_l5 = Tex("2020: world tourism $\\rightarrow$ near zero in a quarter;").scale(0.97).shift(band_shift(3) + DOWN * 1.9)
        b3_l6 = Tex("$\\sim$1 SA job in 20 silenced — luxury spend, fragile floor").scale(0.92).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): GDP, jobs, beneficiaries ---
        self.next_band(4)
        b4_title = Tex("What tourism does to the economy").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{GDP: } \sim 3\% \text{ direct} \rightarrow 8\text{--}9\% \text{ with multiplier}").scale(0.97).shift(band_shift(4) + UP * 1.4)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2.5)
        b4_l2 = Tex("Labour-intensive: beds, meals, guiding by PEOPLE —").scale(0.95).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex("a tourism rand out-hires a mining rand").scale(1.0).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex("Jobs where nothing else goes: semi-skilled,").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        b4_l5 = Tex("women, youth, rural — a lodge is an export in a village").scale(0.92).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2)
        b4_l6 = Tex("Benefits: households, businesses, infrastructure, state").scale(0.92).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): the honest ledger of costs ---
        self.next_band(5)
        b5_title = Tex("The cost column").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Externalities: crowding, water and land pressure,").scale(0.97).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("litter, cultural commodification").scale(1.0).shift(band_shift(5) + UP * 0.7)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Leakages: foreign-owned hotel, imported food,").scale(1.0).shift(band_shift(5) + DOWN * 0.2)
        b5_l4 = Tex("package sold abroad — the rand exits early").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)
        b5_l5 = Tex("Seasonality: the coast hires in December,").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        b5_l6 = Tex("retrenches in February — precarious work").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): the shop window and IKS ---
        self.next_band(6)
        b6_title = Tex("The shop window, and IKS").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Pillars: wildlife and scenery; heritage and culture").scale(0.95).shift(band_shift(6) + UP * 1.5)
        b6_l2 = Tex("(10 UNESCO sites); events and business; climate").scale(0.95).shift(band_shift(6) + UP * 0.8)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("IKS: tracking, healing knowledge, storytelling,").scale(0.97).shift(band_shift(6) + DOWN * 0.1)
        b6_l4 = Tex("craft, cuisine — products no rival can copy").scale(0.97).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Two duties: AUTHENTICITY — the community owns").scale(0.95).shift(band_shift(6) + DOWN * 1.7)
        b6_l6 = Tex("the telling; BENEFIT-SHARING — it banks the earnings").scale(0.92).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): policy architecture and fixes ---
        self.next_band(7)
        b7_title = Tex("Architecture, obstacles, fixes").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("1996 White Paper: state leads, private sector").scale(0.97).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("delivers, communities benefit; Tourism Act 2014;").scale(0.95).shift(band_shift(7) + UP * 0.7)
        b7_l3 = Tex("SA Tourism marketing; TOMSA levy of 1\\%; NDP priority").scale(0.9).shift(band_shift(7))
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("Match obstacle to fix: slow visas $\\rightarrow$ e-visas;").scale(0.95).shift(band_shift(7) + DOWN * 1.0)
        b7_l5 = Tex("crime fear $\\rightarrow$ visible policing; few flights $\\rightarrow$").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        b7_l6 = Tex("direct routes; short skills $\\rightarrow$ train ahead;").scale(0.95).shift(band_shift(7) + DOWN * 2.4)
        b7_l7 = Tex("power cuts $\\rightarrow$ keeping lights on IS marketing").scale(0.95).shift(band_shift(7) + DOWN * 3.1)
        for m in (b7_l4, b7_l5, b7_l6, b7_l7):
            self.play(Write(m))
            self.wait(1.6)
        self.wait(2)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the export that walks in ---
        self.next_band(8)
        b8_title = Tex("The export that walks in").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Coal sails from Richards Bay and never returns.").scale(0.97).shift(band_shift(8) + UP * 1.5)
        b8_l2 = Tex("The visitor flies in, spends dollars, flies out —").scale(0.97).shift(band_shift(8) + UP * 0.8)
        b8_l3 = Tex("and Table Mountain is still here at sunrise").scale(0.97).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l1))
        self.wait(1.5)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Aunt to Margate: domestic. Canadians here:").scale(1.0).shift(band_shift(8) + DOWN * 0.9)
        b8_l5 = Tex("inbound (export). Cousin to Bangkok: outbound").scale(0.97).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("One holiday invoices eight industries at once").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): one busload, three rings ---
        self.next_band(9)
        b9_title = Tex("One busload, many pay packets").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("DIRECT ring: the lodge payroll — chef, guides,").scale(0.97).shift(band_shift(9) + UP * 1.5)
        b9_l2 = Tex("housekeepers, tracker, maintenance").scale(1.0).shift(band_shift(9) + UP * 0.8)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("INDIRECT ring: the farmer, laundry, security,").scale(0.97).shift(band_shift(9))
        b9_l4 = Tex("builder — firms that sell to the lodge").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("INDUCED ring: wages spent at spaza, taxi, salon —").scale(0.95).shift(band_shift(9) + DOWN * 1.6)
        b9_l6 = Tex("the multiplier in a lodge uniform").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(2)
        b9_l7 = Tex("Watch the LEAK: foreign-owned, imported, paid abroad").scale(0.9).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9_l7))
        self.wait(3)

        # --- Band 10 (subtopic_7): selling what only we have ---
        self.next_band(10)
        b10_title = Tex("Selling what only we have").scale(1.2).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("The 11-hour flight buys the only-here shelf:").scale(1.0).shift(band_shift(10) + UP * 1.7)
        b10_l2 = Tex("wild Big Five, Table Mountain, Robben Island,").scale(1.0).shift(band_shift(10) + UP * 1.0)
        b10_l3 = Tex("the Cradle — and living indigenous knowledge").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("IKS rules: own the telling, bank the earnings").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("Fix what blocks the visit: e-visas, safe routes,").scale(0.97).shift(band_shift(10) + DOWN * 1.5)
        b10_l6 = Tex("direct flights, trained staff, steady power").scale(0.97).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(2)
        b10_l7 = Tex("Grows as fast as the visit is easy, safe and shared").scale(0.95).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l7))
        self.wait(4)
