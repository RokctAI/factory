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

# Band-layout whiteboard scene for the IEB Grade 12 Geography session duo
# "Mining and the Platinum Case Study". Bands cover all seven subtopics
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7) with
# dwell time proportional to subtopics.json (240/230/240/240/220/230/230 of
# 1630 s). The Bushveld saucer cross-section and the mine's map signature are
# hand-built from exporter-safe primitives only (Tex/Line/Arrow/Dot/
# Rectangle/VGroup); add-only lifecycle, the camera moves down between bands.

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
        title = Tex("Mining and the Platinum Case Study").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"1867 Kimberley diamonds, 1886 Wits gold").scale(1.0).shift(UP * 0.9)
        b0_l2 = Tex(r"Mines demanded rail, power, machines, money").scale(1.0).shift(UP * 0.1)
        b0_l3 = Tex(r"JSE born to fund the goldfields;").scale(1.0).shift(DOWN * 0.7)
        b0_l4 = Tex(r"Johannesburg built on gold, not water").scale(1.0).shift(DOWN * 1.4)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(1.9)
        b0_l5 = Tex(r"Foundation: the house was built on mining").scale(1.0).shift(DOWN * 2.4)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): today's contribution and the cost column ---
        self.next_band(1)
        b1_t = Tex("Today: contribution and cost").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex(r"Under 10\% of GDP, under 500 000 jobs,").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex(r"BUT an outsized share of export earnings").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1)); self.wait(1.7)
        self.play(Write(b1_l2)); self.wait(2)
        b1_l3 = Tex(r"PGMs, coal, iron ore, gold, manganese").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l3)); self.wait(1.8)
        b1_l4 = Tex(r"Costs: acid mine water, dust, sinkholes,").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        b1_l5 = Tex(r"silicosis, stranded one-purpose towns").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4)); self.wait(1.7)
        self.play(Write(b1_l5)); self.wait(1.7)
        b1_l6 = Tex(r"Critical answers carry both columns").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the Bushveld saucer, drawn in cross-section ---
        self.next_band(2)
        b2_t = Tex("The Bushveld Igneous Complex").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        sc2 = band_shift(2)
        ground = Line(sc2 + UP * 1.0 + LEFT * 4.5, sc2 + UP * 1.0 + RIGHT * 4.5, stroke_width=3)
        self.play(Create(ground))
        saucer_l = Line(sc2 + UP * 1.0 + LEFT * 3.8, sc2 + DOWN * 0.6, color=YELLOW, stroke_width=5)
        saucer_r = Line(sc2 + DOWN * 0.6, sc2 + UP * 1.0 + RIGHT * 3.8, color=YELLOW, stroke_width=5)
        self.play(Create(saucer_l), Create(saucer_r))
        self.wait(1.5)
        lab_m = Tex(r"Merensky Reef + UG2: thin platinum bands").scale(0.9).shift(sc2 + DOWN * 1.3)
        self.play(Write(lab_m))
        self.wait(2)
        d_w = Dot(sc2 + UP * 1.0 + LEFT * 3.8, color=GREEN)
        l_w = Tex("western limb\\\\Rustenburg").scale(0.7).shift(sc2 + UP * 1.7 + LEFT * 3.8)
        d_e = Dot(sc2 + UP * 1.0 + RIGHT * 3.8, color=GREEN)
        l_e = Tex("eastern limb\\\\Burgersfort").scale(0.7).shift(sc2 + UP * 1.7 + RIGHT * 3.8)
        self.play(Create(d_w), Write(l_w)); self.wait(1.5)
        self.play(Create(d_e), Write(l_e)); self.wait(1.5)
        b2_l1 = Tex(r"Northern limb near Mokopane; capital: Rustenburg").scale(0.9).shift(sc2 + DOWN * 2.2)
        self.play(Write(b2_l1))
        self.wait(3)

        # --- Band 3 (subtopic_2): five families of favouring factors ---
        self.next_band(3)
        b3_t = Tex("Five families of favouring factors").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        rows = [
            r"Geology: vast, high-grade, predictable layers",
            r"History: a century of deep-mining craft",
            r"Infrastructure: Gauteng's rail and power near",
            r"Labour: an established mining workforce",
            r"Market: autocatalysts, jewellery, hydrogen",
        ]
        for i, txt in enumerate(rows):
            m = Tex(txt).scale(0.95).shift(band_shift(3) + UP * (1.2 - 0.75 * i))
            self.play(Write(m))
            self.wait(1.7)
        b3_l6 = Tex(r"The world's car industry needs this metal").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): platinum's contribution, counted ---
        self.next_band(4)
        b4_t = Tex("Platinum's contribution").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex(r"Top of the mineral export table").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"$\pm$170 000 direct jobs --- mining's largest").scale(1.0).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex(r"Anchors North West and the eastern limb").scale(1.0).shift(band_shift(4) + DOWN * 0.3)
        for m in (b4_l1, b4_l2, b4_l3):
            self.play(Write(m))
            self.wait(1.8)
        b4_l4 = Tex(r"Beneficiation: smelters and refineries").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        b4_l5 = Tex(r"add value at home before export").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4)); self.wait(1.6)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the two baskets of hindering factors ---
        self.next_band(5)
        b5_t = Tex("Hindering factors: two baskets").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex(r"Physical: metre-thin, deepening reefs ---").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"hot, hand-drilled, hard to mechanise").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1)); self.wait(1.7)
        self.play(Write(b5_l2)); self.wait(2)
        b5_l3 = Tex(r"Economic-social: load-shedding, price swings,").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex(r"strikes and the Marikana legacy, EV risk").scale(0.95).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3)); self.wait(1.7)
        self.play(Write(b5_l4)); self.wait(2)
        b5_l5 = Tex(r"Verdict: a pillar under strain").scale(1.05).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the mine's signature on the map, drawn ---
        self.next_band(6)
        b6_t = Tex("A mine's signature on the sheet").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        sc6 = band_shift(6)
        dump = Rectangle(width=1.6, height=0.7, color=YELLOW).shift(sc6 + UP * 0.9 + LEFT * 3.0)
        l_dump = Tex("dump").scale(0.75).shift(sc6 + UP * 1.8 + LEFT * 3.0)
        dam = Rectangle(width=1.2, height=1.2, color=BLUE).shift(sc6 + UP * 0.9 + LEFT * 0.4)
        l_dam = Tex("slimes dam").scale(0.75).shift(sc6 + UP * 1.8 + LEFT * 0.4)
        self.play(Create(dump), Write(l_dump)); self.wait(1.5)
        self.play(Create(dam), Write(l_dam)); self.wait(1.5)
        rail = Line(sc6 + UP * 0.2 + RIGHT * 4.4, sc6 + UP * 0.2 + RIGHT * 1.4, stroke_width=4)
        works = Rectangle(width=1.0, height=0.7, color=RED).shift(sc6 + UP * 0.2 + RIGHT * 0.7)
        l_rail = Tex("rail spur dead-ends at the works").scale(0.75).shift(sc6 + DOWN * 0.6 + RIGHT * 2.4)
        self.play(Create(rail), Create(works), Write(l_rail))
        self.wait(2)
        b6_l1 = Tex(r"Straight edges: shapes nature refuses to make").scale(0.95).shift(sc6 + DOWN * 1.5)
        self.play(Write(b6_l1)); self.wait(1.7)
        b6_l2 = Tex(r"Plus: Mine / Myn / Colliery printed on the map").scale(0.95).shift(sc6 + DOWN * 2.3)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): grid references and the symbol code ---
        self.next_band(7)
        b7_t = Tex("Grid references and the colour code").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex(r"Six figures: eastings first, then northings").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"Along the corridor, then up the stairs").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1)); self.wait(1.7)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex(r"Blue water, green vegetation,").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex(r"brown contours, black and red built things").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3)); self.wait(1.6)
        self.play(Write(b7_l4)); self.wait(1.8)
        b7_l5 = Tex(r"The legend is printed --- check, never guess").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the country that dug itself into existence ---
        self.next_band(8)
        b8_t = Tex("The country that dug itself into existence").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex(r"Joburg: no river, no harbour --- just gold").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1)); self.wait(2)
        b8_l2 = Tex(r"Mines dragged rails, power, factories,").scale(1.0).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex(r"banks and towns into existence").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l2)); self.wait(1.6)
        self.play(Write(b8_l3)); self.wait(2)
        b8_l4 = Tex(r"Exports: SA's stall at the world's market ---").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        b8_l5 = Tex(r"it pays for the petrol, phones, machines").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l4)); self.wait(1.6)
        self.play(Write(b8_l5)); self.wait(1.8)
        b8_l6 = Tex(r"But the land keeps the bill: acid water, dust").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): the buried saucer, four ingredients ---
        self.next_band(9)
        b9_t = Tex("The buried saucer full of platinum").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex(r"Bushveld: minerals settled in flat bands,").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"like silt in a still dam --- Merensky, UG2").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1)); self.wait(1.7)
        self.play(Write(b9_l2)); self.wait(2)
        b9_l3 = Tex(r"Four ingredients: deposit, craft,").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex(r"next-door infrastructure, hungry market").scale(1.0).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l3)); self.wait(1.6)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(VGroup(b9_l3, b9_l4), color=GREEN)))
        self.wait(2)
        b9_l5 = Tex(r"But: metre-thin bands, kilometres deep ---").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        b9_l6 = Tex(r"the jam layer inside a giant cake").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5)); self.wait(1.6)
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_7): reading the treasure map ---
        self.next_band(10)
        b10_t = Tex("Reading the treasure map").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex(r"Hunt shapes nature refuses to make:").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex(r"straight dumps, square dams, toothed pits,").scale(1.0).shift(band_shift(10) + UP * 0.4)
        b10_l3 = Tex(r"a rail spur dead-ending in open veld").scale(1.0).shift(band_shift(10) + DOWN * 0.3)
        for m in (b10_l1, b10_l2, b10_l3):
            self.play(Write(m))
            self.wait(1.8)
        b10_l4 = Tex(r"Evidence $+$ its grid reference, every time").scale(1.0).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex(r"Chant: along the corridor, then up the stairs").scale(1.0).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(b10_l5)); self.wait(1.8)
        b10_l6 = Tex(r"Behind the map stands the saucer: platinum").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l6))
        self.wait(4)
