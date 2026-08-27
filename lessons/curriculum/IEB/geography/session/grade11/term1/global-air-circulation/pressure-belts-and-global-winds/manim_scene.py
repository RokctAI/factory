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
# "Pressure Belts and Global Winds". One band per teaching beat; the camera
# moves down to fresh space and nothing is ever removed. Diagrams are
# hand-built from Line/Arrow/Dot/Circle/Tex only (exporter-safe).
# Subtopic time shares follow subtopics.json:
# 210/225/240/235/185/190/205 of 1490 s.

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
        # Intro beat: topic held full screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the temperature-pressure-wind chain
        title = Tex("Pressure Belts and Global Winds").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex(r"Sea-level mean: $1\,013$ hPa").scale(1.1).shift(UP * 1.0)
        self.play(Write(s0_l1))
        self.wait(2)
        s0_l2 = Tex("Warm air rises $\\rightarrow$ surface LOW").scale(1.1).shift(UP * 0.1)
        self.play(Write(s0_l2))
        self.wait(2)
        s0_l3 = Tex("Cold air sinks $\\rightarrow$ surface HIGH").scale(1.1).shift(DOWN * 0.8)
        self.play(Write(s0_l3))
        self.wait(2)
        s0_l4 = Tex("Wind: air flowing high $\\rightarrow$ low").scale(1.1).shift(DOWN * 1.8)
        self.play(Write(s0_l4))
        self.play(Create(SurroundingRectangle(s0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): isobars, weather pairing, naming winds
        self.next_band(1)
        b1_title = Tex("Isobars, weather, wind names").scale(1.2).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        # tight isobars on the left, loose on the right
        iso_t = VGroup(
            Line(LEFT * 5.0 + UP * 1.4, LEFT * 2.4 + UP * 1.4, color=WHITE),
            Line(LEFT * 5.0 + UP * 1.0, LEFT * 2.4 + UP * 1.0, color=WHITE),
            Line(LEFT * 5.0 + UP * 0.6, LEFT * 2.4 + UP * 0.6, color=WHITE),
        ).shift(band_shift(1))
        iso_lab = Tex("tight: strong wind").scale(0.85).shift(band_shift(1) + LEFT * 3.7 + DOWN * 0.1)
        loose = VGroup(
            Line(RIGHT * 2.0 + UP * 1.5, RIGHT * 4.6 + UP * 1.5, color=WHITE),
            Line(RIGHT * 2.0 + UP * 0.5, RIGHT * 4.6 + UP * 0.5, color=WHITE),
        ).shift(band_shift(1))
        loose_lab = Tex("spaced: light wind").scale(0.85).shift(band_shift(1) + RIGHT * 3.3 + DOWN * 0.1)
        self.play(Create(iso_t[0]), Create(iso_t[1]), Create(iso_t[2]))
        self.play(Write(iso_lab))
        self.wait(2)
        self.play(Create(loose[0]), Create(loose[1]))
        self.play(Write(loose_lab))
        self.wait(2)
        b1_l1 = Tex("LOW: rising, cloud, rain").scale(1.0).shift(band_shift(1) + DOWN * 1.0)
        b1_l2 = Tex("HIGH: subsiding, clear, dry").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = Tex(r"Named FROM: south-westerly $= 225^\circ$").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l3))
        self.wait(3)

        # --- Band 2 (subtopic_2): the belts, equator to pole
        self.next_band(2)
        b2_title = Tex("The pressure belts").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"$0^\circ$: equatorial LOW — ITCZ, doldrums").scale(1.0).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex(r"$30^\circ$: subtropical HIGHS — deserts").scale(1.0).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex(r"$60^\circ$: sub-polar LOWS — polar front").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex(r"$90^\circ$: polar HIGHS — cold sinking air").scale(1.0).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Ours: S Atlantic, S Indian, continental").scale(0.95).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the migration and two rainfall regimes
        self.next_band(3)
        b3_title = Tex(r"The belts slide $\approx 5^\circ$ with the sun").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        # north-south slider
        rail = Line(UP * 1.6, DOWN * 0.4, color=WHITE).shift(band_shift(3) + LEFT * 4.0)
        knob = Dot(LEFT * 4.0 + UP * 1.2).shift(band_shift(3))
        self.play(Create(rail), Create(knob))
        b3_l1 = Tex("June: north — fronts over the SW Cape").scale(1.0).shift(band_shift(3) + RIGHT * 0.8 + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex("winter rain, dry frosty plateau").scale(0.95).shift(band_shift(3) + RIGHT * 0.8 + UP * 0.3)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("December: south — fronts miss us,").scale(1.0).shift(band_shift(3) + RIGHT * 0.8 + DOWN * 0.7)
        b3_l4 = Tex("moist air floods the interior").scale(1.0).shift(band_shift(3) + RIGHT * 0.8 + DOWN * 1.5)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex("One migration, two rainfall calendars").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the tri-cellular cross-section
        self.next_band(4)
        b4_title = Tex("Three cells per hemisphere").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        base = Line(LEFT * 5.2 + DOWN * 1.2, RIGHT * 5.2 + DOWN * 1.2, color=WHITE).shift(band_shift(4))
        self.play(Create(base))
        # Hadley loop
        h_up = Arrow(LEFT * 4.6 + DOWN * 1.1, LEFT * 4.6 + UP * 1.0, color=YELLOW, buff=0).shift(band_shift(4))
        h_top = Arrow(LEFT * 4.6 + UP * 1.0, LEFT * 1.8 + UP * 1.0, color=YELLOW, buff=0).shift(band_shift(4))
        h_dn = Arrow(LEFT * 1.8 + UP * 1.0, LEFT * 1.8 + DOWN * 1.1, color=YELLOW, buff=0).shift(band_shift(4))
        h_lab = Tex("Hadley: trades").scale(0.85).shift(band_shift(4) + LEFT * 3.3 + DOWN * 1.7)
        self.play(Create(h_up), Create(h_top), Create(h_dn))
        self.play(Write(h_lab))
        self.wait(2)
        # Ferrel loop
        f_sfc = Arrow(LEFT * 1.6 + DOWN * 1.0, RIGHT * 1.6 + DOWN * 1.0, color=BLUE, buff=0).shift(band_shift(4))
        f_lab = Tex("Ferrel: westerlies").scale(0.85).shift(band_shift(4) + RIGHT * 0.0 + DOWN * 1.7)
        self.play(Create(f_sfc), Write(f_lab))
        self.wait(2)
        # Polar loop
        p_dn = Arrow(RIGHT * 4.6 + UP * 1.0, RIGHT * 4.6 + DOWN * 1.1, color=WHITE, buff=0).shift(band_shift(4))
        p_sfc = Arrow(RIGHT * 4.4 + DOWN * 1.0, RIGHT * 2.0 + DOWN * 1.0, color=WHITE, buff=0).shift(band_shift(4))
        p_lab = Tex("Polar: easterlies").scale(0.85).shift(band_shift(4) + RIGHT * 3.4 + DOWN * 1.7)
        self.play(Create(p_dn), Create(p_sfc))
        self.play(Write(p_lab))
        self.wait(2)
        b4_l1 = Tex(r"Jets at the joins: $>200$ km/h").scale(0.95).shift(band_shift(4) + UP * 1.8)
        self.play(Write(b4_l1))
        self.wait(3)

        # --- Band 5 (subtopic_3): the forces that bend the wind
        self.next_band(5)
        b5_title = Tex("The forces on moving air").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Pressure gradient: high $\\rightarrow$ low").scale(1.0).shift(band_shift(5) + UP * 1.3)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Coriolis: bends LEFT in the south,").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l2b = Tex("zero at the equator, direction only").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l2))
        self.play(Write(b5_l2b))
        self.wait(2.5)
        b5_l3 = Tex("Aloft: geostrophic — parallel to isobars").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex(r"Surface: crosses $10$--$20^\circ$ sea, $25$--$45^\circ$ land").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Back to wind: low on your RIGHT").scale(1.0).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): air masses and local winds
        self.next_band(6)
        b6_title = Tex("Air masses and local winds").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Maritime tropical: warm, damp — east coast").scale(0.95).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("Continental tropical: hot, parched — heatwaves").scale(0.95).shift(band_shift(6) + UP * 0.5)
        b6_l3 = Tex("Maritime polar: cold, moist — behind fronts").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Day: sea breeze in; night: land breeze out").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Slopes: anabatic up by day,").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        b6_l6 = Tex("katabatic down by night — frost pockets").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): the berg-wind calculation
        self.next_band(7)
        b7_title = Tex("The berg wind, calculated").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        # escarpment profile
        esc = VGroup(
            Line(LEFT * 5.0 + UP * 1.0, LEFT * 1.5 + UP * 1.0, color=WHITE),
            Line(LEFT * 1.5 + UP * 1.0, RIGHT * 2.5 + DOWN * 1.4, color=WHITE),
            Line(RIGHT * 2.5 + DOWN * 1.4, RIGHT * 5.0 + DOWN * 1.4, color=WHITE),
        ).shift(band_shift(7))
        self.play(Create(esc[0]), Create(esc[1]), Create(esc[2]))
        flow = Arrow(LEFT * 2.5 + UP * 1.4, RIGHT * 2.2 + DOWN * 1.0, color=YELLOW, buff=0).shift(band_shift(7))
        self.play(Create(flow))
        self.wait(2)
        b7_l1 = MathTex(r"\text{rate: } 1\,^\circ\text{C per } 100\text{ m down}").scale(1.0).shift(band_shift(7) + UP * 0.2 + LEFT * 2.6)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"1\,500 \div 100 \times 1 = 15\,^\circ\text{C}").scale(1.05).shift(band_shift(7) + DOWN * 2.2 + LEFT * 2.2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"14 + 15 = 29\,^\circ\text{C at the coast}").scale(1.05).shift(band_shift(7) + DOWN * 3.0 + LEFT * 1.8)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex("Hot, dry, fire danger — front follows").scale(0.9).shift(band_shift(7) + DOWN * 2.2 + RIGHT * 3.2)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): smoke, freezers and the bicycle pump
        self.next_band(8)
        b8_title = Tex("Smoke, freezers and the bicycle pump").scale(1.1).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Campfire smoke climbs: LOW forms below").scale(0.95).shift(band_shift(8) + UP * 1.3)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Freezer air spills down: HIGH stacks up").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Wind: packed hall empties into corridor").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Rising cools: breath-cloud, rain").scale(0.95).shift(band_shift(8) + DOWN * 1.1)
        b8_l5 = Tex("Sinking squashes: pump barrel, blue sky").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("Low, wet; high, dry").scale(1.05).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): three escalator loops
        self.next_band(9)
        b9_title = Tex("Three loops around the planet").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Loop 1: up at the equator,").scale(0.95).shift(band_shift(9) + UP * 1.3)
        b9_l1b = Tex(r"down at $30^\circ$ — the desert ring").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l1b))
        self.wait(2.5)
        b9_l2 = Tex("Loop 2: the freeloader — westerlies").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Loop 3: polar easterlies creep out").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("The hall rolls $5^\\circ$ with the seasons:").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        b9_l5 = Tex("June fronts to the Cape, December storms inland").scale(0.9).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): lazy Susan, Buys Ballot, berg wind, monsoon
        self.next_band(10)
        b10_title = Tex("Why wind never walks straight").scale(1.15).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(2)
        # lazy Susan: circle with a curved-looking chord of two segments
        tray = Circle(radius=1.1, color=WHITE).shift(band_shift(10) + LEFT * 3.4 + UP * 0.6)
        chord = VGroup(
            Line(LEFT * 4.3 + UP * 0.9, LEFT * 3.3 + UP * 0.4, color=YELLOW),
            Line(LEFT * 3.3 + UP * 0.4, LEFT * 2.6 + UP * 1.1, color=YELLOW),
        ).shift(band_shift(10))
        tray_lab = Tex("straight hand, curved line").scale(0.85).shift(band_shift(10) + LEFT * 3.3 + DOWN * 0.9)
        self.play(Create(tray))
        self.play(Create(chord[0]), Create(chord[1]))
        self.play(Write(tray_lab))
        self.wait(2)
        b10_l1 = Tex("South of the equator: bend LEFT").scale(0.95).shift(band_shift(10) + RIGHT * 2.4 + UP * 0.9)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("Back to wind, low on the RIGHT").scale(0.95).shift(band_shift(10) + RIGHT * 2.4 + UP * 0.1)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = MathTex(r"1\,500 \div 100 = 15;\;\; 14 + 15 = 29\,^\circ\text{C}").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = Tex("Monsoon: a sea breeze on a calendar").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l4))
        self.wait(4)
