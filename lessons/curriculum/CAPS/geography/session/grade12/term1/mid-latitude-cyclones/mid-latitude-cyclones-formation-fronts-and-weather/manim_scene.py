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
        # --- Band 0 (subtopic_1): where they form — the polar front
        title = Tex("Mid-Latitude Cyclones").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Born 30--60$^\circ$S over the Southern Ocean,").scale(0.95).shift(UP * 1.4)
        b0_l2 = Tex(r"travel WEST to EAST on the westerlies").scale(0.95).shift(UP * 0.7)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        # Polar front: warm air north (top), cold air south (bottom).
        front = Line(LEFT * 5.0 + DOWN * 0.6, RIGHT * 5.0 + DOWN * 0.6, color=PURPLE)
        front_lab = Tex("polar front").scale(0.9).shift(RIGHT * 3.6 + DOWN * 0.2)
        self.play(Create(front), Write(front_lab))
        warm_ar = Arrow(LEFT * 3.4 + DOWN * 0.05, LEFT * 1.4 + DOWN * 0.05, color=RED)
        warm_lab = Tex("warm subtropical air").scale(0.85).shift(LEFT * 2.4 + UP * 0.35).shift(DOWN * 0.05)
        cold_ar = Arrow(RIGHT * 1.4 + DOWN * 1.15, RIGHT * 3.4 + DOWN * 1.15, color=BLUE)
        cold_ar.put_start_and_end_on(RIGHT * 3.4 + DOWN * 1.15, RIGHT * 1.4 + DOWN * 1.15)
        cold_lab = Tex("cold polar air").scale(0.85).shift(RIGHT * 2.6 + DOWN * 1.6)
        self.play(Create(warm_ar), Write(warm_lab))
        self.play(Create(cold_ar), Write(cold_lab))
        self.wait(2.5)
        b0_l3 = Tex(r"Densities differ — they do not mix:").scale(0.95).shift(DOWN * 2.3)
        b0_l4 = Tex(r"cold wedges under, warm glides up and over").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the three formation conditions
        self.next_band(1)
        b1_title = Tex("Three conditions, one warning").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"1. A sharp temperature contrast (the front)").scale(0.95).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"2. Coriolis: deflects LEFT down here —").scale(0.95).shift(band_shift(1) + UP * 0.4)
        b1_l3 = Tex(r"air spins CLOCKWISE around our lows").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = Tex(r"3. Upper divergence: the jet stream drags").scale(0.95).shift(band_shift(1) + DOWN * 1.3)
        b1_l5 = Tex(r"air off the top; surface pressure falls").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(2.5)
        b1_l6 = Tex(r"1 000--2 000 km wide, 40--50 km/h east,").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        b1_l7 = Tex(r"lasts days, comes in families").scale(0.95).shift(band_shift(1) + DOWN * 3.6)
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three stages, plan view
        self.next_band(2)
        b2_title = Tex("Wave, mature V, occlusion").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Stage 1: friction kinks the front — a wave").scale(0.95).shift(band_shift(2) + UP * 1.3)
        self.play(Write(b2_l1))
        self.wait(2)
        # Mature stage plan view: low centre with two front arms.
        low = Dot(band_shift(2) + DOWN * 0.3 + LEFT * 0.4)
        low_lab = Tex("L").scale(1.1).shift(band_shift(2) + UP * 0.1 + LEFT * 0.4)
        self.play(Create(low), Write(low_lab))
        cold_f = Line(band_shift(2) + DOWN * 0.3 + LEFT * 0.4,
                      band_shift(2) + DOWN * 2.0 + LEFT * 3.4, color=BLUE)
        cold_f_lab = Tex("cold front (trailing)").scale(0.8).shift(band_shift(2) + DOWN * 2.5 + LEFT * 3.4)
        self.play(Create(cold_f), Write(cold_f_lab))
        warm_f = Line(band_shift(2) + DOWN * 0.3 + LEFT * 0.4,
                      band_shift(2) + DOWN * 2.0 + RIGHT * 2.6, color=RED)
        warm_f_lab = Tex("warm front (leading)").scale(0.8).shift(band_shift(2) + DOWN * 2.5 + RIGHT * 2.9)
        self.play(Create(warm_f), Write(warm_f_lab))
        ws_lab = Tex("warm sector").scale(0.85).shift(band_shift(2) + DOWN * 1.7 + LEFT * 0.4)
        self.play(Write(ws_lab))
        self.wait(2.5)
        b2_l2 = Tex(r"Clockwise spin, sliding east").scale(0.9).shift(band_shift(2) + UP * 0.4 + RIGHT * 3.6)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"Stage 3: cold catches warm — sector lifted,").scale(0.85).shift(band_shift(2) + DOWN * 3.1)
        b2_l4 = Tex(r"OCCLUDED, fuel cut, the storm dies").scale(0.85).shift(band_shift(2) + DOWN * 3.7)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): the cross-section
        self.next_band(3)
        b3_title = Tex("The examinable cross-section").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        ground = Line(band_shift(3) + DOWN * 1.8 + LEFT * 5.6, band_shift(3) + DOWN * 1.8 + RIGHT * 5.6)
        self.play(Create(ground))
        # Warm front surface: gentle slope on the right (leading edge).
        wf1 = Line(band_shift(3) + DOWN * 1.8 + RIGHT * 5.2, band_shift(3) + DOWN * 1.0 + RIGHT * 2.2, color=RED)
        wf2 = Line(band_shift(3) + DOWN * 1.0 + RIGHT * 2.2, band_shift(3) + DOWN * 0.4 + RIGHT * 0.2, color=RED)
        wf_lab = Tex(r"warm front $\approx$ 1 in 100:\\ gentle climb").scale(0.8).shift(band_shift(3) + UP * 0.3 + RIGHT * 3.6)
        self.play(Create(wf1), Create(wf2), Write(wf_lab))
        self.wait(2)
        wf_cloud = Tex(r"cirrus $\to$ altostratus $\to$ nimbostratus:\\ hours of steady soaking rain").scale(0.8).shift(band_shift(3) + DOWN * 2.7 + RIGHT * 3.0)
        self.play(Write(wf_cloud))
        self.wait(2.5)
        # Cold front surface: steep slope on the left (trailing edge).
        cf1 = Line(band_shift(3) + DOWN * 1.8 + LEFT * 3.4, band_shift(3) + DOWN * 0.2 + LEFT * 4.2, color=BLUE)
        cf_lab = Tex(r"cold front 1:50\\ hurls air up").scale(0.83).shift(band_shift(3) + UP * 0.6 + LEFT * 3.8)
        self.play(Create(cf1), Write(cf_lab))
        self.wait(2)
        cf_cloud = Tex(r"cumulonimbus:\\ thunder, hail").scale(0.85).shift(band_shift(3) + DOWN * 2.7 + LEFT * 3.2)
        self.play(Write(cf_cloud))
        self.wait(2)
        ws2_lab = Tex("warm sector: mild, humid, overcast").scale(0.8).shift(band_shift(3) + DOWN * 1.3 + LEFT * 0.6)
        self.play(Write(ws2_lab))
        self.wait(3)

        # --- Band 4 (subtopic_3): cold front passage, three scenes
        self.next_band(4)
        b4_title = Tex("Cold front: before, during, after").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Before: warm sector, NW wind, pressure").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"falling, humid, cloud building in the west").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"During: cumulonimbus, heavy showers,").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex(r"thunder, mountain snow — and the wind").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        b4_l5 = Tex(r"swings NW $\to$ W $\to$ SW").scale(1.05).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(2.5)
        b4_l6 = Tex(r"After: 6--10 $^\circ$C colder, pressure rises,").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        b4_l7 = Tex(r"steady SW wind, bright cold showery sky").scale(0.95).shift(band_shift(4) + DOWN * 3.5)
        self.play(Write(b4_l6))
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_3): warm front, impacts, management
        self.next_band(5)
        b5_title = Tex("Impacts and management").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Warm front: long warning, little violence —").scale(0.95).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex(r"usually stays south of SA, over the ocean").scale(0.95).shift(band_shift(5) + UP * 0.6)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Benefits: Western Cape winter rain fills").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        b5_l4 = Tex(r"the dams; mountain snow feeds rivers").scale(0.95).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex(r"Damage: gales strip roofs, Cape Flats").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        b5_l6 = Tex(r"floods, storm surf, snowed-in passes").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(2.5)
        b5_l7 = Tex(r"Manage: SAWS warnings, clear drains, shelters").scale(0.9).shift(band_shift(5) + DOWN * 3.4)
        self.play(Write(b5_l7))
        self.wait(3)

        # --- Band 6 (subtopic_4): the synoptic chart
        self.next_band(6)
        b6_title = Tex("Reading the synoptic chart").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Isobars in hPa (1016, 1012, 1008);").scale(0.95).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex(r"packed isobars $=$ strong wind; L $=$ cyclone").scale(0.95).shift(band_shift(6) + UP * 0.6)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"Cold front: solid triangles, pointing the way").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        b6_l4 = Tex(r"it moves; warm front: semicircles;").scale(0.95).shift(band_shift(6) + DOWN * 1.0)
        b6_l5 = Tex(r"occluded: both symbols on one line").scale(0.95).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex(r"Stage ID: kink $=$ initial; open wave with").scale(0.95).shift(band_shift(6) + DOWN * 2.6)
        b6_l7 = Tex(r"warm sector $=$ mature; merged spiral $=$ occluded").scale(0.9).shift(band_shift(6) + DOWN * 3.3)
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.wait(3)

        # --- Band 7 (subtopic_4): the two highs and the satellite comma
        self.next_band(7)
        b7_title = Tex("The two highs and the comma").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"South Atlantic High west, South Indian east:").scale(0.95).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex(r"fronts slide the corridor between them").scale(0.95).shift(band_shift(7) + UP * 0.6)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Winter: highs shift north, corridor crosses").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        b7_l4 = Tex(r"the Cape — why frontal rain is a winter gift").scale(0.95).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l5 = Tex(r"After passage the Atlantic High ridges in:").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        b7_l6 = Tex(r"clearing skies, onshore south-westerlies").scale(0.95).shift(band_shift(7) + DOWN * 2.45)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(2.5)
        b7_l7 = Tex(r"Satellite: comma cloud; what sits west today").scale(0.9).shift(band_shift(7) + DOWN * 3.15)
        b7_l8 = Tex(r"arrives tomorrow — the westerlies conveyor").scale(0.9).shift(band_shift(7) + DOWN * 3.75)
        self.play(Write(b7_l7))
        self.play(Write(b7_l8))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): two crowds at a rope
        self.next_band(8)
        b8_title = Tex("Two crowds at a rope").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Jackets (cold, heavy) vs T-shirts (warm,").scale(0.95).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex(r"light); the rope between them: polar front").scale(0.95).shift(band_shift(8) + UP * 0.6)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"They never mix — sand settles under water;").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        b8_l4 = Tex(r"the warm air always gets lifted").scale(0.95).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex(r"Lifted air cools $\to$ cloud $\to$ rain").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2.5)
        b8_l6 = Tex(r"Earth's turn nudges air LEFT: clockwise drain;").scale(0.9).shift(band_shift(8) + DOWN * 2.8)
        b8_l7 = Tex(r"the jet stream is the extractor fan on the roof").scale(0.9).shift(band_shift(8) + DOWN * 3.5)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): three photographs
        self.next_band(9)
        b9_title = Tex("The storm's life in three photographs").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Photo 1: the rope gets a bend — the wave").scale(0.95).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex(r"Photo 2: a giant sideways V — warm front").scale(0.95).shift(band_shift(9) + UP * 0.5)
        b9_l3 = Tex(r"the gentle ramp, cold front the spade;").scale(0.95).shift(band_shift(9) + DOWN * 0.2)
        b9_l4 = Tex(r"warm sector: the sandwich filling").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(3)
        b9_l5 = Tex(r"Photo 3: the spade catches the ramp —").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        b9_l6 = Tex(r"filling squeezed off the ground: occlusion,").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        b9_l7 = Tex(r"fuel cut, the fire burns out").scale(0.95).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.play(Create(SurroundingRectangle(b9_l7, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): a rainy Tuesday in Cape Town
        self.next_band(10)
        b10_title = Tex("A rainy Tuesday in Cape Town").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Morning: sticky warm, NW wind, pressure").scale(0.95).shift(band_shift(10) + UP * 1.3)
        b10_l2 = Tex(r"sliding down, cloud stacking out to sea").scale(0.95).shift(band_shift(10) + UP * 0.6)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Afternoon: black sky, hard cold rain,").scale(0.95).shift(band_shift(10) + DOWN * 0.3)
        b10_l4 = Tex(r"Boland snow — wind swings NW $\to$ SW,").scale(0.95).shift(band_shift(10) + DOWN * 1.0)
        b10_l5 = Tex(r"the storm's signature").scale(1.0).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(3)
        b10_l6 = Tex(r"Night: jersey cold, pressure climbs, cold").scale(0.95).shift(band_shift(10) + DOWN * 2.5)
        b10_l7 = Tex(r"sunshine between showers, dams fuller").scale(0.95).shift(band_shift(10) + DOWN * 3.15)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.wait(2.5)
        b10_l8 = Tex(r"Winter only: the storm track shifts north").scale(0.95).shift(band_shift(10) + DOWN * 3.8)
        self.play(Write(b10_l8))
        self.wait(4)
