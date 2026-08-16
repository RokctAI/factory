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

# Band-layout whiteboard scene for "Kalahari High, ITCZ and Africa's
# Climate" (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier 5-7).
# Exporter-safe primitives only: convergence/subsidence cells are straight
# Arrows, the ITCZ migration is a labelled rail of Lines and Dots, and the
# Kalahari High inversion is a hand-built escarpment cross-section of Line
# segments. Add-only lifecycle; camera moves down band by band. Band time
# apportioned to subtopics.json (215/230/240/240/180/185/210 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class KalahariHighITCZSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the rain switch, drawn ---
        title = Tex("Africa's Rain Switch").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        # convergence cell (left): arrows in, air up
        conv_lab = Tex("CONVERGENCE").scale(0.9).shift(LEFT * 3.4 + UP * 1.4)
        self.play(Write(conv_lab))
        cin1 = Arrow(LEFT * 5.6 + DOWN * 1.6, LEFT * 4.0 + DOWN * 1.6, buff=0, color=BLUE, stroke_width=5)
        cin2 = Arrow(LEFT * 1.2 + DOWN * 1.6, LEFT * 2.8 + DOWN * 1.6, buff=0, color=BLUE, stroke_width=5)
        cup = Arrow(LEFT * 3.4 + DOWN * 1.4, LEFT * 3.4 + UP * 0.8, buff=0, color=BLUE, stroke_width=6)
        self.play(Create(cin1), Create(cin2))
        self.play(Create(cup))
        c_txt = Tex("rises, cools, rains").scale(0.8).shift(LEFT * 3.4 + DOWN * 2.4)
        self.play(Write(c_txt))
        self.wait(2)
        # subsidence cell (right): air down, arrows out
        sub_lab = Tex("SUBSIDENCE").scale(0.9).shift(RIGHT * 3.4 + UP * 1.4)
        self.play(Write(sub_lab))
        sdown = Arrow(RIGHT * 3.4 + UP * 0.8, RIGHT * 3.4 + DOWN * 1.4, buff=0, color=RED, stroke_width=6)
        sout1 = Arrow(RIGHT * 2.8 + DOWN * 1.6, RIGHT * 1.2 + DOWN * 1.6, buff=0, color=RED, stroke_width=5)
        sout2 = Arrow(RIGHT * 4.0 + DOWN * 1.6, RIGHT * 5.6 + DOWN * 1.6, buff=0, color=RED, stroke_width=5)
        self.play(Create(sdown))
        self.play(Create(sout1), Create(sout2))
        s_txt = Tex("sinks, warms, dries").scale(0.8).shift(RIGHT * 3.4 + DOWN * 2.4)
        self.play(Write(s_txt))
        self.wait(2)
        sw = Tex("Wet or dry = is the air rising or sinking?").scale(0.95).shift(DOWN * 3.2)
        self.play(Write(sw))
        self.play(Create(SurroundingRectangle(sw, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the inversion lid and the belts ---
        self.next_band(1)
        b1_title = Tex("The inversion is a lid").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        i1 = Tex("Subsidence builds a layer where temperature").scale(0.95).shift(band_shift(1) + UP * 1.2)
        i2 = Tex("RISES with height — thermals stop dead").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(i1))
        self.play(Write(i2))
        self.wait(2.5)
        i3 = Tex("Equator: permanent convergence — Congo wet").scale(0.95).shift(band_shift(1) + DOWN * 0.6)
        i4 = Tex("Near $30^\\circ$N and S: permanent subsidence —").scale(0.95).shift(band_shift(1) + DOWN * 1.4)
        i5 = Tex("Sahara, Kalahari, Namib deserts").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(i3))
        self.wait(2)
        self.play(Write(i4))
        self.play(Write(i5))
        self.wait(2)
        i6 = Tex("In between: rain only when the rising side visits").scale(0.9).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(i6))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the migrating ITCZ ---
        self.next_band(2)
        b2_title = Tex("The ITCZ: the rain belt that migrates").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        d1 = Tex("Where SE trades meet NE trades: massive uplift").scale(0.9).shift(band_shift(2) + UP * 1.6)
        self.play(Write(d1))
        self.wait(2)
        # north-south rail with equator and the two seasonal positions
        rail = Line(band_shift(2) + LEFT * 0.6 + UP * 1.0, band_shift(2) + LEFT * 0.6 + DOWN * 2.6, stroke_width=4)
        eq = Line(band_shift(2) + LEFT * 3.2 + DOWN * 0.8, band_shift(2) + RIGHT * 2.0 + DOWN * 0.8,
                  color=GREY, stroke_width=3)
        eq_lab = Tex("equator").scale(0.7).shift(band_shift(2) + RIGHT * 3.0 + DOWN * 0.8)
        self.play(Create(rail), Create(eq), Write(eq_lab))
        july = Dot(band_shift(2) + LEFT * 0.6 + UP * 0.6, color=RED)
        july_lab = Tex("July: Sahel ($15$--$20^\\circ$N)").scale(0.75).shift(band_shift(2) + RIGHT * 2.6 + UP * 0.6)
        jan = Dot(band_shift(2) + LEFT * 0.6 + DOWN * 2.2, color=BLUE)
        jan_lab = Tex("January: Angola--Zimbabwe").scale(0.75).shift(band_shift(2) + RIGHT * 2.8 + DOWN * 2.2)
        self.play(FadeIn(july), Write(july_lab))
        self.play(FadeIn(jan), Write(jan_lab))
        self.wait(2)
        m1 = Tex("Follows the overhead sun, a month behind").scale(0.9).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex("Crossed twice a year = double maximum (Congo);").scale(0.85).shift(band_shift(2) + DOWN * 3.8)
        self.play(Write(m2))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): the Kalahari High and the escarpment ---
        self.next_band(3)
        b3_title = Tex("The Kalahari High, breathing").scale(1.15).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_title))
        self.wait(1.5)
        # escarpment cross-section: sea (right) up to plateau (left)
        sea = band_shift(3) + RIGHT * 5.0 + DOWN * 2.2
        foot = band_shift(3) + RIGHT * 2.0 + DOWN * 2.0
        crest = band_shift(3) + RIGHT * 0.2 + DOWN * 0.2
        plateau_end = band_shift(3) + LEFT * 5.2 + DOWN * 0.1
        self.play(Create(Line(sea, foot, stroke_width=5)),
                  Create(Line(foot, crest, stroke_width=5)),
                  Create(Line(crest, plateau_end, stroke_width=5)))
        sea_lab = Tex("Indian Ocean").scale(0.7).shift(sea + UP * 0.4 + LEFT * 0.3)
        pla_lab = Tex("plateau").scale(0.7).shift(band_shift(3) + LEFT * 3.6 + UP * 0.5)
        self.play(Write(sea_lab), Write(pla_lab))
        self.wait(1.5)
        winter = Line(band_shift(3) + LEFT * 5.2 + DOWN * 1.2, band_shift(3) + RIGHT * 5.0 + DOWN * 1.2,
                      color=RED, stroke_width=4)
        w_lab = Tex("winter inversion BELOW the crest: dry, clear").scale(0.8).shift(band_shift(3) + DOWN * 3.0)
        self.play(Create(winter), Write(w_lab))
        self.wait(2.5)
        summer = Line(band_shift(3) + LEFT * 5.2 + UP * 1.3, band_shift(3) + RIGHT * 5.0 + UP * 1.3,
                      color=BLUE, stroke_width=4)
        s_lab = Tex("summer inversion lifts ABOVE: moist air floods in,").scale(0.8).shift(band_shift(3) + UP * 1.9)
        s_lab2 = Tex("afternoon thunderstorms on the Highveld").scale(0.8).shift(band_shift(3) + DOWN * 3.7)
        self.play(Create(summer), Write(s_lab))
        self.play(Write(s_lab2))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): two coasts, two currents ---
        self.next_band(4)
        b4_title = Tex("Opposite currents, opposite coasts").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        west = Rectangle(width=5.6, height=2.6).shift(band_shift(4) + LEFT * 3.1 + UP * 0.5)
        w1 = Tex("West: cold Benguela").scale(0.85).shift(band_shift(4) + LEFT * 3.1 + UP * 1.2)
        w2 = Tex("chilled, stable air:").scale(0.8).shift(band_shift(4) + LEFT * 3.1 + UP * 0.5)
        w3 = Tex("fog, no rain — Namib").scale(0.8).shift(band_shift(4) + LEFT * 3.1 + DOWN * 0.2)
        self.play(Create(west), Write(w1))
        self.play(Write(w2), Write(w3))
        self.wait(2)
        east = Rectangle(width=5.6, height=2.6).shift(band_shift(4) + RIGHT * 3.1 + UP * 0.5)
        e1 = Tex("East: warm Mozambique--").scale(0.85).shift(band_shift(4) + RIGHT * 3.1 + UP * 1.2)
        e2 = Tex("Agulhas — unstable moist").scale(0.8).shift(band_shift(4) + RIGHT * 3.1 + UP * 0.5)
        e3 = Tex("air: green Durban").scale(0.8).shift(band_shift(4) + RIGHT * 3.1 + DOWN * 0.2)
        self.play(Create(east), Write(e1))
        self.play(Write(e2), Write(e3))
        self.wait(2)
        b4_l1 = Tex("Port Nolloth and Durban: same latitude,").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        b4_l2 = Tex("opposite currents, opposite climates").scale(0.95).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): reading the synoptic chart ---
        self.next_band(5)
        b5_title = Tex("Reading the synoptic chart").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        y1 = Tex("Isobars every 4 hPa; H = subsidence, clear;").scale(0.9).shift(band_shift(5) + UP * 1.2)
        y2 = Tex("L = uplift, rain; tight spacing = wind").scale(0.9).shift(band_shift(5) + UP * 0.4)
        self.play(Write(y1))
        self.play(Write(y2))
        self.wait(2.5)
        y3 = Tex("Cold front: triangles point where it moves —").scale(0.9).shift(band_shift(5) + DOWN * 0.5)
        y4 = Tex("rain, wind shift, temperature drop behind it").scale(0.9).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(y3))
        self.play(Write(y4))
        self.wait(2.5)
        y5 = Tex("Station model: temp upper left, dew point lower").scale(0.85).shift(band_shift(5) + DOWN * 2.2)
        y6 = Tex("left, shaded circle, feathers = 10 knots each").scale(0.85).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(y5))
        self.play(Write(y6))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): satellites and El Nino ---
        self.next_band(6)
        b6_title = Tex("Satellites, GIS and El Ni\\~no").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        z1 = Tex("On the image: ITCZ = band of storm cloud,").scale(0.9).shift(band_shift(6) + UP * 1.2)
        z2 = Tex("front = curved bar, Kalahari = clear eye").scale(0.9).shift(band_shift(6) + UP * 0.4)
        self.play(Write(z1))
        self.play(Write(z2))
        self.wait(2.5)
        z3 = Tex("GIS layers rain, dams, vegetation: drought").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        z4 = Tex("watched district by district").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(z3))
        self.play(Write(z4))
        self.wait(2)
        z5 = Tex("El Ni\\~no: warm Pacific, our summers dry (2015-16)").scale(0.9).shift(band_shift(6) + DOWN * 2.2)
        z6 = Tex("La Ni\\~na: cool Pacific, wet summers (2021-22)").scale(0.9).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(z5))
        self.wait(2)
        self.play(Write(z6))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the lid and the chimney ---
        self.next_band(7)
        b7_title = Tex("The lid and the chimney").scale(1.2).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        p1 = Tex("Lid OFF = convergence: steam towers, rain").scale(0.95).shift(band_shift(7) + UP * 1.3)
        p2 = Tex("Lid ON = subsidence: nothing rises, nothing rains").scale(0.9).shift(band_shift(7) + UP * 0.5)
        self.play(Write(p1))
        self.wait(2)
        self.play(Write(p2))
        self.wait(2.5)
        p3 = Tex("Burner at the equator: Congo chimney;").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        p4 = Tex("lids near $30^\\circ$: Sahara, Kalahari, Namib").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(p3))
        self.play(Write(p4))
        self.wait(2.5)
        p5 = Tex("The lid's exam name: temperature inversion —").scale(0.9).shift(band_shift(7) + DOWN * 2.1)
        p6 = Tex("warm above cold, thermals stop dead").scale(0.9).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(p5))
        self.play(Write(p6))
        self.play(Create(SurroundingRectangle(p6, color=GREEN)))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): the sprinkler on the rail ---
        self.next_band(8)
        b8_title = Tex("The sprinkler that follows the sun").scale(1.1).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        q1 = Tex("The ITCZ slides on a north-south rail,").scale(0.95).shift(band_shift(8) + UP * 1.3)
        q2 = Tex("chasing the overhead sun a month behind").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(q1))
        self.play(Write(q2))
        self.wait(2.5)
        q3 = Tex("January: hosing Angola--Zimbabwe (our summer)").scale(0.9).shift(band_shift(8) + DOWN * 0.4)
        q4 = Tex("July: watering the Sahel, we wait in the dry").scale(0.9).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(q3))
        self.wait(2)
        self.play(Write(q4))
        self.wait(2.5)
        q5 = Tex("Passes twice (Congo) = two rainy seasons;").scale(0.9).shift(band_shift(8) + DOWN * 2.1)
        q6 = Tex("barely once (Sahel) = one — or a drought").scale(0.9).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(q5))
        self.play(Write(q6))
        self.play(Create(SurroundingRectangle(q6, color=GREEN)))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): two buckets and a weather map ---
        self.next_band(9)
        b9_title = Tex("Two buckets and a weather map").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        t1 = Tex("Warm bucket east (Agulhas): steamy air, rain;").scale(0.9).shift(band_shift(9) + UP * 1.3)
        t2 = Tex("cold bucket west (Benguela): fog at best").scale(0.9).shift(band_shift(9) + UP * 0.5)
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(2.5)
        t3 = Tex("Kalahari High = lid on a hinge: clamped in").scale(0.9).shift(band_shift(9) + DOWN * 0.4)
        t4 = Tex("winter, lifted in summer — storms return").scale(0.9).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(t3))
        self.play(Write(t4))
        self.wait(2.5)
        t5 = Tex("Map symbols: H = lid, L = chimney, packed lines").scale(0.85).shift(band_shift(9) + DOWN * 2.1)
        t6 = Tex("= wind, triangles = cold front on the march").scale(0.85).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(t5))
        self.play(Write(t6))
        self.play(Create(SurroundingRectangle(t6, color=GREEN)))
        self.wait(3)
