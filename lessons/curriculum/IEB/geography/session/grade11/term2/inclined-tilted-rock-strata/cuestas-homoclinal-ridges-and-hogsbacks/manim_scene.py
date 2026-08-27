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
# "Cuestas, Homoclinal Ridges and Hogsbacks" (inclined/tilted rock strata).
# One band per teaching beat; the camera moves down, nothing is removed.
# Diagrams hand-built from Line/Arrow/Dot/Circle/Rectangle/Tex only.
# Subtopic shares follow subtopics.json: 215/230/230/240/180/190/210 of 1495 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CuestasHomoclinalHogsbacksSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): tilted strata and dip
        title = Tex("Cuestas, Homoclinal Ridges, Hogsbacks").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("Crustal forces LEAN the flat strata").scale(1.1).shift(UP * 1.0)
        self.play(Write(s0_l1))
        self.wait(2)
        s0_l2 = Tex("DIP: the layer's angle with horizontal").scale(1.1).shift(UP * 0.1)
        self.play(Write(s0_l2))
        self.play(Create(SurroundingRectangle(s0_l2, color=GREEN)))
        self.wait(2)
        s0_l3 = Tex("Weak layers hollowed into valleys,").scale(1.05).shift(DOWN * 0.9)
        s0_l4 = Tex("resistant layers stand as ridges —").scale(1.05).shift(DOWN * 1.7)
        s0_l5 = Tex("and every such ridge is LOPSIDED").scale(1.1).shift(DOWN * 2.6)
        self.play(Write(s0_l3))
        self.play(Write(s0_l4))
        self.wait(2)
        self.play(Write(s0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): dip slope vs scarp slope drawn
        self.next_band(1)
        b1_title = Tex("Dip follows one layer, scarp cuts many").scale(1.1).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        base1 = Line(LEFT * 6.0 + DOWN * 1.8, RIGHT * 6.0 + DOWN * 1.8, color=WHITE).shift(band_shift(1))
        self.play(Create(base1))
        # tilted layers: three parallel inclined lines
        lay1 = Line(LEFT * 4.6 + DOWN * 1.8, RIGHT * 0.2 + UP * 1.2, color=BLUE).shift(band_shift(1))
        lay2 = Line(LEFT * 3.2 + DOWN * 1.8, RIGHT * 1.2 + UP * 0.9, color=BLUE).shift(band_shift(1))
        lay3 = Line(LEFT * 1.8 + DOWN * 1.8, RIGHT * 2.0 + UP * 0.5, color=BLUE).shift(band_shift(1))
        self.play(Create(lay1), Create(lay2), Create(lay3))
        self.wait(1.5)
        # ridge profile: gentle dip slope right, steep scarp left
        scarp = Line(LEFT * 1.0 + DOWN * 1.8, RIGHT * 0.2 + UP * 1.2, color=RED).shift(band_shift(1))
        dip = Line(RIGHT * 0.2 + UP * 1.2, RIGHT * 5.6 + DOWN * 1.8, color=YELLOW).shift(band_shift(1))
        self.play(Create(scarp))
        self.play(Create(dip))
        scarp_lab = Tex("SCARP: cut edge of the stack").scale(0.85).shift(band_shift(1) + LEFT * 3.6 + UP * 1.5)
        dip_lab = Tex("DIP SLOPE: one layer's surface").scale(0.85).shift(band_shift(1) + RIGHT * 3.4 + UP * 0.6)
        self.play(Write(scarp_lab))
        self.wait(2)
        self.play(Write(dip_lab))
        self.wait(2)
        b1_l1 = Tex("Dip slope angle $=$ dip of the strata").scale(0.95).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l1))
        self.wait(3)

        # --- Band 2 (subtopic_2): the lean-angle scale — three ridges
        self.next_band(2)
        b2_title = Tex("One ridge, three lean angles").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Dip $< 25^\circ$: CUESTA — long easy").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l1b = Tex("ramp, short steep scarp: Soutpansberg flanks").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l1b))
        self.wait(2.5)
        b2_l2 = Tex(r"$25^\circ$--$45^\circ$: HOMOCLINAL RIDGE —").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        b2_l2b = Tex("sharper, narrower: the Magaliesberg").scale(1.0).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l2))
        self.play(Write(b2_l2b))
        self.wait(2.5)
        b2_l3 = Tex(r"$> 45^\circ$: HOGSBACK — layers upended,").scale(1.0).shift(band_shift(2) + DOWN * 2.2)
        b2_l3b = Tex("thin jagged near-symmetrical blade").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l3))
        self.play(Write(b2_l3b))
        self.wait(3)

        # --- Band 3 (subtopic_2): three profiles + the trend
        self.next_band(3)
        b3_title = Tex("The scale, drawn").scale(1.15).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        base3 = Line(LEFT * 6.0 + DOWN * 1.2, RIGHT * 6.0 + DOWN * 1.2, color=WHITE).shift(band_shift(3))
        self.play(Create(base3))
        # cuesta: long ramp, short cliff
        cu = VGroup(
            Line(LEFT * 5.6 + DOWN * 1.2, LEFT * 3.4 + UP * 0.2, color=YELLOW),
            Line(LEFT * 3.4 + UP * 0.2, LEFT * 3.0 + DOWN * 1.2, color=RED),
        ).shift(band_shift(3))
        cu_lab = Tex("cuesta").scale(0.8).shift(band_shift(3) + LEFT * 4.3 + UP * 0.8)
        self.play(Create(cu[0]), Create(cu[1]), Write(cu_lab))
        self.wait(2)
        # homoclinal: steeper both, still asymmetric
        ho = VGroup(
            Line(LEFT * 1.6 + DOWN * 1.2, LEFT * 0.4 + UP * 0.6, color=YELLOW),
            Line(LEFT * 0.4 + UP * 0.6, RIGHT * 0.2 + DOWN * 1.2, color=RED),
        ).shift(band_shift(3))
        ho_lab = Tex("homoclinal").scale(0.8).shift(band_shift(3) + LEFT * 0.6 + UP * 1.2)
        self.play(Create(ho[0]), Create(ho[1]), Write(ho_lab))
        self.wait(2)
        # hogsback: symmetric spike
        hg = VGroup(
            Line(RIGHT * 2.6 + DOWN * 1.2, RIGHT * 3.4 + UP * 0.9, color=RED),
            Line(RIGHT * 3.4 + UP * 0.9, RIGHT * 4.2 + DOWN * 1.2, color=RED),
        ).shift(band_shift(3))
        hg_lab = Tex("hogsback").scale(0.8).shift(band_shift(3) + RIGHT * 3.4 + UP * 1.4)
        self.play(Create(hg[0]), Create(hg[1]), Write(hg_lab))
        self.wait(2)
        b3_l1 = Tex("Steeper lean: narrower ridge, faces").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        b3_l1b = Tex("more equal — the lopsidedness vanishes").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l1))
        self.play(Write(b3_l1b))
        self.play(Create(SurroundingRectangle(b3_l1b, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): cuesta basin
        self.next_band(4)
        b4_title = Tex("Cuesta basin: the satellite dish").scale(1.15).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        ring_out = Circle(radius=2.2, color=BLUE).shift(band_shift(4) + LEFT * 3.0 + DOWN * 0.6)
        ring_in = Circle(radius=1.3, color=BLUE).shift(band_shift(4) + LEFT * 3.0 + DOWN * 0.6)
        centre = Dot(LEFT * 3.0 + DOWN * 0.6).shift(band_shift(4))
        self.play(Create(ring_out), Create(ring_in), Create(centre))
        self.wait(1.5)
        din = Arrow(LEFT * 5.6 + DOWN * 0.6, LEFT * 4.6 + DOWN * 0.6, color=YELLOW, buff=0).shift(band_shift(4))
        din_lab = Tex("dips face IN").scale(0.85).shift(band_shift(4) + LEFT * 5.0 + UP * 0.4)
        self.play(Create(din), Write(din_lab))
        self.wait(2)
        b4_l1 = Tex("Concentric resistant rings:").scale(0.95).shift(band_shift(4) + RIGHT * 3.0 + UP * 1.0)
        b4_l2 = Tex("dips face IN, scarps face OUT").scale(0.95).shift(band_shift(4) + RIGHT * 3.0 + UP * 0.2)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex("Artesian water: rim rain runs down-dip,").scale(0.95).shift(band_shift(4) + RIGHT * 2.8 + DOWN * 0.9)
        b4_l4 = Tex("sits pressurised under the centre").scale(0.95).shift(band_shift(4) + RIGHT * 2.8 + DOWN * 1.7)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): cuesta dome and the anchor
        self.next_band(5)
        b5_title = Tex("Cuesta dome: the umbrella").scale(1.15).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_title))
        self.wait(1.5)
        d_out = Circle(radius=2.2, color=BLUE).shift(band_shift(5) + LEFT * 3.0 + DOWN * 0.6)
        d_in = Circle(radius=1.3, color=BLUE).shift(band_shift(5) + LEFT * 3.0 + DOWN * 0.6)
        self.play(Create(d_out), Create(d_in))
        dout = Arrow(LEFT * 4.6 + DOWN * 0.6, LEFT * 5.6 + DOWN * 0.6, color=YELLOW, buff=0).shift(band_shift(5))
        dout_lab = Tex("dips face OUT").scale(0.85).shift(band_shift(5) + LEFT * 5.0 + UP * 0.4)
        self.play(Create(dout), Write(dout_lab))
        self.wait(2)
        b5_l1 = Tex("Crown breached, core gutted:").scale(0.95).shift(band_shift(5) + RIGHT * 3.0 + UP * 1.0)
        b5_l2 = Tex("dips face OUT, scarps face IN").scale(0.95).shift(band_shift(5) + RIGHT * 3.0 + UP * 0.2)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("Vredefort Dome: impact-arched strata,").scale(0.95).shift(band_shift(5) + RIGHT * 2.8 + DOWN * 0.9)
        b5_l4 = Tex("rings you can trace from space").scale(0.95).shift(band_shift(5) + RIGHT * 2.8 + DOWN * 1.7)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Anchor: the dip slope faces where the layers lean down").scale(0.85).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the two gradients
        self.next_band(6)
        b6_title = Tex("Two gradients prove the dip").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Crest 900 m; 750 m contour:").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l1b = Tex(r"300 m away east, 3\,000 m west").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l1b))
        self.wait(2.5)
        b6_l2 = MathTex(r"\text{East: } \frac{150}{300} = 1:2 \;\; \text{(scarp)}").scale(1.05).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = MathTex(r"\text{West: } \frac{150}{3\,000} = 1:20 \;\; \text{(dip)}").scale(1.05).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex("Strata dip toward the gentle side: west").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): VE and where the people go
        self.next_band(7)
        b7_title = Tex("Cross-sections and the human map").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{VE} = \frac{1/5\,000}{1/50\,000} = \frac{50\,000}{5\,000}").scale(0.99).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"= 10 \text{ times}").scale(1.1).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex("Towns and rail: strike valleys; crossings").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        b7_l3b = Tex("where rivers saw poorts — Olifantsnek").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l3))
        self.play(Write(b7_l3b))
        self.wait(2.5)
        b7_l4 = Tex("Dip slopes farmed; scarp faces left wild").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the tilted sandwich
        self.next_band(8)
        b8_title = Tex("The tilted sandwich").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Matchbox under one end: the lean").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("of the sandwich is the dip").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Top slice: smooth ramp — dip slope").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex("Cut end, layered edges — scarp slope").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("``Dip follows, scarp cuts''").scale(1.1).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2)
        b8_l6 = Tex("Biltong layers survive as the ridges").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): three clicks of the car jack
        self.next_band(9)
        b9_title = Tex("Three clicks of the car jack").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Click 1 ($<25^\circ$): cuesta —").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l1b = Tex("wheelbarrow ramp, short steep cut end").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l1b))
        self.wait(2.5)
        b9_l2 = Tex(r"Click 2 ($25$--$45^\circ$): homoclinal —").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        b9_l2b = Tex("hands-and-knees ramp: the Magaliesberg").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l2))
        self.play(Write(b9_l2b))
        self.wait(2.5)
        b9_l3 = Tex(r"Click 3 ($>45^\circ$): hogsback — ramp").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        b9_l3b = Tex("gone, both faces steep, blade crest").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l3))
        self.play(Write(b9_l3b))
        self.play(Create(SurroundingRectangle(b9_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): dishes, umbrellas, the gap
        self.next_band(10)
        b10_title = Tex("Dishes, umbrellas, the gap").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Satellite dish $=$ basin: dips IN,").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l1b = Tex("scarps OUT — artesian water beneath").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.wait(2.5)
        b10_l2 = Tex("Umbrella $=$ dome: dips OUT,").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        b10_l2b = Tex("scarps IN — the Vredefort rings").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l2))
        self.play(Write(b10_l2b))
        self.wait(2.5)
        b10_l3 = Tex("Map: one crowded side $=$ lopsided ridge;").scale(0.9).shift(band_shift(10) + DOWN * 2.2)
        b10_l3b = Tex("towns in valleys, crossings through poorts").scale(0.9).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l3b))
        self.play(Create(SurroundingRectangle(b10_l3b, color=GREEN)))
        self.wait(4)
