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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex keep the export to the
# allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/210/220/190/190/180 of
# 1440 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GlobalEconomySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Globalisation and Why Countries Trade
        b0_title = Tex("Globalisation").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Flows: goods, money, technology, people").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Resources and climates differ").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Specialise, then trade").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Comparative advantage: Ricardo, 1817").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Imports, Exports, the Balance of Trade and Exchange Rates
        self.next_band(1)
        b1_title = Tex("Trade and exchange rates").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Exports in, imports out").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("R150m - R120m = R30m surplus").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("500 dollars at R18 = R9 000").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Weaker rand: imports dearer, exports cheaper").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): International Organisations and Trade Agreements
        self.next_band(2)
        b2_title = Tex("Rules of world trade").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Tariff: tax on imports; quota: limit").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("WTO 1995; IMF and World Bank 1944").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("SACU 1910; SADC; AfCFTA 2021").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("BRICS: SA invited 2010; G20").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Benefits and Costs of Globalisation for South Africa
        self.next_band(3)
        b3_title = Tex("Benefits and costs").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Plus: markets, jobs, choice, investment").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Minus: lost jobs in clothing").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Minus: shocks of 2008 and 2020").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Minus: profits flow out, inequality").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Benefits and Costs of Globalisation for South Africa
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``A weaker rand makes imports cheaper''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``A trade deficit means bankruptcy''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Globalisation is only goods''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``You must be best to export''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Journey of a Cellphone
        self.next_band(5)
        b5_title = Tex("Journey of a cellphone").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Designed, chips, metals, assembled").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Ship to Durban, truck to your town").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Export: money in").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Import: money out").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Rands and Dollars at the Border
        self.next_band(6)
        b6_title = Tex("Rands and dollars").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("50 x R18 = R900").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("50 x R20 = R1 000").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Oranges R180: 10 dollars, then 9").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Weak rand helps exporters").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Winners and Losers in the Global Village
        self.next_band(7)
        b7_title = Tex("Winners and losers").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Winners: car exports, tourism, choice").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Losers: clothing factories").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Rule makers: WTO, SACU, AfCFTA").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Tariff protects local jobs").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l1, color=YELLOW)))
        self.wait(4)
