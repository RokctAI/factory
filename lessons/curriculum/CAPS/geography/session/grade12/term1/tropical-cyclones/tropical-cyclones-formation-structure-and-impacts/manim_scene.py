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

# Band-layout whiteboard scene for the tropical-cyclones session duo.
# Content is laid out in sequential vertical bands (one frame-height each);
# nothing is ever faded out — the camera moves down to clean space instead.
# Exporter-safe vocabulary only: Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/
# VGroup. Diagrams (cross-section, rotation, satellite shapes) are hand-built
# from these primitives, element by element, in sync with the script.
#
# Subtopic time shares (subtopics.json, total 1590 s):
# 240/250/240/260 expert, 195/205/200 simplifier. Bands 0-7 cover Part 1
# (two bands per expert subtopic), bands 8-10 cover Part 2 (one fresh band
# per simplifier subtopic). Level 6 rescales times, so proportion rules.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TropicalCyclonesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the four birth conditions ---
        title = Tex("Tropical Cyclones: Birth Conditions").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        c1 = Tex(r"1. Sea $\geq 26{,}5^\circ$C, warm to 50 m deep").scale(1.1).shift(UP * 1.1)
        c2 = Tex(r"2. At least $5^\circ$ from the equator (Coriolis)").scale(1.1).shift(UP * 0.2)
        c3 = Tex(r"3. Converging trade winds (thunderstorm cluster)").scale(1.05).shift(DOWN * 0.7)
        c4 = Tex(r"4. Weak wind shear aloft").scale(1.1).shift(DOWN * 1.6)
        self.play(Write(c1))
        self.wait(2.5)
        self.play(Write(c2))
        self.wait(2.5)
        self.play(Write(c3))
        self.wait(2)
        self.play(Write(c4))
        self.wait(2)
        fuel = Tex(r"Warm ocean $\Rightarrow$ latent heat = the engine").scale(1.1).shift(DOWN * 2.7)
        self.play(Write(fuel))
        self.play(Create(SurroundingRectangle(fuel, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): names, season, rotation ---
        self.next_band(1)
        b1_t = Tex("One machine, three names").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        n1 = Tex(r"Hurricane — N Atlantic, E Pacific").scale(1.05).shift(band_shift(1) + UP * 1.2)
        n2 = Tex(r"Typhoon — NW Pacific").scale(1.05).shift(band_shift(1) + UP * 0.4)
        n3 = Tex(r"Cyclone — Indian Ocean, Australia").scale(1.05).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(n1))
        self.wait(1.5)
        self.play(Write(n2))
        self.wait(1.5)
        self.play(Write(n3))
        self.wait(2)
        # Rotation diagram: low-pressure centre with clockwise tangent arrows
        rot_c = Circle(radius=0.8, color=BLUE).shift(band_shift(1) + DOWN * 1.9 + LEFT * 3.0)
        rot_l = MathTex(r"L").scale(1.1).shift(band_shift(1) + DOWN * 1.9 + LEFT * 3.0)
        a_top = Arrow(band_shift(1) + DOWN * 1.0 + LEFT * 3.6,
                      band_shift(1) + DOWN * 1.0 + LEFT * 2.4, buff=0, color=YELLOW)
        a_bot = Arrow(band_shift(1) + DOWN * 2.8 + LEFT * 2.4,
                      band_shift(1) + DOWN * 2.8 + LEFT * 3.6, buff=0, color=YELLOW)
        rot_lab = Tex(r"SW Indian Ocean: clockwise, Nov--Apr").scale(1.05).shift(band_shift(1) + DOWN * 1.7 + RIGHT * 1.6)
        rot_lab2 = Tex(r"Named A to Z: Ana before Freddy").scale(1.0).shift(band_shift(1) + DOWN * 2.6 + RIGHT * 1.6)
        self.play(Create(rot_c), Write(rot_l))
        self.play(Create(a_top), Create(a_bot))
        self.wait(1.5)
        self.play(Write(rot_lab))
        self.wait(1.5)
        self.play(Write(rot_lab2))
        self.wait(3)

        # --- Band 2 (subtopic_2): four growth stages ---
        self.next_band(2)
        b2_t = Tex("Four stages, sorted by wind speed").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        s1 = Tex(r"1. Disturbance — thunderstorm cluster").scale(1.05).shift(band_shift(2) + UP * 1.1)
        s2 = Tex(r"2. Depression — winds $< 63$ km/h").scale(1.05).shift(band_shift(2) + UP * 0.2)
        s3 = Tex(r"3. Storm — 63--118 km/h, gets its NAME").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        s4 = Tex(r"4. Cyclone — $> 118$ km/h, eye appears").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.wait(2)
        self.play(Write(s3))
        self.wait(2)
        self.play(Write(s4))
        self.play(Create(SurroundingRectangle(s4, color=GREEN)))
        self.wait(2)
        s5 = Tex(r"Pressure can fall below 960 hPa").scale(1.05).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(s5))
        self.wait(3)

        # --- Band 3 (subtopic_2): cross-section anatomy, built outward ---
        self.next_band(3)
        b3_t = Tex("Anatomy: the exam cross-section").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        sea = Line(band_shift(3) + DOWN * 2.4 + LEFT * 5.5,
                   band_shift(3) + DOWN * 2.4 + RIGHT * 5.5, color=BLUE, stroke_width=6)
        sea_lab = Tex(r"warm ocean").scale(0.9).shift(band_shift(3) + DOWN * 2.9 + LEFT * 4.0)
        self.play(Create(sea), Write(sea_lab))
        self.wait(1.5)
        # Eye: sinking air in the centre
        eye_arrow = Arrow(band_shift(3) + UP * 1.2, band_shift(3) + DOWN * 2.0,
                          buff=0, color=YELLOW)
        eye_lab = Tex(r"EYE: sinking, calm, clear").scale(0.95).shift(band_shift(3) + UP * 1.7)
        self.play(Create(eye_arrow), Write(eye_lab))
        self.wait(2)
        # Eye wall towers either side
        wall_l = Rectangle(width=1.0, height=3.2, color=GREY).shift(band_shift(3) + DOWN * 0.8 + LEFT * 1.6)
        wall_r = Rectangle(width=1.0, height=3.2, color=GREY).shift(band_shift(3) + DOWN * 0.8 + RIGHT * 1.6)
        up_l = Arrow(band_shift(3) + DOWN * 2.2 + LEFT * 1.6,
                     band_shift(3) + UP * 0.6 + LEFT * 1.6, buff=0, color=RED)
        up_r = Arrow(band_shift(3) + DOWN * 2.2 + RIGHT * 1.6,
                     band_shift(3) + UP * 0.6 + RIGHT * 1.6, buff=0, color=RED)
        wall_lab = Tex(r"EYE WALL: strongest wind + rain").scale(0.95).shift(band_shift(3) + UP * 0.9 + RIGHT * 3.4)
        self.play(Create(wall_l), Create(wall_r))
        self.play(Create(up_l), Create(up_r))
        self.play(Write(wall_lab))
        self.wait(2)
        # Spiral rain bands further out
        band_l = Rectangle(width=0.7, height=1.8, color=GREY).shift(band_shift(3) + DOWN * 1.5 + LEFT * 3.6)
        band_r = Rectangle(width=0.7, height=1.8, color=GREY).shift(band_shift(3) + DOWN * 1.5 + RIGHT * 3.6)
        bands_lab = Tex(r"rain bands: rain in pulses").scale(0.95).shift(band_shift(3) + DOWN * 0.2 + LEFT * 3.6)
        self.play(Create(band_l), Create(band_r))
        self.play(Write(bands_lab))
        self.wait(2)
        loop = Tex(r"Condensation $\Rightarrow$ latent heat $\Rightarrow$ deeper low").scale(0.88).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(loop))
        self.wait(3)

        # --- Band 4 (subtopic_3): the weather sequence over a town ---
        self.next_band(4)
        b4_t = Tex("The storm marches over Beira").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        q1 = Tex(r"1. Swell, thickening cloud, pressure slides").scale(1.05).shift(band_shift(4) + UP * 1.1)
        q2 = Tex(r"2. Front half: squalls, blinding rain").scale(1.05).shift(band_shift(4) + UP * 0.2)
        q3 = Tex(r"3. STORM SURGE — the biggest killer").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(q1))
        self.wait(2)
        self.play(Write(q2))
        self.wait(2)
        self.play(Write(q3))
        self.play(Create(SurroundingRectangle(q3, color=GREEN)))
        self.wait(2)
        surge = Tex(r"Low pressure lifts the sea; wind drives it ashore").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(surge))
        self.wait(2.5)
        q4 = Tex(r"4. The eye: 20 min--1 h of false calm").scale(1.05).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(q4))
        self.wait(3)

        # --- Band 5 (subtopic_3): the eye trap and how the storm dies ---
        self.next_band(5)
        b5_t = Tex("The false calm — and the fuel cut").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        trap = Tex(r"``The storm is over'' — do NOT go outside").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(trap))
        self.play(Create(strike(trap)))
        self.wait(2)
        rev = Tex(r"Second eye wall: full violence, wind REVERSED").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(rev))
        self.wait(2.5)
        d_t = Tex(r"Three ways the engine starves:").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        d1 = Tex(r"landfall — no warm sea, friction slows winds").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        d2 = Tex(r"cold water poleward of $30^\circ$; strong shear").scale(1.0).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(d_t))
        self.wait(1.5)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.wait(2)
        idai = Tex(r"Dying storms still flood far inland (Idai)").scale(1.0).shift(band_shift(5) + DOWN * 3.2)
        self.play(Write(idai))
        self.wait(3)

        # --- Band 6 (subtopic_4): case study — Cyclone Freddy ---
        self.next_band(6)
        b6_t = Tex("Case study: Cyclone Freddy (2023)").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        f1 = Tex(r"Crossed the S Indian Ocean; one of the").scale(1.0).shift(band_shift(6) + UP * 1.2)
        f1b = Tex(r"longest-lived cyclones ever recorded").scale(1.0).shift(band_shift(6) + UP * 0.5)
        self.play(Write(f1))
        self.play(Write(f1b))
        self.wait(2)
        f2 = Tex(r"Madagascar $\rightarrow$ Mozambique $\rightarrow$ looped back").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        f3 = Tex(r"REFUELLED over the warm Channel, hit again").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(f2))
        self.wait(2)
        self.play(Write(f3))
        self.play(Create(SurroundingRectangle(f3, color=GREEN)))
        self.wait(2)
        f4 = Tex(r"Impacts: hundreds dead (worst in Malawi),").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        f5 = Tex(r"floods, mudslides, cholera, crops lost").scale(1.0).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(f4))
        self.wait(2)
        self.play(Write(f5))
        self.wait(3)

        # --- Band 7 (subtopic_4): satellite ID + management ---
        self.next_band(7)
        b7_t = Tex("Spot it, then manage it").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        # Tropical: tight circle with an eye (dot)
        tc = Circle(radius=1.0, color=WHITE).shift(band_shift(7) + UP * 0.5 + LEFT * 3.2)
        tc_eye = Dot(band_shift(7) + UP * 0.5 + LEFT * 3.2, color=YELLOW)
        tc_lab = Tex(r"tropical: circle + eye").scale(0.9).shift(band_shift(7) + DOWN * 0.9 + LEFT * 3.2)
        self.play(Create(tc), Create(tc_eye))
        self.play(Write(tc_lab))
        self.wait(2)
        # Mid-latitude: open comma from chained lines
        com1 = Line(band_shift(7) + UP * 1.1 + RIGHT * 2.4,
                    band_shift(7) + UP * 0.6 + RIGHT * 3.4, color=WHITE, stroke_width=5)
        com2 = Line(band_shift(7) + UP * 0.6 + RIGHT * 3.4,
                    band_shift(7) + DOWN * 0.1 + RIGHT * 3.0, color=WHITE, stroke_width=5)
        com3 = Line(band_shift(7) + DOWN * 0.1 + RIGHT * 3.0,
                    band_shift(7) + DOWN * 0.6 + RIGHT * 4.4, color=WHITE, stroke_width=5)
        com_lab = Tex(r"mid-latitude: open comma").scale(0.9).shift(band_shift(7) + DOWN * 0.9 + RIGHT * 3.4)
        self.play(Create(com1), Create(com2), Create(com3))
        self.play(Write(com_lab))
        self.wait(2)
        m1 = Tex(r"Before: warnings, codes, mangroves, drills").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        m2 = Tex(r"During: shelter high, sit out the eye").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        m3 = Tex(r"After: clean water first, rebuild stronger").scale(1.0).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(m1))
        self.wait(2)
        self.play(Write(m2))
        self.wait(2)
        self.play(Write(m3))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the pot and the spin ---
        self.next_band(8)
        b8_t = Tex("The pot, the spin and the birth rules").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        p1 = Tex(r"Warm ocean = the boiling pot").scale(1.05).shift(band_shift(8) + UP * 1.1)
        p2 = Tex(r"Vapour condenses $\Rightarrow$ latent heat = petrol").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(p1))
        self.wait(2.5)
        self.play(Write(p2))
        self.play(Create(SurroundingRectangle(p2, color=GREEN)))
        self.wait(2.5)
        p3 = Tex(r"Netball spin = Coriolis; zero on the equator").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        p4 = Tex(r"So: never born on it, never crosses it").scale(1.05).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(p3))
        self.wait(2.5)
        self.play(Write(p4))
        self.wait(2)
        p5 = Tex(r"Gentle upper winds, or the tower is knocked over").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(p5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the doughnut with the hole ---
        self.next_band(9)
        b9_t = Tex("The doughnut with the hole in the middle").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        ring_o = Circle(radius=1.5, color=GREY).shift(band_shift(9) + UP * 0.2 + LEFT * 3.4)
        ring_i = Circle(radius=0.5, color=WHITE).shift(band_shift(9) + UP * 0.2 + LEFT * 3.4)
        hole_lab = Tex(r"hole = EYE: clear, calm").scale(0.9).shift(band_shift(9) + DOWN * 1.6 + LEFT * 3.4)
        self.play(Create(ring_o), Create(ring_i))
        self.play(Write(hole_lab))
        self.wait(2)
        d1 = Tex(r"dough ring = EYE WALL: the worst place").scale(1.0).shift(band_shift(9) + UP * 0.7 + RIGHT * 2.4)
        d2 = Tex(r"arms = rain bands: squall, breather...").scale(1.0).shift(band_shift(9) + DOWN * 0.2 + RIGHT * 2.4)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.wait(2)
        trap2 = Tex(r"Blue sky mid-storm = the HOLE, not the end").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(trap2))
        self.play(Create(SurroundingRectangle(trap2, color=GREEN)))
        self.wait(2.5)
        surge2 = Tex(r"Storm surge: metres of ocean walking ashore").scale(0.95).shift(band_shift(9) + DOWN * 3.3)
        self.play(Write(surge2))
        self.wait(3)

        # --- Band 10 (subtopic_7): Freddy, the fuel gauge, being ready ---
        self.next_band(10)
        b10_t = Tex("Freddy, the fuel gauge and being ready").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        g1 = Tex(r"Warm water: gauge fills, storm strengthens").scale(1.0).shift(band_shift(10) + UP * 1.1)
        g2 = Tex(r"Land or cold sea: gauge drains, storm dies").scale(1.0).shift(band_shift(10) + UP * 0.3)
        g3 = Tex(r"Freddy found a filling station: the Channel").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(g1))
        self.wait(2)
        self.play(Write(g2))
        self.wait(2)
        self.play(Write(g3))
        self.play(Create(SurroundingRectangle(g3, color=GREEN)))
        self.wait(2.5)
        g4 = Tex(r"Pinwheel + dot: tropical. Comma + tail: mid-latitude").scale(0.95).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(g4))
        self.wait(2.5)
        g5 = Tex(r"Before: warnings, route, kit. During: stay in").scale(0.95).shift(band_shift(10) + DOWN * 2.3)
        g6 = Tex(r"After: clean water first. Disaster is partly human").scale(0.95).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(g5))
        self.wait(2.5)
        self.play(Write(g6))
        self.wait(4)
