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

# Band-layout whiteboard scene for the CAPS Grade 11 Geography session duo
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
        # --- Band 0 (subtopic_1): definition and the contest
        title = Tex("Mass Movement: Types, Impacts, Prevention").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("Downslope movement under GRAVITY,").scale(1.1).shift(UP * 1.1)
        s0_l2 = Tex("with NO transporting agent").scale(1.1).shift(UP * 0.3)
        self.play(Write(s0_l1))
        self.play(Write(s0_l2))
        self.play(Create(SurroundingRectangle(VGroup(s0_l1, s0_l2), color=GREEN)))
        self.wait(2.5)
        # tug-of-war on a slope
        slope0 = Line(LEFT * 4.5 + DOWN * 2.6, RIGHT * 4.5 + DOWN * 1.0, color=WHITE)
        drive = Arrow(RIGHT * 0.6 + DOWN * 1.5, LEFT * 1.6 + DOWN * 1.9, color=RED, buff=0)
        resist = Arrow(LEFT * 1.6 + DOWN * 2.2, RIGHT * 0.6 + DOWN * 1.8, color=BLUE, buff=0)
        d_lab = Tex("gravity drives").scale(0.85).shift(LEFT * 3.4 + DOWN * 1.3)
        r_lab = Tex("friction, roots resist").scale(0.85).shift(RIGHT * 3.7 + DOWN * 2.5)
        self.play(Create(slope0))
        self.play(Create(drive), Write(d_lab))
        self.play(Create(resist), Write(r_lab))
        self.wait(3)

        # --- Band 1 (subtopic_1): water and the other triggers
        self.next_band(1)
        b1_title = Tex("Water: the great destabiliser").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("A little binds (damp sandcastle);").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("saturation pushes grains apart, adds").scale(1.0).shift(band_shift(1) + UP * 0.4)
        b1_l3 = Tex("weight, lubricates slide surfaces").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex("Triggers: undercutting the base,").scale(0.95).shift(band_shift(1) + DOWN * 1.3)
        b1_l5 = Tex("earthquakes, freeze-thaw — and people:").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        b1_l6 = Tex("stripped roots, loads, leaks, steep cuts").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): the slow movers
        self.next_band(2)
        b2_title = Tex("Slow movers: creep and solifluction").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("SOIL CREEP: millimetres per year").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("Evidence: tilted posts and gravestones,").scale(0.95).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("curved trunks, terracettes, soil").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex("piled upslope of walls").scale(0.95).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l2))
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = Tex("SOLIFLUCTION: thawed, waterlogged layer").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        b2_l6 = Tex("flows over frozen subsoil — Drakensberg").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): the fast movers and the ladder
        self.next_band(3)
        b3_title = Tex("Slides, falls and flows").scale(1.15).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("LANDSLIDE: mass slides on a plane").scale(0.95).shift(band_shift(3) + UP * 1.7)
        b3_l2 = Tex("SLUMP: curved surface — mass ROTATES,").scale(0.95).shift(band_shift(3) + UP * 0.9)
        b3_l2b = Tex("crescent scar above, tilted block below").scale(0.95).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Write(b3_l2b))
        self.wait(2)
        # slump spoon: curved surface as 3-segment chain
        spoon = VGroup(
            Line(LEFT * 5.2 + UP * 0.2, LEFT * 4.6 + DOWN * 0.9, color=RED),
            Line(LEFT * 4.6 + DOWN * 0.9, LEFT * 3.4 + DOWN * 1.5, color=RED),
            Line(LEFT * 3.4 + DOWN * 1.5, LEFT * 2.2 + DOWN * 1.6, color=RED),
        ).shift(band_shift(3))
        spoon_lab = Tex("spoon-shaped slide plane").scale(0.8).shift(band_shift(3) + LEFT * 3.6 + DOWN * 2.3)
        self.play(Create(spoon[0]), Create(spoon[1]), Create(spoon[2]))
        self.play(Write(spoon_lab))
        self.wait(2)
        b3_l3 = Tex("ROCK FALL: free-fall onto talus").scale(0.95).shift(band_shift(3) + RIGHT * 2.6 + DOWN * 0.9)
        b3_l4 = Tex("MUD FLOW: fluid, fastest, deadliest").scale(0.95).shift(band_shift(3) + RIGHT * 2.6 + DOWN * 1.7)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Ladder: speed up, water up").scale(1.0).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): impacts on land and people
        self.next_band(4)
        b4_title = Tex("Impacts").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Environment: topsoil buried, rivers").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l1b = Tex("choked with sediment, dams silted").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l1b))
        self.wait(2.5)
        b4_l2 = Tex("People: creep cracks walls; rock falls").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        b4_l2b = Tex("close passes; flows destroy in seconds").scale(1.0).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l2))
        self.play(Write(b4_l2b))
        self.wait(2.5)
        b4_l3 = Tex("Poverty pushes settlement onto the").scale(1.0).shift(band_shift(4) + DOWN * 2.2)
        b4_l3b = Tex("steepest, least stable slopes").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l3))
        self.play(Write(b4_l3b))
        self.wait(3)

        # --- Band 5 (subtopic_3): KwaZulu-Natal, April 2022
        self.next_band(5)
        b5_title = Tex("Case study: KwaZulu-Natal, April 2022").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"$>300$ mm of rain in 24 hours").scale(1.1).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2.5)
        b5_l2 = Tex("Hundreds of slope failures in one night").scale(1.0).shift(band_shift(5) + UP * 0.1)
        b5_l3 = Tex(r"$>400$ deaths, thousands of homes lost,").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        b5_l3b = Tex("billions of rands of damage").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.play(Write(b5_l3b))
        self.wait(2.5)
        b5_l4 = Tex("Trigger + setting + vulnerability").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): engineer the slope, manage the water
        self.next_band(6)
        b6_title = Tex("Engineer the slope, manage the water").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Regrade gentler; terrace long slopes;").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("retaining walls and gabions at the toe;").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("rock bolts, mesh and catch fences").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Chapman's Peak: nets, mesh, half-tunnel").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Water: cut-off drains above, subsurface").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        b6_l5b = Tex("drains within, fix leaks, no outfalls").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l5))
        self.play(Write(b6_l5b))
        self.wait(3)

        # --- Band 7 (subtopic_4): protect the surface, plan the people
        self.next_band(7)
        b7_title = Tex("Protect the surface, plan the people").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Vegetation: roots bind, plants intercept,").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l1b = Tex("transpiration dries the slope").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l1b))
        self.wait(2.5)
        b7_l2 = Tex("GIS hazard maps: overlay slope, soil,").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l2b = Tex("drainage, rainfall — keep housing off").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l2))
        self.play(Write(b7_l2b))
        self.wait(2.5)
        b7_l3 = Tex("Early-warning gauges (Durban since 2022)").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        b7_l4 = Tex("Signs: new cracks, tilting poles, springs").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the tug-of-war and the sandcastle
        self.next_band(8)
        b8_title = Tex("Why slopes let go").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Tug-of-war: gravity vs friction,").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l1b = Tex("interlock and roots stitching the soil").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l1b))
        self.wait(2.5)
        b8_l2 = Tex("Damp sand builds castles; a bucket").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l2b = Tex("of water turns the castle to soup").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l2))
        self.play(Write(b8_l2b))
        self.wait(2.5)
        b8_l3 = Tex("Lose the match: undercut the toe,").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        b8_l3b = Tex("shake the slope, strip the defenders").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l3))
        self.play(Write(b8_l3b))
        self.wait(3)

        # --- Band 9 (subtopic_6): the six gears
        self.next_band(9)
        b9_title = Tex("The six speeds of falling ground").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("1 creep: fence posts leaning drunk").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("2 solifluction: cold porridge oozing").scale(0.95).shift(band_shift(9) + UP * 0.5)
        b9_l3 = Tex("3 landslide: slab off the flatbed").scale(0.95).shift(band_shift(9) + DOWN * 0.2)
        b9_l4 = Tex("4 slump: the slide with a rotation").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        b9_l5 = Tex("5 rock fall: free-fall into the nets").scale(0.95).shift(band_shift(9) + DOWN * 1.6)
        b9_l6 = Tex("6 mud flow: porridge at highway speed").scale(0.95).shift(band_shift(9) + DOWN * 2.3)
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
        self.wait(2)
        b9_l7 = Tex("Speed up, water up").scale(1.05).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l7))
        self.play(Create(SurroundingRectangle(b9_l7, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): April 2022 and the four moves
        self.next_band(10)
        b10_title = Tex("April 2022 and how to fight back").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"300 mm in 24 h; $>400$ deaths;").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l1b = Tex("same rain, unequal risk").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.play(Create(SurroundingRectangle(b10_l1b, color=GREEN)))
        self.wait(2.5)
        b10_l2 = Tex("1 ENGINEER: terraces, walls, gabions").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10_l3 = Tex("2 DRAIN: catch, bleed, fix the leaks").scale(0.95).shift(band_shift(10) + DOWN * 1.2)
        b10_l4 = Tex("3 PLANT: roots are free engineering").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        b10_l5 = Tex("4 PLAN: GIS maps, gauges, warning signs").scale(0.95).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.wait(2)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
