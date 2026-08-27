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

# Band-layout whiteboard scene for "Economic Redress and Democratisation"
# (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier subtopics 5-7).
# Exporter-safe primitives only; add-only lifecycle.
# Subtopic durations: 220/240/220/230/190/200/190 of 1490 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EconomicRedressDemocratisationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===================== Part 1 — Expert =====================
        # --- Band 0 (subtopic_1): what marginalised means ---
        title = Tex("Economic Redress and Democratisation").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0a = Tex("Marginalised: held at the margin of the economy").scale(1.0).shift(UP * 1.2)
        b0a2 = Tex("— exclusion written into statute, by design").scale(1.0).shift(UP * 0.5)
        self.play(Write(b0a))
        self.play(Write(b0a2))
        self.wait(2)
        b0b = Tex("Black South Africans $\\cdot$ women $\\cdot$ rural areas").scale(0.91).shift(DOWN * 0.4)
        b0c = Tex("people with disabilities $\\cdot$ youth").scale(1.0).shift(DOWN * 1.1)
        self.play(Write(b0b))
        self.wait(2)
        self.play(Write(b0c))
        self.wait(2)
        b0d = Tex("Redress: policy-driven correction of that past").scale(1.05).shift(DOWN * 2.1)
        self.play(Write(b0d))
        self.play(Create(SurroundingRectangle(b0d, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): mechanisms and intersection ---
        self.next_band(1)
        b1t = Tex("Group + MECHANISM = analysis").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("Land ownership stripped; inferior schooling;").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1a2 = Tex("migrant labour at captive wages").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1a))
        self.play(Write(b1a2))
        self.wait(2)
        b1b = Tex("Women: barred from property, contracts, credit;").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        b1b2 = Tex("unpaid care work limits hours to sell").scale(0.95).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1b))
        self.play(Write(b1b2))
        self.wait(2)
        b1c = Tex("Rural distance; inaccessible workplaces; youth inherit").scale(0.9).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1c))
        self.wait(2)
        b1d = Tex("Intersecting categories: one compounded wall").scale(1.05).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1d))
        self.play(Create(SurroundingRectangle(b1d, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): land reform's three tracks ---
        self.next_band(2)
        b2t = Tex("Redress via factors: land first").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        r2a = Rectangle(width=3.6, height=1.0).shift(band_shift(2) + UP * 0.9 + LEFT * 4.6)
        t2a = Tex("Restitution").scale(0.9).move_to(r2a.get_center())
        d2a = Tex("return or compensate post-1913 loss").scale(0.9).shift(band_shift(2) + UP * 0.9 + RIGHT * 2.0)
        self.play(Create(r2a), Write(t2a))
        self.play(Write(d2a))
        self.wait(2)
        r2b = Rectangle(width=3.6, height=1.0).shift(band_shift(2) + DOWN * 0.3 + LEFT * 4.6)
        t2b = Tex("Redistribution").scale(0.9).move_to(r2b.get_center())
        d2b = Tex("open access for those never allowed to own").scale(0.85).shift(band_shift(2) + DOWN * 0.3 + RIGHT * 2.2)
        self.play(Create(r2b), Write(t2b))
        self.play(Write(d2b))
        self.wait(2)
        r2c = Rectangle(width=3.6, height=1.0).shift(band_shift(2) + DOWN * 1.5 + LEFT * 4.6)
        t2c = Tex("Tenure reform").scale(0.9).move_to(r2c.get_center())
        d2c = Tex("occupation becomes defensible rights").scale(0.9).shift(band_shift(2) + DOWN * 1.5 + RIGHT * 2.0)
        self.play(Create(r2c), Write(t2c))
        self.play(Write(d2c))
        self.wait(2)
        b2e = Tex("Transfer plus support — alone it is a ceremony").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2e))
        self.play(Create(SurroundingRectangle(b2e, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): labour, capital, entrepreneurship ---
        self.next_band(3)
        b3t = Tex("Labour, capital, entrepreneurship").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("Labour: employment equity up to management;").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3a2 = Tex("levy-funded learnerships and artisan training").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3a))
        self.play(Write(b3a2))
        self.wait(2.5)
        b3b = Tex("Capital: B-BBEE ownership and procurement;").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        b3b2 = Tex("development finance where banks see no collateral").scale(0.95).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3b))
        self.play(Write(b3b2))
        self.wait(2.5)
        b3c = Tex("Entrepreneurship: incubation, set-asides, mentorship").scale(0.95).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3c))
        self.wait(2)
        b3d = Tex("Denied what? Which instrument? What support?").scale(1.0).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3d))
        self.play(Create(SurroundingRectangle(b3d, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): channels of participation ---
        self.next_band(4)
        b4t = Tex("Democratising economic decisions").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("Labour law: decisions negotiated WITH workers").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4a))
        self.wait(2)
        b4b = Tex("Public participation: submissions to Parliament,").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4b2 = Tex("municipal consultation, tariff hearings").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(b4b))
        self.play(Write(b4b2))
        self.wait(2)
        b4c = Tex("Self-regulating bodies: codes set by practitioners").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4c))
        self.wait(2)
        b4d = Tex("Widen the circle of voices that count").scale(1.05).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4d))
        self.play(Create(SurroundingRectangle(b4d, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): NEDLAC — four constituencies ---
        self.next_band(5)
        b5t = Tex("NEDLAC: negotiate BEFORE Parliament").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        table = Rectangle(width=3.6, height=1.2).shift(band_shift(5) + DOWN * 0.2)
        t_tab = Tex("NEDLAC").scale(0.9).move_to(table.get_center())
        self.play(Create(table), Write(t_tab))
        self.wait(1.5)
        c1 = Tex("Government").scale(0.85).shift(band_shift(5) + UP * 1.2 + LEFT * 4.2)
        c2 = Tex("Business").scale(0.85).shift(band_shift(5) + UP * 1.2 + RIGHT * 4.2)
        c3 = Tex("Labour").scale(0.85).shift(band_shift(5) + DOWN * 1.7 + LEFT * 4.2)
        c4 = Tex("Community").scale(0.85).shift(band_shift(5) + DOWN * 1.7 + RIGHT * 4.2)
        a1 = Arrow(c1.get_right(), table.get_corner(UL), buff=0.15)
        a2 = Arrow(c2.get_left(), table.get_corner(UR), buff=0.15)
        a3 = Arrow(c3.get_right(), table.get_corner(DL), buff=0.15)
        a4 = Arrow(c4.get_left(), table.get_corner(DR), buff=0.15)
        self.play(Write(c1), Create(a1))
        self.play(Write(c2), Create(a2))
        self.play(Write(c3), Create(a3))
        self.play(Write(c4), Create(a4))
        self.wait(2)
        b5a = Tex("Social dialogue: consensus, durable buy-in").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5a))
        self.wait(2)
        b5b = Tex("Limit: slow; unorganised voices heard least").scale(0.9).shift(band_shift(5) + DOWN * 3.3)
        self.play(Write(b5b))
        self.wait(3)

        # --- Band 6 (subtopic_4): the five aims and their pull ---
        self.next_band(6)
        b6t = Tex("Macro-economic aims pull against each other").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("Performance $\\cdot$ employment $\\cdot$ distribution").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6b = Tex("internal stability $\\cdot$ external stability").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6a))
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = Tex("Redistribution needs revenue; revenue needs growth;").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6d = Tex("stability disciplines the borrowing spending needs").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6c))
        self.play(Write(b6d))
        self.wait(2.5)
        b6e = Tex("No dial setting maximises everything at once").scale(1.05).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6e))
        self.play(Create(SurroundingRectangle(b6e, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): both ledgers open ---
        self.next_band(7)
        b7t = Tex("Judge redress with BOTH ledgers open").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("Gains: services, grants, housing reached millions;").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7a2 = Tex("professional class; rights and institutions").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7a))
        self.play(Write(b7a2))
        self.wait(2.5)
        b7b = Tex("Shortfalls: extreme unemployment and inequality;").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7b2 = Tex("slow land reform; benefits sometimes captured").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7b))
        self.play(Write(b7b2))
        self.wait(2.5)
        b7c = Tex("Mechanisms attached; evidence apart from preference").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7c))
        self.play(Create(SurroundingRectangle(b7c, color=GREEN)))
        self.wait(3)

        # ===================== Part 2 — Simplifier =====================
        # --- Band 8 (subtopic_5): two applicants, one post ---
        self.next_band(8)
        b8t = Tex("Starting the race at different lines").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Same post, same interview —").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8a2 = Tex("car and contacts against two borrowed taxi fares").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8a))
        self.play(Write(b8a2))
        self.wait(2.5)
        b8wrong = Tex("Equal laws mean an equal economy").scale(1.05).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8wrong))
        self.play(Create(strike(b8wrong)))
        self.wait(2)
        b8b = Tex("Inheritance carries it: property, schooling,").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8b2 = Tex("contacts, location").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8b))
        self.play(Write(b8b2))
        self.wait(2)
        b8c = Tex("Redress: closing the gap between law and economy").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8c))
        self.play(Create(SurroundingRectangle(b8c, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): Naledi's four needs ---
        self.next_band(9)
        b9t = Tex("Four things you need to build a livelihood").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("A PLACE: title, access or security — plus support;").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9a2 = Tex("a plot with no buyer is not yet a business").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9a))
        self.play(Write(b9a2))
        self.wait(2.5)
        b9b = Tex("SKILLS: learnerships, trades, equity to the top").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("MONEY: ownership channels, no-collateral finance").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9c))
        self.wait(2)
        b9d = Tex("THE CHANCE: registration, mentor, first order").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9d))
        self.wait(2)
        b9e = Tex("Test: an OBJECT handed over, or a LIVELIHOOD left?").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9e))
        self.play(Create(SurroundingRectangle(b9e, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): voice, and the final judgement ---
        self.next_band(10)
        b10t = Tex("Who sits at the table").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("Workers with a chair; residents at hearings;").scale(0.95).shift(band_shift(10) + UP * 1.1)
        b10a2 = Tex("professions policing their own codes").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10a))
        self.play(Write(b10a2))
        self.wait(2.5)
        b10b = Tex("NEDLAC's four chairs: government, business,").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        b10b2 = Tex("labour, community — the argument happens early").scale(1.0).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10b))
        self.play(Write(b10b2))
        self.wait(2.5)
        b10c = Tex("Both columns: real gains and real shortfalls").scale(0.95).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(b10c))
        self.wait(2)
        b10d = Tex("Mechanisms, not slogans — that is economics").scale(1.05).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10d))
        self.play(Create(SurroundingRectangle(b10d, color=GREEN)))
        self.wait(4)
