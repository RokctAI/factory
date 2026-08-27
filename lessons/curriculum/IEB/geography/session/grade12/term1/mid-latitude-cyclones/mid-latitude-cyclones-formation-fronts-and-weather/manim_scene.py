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

# Band-layout whiteboard scene for "Mid-Latitude Cyclones: Formation, Fronts
# and Weather" (grade 12, term 1). All seven subtopics: Part 1 Expert (1-4),
# Part 2 Simplifier (5-7). Band time apportioned to subtopics.json
# (230/250/250/250/190/190/200 of 1560 s). Exporter-safe primitives only;
# the polar front, the mature-stage plan view and the frontal cross-section
# are hand-built from Line/Arrow/Dot/Tex, element by element.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MidLatitudeCyclonesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): breeding ground and the polar front
        title = Tex("Mid-Latitude Cyclones").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Bred 30--60$^\circ$S over the ocean;").scale(0.95).shift(UP * 1.4)
        b0_l2 = Tex(r"the westerlies carry them WEST $\to$ EAST").scale(0.95).shift(UP * 0.7)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        # Polar front: warm air equatorward, cold air poleward.
        front = Line(LEFT * 5.0 + DOWN * 0.6, RIGHT * 5.0 + DOWN * 0.6, color=PURPLE)
        front_lab = Tex("polar front").scale(0.9).shift(RIGHT * 3.6 + DOWN * 0.2)
        self.play(Create(front), Write(front_lab))
        warm_ar = Arrow(LEFT * 3.4 + DOWN * 0.05, LEFT * 1.4 + DOWN * 0.05, color=RED)
        warm_lab = Tex("warm subtropical air").scale(0.85).shift(LEFT * 2.4 + UP * 0.3)
        cold_ar = Arrow(RIGHT * 3.4 + DOWN * 1.15, RIGHT * 1.4 + DOWN * 1.15, color=BLUE)
        cold_lab = Tex("cold polar air").scale(0.85).shift(RIGHT * 2.6 + DOWN * 1.6)
        self.play(Create(warm_ar), Write(warm_lab))
        self.play(Create(cold_ar), Write(cold_lab))
        self.wait(2.5)
        b0_l3 = Tex(r"Different densities never blend:").scale(0.95).shift(DOWN * 2.3)
        b0_l4 = Tex(r"cold slides under, warm is levered up").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the three ingredients
        self.next_band(1)
        b1_title = Tex("Three ingredients of development").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"1. Sharp temperature contrast at the front").scale(0.95).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"2. Coriolis deflects moving air LEFT here,").scale(0.95).shift(band_shift(1) + UP * 0.4)
        b1_l3 = Tex(r"so our lows spin CLOCKWISE").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = Tex(r"3. Jet-stream divergence drains the top;").scale(0.95).shift(band_shift(1) + DOWN * 1.3)
        b1_l5 = Tex(r"surface pressure falls, inflow spirals in").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(2.5)
        b1_l6 = Tex(r"1 000--2 000 km wide, $\sim$40--50 km/h east,").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        b1_l7 = Tex(r"lasts days, arrives in families").scale(0.95).shift(band_shift(1) + DOWN * 3.6)
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three stages, plan view
        self.next_band(2)
        b2_title = Tex("Ripple, open V, occluded spiral").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Stage 1: shearing flows kink the front").scale(0.95).shift(band_shift(2) + UP * 1.3)
        self.play(Write(b2_l1))
        self.wait(2)
        # Mature stage plan view: low centre with two front arms.
        low = Dot(band_shift(2) + DOWN * 0.3 + LEFT * 0.4)
        low_lab = Tex("L").scale(1.1).shift(band_shift(2) + UP * 0.1 + LEFT * 0.4)
        self.play(Create(low), Write(low_lab))
        cold_f = Line(band_shift(2) + DOWN * 0.3 + LEFT * 0.4,
                      band_shift(2) + DOWN * 2.0 + LEFT * 3.4, color=BLUE)
        cold_f_lab = Tex("cold front (trailing arm)").scale(0.8).shift(band_shift(2) + DOWN * 2.5 + LEFT * 3.4)
        self.play(Create(cold_f), Write(cold_f_lab))
        warm_f = Line(band_shift(2) + DOWN * 0.3 + LEFT * 0.4,
                      band_shift(2) + DOWN * 2.0 + RIGHT * 2.6, color=RED)
        warm_f_lab = Tex("warm front (leading arm)").scale(0.8).shift(band_shift(2) + DOWN * 2.5 + RIGHT * 2.9)
        self.play(Create(warm_f), Write(warm_f_lab))
        ws_lab = Tex("warm sector").scale(0.85).shift(band_shift(2) + DOWN * 1.7 + LEFT * 0.4)
        self.play(Write(ws_lab))
        self.wait(2.5)
        b2_l2 = Tex(r"Clockwise, sliding east").scale(0.9).shift(band_shift(2) + UP * 0.4 + RIGHT * 3.6)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"Stage 3: cold arm catches warm arm — sector").scale(0.85).shift(band_shift(2) + DOWN * 3.1)
        b2_l4 = Tex(r"lifted off, OCCLUDED, contrast collapses").scale(0.85).shift(band_shift(2) + DOWN * 3.7)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): the cross-section
        self.next_band(3)
        b3_title = Tex("Section through the warm sector").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        ground = Line(band_shift(3) + DOWN * 1.8 + LEFT * 5.6, band_shift(3) + DOWN * 1.8 + RIGHT * 5.6)
        self.play(Create(ground))
        # Warm front surface: gentle slope at the leading edge (right).
        wf1 = Line(band_shift(3) + DOWN * 1.8 + RIGHT * 5.2, band_shift(3) + DOWN * 1.0 + RIGHT * 2.2, color=RED)
        wf2 = Line(band_shift(3) + DOWN * 1.0 + RIGHT * 2.2, band_shift(3) + DOWN * 0.4 + RIGHT * 0.2, color=RED)
        wf_lab = Tex(r"warm front $\approx$ 1 in 100:\\ slow steady climb").scale(0.8).shift(band_shift(3) + UP * 0.3 + RIGHT * 3.6)
        self.play(Create(wf1), Create(wf2), Write(wf_lab))
        self.wait(2)
        wf_cloud = Tex(r"cirrus $\to$ altostratus $\to$ nimbostratus:\\ hours of soaking rain ahead of the front").scale(0.75).shift(band_shift(3) + DOWN * 2.7 + RIGHT * 3.0)
        self.play(Write(wf_cloud))
        self.wait(2.5)
        # Cold front surface: steep wedge at the trailing edge (left).
        cf1 = Line(band_shift(3) + DOWN * 1.8 + LEFT * 3.4, band_shift(3) + DOWN * 0.2 + LEFT * 4.2, color=BLUE)
        cf_lab = Tex(r"cold front $\approx$ 1 in 50:\\ air flung upward").scale(0.83).shift(band_shift(3) + UP * 0.6 + LEFT * 3.8)
        self.play(Create(cf1), Write(cf_lab))
        self.wait(2)
        cf_cloud = Tex(r"cumulonimbus:\\ thunder, possible hail").scale(0.85).shift(band_shift(3) + DOWN * 2.7 + LEFT * 3.2)
        self.play(Write(cf_cloud))
        self.wait(2)
        ws2_lab = Tex("warm sector: mild, muggy, overcast").scale(0.8).shift(band_shift(3) + DOWN * 1.3 + LEFT * 0.6)
        self.play(Write(ws2_lab))
        self.wait(3)

        # --- Band 4 (subtopic_3): cold front passage, three scenes
        self.next_band(4)
        b4_title = Tex("Cold front: three scenes in time").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Ahead: warm sector, NW wind, barometer").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"falling, humid, cloud wall in the west").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Passage: cumulonimbus bursts, thunder,").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex(r"snow on high peaks — and the wind").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        b4_l5 = Tex(r"backs NW $\to$ W $\to$ SW").scale(1.05).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(2.5)
        b4_l6 = Tex(r"Behind: 6--10 $^\circ$C colder, pressure climbs,").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        b4_l7 = Tex(r"gusty SW wind, cold sunshine and showers").scale(0.95).shift(band_shift(4) + DOWN * 3.5)
        self.play(Write(b4_l6))
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_3): warm front, impacts, management
        self.next_band(5)
        b5_title = Tex("Impacts and management").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Warm front: a day of warning, gentle rain —").scale(0.95).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex(r"usually passes south of SA over the sea").scale(0.95).shift(band_shift(5) + UP * 0.6)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Benefits: winter rain fills Theewaterskloof").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        b5_l4 = Tex(r"and Garden Route dams; snow banks water").scale(0.95).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex(r"Damage: gales strip roofs, settlements flood,").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        b5_l6 = Tex(r"storm swell, Outeniqua passes snowed shut").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(2.5)
        b5_l7 = Tex(r"Manage: early warnings, drains, shelters, stock down").scale(0.85).shift(band_shift(5) + DOWN * 3.4)
        self.play(Write(b5_l7))
        self.wait(3)

        # --- Band 6 (subtopic_4): the synoptic chart
        self.next_band(6)
        b6_title = Tex("Reading the synoptic chart").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Isobars in hPa (1020, 1012, 1004);").scale(0.95).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex(r"crowded isobars $=$ strong wind; L $=$ cyclone").scale(0.95).shift(band_shift(6) + UP * 0.6)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"Cold front: solid triangles pointing the way;").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        b6_l4 = Tex(r"warm front: solid semicircles;").scale(0.95).shift(band_shift(6) + DOWN * 1.0)
        b6_l5 = Tex(r"occluded: both symbols, one line").scale(0.95).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex(r"Staging: slight kink $=$ initial; open warm").scale(0.95).shift(band_shift(6) + DOWN * 2.6)
        b6_l7 = Tex(r"sector $=$ mature; tight merged spiral $=$ occluded").scale(0.9).shift(band_shift(6) + DOWN * 3.3)
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.wait(3)

        # --- Band 7 (subtopic_4): the two highs and the satellite comma
        self.next_band(7)
        b7_title = Tex("The two highs and the comma").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"South Atlantic High west, South Indian High east:").scale(0.9).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex(r"fronts must thread the corridor between them").scale(0.95).shift(band_shift(7) + UP * 0.6)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Winter: highs migrate north with the sun —").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        b7_l4 = Tex(r"the corridor crosses the southern tip of Africa").scale(0.95).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l5 = Tex(r"Afterwards the Atlantic High ridges in:").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        b7_l6 = Tex(r"rising pressure, clear sky, cool SW onshore").scale(0.95).shift(band_shift(7) + DOWN * 2.45)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(2.5)
        b7_l7 = Tex(r"Satellite: bright comma of cloud; today's chart").scale(0.9).shift(band_shift(7) + DOWN * 3.15)
        b7_l8 = Tex(r"to your west is tomorrow's weather overhead").scale(0.9).shift(band_shift(7) + DOWN * 3.75)
        self.play(Write(b7_l7))
        self.play(Write(b7_l8))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): two crowds at a rope
        self.next_band(8)
        b8_title = Tex("Two crowds at a rope").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Blankets (cold, heavy) vs shorts (warm,").scale(0.95).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex(r"light); the rope between them: polar front").scale(0.95).shift(band_shift(8) + UP * 0.6)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"They never blend — cold syrup slides under").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        b8_l4 = Tex(r"water; the warm air is always shoved up").scale(0.95).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex(r"Rising air cools $\to$ cloud $\to$ rain").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2.5)
        b8_l6 = Tex(r"Earth's turn nudges air LEFT: clockwise plughole;").scale(0.88).shift(band_shift(8) + DOWN * 2.8)
        b8_l7 = Tex(r"the jet stream is the chimney drawing from above").scale(0.88).shift(band_shift(8) + DOWN * 3.5)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): three photographs
        self.next_band(9)
        b9_title = Tex("The storm's life in three photographs").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Photo 1: the rope develops a bend — the wave").scale(0.95).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex(r"Photo 2: a huge sideways V — warm front").scale(0.95).shift(band_shift(9) + UP * 0.5)
        b9_l3 = Tex(r"the escalator, cold front the snowplough;").scale(0.95).shift(band_shift(9) + DOWN * 0.2)
        b9_l4 = Tex(r"warm sector: the vetkoek filling").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(3)
        b9_l5 = Tex(r"Photo 3: the snowplough catches the escalator —").scale(0.9).shift(band_shift(9) + DOWN * 1.8)
        b9_l6 = Tex(r"filling squeezed off the ground: occlusion,").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        b9_l7 = Tex(r"fuel gone, the braai fire dies at midnight").scale(0.95).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.play(Create(SurroundingRectangle(b9_l7, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): a stormy Thursday in George
        self.next_band(10)
        b10_title = Tex("A stormy Thursday in George").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Morning: warm and sticky, NW wind off the").scale(0.95).shift(band_shift(10) + UP * 1.3)
        b10_l2 = Tex(r"Karoo, barometer draining, cloud wall at sea").scale(0.95).shift(band_shift(10) + UP * 0.6)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Afternoon: sky shuts, cold hammering rain,").scale(0.95).shift(band_shift(10) + DOWN * 0.3)
        b10_l4 = Tex(r"Outeniqua snow — flags swing NW $\to$ SW,").scale(0.95).shift(band_shift(10) + DOWN * 1.0)
        b10_l5 = Tex(r"the storm signs its name").scale(1.0).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(3)
        b10_l6 = Tex(r"Night: jacket cold, pressure climbing, cold").scale(0.95).shift(band_shift(10) + DOWN * 2.5)
        b10_l7 = Tex(r"sun between showers, the dam creeps up").scale(0.95).shift(band_shift(10) + DOWN * 3.15)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.wait(2.5)
        b10_l8 = Tex(r"Winter only: the storm highway shifts north").scale(0.95).shift(band_shift(10) + DOWN * 3.8)
        self.play(Write(b10_l8))
        self.wait(4)
