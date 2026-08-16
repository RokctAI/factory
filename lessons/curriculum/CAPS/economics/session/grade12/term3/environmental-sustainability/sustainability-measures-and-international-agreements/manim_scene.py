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

# Band-layout whiteboard scene for the environmental-sustainability duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 235/235/250/255/190/195/195 of 1555 s — bands
# 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10 apportioned to match.
# All diagrams hand-built from Arrow/Line/Dot/Rectangle/Tex primitives.

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
        title = Tex("Environmental Sustainability").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Sustainable development (Brundtland, 1987):").scale(1.05).shift(UP * 1.4)
        d2 = Tex("meets the needs of the present WITHOUT").scale(1.05).shift(UP * 0.6)
        d3 = Tex("compromising future generations' ability").scale(1.05).shift(DOWN * 0.2)
        d4 = Tex("to meet their own needs").scale(1.05).shift(DOWN * 1.0)
        self.play(Write(d1))
        self.wait(1.5)
        self.play(Write(d2))
        self.play(Write(d3))
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(VGroup(d2, d3, d4), color=GREEN)))
        self.wait(2.5)
        d5 = Tex("Three legs: economic, social, environmental").scale(1.0).shift(DOWN * 2.0)
        d6 = Tex("Consuming natural capital = spending inheritance").scale(1.0).shift(DOWN * 2.8)
        self.play(Write(d5))
        self.wait(2)
        self.play(Write(d6))
        self.wait(3)

        # --- Band 1 (subtopic_1): three market failures ---
        self.next_band(1)
        b1_title = Tex("Why markets fail the environment").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("1. EXTERNALITIES: costs land outside the deal").scale(1.0).shift(band_shift(1) + UP * 1.5)
        b1_l2 = MathTex(r"\text{private cost} < \text{social cost} \Rightarrow \text{too cheap}").scale(0.87).shift(band_shift(1) + UP * 0.7)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("2. PUBLIC GOODS: non-excludable, non-rival —").scale(1.0).shift(band_shift(1) + DOWN * 0.2)
        b1_l4 = Tex("no one can charge, everyone free rides").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("3. NO PROPERTY RIGHTS: tragedy of the commons").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        b1_l6 = Tex("— what everybody owns, nobody protects").scale(1.0).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.wait(2)
        b1_l7 = Tex("Fix: price the unpriced, give the ownerless an owner").scale(0.95).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l7))
        self.play(Create(SurroundingRectangle(b1_l7, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): climate and water ---
        self.next_band(2)
        b2_title = Tex("The state of the environment I").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Climate: greenhouse gases trap heat;").scale(1.0).shift(band_shift(2) + UP * 1.5)
        b2_l2 = Tex("already warmed over 1°C since industrialisation").scale(1.0).shift(band_shift(2) + UP * 0.8)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("SA doubly exposed: coal-run economy (Eskom),").scale(1.0).shift(band_shift(2) + DOWN * 0.1)
        b2_l4 = Tex("region warming at nearly twice the global average").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = Tex("Water: rainfall about half the world average;").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        b2_l6 = Tex("acid drainage, sewage, drained wetlands").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(2)
        b2_l7 = Tex("Day Zero and the Durban floods: the local face").scale(1.0).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_l7))
        self.wait(3)

        # --- Band 3 (subtopic_2): air, land, waste — future GDP ---
        self.next_band(3)
        b3_title = Tex("The state of the environment II").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Air: Highveld coal-belt towns — asthma,").scale(1.0).shift(band_shift(3) + UP * 1.5)
        b3_l2 = Tex("lost work days: externalities with addresses").scale(1.0).shift(band_shift(3) + UP * 0.8)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Land and biodiversity: erosion, deforestation;").scale(1.0).shift(band_shift(3) + DOWN * 0.1)
        b3_l4 = Tex("biodiversity is economic capital — genes, tourism").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex("Waste: leaking landfills, plastic in rivers").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = Tex("Every item is future GDP draining away —").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        b3_l7 = Tex("unmanaged damage is a tax on all future growth").scale(1.0).shift(band_shift(3) + DOWN * 3.2)
        self.play(Write(b3_l6))
        self.play(Write(b3_l7))
        self.play(Create(SurroundingRectangle(b3_l7, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): command and control ---
        self.next_band(4)
        b4_title = Tex("Toolkit I: command and control").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Emission standards, zoning off wetlands,").scale(1.0).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("impact assessments, protected areas, quotas").scale(1.0).shift(band_shift(4) + UP * 0.7)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Strength: certainty where danger is acute").scale(1.0).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("Weaknesses: costly inspection; no reward").scale(1.0).shift(band_shift(4) + DOWN * 1.1)
        b4_l5 = Tex("beyond the minimum; uniform rule ignores").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        b4_l6 = Tex("that abatement costs differ across firms").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): market-based measures ---
        self.next_band(5)
        b5_title = Tex("Toolkit II: make the polluter pay").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Carbon tax (2019, Africa's first) per ton of CO$_2$;").scale(1.0).shift(band_shift(5) + UP * 1.5)
        b5_l2 = Tex("plastic-bag and tyre levies — pollute less, pay less").scale(1.0).shift(band_shift(5) + UP * 0.8)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Subsidies pull: solar rebates, renewables in the Karoo").scale(0.95).shift(band_shift(5))
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("Tradable permits: cap total, trade allowances —").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        b5_l5 = Tex("cap guarantees outcome, trade finds cheap cutters").scale(1.0).shift(band_shift(5) + DOWN * 1.5)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(2.5)
        b5_l6 = Tex("Property rights: conservancies, Working for Water").scale(1.0).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_l6))
        self.wait(2)
        b5_l7 = Tex("Commands set the floor; prices move the average").scale(1.0).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5_l7))
        self.play(Create(SurroundingRectangle(b5_l7, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): treaty ladder to 2002 ---
        self.next_band(6)
        b6_title = Tex("The treaty ladder I").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        tl = Arrow(band_shift(6) + LEFT * 6.0 + UP * 1.4, band_shift(6) + RIGHT * 6.0 + UP * 1.4,
                   buff=0, stroke_width=3)
        self.play(Create(tl))
        years = [("1987", -4.8), ("1992", -1.6), ("1997", 1.6), ("2002", 4.8)]
        for y, x in years:
            d = Dot(band_shift(6) + RIGHT * x + UP * 1.4, color=YELLOW)
            lab = Tex(y).scale(0.9).next_to(band_shift(6) + RIGHT * x + UP * 1.4, UP, buff=0.2)
            self.play(Create(d), Write(lab), run_time=0.7)
        self.wait(1.5)
        b6_l1 = Tex("Montreal 1987: CFCs out, ozone healing —").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l2 = Tex("the most successful environmental treaty ever").scale(1.0).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Rio 1992: Agenda 21, biodiversity, UNFCCC —").scale(1.0).shift(band_shift(6) + DOWN * 1.1)
        b6_l4 = Tex("common but differentiated responsibilities").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Kyoto 1997: binding, rich only — coverage shrank").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        b6_l6 = Tex("Johannesburg 2002: implementation and poverty").scale(1.0).shift(band_shift(6) + DOWN * 3.3)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): Paris, the COPs, and the JETP ---
        self.next_band(7)
        b7_title = Tex("The treaty ladder II: Paris and after").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Paris 2015: every nation sets NDCs, tightened").scale(1.0).shift(band_shift(7) + UP * 1.5)
        b7_l2 = Tex("over time — well below 2°C, pursue 1,5°C").scale(1.0).shift(band_shift(7) + UP * 0.8)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Universal where Kyoto was partial; voluntary").scale(1.0).shift(band_shift(7))
        b7_l4 = Tex("where Kyoto was binding — strength AND weakness").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l5 = Tex("Glasgow 2021: phase DOWN coal; Sharm 2022:").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        b7_l6 = Tex("loss-and-damage fund; Dubai 2023: stocktake").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(2.5)
        b7_l7 = Tex("SA's JETP: \\$8,5 bn pledged for a JUST transition").scale(1.0).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l7))
        self.play(Create(SurroundingRectangle(b7_l7, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the river nobody owns ---
        self.next_band(8)
        b8_title = Tex("The river nobody owns").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        f_rect = Rectangle(width=3.4, height=1.3).shift(band_shift(8) + LEFT * 4.4 + UP * 1.2)
        f_lab = Tex("Factory").scale(1.0).shift(band_shift(8) + LEFT * 4.4 + UP * 1.2)
        self.play(Create(f_rect), Write(f_lab))
        river = Arrow(band_shift(8) + LEFT * 2.6 + UP * 1.2, band_shift(8) + RIGHT * 2.6 + UP * 1.2,
                      buff=0, stroke_width=5, color=BLUE)
        r_lab = Tex("the river").scale(0.9).next_to(band_shift(8) + UP * 1.2, UP, buff=0.25)
        self.play(Create(river), Write(r_lab))
        v_rect = Rectangle(width=3.4, height=1.3).shift(band_shift(8) + RIGHT * 4.4 + UP * 1.2)
        v_lab = Tex("Village").scale(1.0).shift(band_shift(8) + RIGHT * 4.4 + UP * 1.2)
        self.play(Create(v_rect), Write(v_lab))
        self.wait(2)
        b8_l1 = Tex("Dead fish, boiled water, clinic queues —").scale(1.0).shift(band_shift(8) + UP * 0.1)
        b8_l2 = Tex("real rand costs, outside the factory's books").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("No owner to send the bill: the commons tragedy").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8_l4 = Tex("Fresh air can't be fenced: the free rider waits").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Diagnosis: the damage is priced at ZERO").scale(1.05).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): sending the river a bill ---
        self.next_band(9)
        b9_title = Tex("Sending the river a bill: four tags").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("1. The RULE: chief bans dumping — but the").scale(1.0).shift(band_shift(9) + UP * 1.5)
        b9_l2 = Tex("inspector must keep coming back").scale(1.0).shift(band_shift(9) + UP * 0.8)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("2. The TAX: charge per litre — the factory's own").scale(1.0).shift(band_shift(9))
        b9_l4 = Tex("accountant now polices the pipe, all year").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("3. The REWARD: solar rebates — subsidy pulls").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("4. The OWNER: a springbok that pays school").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        b9_l7 = Tex("fees is guarded, not poached — mix all four").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.play(Create(SurroundingRectangle(b9_l7, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): promises between countries ---
        self.next_band(10)
        b10_title = Tex("Promises between countries").scale(1.2).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Montreal 1987 worked completely — keep it").scale(1.0).shift(band_shift(10) + UP * 1.8)
        b10_l2 = Tex("in your pocket against the cynics").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Rio wrote the constitution; Kyoto set homework").scale(1.0).shift(band_shift(10) + UP * 0.3)
        b10_l4 = Tex("for the rich only; Paris: everyone writes their own").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("COPs since: phase down coal, loss-and-damage").scale(1.0).shift(band_shift(10) + DOWN * 1.2)
        b10_l6 = Tex("fund, move away from fossil fuels").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(2.5)
        b10_l7 = Tex("JUST transition: retrain coal workers, new").scale(1.0).shift(band_shift(10) + DOWN * 2.6)
        b10_l8 = Tex("industries for coal towns, lights kept on").scale(1.0).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l7))
        self.play(Write(b10_l8))
        self.play(Create(SurroundingRectangle(b10_l8, color=GREEN)))
        self.wait(4)
