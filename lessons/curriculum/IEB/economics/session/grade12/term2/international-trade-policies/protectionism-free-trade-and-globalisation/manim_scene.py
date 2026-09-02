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

# Band-layout whiteboard scene for the trade-policies session duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 235/245/240/250/195/195/205 of 1565 s — band dwell
# times are apportioned to match. All diagrams are hand-built from
# exporter-safe primitives (Arrow/Line/Dot/Rectangle/Tex only).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ProtectionismFreeTradeGlobalisationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the toolkit of protection ---
        title = Tex("Protectionism, Free Trade, Globalisation").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        t1 = Tex("Tariff: border tax — import's price rises").scale(1.0).shift(UP * 1.4)
        t2 = Tex("Quota: quantity capped — licences become prizes").scale(1.0).shift(UP * 0.6)
        t3 = Tex("Subsidy: home costs cut — hidden in the budget").scale(1.0).shift(DOWN * 0.2)
        t4 = Tex("Exchange control: no currency, no imports").scale(1.0).shift(DOWN * 1.0)
        t5 = Tex("Standards and red tape: the polite barriers").scale(1.0).shift(DOWN * 1.8)
        for m in (t1, t2, t3, t4, t5):
            self.play(Write(m))
            self.wait(1.7)
        self.wait(2)

        # --- Band 1 (subtopic_1): dumping, infants, incidence ---
        self.next_band(1)
        b1_title = Tex("Two special terms — and who really pays").scale(1.1).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("DUMPING: exporting below cost to kill rivals").scale(1.0).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("— answered by anti-dumping duties").scale(1.0).shift(band_shift(1) + UP * 0.7)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("INFANT INDUSTRY: young, promising, needs").scale(1.0).shift(band_shift(1) + DOWN * 0.2)
        b1_l4 = Tex("temporary shelter to reach scale").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Every tool: consumers pay a little each,").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        b1_l6 = Tex("producers gain a lot each — thin losses, loud gains").scale(1.0).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): protection's case with rebuttals ---
        self.next_band(2)
        b2_title = Tex("For protection — each with its rebuttal").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Infants need shelter / infants never admit growing up").scale(0.9).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("Saves jobs / visible jobs saved, invisible jobs lost").scale(0.9).shift(band_shift(2) + UP * 0.6)
        b2_l3 = Tex("Anti-dumping / the strongest, least contested card").scale(0.9).shift(band_shift(2) + DOWN * 0.2)
        b2_l4 = Tex("Self-sufficiency / resilience — at a standing cost").scale(0.9).shift(band_shift(2) + DOWN * 1.0)
        b2_l5 = Tex("Revenue and BoP / better instruments usually exist").scale(0.9).shift(band_shift(2) + DOWN * 1.8)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4, b2_l5):
            self.play(Write(m))
            self.wait(2)
        self.wait(2)

        # --- Band 3 (subtopic_2): free trade and the mix ---
        self.next_band(3)
        b3_title = Tex("For free trade — and the desirable mix").scale(1.1).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Specialisation lifts total output").scale(1.0).shift(band_shift(3) + UP * 1.4)
        b3_l2 = Tex("Lower prices, wider choice, disciplined monopolies").scale(1.0).shift(band_shift(3) + UP * 0.6)
        b3_l3 = Tex("Scale beyond sixty million people; ideas travel").scale(1.0).shift(band_shift(3) + DOWN * 0.2)
        for m in (b3_l1, b3_l2, b3_l3):
            self.play(Write(m))
            self.wait(2)
        b3_l4 = Tex("The mix: broadly open, plus rare shelter").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        b3_l5 = Tex("that is targeted, temporary, conditional").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the two grand strategies ---
        self.next_band(4)
        b4_title = Tex("Two roads to industry").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        r1 = Rectangle(width=5.8, height=2.6).shift(band_shift(4) + LEFT * 3.3 + UP * 0.6)
        r1_a = Tex("Import substitution").scale(0.95).shift(band_shift(4) + LEFT * 3.3 + UP * 1.4)
        r1_b = Tex("inward, behind walls —").scale(0.8).shift(band_shift(4) + LEFT * 3.3 + UP * 0.6)
        r1_c = Tex("safe, small, ceilinged").scale(0.8).shift(band_shift(4) + LEFT * 3.3 + UP * 0.0)
        self.play(Create(r1), Write(r1_a))
        self.play(Write(r1_b), Write(r1_c))
        self.wait(2)
        r2 = Rectangle(width=5.8, height=2.6).shift(band_shift(4) + RIGHT * 3.3 + UP * 0.6)
        r2_a = Tex("Export promotion").scale(0.95).shift(band_shift(4) + RIGHT * 3.3 + UP * 1.4)
        r2_b = Tex("outward, into the world —").scale(0.8).shift(band_shift(4) + RIGHT * 3.3 + UP * 0.6)
        r2_c = Tex("no ceiling, no shelter").scale(0.8).shift(band_shift(4) + RIGHT * 3.3 + UP * 0.0)
        self.play(Create(r2), Write(r2_a))
        self.play(Write(r2_b), Write(r2_c))
        self.wait(2)
        b4_l1 = Tex("East Asia went outward and industrialised;").scale(1.0).shift(band_shift(4) + DOWN * 1.3)
        b4_l2 = Tex("walls kept too long built industries that gasped").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): South Africa's path ---
        self.next_band(5)
        b5_title = Tex("South Africa's path").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Apartheid era: import substitution + sanctions").scale(1.0).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("1990s: steep tariff cuts, trade agreements").scale(1.0).shift(band_shift(5) + UP * 0.6)
        b5_l3 = Tex("Now: sector master plans — automotive flagship,").scale(1.0).shift(band_shift(5) + DOWN * 0.2)
        b5_l4 = Tex("vehicles exported from Eastern Cape and Gauteng").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        b5_l5 = Tex("Contested files: clothing, poultry, steel").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4, b5_l5):
            self.play(Write(m))
            self.wait(1.8)
        b5_l6 = Tex("Real constraint: logistics and electricity").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): globalisation and the WTO ---
        self.next_band(6)
        b6_title = Tex("Globalisation and the rulebook").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Engines: containers, telecoms, finance, treaties").scale(1.0).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("GATT 1947 $\\rightarrow$ eight rounds $\\rightarrow$ WTO 1995").scale(1.0).shift(band_shift(6) + UP * 0.6)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Rules: most-favoured-nation; national treatment;").scale(1.0).shift(band_shift(6) + DOWN * 0.3)
        b6_l4 = Tex("bound tariffs; disputes to the panel, not the fist").scale(1.0).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("Critiques: farm walls kept by the rich; ladder rules").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        b6_l6 = Tex("tightened after they climbed; gains divided unevenly").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): the ladder of integration ---
        self.next_band(7)
        b7_title = Tex("The ladder of integration").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        l1 = Tex("1. Free trade area — AfCFTA, world's largest").scale(1.0).shift(band_shift(7) + UP * 1.4)
        l2 = Tex("2. Customs union — SACU, world's oldest").scale(1.0).shift(band_shift(7) + UP * 0.6)
        l3 = Tex("3. Common market — labour and capital move").scale(1.0).shift(band_shift(7) + DOWN * 0.2)
        l4 = Tex("4. Economic union — the EU, one currency").scale(1.0).shift(band_shift(7) + DOWN * 1.0)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2)
        b7_l5 = Tex("South Africa stands on several rungs at once").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the chip stall and the hawkers ---
        self.next_band(8)
        b8_title = Tex("The chip stall and the hawkers").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("R30 a day at the fence = a TARIFF").scale(1.0).shift(band_shift(8) + UP * 1.4)
        b8_l2 = Tex("Four licensed hawkers = a QUOTA (licences = gold)").scale(1.0).shift(band_shift(8) + UP * 0.6)
        b8_l3 = Tex("Free cold room = a SUBSIDY, invisible but real").scale(1.0).shift(band_shift(8) + DOWN * 0.2)
        b8_l4 = Tex("Certificates for the fence only = a STANDARD").scale(1.0).shift(band_shift(8) + DOWN * 1.0)
        b8_l5 = Tex("Boerie rolls below cost = DUMPING, the serious one").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4, b8_l5):
            self.play(Write(m))
            self.wait(1.8)
        b8_l6 = Tex("Two jobs saved, loudly; 2 000 lunches dearer, silently").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the young stall ---
        self.next_band(9)
        b9_title = Tex("Raising the young stall").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("One sheltered season: fair — nobody learns").scale(1.0).shift(band_shift(9) + UP * 1.4)
        b9_l2 = Tex("to swim mid-shipwreck").scale(1.0).shift(band_shift(9) + UP * 0.7)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("But sheltered chips sell anyway — why improve?").scale(1.0).shift(band_shift(9) + DOWN * 0.2)
        b9_l4 = Tex("The ladder becomes a hammock").scale(1.0).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.play(Create(strike(b9_l4)))
        self.wait(2)
        b9_l5 = Tex("Honest shelter: expiry date + targets + real infants").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(2)
        b9_l6 = Tex("Two futures: this rank forever — or every rank,").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        b9_l7 = Tex("if the scooter starts").scale(0.95).shift(band_shift(9) + DOWN * 3.3)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.wait(3)

        # --- Band 10 (subtopic_7): one big rank ---
        self.next_band(10)
        b10_title = Tex("One big rank").scale(1.2).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Any vendor, any rank, no fees = free trade area").scale(1.0).shift(band_shift(10) + UP * 1.7)
        b10_l2 = Tex("One outside entry fee = customs union").scale(1.0).shift(band_shift(10) + UP * 0.9)
        b10_l3 = Tex("Vendors relocate freely = common market").scale(1.0).shift(band_shift(10) + UP * 0.1)
        b10_l4 = Tex("One trading card, one rulebook = economic union").scale(1.0).shift(band_shift(10) + DOWN * 0.7)
        for m in (b10_l1, b10_l2, b10_l3, b10_l4):
            self.play(Write(m))
            self.wait(1.9)
        b10_l5 = Tex("The referee's desk: no favourites, treat insiders").scale(0.95).shift(band_shift(10) + DOWN * 1.6)
        b10_l6 = Tex("as your own, frozen fees stay frozen, quarrels to the desk").scale(0.95).shift(band_shift(10) + DOWN * 2.3)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
