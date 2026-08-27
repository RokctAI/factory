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

# Band-layout whiteboard scene for the industrial-and-regional-development duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 230/235/245/245/190/195/190 of 1530 s — bands
# 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10 apportioned to match.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IndustrialRegionalDevelopmentSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the value chain ---
        title = Tex("Industrial and Regional Development").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        v1 = Tex("chrome ore $\\rightarrow$ ferrochrome $\\rightarrow$ stainless").scale(1.0).shift(UP * 1.3)
        v2 = Tex("steel $\\rightarrow$ finished instruments").scale(1.0).shift(UP * 0.6)
        self.play(Write(v1))
        self.play(Write(v2))
        self.wait(2.5)
        v3 = Tex("Each stage keeps wages, profits, taxes —").scale(1.0).shift(DOWN * 0.3)
        v4 = Tex("that is VALUE ADDED").scale(1.05).shift(DOWN * 1.0)
        self.play(Write(v3))
        self.play(Write(v4))
        self.play(Create(SurroundingRectangle(v4, color=GREEN)))
        self.wait(2.5)
        v5 = Tex("BENEFICIATION: do the stages at home —").scale(1.0).shift(DOWN * 2.0)
        v6 = Tex("export the instrument tray, not the ore").scale(1.0).shift(DOWN * 2.7)
        self.play(Write(v5))
        self.play(Write(v6))
        self.wait(3)

        # --- Band 1 (subtopic_1): four arguments and the caution ---
        self.next_band(1)
        b1_title = Tex("Why industrialise deliberately?").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("1. Value added stays home").scale(1.0).shift(band_shift(1) + UP * 1.5)
        b1_l2 = Tex("2. Factories absorb semi-skilled labour").scale(1.0).shift(band_shift(1) + UP * 0.8)
        b1_l3 = Tex("3. Diversification smooths commodity swings").scale(1.0).shift(band_shift(1) + UP * 0.1)
        b1_l4 = Tex("4. Linkages: backward to suppliers,").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        b1_l5 = Tex("forward to dealers — one plant, hundreds of firms").scale(0.95).shift(band_shift(1) + DOWN * 1.3)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4, b1_l5):
            self.play(Write(m))
            self.wait(1.6)
        b1_l6 = Tex("Caution: an infant kept on support forever").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        b1_l7 = Tex("becomes comfortable, never competitive").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.play(Create(SurroundingRectangle(b1_l7, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the named strategies ---
        self.next_band(2)
        b2_title = Tex("The named strategies").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("NIPF 2007 $\\rightarrow$ rolling IPAPs: pick priority").scale(1.0).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("sectors, back them with targeted support").scale(1.0).shift(band_shift(2) + UP * 0.7)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("APDP: duty credits for producing and investing —").scale(0.95).shift(band_shift(2) + DOWN * 0.2)
        b2_l4 = Tex("seven global carmakers assemble here").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)
        b2_l5 = Tex("Clothing programme; 12I allowances; Black").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        b2_l6 = Tex("Industrialists Scheme; IDC patient finance").scale(1.0).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): localisation and the headwinds ---
        self.next_band(3)
        b3_title = Tex("Localisation, and the honest headwinds").scale(1.1).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Designated procurement: the state must buy").scale(1.0).shift(band_shift(3) + UP * 1.4)
        b3_l2 = Tex("buses, rail stock, cables, uniforms locally").scale(1.0).shift(band_shift(3) + UP * 0.7)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("NDP goal: lift manufacturing's share of").scale(1.0).shift(band_shift(3) + DOWN * 0.2)
        b3_l4 = Tex("output and jobs; grow small suppliers").scale(1.0).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex("Headwinds: costly failing power, port and rail").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        b3_l6 = Tex("bottlenecks, scarce skills, Asian scale —").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        b3_l7 = Tex("paper strategies must survive load-shedding").scale(1.0).shift(band_shift(3) + DOWN * 3.2)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.play(Write(b3_l7))
        self.wait(3)

        # --- Band 4 (subtopic_3): clumping, the homeland lesson, the corridor ---
        self.next_band(4)
        b4_title = Tex("Regional development: the counter-pull").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Industry clumps: Gauteng $\\sim$2\\% of land,").scale(1.0).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("$\\sim\\tfrac{1}{3}$ of output — factories follow factories").scale(1.0).shift(band_shift(4) + UP * 0.6)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Homeland decentralisation: paid to arrive,").scale(1.0).shift(band_shift(4) + DOWN * 0.3)
        b4_l4 = Tex("died when payments stopped").scale(1.0).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.play(Create(strike(b4_l4)))
        self.wait(2.5)
        b4_l5 = Tex("Maputo Corridor: N4 $+$ rail $+$ border upgrades,").scale(0.97).shift(band_shift(4) + DOWN * 1.9)
        b4_l6 = Tex("Gauteng to a closer port — a whole line of towns").scale(0.95).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the SEZ toolkit ---
        self.next_band(5)
        b5_title = Tex("Special economic zones (SEZ Act, 2014)").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Serviced precinct at a port or airport, plus:").scale(1.0).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("15\\% company tax, building allowances,").scale(1.0).shift(band_shift(5) + UP * 0.7)
        b5_l3 = Tex("employment incentives, duty-free export inputs").scale(0.97).shift(band_shift(5))
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex("Coega (Ngqura, largest); East London (vehicles);").scale(0.92).shift(band_shift(5) + DOWN * 1.0)
        b5_l5 = Tex("Richards Bay (metals); Dube TradePort (air cargo);").scale(0.92).shift(band_shift(5) + DOWN * 1.7)
        b5_l6 = Tex("Saldanha (oil and gas); Tshwane (automotive)").scale(0.92).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): best practice and results ---
        self.next_band(6)
        b6_title = Tex("Judging: the test, then the scoreboard").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Best practice: tie support to EXPORTS, keep it").scale(0.97).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("TEMPORARY, invest in skills and infrastructure").scale(0.97).shift(band_shift(6) + UP * 0.7)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Wins: APDP passes the export test; Coega and").scale(0.97).shift(band_shift(6) + DOWN * 0.2)
        b6_l4 = Tex("Dube TradePort hold real tenants and cargo").scale(0.97).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Failures: manufacturing's GDP share").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        b6_l6 = MathTex(r"19\%+ \;\rightarrow\; 12\text{--}13\% \;\; \text{(deindustrialisation)}").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): constraints, cost, verdict ---
        self.next_band(7)
        b7_title = Tex("Constraints, cost, verdict").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Binding constraints: no incentive outbids a").scale(1.0).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("power cut, a queuing port, a broken railway").scale(1.0).shift(band_shift(7) + UP * 0.7)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("Cost test: rands per SUSTAINABLE job —").scale(1.0).shift(band_shift(7) + DOWN * 0.3)
        b7_l4 = Tex("permanent subsidy $=$ the homeland mistake rebranded").scale(0.92).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Verdict: flagships deliver, foundations crumble —").scale(0.95).shift(band_shift(7) + DOWN * 1.9)
        b7_l6 = Tex("fix the constraints so incentives can bite").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the bakkie and the bag of ore ---
        self.next_band(8)
        b8_title = Tex("The bakkie and the bag of ore").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Bag of ore: a few hundred rand, digging wages").scale(0.97).shift(band_shift(8) + UP * 1.5)
        b8_l2 = Tex("Bakkie: hundreds of thousands — with every").scale(0.97).shift(band_shift(8) + UP * 0.8)
        b8_l3 = Tex("maker's wage, profit and tax folded inside").scale(0.97).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l1))
        self.wait(1.5)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Dig only, and you sell the cheapest link,").scale(1.0).shift(band_shift(8) + DOWN * 0.9)
        b8_l5 = Tex("then buy back the dearest one").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("And help needs a finish line: support the infant").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        b8_l7 = Tex("to grow up, never to stay an infant").scale(1.0).shift(band_shift(8) + DOWN * 3.2)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): why the factory went to Coega ---
        self.next_band(9)
        b9_title = Tex("Why the factory went to Coega").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Factories follow factories — so the state").scale(1.0).shift(band_shift(9) + UP * 1.5)
        b9_l2 = Tex("builds foundations, then sweetens the sums:").scale(1.0).shift(band_shift(9) + UP * 0.8)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("deep-water port, serviced land, 15\\% tax,").scale(1.0).shift(band_shift(9))
        b9_l4 = Tex("hiring breaks, duty-free inputs for exporters").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("A corridor is a road-shaped sweetener: the N4").scale(0.97).shift(band_shift(9) + DOWN * 1.6)
        b9_l6 = Tex("woke a whole line of towns to Maputo").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(2)
        b9_l7 = Tex("Paid to ARRIVE anywhere; STAYS only where it works").scale(0.92).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9_l7))
        self.wait(3)

        # --- Band 10 (subtopic_7): marking the government's homework ---
        self.next_band(10)
        b10_title = Tex("Marking the government's homework").scale(1.15).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("1. State the test: exports, temporary, foundations").scale(0.95).shift(band_shift(10) + UP * 1.7)
        b10_l2 = Tex("2. Wins by name: cars, Coega, Dube, the N4").scale(0.97).shift(band_shift(10) + UP * 1.0)
        b10_l3 = Tex("3. Failures by name: share shrunk to an eighth,").scale(0.95).shift(band_shift(10) + UP * 0.3)
        b10_l4 = Tex("clothing jobs, zones without tenants").scale(0.97).shift(band_shift(10) + DOWN * 0.4)
        for m in (b10_l1, b10_l2, b10_l3, b10_l4):
            self.play(Write(m))
            self.wait(1.6)
        b10_l5 = Tex("4. The bottleneck: no sweetener outbids a").scale(0.97).shift(band_shift(10) + DOWN * 1.3)
        b10_l6 = Tex("power cut — fix power, rail, ports, training").scale(0.97).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(2)
        b10_l7 = Tex("Verdict: right direction, crumbling foundations").scale(0.97).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l7))
        self.wait(4)
