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

# Band-layout whiteboard scene for the session duo "Environmental
# Deterioration and Sustainability" (Grade 11, Term 4). One band per teaching
# step; the camera moves down and nothing is removed. Exporter-safe mobjects
# only; the externality diagram is hand-built from Rectangles and Arrows.
# Band time apportioned to subtopics.json (240/255/250/245/205/205/210 of
# 1610 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EnvironmentalSustainabilitySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): externalities — the smoke diagram ---
        title = Tex("Why Markets Fail the Environment").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        fac = Rectangle(width=3.2, height=1.1).shift(LEFT * 4.2 + UP * 0.9)
        fac_lab = Tex("Factory (coal)").scale(0.75).move_to(fac.get_center())
        buyer = Rectangle(width=3.2, height=1.1).shift(RIGHT * 4.2 + UP * 0.9)
        buyer_lab = Tex("Buyer pays").scale(0.75).move_to(buyer.get_center())
        self.play(Create(fac), Write(fac_lab))
        self.play(Create(buyer), Write(buyer_lab))
        a1 = Arrow(fac.get_right(), buyer.get_left(), buff=0.1)
        a1_lab = Tex("priced transaction").scale(0.7).shift(UP * 1.6)
        self.play(Create(a1), Write(a1_lab))
        self.wait(2)
        nb = Rectangle(width=3.6, height=1.1).shift(LEFT * 4.2 + DOWN * 1.1)
        nb_lab = Tex("Neighbour breathes").scale(0.7).move_to(nb.get_center())
        a2 = Arrow(fac.get_bottom(), nb.get_top(), buff=0.1, color=RED)
        a2_lab = Tex("smoke: no price tag").scale(0.7).shift(LEFT * 1.6 + DOWN * 0.1)
        self.play(Create(nb), Write(nb_lab))
        self.play(Create(a2), Write(a2_lab))
        self.wait(2.5)
        e1 = Tex("EXTERNALITY: a cost on someone outside the deal").scale(0.9).shift(DOWN * 2.1)
        self.play(Write(e1))
        self.play(Create(SurroundingRectangle(e1, color=GREEN)))
        self.wait(2)
        e2 = Tex("Too cheap, so too much made: prices that LIE").scale(0.9).shift(DOWN * 3.0)
        self.play(Write(e2))
        self.wait(3)

        # --- Band 1 (subtopic_1): commons, the missing future, SA's ledger ---
        self.next_band(1)
        b1_title = Tex("The commons, and the missing future").scale(1.1).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        c1 = Tex("Common resources: nobody owns, everybody uses").scale(0.95).shift(band_shift(1) + UP * 1.4)
        c2 = Tex("Each taker gains the whole fish; the loss is shared").scale(0.95).shift(band_shift(1) + UP * 0.55)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        c3 = Tex("What belongs to everyone is cared for by no one").scale(0.95).shift(band_shift(1) + DOWN * 0.35)
        self.play(Write(c3))
        self.play(Create(SurroundingRectangle(c3, color=GREEN)))
        self.wait(2.5)
        c4 = Tex("People born in 2060 place no orders today").scale(0.95).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(c4))
        self.wait(2)
        c5 = Tex("SA ledger: acid mine drainage, Highveld air,").scale(0.9).shift(band_shift(1) + DOWN * 2.2)
        c6 = Tex("overfished West Coast, coal-heavy emissions per person").scale(0.85).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(c5))
        self.play(Write(c6))
        self.wait(3)

        # --- Band 2 (subtopic_2): toolbox — rules and prices ---
        self.next_band(2)
        b2_title = Tex("The policy toolbox: rules and prices").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        t1 = Tex("1. Command and control: emission standards, EIAs,").scale(0.9).shift(band_shift(2) + UP * 1.4)
        t1b = Tex("quotas, protected areas — the limit is the limit").scale(0.9).shift(band_shift(2) + UP * 0.6)
        self.play(Write(t1))
        self.play(Write(t1b))
        self.wait(2.5)
        t2 = Tex("An unenforced rule is a suggestion").scale(0.9).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(t2))
        self.wait(2)
        t3 = Tex("2. Market-based: carbon tax, bag levy, tyre levy —").scale(0.9).shift(band_shift(2) + DOWN * 1.2)
        t3b = Tex("the tax writes the missing invoice").scale(0.9).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(t3))
        self.play(Write(t3b))
        self.wait(2.5)
        t4 = Tex("Plus clean subsidies, and tradable permits under a cap").scale(0.85).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(t4))
        self.wait(3)

        # --- Band 3 (subtopic_2): owners, treaties, evaluation ---
        self.next_band(3)
        b3_title = Tex("Owners, treaties — and the evaluation").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        o1 = Tex("3. Property rights: community quotas, conservancies —").scale(0.85).shift(band_shift(3) + UP * 1.4)
        o1b = Tex("owners harvest sustainably; the future value is theirs").scale(0.85).shift(band_shift(3) + UP * 0.6)
        self.play(Write(o1))
        self.play(Write(o1b))
        self.wait(2.5)
        o2 = Tex("4. International agreements: Paris — carbon ignores").scale(0.85).shift(band_shift(3) + DOWN * 0.3)
        o2b = Tex("borders, so countries commit together").scale(0.85).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(o2))
        self.play(Write(o2b))
        self.wait(2.5)
        o3 = Tex("Rules: certain but need police. Taxes: clever but pinch").scale(0.8).shift(band_shift(3) + DOWN * 2.0)
        o3b = Tex("the poor. Permits: cheap cuts. Treaties: weak teeth.").scale(0.8).shift(band_shift(3) + DOWN * 2.7)
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
        s2 = Tex("Nature is CAPITAL; harvest no faster than it regrows").scale(0.9).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(s2))
        self.wait(2)
        s3 = Tex("Renewables have a threshold: fish gently, forever;").scale(0.85).shift(band_shift(4) + DOWN * 1.3)
        s3b = Tex("fish hard, and the renewable dies like a non-renewable").scale(0.85).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(s3))
        self.play(Write(s3b))
        self.wait(2.5)
        s4 = Tex("Coal and gold: spend once — build skills and assets instead").scale(0.8).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(s4))
        self.wait(3)

        # --- Band 5 (subtopic_3): the tripod and the just transition ---
        self.next_band(5)
        b5_title = Tex("Three legs, and the just transition").scale(1.1).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        p1 = Tex("Environmental: keep the stocks alive").scale(0.95).shift(band_shift(5) + UP * 1.4)
        p2 = Tex("Economic: keep production and livelihoods going").scale(0.95).shift(band_shift(5) + UP * 0.55)
        p3 = Tex("Social: share costs and benefits fairly").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        for m in (p1, p2, p3):
            self.play(Write(m))
            self.wait(1.8)
        self.play(Create(SurroundingRectangle(VGroup(p1, p2, p3), color=GREEN)))
        self.wait(2)
        p4 = Tex("Pull any leg away and the stool falls").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(p4))
        self.wait(2)
        p5 = Tex("Just transition: decarbonise coal power WHILE").scale(0.9).shift(band_shift(5) + DOWN * 2.2)
        p5b = Tex("retraining workers and rebuilding Mpumalanga").scale(0.9).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(p5))
        self.play(Write(p5b))
        self.wait(3)

        # --- Band 6 (subtopic_4): the warming mechanism and the local ledger ---
        self.next_band(6)
        b6_title = Tex("The mechanism, and the recent memory").scale(1.1).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        w1 = Tex(r"Fossil fuels $\to$ greenhouse gases $\to$ trapped heat").scale(0.9).shift(band_shift(6) + UP * 1.4)
        w2 = Tex(r"$\to$ 1$^{\circ}$C$+$ warming $\to$ loaded dice: droughts, floods").scale(0.9).shift(band_shift(6) + UP * 0.55)
        self.play(Write(w1))
        self.wait(2)
        self.play(Write(w2))
        self.wait(2.5)
        w3 = Tex("North built wealth on emissions; the South takes").scale(0.9).shift(band_shift(6) + DOWN * 0.35)
        w3b = Tex("the earliest, hardest hits — Africa emits a few percent").scale(0.85).shift(band_shift(6) + DOWN * 1.15)
        self.play(Write(w3))
        self.play(Write(w3b))
        self.wait(2.5)
        w4 = Tex("Cape Town's Day Zero: weeks from dry taps").scale(0.9).shift(band_shift(6) + DOWN * 2.05)
        w5 = Tex("Durban 2022 floods: over 400 lives, billions in damage").scale(0.85).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(w4))
        self.wait(2)
        self.play(Write(w5))
        self.wait(3)

        # --- Band 7 (subtopic_4): trade exposure and the response ---
        self.next_band(7)
        b7_title = Tex("Triple exposure — and the response").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        x1 = Tex("Carbon border taxes: coal-fired exports pay at the door").scale(0.85).shift(band_shift(7) + UP * 1.4)
        x2 = Tex("Coal dependence becomes a tariff on everything we sell").scale(0.85).shift(band_shift(7) + UP * 0.55)
        self.play(Write(x1))
        self.wait(2)
        self.play(Write(x2))
        self.wait(2.5)
        x3 = Tex("Response: Paris commitments, carbon tax, renewable").scale(0.85).shift(band_shift(7) + DOWN * 0.35)
        x3b = Tex("auctions, and the Just Energy Transition Partnership").scale(0.85).shift(band_shift(7) + DOWN * 1.15)
        self.play(Write(x3))
        self.play(Write(x3b))
        self.wait(2.5)
        x4 = Tex("SA is triply exposed: polluter, victim, coal exporter —").scale(0.85).shift(band_shift(7) + DOWN * 2.1)
        x4b = Tex("sustainability here is economic survival").scale(0.9).shift(band_shift(7) + DOWN * 2.9)
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
        v1 = Tex("Brick factory: buyers pay, owner pays — village coughs").scale(0.85).shift(band_shift(8) + UP * 1.4)
        v2 = Tex("A cost that appears on nobody's invoice: externality").scale(0.9).shift(band_shift(8) + UP * 0.55)
        self.play(Write(v1))
        self.wait(2)
        self.play(Write(v2))
        self.wait(2.5)
        v3 = Tex("Bricks priced too cheap, so the market orders MORE smoke").scale(0.85).shift(band_shift(8) + DOWN * 0.35)
        self.play(Write(v3))
        self.wait(2)
        v4 = Tex("The unowned river: each sensible fisherman empties it").scale(0.85).shift(band_shift(8) + DOWN * 1.25)
        self.play(Write(v4))
        self.wait(2)
        v5 = Tex("And the girl who needs this river in 2060 places no orders").scale(0.85).shift(band_shift(8) + DOWN * 2.15)
        self.play(Write(v5))
        self.play(Create(SurroundingRectangle(v5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): putting a price on the smoke ---
        self.next_band(9)
        b9_title = Tex("Putting a price on the smoke: four fixes").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        f1 = Tex("1. Rules with teeth — but no inspector, no rule").scale(0.9).shift(band_shift(9) + UP * 1.4)
        f2 = Tex("2. Send the bill: bag levy, carbon tax — greed harnessed").scale(0.85).shift(band_shift(9) + UP * 0.55)
        f3 = Tex("3. Give the river an owner: quotas, conservancies").scale(0.9).shift(band_shift(9) + DOWN * 0.3)
        f4 = Tex("4. Get the neighbours to sign: Paris, together").scale(0.9).shift(band_shift(9) + DOWN * 1.15)
        for m in (f1, f2, f3, f4):
            self.play(Write(m))
            self.wait(1.9)
        f5 = Tex("The moment smoke has a price, cleaning up pays").scale(0.9).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(f5))
        self.play(Create(SurroundingRectangle(f5, color=GREEN)))
        self.wait(2)
        f6 = Tex("No fix is perfect — real protection stacks all four").scale(0.85).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(f6))
        self.wait(3)

        # --- Band 10 (subtopic_7): eating the seed mealies ---
        self.next_band(10)
        b10_title = Tex("Eating the seed mealies").scale(1.2).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        z1 = Tex("Eat the harvest, never the seed — that rule,").scale(0.9).shift(band_shift(10) + UP * 1.4)
        z1b = Tex("scaled to a planet, is sustainability").scale(0.9).shift(band_shift(10) + UP * 0.6)
        self.play(Write(z1))
        self.play(Write(z1b))
        self.wait(2.5)
        z2 = Tex("Digging up the family gold to buy groceries is eating seed").scale(0.8).shift(band_shift(10) + DOWN * 0.3)
        self.play(Write(z2))
        self.wait(2)
        z3 = Tex("Three legs: nature alive, economy working, people fair").scale(0.85).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(z3))
        self.play(Create(SurroundingRectangle(z3, color=GREEN)))
        self.wait(2)
        z4 = Tex("Day Zero and the Durban floods: no longer theory").scale(0.85).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(z4))
        self.wait(2)
        z5 = Tex("Close the coal era without abandoning the coal towns").scale(0.85).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(z5))
        self.wait(4)
