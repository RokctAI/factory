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

# Band-layout whiteboard scene for the CAPS Grade 11 Geography session duo
# "Pressure Belts and Global Winds". One band per teaching beat; the camera
# moves down to fresh space and nothing is removed. All diagrams hand-built
# from Line/Arrow/Dot/Circle/Rectangle/Tex (exporter-safe primitives only).
# Subtopic shares follow subtopics.json: 210/225/240/235/185/190/205 of 1490 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PressureBeltsGlobalWindsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the temperature-pressure-wind chain
        title = Tex("Pressure Belts and Global Winds").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex(r"Mean sea-level pressure: $1\,013$ hPa").scale(1.1).shift(UP * 1.1)
        self.play(Write(s0_l1))
        self.wait(2)
        s0_l2 = Tex(r"Warm air rises $\Rightarrow$ pressure falls: LOW").scale(1.1).shift(UP * 0.2)
        s0_l3 = Tex(r"Cold air sinks $\Rightarrow$ pressure rises: HIGH").scale(1.1).shift(DOWN * 0.7)
        self.play(Write(s0_l2))
        self.wait(2)
        self.play(Write(s0_l3))
        self.wait(2)
        s0_l4 = Tex(r"Wind: air moving high $\rightarrow$ low").scale(1.1).shift(DOWN * 1.7)
        self.play(Write(s0_l4))
        self.play(Create(SurroundingRectangle(s0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): isobars, weather pairing, naming winds
        self.next_band(1)
        b1_title = Tex("Isobars, weather and wind names").scale(1.15).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        # tight isobars (left) vs wide isobars (right)
        tight = VGroup(
            Line(LEFT * 5.2 + UP * 1.5, LEFT * 2.6 + UP * 1.5, color=BLUE),
            Line(LEFT * 5.2 + UP * 1.1, LEFT * 2.6 + UP * 1.1, color=BLUE),
            Line(LEFT * 5.2 + UP * 0.7, LEFT * 2.6 + UP * 0.7, color=BLUE),
        ).shift(band_shift(1))
        tight_lab = Tex("packed: strong wind").scale(0.85).shift(band_shift(1) + LEFT * 3.9 + UP * 0.1)
        wide = VGroup(
            Line(RIGHT * 2.0 + UP * 1.7, RIGHT * 4.6 + UP * 1.7, color=BLUE),
            Line(RIGHT * 2.0 + UP * 0.6, RIGHT * 4.6 + UP * 0.6, color=BLUE),
        ).shift(band_shift(1))
        wide_lab = Tex("spaced: light wind").scale(0.85).shift(band_shift(1) + RIGHT * 3.3 + UP * 0.0)
        self.play(Create(tight[0]), Create(tight[1]), Create(tight[2]))
        self.play(Write(tight_lab))
        self.wait(1.5)
        self.play(Create(wide[0]), Create(wide[1]))
        self.play(Write(wide_lab))
        self.wait(2)
        b1_l1 = Tex("LOW: air rises, cools, condenses — rain").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        b1_l2 = Tex("HIGH: air subsides, warms — clear, dry").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(VGroup(b1_l1, b1_l2), color=GREEN)))
        self.wait(2)
        b1_l3 = Tex(r"Named FROM: south-easter $= 135^\circ$").scale(1.0).shift(band_shift(1) + DOWN * 2.6)
        b1_l4 = MathTex(r"360 \div 16 = 22{,}5^\circ \text{ per point}").scale(0.95).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the belts, equator to pole
        self.next_band(2)
        b2_title = Tex("The world's pressure belts").scale(1.15).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_title))
        self.wait(1.5)
        # latitude column: equator at left, pole at right
        lat = Line(LEFT * 5.5 + UP * 1.2, RIGHT * 5.5 + UP * 1.2, color=WHITE).shift(band_shift(2))
        self.play(Create(lat))
        d0 = Dot(LEFT * 5.0 + UP * 1.2).shift(band_shift(2))
        d30 = Dot(LEFT * 1.7 + UP * 1.2).shift(band_shift(2))
        d60 = Dot(RIGHT * 1.7 + UP * 1.2).shift(band_shift(2))
        d90 = Dot(RIGHT * 5.0 + UP * 1.2).shift(band_shift(2))
        l0 = MathTex(r"0^\circ").scale(0.85).shift(band_shift(2) + LEFT * 5.0 + UP * 1.8)
        l30 = MathTex(r"30^\circ").scale(0.85).shift(band_shift(2) + LEFT * 1.7 + UP * 1.8)
        l60 = MathTex(r"60^\circ").scale(0.85).shift(band_shift(2) + RIGHT * 1.7 + UP * 1.8)
        l90 = MathTex(r"90^\circ").scale(0.85).shift(band_shift(2) + RIGHT * 5.0 + UP * 1.8)
        self.play(Create(d0), Create(d30), Create(d60), Create(d90))
        self.play(Write(l0), Write(l30), Write(l60), Write(l90))
        self.wait(2)
        b2_l1 = Tex("Equatorial LOW (ITCZ): rising, doldrums").scale(0.95).shift(band_shift(2) + UP * 0.4)
        b2_l2 = Tex("Subtropical HIGHS: subsiding — deserts").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        b2_l3 = Tex("Sub-polar LOWS: polar front, cyclones").scale(0.95).shift(band_shift(2) + DOWN * 1.2)
        b2_l4 = Tex("Polar HIGHS: cold dense air sinks").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Kalahari, S Atlantic and S Indian Highs").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the migration and two rainfall regimes
        self.next_band(3)
        b3_title = Tex(r"Belts slide $\approx 5^\circ$ with the sun").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("June: belts move NORTH").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("Westerlies reach the Cape: winter rain").scale(1.0).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex("Kalahari High: dry, cold Highveld").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("December: belts move SOUTH").scale(1.05).shift(band_shift(3) + DOWN * 1.4)
        b3_l5 = Tex("Moist tropical air into Limpopo, Gauteng").scale(1.0).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        b3_l6 = Tex("One migration, two rainfall regimes").scale(1.0).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the tri-cellular cross-section
        self.next_band(4)
        b4_title = Tex("Three cells per hemisphere").scale(1.15).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        ground4 = Line(LEFT * 6.0 + DOWN * 1.5, RIGHT * 6.0 + DOWN * 1.5, color=WHITE).shift(band_shift(4))
        self.play(Create(ground4))
        g0 = MathTex(r"0^\circ").scale(0.8).shift(band_shift(4) + LEFT * 5.6 + DOWN * 2.1)
        g30 = MathTex(r"30^\circ").scale(0.8).shift(band_shift(4) + LEFT * 1.8 + DOWN * 2.1)
        g60 = MathTex(r"60^\circ").scale(0.8).shift(band_shift(4) + RIGHT * 1.8 + DOWN * 2.1)
        g90 = MathTex(r"90^\circ").scale(0.8).shift(band_shift(4) + RIGHT * 5.6 + DOWN * 2.1)
        self.play(Write(g0), Write(g30), Write(g60), Write(g90))
        # Hadley loop: rise at 0, poleward aloft, sink at 30, trades back
        h_up = Arrow(LEFT * 5.4 + DOWN * 1.4, LEFT * 5.4 + UP * 1.2, color=RED, buff=0).shift(band_shift(4))
        h_top = Arrow(LEFT * 5.2 + UP * 1.3, LEFT * 2.0 + UP * 1.3, color=RED, buff=0).shift(band_shift(4))
        h_dn = Arrow(LEFT * 1.8 + UP * 1.2, LEFT * 1.8 + DOWN * 1.4, color=BLUE, buff=0).shift(band_shift(4))
        h_sfc = Arrow(LEFT * 2.0 + DOWN * 1.2, LEFT * 5.2 + DOWN * 1.2, color=BLUE, buff=0).shift(band_shift(4))
        h_lab = Tex("HADLEY: trades").scale(0.85).shift(band_shift(4) + LEFT * 3.6 + DOWN * 0.5)
        self.play(Create(h_up), Create(h_top))
        self.play(Create(h_dn), Create(h_sfc), Write(h_lab))
        self.wait(2)
        # Ferrel loop (indirect): surface poleward, rise at 60
        f_sfc = Arrow(LEFT * 1.6 + DOWN * 1.2, RIGHT * 1.6 + DOWN * 1.2, color=BLUE, buff=0).shift(band_shift(4))
        f_up = Arrow(RIGHT * 1.8 + DOWN * 1.4, RIGHT * 1.8 + UP * 1.2, color=RED, buff=0).shift(band_shift(4))
        f_lab = Tex("FERREL: westerlies").scale(0.85).shift(band_shift(4) + UP * 0.0)
        self.play(Create(f_sfc), Create(f_up), Write(f_lab))
        self.wait(2)
        # Polar loop
        p_dn = Arrow(RIGHT * 5.4 + UP * 1.2, RIGHT * 5.4 + DOWN * 1.4, color=BLUE, buff=0).shift(band_shift(4))
        p_sfc = Arrow(RIGHT * 5.2 + DOWN * 1.2, RIGHT * 2.0 + DOWN * 1.2, color=BLUE, buff=0).shift(band_shift(4))
        p_lab = Tex("POLAR: easterlies").scale(0.85).shift(band_shift(4) + RIGHT * 3.7 + DOWN * 0.5)
        self.play(Create(p_dn), Create(p_sfc), Write(p_lab))
        self.wait(2)
        b4_l1 = Tex("Jet streams at the joins: $>200$ km/h").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l1))
        self.wait(3)

        # --- Band 5 (subtopic_3): the forces that bend the wind
        self.next_band(5)
        b5_title = Tex("The forces that bend every wind").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Pressure gradient force: high $\rightarrow$ low").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("Coriolis: LEFT in Southern Hemisphere").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("Zero at equator, greatest at poles").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("Aloft: geostrophic — parallel to isobars").scale(1.0).shift(band_shift(5) + DOWN * 1.3)
        b5_l5 = Tex(r"Surface friction: crosses into the low").scale(1.0).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(2)
        b5_l6 = Tex("Buys Ballot: back to wind, low on RIGHT").scale(1.0).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): air masses and local winds
        self.next_band(6)
        b6_title = Tex("Air masses and local winds").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Maritime tropical: warm, humid — east coast").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("Continental tropical: hot, dry — heatwaves").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Maritime polar: cold, moist — behind fronts").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Day: sea breeze onshore — Durban relief").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        b6_l5 = Tex("Night: land breeze offshore").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        b6_l6 = Tex("Anabatic up by day, katabatic down by night").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.wait(2)
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): the berg-wind calculation
        self.next_band(7)
        b7_title = Tex("Berg wind — the calculation").scale(1.15).shift(band_shift(7) + UP * 2.6)
        self.play(Write(b7_title))
        self.wait(1.5)
        # escarpment profile: plateau, steep descent, coast
        prof = VGroup(
            Line(LEFT * 5.5 + UP * 1.2, LEFT * 2.0 + UP * 1.2, color=WHITE),
            Line(LEFT * 2.0 + UP * 1.2, RIGHT * 1.5 + DOWN * 1.2, color=WHITE),
            Line(RIGHT * 1.5 + DOWN * 1.2, RIGHT * 5.5 + DOWN * 1.2, color=WHITE),
        ).shift(band_shift(7))
        self.play(Create(prof[0]), Create(prof[1]), Create(prof[2]))
        plat_lab = Tex(r"plateau $1\,800$ m, $12\,^\circ$C").scale(0.85).shift(band_shift(7) + LEFT * 3.9 + UP * 1.8)
        coast_lab = Tex("sea level").scale(0.85).shift(band_shift(7) + RIGHT * 3.7 + DOWN * 0.7)
        flow = Arrow(LEFT * 2.2 + UP * 1.5, RIGHT * 1.7 + DOWN * 0.9, color=RED, buff=0).shift(band_shift(7))
        self.play(Write(plat_lab), Write(coast_lab))
        self.play(Create(flow))
        self.wait(2)
        b7_l1 = Tex(r"DALR: $1\,^\circ$C per 100 m of descent").scale(0.93).shift(band_shift(7) + DOWN * 1.7 + LEFT * 2.4)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"1\,800 \div 100 \times 1 = 18\,^\circ\text{C}").scale(0.99).shift(band_shift(7) + DOWN * 2.4 + LEFT * 2.4)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"12 + 18 = 30\,^\circ\text{C}").scale(1.1).shift(band_shift(7) + DOWN * 3.0 + LEFT * 2.4)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex("Hot, dry, dusty — fire danger,").scale(0.9).shift(band_shift(7) + DOWN * 2.2 + RIGHT * 3.6)
        b7_l5 = Tex("often a day before a front").scale(0.9).shift(band_shift(7) + DOWN * 2.9 + RIGHT * 3.6)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the whole machine in a kitchen
        self.next_band(8)
        b8_title = Tex("Hot air rises — the kitchen machine").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Kettle steam climbs: LOW forms below").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("Freezer air spills to your ankles: HIGH").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex(r"Full taxi $\rightarrow$ empty taxi $=$ wind").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex("Taxis parked close: fast scramble").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Fogged mirror: rising air rains (LOW)").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        b8_l6 = Tex("Hair dryer: sinking air dries (HIGH)").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l5))
        self.wait(2)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(VGroup(b8_l5, b8_l6), color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): three revolving doors
        self.next_band(9)
        b9_title = Tex("Three loops around the planet").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Door 1: sun-driven — up at the equator,").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l1b = Tex(r"down at $30^\circ$ — the desert ring").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l1b))
        self.wait(2.5)
        b9_l2 = Tex("Door 2: lazy — pushed by its neighbours,").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        b9_l2b = Tex("westerlies hurling fronts at Cape Town").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l2))
        self.play(Write(b9_l2b))
        self.wait(2.5)
        b9_l3 = Tex("Door 3: polar easterlies creep out").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Belts slide with the sun: two rainy seasons").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): why wind never walks straight
        self.next_band(10)
        b10_title = Tex("Why wind never walks straight").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Ball across a roundabout: it bends —").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("the ground turned underneath: CORIOLIS").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("South of the equator: bends LEFT").scale(1.05).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = Tex("Back to the wind: low on your RIGHT").scale(1.0).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = MathTex(r"\text{Berg wind: } 1\,800 \div 100 = 18").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        b10_l6 = MathTex(r"12 + 18 = 30\,^\circ\text{C at the coast}").scale(1.0).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l5))
        self.wait(2)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
