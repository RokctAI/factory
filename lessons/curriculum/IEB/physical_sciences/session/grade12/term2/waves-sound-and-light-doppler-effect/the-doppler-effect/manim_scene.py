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

# Band-layout whiteboard scene for "The Doppler Effect"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only; wavefront pictures hand-built from
# Dot/Circle/Line/Arrow/Tex. Write-only reveals.
# Subtopic durations 235/240/240/235/190/195/195 of 1530 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DopplerEffectSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): definition + wavefront picture ---
        title = Tex("The Doppler Effect").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Change in frequency DETECTED by a listener,").scale(0.95).shift(UP * 1.3)
        b0_l2 = Tex("source and listener moving relative to the medium").scale(0.95).shift(UP * 0.5)
        self.play(Write(b0_l1))
        self.wait(1.5)
        self.play(Write(b0_l2))
        self.wait(2.5)
        # Wavefront sketch: moving source, circles offset to the right.
        c0 = DOWN * 1.6 + LEFT * 0.5
        src = Dot(c0 + RIGHT * 1.2, radius=0.1, color=YELLOW)
        w1 = Circle(radius=0.5, color=BLUE).move_to(c0 + RIGHT * 0.9)
        w2 = Circle(radius=1.0, color=BLUE).move_to(c0 + RIGHT * 0.5)
        w3 = Circle(radius=1.5, color=BLUE).move_to(c0)
        self.play(FadeIn(src))
        self.play(Create(w3), Create(w2), Create(w1))
        self.wait(2)
        b0_l3 = Tex("ahead: bunched — HIGHER $f$").scale(0.85).shift(c0 + RIGHT * 4.3 + UP * 0.4)
        b0_l4 = Tex("behind: stretched — lower $f$").scale(0.85).shift(c0 + LEFT * 4.6 + UP * 0.4)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): what changes, what does not ---
        self.next_band(1)
        b1_title = Tex("What changes, what does not").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex("source frequency: FIXED").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("speed of sound in air: FIXED ($\\sim$340 m·s$^{-1}$)").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("detected frequency: CHANGES with motion").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_wrong = Tex("Getting louder is the Doppler effect").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l4 = Tex("loudness = distance; PITCH = frequency").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the equation and its signs ---
        self.next_band(2)
        b2_eq = MathTex(r"f_L = \frac{v \pm v_L}{v \pm v_s} \, f_s").scale(1.2).shift(band_shift(2) + UP * 1.8)
        self.play(Write(b2_eq))
        self.play(Create(SurroundingRectangle(b2_eq, color=GREEN)))
        self.wait(2.5)
        b2_l1 = Tex("listener in the NUMERATOR: toward $\\Rightarrow$ add").scale(0.95).shift(band_shift(2) + UP * 0.5)
        b2_l2 = Tex("source in the DENOMINATOR: toward $\\Rightarrow$ subtract").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("approach RAISES $f_L$; recession LOWERS it —").scale(0.95).shift(band_shift(2) + DOWN * 1.5)
        b2_l4 = Tex("decide the direction first, then pick the signs").scale(0.95).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the fire engine, both sides of the pass ---
        self.next_band(3)
        b3_title = Tex("840 Hz siren, 25 m·s$^{-1}$, listener at rest").scale(1.0).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\text{approach: } f_L = \frac{340}{340 - 25} \times 840").scale(0.95).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"f_L = 906{,}67\ \text{Hz}").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{recede: } f_L = \frac{340}{340 + 25} \times 840").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        b3_l4 = MathTex(r"f_L = 782{,}47\ \text{Hz}").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l3))
        self.wait(2.5)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("the note plunges $\\sim$124 Hz; the siren never wavered").scale(0.9).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): moving listener + the reverse problem ---
        self.next_band(4)
        b4_title = Tex("Moving listener; reverse problems").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\text{car at 15 toward 600 Hz: } \frac{340 + 15}{340} \times 600 = 626{,}47\ \text{Hz}").scale(0.85).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("Hooter 750 Hz heard as 800 Hz: higher, so APPROACHING").scale(0.85).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"800 = \frac{340}{340 - v_s} \times 750").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        b4_l4 = MathTex(r"340 - v_s = 318{,}75 \Rightarrow v_s = 21{,}25\ \text{m·s}^{-1}").scale(0.95).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): ultrasound in the clinic ---
        self.next_band(5)
        b5_title = Tex("Ultrasound: speed measured by echo").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("beam $>$ 20 kHz into the body").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("reflects off moving blood cells, shifted in $f$").scale(0.95).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex("size of shift $\\Rightarrow$ speed of the blood").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex("narrowed artery: blood speeds up — the machine hears it").scale(0.9).shift(band_shift(5) + DOWN * 1.7)
        b5_l5 = Tex("foetal heartbeat: rhythmic shifts made audible").scale(0.9).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): red shift and the expanding universe ---
        self.next_band(6)
        b6_title = Tex("Red shift").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        # Spectral fingerprint: lab lines vs shifted lines.
        lab_y = band_shift(6) + UP * 0.9
        gal_y = band_shift(6) + DOWN * 0.3
        lab_lbl = Tex("laboratory:").scale(0.8).shift(lab_y + LEFT * 5.0)
        gal_lbl = Tex("galaxy:").scale(0.8).shift(gal_y + LEFT * 5.0)
        self.play(Write(lab_lbl), Write(gal_lbl))
        for dx in (0.0, 0.7, 1.8, 2.3):
            self.play(Create(Line(lab_y + LEFT * 2.5 + RIGHT * dx + UP * 0.3,
                                  lab_y + LEFT * 2.5 + RIGHT * dx + DOWN * 0.3)), run_time=0.4)
        for dx in (0.0, 0.7, 1.8, 2.3):
            self.play(Create(Line(gal_y + LEFT * 1.3 + RIGHT * dx + UP * 0.3,
                                  gal_y + LEFT * 1.3 + RIGHT * dx + DOWN * 0.3,
                                  color=RED)), run_time=0.4)
        self.wait(2)
        b6_l1 = Tex("same fingerprint, slid toward the red").scale(0.95).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex("farther galaxy $\\Rightarrow$ bigger shift $\\Rightarrow$ faster recession").scale(0.9).shift(band_shift(6) + DOWN * 2.3)
        b6_l3 = Tex("the universe is EXPANDING").scale(1.0).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the siren that lies to you ---
        self.next_band(7)
        b7_title = Tex("The siren that lies to you").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("in the cab: one steady note, all day").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("on the pavement: high wail, then a sudden sag").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("approaching: crests launched closer — bunched arrivals").scale(0.9).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = Tex("passed: crests launched farther — stretched arrivals").scale(0.9).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_rule = Tex("motion re-spaces the waves — that is Doppler").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_rule))
        self.play(Create(SurroundingRectangle(b7_rule, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): taxis every ten minutes ---
        self.next_band(8)
        b8_title = Tex("Taxis leaving every ten minutes").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("stand still: one taxi per ten minutes").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("walk toward the rank: every eight or nine").scale(0.95).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("walk away: eleven or twelve").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("rank rolling toward you: taxis packed closer on the road").scale(0.85).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_rule = Tex("schedule fixed; only the ARRIVAL rate changes").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_rule))
        self.play(Create(SurroundingRectangle(b8_rule, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): maternity ward to the whole sky ---
        self.next_band(9)
        b9_title = Tex("One effect, three sizes").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("street: the sagging siren").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("clinic: echo off moving blood — speed, no needles").scale(0.9).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("sky: fingerprints slid red — galaxies receding").scale(0.9).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("farther $\\Rightarrow$ faster: space itself is stretching").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_rule = Tex("bounce a wave off it — read the shift — know the speed").scale(0.9).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_rule))
        self.play(Create(SurroundingRectangle(b9_rule, color=GREEN)))
        self.wait(4)
