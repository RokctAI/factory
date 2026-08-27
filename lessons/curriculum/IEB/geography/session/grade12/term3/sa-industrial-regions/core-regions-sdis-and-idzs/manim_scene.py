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

# Band-layout whiteboard scene for the IEB Grade 12 Geography session duo
# "Core Regions, SDIs and IDZs". Bands cover all seven subtopics (Part 1 —
# Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7) with dwell time
# proportional to subtopics.json (225/245/240/250/210/240/250 of 1660 s).
# The four-engine sketch and the Maputo corridor are hand-built from
# exporter-safe primitives only (Tex/Line/Arrow/Dot/Rectangle/VGroup);
# add-only lifecycle, the camera moves down between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CoreRegionsSdisIdzsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # --- Band 0 (subtopic_1): the four regions and the one-line secret ---
        title = Tex("SA Industrial Regions, SDIs and IDZs").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"1. Gauteng --- the PWV (inland colossus)").scale(1.05).shift(UP * 0.9)
        b0_l2 = Tex(r"2. Durban--Pinetown (busiest harbour)").scale(1.05).shift(UP * 0.1)
        b0_l3 = Tex(r"3. Port Elizabeth--Uitenhage (motor coast)").scale(1.05).shift(DOWN * 0.7)
        b0_l4 = Tex(r"4. South-Western Cape (consumer goods)").scale(1.05).shift(DOWN * 1.5)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(1.8)
        b0_l5 = Tex(r"Minerals built Gauteng; harbours built the rest").scale(1.0).shift(DOWN * 2.5)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the four-row case study grid ---
        self.next_band(1)
        b1_t = Tex("The case-study grid: four rows").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex(r"WHY there --- location factors").scale(1.1).shift(band_shift(1) + UP * 1.0)
        b1_l2 = Tex(r"WHAT happens --- main activities").scale(1.1).shift(band_shift(1) + UP * 0.1)
        b1_l3 = Tex(r"HOW it fares --- favouring and hindering").scale(1.1).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = Tex(r"WHO feels it --- economic and social impacts").scale(1.1).shift(band_shift(1) + DOWN * 1.7)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(1.9)
        b1_l5 = Tex(r"Four rows $\times$ two case-study regions").scale(1.05).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): Gauteng — why there ---
        self.next_band(2)
        b2_t = Tex("Gauteng (PWV): why there").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        rows = [
            r"Gold pulled capital, labour, railways",
            r"Coal next door fed cheap power",
            r"Water piped in: Vaal Dam, Lesotho",
            r"Rail hub + OR Tambo air freight",
            r"Skills pool + Africa's richest market",
        ]
        for i, txt in enumerate(rows):
            m = Tex(txt).scale(1.05).shift(band_shift(2) + UP * (1.1 - 0.8 * i))
            self.play(Write(m))
            self.wait(1.7)
        b2_l6 = Tex(r"The gold is nearly gone --- the region is not").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): Gauteng — activities, hindrances, impacts ---
        self.next_band(3)
        b3_t = Tex("Gauteng: what, how, who").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex(r"Vanderbijlpark steel, Sasolburg chemicals,").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex(r"Rosslyn vehicles, banks and head offices").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1)); self.wait(1.6)
        self.play(Write(b3_l2)); self.wait(2)
        b3_l3 = Tex(r"Strains: NO PORT, water pumped uphill,").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex(r"load-shedding, congestion, Vaal smoke").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_l3)); self.wait(1.6)
        self.play(Write(b3_l4)); self.wait(2)
        b3_l5 = Tex(r"A third of GDP --- yet Sandton faces Alexandra").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): PE–Uitenhage — the motor town ---
        self.next_band(4)
        b4_t = Tex("Port Elizabeth--Uitenhage: the motor town").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex(r"Natural harbour on Algoa Bay + rail to the Karoo").scale(0.95).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"Car makers chose it: VW at Kariega, Isuzu").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex(r"Component belt: catalytic converters").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex(r"(platinum's thread), plus Ngqura deep water").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(1.8)
        b4_l5 = Tex(r"Port, rail, chosen by car makers").scale(1.05).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): PE–Uitenhage — risk and impacts ---
        self.next_band(5)
        b5_t = Tex("Strength and fragility, one postcode").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex(r"Favouring: automotive skill, export deals,").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"two harbours, Coega next door").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1)); self.wait(1.6)
        self.play(Write(b5_l2)); self.wait(2)
        b5_l3 = Tex(r"Hindering: ONE industry --- a slump in car").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex(r"demand shakes the region; drought scares,").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        b5_l5 = Tex(r"load-shedding, deep unemployment").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        for m in (b5_l3, b5_l4, b5_l5):
            self.play(Write(m))
            self.wait(1.7)
        b5_l6 = Tex(r"Good wages inside the fence, poverty outside").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): SDIs and the Maputo corridor, drawn ---
        self.next_band(6)
        b6_t = Tex("SDIs: invest along a corridor").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        sc6 = band_shift(6)
        d_g = Dot(sc6 + UP * 0.8 + LEFT * 3.6, color=YELLOW)
        l_g = Tex("Gauteng").scale(0.95).shift(sc6 + UP * 1.3 + LEFT * 3.6)
        d_m = Dot(sc6 + UP * 0.8 + RIGHT * 3.6, color=YELLOW)
        l_m = Tex("Maputo port").scale(0.95).shift(sc6 + UP * 1.3 + RIGHT * 3.6)
        self.play(Create(d_g), Write(l_g))
        self.play(Create(d_m), Write(l_m))
        self.wait(1.5)
        corridor = Arrow(sc6 + UP * 0.8 + LEFT * 3.3, sc6 + UP * 0.8 + RIGHT * 3.3, color=GREEN, buff=0.1)
        l_c = Tex(r"Maputo Development Corridor").scale(0.95).shift(sc6 + UP * 0.15)
        self.play(Create(corridor), Write(l_c))
        self.wait(2)
        b6_l1 = Tex(r"Upgrade the whole road-rail artery;").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        b6_l2 = Tex(r"industry sprouts all along the line").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l1)); self.wait(1.6)
        self.play(Write(b6_l2)); self.wait(2)
        b6_l3 = Tex(r"Also: Lubombo, Wild Coast, West Coast").scale(1.0).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l3))
        self.wait(3)

        # --- Band 7 (subtopic_4): IDZs, SEZs and the balanced verdict ---
        self.next_band(7)
        b7_t = Tex("IDZs inside the SEZ framework").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex(r"Recipe: serviced estate at a port, tax breaks,").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"duty-free inputs, one-stop services").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1)); self.wait(1.6)
        self.play(Write(b7_l2)); self.wait(2)
        b7_l3 = Tex(r"Coega (flagship), East London, Richards Bay,").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex(r"Dube TradePort, Saldanha Bay").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3)); self.wait(1.6)
        self.play(Write(b7_l4)); self.wait(2)
        b7_l5 = Tex(r"Verdict: real jobs at the margin --- the").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        b7_l6 = Tex(r"four-region pattern still stands").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5)); self.wait(1.5)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): four engines pulling one train ---
        self.next_band(8)
        b8_t = Tex("Four engines pulling one train").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        sc8 = band_shift(8)
        track = Line(sc8 + UP * 0.1 + LEFT * 4.4, sc8 + UP * 0.1 + RIGHT * 4.4, stroke_width=4)
        self.play(Create(track))
        e_names = ["Gauteng", "Durban--\\\\Pinetown", "PE--\\\\Uitenhage", "SW Cape"]
        for i, name in enumerate(e_names):
            ex = -3.15 + 2.1 * i
            e_rect = Rectangle(width=1.8, height=1.1, color=YELLOW).shift(sc8 + UP * 0.75 + RIGHT * ex)
            e_lab = Tex(name).scale(0.7).shift(sc8 + UP * 0.75 + RIGHT * ex)
            self.play(Create(e_rect), Write(e_lab))
            self.wait(1.2)
        b8_l1 = Tex(r"Minerals built the inland engine;").scale(1.0).shift(sc8 + DOWN * 2.0)
        b8_l2 = Tex(r"harbours built the coastal three").scale(1.0).shift(sc8 + DOWN * 2.7)
        self.play(Write(b8_l1)); self.wait(1.6)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the engine that outlived its gold ---
        self.next_band(9)
        b9_t = Tex("The engine that outlived its gold").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex(r"No port: exports ride 600 km to Durban").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"No great river: water pumped from Lesotho").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1)); self.wait(1.8)
        self.play(Write(b9_l2)); self.wait(2)
        b9_l3 = Tex(r"So why a third of the economy up there?").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3)); self.wait(1.8)
        b9_l4 = Tex(r"The engine outlived the gold that built it:").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        b9_l5 = Tex(r"rails, skills, market, linked factories remain").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l4)); self.wait(1.6)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(VGroup(b9_l4, b9_l5), color=GREEN)))
        self.wait(2)
        b9_l6 = Tex(r"Wealth and want one window apart: Sandton, Alex").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_7): the car town, and starting new engines ---
        self.next_band(10)
        b10_t = Tex("The car town, and starting new engines").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex(r"Six words: port, rail, chosen by car makers").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1)); self.wait(2)
        b10_l2 = Tex(r"One-industry risk: when cars stop selling,").scale(1.0).shift(band_shift(10) + UP * 0.3)
        b10_l3 = Tex(r"the whole town holds its breath").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l2)); self.wait(1.6)
        self.play(Write(b10_l3)); self.wait(2)
        b10_l4 = Tex(r"SDI $=$ upgraded artery (Maputo Corridor)").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        b10_l5 = Tex(r"IDZ $=$ furnished flat for factories (Coega)").scale(1.0).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l4)); self.wait(1.8)
        self.play(Write(b10_l5)); self.wait(1.8)
        b10_l6 = Tex(r"Honest verdict: coupled, but still small").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
