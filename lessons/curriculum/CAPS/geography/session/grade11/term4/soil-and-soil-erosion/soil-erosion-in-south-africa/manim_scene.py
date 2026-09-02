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

# Band-layout whiteboard scene for "Soil Erosion in South Africa"
# (grade 11, term 4). All seven subtopics: Part 1 Expert (1-4), Part 2
# Simplifier (5-7). Band time apportioned to subtopics.json
# (225/240/225/240/185/200/205 of 1520 s). Exporter-safe primitives only;
# the soil-horizon column and gabion check-dam are hand-built from
# Rectangle/Line/Arrow/Tex, element by element.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SoilErosionSouthAfricaSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the living skin and its horizons
        title = Tex("Soil Erosion in South Africa").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Soil: minerals $+$ humus $+$ water $+$ air $+$ life").scale(0.95).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        # Horizon column: stacked rectangles, labelled as drawn.
        h1 = Rectangle(width=3.2, height=0.7, color=GREEN).shift(LEFT * 3.0 + UP * 0.2)
        h1_lab = Tex("topsoil: humus-rich").scale(0.8).shift(RIGHT * 0.6 + UP * 0.2)
        self.play(Create(h1), Write(h1_lab))
        self.wait(1.5)
        h2 = Rectangle(width=3.2, height=0.8, color=ORANGE).shift(LEFT * 3.0 + DOWN * 0.55)
        h2_lab = Tex("subsoil: poorer").scale(0.8).shift(RIGHT * 0.4 + DOWN * 0.55)
        self.play(Create(h2), Write(h2_lab))
        self.wait(1.5)
        h3 = Rectangle(width=3.2, height=0.9, color=GREY).shift(LEFT * 3.0 + DOWN * 1.4)
        h3_lab = Tex("weathered $\\to$ parent rock").scale(0.8).shift(RIGHT * 0.9 + DOWN * 1.4)
        self.play(Create(h3), Write(h3_lab))
        self.wait(2)
        b0_l2 = Tex(r"Nearly all fertility lives in the thin topsoil").scale(0.95).shift(DOWN * 2.5)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the asymmetry and the bodyguard
        self.next_band(1)
        b1_title = Tex("Slow to form, fast to lose").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Centuries to build a few cm of topsoil;").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"one storm on bare ground strips more").scale(1.0).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex(r"Effectively NON-RENEWABLE for humans").scale(1.05).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = Tex(r"Only 12\% arable, barely 3\% high-potential;").scale(0.95).shift(band_shift(1) + DOWN * 1.4)
        b1_l5 = Tex(r"losses: 100s of millions of tonnes a year").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(2.5)
        b1_l6 = Tex(r"Vegetation is the soil's bodyguard —").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        b1_l7 = Tex(r"every cause works by removing it").scale(0.95).shift(band_shift(1) + DOWN * 3.6)
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.wait(3)

        # --- Band 2 (subtopic_2): physical causes — the water sequence
        self.next_band(2)
        b2_title = Tex("Physical causes: water and wind").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"splash $\to$ sheet $\to$ rill $\to$ gully (donga)").scale(1.05).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(3)
        b2_l2 = Tex(r"Wind lifts dry bare soil — the 1930s").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l3 = Tex(r"Dust Bowl on America's ploughed plains").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_l2))
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex(r"SA is erosion-prone: steep slopes, Highveld").scale(0.95).shift(band_shift(2) + DOWN * 1.4)
        b2_l5 = Tex(r"thunderstorms, droughts, thin cover").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(2.5)
        b2_l6 = Tex(r"But bare ground is usually MADE — physical").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        b2_l7 = Tex(r"agents finish what land use starts").scale(0.95).shift(band_shift(2) + DOWN * 3.6)
        self.play(Write(b2_l6))
        self.play(Write(b2_l7))
        self.wait(3)

        # --- Band 3 (subtopic_2): human and animal causes
        self.next_band(3)
        b3_title = Tex("Human and animal causes").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Overcultivation exhausts humus; up-down").scale(0.95).shift(band_shift(3) + UP * 1.4)
        b3_l2 = Tex(r"ploughing turns furrows into drains").scale(0.95).shift(band_shift(3) + UP * 0.75)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex(r"Deforestation (firewood), mining dumps,").scale(0.95).shift(band_shift(3) + UP * 0.05)
        b3_l4 = Tex(r"construction and settlement edges").scale(0.95).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex(r"Past: homelands crowded herds on poor land —").scale(0.9).shift(band_shift(3) + DOWN * 1.4)
        b3_l6 = Tex(r"the Eastern Cape's donga scars remain").scale(0.9).shift(band_shift(3) + DOWN * 2.05)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.wait(2.5)
        b3_l7 = Tex(r"Overgrazing bares the veld; trampled").scale(0.95).shift(band_shift(3) + DOWN * 2.8)
        b3_l8 = Tex(r"cattle paths become starter channels").scale(0.95).shift(band_shift(3) + DOWN * 3.45)
        self.play(Write(b3_l7))
        self.play(Write(b3_l8))
        self.wait(3)

        # --- Band 4 (subtopic_3): evidence on the landscape
        self.next_band(4)
        b4_title = Tex("Evidence across South Africa").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Dongas: Eastern Cape, KZN, Limpopo —").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"deepest in former homeland districts").scale(1.0).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Brown rivers after storms: topsoil in transit").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex(r"Dams silt up: Welbedacht Dam (Caledon River)").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        b4_l5 = Tex(r"lost most capacity within decades").scale(0.95).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(2.5)
        b4_l6 = Tex(r"Dust plumes, exposed roots, fence posts").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        b4_l7 = Tex(r"on pedestals of wind-stripped soil").scale(0.95).shift(band_shift(4) + DOWN * 3.5)
        self.play(Write(b4_l6))
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_3): effects on people and environment
        self.next_band(5)
        b5_title = Tex("Effects: people and environment").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_mid = Line(band_shift(5) + UP * 1.6, band_shift(5) + DOWN * 2.4)
        self.play(Create(b5_mid))
        b5_ph = Tex("People", color=YELLOW).scale(1.0).shift(band_shift(5) + UP * 1.3 + LEFT * 3.2)
        b5_eh = Tex("Environment", color=GREEN).scale(1.0).shift(band_shift(5) + UP * 1.3 + RIGHT * 3.2)
        self.play(Write(b5_ph), Write(b5_eh))
        self.wait(1.5)
        b5_p1 = Tex(r"yields fall,\\ food prices climb").scale(0.85).shift(band_shift(5) + UP * 0.4 + LEFT * 3.2)
        b5_e1 = Tex(r"rivers choke\\ with sediment").scale(0.85).shift(band_shift(5) + UP * 0.4 + RIGHT * 3.2)
        self.play(Write(b5_p1))
        self.play(Write(b5_e1))
        self.wait(2)
        b5_p2 = Tex(r"livelihoods collapse,\\ people leave").scale(0.85).shift(band_shift(5) + DOWN * 0.8 + LEFT * 3.2)
        b5_e2 = Tex(r"floods sharpen,\\ dry flows weaken").scale(0.85).shift(band_shift(5) + DOWN * 0.8 + RIGHT * 3.2)
        self.play(Write(b5_p2))
        self.play(Write(b5_e2))
        self.wait(2)
        b5_p3 = Tex(r"dams silt;\\ fertiliser costs").scale(0.85).shift(band_shift(5) + DOWN * 2.0 + LEFT * 3.2)
        b5_e3 = Tex(r"biodiversity falls;\\ desertification").scale(0.85).shift(band_shift(5) + DOWN * 2.0 + RIGHT * 3.2)
        self.play(Write(b5_p3))
        self.play(Write(b5_e3))
        self.wait(2.5)
        b5_l1 = Tex(r"A slow-motion disaster on three fronts").scale(1.0).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): prevention
        self.next_band(6)
        b6_title = Tex("Management: prevention first").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Contour ploughing: each ridge a small dam").scale(0.95).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex(r"Strip cropping; rotation and fallow;").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex(r"mulch and stubble — never bare ground").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(b6_l2))
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex(r"Windbreak tree rows slow erosive wind").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex(r"Grazing: stock to carrying capacity,").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        b6_l6 = Tex(r"rest camps in rotation, manage water routes").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): control and the GIS toolkit
        self.next_band(7)
        b7_title = Tex("Control, and the GIS toolkit").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        # Gabion check dam in a gully: channel sides + rock basket.
        g_left = Line(band_shift(7) + UP * 1.4 + LEFT * 4.8, band_shift(7) + UP * 0.3 + LEFT * 3.4)
        g_right = Line(band_shift(7) + UP * 0.3 + LEFT * 1.6, band_shift(7) + UP * 1.4 + LEFT * 0.2)
        gabion = Rectangle(width=1.4, height=0.6, color=GREY).shift(band_shift(7) + UP * 0.6 + LEFT * 2.5)
        gab_lab = Tex(r"gabion: rock basket\\ slows each flood").scale(0.8).shift(band_shift(7) + UP * 1.6 + LEFT * 2.5)
        flow = Arrow(band_shift(7) + UP * 0.9 + LEFT * 4.3, band_shift(7) + UP * 0.9 + LEFT * 3.3, color=BLUE)
        self.play(Create(g_left), Create(g_right))
        self.play(Create(gabion), Write(gab_lab))
        self.play(Create(flow))
        self.wait(2)
        b7_l1 = Tex(r"Re-vegetate, fence off; LandCare,\\ Working for Water and on Fire").scale(0.85).shift(band_shift(7) + UP * 0.9 + RIGHT * 3.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex(r"GIS: spatially referenced data — tied to").scale(0.95).shift(band_shift(7) + DOWN * 0.6)
        b7_l3 = Tex(r"coordinates. Spatial resolution: pixel size;").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        b7_l4 = Tex(r"spectral: which bands — infrared exposes").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        b7_l5 = Tex(r"bare, stressed ground").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(2)
        b7_l6 = Tex(r"Point: gully head. Line: river. Area: risk zone").scale(0.9).shift(band_shift(7) + DOWN * 3.5)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the teaspoon bank account
        self.next_band(8)
        b8_title = Tex("The bank account of teaspoons").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Deposits: one teaspoon a year (centuries").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"per few cm). Withdrawals: by the bucket").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Teaspoons in, buckets out — non-renewable").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex(r"Ten plates of food: only ONE stands on").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        b8_l5 = Tex(r"cropland; 60 million people eat off it").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex(r"Grass is the bodyguard: leaves soften rain,").scale(0.9).shift(band_shift(8) + DOWN * 2.8)
        b8_l7 = Tex(r"roots grip, litter feeds the glue").scale(0.9).shift(band_shift(8) + DOWN * 3.5)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): footpath to canyon
        self.next_band(9)
        b9_title = Tex("How a footpath becomes a canyon").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Act 1: overgrazing bares a patch").scale(0.95).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex(r"Act 2: raindrops hammer soil loose").scale(0.95).shift(band_shift(9) + UP * 0.6)
        b9_l3 = Tex(r"Act 3: sheet flow steals the surface").scale(0.95).shift(band_shift(9) + DOWN * 0.1)
        b9_l4 = Tex(r"Act 4: rills — easy to ignore").scale(0.95).shift(band_shift(9) + DOWN * 0.8)
        b9_l5 = Tex(r"Act 5: rills join, deepen — a DONGA opens").scale(0.95).shift(band_shift(9) + DOWN * 1.5)
        for m in (b9_l1, b9_l2, b9_l3, b9_l4, b9_l5):
            self.play(Write(m))
            self.wait(1.6)
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(1.5)
        b9_l6 = Tex(r"The cattle path was the first drain;").scale(0.95).shift(band_shift(9) + DOWN * 2.4)
        b9_l7 = Tex(r"wind runs the Dust Bowl plot on dry fields").scale(0.9).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.wait(2)
        b9_l8 = Tex(r"History too: homelands built the overload in").scale(0.9).shift(band_shift(9) + DOWN * 3.8)
        self.play(Write(b9_l8))
        self.wait(3)

        # --- Band 10 (subtopic_7): stitching the land back together
        self.next_band(10)
        b10_title = Tex("Stitching the land back together").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Stop new tears: plough ALONG the slope,").scale(0.95).shift(band_shift(10) + UP * 1.3)
        b10_l2 = Tex(r"blanket fields with mulch, rotate crops,").scale(0.95).shift(band_shift(10) + UP * 0.6)
        b10_l3 = Tex(r"herd to what the grass can feed").scale(0.95).shift(band_shift(10) + DOWN * 0.1)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(3)
        b10_l4 = Tex(r"In the donga: gabions as speed bumps —").scale(0.95).shift(band_shift(10) + DOWN * 1.0)
        b10_l5 = Tex(r"floods drop their load, the floor rises").scale(0.95).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(2.5)
        b10_l6 = Tex(r"Where to stitch first? Look from space:").scale(0.95).shift(band_shift(10) + DOWN * 2.6)
        b10_l7 = Tex(r"pixel size, infrared bands; point, line, area").scale(0.9).shift(band_shift(10) + DOWN * 3.3)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.wait(4)
