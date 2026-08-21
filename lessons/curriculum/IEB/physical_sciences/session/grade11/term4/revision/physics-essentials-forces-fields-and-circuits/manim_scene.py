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

# Band-layout whiteboard scene for the physics revision session duo
# (forces, fields and circuits). Covers all seven subtopics (Part 1 Expert:
# 1-4, Part 2 Simplifier: 5-7), band time proportional to subtopics.json
# (245/250/250/250/200/195/195 of 1585 s). Add-only lifecycle; free-body
# diagram and circuit hand-built from Dot/Arrow/Line/Rectangle/Tex
# (exporter-safe primitives only).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PhysicsEssentialsRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(15)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the five steps and the three laws ---
        title = Tex("The Free-Body Method").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("1. Free-body diagram \\; 2. Choose positive").scale(0.95).shift(UP * 1.2)
        b0_l2 = Tex(r"3. Components: $F_x = F\cos\theta$, $F_y = F\sin\theta$").scale(0.95).shift(UP * 0.4)
        b0_l3 = Tex(r"4. $F_{net} = ma$ per axis \\; 5. Solve + units").scale(0.95).shift(DOWN * 0.4)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Law 1: inertia. Law 2: $F_{net} = ma$.").scale(1.0).shift(DOWN * 1.4)
        b0_l5 = Tex("Law 3: equal, opposite, DIFFERENT objects").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the trolley, free body drawn ---
        self.next_band(1)
        b1_t = Tex("8 kg trolley: 60 N pull, 12 N friction").scale(1.1).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_t))
        self.wait(2)
        # free-body diagram: dot + four labelled arrows
        c = band_shift(1) + LEFT * 3.0 + DOWN * 0.3
        dot = Dot(c, radius=0.12)
        self.play(Create(dot))
        a_up = Arrow(c, c + UP * 1.5, buff=0, color=BLUE)
        l_up = MathTex(r"N").scale(0.9).next_to(a_up, UP, buff=0.1)
        a_dn = Arrow(c, c + DOWN * 1.5, buff=0, color=BLUE)
        l_dn = MathTex(r"w").scale(0.9).next_to(a_dn, DOWN, buff=0.1)
        a_rt = Arrow(c, c + RIGHT * 2.2, buff=0, color=YELLOW)
        l_rt = MathTex(r"60 \text{ N}").scale(0.85).next_to(a_rt, RIGHT, buff=0.1)
        a_lf = Arrow(c, c + LEFT * 1.1, buff=0, color=RED)
        l_lf = MathTex(r"12 \text{ N}").scale(0.85).next_to(a_lf, LEFT, buff=0.1)
        self.play(Create(a_up), Write(l_up))
        self.play(Create(a_dn), Write(l_dn))
        self.wait(1.5)
        self.play(Create(a_rt), Write(l_rt))
        self.play(Create(a_lf), Write(l_lf))
        self.wait(2)
        b1_l1 = MathTex(r"F_{net} = 60 - 12 = 48 \text{ N}").scale(1.0).shift(band_shift(1) + RIGHT * 3.4 + UP * 0.4)
        b1_l2 = MathTex(r"a = \frac{48}{8} = 6 \text{ m/s}^2").scale(1.0).shift(band_shift(1) + RIGHT * 3.4 + DOWN * 0.8)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = Tex("Only forces ON the trolley enter its diagram").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l3))
        self.wait(3)

        # --- Band 2 (subtopic_2): the inverse-square twins ---
        self.next_band(2)
        b2_t = Tex("The inverse-square twins").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_f1 = MathTex(r"F = \frac{Gm_1m_2}{r^2}, \; G = 6{,}67 \times 10^{-11}").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_f2 = MathTex(r"F = \frac{kQ_1Q_2}{r^2}, \; k = 9 \times 10^{9}").scale(1.0).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_f1))
        self.wait(2)
        self.play(Write(b2_f2))
        self.wait(2)
        b2_l1 = Tex("Double $r$: quarter force. Triple: a ninth").scale(1.0).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = Tex("Gravity only attracts; charge has two signs").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l2))
        self.wait(3)

        # --- Band 3 (subtopic_2): Coulomb worked; mass vs weight ---
        self.next_band(3)
        b3_t = Tex(r"4 $\mu$C and 5 $\mu$C, 0{,}2 m apart").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = MathTex(r"F = \frac{9 \times 10^9 \times 4 \times 10^{-6} \times 5 \times 10^{-6}}{(0{,}2)^2}").scale(0.95).shift(band_shift(3) + UP * 1.0)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"F = \frac{0{,}18}{0{,}04} = 4{,}5 \text{ N, repulsive}").scale(1.0).shift(band_shift(3) + DOWN * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = MathTex(r"w = mg: \; 196 \text{ N at surface}").scale(1.0).shift(band_shift(3) + DOWN * 1.4)
        b3_l4 = Tex(r"Two Earth-radii up: $r$ triples, $g$ ninths —").scale(0.95).shift(band_shift(3) + DOWN * 2.3)
        b3_l5 = Tex(r"21{,}8 N. Mass never changed; weight did").scale(0.95).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(1.5)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the network, drawn and collapsed ---
        self.next_band(4)
        b4_t = Tex(r"24 V: 2 $\Omega$ + (6 $\Omega \parallel$ 3 $\Omega$)").scale(1.0).shift(band_shift(4) + UP * 2.8)
        self.play(Write(b4_t))
        self.wait(2)
        # circuit sketch: battery loop, series resistor, parallel pair
        o = band_shift(4) + DOWN * 0.6
        wire_top = Line(o + LEFT * 4 + UP * 1.6, o + RIGHT * 4 + UP * 1.6)
        wire_bot = Line(o + LEFT * 4 + DOWN * 1.6, o + RIGHT * 4 + DOWN * 1.6)
        wire_lf = Line(o + LEFT * 4 + UP * 1.6, o + LEFT * 4 + DOWN * 1.6)
        bat = Tex("24 V").scale(0.8).next_to(wire_lf, LEFT, buff=0.15)
        self.play(Create(wire_top), Create(wire_bot), Create(wire_lf), Write(bat))
        r_ser = Rectangle(width=1.2, height=0.5).move_to(o + UP * 1.6 + LEFT * 1.0)
        l_ser = Tex(r"2 $\Omega$").scale(0.7).next_to(r_ser, UP, buff=0.1)
        self.play(Create(r_ser), Write(l_ser))
        wire_r1 = Line(o + RIGHT * 4 + UP * 1.6, o + RIGHT * 4 + DOWN * 1.6)
        r_b1 = Rectangle(width=0.5, height=1.0).move_to(o + RIGHT * 2.6)
        l_b1 = Tex(r"6 $\Omega$").scale(0.7).next_to(r_b1, LEFT, buff=0.1)
        wire_b1a = Line(o + RIGHT * 2.6 + UP * 1.6, o + RIGHT * 2.6 + UP * 0.5)
        wire_b1b = Line(o + RIGHT * 2.6 + DOWN * 0.5, o + RIGHT * 2.6 + DOWN * 1.6)
        r_b2 = Rectangle(width=0.5, height=1.0).move_to(o + RIGHT * 4.0)
        l_b2 = Tex(r"3 $\Omega$").scale(0.7).next_to(r_b2, RIGHT, buff=0.1)
        self.play(Create(wire_r1), Create(wire_b1a), Create(r_b1), Write(l_b1), Create(wire_b1b))
        self.play(Create(r_b2), Write(l_b2))
        self.wait(2)
        b4_l1 = MathTex(r"R_p = \frac{18}{9} = 2, \quad R_{tot} = 4 \; \Omega").scale(0.95).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): solve, expand, audit ---
        self.next_band(5)
        b5_t = Tex("Solve the loop, expand back, audit").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = MathTex(r"I = \frac{V}{R} = \frac{24}{4} = 6 \text{ A}").scale(1.05).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"V_{2\Omega} = 6 \times 2 = 12 \text{ V}; \; 12 \text{ V left for the pair}").scale(0.95).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"I_6 = 2 \text{ A}, \quad I_3 = 4 \text{ A}").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"2 + 4 = 6 \text{ A} \; \checkmark").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = MathTex(r"P: \; 72 + 24 + 48 = 144 = 24 \times 6 \; \checkmark").scale(0.95).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): field and flux ---
        self.next_band(6)
        b6_t = Tex("Currents make fields; fields count as flux").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("Right-hand rule: thumb = current,").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("curled fingers = circular field lines").scale(1.0).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.wait(1.5)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_f = MathTex(r"\phi = BA\cos\theta \quad \text{(weber)}").scale(1.1).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_f))
        self.play(Create(SurroundingRectangle(b6_f, color=GREEN)))
        self.wait(2.5)
        b6_l3 = MathTex(r"\phi = 0{,}4 \times 0{,}05 = 0{,}02 \text{ Wb square-on}").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        b6_l4 = Tex("Edge-on: zero — nothing threads through").scale(0.95).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): Faraday and Lenz ---
        self.next_band(7)
        b7_t = Tex("Faraday: CHANGING flux makes emf").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_f = MathTex(r"\varepsilon = \frac{N\,\Delta\phi}{\Delta t}").scale(1.15).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_f))
        self.wait(2)
        b7_l1 = MathTex(r"\varepsilon = \frac{200 \times 0{,}02}{0{,}5} = 8 \text{ V}").scale(1.05).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(2.5)
        b7_l2 = Tex("Halve the pull time: 16 V — speed is everything").scale(0.95).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Lenz: the induced current OPPOSES").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        b7_l4 = Tex("the change — energy conservation demands it").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l3))
        self.wait(1.5)
        self.play(Write(b7_l4))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): springs and spray ---
        self.next_band(8)
        b8_t = Tex("Invisible springs and the thinning spray").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Every force is a two-ended spring:").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("Earth pulls phone; phone pulls Earth — equally").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.wait(1.5)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Sprinkler: double distance, four times").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        b8_l4 = Tex("the area, quarter the soaking").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l3))
        self.wait(1.5)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex("Field map: N per kg, or N per C, at every point").scale(0.95).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the delivery network ---
        self.next_band(9)
        b9_t = Tex("The delivery network").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Depot = battery; cargo/coulomb = emf;").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("traffic = current; stops = resistors").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Series: one route — same current, shares add").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        b9_l4 = Tex("Parallel: side streets — full load each,").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        b9_l5 = Tex("currents add, total always below smallest").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(1.5)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = MathTex(r"144 = 72 + 24 + 48 \; \checkmark \text{ ledger closed}").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the trap museum ---
        self.next_band(10)
        b10_t = Tex("The trap museum").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("1. Weight in kilograms").scale(0.95).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1))
        self.play(Create(strike(b10_l1)))
        self.wait(1.5)
        b10_l2 = Tex("2. The unsquared distance").scale(0.95).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l2))
        self.play(Create(strike(b10_l2)))
        self.wait(1.5)
        b10_l3 = Tex("3. The missed prefix ($\\mu$, n)").scale(0.95).shift(band_shift(10) + DOWN * 0.3)
        self.play(Write(b10_l3))
        self.play(Create(strike(b10_l3)))
        self.wait(1.5)
        b10_l4 = Tex("4. Series/parallel formulas swapped").scale(0.95).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l4))
        self.play(Create(strike(b10_l4)))
        self.wait(1.5)
        b10_l5 = Tex("5. Emf claimed from a steady flux").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l5))
        self.play(Create(strike(b10_l5)))
        self.wait(2)
        b10_l6 = Tex("Every answer sealed by its own audit").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
