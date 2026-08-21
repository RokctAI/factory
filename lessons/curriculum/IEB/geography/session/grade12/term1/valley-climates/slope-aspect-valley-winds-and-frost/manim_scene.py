# Copyright (c) 2026 RokctAI
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

# Band-layout whiteboard scene for "Slope Aspect, Valley Winds and Frost"
# (grade 12, term 1). All seven subtopics: Part 1 Expert (1-4), Part 2
# Simplifier (5-7). Band time apportioned to subtopics.json
# (225/235/240/250/195/195/210 of 1550 s). Exporter-safe primitives only;
# the valley cross-section, the winds and the thermal belt are hand-built
# from Line/Arrow/Dot/Tex, element by element.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def valley(shift):
    left = Line(shift + UP * 1.0 + LEFT * 4.6, shift + DOWN * 1.8 + LEFT * 0.8)
    floor = Line(shift + DOWN * 1.8 + LEFT * 0.8, shift + DOWN * 1.8 + RIGHT * 0.8)
    right = Line(shift + DOWN * 1.8 + RIGHT * 0.8, shift + UP * 1.0 + RIGHT * 4.6)
    return left, floor, right


class ValleyClimatesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): aspect — the Southern Hemisphere geometry
        title = Tex("Valley Climates").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Aspect $=$ the direction a slope faces").scale(1.0).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex(r"SA midday sun stands in the NORTHERN sky").scale(0.95).shift(UP * 0.5)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex(r"North-facing wall: steep rays, more hours —").scale(0.95).shift(DOWN * 0.4)
        b0_l4 = Tex(r"the WARM slope").scale(1.0).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2.5)
        b0_l5 = Tex(r"South-facing wall: glancing rays — cool,").scale(0.95).shift(DOWN * 2.0)
        b0_l6 = Tex(r"shaded, moister; flip it for Europe").scale(0.95).shift(DOWN * 2.7)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): consequences and precision points
        self.next_band(1)
        b1_title = Tex("Reading aspect off the land").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Warm wall: dry soil, grassier, snow gone first;").scale(0.9).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"vines and fruit sun themselves here").scale(0.9).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex(r"Cool wall: damp, denser green, kloof forest,").scale(0.9).shift(band_shift(1) + DOWN * 0.4)
        b1_l4 = Tex(r"snow lingers; plantations and pasture").scale(0.9).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex(r"Contrast peaks in WINTER (low sun)").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        b1_l6 = Tex(r"and in EAST--WEST valleys; a north--south").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        b1_l7 = Tex(r"valley shares the sun between its walls").scale(0.95).shift(band_shift(1) + DOWN * 3.4)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.wait(3)

        # --- Band 2 (subtopic_2): anabatic wind (day)
        self.next_band(2)
        b2_title = Tex("Day: the anabatic wind").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        vl, vf, vr = valley(band_shift(2) + DOWN * 0.6)
        self.play(Create(vl), Create(vf), Create(vr))
        up1 = Arrow(band_shift(2) + DOWN * 1.9 + LEFT * 1.6, band_shift(2) + DOWN * 0.3 + LEFT * 3.4, color=RED)
        up2 = Arrow(band_shift(2) + DOWN * 1.9 + RIGHT * 1.6, band_shift(2) + DOWN * 0.3 + RIGHT * 3.4, color=RED)
        self.play(Create(up1), Create(up2))
        an_lab = Tex("upslope breeze on the heated walls").scale(0.85).shift(band_shift(2) + UP * 1.0)
        self.play(Write(an_lab))
        self.wait(2.5)
        b2_l1 = Tex(r"Walls heat faster than free air; contact air").scale(0.9).shift(band_shift(2) + DOWN * 2.6)
        b2_l2 = Tex(r"warms, rises along the slope — cumulus").scale(0.9).shift(band_shift(2) + DOWN * 3.3)
        b2_l3 = Tex(r"crowns the peaks by afternoon").scale(0.9).shift(band_shift(2) + DOWN * 4.0)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.play(Write(b2_l3))
        self.wait(3)

        # --- Band 3 (subtopic_2): katabatic wind (night) and pooling
        self.next_band(3)
        b3_title = Tex("Night: the katabatic wind").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        wl, wf, wr = valley(band_shift(3) + DOWN * 0.6)
        self.play(Create(wl), Create(wf), Create(wr))
        dn1 = Arrow(band_shift(3) + DOWN * 0.3 + LEFT * 3.4, band_shift(3) + DOWN * 1.9 + LEFT * 1.6, color=BLUE)
        dn2 = Arrow(band_shift(3) + DOWN * 0.3 + RIGHT * 3.4, band_shift(3) + DOWN * 1.9 + RIGHT * 1.6, color=BLUE)
        self.play(Create(dn1), Create(dn2))
        pool = Line(band_shift(3) + DOWN * 2.0 + LEFT * 1.3, band_shift(3) + DOWN * 2.0 + RIGHT * 1.3, color=BLUE)
        pool_lab = Tex("cold air ponds on the floor").scale(0.85).shift(band_shift(3) + DOWN * 3.0)
        self.play(Create(pool), Write(pool_lab))
        self.wait(2.5)
        b3_l1 = Tex(r"Slopes radiate to a clear sky; chilled dense").scale(0.9).shift(band_shift(3) + DOWN * 3.7)
        b3_l2 = Tex(r"air slides downhill — gravity's wind, strongest").scale(0.9).shift(band_shift(3) + DOWN * 4.4)
        b3_l3 = Tex(r"on clear calm winter nights").scale(0.9).shift(band_shift(3) + DOWN * 5.0)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.wait(3)

        # --- Band 4 (subtopic_3): the inversion and the thermal belt
        self.next_band(4)
        b4_title = Tex("The inversion and the thermal belt").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"By the small hours: coldest air at the").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"BOTTOM, warmer above — upside down").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex(r"Floor: below freezing before dawn").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex(r"Mid-slope: the THERMAL BELT — warmest").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        b4_l5 = Tex(r"address of the night-time valley").scale(0.95).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2.5)
        b4_l6 = Tex(r"Above it, the high slopes and ridge cool").scale(0.95).shift(band_shift(4) + DOWN * 2.7)
        b4_l7 = Tex(r"again toward the free-air temperature").scale(0.95).shift(band_shift(4) + DOWN * 3.4)
        self.play(Write(b4_l6))
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_3): frost pocket, radiation fog, smoke trap
        self.next_band(5)
        b5_title = Tex("Frost, fog and the smoke trap").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Frost pocket: ponded air below zero whitens").scale(0.9).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"the floor; any hollow that traps drainage").scale(0.9).shift(band_shift(5) + UP * 0.5)
        b5_l3 = Tex(r"freezes first — the Underberg hollows").scale(0.9).shift(band_shift(5) + DOWN * 0.2)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex(r"Radiation fog: pond cooled to dew point —").scale(0.9).shift(band_shift(5) + DOWN * 1.1)
        b5_l5 = Tex(r"white river at dawn, burning off top-down;").scale(0.9).shift(band_shift(5) + DOWN * 1.8)
        b5_l6 = Tex(r"the N3's winter dips map the inversions").scale(0.9).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(2.5)
        b5_l7 = Tex(r"The lid traps smoke: valley towns wear a").scale(0.9).shift(band_shift(5) + DOWN * 3.3)
        b5_l8 = Tex(r"grey blanket on winter mornings").scale(0.9).shift(band_shift(5) + DOWN * 4.0)
        self.play(Write(b5_l7))
        self.play(Write(b5_l8))
        self.wait(3)

        # --- Band 6 (subtopic_4): farming the physics
        self.next_band(6)
        b6_title = Tex("Farming the physics").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Frost-tender fruit and vines $\to$ the thermal").scale(0.9).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"belt: Langkloof apples ribbon the mid-slope").scale(0.9).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex(r"Aspect assigns the walls: sun-lovers north,").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex(r"chill-needers and timber south").scale(0.9).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex(r"Hardy crops take the risky floor (deep soils,").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        b6_l6 = Tex(r"the river); frost fight: wind machines,").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        b6_l7 = Tex(r"heaters, helicopters — stirring the inversion").scale(0.9).shift(band_shift(6) + DOWN * 3.3)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.wait(3)

        # --- Band 7 (subtopic_4): settlement and planning
        self.next_band(7)
        b7_title = Tex("Settlement and planning").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Farmsteads and old towns: lower slopes —").scale(0.9).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"above floods and frost, on the warm shelf").scale(0.9).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Roads and rail: the flat floor — accepting").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex(r"the fog; winter pile-ups in the dips").scale(0.9).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2)
        bad = Tex(r"low-cost housing on the valley floor").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(bad))
        self.play(Create(strike(bad)))
        self.wait(2)
        b7_l5 = Tex(r"Fix: homes on the mid-slope, industry out of").scale(0.9).shift(band_shift(7) + DOWN * 2.9)
        b7_l6 = Tex(r"the pond, floor for fields and floodplain").scale(0.9).shift(band_shift(7) + DOWN * 3.6)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the sunny wall and the shady wall
        self.next_band(8)
        b8_title = Tex("The sunny wall and the shady wall").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Torch straight at the wall: small hot circle;").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"torch at a slant: long pale smear").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex(r"Stoep side (faces north): warm, dry, vines,").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex(r"frost gone first").scale(0.95).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex(r"Pantry side (faces south): cool, damp, green,").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        b8_l6 = Tex(r"snow keeps; biggest contrast in winter,").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        b8_l7 = Tex(r"east--west valleys; flip for Europe").scale(0.95).shift(band_shift(8) + DOWN * 3.3)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): the bathtub of cold air
        self.next_band(9)
        b9_title = Tex("The bathtub that fills with cold air").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Day: sun grills the walls, breezes climb —").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex(r"anabatic ascends (two As)").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex(r"Night: walls chill, heavy air FLOWS downhill").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        b9_l4 = Tex(r"like water — katabatic, gravity's wind").scale(0.95).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex(r"The floor is the tub: full by the small hours;").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        b9_l6 = Tex(r"cold below, warm above $=$ the inversion;").scale(0.95).shift(band_shift(9) + DOWN * 2.6)
        b9_l7 = Tex(r"the warm shelf above the water line $=$").scale(0.95).shift(band_shift(9) + DOWN * 3.3)
        b9_l8 = Tex(r"the THERMAL BELT").scale(1.0).shift(band_shift(9) + DOWN * 4.0)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.play(Write(b9_l8))
        self.play(Create(SurroundingRectangle(b9_l8, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): frost on the floor, money on the shelf
        self.next_band(10)
        b10_title = Tex("Frost on the floor, money on the shelf").scale(1.05).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Dawn mischief: tub below zero $=$ frost pocket;").scale(0.9).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"moist tub at dew point $=$ radiation fog;").scale(0.9).shift(band_shift(10) + UP * 0.5)
        b10_l3 = Tex(r"smoke stops under the lid — grey blanket").scale(0.9).shift(band_shift(10) + DOWN * 0.2)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"Money on the shelf: Langkloof fruit ribbons").scale(0.9).shift(band_shift(10) + DOWN * 1.1)
        b10_l5 = Tex(r"the thermal belt; sun-lovers on the stoep side;").scale(0.9).shift(band_shift(10) + DOWN * 1.8)
        b10_l6 = Tex(r"hardy crops, road and rail on the floor").scale(0.9).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l7 = Tex(r"Homes on the shelf, never at the tub's bottom;").scale(0.9).shift(band_shift(10) + DOWN * 3.3)
        b10_l8 = Tex(r"frost fight: fans and heaters stir the tub").scale(0.9).shift(band_shift(10) + DOWN * 4.0)
        self.play(Write(b10_l7))
        self.play(Write(b10_l8))
        self.wait(4)
