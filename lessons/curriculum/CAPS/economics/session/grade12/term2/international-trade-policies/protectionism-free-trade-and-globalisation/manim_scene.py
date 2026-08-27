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

# Band layout: one frame-tall bands down a long canvas; camera moves down,
# nothing is removed. Exporter-safe mobjects only (Tex/MathTex/Line/Arrow/
# Dot/Circle/Rectangle/VGroup); write-only reveals — no Transform/FadeOut.
#
# Mirrors script.md across the seven subtopics of the duo
# (Expert 1-4: bands 0-7; Simplifier 5-7: bands 8-10), scene time
# apportioned to subtopics.json (235/245/240/250/195/195/205 of 1565 s).

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
        # Intro beat: topic full-screen while intro.md plays (~4-5%).
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the toolkit of protection ---
        title = Tex("Protectionism, Free Trade, Globalisation").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        t1 = Tex(r"TARIFF: border tax lifts the import's price").scale(0.95).shift(UP * 1.2)
        t2 = Tex(r"QUOTA: quantity limit — licences worth money").scale(0.95).shift(UP * 0.4)
        t3 = Tex(r"SUBSIDY: home costs cut, hidden in the budget").scale(0.95).shift(DOWN * 0.4)
        t4 = Tex(r"Exchange control, bans, zealous standards,").scale(0.95).shift(DOWN * 1.2)
        t5 = Tex(r"red tape — and export incentives").scale(0.95).shift(DOWN * 1.9)
        self.play(Write(t1))
        self.wait(2)
        self.play(Write(t2))
        self.wait(2)
        self.play(Write(t3))
        self.wait(2)
        self.play(Write(t4))
        self.play(Write(t5))
        self.wait(2.5)
        econ = Tex(r"Economists dislike quotas more than tariffs").scale(0.95).shift(DOWN * 2.8)
        self.play(Write(econ))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): dumping, infants, incidence ---
        self.next_band(1)
        b1_title = Tex("Dumping, infants, and who pays").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        d1 = Tex(r"DUMPING: exports below cost to kill rivals —").scale(0.95).shift(band_shift(1) + UP * 1.2)
        d2 = Tex(r"SA's anti-dumping duties: chicken, steel").scale(0.95).shift(band_shift(1) + UP * 0.5)
        self.play(Write(d1))
        self.play(Write(d2))
        self.wait(2.5)
        d3 = Tex(r"INFANT INDUSTRY: could match rivals at scale —").scale(0.9).shift(band_shift(1) + DOWN * 0.4)
        d4 = Tex(r"the candidate for TEMPORARY protection").scale(0.95).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(d3))
        self.play(Write(d4))
        self.wait(2.5)
        wrong = Tex(r"Protection is free").scale(1.0).shift(band_shift(1) + DOWN * 2.0 + LEFT * 3.4)
        self.play(Write(wrong))
        self.play(Create(strike(wrong)))
        inc = Tex(r"A transfer from consumers to producers").scale(0.95).shift(band_shift(1) + DOWN * 2.0 + RIGHT * 2.6)
        self.play(Write(inc))
        self.wait(2)
        asym = Tex(r"Losses spread thin; gains concentrated").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(asym))
        self.play(Create(SurroundingRectangle(asym, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): protection's case with rebuttals ---
        self.next_band(2)
        b2_title = Tex("For protection — each with its rebuttal").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        a1 = Tex(r"Infants need shelter / infants never grow up").scale(0.9).shift(band_shift(2) + UP * 1.2)
        a2 = Tex(r"Saves jobs / visible jobs, invisible losses").scale(0.9).shift(band_shift(2) + UP * 0.4)
        a3 = Tex(r"Anti-dumping — the strongest card").scale(0.9).shift(band_shift(2) + DOWN * 0.4)
        a4 = Tex(r"Self-sufficiency: resilience after the pandemic").scale(0.9).shift(band_shift(2) + DOWN * 1.2)
        a5 = Tex(r"BoP support and revenue / better tools exist").scale(0.9).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(a1))
        self.wait(2)
        self.play(Write(a2))
        self.wait(2)
        self.play(Write(a3))
        self.wait(2)
        self.play(Write(a4))
        self.wait(2)
        self.play(Write(a5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): free trade and the mix ---
        self.next_band(3)
        b3_title = Tex("For free trade — and the desirable mix").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        f1 = Tex(r"Specialisation lifts output; prices fall;").scale(0.95).shift(band_shift(3) + UP * 1.2)
        f2 = Tex(r"competition disciplines; scale opens;").scale(0.95).shift(band_shift(3) + UP * 0.5)
        f3 = Tex(r"technology travels with goods").scale(0.95).shift(band_shift(3) + DOWN * 0.2)
        self.play(Write(f1))
        self.wait(2)
        self.play(Write(f2))
        self.wait(2)
        self.play(Write(f3))
        self.wait(2)
        ag = Tex(r"Against: jobs shed fast, gains uneven,").scale(0.95).shift(band_shift(3) + DOWN * 1.1)
        ag2 = Tex(r"raw-export lock-in").scale(0.95).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(ag))
        self.play(Write(ag2))
        self.wait(2.5)
        mix = Tex(r"Mix: open trade + rare, temporary,").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        mix2 = Tex(r"conditional shelter — scalpel, never blanket").scale(0.95).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(mix))
        self.play(Write(mix2))
        self.play(Create(SurroundingRectangle(mix2, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the two grand strategies ---
        self.next_band(4)
        b4_title = Tex("Inward or outward: two strategies").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        is1 = Tex(r"IMPORT SUBSTITUTION: fill the home market").scale(0.95).shift(band_shift(4) + UP * 1.2)
        is2 = Tex(r"behind tariff walls — apartheid SA's model").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(is1))
        self.play(Write(is2))
        self.wait(2.5)
        is3 = Tex(r"Caution: small (home ceiling), inefficient,").scale(0.9).shift(band_shift(4) + DOWN * 0.3)
        is4 = Tex(r"consumers fund it through higher prices").scale(0.9).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(is3))
        self.play(Write(is4))
        self.wait(2.5)
        ep1 = Tex(r"EXPORT PROMOTION: sell to the world —").scale(0.95).shift(band_shift(4) + DOWN * 1.9)
        ep2 = Tex(r"no ceiling, forced efficiency — East Asia's path").scale(0.9).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(ep1))
        self.play(Write(ep2))
        self.play(Create(SurroundingRectangle(ep2, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): South Africa's path ---
        self.next_band(5)
        b5_title = Tex("South Africa's current mix").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        sa1 = Tex(r"Tariffs cut from the 1990s; IPAP and").scale(0.95).shift(band_shift(5) + UP * 1.2)
        sa2 = Tex(r"sector master plans — automotive the flagship").scale(0.9).shift(band_shift(5) + UP * 0.5)
        self.play(Write(sa1))
        self.play(Write(sa2))
        self.wait(2.5)
        sa3 = Tex(r"Contested cases: clothing, poultry, steel").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(sa3))
        self.wait(2.5)
        sa4 = Tex(r"Judgment: export-led on paper, selective").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        sa5 = Tex(r"protection kept — throttled by logistics").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        sa6 = Tex(r"and electricity, not trade policy").scale(0.95).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(sa4))
        self.play(Write(sa5))
        self.play(Write(sa6))
        self.play(Create(SurroundingRectangle(sa6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): globalisation and the WTO ---
        self.next_band(6)
        b6_title = Tex("Globalisation and the WTO").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        g1 = Tex(r"Engines: containers, telecoms, finance,").scale(0.95).shift(band_shift(6) + UP * 1.2)
        g2 = Tex(r"barrier-cutting — GATT 1947 to WTO 1995").scale(0.95).shift(band_shift(6) + UP * 0.5)
        self.play(Write(g1))
        self.play(Write(g2))
        self.wait(2.5)
        r1 = Tex(r"Rules: most-favoured-nation, national").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        r2 = Tex(r"treatment, bound tariffs, dispute desk").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(r1))
        self.play(Write(r2))
        self.play(Create(SurroundingRectangle(r2, color=GREEN)))
        self.wait(2.5)
        cr1 = Tex(r"Critiques: rich farm protection, kicked-away").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        cr2 = Tex(r"ladders, uneven gains").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(cr1))
        self.play(Write(cr2))
        self.wait(3)

        # --- Band 7 (subtopic_4): the ladder of integration ---
        self.next_band(7)
        b7_title = Tex("The ladder of integration").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        l1 = Tex(r"1. Free trade area — AfCFTA, world's largest").scale(0.95).shift(band_shift(7) + UP * 1.2)
        l2 = Tex(r"2. Customs union: common external tariff —").scale(0.95).shift(band_shift(7) + UP * 0.4)
        l2b = Tex(r"SACU, the world's oldest").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        l3 = Tex(r"3. Common market: labour and capital move").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        l4 = Tex(r"4. Economic union: one policy, one currency — EU").scale(0.9).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(l1))
        self.wait(2)
        self.play(Write(l2))
        self.play(Write(l2b))
        self.wait(2)
        self.play(Write(l3))
        self.wait(2)
        self.play(Write(l4))
        self.wait(2)
        sa7 = Tex(r"SA stands on several rungs at once").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(sa7))
        self.play(Create(SurroundingRectangle(sa7, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the tuckshop and the gate ---
        self.next_band(8)
        b8_title = Tex("The tuckshop and the vendors at the gate").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        v1 = Tex(r"R20 a day to trade $=$ TARIFF").scale(0.95).shift(band_shift(8) + UP * 1.2)
        v2 = Tex(r"Only three vendors $=$ QUOTA (licences love it)").scale(0.9).shift(band_shift(8) + UP * 0.4)
        v3 = Tex(r"Free kitchen $=$ SUBSIDY; sweet ban $=$ STANDARD").scale(0.9).shift(band_shift(8) + DOWN * 0.4)
        v4 = Tex(r"Selling below cost to kill the shop $=$ DUMPING").scale(0.9).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(v1))
        self.wait(2.5)
        self.play(Write(v2))
        self.wait(2.5)
        self.play(Write(v3))
        self.wait(2.5)
        self.play(Write(v4))
        self.wait(2.5)
        arith = Tex(r"Two workers saved — 800 learners pay").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        arith2 = Tex(r"R2 more daily: thin losses dwarf the gain").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(arith))
        self.play(Write(arith2))
        self.play(Create(SurroundingRectangle(arith2, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the young shop ---
        self.next_band(9)
        b9_title = Tex("Raising the young shop without spoiling it").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        y1 = Tex(r"New shop, one sheltered year: the infant case").scale(0.9).shift(band_shift(9) + UP * 1.2)
        self.play(Write(y1))
        self.wait(2.5)
        y2 = Tex(r"But sheltered pies sell regardless — the").scale(0.95).shift(band_shift(9) + UP * 0.4)
        y3 = Tex(r"ladder becomes a hammock").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(y2))
        self.play(Write(y3))
        self.wait(2.5)
        y4 = Tex(r"Honesty rules: expiry date, pressure targets,").scale(0.9).shift(band_shift(9) + DOWN * 1.2)
        y5 = Tex(r"genuine infants only").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(y4))
        self.play(Write(y5))
        self.play(Create(SurroundingRectangle(y5, color=GREEN)))
        self.wait(2.5)
        y6 = Tex(r"Two futures: sell to your 800, or bake well").scale(0.9).shift(band_shift(9) + DOWN * 2.7)
        y7 = Tex(r"enough for other schools — if the van starts").scale(0.9).shift(band_shift(9) + DOWN * 3.4)
        self.play(Write(y6))
        self.play(Write(y7))
        self.wait(3)

        # --- Band 10 (subtopic_7): one big playground ---
        self.next_band(10)
        b10_title = Tex("One big playground").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        p1 = Tex(r"District deal, no gate fees $=$ free trade area:").scale(0.9).shift(band_shift(10) + UP * 1.2)
        p2 = Tex(r"the kota stand sells to five schools — AfCFTA").scale(0.9).shift(band_shift(10) + UP * 0.5)
        self.play(Write(p1))
        self.play(Write(p2))
        self.wait(2.5)
        p3 = Tex(r"Common outsider fee: customs union (SACU);").scale(0.9).shift(band_shift(10) + DOWN * 0.3)
        p4 = Tex(r"vendors move: common market; one card: union").scale(0.9).shift(band_shift(10) + DOWN * 1.0)
        self.play(Write(p3))
        self.play(Write(p4))
        self.wait(2.5)
        p5 = Tex(r"The district desk $=$ the WTO: no favourites,").scale(0.9).shift(band_shift(10) + DOWN * 1.9)
        p6 = Tex(r"treat insiders alike, frozen fees, complaints desk").scale(0.85).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(p5))
        self.play(Write(p6))
        self.wait(2.5)
        p7 = Tex(r"Better lunches, real losers, arguing rulebook").scale(0.9).shift(band_shift(10) + DOWN * 3.4)
        self.play(Write(p7))
        self.play(Create(SurroundingRectangle(p7, color=GREEN)))
        self.wait(4)
