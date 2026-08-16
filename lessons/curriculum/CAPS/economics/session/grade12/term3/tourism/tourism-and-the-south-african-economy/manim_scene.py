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
# Flow diagrams hand-built from Arrow/Line/Rectangle/Tex primitives only.

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
        title = Tex("Tourism and the South African Economy").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Tourist (UNWTO): travels OUTSIDE the usual").scale(1.05).shift(UP * 1.4)
        d2 = Tex("environment, for LESS THAN A YEAR, and is").scale(1.05).shift(UP * 0.6)
        d3 = Tex("NOT PAID at the destination").scale(1.05).shift(DOWN * 0.2)
        self.play(Write(d1))
        self.play(Write(d2))
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(VGroup(d1, d2, d3), color=GREEN)))
        self.wait(3)
        d4 = Tex("Stays at least one night = tourist proper;").scale(1.0).shift(DOWN * 1.3)
        d5 = Tex("same-day arrival = DAY VISITOR (spends less)").scale(1.0).shift(DOWN * 2.0)
        self.play(Write(d4))
        self.play(Write(d5))
        self.wait(2.5)
        d6 = Tex("Purposes: leisure, business (MICE), VFR, medical...").scale(0.95).shift(DOWN * 2.9)
        self.play(Write(d6))
        self.wait(3)

        # --- Band 1 (subtopic_1): the three flows ---
        self.next_band(1)
        b1_title = Tex("Three directions of flow").scale(1.15).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        border = DashedLine(band_shift(1) + UP * 1.8, band_shift(1) + DOWN * 1.4, stroke_width=3)
        sa_lab = Tex("South Africa").scale(0.95).shift(band_shift(1) + LEFT * 3.6 + UP * 1.5)
        abroad_lab = Tex("Abroad").scale(0.95).shift(band_shift(1) + RIGHT * 3.6 + UP * 1.5)
        self.play(Create(border), Write(sa_lab), Write(abroad_lab))
        self.wait(1.5)
        dom = Arrow(band_shift(1) + LEFT * 5.2 + UP * 0.7, band_shift(1) + LEFT * 1.6 + UP * 0.7,
                    buff=0, stroke_width=4, color=YELLOW)
        dom_lab = Tex("Domestic: inside — no new money").scale(0.84).shift(band_shift(1) + LEFT * 3.4 + UP * 0.2)
        self.play(Create(dom), Write(dom_lab))
        self.wait(2)
        inb = Arrow(band_shift(1) + RIGHT * 4.8 + DOWN * 0.6, band_shift(1) + LEFT * 3.6 + DOWN * 0.6,
                    buff=0, stroke_width=4, color=GREEN)
        inb_lab = Tex("Inbound: foreigners arrive = an EXPORT").scale(0.9).shift(band_shift(1) + DOWN * 1.1)
        self.play(Create(inb), Write(inb_lab))
        self.wait(2)
        outb = Arrow(band_shift(1) + LEFT * 3.6 + DOWN * 1.9, band_shift(1) + RIGHT * 4.8 + DOWN * 1.9,
                     buff=0, stroke_width=4, color=RED)
        outb_lab = Tex("Outbound: residents leave = an import").scale(0.9).shift(band_shift(1) + DOWN * 2.4)
        self.play(Create(outb), Write(outb_lab))
        self.wait(2)
        b1_l1 = Tex("SA's tourism balance: a healthy surplus").scale(1.0).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): why tourism has grown ---
        self.next_band(2)
        b2_title = Tex("Why tourism grew: millions to a billion+").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Demand: rising incomes, Asia's middle class,").scale(1.0).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("paid leave, pensions, longer healthier lives").scale(1.0).shift(band_shift(2) + UP * 0.7)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("Supply: jets and low-cost carriers collapsed").scale(1.0).shift(band_shift(2) + DOWN * 0.2)
        b2_l4 = Tex("the price of distance — a year's salary").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        b2_l5 = Tex("became a week's; internet booking, packages").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): enablers and fragility ---
        self.next_band(3)
        b3_title = Tex("Enablers — and the fragile floor").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Tourism follows safety: open borders, easy").scale(1.0).shift(band_shift(3) + UP * 1.4)
        b3_l2 = Tex("visas, converting currencies").scale(1.0).shift(band_shift(3) + UP * 0.7)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("1994: end of apartheid and sanctions turned a").scale(1.0).shift(band_shift(3) + DOWN * 0.2)
        b3_l4 = Tex("pariah into a fast-growing destination").scale(1.0).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)
        b3_l5 = Tex("Mirror: luxury spend, first cut in hard times —").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        b3_l6 = Tex("2020 shut world tourism in one quarter,").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        b3_l7 = Tex("silencing about one SA job in twenty").scale(1.0).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.play(Write(b3_l7))
        self.wait(3)

        # --- Band 4 (subtopic_3): GDP, jobs, beneficiaries ---
        self.next_band(4)
        b4_title = Tex("What tourism does to an economy").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("GDP: $\\sim$3\\% direct, 8–9\\% with the multiplier —").scale(1.0).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("hotel buys vegetables, worker spends at the spaza").scale(1.0).shift(band_shift(4) + UP * 0.7)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("LABOUR-INTENSIVE: each million rand employs").scale(1.0).shift(band_shift(4) + DOWN * 0.2)
        b4_l4 = Tex("more than mining or banking; semi-skilled,").scale(1.0).shift(band_shift(4) + DOWN * 0.9)
        b4_l5 = Tex("women, youth, rural corners").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2.5)
        b4_l6 = Tex("Households: wages. Businesses: revenue.").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        b4_l7 = Tex("Infrastructure stays. State: VAT and levies.").scale(1.0).shift(band_shift(4) + DOWN * 3.2)
        self.play(Write(b4_l6))
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_3): the honest ledger of costs ---
        self.next_band(5)
        b5_title = Tex("The cost column").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Externalities: crowding, water and land").scale(1.0).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("pressure, litter, cultural commodification").scale(1.0).shift(band_shift(5) + UP * 0.7)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("LEAKAGES: foreign-owned hotels, imported food,").scale(1.0).shift(band_shift(5) + DOWN * 0.2)
        b5_l4 = Tex("packages sold abroad — the rand exits").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        b5_l5 = Tex("before it multiplies").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(2.5)
        b5_l6 = Tex("Seasonality: the coast hires in December,").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        b5_l7 = Tex("retrenches in February — weigh both columns").scale(1.0).shift(band_shift(5) + DOWN * 3.2)
        self.play(Write(b5_l6))
        self.play(Write(b5_l7))
        self.wait(3)

        # --- Band 6 (subtopic_4): the shop window and IKS ---
        self.next_band(6)
        b6_title = Tex("South Africa's shop window").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Scenery and wildlife: Kruger, the Big Five;").scale(1.0).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("heritage: ten UNESCO sites, Robben Island;").scale(1.0).shift(band_shift(6) + UP * 0.7)
        b6_l3 = Tex("events and business (MICE); sunshine itself").scale(1.0).shift(band_shift(6))
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.play(Write(b6_l3))
        self.wait(3)
        b6_l4 = Tex("IKS: traditional medicine, San tracking and").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        b6_l5 = Tex("rock art, storytelling, beadwork, cuisine").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex("Two duties: AUTHENTICITY (owned by the").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        b6_l7 = Tex("community) and BENEFIT-SHARING").scale(1.0).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.play(Create(SurroundingRectangle(b6_l7, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): policy architecture and fixes ---
        self.next_band(7)
        b7_title = Tex("Policy: the architecture and the fixes").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("1996 White Paper: government leads, private").scale(1.0).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("sector delivers, communities benefit").scale(1.0).shift(band_shift(7) + UP * 0.7)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Tourism Act 2014; SA Tourism markets abroad;").scale(1.0).shift(band_shift(7) + DOWN * 0.2)
        b7_l4 = Tex("TOMSA levy (1\\%) funds it; NDP priority sector").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Fixes tied to obstacles: e-visas for China and").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        b7_l6 = Tex("India, visible policing, direct flights, training,").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        b7_l7 = Tex("spread beyond the Cape–Kruger corridor").scale(1.0).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.play(Write(b7_l7))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the export that walks in ---
        self.next_band(8)
        b8_title = Tex("The export that walks in").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Platinum: loaded on a ship, gone forever").scale(1.0).shift(band_shift(8) + UP * 1.5)
        b8_l2 = Tex("The Kruger: sold today, still here tomorrow").scale(1.0).shift(band_shift(8) + UP * 0.8)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Aunt in Durban: domestic — rands move inside").scale(1.0).shift(band_shift(8) + DOWN * 0.2)
        b8_l4 = Tex("German couple: inbound — new money, an export").scale(1.0).shift(band_shift(8) + DOWN * 0.9)
        b8_l5 = Tex("Cousin to Dubai: outbound — an import").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        for m in (b8_l3, b8_l4, b8_l5):
            self.play(Write(m))
            self.wait(1.8)
        b8_l6 = Tex("One holiday feeds six industries: hotel, taxi,").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        b8_l7 = Tex("park, craft stall, restaurant, guide").scale(1.0).shift(band_shift(8) + DOWN * 3.2)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): one busload, three rings ---
        self.next_band(9)
        b9_title = Tex("One busload, many pay packets").scale(1.2).shift(band_shift(9) + UP * 2.5)
        self.play(Write(b9_title))
        self.wait(2)
        r1 = Rectangle(width=3.4, height=1.2).shift(band_shift(9) + LEFT * 4.4 + UP * 1.2)
        r1_lab = Tex("DIRECT: lodge staff").scale(0.85).shift(band_shift(9) + LEFT * 4.4 + UP * 1.2)
        self.play(Create(r1), Write(r1_lab))
        a1 = Arrow(band_shift(9) + LEFT * 2.6 + UP * 1.2, band_shift(9) + LEFT * 1.8 + UP * 1.2, buff=0, stroke_width=4)
        r2 = Rectangle(width=3.4, height=1.2).shift(band_shift(9) + UP * 1.2)
        r2_lab = Tex("INDIRECT: suppliers").scale(0.85).shift(band_shift(9) + UP * 1.2)
        self.play(Create(a1), Create(r2), Write(r2_lab))
        a2 = Arrow(band_shift(9) + RIGHT * 1.8 + UP * 1.2, band_shift(9) + RIGHT * 2.6 + UP * 1.2, buff=0, stroke_width=4)
        r3 = Rectangle(width=3.4, height=1.2).shift(band_shift(9) + RIGHT * 4.4 + UP * 1.2)
        r3_lab = Tex("INDUCED: spaza, taxi").scale(0.85).shift(band_shift(9) + RIGHT * 4.4 + UP * 1.2)
        self.play(Create(a2), Create(r3), Write(r3_lab))
        self.wait(2.5)
        b9_l1 = Tex("The multiplier wearing khaki — three rings").scale(1.0).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l1))
        self.play(Create(SurroundingRectangle(b9_l1, color=GREEN)))
        self.wait(2)
        b9_l2 = Tex("Jobs of hands and hospitality: more employment").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        b9_l3 = Tex("per rand than mining; hires where nothing else does").scale(0.95).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("The leak: foreign-owned lodge, imported food,").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        b9_l5 = Tex("package paid in London — policy shouts LOCAL").scale(1.0).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): selling what only we have ---
        self.next_band(10)
        b10_title = Tex("Selling what only we have").scale(1.2).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Only here: Big Five wild, Table Mountain,").scale(1.0).shift(band_shift(10) + UP * 1.8)
        b10_l2 = Tex("Robben Island's cell — and living cultures").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("IKS rules: culture performed WITH people,").scale(1.0).shift(band_shift(10) + UP * 0.2)
        b10_l4 = Tex("not ABOUT them; the community banks the earnings").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("Obstacle-fix pairs: slow visas $\\rightarrow$ e-visas;").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        b10_l6 = Tex("crime fear $\\rightarrow$ visible policing; few flights").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        b10_l7 = Tex("$\\rightarrow$ direct routes; keeping power on IS marketing").scale(0.95).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.wait(2.5)
        b10_l8 = Tex("Grows as fast as the visit is easy, safe, shared").scale(1.0).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l8))
        self.play(Create(SurroundingRectangle(b10_l8, color=GREEN)))
        self.wait(4)
