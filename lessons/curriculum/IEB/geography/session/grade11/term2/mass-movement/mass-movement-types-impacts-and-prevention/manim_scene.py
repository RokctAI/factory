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

# Band-layout whiteboard scene for the IEB Grade 11 Geography session duo
# "Mass Movement — Types, Impacts and Prevention". One band per teaching
# beat; the camera moves down, nothing is removed. Diagrams hand-built from
# Line/Arrow/Dot/Circle/Rectangle/Tex only (exporter-safe primitives).
# Subtopic shares follow subtopics.json: 215/235/230/240/185/195/215 of 1515 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MassMovementSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): definition and the arm-wrestle
        title = Tex("Mass Movement: Types, Impacts, Prevention").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("Downslope movement under GRAVITY —").scale(1.1).shift(UP * 1.1)
        s0_l2 = Tex("no river, glacier or wind carrying it").scale(1.1).shift(UP * 0.3)
        self.play(Write(s0_l1))
        self.play(Write(s0_l2))
        self.play(Create(SurroundingRectangle(VGroup(s0_l1, s0_l2), color=GREEN)))
        self.wait(2.5)
        slope0 = Line(LEFT * 4.5 + DOWN * 2.6, RIGHT * 4.5 + DOWN * 1.0, color=WHITE)
        self.play(Create(slope0))
        drive = Arrow(RIGHT * 1.0 + DOWN * 1.4, LEFT * 1.0 + DOWN * 2.0, color=RED, buff=0)
        d_lab = Tex("gravity drives").scale(0.85).shift(LEFT * 3.4 + DOWN * 1.2)
        hold = Arrow(LEFT * 1.6 + DOWN * 2.3, RIGHT * 0.4 + DOWN * 1.7, color=YELLOW, buff=0)
        h_lab = Tex("friction, grip, roots hold").scale(0.85).shift(RIGHT * 3.9 + DOWN * 2.4)
        self.play(Create(drive), Write(d_lab))
        self.play(Create(hold), Write(h_lab))
        self.wait(3)

        # --- Band 1 (subtopic_1): water and the other triggers
        self.next_band(1)
        b1_title = Tex("Water plays both sides").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Damp: surface tension binds the grains").scale(1.0).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("Saturated: pores full, grains apart,").scale(1.0).shift(band_shift(1) + UP * 0.6)
        b1_l2b = Tex("extra weight, slide surfaces greased").scale(1.0).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Write(b1_l2b))
        self.wait(2.5)
        b1_l3 = Tex("Other triggers: undercut toe, quakes,").scale(0.95).shift(band_shift(1) + DOWN * 1.2)
        b1_l3b = Tex("freeze-thaw, stripped roots, leaks, cuts").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l3))
        self.play(Write(b1_l3b))
        self.wait(2)
        b1_l4 = Tex("Most disasters arrive with rain").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the slow movers
        self.next_band(2)
        b2_title = Tex("The slow lanes: creep and solifluction").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("CREEP: soil blanket, millimetres a year —").scale(0.95).shift(band_shift(2) + UP * 1.4)
        b2_l1b = Tex("lift perpendicular, settle vertical").scale(0.95).shift(band_shift(2) + UP * 0.6)
        self.play(Write(b2_l1))
        self.play(Write(b2_l1b))
        self.wait(2)
        # leaning post evidence
        ground2 = Line(LEFT * 5.5 + DOWN * 2.2, LEFT * 0.5 + DOWN * 1.4, color=WHITE).shift(band_shift(2))
        post = Line(LEFT * 3.0 + DOWN * 1.8, LEFT * 2.4 + DOWN * 0.2, color=YELLOW).shift(band_shift(2))
        post_lab = Tex("leaning post").scale(0.8).shift(band_shift(2) + LEFT * 2.7 + UP * 0.5)
        self.play(Create(ground2), Create(post), Write(post_lab))
        self.wait(2)
        b2_l2 = Tex("Evidence: posts, curved trunks,").scale(0.95).shift(band_shift(2) + RIGHT * 3.2 + DOWN * 0.3)
        b2_l2b = Tex("terracettes, soil against walls").scale(0.95).shift(band_shift(2) + RIGHT * 3.2 + DOWN * 1.1)
        self.play(Write(b2_l2))
        self.play(Write(b2_l2b))
        self.wait(2)
        b2_l3 = Tex("SOLIFLUCTION: thawed sludge flows in lobes").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        b2_l3b = Tex("over frozen subsoil — high Maloti-Drakensberg").scale(0.95).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l3))
        self.play(Write(b2_l3b))
        self.wait(3)

        # --- Band 3 (subtopic_2): the fast movers and the grid
        self.next_band(3)
        b3_title = Tex("The fast lanes").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("LANDSLIDE: one slab, one slide surface").scale(0.95).shift(band_shift(3) + UP * 1.5)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("SLUMP: curved spoon surface — block").scale(0.95).shift(band_shift(3) + UP * 0.7)
        b3_l2b = Tex("ROTATES; crescent scar, tilted block").scale(0.95).shift(band_shift(3) + DOWN * 0.1)
        self.play(Write(b3_l2))
        self.play(Write(b3_l2b))
        self.wait(2)
        b3_l3 = Tex("ROCK FALL: free-fall off the cliff, talus below").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("MUD FLOW: saturated debris as fluid —").scale(0.95).shift(band_shift(3) + DOWN * 1.7)
        b3_l4b = Tex("valley speed, sets like concrete").scale(0.95).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l4))
        self.play(Write(b3_l4b))
        self.wait(2)
        b3_l5 = Tex("Grid: creep, solifluction, slide, slump, fall, flow").scale(0.9).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): impacts on land and people
        self.next_band(4)
        b4_title = Tex("Impacts: land, then people").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Scars stripped to bedrock; topsoil buried;").scale(0.95).shift(band_shift(4) + UP * 1.4)
        b4_l1b = Tex("rivers choked, dams silted, gullies open").scale(0.95).shift(band_shift(4) + UP * 0.6)
        self.play(Write(b4_l1))
        self.play(Write(b4_l1b))
        self.wait(2.5)
        b4_l2 = Tex("Creep: slow tax — tilted poles, cracked walls").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        b4_l3 = Tex("Rock falls: Van Reenen's and Sani Pass").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        b4_l4 = Tex("Slides and flows: houses, roads, lives").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("Hazard is natural; exposure is social").scale(1.0).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): KwaZulu-Natal, April 2022
        self.next_band(5)
        b5_title = Tex("Case study: KwaZulu-Natal, April 2022").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("300$+$ mm in 24 hours over the Durban metro").scale(1.0).shift(band_shift(5) + UP * 1.4)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2)
        b5_l2 = Tex("Hundreds of failures in one night;").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l2b = Tex("400$+$ deaths; billions in damage").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l2))
        self.play(Write(b5_l2b))
        self.wait(2.5)
        b5_l3 = Tex("Trigger: extreme rain. Setting: steep").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        b5_l3b = Tex("soaked hills. Multiplier: exposed settlement").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l3))
        self.play(Write(b5_l3b))
        self.wait(2)
        b5_l4 = Tex("Merriespruit 1994: tailings mud flow, 17 dead").scale(0.9).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): reshape the slope, control the water
        self.next_band(6)
        b6_title = Tex("Reshape the slope, control the water").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Regrade cuts; terrace long slopes;").scale(0.95).shift(band_shift(6) + UP * 1.4)
        b6_l1b = Tex("retaining walls and GABIONS at the toe").scale(0.95).shift(band_shift(6) + UP * 0.6)
        self.play(Write(b6_l1))
        self.play(Write(b6_l1b))
        self.wait(2.5)
        b6_l2 = Tex("Anchor bolts; mesh and catch fences").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        b6_l2b = Tex("above the mountain-pass hairpins").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l2))
        self.play(Write(b6_l2b))
        self.wait(2.5)
        b6_l3 = Tex("Cut-off drains at the crest; buried drains").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        b6_l3b = Tex("bleed the slope; fix leaks; no outlets at faces").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l3))
        self.play(Write(b6_l3b))
        self.wait(3)

        # --- Band 7 (subtopic_4): protect the surface, plan the settlement
        self.next_band(7)
        b7_title = Tex("Protect the surface, plan the settlement").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Vegetation: engineering that grows —").scale(0.95).shift(band_shift(7) + UP * 1.4)
        b7_l1b = Tex("roots bind, canopies shield, leaves pump").scale(0.95).shift(band_shift(7) + UP * 0.6)
        self.play(Write(b7_l1))
        self.play(Write(b7_l1b))
        self.wait(2.5)
        b7_l2 = Tex("GIS hazard maps: slope $+$ soil $+$ rain").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        b7_l2b = Tex("overlay paints the red zones").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l2))
        self.play(Write(b7_l2b))
        self.wait(2.5)
        b7_l3 = Tex("Rainfall-triggered warnings — Durban since 2022;").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        b7_l3b = Tex("upgrade or relocate with dignity").scale(0.9).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l3))
        self.play(Write(b7_l3b))
        self.play(Create(SurroundingRectangle(b7_l3b, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the arm-wrestle and the rusk
        self.next_band(8)
        b8_title = Tex("The arm-wrestle and the rusk").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Gravity vs friction, grip and roots").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("Failure $=$ the moment the arm goes down").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Quick dip: rusk holds — damp binds").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex("Long soak: rusk lets go — saturation kills").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex("Cut the toe, strip the grass, leak the pipe:").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        b8_l5b = Tex("three own-goals on one hillside").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l5))
        self.play(Write(b8_l5b))
        self.wait(3)

        # --- Band 9 (subtopic_6): the six lanes
        self.next_band(9)
        b9_title = Tex("Six lanes on the starting grid").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("1 creep: posts lean, trunks curve").scale(0.95).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex("2 solifluction: cold sludge over ice").scale(0.95).shift(band_shift(9) + UP * 0.5)
        b9_l3 = Tex("3 landslide: bricks off the tipper").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        b9_l4 = Tex("4 slump: ice-cream scoop rotates").scale(0.95).shift(band_shift(9) + DOWN * 1.1)
        b9_l5 = Tex("5 rock fall: pure drop into the nets").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        b9_l6 = Tex("6 mud flow: boulder milkshake at speed").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l1))
        self.wait(1.5)
        self.play(Write(b9_l2))
        self.wait(1.5)
        self.play(Write(b9_l3))
        self.wait(1.5)
        self.play(Write(b9_l4))
        self.wait(1.5)
        self.play(Write(b9_l5))
        self.wait(1.5)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): April 2022 and the four moves
        self.next_band(10)
        b10_title = Tex("April 2022 and the four moves").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("300$+$ mm / 24 h; 400$+$ lives; billions lost").scale(0.95).shift(band_shift(10) + UP * 1.3)
        b10_l2 = Tex("Same rain, unequal risk").scale(1.05).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex("RESHAPE — terraces, gabions, nets").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10_l4 = Tex("DRAIN — catch, bleed, fix the leaks").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        b10_l5 = Tex("PLANT — roots are free engineering").scale(0.95).shift(band_shift(10) + DOWN * 2.1)
        b10_l6 = Tex("PLAN — red zones, warnings, dignity").scale(0.95).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l3))
        self.wait(1.5)
        self.play(Write(b10_l4))
        self.wait(1.5)
        self.play(Write(b10_l5))
        self.wait(1.5)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
