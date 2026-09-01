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
        s0_l1 = Tex("Folding, uplift or sagging TILTS strata").scale(1.1).shift(UP * 1.0)
        self.play(Write(s0_l1))
        self.wait(2)
        s0_l2 = Tex("DIP: angle between layer and horizontal").scale(1.1).shift(UP * 0.1)
        self.play(Write(s0_l2))
        self.play(Create(SurroundingRectangle(s0_l2, color=GREEN)))
        self.wait(2)
        s0_l3 = Tex("Soft layers become valleys,").scale(1.05).shift(DOWN * 0.9)
        s0_l4 = Tex("resistant layers stand as ridges —").scale(1.05).shift(DOWN * 1.7)
        s0_l5 = Tex("but the ridge is ASYMMETRICAL").scale(1.1).shift(DOWN * 2.6)
        self.play(Write(s0_l3))
        self.play(Write(s0_l4))
        self.wait(2)
        self.play(Write(s0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): dip slope vs scarp slope drawn
        self.next_band(1)
        b1_title = Tex("Dip slope follows, scarp slope cuts").scale(1.15).shift(band_shift(1) + UP * 2.6)
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
        scarp_lab = Tex("SCARP: steep, cuts layer ends").scale(0.85).shift(band_shift(1) + LEFT * 3.6 + UP * 1.5)
        dip_lab = Tex("DIP SLOPE: gentle, rides one layer").scale(0.85).shift(band_shift(1) + RIGHT * 3.4 + UP * 0.6)
        self.play(Write(scarp_lab))
        self.wait(2)
        self.play(Write(dip_lab))
        self.wait(2)
        b1_l1 = Tex("Dip slope angle $=$ dip of the rock").scale(0.95).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l1))
        self.wait(3)

        # --- Band 2 (subtopic_2): the dip dial — three ridges
        self.next_band(2)
        b2_title = Tex("One ridge, three dip angles").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Dip $< 25^\circ$: CUESTA — long gentle").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l1b = Tex("dip slope, short steep scarp").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l1b))
        self.wait(2.5)
        b2_l2 = Tex(r"$25^\circ$--$45^\circ$: HOMOCLINAL RIDGE —").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        b2_l2b = Tex("narrower, sharper: the Magaliesberg").scale(1.0).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l2))
        self.play(Write(b2_l2b))
        self.wait(2.5)
        b2_l3 = Tex(r"$> 45^\circ$: HOGSBACK — near-vertical").scale(1.0).shift(band_shift(2) + DOWN * 2.2)
        b2_l3b = Tex("layers, jagged symmetrical crest").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l3))
        self.play(Write(b2_l3b))
        self.wait(3)

        # --- Band 3 (subtopic_2): three profiles + the trend
        self.next_band(3)
        b3_title = Tex("The dial, drawn").scale(1.15).shift(band_shift(3) + UP * 2.6)
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
        b3_l1 = Tex("Steeper dip: narrower ridge, more").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        b3_l1b = Tex("equal slopes — asymmetry vanishes").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l1))
        self.play(Write(b3_l1b))
        self.play(Create(SurroundingRectangle(b3_l1b, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): cuesta basin
        self.next_band(4)
        b4_title = Tex("Cuesta basin: nested mixing bowls").scale(1.15).shift(band_shift(4) + UP * 2.6)
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
        b4_l1 = Tex("Concentric ridges ring the basin:").scale(0.95).shift(band_shift(4) + RIGHT * 3.0 + UP * 1.0)
        b4_l2 = Tex("scarps face OUT, dips face IN").scale(0.95).shift(band_shift(4) + RIGHT * 3.0 + UP * 0.2)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex("Artesian water: rain enters the rim,").scale(0.95).shift(band_shift(4) + RIGHT * 2.8 + DOWN * 0.9)
        b4_l4 = Tex("flows down-dip, pressurised at centre").scale(0.95).shift(band_shift(4) + RIGHT * 2.8 + DOWN * 1.7)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): cuesta dome and the anchor
        self.next_band(5)
        b5_title = Tex("Cuesta dome: the saucer flipped").scale(1.15).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_title))
        self.wait(1.5)
        d_out = Circle(radius=2.2, color=BLUE).shift(band_shift(5) + LEFT * 3.0 + DOWN * 0.6)
        d_in = Circle(radius=1.3, color=BLUE).shift(band_shift(5) + LEFT * 3.0 + DOWN * 0.6)
        self.play(Create(d_out), Create(d_in))
        dout = Arrow(LEFT * 4.6 + DOWN * 0.6, LEFT * 5.6 + DOWN * 0.6, color=YELLOW, buff=0).shift(band_shift(5))
        dout_lab = Tex("dips face OUT").scale(0.85).shift(band_shift(5) + LEFT * 5.0 + UP * 0.4)
        self.play(Create(dout), Write(dout_lab))
        self.wait(2)
        b5_l1 = Tex("Crest breached, core gutted:").scale(0.95).shift(band_shift(5) + RIGHT * 3.0 + UP * 1.0)
        b5_l2 = Tex("dips face OUT, scarps face IN").scale(0.95).shift(band_shift(5) + RIGHT * 3.0 + UP * 0.2)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("Vredefort Dome: impact-arched rings,").scale(0.95).shift(band_shift(5) + RIGHT * 2.8 + DOWN * 0.9)
        b5_l4 = Tex("a World Heritage Site").scale(0.95).shift(band_shift(5) + RIGHT * 2.8 + DOWN * 1.7)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Anchor: dip slope faces the way the rock dips").scale(0.9).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the two gradients
        self.next_band(6)
        b6_title = Tex("Gradient proves the asymmetry").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Crest 1\,500 m; 1\,300 m contour:").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l1b = Tex(r"400 m away north, 2\,000 m south").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l1b))
        self.wait(2.5)
        b6_l2 = MathTex(r"\text{North: } \frac{200}{400} = 1:2 \;\; \text{(scarp)}").scale(1.05).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = MathTex(r"\text{South: } \frac{200}{2\,000} = 1:10 \;\; \text{(dip)}").scale(1.05).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex("Strata dip toward the gentle side: south").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): VE and where the people go
        self.next_band(7)
        b7_title = Tex("Cross-sections and the human map").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{VE} = \frac{1/10\,000}{1/50\,000} = \frac{50\,000}{10\,000}").scale(0.99).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"= 5 \text{ times}").scale(1.1).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex("Roads and rail: strike valleys; passes").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        b7_l3b = Tex("where rivers cut poorts — Hartbeespoort").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l3))
        self.play(Write(b7_l3b))
        self.wait(2.5)
        b7_l4 = Tex("Dip slopes: farms; scarp faces: wild").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the file that slipped over
        self.next_band(8)
        b8_title = Tex("The file that slipped over").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Book under one end: the file tilts —").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("the pages' new angle is the dip").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Top cover: long smooth ramp — dip slope").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex("High end, cut page edges — scarp slope").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("``Dip follows, scarp cuts''").scale(1.1).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2)
        b8_l6 = Tex("Cardboard pages survive as the ridges").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): the dial from ramp to hedgehog
        self.next_band(9)
        b9_title = Tex("Turning the dial to hedgehog").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Soft tilt ($<25^\circ$): cuesta —").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l1b = Tex("wheelchair ramp with a cliff behind").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l1b))
        self.wait(2.5)
        b9_l2 = Tex(r"Middle tilt ($25$--$45^\circ$): homoclinal —").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        b9_l2b = Tex("scramble, not cycle: the Magaliesberg").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l2))
        self.play(Write(b9_l2b))
        self.wait(2.5)
        b9_l3 = Tex(r"Past $45^\circ$: hogsback — the ramp is").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        b9_l3b = Tex("gone, both sides steep, spiky crest").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l3))
        self.play(Write(b9_l3b))
        self.play(Create(SurroundingRectangle(b9_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): soup bowls, blisters, roads
        self.next_band(10)
        b10_title = Tex("Soup bowls, blisters, roads").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Nested bowls $=$ basin: dips IN,").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l1b = Tex("scarps OUT — artesian water below").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.wait(2.5)
        b10_l2 = Tex("Blister pile $=$ dome: dips OUT,").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        b10_l2b = Tex("scarps IN — the Vredefort rings").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l2))
        self.play(Write(b10_l2b))
        self.wait(2.5)
        b10_l3 = Tex("Map: one crowded side $=$ cuesta;").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        b10_l3b = Tex("towns in valleys, traffic through poorts").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l3b))
        self.play(Create(SurroundingRectangle(b10_l3b, color=GREEN)))
        self.wait(4)
