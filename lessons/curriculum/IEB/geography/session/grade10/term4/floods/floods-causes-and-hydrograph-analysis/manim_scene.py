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

# Band-layout whiteboard scene for "Floods: Causes and Hydrograph Analysis"
# (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier 5-7). Exporter-safe
# primitives only: the hydrograph is hand-built from Arrow axes, Rectangle
# rain bars and chained Line segments, labelled as it grows; the urban-vs-
# rural comparison overlays two Line-chain curves. Add-only lifecycle;
# camera moves down band by band. Band time apportioned to subtopics.json
# (240/235/250/240/185/185/165 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class FloodsHydrographSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the rain's character ---
        title = Tex("Floods and the Hydrograph").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Flood: water covers land that is usually dry").scale(1.0).shift(UP * 1.1)
        self.play(Write(d1))
        self.wait(2)
        d2 = Tex("INTENSITY beats total:").scale(1.05).shift(UP * 0.2)
        d3 = Tex("60 mm in 90 minutes runs off; over a fortnight it soaks in").scale(0.9).shift(DOWN * 0.6)
        self.play(Write(d2))
        self.play(Write(d3))
        self.wait(2.5)
        d4 = Tex("Cut-off low: stalled cold pool, days of rain").scale(0.95).shift(DOWN * 1.5)
        d5 = Tex("Natal Sept 1987, Western Cape 2023;").scale(0.95).shift(DOWN * 2.3)
        d6 = Tex("cyclones Domoina 1984, Dineo 2017 in the north-east").scale(0.9).shift(DOWN * 3.1)
        self.play(Write(d4))
        self.wait(2)
        self.play(Write(d5))
        self.play(Write(d6))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): five catchment properties ---
        self.next_band(1)
        b1_title = Tex("Five properties of the catchment").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        c1 = Tex("Antecedent moisture: full soil turns rain to runoff").scale(0.9).shift(band_shift(1) + UP * 1.2)
        c2 = Tex("Slope: steep gradients outrun infiltration").scale(0.95).shift(band_shift(1) + UP * 0.4)
        c3 = Tex("Rock and soil: shale rejects, deep sand swallows").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        c4 = Tex("Vegetation: intercepts, slows, keeps soil open").scale(0.95).shift(band_shift(1) + DOWN * 1.2)
        c5 = Tex("Shape: a round catchment arrives all at once").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2)
        self.play(Write(c4))
        self.wait(2)
        self.play(Write(c5))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the human hand ---
        self.next_band(2)
        b2_title = Tex("The human hand in flooding").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        h1 = Tex("1. Urbanisation: sealed ground plus stormwater").scale(0.95).shift(band_shift(2) + UP * 1.2)
        h1b = Tex("pipes aimed at the river (the Jukskei)").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(h1))
        self.play(Write(h1b))
        self.wait(2.5)
        h2 = Tex("2. Stripped vegetation; silt raises beds and dams").scale(0.9).shift(band_shift(2) + DOWN * 0.4)
        h3 = Tex("3. Wetlands drained: free flood storage lost").scale(0.95).shift(band_shift(2) + DOWN * 1.2)
        h4 = Tex("4. Blocked drains, small culverts, tired dams").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(h2))
        self.wait(2)
        self.play(Write(h3))
        self.wait(2)
        self.play(Write(h4))
        self.wait(2)
        h5 = Tex("5. Floodplain settlement: exposure maps onto poverty").scale(0.9).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(h5))
        self.play(Create(SurroundingRectangle(h5, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): the hydrograph, built line by line ---
        self.next_band(3)
        b3_title = Tex("The flood hydrograph").scale(1.15).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_title))
        self.wait(1.5)
        o = band_shift(3) + LEFT * 4.8 + DOWN * 2.4
        x_ax = Arrow(o, o + RIGHT * 9.4, buff=0, stroke_width=4)
        y_ax = Arrow(o, o + UP * 4.4, buff=0, stroke_width=4)
        x_lab = Tex("time").scale(0.8).shift(band_shift(3) + RIGHT * 4.6 + DOWN * 2.9)
        y_lab = Tex("discharge (cumecs)").scale(0.8).shift(band_shift(3) + LEFT * 2.9 + UP * 2.1)
        self.play(Create(x_ax), Create(y_ax))
        self.play(Write(x_lab), Write(y_lab))
        self.wait(1.5)
        rain1 = Rectangle(width=0.4, height=1.2).shift(o + RIGHT * 0.9 + UP * 0.6)
        rain2 = Rectangle(width=0.4, height=2.0).shift(o + RIGHT * 1.35 + UP * 1.0)
        rain3 = Rectangle(width=0.4, height=0.9).shift(o + RIGHT * 1.8 + UP * 0.45)
        rain_lab = Tex("rain").scale(0.7).shift(o + RIGHT * 1.35 + UP * 2.4)
        self.play(Create(rain1), Create(rain2), Create(rain3), Write(rain_lab))
        self.wait(1.5)
        base1 = Line(o + UP * 0.5, o + RIGHT * 2.6 + UP * 0.55, color=BLUE, stroke_width=5)
        base_lab = Tex("base flow").scale(0.7).shift(o + RIGHT * 1.6 + UP * 0.15)
        self.play(Create(base1), Write(base_lab))
        self.wait(2)
        rise1 = Line(o + RIGHT * 2.6 + UP * 0.55, o + RIGHT * 3.5 + UP * 2.2, color=BLUE, stroke_width=5)
        rise2 = Line(o + RIGHT * 3.5 + UP * 2.2, o + RIGHT * 4.1 + UP * 3.5, color=BLUE, stroke_width=5)
        rise_lab = Tex("rising limb (steep)").scale(0.7).shift(o + RIGHT * 2.0 + UP * 3.0)
        self.play(Create(rise1), Create(rise2), Write(rise_lab))
        self.wait(2)
        peak = Dot(o + RIGHT * 4.1 + UP * 3.5, color=RED)
        peak_lab = Tex("peak discharge").scale(0.7).shift(o + RIGHT * 4.3 + UP * 4.0)
        self.play(FadeIn(peak), Write(peak_lab))
        self.wait(1.5)
        lag = Arrow(o + RIGHT * 1.35 + UP * 0.15, o + RIGHT * 4.1 + UP * 0.15,
                    buff=0, color=YELLOW, stroke_width=4)
        lag_lab = Tex("lag time").scale(0.7).shift(o + RIGHT * 2.8 + DOWN * 0.35)
        self.play(Create(lag), Write(lag_lab))
        self.wait(2)
        fall1 = Line(o + RIGHT * 4.1 + UP * 3.5, o + RIGHT * 5.9 + UP * 2.0, color=BLUE, stroke_width=5)
        fall2 = Line(o + RIGHT * 5.9 + UP * 2.0, o + RIGHT * 7.5 + UP * 1.05, color=BLUE, stroke_width=5)
        fall3 = Line(o + RIGHT * 7.5 + UP * 1.05, o + RIGHT * 9.0 + UP * 0.75, color=BLUE, stroke_width=5)
        fall_lab = Tex("falling limb (gentler)").scale(0.7).shift(o + RIGHT * 7.2 + UP * 2.6)
        self.play(Create(fall1), Write(fall_lab))
        self.play(Create(fall2), Create(fall3))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the three readings ---
        self.next_band(4)
        b4_title = Tex("Three readings, only three").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        r1 = Tex("1. How HIGH did the discharge peak?").scale(1.05).shift(band_shift(4) + UP * 1.2)
        r2 = Tex("2. How SHORT was the lag?").scale(1.05).shift(band_shift(4) + UP * 0.4)
        r3 = Tex("3. How STEEP were the limbs?").scale(1.05).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(r1))
        self.wait(1.5)
        self.play(Write(r2))
        self.wait(1.5)
        self.play(Write(r3))
        self.wait(2)
        r4 = Tex("High + short + steep = FLASHY catchment").scale(1.05).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(r4))
        self.play(Create(SurroundingRectangle(r4, color=GREEN)))
        self.wait(2)
        r5 = Tex("Low + long + gentle = absorbent catchment").scale(1.0).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(r5))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): one storm, two catchments ---
        self.next_band(5)
        b5_title = Tex("One storm, two catchments").scale(1.15).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_title))
        self.wait(1.5)
        o5 = band_shift(5) + LEFT * 4.8 + DOWN * 2.4
        x5 = Arrow(o5, o5 + RIGHT * 9.4, buff=0, stroke_width=4)
        y5 = Arrow(o5, o5 + UP * 4.4, buff=0, stroke_width=4)
        self.play(Create(x5), Create(y5))
        # urban spike: short lag, high narrow peak
        u1 = Line(o5 + UP * 0.4, o5 + RIGHT * 1.3 + UP * 0.45, color=RED, stroke_width=5)
        u2 = Line(o5 + RIGHT * 1.3 + UP * 0.45, o5 + RIGHT * 2.3 + UP * 3.8, color=RED, stroke_width=5)
        u3 = Line(o5 + RIGHT * 2.3 + UP * 3.8, o5 + RIGHT * 3.5 + UP * 1.0, color=RED, stroke_width=5)
        u4 = Line(o5 + RIGHT * 3.5 + UP * 1.0, o5 + RIGHT * 5.0 + UP * 0.4, color=RED, stroke_width=5)
        u_lab = Tex("urbanised: short lag, high peak").scale(0.75).shift(o5 + RIGHT * 4.7 + UP * 3.9)
        self.play(Create(u1), Create(u2))
        self.play(Create(u3), Create(u4), Write(u_lab))
        self.wait(2)
        # rural mound: long lag, low broad peak
        g1 = Line(o5 + UP * 0.5, o5 + RIGHT * 2.7 + UP * 0.7, color=GREEN, stroke_width=5)
        g2 = Line(o5 + RIGHT * 2.7 + UP * 0.7, o5 + RIGHT * 4.7 + UP * 1.7, color=GREEN, stroke_width=5)
        g3 = Line(o5 + RIGHT * 4.7 + UP * 1.7, o5 + RIGHT * 6.7 + UP * 1.35, color=GREEN, stroke_width=5)
        g4 = Line(o5 + RIGHT * 6.7 + UP * 1.35, o5 + RIGHT * 9.0 + UP * 0.6, color=GREEN, stroke_width=5)
        g_lab = Tex("grassland: long lag, low broad peak").scale(0.75).shift(o5 + RIGHT * 6.3 + UP * 2.6)
        self.play(Create(g1), Create(g2))
        self.play(Create(g3), Create(g4), Write(g_lab))
        self.wait(2.5)
        b5_l1 = Tex("Sealing a catchment: peak up, lag down, limbs steeper").scale(0.85).shift(band_shift(5) + DOWN * 3.2)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): flash vs regional, and remedies ---
        self.next_band(6)
        b6_title = Tex("Flash flood vs regional flood").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        f1 = Tex("Jukskei, 3 Dec 2022: storm on a sealed catchment,").scale(0.9).shift(band_shift(6) + UP * 1.2)
        f2 = Tex("lag of minutes, at least 14 died at the river").scale(0.9).shift(band_shift(6) + UP * 0.4)
        self.play(Write(f1))
        self.play(Write(f2))
        self.wait(2.5)
        f3 = Tex("Natal, Sept 1987: cut-off low, days of rain,").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        f4 = Tex("rivers up across a province, $300+$ died").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(f3))
        self.play(Write(f4))
        self.wait(2.5)
        f5 = Tex("Every remedy lengthens lag or lowers peak:").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        f6 = Tex("wetlands, vegetation, zoning, drains, warnings").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(f5))
        self.play(Write(f6))
        self.play(Create(SurroundingRectangle(f6, color=GREEN)))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the lawn and the driveway ---
        self.next_band(7)
        b7_title = Tex("The lawn and the driveway").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Lawn: the water darkens the grass and is gone").scale(0.95).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex("= grass, roots, deep soil, the valley wetland").scale(0.95).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Driveway: at the gate before the bucket is empty").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("= rock, baked ground, tar, paving, rooftops").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("A soaked lawn sheds water like paving").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(2)
        b7_l6 = Tex("Build a suburb: the catchment is paved for good").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l6))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): a graph you can hear ---
        self.next_band(8)
        b8_title = Tex("A graph you can hear").scale(1.2).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Steady murmur before the storm: base flow,").scale(0.95).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("groundwater seeping out, not rainwater").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Rain lands... the river waits: LAG TIME").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Fast build (the sprinters), the loudest moment,").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        b8_l5 = Tex("then a slow fade (the walkers through the soil)").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex("Ask: how high, how soon, how steep?").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l6))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): the Jukskei and the Natal floods ---
        self.next_band(9)
        b9_title = Tex("The Jukskei and the Natal floods").scale(1.15).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("2022: storm on a paved city catchment,").scale(0.9).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex("minutes of lag, a surge through the gathering").scale(0.9).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("1987: days of rain on soaked hills,").scale(0.9).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex("a province's rivers up together for days").scale(0.9).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("The sharp crack vs the long swell —").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        b9_l6 = Tex("what catchment will the next rain find?").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.wait(2)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)
