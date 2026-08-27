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
# "Batholiths, Granite Domes and Tors" (massive igneous rocks).
# One band per teaching beat; the camera moves down, nothing is removed.
# Diagrams hand-built from Line/Arrow/Dot/Circle/Rectangle/Tex only.
# Subtopic shares follow subtopics.json: 220/230/230/240/185/185/210 of 1500 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BatholithsDomesTorsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): intrusive rock and the sorting test
        title = Tex("Batholiths, Granite Domes and Tors").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("Magma stalls underground: INTRUSIVE rock").scale(1.05).shift(UP * 1.0)
        self.play(Write(s0_l1))
        self.wait(2)
        s0_l2 = Tex("Slow cooling $=$ coarse crystals").scale(1.05).shift(UP * 0.2)
        self.play(Write(s0_l2))
        self.wait(2)
        s0_l3 = Tex("CONCORDANT: lies WITH the strata").scale(1.05).shift(DOWN * 0.8)
        s0_l4 = Tex("DISCORDANT: CUTS across them").scale(1.05).shift(DOWN * 1.6)
        self.play(Write(s0_l3))
        self.play(Write(s0_l4))
        self.play(Create(SurroundingRectangle(VGroup(s0_l3, s0_l4), color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the five bodies drawn
        self.next_band(1)
        b1_title = Tex("The family: batholith to sill").scale(1.15).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        # strata as horizontal lines
        st1 = Line(LEFT * 6.0 + UP * 0.8, RIGHT * 6.0 + UP * 0.8, color=BLUE).shift(band_shift(1))
        st2 = Line(LEFT * 6.0 + UP * 0.0, RIGHT * 6.0 + UP * 0.0, color=BLUE).shift(band_shift(1))
        st3 = Line(LEFT * 6.0 + DOWN * 0.8, RIGHT * 6.0 + DOWN * 0.8, color=BLUE).shift(band_shift(1))
        self.play(Create(st1), Create(st2), Create(st3))
        self.wait(1.5)
        # batholith: big mass at depth
        bath = Circle(radius=1.2, color=RED).shift(band_shift(1) + LEFT * 4.0 + DOWN * 2.2)
        bath_lab = Tex("batholith").scale(0.75).shift(band_shift(1) + LEFT * 4.0 + DOWN * 3.6)
        self.play(Create(bath), Write(bath_lab))
        self.wait(1.5)
        # sill: thick line along a stratum; dyke: vertical line
        sill = Line(LEFT * 1.2 + UP * 0.4, RIGHT * 2.2 + UP * 0.4, color=RED, stroke_width=8).shift(band_shift(1))
        sill_lab = Tex("sill").scale(0.75).shift(band_shift(1) + RIGHT * 0.5 + UP * 1.1)
        dyke = Line(RIGHT * 3.6 + DOWN * 2.6, RIGHT * 3.6 + UP * 1.4, color=RED, stroke_width=8).shift(band_shift(1))
        dyke_lab = Tex("dyke").scale(0.75).shift(band_shift(1) + RIGHT * 4.4 + UP * 1.2)
        self.play(Create(sill), Write(sill_lab))
        self.play(Create(dyke), Write(dyke_lab))
        self.wait(2)
        b1_l1 = Tex("Laccolith: arched roof. Lopolith: sagged saucer —").scale(0.85).shift(band_shift(1) + DOWN * 2.9 + RIGHT * 0.6)
        b1_l2 = Tex("Bushveld Complex, world's largest, platinum").scale(0.85).shift(band_shift(1) + DOWN * 3.5 + RIGHT * 0.6)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(3)

        # --- Band 2 (subtopic_2): exposure in two steps
        self.next_band(2)
        b2_title = Tex("Buried body to standing landform").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Step 1: erosion strips the cover").scale(1.0).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("Step 2: hard intrusion resists, country").scale(1.0).shift(band_shift(2) + UP * 0.6)
        b2_l2b = Tex("rock wastes away — differential erosion").scale(1.0).shift(band_shift(2) + DOWN * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.play(Write(b2_l2b))
        self.wait(2.5)
        b2_l3 = Tex("Batholith: granite dome country — Lowveld").scale(0.95).shift(band_shift(2) + DOWN * 1.2)
        b2_l4 = Tex("Laccolith: dome-cored hill; lopolith: basin").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): dyke and sill signatures
        self.next_band(3)
        b3_title = Tex("The sheets in the landscape").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Dyke: straight wall-ridge across country,").scale(0.95).shift(band_shift(3) + UP * 1.4)
        b3_l1b = Tex("ignores hills, rivers and contours").scale(0.95).shift(band_shift(3) + UP * 0.6)
        self.play(Write(b3_l1))
        self.play(Write(b3_l1b))
        self.wait(2.5)
        b3_l2 = Tex("Sill: level cliff band, mesa cap,").scale(0.95).shift(band_shift(3) + DOWN * 0.3)
        b3_l2b = Tex("or waterfall lip — Howick Falls, 95 m").scale(0.95).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l2))
        self.play(Write(b3_l2b))
        self.play(Create(SurroundingRectangle(b3_l2b, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Map: dyke $=$ ruler line; sill $=$ contour-hugger").scale(0.9).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l3))
        self.wait(3)

        # --- Band 4 (subtopic_3): pressure release
        self.next_band(4)
        b4_title = Tex("Unloading: the pressure comes off").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Granite set kilometres down, compressed").scale(0.95).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("Erosion strips the load; granite expands").scale(0.95).shift(band_shift(4) + UP * 0.6)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        # dome with nested curved sheets
        dome_out = Arc(radius=2.6, angle=PI, color=YELLOW).shift(band_shift(4) + DOWN * 1.8)
        dome_mid = Arc(radius=2.0, angle=PI, color=YELLOW).shift(band_shift(4) + DOWN * 1.8)
        dome_in = Arc(radius=1.4, angle=PI, color=YELLOW).shift(band_shift(4) + DOWN * 1.8)
        self.play(Create(dome_out), Create(dome_mid), Create(dome_in))
        d_lab = Tex("SHEET JOINTS: curved, parallel to surface").scale(0.85).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(d_lab))
        self.play(Create(SurroundingRectangle(d_lab, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): exfoliation and the bornhardt
        self.next_band(5)
        b5_title = Tex("Exfoliation: peeling into roundness").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Water and heat work the curved joints;").scale(0.95).shift(band_shift(5) + UP * 1.4)
        b5_l1b = Tex("outer sheets loosen and slide off").scale(0.95).shift(band_shift(5) + UP * 0.6)
        self.play(Write(b5_l1))
        self.play(Write(b5_l1b))
        self.wait(2.5)
        b5_l2 = Tex("Curved sheets shed from curves:").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        b5_l2b = Tex("every peel leaves a ROUNDER dome").scale(0.95).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l2))
        self.play(Write(b5_l2b))
        self.play(Create(SurroundingRectangle(b5_l2b, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("Isolated giant over the plain: BORNHARDT —").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        b5_l3b = Tex("Legogote in the Lowveld; Spitzkoppe in Namibia").scale(0.9).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l3))
        self.play(Write(b5_l3b))
        self.wait(3)

        # --- Band 6 (subtopic_4): the underground stage
        self.next_band(6)
        b6_title = Tex("Tors, stage one: rot underground").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        # jointed block grid
        g1 = Rectangle(width=1.2, height=1.2, color=BLUE).shift(band_shift(6) + LEFT * 4.2 + UP * 0.6)
        g2 = Rectangle(width=1.2, height=1.2, color=BLUE).shift(band_shift(6) + LEFT * 2.9 + UP * 0.6)
        g3 = Rectangle(width=1.2, height=1.2, color=BLUE).shift(band_shift(6) + LEFT * 4.2 + DOWN * 0.7)
        g4 = Rectangle(width=1.2, height=1.2, color=BLUE).shift(band_shift(6) + LEFT * 2.9 + DOWN * 0.7)
        self.play(Create(g1), Create(g2), Create(g3), Create(g4))
        grid_lab = Tex("joints: brickwork of blocks").scale(0.8).shift(band_shift(6) + LEFT * 3.5 + DOWN * 1.8)
        self.play(Write(grid_lab))
        self.wait(2)
        # corestones as circles
        c1 = Circle(radius=0.5, color=YELLOW).shift(band_shift(6) + RIGHT * 2.6 + UP * 0.6)
        c2 = Circle(radius=0.5, color=YELLOW).shift(band_shift(6) + RIGHT * 3.9 + UP * 0.6)
        c3 = Circle(radius=0.5, color=YELLOW).shift(band_shift(6) + RIGHT * 2.6 + DOWN * 0.7)
        c4 = Circle(radius=0.5, color=YELLOW).shift(band_shift(6) + RIGHT * 3.9 + DOWN * 0.7)
        self.play(Create(c1), Create(c2), Create(c3), Create(c4))
        core_lab = Tex("corners rot first: CORESTONES in grus").scale(0.8).shift(band_shift(6) + RIGHT * 3.2 + DOWN * 1.8)
        self.play(Write(core_lab))
        self.wait(2)
        b6_l1 = Tex("Water rots blocks from every crack inward").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l1))
        self.wait(3)

        # --- Band 7 (subtopic_4): exhumation and the spacing rule
        self.next_band(7)
        b7_title = Tex("Stage two: strip and reveal").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Erosion carries off the soft grus;").scale(0.95).shift(band_shift(7) + UP * 1.4)
        b7_l1b = Tex("corestones stand stacked: a TOR").scale(0.95).shift(band_shift(7) + UP * 0.6)
        self.play(Write(b7_l1))
        self.play(Write(b7_l1b))
        self.play(Create(SurroundingRectangle(b7_l1b, color=GREEN)))
        self.wait(2.5)
        b7_l2 = Tex("Order for marks: rot FIRST, strip SECOND").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Joint spacing rules: wide $=$ dome,").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        b7_l3b = Tex("close $=$ tor — same granite, two landforms").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l3))
        self.play(Write(b7_l3b))
        self.play(Create(SurroundingRectangle(b7_l3b, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex("Lowveld and Limpopo koppies show both").scale(0.9).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the concrete that set underground
        self.next_band(8)
        b8_title = Tex("The concrete that set underground").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Full pour, no bottom: batholith").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("Ceiling jacked up: laccolith (blister)").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("Floor bowed down: lopolith — Bushveld").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Up a crack: dyke (wall); between boards: sill (shelf)").scale(0.9).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Test: lies WITH, or CUTS across?").scale(1.05).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the orange-peel mountain
        self.next_band(9)
        b9_title = Tex("The orange-peel mountain").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Backpack off: cover stripped, granite swells").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Cracks in curved shells, like orange peel").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Sun, cold and rain pry the peels off:").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        b9_l3b = Tex("exfoliation — slab after slab").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l3))
        self.play(Write(b9_l3b))
        self.wait(2.5)
        b9_l4 = Tex("Every peel leaves the dome ROUNDER —").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        b9_l4b = Tex("the mountain polishes itself").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l4))
        self.play(Write(b9_l4b))
        self.play(Create(SurroundingRectangle(b9_l4b, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): soap blocks and the stacked boulders
        self.next_band(10)
        b10_title = Tex("Soap blocks, stacked boulders").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Water in the gaps: corners melt first,").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l1b = Tex("every block rounds into a corestone").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.wait(2.5)
        b10_l2 = Tex("Strip the grus: survivors stand stacked —").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10_l2b = Tex("a tor is LEFT BEHIND, not built").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l2))
        self.play(Write(b10_l2b))
        self.play(Create(SurroundingRectangle(b10_l2b, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex("Wide joints: dome. Close joints: tor.").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        b10_l3b = Tex("Same granite — the cracks decide").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l3b))
        self.play(Create(SurroundingRectangle(b10_l3b, color=GREEN)))
        self.wait(4)
