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

# Band-layout whiteboard scene for the CAPS Grade 12 Geography session duo
# "Mining and the Platinum Case Study". Bands cover all seven subtopics
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7) with
# dwell time proportional to subtopics.json (240/230/240/240/220/230/230 of
# 1630 s). The Bushveld saucer cross-section and the mine's map signature are
# hand-built from exporter-safe primitives only (Line/Arrow/Dot/Circle/
# Rectangle/Tex); add-only lifecycle, camera moves between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MiningPlatinumCaseStudySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # --- Band 0 (subtopic_1): mining as foundation — the evidence chain ---
        title = Tex("Mining and the Platinum Case Study").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Claim: mining is the economy's foundation").scale(1.1).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex(r"Diamonds 1867 $\rightarrow$ gold 1886 $\rightarrow$ platinum").scale(1.05).shift(UP * 0.0)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex(r"Mines demanded rail, Eskom power,").scale(1.05).shift(DOWN * 0.9)
        b0_l4 = Tex(r"machinery, finance --- the JSE itself").scale(1.05).shift(DOWN * 1.6)
        self.play(Write(b0_l3)); self.wait(1.8)
        self.play(Write(b0_l4)); self.wait(2)
        b0_l5 = Tex(r"Migrant labour reshaped the whole region").scale(1.05).shift(DOWN * 2.5)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): today's contribution and the cost ledger ---
        self.next_band(1)
        b1_t = Tex("Contribution today --- and the other ledger").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex(r"Under 10\% of GDP, under 500 000 jobs").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex(r"But an outsized share of export earnings").scale(1.05).shift(band_shift(1) + UP * 0.3)
        b1_l3 = Tex(r"Multipliers, royalties, whole mining towns").scale(1.05).shift(band_shift(1) + DOWN * 0.5)
        for m in (b1_l1, b1_l2, b1_l3):
            self.play(Write(m))
            self.wait(1.8)
        b1_l4 = Tex(r"Costs: acid mine drainage, dust, sinkholes").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        b1_l5 = Tex(r"Social: silicosis, stranded towns, migrancy").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l4)); self.wait(1.8)
        self.play(Write(b1_l5)); self.wait(1.5)
        b1_l6 = Tex(r"Critical answers carry BOTH ledgers").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the Bushveld saucer, drawn in cross-section ---
        self.next_band(2)
        b2_t = Tex("The Bushveld Igneous Complex").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        surface = Line(band_shift(2) + UP * 1.1 + LEFT * 4.2,
                       band_shift(2) + UP * 1.1 + RIGHT * 4.2, stroke_width=3)
        self.play(Create(surface))
        # saucer: two dipping limbs meeting a flat base (3-segment line chain)
        sc = band_shift(2)
        saucer = VGroup(
            Line(sc + UP * 1.1 + LEFT * 3.6, sc + DOWN * 0.7 + LEFT * 1.4, color=YELLOW, stroke_width=5),
            Line(sc + DOWN * 0.7 + LEFT * 1.4, sc + DOWN * 0.7 + RIGHT * 1.4, color=YELLOW, stroke_width=5),
            Line(sc + DOWN * 0.7 + RIGHT * 1.4, sc + UP * 1.1 + RIGHT * 3.6, color=YELLOW, stroke_width=5),
        )
        self.play(Create(saucer[0])); self.play(Create(saucer[1])); self.play(Create(saucer[2]))
        self.wait(1.5)
        b2_l1 = Tex(r"Layered, saucer-shaped molten body").scale(0.95).shift(sc + DOWN * 1.5)
        self.play(Write(b2_l1))
        self.wait(1.5)
        d_w = Dot(sc + UP * 1.1 + LEFT * 3.6, color=RED)
        l_w = Tex(r"West: Rustenburg, Brits").scale(0.85).shift(sc + UP * 1.7 + LEFT * 3.4)
        d_e = Dot(sc + UP * 1.1 + RIGHT * 3.6, color=RED)
        l_e = Tex(r"East: Burgersfort").scale(0.85).shift(sc + UP * 1.7 + RIGHT * 3.5)
        d_n = Dot(sc + UP * 1.1 + RIGHT * 0.0, color=RED)
        l_n = Tex(r"North: Mokopane").scale(0.85).shift(sc + UP * 1.6)
        self.play(Create(d_w), Write(l_w)); self.wait(1.3)
        self.play(Create(d_e), Write(l_e)); self.wait(1.3)
        self.play(Create(d_n), Write(l_n)); self.wait(1.3)
        b2_l2 = Tex(r"Metal in thin horizons: Merensky Reef, UG2").scale(0.95).shift(sc + DOWN * 2.3)
        self.play(Write(b2_l2))
        self.wait(3)

        # --- Band 3 (subtopic_2): five families of favouring factors ---
        self.next_band(3)
        b3_t = Tex("Why South Africa leads: five factor families").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        rows = [
            r"Geological: huge, high-grade, predictable layers",
            r"Historical: a century of deep-mining skill",
            r"Infrastructural: Gauteng's rail, power, water",
            r"Labour: an established mining workforce",
            r"Market: autocatalysts, jewellery, hydrogen",
        ]
        for i, txt in enumerate(rows):
            m = Tex(txt).scale(1.0).shift(band_shift(3) + UP * (1.1 - 0.85 * i))
            self.play(Write(m))
            self.wait(1.8)
        self.wait(2.5)

        # --- Band 4 (subtopic_3): platinum's contribution, counted properly ---
        self.next_band(4)
        b4_t = Tex("Platinum's contribution").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex(r"Among the largest export earners").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"$\pm$170 000 direct jobs --- mining's biggest").scale(1.05).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex(r"Anchors North West; Rustenburg grew on it").scale(1.05).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex(r"Beneficiation: smelters and refineries add").scale(1.05).shift(band_shift(4) + DOWN * 1.3)
        b4_l5 = Tex(r"value locally before export").scale(1.05).shift(band_shift(4) + DOWN * 2.0)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4, b4_l5):
            self.play(Write(m))
            self.wait(1.8)
        self.wait(2)

        # --- Band 5 (subtopic_3): the two baskets of hindering factors ---
        self.next_band(5)
        b5_t = Tex("Hindering factors --- two baskets").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex(r"Physical: reefs $\pm$1 m thin, deep, hot,").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"hard to mechanise; energy-hungry smelting").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1)); self.wait(1.6)
        self.play(Write(b5_l2)); self.wait(2)
        b5_l3 = Tex(r"Economic-social: load-shedding stalls smelters,").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex(r"volatile prices, strikes --- Marikana 2012 ---").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        b5_l5 = Tex(r"rising costs, failing rail, EV demand risk").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l3)); self.wait(1.6)
        self.play(Write(b5_l4)); self.wait(1.6)
        self.play(Write(b5_l5)); self.wait(1.6)
        b5_l6 = Tex(r"Verdict: a pillar, but a pillar under strain").scale(1.05).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the mine's signature on the map, drawn ---
        self.next_band(6)
        b6_t = Tex("A mine's signature on the map").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        sc6 = band_shift(6)
        # main railway line with a spur dead-ending at the works
        main_rail = Line(sc6 + DOWN * 1.9 + LEFT * 4.2, sc6 + DOWN * 1.9 + RIGHT * 4.2, stroke_width=4)
        self.play(Create(main_rail))
        spur = Line(sc6 + DOWN * 1.9 + LEFT * 1.0, sc6 + UP * 0.2 + LEFT * 1.0, stroke_width=4)
        self.play(Create(spur))
        l_spur = Tex(r"rail spur to nowhere").scale(0.85).shift(sc6 + DOWN * 0.9 + LEFT * 2.9)
        self.play(Write(l_spur))
        self.wait(1.5)
        works = Rectangle(width=1.4, height=0.7).shift(sc6 + UP * 0.6 + LEFT * 1.0)
        l_works = Tex(r"works").scale(0.8).shift(sc6 + UP * 0.6 + LEFT * 1.0)
        self.play(Create(works), Write(l_works))
        self.wait(1.5)
        dump1 = Rectangle(width=1.2, height=0.6, color=YELLOW).shift(sc6 + UP * 0.6 + RIGHT * 1.2)
        dump2 = Rectangle(width=1.2, height=0.6, color=YELLOW).shift(sc6 + DOWN * 0.4 + RIGHT * 1.2)
        l_dump = Tex(r"dumps and slimes dams:").scale(0.85).shift(sc6 + UP * 1.5 + RIGHT * 2.2)
        l_dump2 = Tex(r"straight edges give them away").scale(0.85).shift(sc6 + UP * 1.0 + RIGHT * 2.4)
        self.play(Create(dump1), Create(dump2))
        self.play(Write(l_dump), Write(l_dump2))
        self.wait(2)
        pw = Line(sc6 + UP * 1.6 + LEFT * 4.2, sc6 + UP * 0.9 + LEFT * 1.6, color=BLUE, stroke_width=3)
        l_pw = Tex(r"power lines converge").scale(0.85).shift(sc6 + UP * 1.9 + LEFT * 2.9)
        self.play(Create(pw), Write(l_pw))
        self.wait(1.5)
        b6_l1 = Tex(r"Plus the word itself: Mine, Myn, Colliery").scale(0.95).shift(sc6 + DOWN * 2.7)
        self.play(Write(b6_l1))
        self.wait(3)

        # --- Band 7 (subtopic_4): grid references and the symbol code ---
        self.next_band(7)
        b7_t = Tex("References and symbols").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex(r"Six figures: eastings first, then northings").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"``Along the corridor, then up the stairs''").scale(1.05).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1)); self.wait(1.8)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_wrong = Tex(r"Northings first --- reversed pair, mark lost").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2)
        b7_l3 = Tex(r"Colours: blue water, green vegetation,").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        b7_l4 = Tex(r"brown contours, black/red human works").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l3)); self.wait(1.6)
        self.play(Write(b7_l4)); self.wait(1.6)
        b7_l5 = Tex(r"The legend is printed --- check, never guess").scale(1.0).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the country that dug itself into existence ---
        self.next_band(8)
        b8_t = Tex("The country that dug itself into existence").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex(r"Joburg: no river, no harbour --- just gold, 1886").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1)); self.wait(2)
        b8_l2 = Tex(r"Everything else came running: railways,").scale(1.0).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex(r"power stations, factories, the JSE, towns").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l2)); self.wait(1.8)
        self.play(Write(b8_l3)); self.wait(2)
        b8_l4 = Tex(r"Exports: the family member working overseas").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        b8_l5 = Tex(r"whose payments balance the account").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l4)); self.wait(1.8)
        self.play(Write(b8_l5)); self.wait(1.8)
        b8_l6 = Tex(r"But the land remembers: the foundation AND the bill").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): the buried saucer, four lucky cards ---
        self.next_band(9)
        b9_t = Tex("The buried saucer full of platinum").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex(r"Cooling rock settled in layers, like soup").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"Rim surfaces in three arcs of mines").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1)); self.wait(1.8)
        self.play(Write(b9_l2)); self.wait(2)
        b9_l3 = Tex(r"Card 1: most of the world's platinum here").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex(r"Card 2: gold-era deep-mining know-how").scale(1.0).shift(band_shift(9) + DOWN * 1.1)
        b9_l5 = Tex(r"Card 3: Gauteng's infrastructure next door").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        b9_l6 = Tex(r"Card 4: a hungry world market --- exhausts").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        for m in (b9_l3, b9_l4, b9_l5, b9_l6):
            self.play(Write(m))
            self.wait(1.7)
        self.play(Create(SurroundingRectangle(VGroup(b9_l3, b9_l4, b9_l5, b9_l6), color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): reading the treasure map ---
        self.next_band(10)
        b10_t = Tex("Reading the treasure map").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex(r"Look for shapes nature refuses to make:").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex(r"straight-edged dumps, square dams, pits,").scale(1.0).shift(band_shift(10) + UP * 0.4)
        b10_l3 = Tex(r"a rail spur dead-ending in open veld").scale(1.0).shift(band_shift(10) + DOWN * 0.3)
        for m in (b10_l1, b10_l2, b10_l3):
            self.play(Write(m))
            self.wait(1.7)
        b10_l4 = Tex(r"Evidence $+$ its grid reference, every time").scale(1.0).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex(r"Chant: along the corridor, then up the stairs").scale(1.0).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(b10_l5)); self.wait(1.8)
        b10_l6 = Tex(r"Behind the map stands the saucer: platinum").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l6))
        self.wait(4)
