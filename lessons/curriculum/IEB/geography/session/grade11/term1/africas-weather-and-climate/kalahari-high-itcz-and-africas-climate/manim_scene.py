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
# "Kalahari High, ITCZ and Africa's Climate". One band per teaching beat; the
# camera moves down to fresh space and nothing is ever removed. Diagrams are
# hand-built from Line/Arrow/Dot/Circle/Tex only (exporter-safe).
# Subtopic time shares follow subtopics.json:
# 215/230/240/240/180/185/210 of 1500 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class KalahariHighITCZSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the rain switch, drawn ---
        title = Tex("Kalahari High, ITCZ and Africa's Climate").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        ground = Line(LEFT * 5.2 + DOWN * 1.6, RIGHT * 5.2 + DOWN * 1.6, color=WHITE)
        self.play(Create(ground))
        # convergence: two arrows meet, one rises
        c_in1 = Arrow(LEFT * 5.0 + DOWN * 1.3, LEFT * 3.6 + DOWN * 1.3, color=YELLOW, buff=0)
        c_in2 = Arrow(LEFT * 2.2 + DOWN * 1.3, LEFT * 3.6 + DOWN * 1.3, color=YELLOW, buff=0)
        c_up = Arrow(LEFT * 3.6 + DOWN * 1.1, LEFT * 3.6 + UP * 1.2, color=YELLOW, buff=0)
        c_lab = Tex("CONVERGENCE: up, cloud, rain").scale(0.85).shift(LEFT * 3.2 + UP * 1.8)
        self.play(Create(c_in1), Create(c_in2))
        self.play(Create(c_up))
        self.play(Write(c_lab))
        self.wait(2.5)
        # subsidence: one sinks, two diverge
        s_dn = Arrow(RIGHT * 3.6 + UP * 1.2, RIGHT * 3.6 + DOWN * 1.1, color=BLUE, buff=0)
        s_o1 = Arrow(RIGHT * 3.6 + DOWN * 1.3, RIGHT * 2.2 + DOWN * 1.3, color=BLUE, buff=0)
        s_o2 = Arrow(RIGHT * 3.6 + DOWN * 1.3, RIGHT * 5.0 + DOWN * 1.3, color=BLUE, buff=0)
        s_lab = Tex("SUBSIDENCE: down, dry, clear").scale(0.85).shift(RIGHT * 3.2 + UP * 1.8)
        self.play(Create(s_dn))
        self.play(Create(s_o1), Create(s_o2))
        self.play(Write(s_lab))
        self.wait(2.5)
        q = Tex("One question: rising or sinking?").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(q))
        self.play(Create(SurroundingRectangle(q, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the inversion ceiling and the belts ---
        self.next_band(1)
        b1_title = Tex("The inversion is a ceiling").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        inv = Line(LEFT * 4.5 + UP * 0.8, RIGHT * 4.5 + UP * 0.8, color=RED).shift(band_shift(1))
        inv_lab = Tex("warm layer aloft: thermals stop here").scale(0.85).shift(band_shift(1) + UP * 1.4)
        th = Arrow(DOWN * 1.6, UP * 0.6, color=YELLOW, buff=0).shift(band_shift(1) + LEFT * 2.0)
        self.play(Create(inv), Write(inv_lab))
        self.play(Create(th))
        self.wait(2.5)
        b1_l1 = Tex("Equator: permanent convergence — wet").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        b1_l2 = Tex(r"$30^\circ$ N and S: permanent subsidence —").scale(0.95).shift(band_shift(1) + DOWN * 1.7)
        b1_l3 = Tex("Sahara, Kalahari, Namib").scale(0.95).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the migrating ITCZ ---
        self.next_band(2)
        b2_title = Tex("The ITCZ migrates with the sun").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        # north-south rail with two stops
        rail = Line(UP * 1.6, DOWN * 1.8, color=WHITE).shift(band_shift(2) + LEFT * 4.2)
        stop_n = Dot(LEFT * 4.2 + UP * 1.2).shift(band_shift(2))
        stop_s = Dot(LEFT * 4.2 + DOWN * 1.4).shift(band_shift(2))
        lab_n = Tex(r"July: Sahel, $15$--$20^\circ$N").scale(0.9).shift(band_shift(2) + LEFT * 1.4 + UP * 1.2)
        lab_s = Tex("January: Angola--Zambia--Zimbabwe").scale(0.9).shift(band_shift(2) + RIGHT * 0.2 + DOWN * 1.4)
        self.play(Create(rail))
        self.play(Create(stop_n), Write(lab_n))
        self.wait(2)
        self.play(Create(stop_s), Write(lab_s))
        self.wait(2)
        b2_l1 = Tex("Lags the overhead sun by about a month").scale(0.95).shift(band_shift(2) + UP * 0.2 + RIGHT * 0.6)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("Middle: crossed twice — double maximum").scale(0.95).shift(band_shift(2) + DOWN * 2.3)
        b2_l3 = Tex("Ends: crossed once — single maximum").scale(0.95).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): the Kalahari High and the escarpment ---
        self.next_band(3)
        b3_title = Tex("The Kalahari High breathes").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        # plateau profile with escarpment edge
        prof = VGroup(
            Line(LEFT * 5.0 + UP * 0.2, LEFT * 0.5 + UP * 0.2, color=WHITE),
            Line(LEFT * 0.5 + UP * 0.2, RIGHT * 1.5 + DOWN * 1.6, color=WHITE),
            Line(RIGHT * 1.5 + DOWN * 1.6, RIGHT * 5.0 + DOWN * 1.6, color=WHITE),
        ).shift(band_shift(3))
        self.play(Create(prof[0]), Create(prof[1]), Create(prof[2]))
        winter_inv = Line(LEFT * 5.0 + DOWN * 0.5, RIGHT * 5.0 + DOWN * 0.5, color=RED).shift(band_shift(3))
        w_lab = Tex("winter: inversion BELOW the crest — dry").scale(0.85).shift(band_shift(3) + RIGHT * 0.6 + DOWN * 2.3)
        self.play(Create(winter_inv), Write(w_lab))
        self.wait(2.5)
        summer_inv = Line(LEFT * 5.0 + UP * 1.5, RIGHT * 5.0 + UP * 1.5, color=YELLOW).shift(band_shift(3))
        s_lab3 = Tex("summer: inversion ABOVE — moisture floods in").scale(0.85).shift(band_shift(3) + UP * 2.0 + RIGHT * 0.4)
        moist = Arrow(RIGHT * 4.6 + DOWN * 1.2, LEFT * 0.2 + UP * 0.6, color=BLUE, buff=0).shift(band_shift(3))
        self.play(Create(summer_inv), Write(s_lab3))
        self.play(Create(moist))
        self.wait(2.5)
        b3_l1 = Tex("One valve: dry winters, stormy summers").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l1))
        self.wait(3)

        # --- Band 4 (subtopic_3): two coasts, two currents ---
        self.next_band(4)
        b4_title = Tex("Two coasts, two currents").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        west = Arrow(LEFT * 3.5 + DOWN * 1.8, LEFT * 3.5 + UP * 1.0, color=BLUE, buff=0).shift(band_shift(4))
        w_lab4 = Tex("Benguela: cold, stable air — fog only").scale(0.9).shift(band_shift(4) + LEFT * 2.6 + DOWN * 2.4)
        east = Arrow(RIGHT * 3.5 + UP * 1.0, RIGHT * 3.5 + DOWN * 1.8, color=RED, buff=0).shift(band_shift(4))
        e_lab4 = Tex("Mozambique-Agulhas: warm, unstable — rain").scale(0.85).shift(band_shift(4) + RIGHT * 2.2 + DOWN * 2.4)
        self.play(Create(west), Write(w_lab4))
        self.wait(2.5)
        self.play(Create(east), Write(e_lab4))
        self.wait(2.5)
        b4_l1 = Tex("Alexander Bay: desert. Richards Bay: green.").scale(0.95).shift(band_shift(4) + UP * 0.2)
        b4_l2 = Tex("Nearly the same latitude — the current decides").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): reading the synoptic chart ---
        self.next_band(5)
        b5_title = Tex("Reading the synoptic chart").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Isobars every 4 hPa; H settled, L rain").scale(0.95).shift(band_shift(5) + UP * 1.3)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Cold front: triangles point where it goes").scale(0.95).shift(band_shift(5) + UP * 0.5)
        # front line with two triangles suggested by line pairs
        fr = Line(LEFT * 4.0 + DOWN * 0.6, RIGHT * 0.5 + DOWN * 1.4, color=BLUE).shift(band_shift(5))
        t1 = VGroup(
            Line(LEFT * 3.0 + DOWN * 0.8, LEFT * 2.6 + DOWN * 0.4, color=BLUE),
            Line(LEFT * 2.6 + DOWN * 0.4, LEFT * 2.2 + DOWN * 0.95, color=BLUE),
        ).shift(band_shift(5))
        self.play(Write(b5_l2))
        self.play(Create(fr), Create(t1[0]), Create(t1[1]))
        self.wait(2.5)
        b5_l3 = Tex("Station: temp top left, dew point below,").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        b5_l4 = Tex("cloud in the circle, wind FROM the shaft").scale(0.9).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): satellites and El Nino ---
        self.next_band(6)
        b6_title = Tex("Satellites and El Ni\\~no").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("ITCZ: band of storm cloud on the image").scale(0.95).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("Front: long curved cloud bar").scale(0.95).shift(band_shift(6) + UP * 0.5)
        b6_l3 = Tex("Subsidence: cloud-free void inland").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("GIS layers: rain, dams, vegetation").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("El Ni\\~no 2023-24: seared midsummer").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        b6_l6 = Tex("La Ni\\~na: usually generous summers").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.wait(2)
        self.play(Write(b6_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the duvet and the hot-air balloon ---
        self.next_band(7)
        b7_title = Tex("The duvet and the hot-air balloon").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        balloon = Circle(radius=0.7, color=YELLOW).shift(band_shift(7) + LEFT * 3.2 + UP * 0.8)
        b_up = Arrow(LEFT * 3.2 + DOWN * 1.2, LEFT * 3.2 + UP * 0.0, color=YELLOW, buff=0).shift(band_shift(7))
        b_lab = Tex("balloon: converge, rise, rain").scale(0.85).shift(band_shift(7) + LEFT * 3.0 + DOWN * 1.8)
        self.play(Create(balloon), Create(b_up))
        self.play(Write(b_lab))
        self.wait(2.5)
        duvet = Line(RIGHT * 1.6 + UP * 1.0, RIGHT * 4.8 + UP * 1.0, color=BLUE).shift(band_shift(7))
        d_dn = Arrow(RIGHT * 3.2 + UP * 0.8, RIGHT * 3.2 + DOWN * 0.8, color=BLUE, buff=0).shift(band_shift(7))
        d_lab = Tex("duvet: sink, press, no rain").scale(0.85).shift(band_shift(7) + RIGHT * 3.0 + DOWN * 1.8)
        self.play(Create(duvet), Create(d_dn))
        self.play(Write(d_lab))
        self.wait(2.5)
        b7_l1 = Tex("Smoke flattening sideways = the ceiling").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the water truck on its route ---
        self.next_band(8)
        b8_title = Tex("The water truck on its route").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        route = Line(UP * 1.5, DOWN * 1.9, color=WHITE).shift(band_shift(8) + LEFT * 4.0)
        truck = Dot(LEFT * 4.0 + DOWN * 1.2).shift(band_shift(8))
        self.play(Create(route), Create(truck))
        b8_l1 = Tex("January: parked south — our rains").scale(0.95).shift(band_shift(8) + RIGHT * 0.6 + UP * 1.0)
        b8_l2 = Tex("July: parked north — Sahel rains").scale(0.95).shift(band_shift(8) + RIGHT * 0.6 + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Middle of the route: watered twice").scale(0.95).shift(band_shift(8) + DOWN * 1.0 + RIGHT * 0.4)
        b8_l4 = Tex("Ends of the route: watered once").scale(0.95).shift(band_shift(8) + DOWN * 1.8 + RIGHT * 0.4)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("A late truck = a failed harvest").scale(1.0).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): two pots and the weather map ---
        self.next_band(9)
        b9_title = Tex("Two pots and the weather map").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        pot_w = Circle(radius=0.55, color=RED).shift(band_shift(9) + LEFT * 3.4 + UP * 0.9)
        pw_lab = Tex("simmering: east coast rain").scale(0.85).shift(band_shift(9) + LEFT * 3.2 + UP * 0.0)
        pot_c = Circle(radius=0.55, color=BLUE).shift(band_shift(9) + RIGHT * 3.4 + UP * 0.9)
        pc_lab = Tex("iced: west coast fog").scale(0.85).shift(band_shift(9) + RIGHT * 3.3 + UP * 0.0)
        self.play(Create(pot_w), Write(pw_lab))
        self.wait(2)
        self.play(Create(pot_c), Write(pc_lab))
        self.wait(2)
        b9_l1 = Tex("Escarpment gate: bolted in winter,").scale(0.95).shift(band_shift(9) + DOWN * 1.0)
        b9_l2 = Tex("lifted in summer — storms return").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("H duvet, L balloon, triangles = front,").scale(0.95).shift(band_shift(9) + DOWN * 2.6)
        b9_l4 = Tex("feathers fly FROM the wind").scale(0.95).shift(band_shift(9) + DOWN * 3.4)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(4)
