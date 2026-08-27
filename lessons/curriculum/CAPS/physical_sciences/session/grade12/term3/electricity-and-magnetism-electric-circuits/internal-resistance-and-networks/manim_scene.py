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

# Band-layout whiteboard scene for the session duo "Internal Resistance and
# Networks" (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier subtopics 5-7).
# Only exporter-safe mobjects (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/
# SurroundingRectangle/VGroup), write-only reveals, camera moves between bands.
# Band dwell time follows subtopics.json (235/240/240/235/190/195/195 of 1530).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class InternalResistanceNetworksSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the two rules of combination
        title = Tex("Internal Resistance and Networks").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_s = Tex("Series: one path, same current").scale(1.1).shift(UP * 1.2)
        b0_f1 = MathTex(r"R_s = R_1 + R_2 + R_3").scale(1.2).shift(UP * 0.3)
        self.play(Write(b0_s))
        self.wait(1.5)
        self.play(Write(b0_f1))
        self.wait(2.5)
        b0_p = Tex("Parallel: same voltage, currents add").scale(1.1).shift(DOWN * 0.7)
        b0_f2 = MathTex(r"\frac{1}{R_p} = \frac{1}{R_1} + \frac{1}{R_2}").scale(1.15).shift(DOWN * 1.7)
        self.play(Write(b0_p))
        self.wait(1.5)
        self.play(Write(b0_f2))
        self.wait(2.5)
        b0_rule = Tex(r"Parallel pair $<$ smallest branch").scale(1.1).shift(DOWN * 2.8)
        self.play(Write(b0_rule))
        self.wait(3)

        # --- Band 1 (subtopic_1): collapse a network — 6 // 3 in series with 4
        self.next_band(1)
        b1_title = Tex("Collapse: parallel first, then series").scale(1.15).shift(band_shift(1) + UP * 2.8)
        self.play(Write(b1_title))
        self.wait(1.5)
        # hand-built network diagram: dot - wire - 4-ohm - node - two branches - node - dot
        nA = Dot(band_shift(1) + LEFT * 4.4 + UP * 1.2)
        w1 = Line(band_shift(1) + LEFT * 4.4 + UP * 1.2, band_shift(1) + LEFT * 3.4 + UP * 1.2)
        r4 = Rectangle(width=1.2, height=0.5).shift(band_shift(1) + LEFT * 2.8 + UP * 1.2)
        r4_lab = MathTex(r"4\ \Omega").scale(0.9).shift(band_shift(1) + LEFT * 2.8 + UP * 1.9)
        w2 = Line(band_shift(1) + LEFT * 2.2 + UP * 1.2, band_shift(1) + LEFT * 1.2 + UP * 1.2)
        self.play(Create(nA), Create(w1), Create(r4), Write(r4_lab), Create(w2))
        self.wait(1.5)
        v1 = Line(band_shift(1) + LEFT * 1.2 + UP * 1.7, band_shift(1) + LEFT * 1.2 + UP * 0.7)
        top_w = Line(band_shift(1) + LEFT * 1.2 + UP * 1.7, band_shift(1) + RIGHT * 1.2 + UP * 1.7)
        r6 = Rectangle(width=1.2, height=0.45).shift(band_shift(1) + UP * 1.7)
        r6_lab = MathTex(r"6\ \Omega").scale(0.9).shift(band_shift(1) + UP * 2.25)
        bot_w = Line(band_shift(1) + LEFT * 1.2 + UP * 0.7, band_shift(1) + RIGHT * 1.2 + UP * 0.7)
        r3 = Rectangle(width=1.2, height=0.45).shift(band_shift(1) + UP * 0.7)
        r3_lab = MathTex(r"3\ \Omega").scale(0.9).shift(band_shift(1) + UP * 0.15)
        v2 = Line(band_shift(1) + RIGHT * 1.2 + UP * 1.7, band_shift(1) + RIGHT * 1.2 + UP * 0.7)
        w3 = Line(band_shift(1) + RIGHT * 1.2 + UP * 1.2, band_shift(1) + RIGHT * 2.4 + UP * 1.2)
        nB = Dot(band_shift(1) + RIGHT * 2.4 + UP * 1.2)
        self.play(Create(v1), Create(top_w), Create(r6), Write(r6_lab))
        self.play(Create(bot_w), Create(r3), Write(r3_lab), Create(v2), Create(w3), Create(nB))
        self.wait(2)
        b1_l1 = MathTex(r"R_p = \frac{6 \times 3}{6 + 3} = \frac{18}{9} = 2\ \Omega").scale(1.1).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex(r"Check: 2 $\Omega < 3\ \Omega$, as parallel demands").scale(1.05).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"R_{ext} = 4 + 2 = 6\ \Omega").scale(1.15).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): emf, internal resistance, the master equation
        self.next_band(2)
        b2_title = Tex("EMF and Internal Resistance").scale(1.2).shift(band_shift(2) + UP * 2.8)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"$\varepsilon$: energy per coulomb — the full budget").scale(1.05).shift(band_shift(2) + UP * 1.8)
        b2_l2 = Tex(r"$r$: a small resistor hidden inside the cell").scale(1.05).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_eq = MathTex(r"\varepsilon = IR_{ext} + Ir").scale(1.3).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_eq))
        self.play(Create(SurroundingRectangle(b2_eq, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex(r"$IR_{ext}$: terminal voltage (outside share)").scale(1.05).shift(band_shift(2) + DOWN * 1.1)
        b2_l4 = Tex(r"$Ir$: lost volts — heat inside the battery").scale(1.05).shift(band_shift(2) + DOWN * 1.9)
        b2_l5 = Tex(r"Switch open: $I = 0$, voltmeter reads $\varepsilon$").scale(1.05).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): worked budget — 12 V, r = 0,5, R = 5,5
        self.next_band(3)
        b3_title = Tex(r"$\varepsilon = 12$ V, $r = 0{,}5\ \Omega$, $R = 5{,}5\ \Omega$").scale(1.0).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"R_{tot} = 5{,}5 + 0{,}5 = 6\ \Omega").scale(1.1).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"I = \frac{12}{6} = 2\ \text{A}").scale(1.1).shift(band_shift(3) + UP * 0.1)
        b3_l3 = MathTex(r"V_{term} = 2 \times 5{,}5 = 11\ \text{V}").scale(1.1).shift(band_shift(3) + DOWN * 0.9)
        b3_l4 = MathTex(r"\text{Lost volts} = 2 \times 0{,}5 = 1\ \text{V}").scale(1.1).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = MathTex(r"\text{Check: } 11 + 1 = 12 = \varepsilon").scale(1.1).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): full circuit — draw it, collapse the outside
        self.next_band(4)
        b4_title = Tex(r"Full circuit: $\varepsilon = 24$ V, $r = 1\ \Omega$").scale(1.15).shift(band_shift(4) + UP * 3.0)
        self.play(Write(b4_title))
        self.wait(1.5)
        # battery on the left (vertical branch), 5 ohm on top wire, 6//3 pair on right
        bat = Rectangle(width=0.7, height=0.9).shift(band_shift(4) + LEFT * 4.2 + UP * 0.55)
        bat_lab = MathTex(r"\varepsilon,\ r").scale(0.85).shift(band_shift(4) + LEFT * 5.2 + UP * 0.55)
        wl1 = Line(band_shift(4) + LEFT * 4.2 + UP * 1.0, band_shift(4) + LEFT * 4.2 + UP * 1.5)
        wt1 = Line(band_shift(4) + LEFT * 4.2 + UP * 1.5, band_shift(4) + LEFT * 2.6 + UP * 1.5)
        r5 = Rectangle(width=1.2, height=0.5).shift(band_shift(4) + LEFT * 2.0 + UP * 1.5)
        r5_lab = MathTex(r"5\ \Omega").scale(0.85).shift(band_shift(4) + LEFT * 2.0 + UP * 2.15)
        wt2 = Line(band_shift(4) + LEFT * 1.4 + UP * 1.5, band_shift(4) + RIGHT * 0.2 + UP * 1.5)
        self.play(Create(bat), Write(bat_lab), Create(wl1), Create(wt1))
        self.play(Create(r5), Write(r5_lab), Create(wt2))
        self.wait(1.5)
        vv1 = Line(band_shift(4) + RIGHT * 0.2 + UP * 1.9, band_shift(4) + RIGHT * 0.2 + UP * 1.1)
        br_t = Line(band_shift(4) + RIGHT * 0.2 + UP * 1.9, band_shift(4) + RIGHT * 2.4 + UP * 1.9)
        r6b = Rectangle(width=1.1, height=0.42).shift(band_shift(4) + RIGHT * 1.3 + UP * 1.9)
        r6b_lab = MathTex(r"6\ \Omega").scale(0.8).shift(band_shift(4) + RIGHT * 1.3 + UP * 2.4)
        br_b = Line(band_shift(4) + RIGHT * 0.2 + UP * 1.1, band_shift(4) + RIGHT * 2.4 + UP * 1.1)
        r3b = Rectangle(width=1.1, height=0.42).shift(band_shift(4) + RIGHT * 1.3 + UP * 1.1)
        r3b_lab = MathTex(r"3\ \Omega").scale(0.8).shift(band_shift(4) + RIGHT * 1.3 + UP * 0.6)
        vv2 = Line(band_shift(4) + RIGHT * 2.4 + UP * 1.9, band_shift(4) + RIGHT * 2.4 + UP * 1.1)
        wdn = Line(band_shift(4) + RIGHT * 2.4 + UP * 1.5, band_shift(4) + RIGHT * 3.6 + UP * 1.5)
        wr = Line(band_shift(4) + RIGHT * 3.6 + UP * 1.5, band_shift(4) + RIGHT * 3.6 + DOWN * 0.3)
        wb = Line(band_shift(4) + RIGHT * 3.6 + DOWN * 0.3, band_shift(4) + LEFT * 4.2 + DOWN * 0.3)
        wl2 = Line(band_shift(4) + LEFT * 4.2 + DOWN * 0.3, band_shift(4) + LEFT * 4.2 + UP * 0.1)
        self.play(Create(vv1), Create(br_t), Create(r6b), Write(r6b_lab))
        self.play(Create(br_b), Create(r3b), Write(r3b_lab), Create(vv2))
        self.play(Create(wdn), Create(wr), Create(wb), Create(wl2))
        self.wait(2)
        b4_l1 = Tex(r"Step 1 — collapse the outside:").scale(1.05).shift(band_shift(4) + DOWN * 1.0)
        b4_l2 = MathTex(r"R_p = \frac{6 \times 3}{6 + 3} = 2\ \Omega").scale(1.1).shift(band_shift(4) + DOWN * 1.9)
        b4_l3 = MathTex(r"R_{ext} = 5 + 2 = 7\ \Omega").scale(1.1).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l1))
        self.wait(1.5)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): solve the loop, walk back in, audit
        self.next_band(5)
        b5_title = Tex("Steps 2 and 3: loop, then walk back in").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"I = \frac{24}{7 + 1} = \frac{24}{8} = 3\ \text{A}").scale(1.1).shift(band_shift(5) + UP * 1.2)
        b5_l2 = MathTex(r"V_{term} = 24 - 3 \times 1 = 21\ \text{V}").scale(1.1).shift(band_shift(5) + UP * 0.3)
        b5_l3 = MathTex(r"V_5 = 3 \times 5 = 15\ \text{V}").scale(1.1).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = MathTex(r"V_p = 21 - 15 = 6\ \text{V}").scale(1.1).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = MathTex(r"I_6 = \frac{6}{6} = 1\ \text{A}, \quad I_3 = \frac{6}{3} = 2\ \text{A}").scale(1.0).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2)
        b5_chk = Tex(r"Audit: $1 + 2 = 3$ A, the main current").scale(1.05).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_chk))
        self.wait(3)

        # --- Band 6 (subtopic_4): the V-I graph reads the battery
        self.next_band(6)
        b6_title = Tex(r"The graph: $V_{term} = \varepsilon - Ir$").scale(1.15).shift(band_shift(6) + UP * 2.6)
        self.play(Write(b6_title))
        self.wait(2)
        ax_y = Arrow(band_shift(6) + LEFT * 3.0 + DOWN * 1.8, band_shift(6) + LEFT * 3.0 + UP * 1.9, buff=0)
        ax_x = Arrow(band_shift(6) + LEFT * 3.0 + DOWN * 1.8, band_shift(6) + RIGHT * 2.8 + DOWN * 1.8, buff=0)
        y_lab = Tex("V (V)").scale(0.9).shift(band_shift(6) + LEFT * 3.9 + UP * 1.6)
        x_lab = Tex("I (A)").scale(0.9).shift(band_shift(6) + RIGHT * 3.4 + DOWN * 2.1)
        self.play(Create(ax_y), Create(ax_x), Write(y_lab), Write(x_lab))
        self.wait(1.5)
        vline = Line(band_shift(6) + LEFT * 3.0 + UP * 1.3, band_shift(6) + RIGHT * 2.2 + DOWN * 1.3, color=BLUE)
        emf_dot = Dot(band_shift(6) + LEFT * 3.0 + UP * 1.3, color=YELLOW)
        emf_lab = MathTex(r"\varepsilon").scale(1.0).shift(band_shift(6) + LEFT * 3.5 + UP * 1.3)
        self.play(Create(vline))
        self.play(Create(emf_dot), Write(emf_lab))
        self.wait(2)
        grad_lab = Tex(r"gradient $= -r$").scale(1.0).shift(band_shift(6) + RIGHT * 0.9 + UP * 0.7)
        self.play(Write(grad_lab))
        self.wait(2)
        b6_l1 = Tex(r"Intercept reads $\varepsilon$; slope reads $r$").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l1))
        self.wait(3)

        # --- Band 7 (subtopic_4): loading and power
        self.next_band(7)
        b7_title = Tex("Loading and power").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"More parallel bulbs: $R_{ext}\downarrow$, $I\uparrow$,").scale(1.05).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"$Ir\uparrow$, so $V_{term}$ DROPS — bulbs dim").scale(1.05).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"P = VI = I^2R = \frac{V^2}{R}").scale(1.15).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"P_5 = I^2R = 9 \times 5 = 45\ \text{W}").scale(1.1).shift(band_shift(7) + DOWN * 1.6)
        b7_l5 = MathTex(r"P_r = 9 \times 1 = 9\ \text{W (internal heat)}").scale(1.05).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the battery charges a toll
        self.next_band(8)
        b8_title = Tex("The battery charges a toll").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Promise ($\varepsilon$) $-$ toll ($Ir$) $=$ delivery").scale(1.1).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex(r"No current, no toll: idle battery reads 12 V").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Big current, big toll: less push gets out").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Old torch: full promise, huge toll, dim glow").scale(1.05).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = MathTex(r"V_{term} = \varepsilon - Ir").scale(1.2).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): one river, many channels
        self.next_band(9)
        b9_title = Tex("One river, many channels").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Series = rapids on one river: difficulty adds").scale(1.05).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Parallel = extra channels: journey gets EASIER").scale(1.05).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2.5)
        # tiny river sketch: main line splitting into two channels
        rv_in = Line(band_shift(9) + LEFT * 3.6 + DOWN * 0.8, band_shift(9) + LEFT * 1.6 + DOWN * 0.8)
        rv_t = Line(band_shift(9) + LEFT * 1.6 + DOWN * 0.8, band_shift(9) + LEFT * 0.2 + DOWN * 0.3)
        rv_b = Line(band_shift(9) + LEFT * 1.6 + DOWN * 0.8, band_shift(9) + LEFT * 0.2 + DOWN * 1.3)
        rv_t2 = Line(band_shift(9) + LEFT * 0.2 + DOWN * 0.3, band_shift(9) + RIGHT * 1.2 + DOWN * 0.8)
        rv_b2 = Line(band_shift(9) + LEFT * 0.2 + DOWN * 1.3, band_shift(9) + RIGHT * 1.2 + DOWN * 0.8)
        rv_out = Line(band_shift(9) + RIGHT * 1.2 + DOWN * 0.8, band_shift(9) + RIGHT * 3.2 + DOWN * 0.8)
        self.play(Create(rv_in), Create(rv_t), Create(rv_b))
        self.play(Create(rv_t2), Create(rv_b2), Create(rv_out))
        self.wait(2)
        b9_l3 = Tex("Series shares the PUSH; parallel shares the FLOW").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Same current in series, same voltage in parallel").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the night the headlights dimmed
        self.next_band(10)
        b10_title = Tex("The night the headlights dimmed").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        c1 = Tex("1. Starter joins: new parallel branch").scale(1.05).shift(band_shift(10) + UP * 1.2)
        c2 = Tex(r"2. $R_{ext}$ falls $\Rightarrow$ total current rises").scale(1.05).shift(band_shift(10) + UP * 0.3)
        c3 = Tex(r"3. Toll $Ir$ rises with the current").scale(1.05).shift(band_shift(10) + DOWN * 0.6)
        c4 = Tex(r"4. $V_{term}$ sags — the headlights dim").scale(1.05).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2)
        self.play(Write(c4))
        self.play(Create(SurroundingRectangle(VGroup(c1, c2, c3, c4), color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex("Idle voltage tests the promise;").scale(1.05).shift(band_shift(10) + DOWN * 2.45)
        b10_l6 = Tex("voltage under load tests the battery").scale(1.05).shift(band_shift(10) + DOWN * 3.05)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(4)
