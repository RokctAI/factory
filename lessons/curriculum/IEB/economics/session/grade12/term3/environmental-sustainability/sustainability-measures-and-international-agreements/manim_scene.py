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

# Band-layout whiteboard scene for the environmental-sustainability duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 235/235/250/255/190/195/195 of 1555 s — bands
# 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10 apportioned to match.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SustainabilityMeasuresAgreementsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the Brundtland definition ---
        title = Tex("Environmental Sustainability").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Sustainable development (Brundtland, 1987):").scale(1.0).shift(UP * 1.4)
        d2 = Tex("meet the needs of the PRESENT without").scale(1.05).shift(UP * 0.6)
        d3 = Tex("compromising FUTURE generations' needs").scale(1.05).shift(DOWN * 0.2)
        self.play(Write(d1))
        self.play(Write(d2))
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(VGroup(d2, d3), color=GREEN)))
        self.wait(2.5)
        d4 = Tex("Three legs: economic, social, environmental").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(d4))
        self.wait(2)
        d5 = Tex("Nature is CAPITAL: growth that consumes it").scale(1.0).shift(DOWN * 2.1)
        d6 = Tex("is spending inheritance, not earning income").scale(1.0).shift(DOWN * 2.8)
        self.play(Write(d5))
        self.play(Write(d6))
        self.wait(3)

        # --- Band 1 (subtopic_1): three market failures ---
        self.next_band(1)
        b1_title = Tex("Three ways the market fails the environment").scale(1.05).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("1. EXTERNALITIES: the tannery's biggest cost").scale(1.0).shift(band_shift(1) + UP * 1.4)
        b1_l2 = MathTex(r"\text{private cost} < \text{social cost} \Rightarrow \text{overproduction}").scale(0.95).shift(band_shift(1) + UP * 0.6)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("2. PUBLIC GOODS: non-excludable, non-rival —").scale(1.0).shift(band_shift(1) + DOWN * 0.3)
        b1_l4 = Tex("unsellable, so everyone FREE RIDES").scale(1.0).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("3. NO PROPERTY RIGHTS: the unowned abalone bed").scale(0.97).shift(band_shift(1) + DOWN * 1.9)
        b1_l6 = Tex("raced to zero — what all own, none protects").scale(1.0).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): climate and water ---
        self.next_band(2)
        b2_title = Tex("The state of the environment, part one").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Climate: $>1^{\\circ}$C warming since industrialisation").scale(0.97).shift(band_shift(2) + UP * 1.4)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("SA doubly exposed: coal-heavy grid, and the").scale(1.0).shift(band_shift(2) + UP * 0.5)
        b2_l3 = Tex("region warming at $\\sim$twice the global average").scale(1.0).shift(band_shift(2) + DOWN * 0.2)
        self.play(Write(b2_l2))
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(VGroup(b2_l2, b2_l3), color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Water: $\\sim$half world-average rainfall; rivers carry").scale(0.95).shift(band_shift(2) + DOWN * 1.2)
        b2_l5 = Tex("mine acid, sewage, runoff; wetlands drained").scale(0.97).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): air, land, waste — future GDP ---
        self.next_band(3)
        b3_title = Tex("The state of the environment, part two").scale(1.1).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Air: Highveld coal belt among world's dirtiest —").scale(0.97).shift(band_shift(3) + UP * 1.4)
        b3_l2 = Tex("asthma, lost work days: externalities with addresses").scale(0.92).shift(band_shift(3) + UP * 0.7)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Land and biodiversity: erosion, deforestation,").scale(1.0).shift(band_shift(3) + DOWN * 0.2)
        b3_l4 = Tex("species loss — the asset register shrinking").scale(1.0).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex("Waste: leaking landfills, plastic in every river").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = Tex("Every entry $=$ future GDP leaking away").scale(1.05).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): command and control ---
        self.next_band(4)
        b4_title = Tex("Toolkit I: command and control").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Emission standards, EIAs before development,").scale(1.0).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("zoning off wetlands, protected areas, quotas").scale(1.0).shift(band_shift(4) + UP * 0.7)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Strength: certainty where poison is acute —").scale(1.0).shift(band_shift(4) + DOWN * 0.2)
        b4_l4 = Tex("what kills gets banned, not taxed").scale(1.0).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex("Weakness: costly inspection, no reward for").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        b4_l6 = Tex("beating the minimum, one rule for unequal firms").scale(0.97).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): market-based measures ---
        self.next_band(5)
        b5_title = Tex("Toolkit II: price the externality").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("TAX: carbon tax (2019, Africa's first), bag and").scale(0.97).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("tyre levies — pollute less, pay less, all year").scale(0.97).shift(band_shift(5) + UP * 0.7)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("SUBSIDY: solar rebates, renewable procurement").scale(0.97).shift(band_shift(5) + DOWN * 0.2)
        b5_l4 = Tex("PERMITS: cap total, trade allowances — cap").scale(1.0).shift(band_shift(5) + DOWN * 1.0)
        b5_l5 = Tex("guarantees outcome, trade finds cheapest cuts").scale(0.97).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(2.5)
        b5_l6 = Tex("OWNERSHIP: conservancies; Working for Water —").scale(0.97).shift(band_shift(5) + DOWN * 2.6)
        b5_l7 = Tex("the village becomes the river's paid bodyguard").scale(0.97).shift(band_shift(5) + DOWN * 3.3)
        self.play(Write(b5_l6))
        self.play(Write(b5_l7))
        self.wait(3)

        # --- Band 6 (subtopic_4): treaty ladder to 2002 ---
        self.next_band(6)
        b6_title = Tex("The treaty ladder, first rungs").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Montreal 1987: CFCs phased out, ozone healing —").scale(0.97).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("the existence proof of cooperation").scale(1.0).shift(band_shift(6) + UP * 0.7)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex("Rio 1992: Agenda 21 $+$ biodiversity convention").scale(0.97).shift(band_shift(6) + DOWN * 0.2)
        b6_l4 = Tex("$+$ UNFCCC — common but differentiated duties").scale(0.97).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Kyoto 1997: binding, but rich-only — curve unmoved").scale(0.92).shift(band_shift(6) + DOWN * 1.8)
        b6_l6 = Tex("Johannesburg 2002: implementation, poverty links").scale(0.92).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): Paris, the COPs, and the JETP ---
        self.next_band(7)
        b7_title = Tex("Paris and after").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Paris 2015: every nation pledges NDCs, ratcheted").scale(0.95).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("over time — universal but voluntary: strength").scale(0.97).shift(band_shift(7) + UP * 0.7)
        b7_l3 = Tex("and weakness in one design").scale(1.0).shift(band_shift(7))
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Glasgow 2021: coal phase-down. Sharm el-Sheikh").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        b7_l5 = Tex("2022: loss-and-damage fund. Dubai 2023: stocktake").scale(0.92).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(2.5)
        b7_l6 = Tex("JETP: 8,5 billion dollars to decarbonise SA").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        b7_l7 = Tex("JUSTLY — workers retrained, towns renewed").scale(1.0).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_l6))
        self.play(Write(b7_l7))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the river nobody owns ---
        self.next_band(8)
        b8_title = Tex("The river nobody owns").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Kiln upstream: pipe pays nothing. Village").scale(1.0).shift(band_shift(8) + UP * 1.5)
        b8_l2 = Tex("downstream: boiled water, empty traps, clinic queue").scale(0.92).shift(band_shift(8) + UP * 0.8)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("The biggest cost sits outside the kiln's books:").scale(1.0).shift(band_shift(8) + DOWN * 0.1)
        b8_l4 = Tex("an EXTERNALITY, real and payable in rands").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2.5)
        b8_l5 = Tex("The garden has an owner; the river has none.").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        b8_l6 = Tex("Free riders sink the chimney collection.").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        b8_l7 = Tex("Diagnosis: the damage is priced at ZERO").scale(1.0).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): sending the river a bill ---
        self.next_band(9)
        b9_title = Tex("Sending the river a bill: four tags").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("RULE: ban, fine, inspect — certain but blunt").scale(0.97).shift(band_shift(9) + UP * 1.5)
        b9_l2 = Tex("TAX: charge per barrel — the bookkeeper").scale(0.97).shift(band_shift(9) + UP * 0.7)
        b9_l3 = Tex("polices the pipe, every day, forever").scale(0.97).shift(band_shift(9))
        self.play(Write(b9_l1))
        self.wait(1.5)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("REWARD: rebates and contracts pull the new").scale(0.97).shift(band_shift(9) + DOWN * 0.9)
        b9_l5 = Tex("OWNER: the antelope that pays school fees").scale(0.97).shift(band_shift(9) + DOWN * 1.7)
        b9_l6 = Tex("is the antelope the whole village guards").scale(0.97).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(2)
        b9_l7 = Tex("Mix them: ban, tax, reward, own").scale(1.0).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l7))
        self.wait(3)

        # --- Band 10 (subtopic_7): promises between countries ---
        self.next_band(10)
        b10_title = Tex("Promises between countries").scale(1.2).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("The sky is the biggest shared river —").scale(1.0).shift(band_shift(10) + UP * 1.7)
        b10_l2 = Tex("free riding at the scale of nations").scale(1.0).shift(band_shift(10) + UP * 1.0)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Montreal worked. Kyoto: homework for the rich").scale(0.97).shift(band_shift(10) + UP * 0.1)
        b10_l4 = Tex("only — curve unmoved. Paris: everyone writes").scale(0.97).shift(band_shift(10) + DOWN * 0.6)
        b10_l5 = Tex("their own promise, and must tighten it").scale(0.97).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex("SA the test case: 8,5 billion dollars, one").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        b10_l7 = Tex("condition — the transition must be JUST").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.play(Create(SurroundingRectangle(b10_l7, color=GREEN)))
        self.wait(4)
