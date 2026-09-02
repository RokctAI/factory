# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene for the session duo "Environmental
# Deterioration and Sustainability" (Grade 11, Term 4, IEB catalogue). One
# band per teaching step; the camera moves down and nothing is removed.
# Exporter-safe mobjects only; the tannery externality diagram is hand-built
# from Rectangles and Arrows. Band time apportioned to subtopics.json
# (240/255/250/245/205/205/210 of 1610 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class EnvironmentalSustainabilitySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): externalities — the tannery diagram ---
        title = Tex("Why Markets Fail the Environment").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        tan = Rectangle(width=3.2, height=1.1).shift(LEFT * 4.2 + UP * 0.9)
        tan_lab = Tex("Tannery").scale(0.75).move_to(tan.get_center())
        buyer = Rectangle(width=3.2, height=1.1).shift(RIGHT * 4.2 + UP * 0.9)
        buyer_lab = Tex("Leather buyer").scale(0.75).move_to(buyer.get_center())
        self.play(Create(tan), Write(tan_lab))
        self.play(Create(buyer), Write(buyer_lab))
        a1 = Arrow(tan.get_right(), buyer.get_left(), buff=0.1)
        a1_lab = Tex("every rand accounted for").scale(0.7).shift(UP * 1.6)
        self.play(Create(a1), Write(a1_lab))
        self.wait(2)
        farm = Rectangle(width=3.6, height=1.1).shift(LEFT * 4.2 + DOWN * 1.1)
        farm_lab = Tex("Farmers downstream").scale(0.65).move_to(farm.get_center())
        a2 = Arrow(tan.get_bottom(), farm.get_top(), buff=0.1, color=RED)
        a2_lab = Tex("effluent: price zero").scale(0.7).shift(LEFT * 1.5 + DOWN * 0.1)
        self.play(Create(farm), Write(farm_lab))
        self.play(Create(a2), Write(a2_lab))
        self.wait(2.5)
        e1 = Tex("EXTERNALITY: a cost on someone outside the deal").scale(0.9).shift(DOWN * 2.1)
        self.play(Write(e1))
        self.play(Create(SurroundingRectangle(e1, color=GREEN)))
        self.wait(2)
        e2 = Tex("Sold too cheap, made in too great a quantity").scale(0.9).shift(DOWN * 3.0)
        self.play(Write(e2))
        self.wait(3)

        # --- Band 1 (subtopic_1): commons, missing future, SA case file ---
        self.next_band(1)
        b1_title = Tex("The commons, and the missing voters").scale(1.1).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        c1 = Tex("Common resources: open to all, owned by none").scale(0.95).shift(band_shift(1) + UP * 1.4)
        c2 = Tex("Each user keeps the gain; depletion is shared").scale(0.95).shift(band_shift(1) + UP * 0.55)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        c3 = Tex("Whatever belongs to everybody is protected by nobody").scale(0.9).shift(band_shift(1) + DOWN * 0.35)
        self.play(Write(c3))
        self.play(Create(SurroundingRectangle(c3, color=GREEN)))
        self.wait(2.5)
        c4 = Tex("A child needing water in 2070 casts no vote today").scale(0.9).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(c4))
        self.wait(2)
        c5 = Tex("SA case file: Vaal sewage, overstocked rangelands,").scale(0.85).shift(band_shift(1) + DOWN * 2.2)
        c6 = Tex("stripped abalone reefs, coal-heavy emissions per person").scale(0.8).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(c5))
        self.play(Write(c6))
        self.wait(3)

        # --- Band 2 (subtopic_2): toolbox — rules and prices ---
        self.next_band(2)
        b2_title = Tex("The policy toolbox: rules and prices").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        t1 = Tex("1. Command and control: emission ceilings, EIAs,").scale(0.9).shift(band_shift(2) + UP * 1.4)
        t1b = Tex("quotas, protected areas — a legal ceiling is a ceiling").scale(0.85).shift(band_shift(2) + UP * 0.6)
        self.play(Write(t1))
        self.play(Write(t1b))
        self.wait(2.5)
        t2 = Tex("A standard without inspectors is a press release").scale(0.9).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(t2))
        self.wait(2)
        t3 = Tex("2. Market-based: carbon tax, bag levy, tyre levy —").scale(0.9).shift(band_shift(2) + DOWN * 1.2)
        t3b = Tex("the tax replaces the zero with a number").scale(0.9).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(t3))
        self.play(Write(t3b))
        self.wait(2.5)
        t4 = Tex("Plus clean subsidies, and permits traded under a cap").scale(0.85).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(t4))
        self.wait(3)

        # --- Band 3 (subtopic_2): owners, treaties, evaluation ---
        self.next_band(3)
        b3_title = Tex("Owners, treaties — and the evaluation").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        o1 = Tex("3. Property rights: community fishing rights,").scale(0.85).shift(band_shift(3) + UP * 1.4)
        o1b = Tex("restitution parks — next decade's value is the owner's").scale(0.85).shift(band_shift(3) + UP * 0.6)
        self.play(Write(o1))
        self.play(Write(o1b))
        self.wait(2.5)
        o2 = Tex("4. International agreements: Paris — nobody").scale(0.85).shift(band_shift(3) + DOWN * 0.3)
        o2b = Tex("cuts alone, so nobody free-rides for long").scale(0.85).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(o2))
        self.play(Write(o2b))
        self.wait(2.5)
        o3 = Tex("Rules: certain, admin-hungry. Taxes: efficient,").scale(0.8).shift(band_shift(3) + DOWN * 2.0)
        o3b = Tex("regressive. Permits: cheap cuts. Treaties: weak teeth.").scale(0.8).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(o3))
        self.play(Write(o3b))
        self.play(Create(SurroundingRectangle(VGroup(o3, o3b), color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): sustainability — interest, not capital ---
        self.next_band(4)
        b4_title = Tex("Sustainability: live off the interest").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        s1 = Tex("Brundtland: meet present needs without compromising").scale(0.85).shift(band_shift(4) + UP * 1.4)
        s1b = Tex("future generations' ability to meet their own").scale(0.85).shift(band_shift(4) + UP * 0.6)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.play(Create(SurroundingRectangle(VGroup(s1, s1b), color=GREEN)))
        self.wait(2.5)
        s2 = Tex("Nature is CAPITAL: intact stock, income forever").scale(0.9).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(s2))
        self.wait(2)
        s3 = Tex("Renewables have a critical rate: below it, immortal;").scale(0.85).shift(band_shift(4) + DOWN * 1.3)
        s3b = Tex("above it, the renewable dies like a mined-out seam").scale(0.85).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(s3))
        self.play(Write(s3b))
        self.wait(2.5)
        s4 = Tex("Coal and platinum: spend once — build lasting assets").scale(0.8).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(s4))
        self.wait(3)

        # --- Band 5 (subtopic_3): the pillars and the just transition ---
        self.next_band(5)
        b5_title = Tex("Three pillars, and the just transition").scale(1.1).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        p1 = Tex("Environmental: keep the natural stocks alive").scale(0.95).shift(band_shift(5) + UP * 1.4)
        p2 = Tex("Economic: keep production and jobs running").scale(0.95).shift(band_shift(5) + UP * 0.55)
        p3 = Tex("Social: distribute costs and benefits justly").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        for m in (p1, p2, p3):
            self.play(Write(m))
            self.wait(1.8)
        self.play(Create(SurroundingRectangle(VGroup(p1, p2, p3), color=GREEN)))
        self.wait(2)
        p4 = Tex("Remove any pillar and the structure fails").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(p4))
        self.wait(2)
        p5 = Tex("Just transition: build clean energy at speed WHILE").scale(0.9).shift(band_shift(5) + DOWN * 2.2)
        p5b = Tex("retraining workers and reindustrialising coal regions").scale(0.85).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(p5))
        self.play(Write(p5b))
        self.wait(3)

        # --- Band 6 (subtopic_4): the warming mechanism and local evidence ---
        self.next_band(6)
        b6_title = Tex("The mechanism, and the evidence at home").scale(1.1).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        w1 = Tex(r"Fossil fuels $\to$ greenhouse gases $\to$ trapped heat").scale(0.9).shift(band_shift(6) + UP * 1.4)
        w2 = Tex(r"$\to$ 1$^{\circ}$C$+$ warming $\to$ deeper droughts, harder rain").scale(0.85).shift(band_shift(6) + UP * 0.55)
        self.play(Write(w1))
        self.wait(2)
        self.play(Write(w2))
        self.wait(2.5)
        w3 = Tex("North: two centuries of emissions built the wealth").scale(0.85).shift(band_shift(6) + DOWN * 0.35)
        w3b = Tex("South: a few percent of emissions, the earliest damage").scale(0.85).shift(band_shift(6) + DOWN * 1.15)
        self.play(Write(w3))
        self.play(Write(w3b))
        self.wait(2.5)
        w4 = Tex("KZN floods, April 2022: 400+ lives, billions lost").scale(0.85).shift(band_shift(6) + DOWN * 2.05)
        w5 = Tex("2016 drought: a maize exporter forced to import grain").scale(0.85).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(w4))
        self.wait(2)
        self.play(Write(w5))
        self.wait(3)

        # --- Band 7 (subtopic_4): trade exposure and the response file ---
        self.next_band(7)
        b7_title = Tex("Triple exposure — and the response file").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        x1 = Tex("Carbon border charges: coal-made exports pay").scale(0.9).shift(band_shift(7) + UP * 1.4)
        x2 = Tex("a climate penalty at the customer's customs post").scale(0.9).shift(band_shift(7) + UP * 0.55)
        self.play(Write(x1))
        self.wait(2)
        self.play(Write(x2))
        self.wait(2.5)
        x3 = Tex("Response: Paris commitments, carbon tax, record-cheap").scale(0.8).shift(band_shift(7) + DOWN * 0.35)
        x3b = Tex("wind and solar auctions, the JET Partnership billions").scale(0.8).shift(band_shift(7) + DOWN * 1.15)
        self.play(Write(x3))
        self.play(Write(x3b))
        self.wait(2.5)
        x4 = Tex("Polluter, victim, coal-dependent exporter —").scale(0.85).shift(band_shift(7) + DOWN * 2.1)
        x4b = Tex("sustainability here is solvency").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(x4))
        self.play(Write(x4b))
        self.play(Create(SurroundingRectangle(x4b, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the smoke nobody pays for ---
        self.next_band(8)
        b8_title = Tex("The smoke nobody pays for").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        v1 = Tex("Smelter: builders pay, owner pays — the township coughs").scale(0.8).shift(band_shift(8) + UP * 1.4)
        v2 = Tex("An unposted bill: the externality").scale(0.9).shift(band_shift(8) + UP * 0.55)
        self.play(Write(v1))
        self.wait(2)
        self.play(Write(v2))
        self.wait(2.5)
        v3 = Tex("Rods too cheap, furnace runs longer, ash falls thicker").scale(0.8).shift(band_shift(8) + DOWN * 0.35)
        self.play(Write(v3))
        self.wait(2)
        v4 = Tex("The shared field: forty sensible families, one dust bowl").scale(0.8).shift(band_shift(8) + DOWN * 1.25)
        self.play(Write(v4))
        self.wait(2)
        v5 = Tex("And the girl of 2070 buys nothing today: price zero").scale(0.85).shift(band_shift(8) + DOWN * 2.15)
        self.play(Write(v5))
        self.play(Create(SurroundingRectangle(v5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): putting a price on the smoke ---
        self.next_band(9)
        b9_title = Tex("Putting a price on the smoke: four cures").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        f1 = Tex("1. Limits with consequences — else a polite notice").scale(0.85).shift(band_shift(9) + UP * 1.4)
        f2 = Tex("2. Deliver the bill: bag levy, carbon tax").scale(0.9).shift(band_shift(9) + UP * 0.55)
        f3 = Tex("3. Appoint an owner: grazing committee, abalone rights").scale(0.8).shift(band_shift(9) + DOWN * 0.3)
        f4 = Tex("4. Sign with the neighbours: Paris, together").scale(0.9).shift(band_shift(9) + DOWN * 1.15)
        for m in (f1, f2, f3, f4):
            self.play(Write(m))
            self.wait(1.9)
        f5 = Tex("Priced smoke turns self-interest into the cleaner").scale(0.9).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(f5))
        self.play(Create(SurroundingRectangle(f5, color=GREEN)))
        self.wait(2)
        f6 = Tex("No cure is complete — real protection stacks all four").scale(0.85).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(f6))
        self.wait(3)

        # --- Band 10 (subtopic_7): eating the seed mealies ---
        self.next_band(10)
        b10_title = Tex("Eating the seed mealies").scale(1.2).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        z1 = Tex("Eat the harvest, never the seed — that rule,").scale(0.9).shift(band_shift(10) + UP * 1.4)
        z1b = Tex("written large, is sustainability").scale(0.9).shift(band_shift(10) + UP * 0.6)
        self.play(Write(z1))
        self.play(Write(z1b))
        self.wait(2.5)
        z2 = Tex("The spaza owner eating the stock money kills the shop").scale(0.8).shift(band_shift(10) + DOWN * 0.3)
        self.play(Write(z2))
        self.wait(2)
        z3 = Tex("Three books balanced: nature, economy, fairness").scale(0.85).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(z3))
        self.play(Create(SurroundingRectangle(z3, color=GREEN)))
        self.wait(2)
        z4 = Tex("Drought, floods, maize imports: no longer theory").scale(0.85).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(z4))
        self.wait(2)
        z5 = Tex("Shut the coal era without shutting the coal towns").scale(0.85).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(z5))
        self.wait(4)
