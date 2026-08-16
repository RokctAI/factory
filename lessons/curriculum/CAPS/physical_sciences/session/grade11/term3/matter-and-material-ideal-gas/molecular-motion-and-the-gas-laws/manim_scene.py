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

# Band-layout whiteboard scene for the molecular motion and gas laws session
# duo. Covers all seven subtopics (Part 1 Expert: 1-4, Part 2 Simplifier:
# 5-7), band time proportional to subtopics.json
# (235/225/250/250/200/200/210 of 1570 s). Add-only lifecycle; Boyle graphs
# hand-built from Arrow axes and Line segment chains (exporter-safe only).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MolecularMotionGasLawsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the kinetic model ---
        title = Tex("The Kinetic Model of a Gas").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Particles in continuous, random motion;").scale(1.0).shift(UP * 1.2)
        b0_l2 = Tex("elastic collisions; mostly empty space;").scale(1.0).shift(UP * 0.5)
        b0_l3 = Tex("negligible forces between particles").scale(1.0).shift(DOWN * 0.2)
        self.play(Write(b0_l1))
        self.wait(1.5)
        self.play(Write(b0_l2))
        self.wait(1.5)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("PRESSURE = the storm of wall collisions").scale(1.05).shift(DOWN * 1.2)
        b0_l5 = Tex("TEMPERATURE = average kinetic energy").scale(1.05).shift(DOWN * 2.1)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the average, and the kelvin scale ---
        self.next_band(1)
        b1_t = Tex("Average speed, absolute scale").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = Tex("Molecules carry a DISTRIBUTION of speeds;").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("heating shifts the whole crowd faster").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex(r"Zero of temperature = zero motion:").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = Tex(r"absolute zero, $-273\,^\circ$C").scale(1.05).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_l3))
        self.wait(1.5)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_f = MathTex(r"T(K) = t(^\circ C) + 273").scale(1.15).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_f))
        self.play(Create(SurroundingRectangle(b1_f, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex(r"$25\,^\circ$C $= 298$ K — kelvin, always").scale(1.0).shift(band_shift(1) + DOWN * 3.3)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): ideal vs real gases ---
        self.next_band(2)
        b2_t = Tex("Ideal gases and real gases").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("Ideal: zero particle volume, zero forces").scale(1.05).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("Real gases deviate at HIGH pressure:").scale(1.0).shift(band_shift(2) + UP * 0.3)
        b2_l3 = Tex("molecular volume becomes significant").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l2))
        self.wait(1.5)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("...and at LOW temperature:").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        b2_l5 = Tex("intermolecular forces get time to act").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.wait(1.5)
        self.play(Write(b2_l5))
        self.wait(2)
        b2_l6 = Tex(r"Most ideal: low $p$, high $T$ — He and $H_2$").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): Boyle's law from the practical ---
        self.next_band(3)
        b3_t = Tex("Boyle's law from the practical").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = MathTex(r"100 \times 2{,}0 = 200").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"125 \times 1{,}6 = 200").scale(1.0).shift(band_shift(3) + UP * 0.4)
        b3_l3 = MathTex(r"200 \times 1{,}0 = 200").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = MathTex(r"400 \times 0{,}5 = 200").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_l1))
        self.wait(1.5)
        self.play(Write(b3_l2))
        self.wait(1.5)
        self.play(Write(b3_l3))
        self.wait(1.5)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_f = MathTex(r"pV = k \;\Rightarrow\; p_1V_1 = p_2V_2").scale(1.15).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_f))
        self.play(Create(SurroundingRectangle(b3_f, color=GREEN)))
        self.wait(2)
        b3_n = Tex("constant T, fixed amount of gas").scale(0.95).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_n))
        self.wait(3)

        # --- Band 4 (subtopic_3): the graphs and the calculation ---
        self.next_band(4)
        b4_t = Tex("The three graphs, and a calculation").scale(1.1).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_t))
        self.wait(2)
        # Left mini-graph: p vs V — falling hyperbola (line chain)
        oL = band_shift(4) + LEFT * 5.6 + DOWN * 1.4
        axL1 = Arrow(oL, oL + UP * 3.0, buff=0, stroke_width=3)
        axL2 = Arrow(oL, oL + RIGHT * 3.6, buff=0, stroke_width=3)
        labL = Tex(r"$p$ vs $V$: hyperbola").scale(0.7).shift(oL + RIGHT * 1.8 + DOWN * 0.6)
        h1 = Line(oL + RIGHT * 0.4 + UP * 2.6, oL + RIGHT * 0.9 + UP * 1.5, color=BLUE, stroke_width=4)
        h2 = Line(oL + RIGHT * 0.9 + UP * 1.5, oL + RIGHT * 1.7 + UP * 0.9, color=BLUE, stroke_width=4)
        h3 = Line(oL + RIGHT * 1.7 + UP * 0.9, oL + RIGHT * 2.6 + UP * 0.6, color=BLUE, stroke_width=4)
        h4 = Line(oL + RIGHT * 2.6 + UP * 0.6, oL + RIGHT * 3.3 + UP * 0.45, color=BLUE, stroke_width=4)
        self.play(Create(axL1), Create(axL2))
        self.play(Create(h1), Create(h2), Create(h3), Create(h4))
        self.play(Write(labL))
        self.wait(2)
        # Right mini-graph: p vs 1/V — straight line through origin
        oR = band_shift(4) + RIGHT * 1.2 + DOWN * 1.4
        axR1 = Arrow(oR, oR + UP * 3.0, buff=0, stroke_width=3)
        axR2 = Arrow(oR, oR + RIGHT * 3.6, buff=0, stroke_width=3)
        sline = Line(oR, oR + RIGHT * 3.1 + UP * 2.5, color=BLUE, stroke_width=4)
        labR = Tex(r"$p$ vs $\frac{1}{V}$: line through origin").scale(0.7).shift(oR + RIGHT * 1.9 + DOWN * 0.6)
        self.play(Create(axR1), Create(axR2))
        self.play(Create(sline))
        self.play(Write(labR))
        self.wait(2)
        b4_c1 = MathTex(r"100 \times 2 = p_2 \times 0{,}5").scale(1.0).shift(band_shift(4) + UP * 1.5 + RIGHT * 3.2)
        b4_c2 = MathTex(r"p_2 = 400 \text{ kPa}").scale(1.05).shift(band_shift(4) + UP * 0.6 + RIGHT * 3.2)
        self.play(Write(b4_c1))
        self.wait(2)
        self.play(Write(b4_c2))
        self.play(Create(SurroundingRectangle(b4_c2, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): the general gas equation ---
        self.next_band(5)
        b5_t = Tex("The general gas equation").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_f = MathTex(r"\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}").scale(1.2).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_f))
        self.wait(2.5)
        b5_l1 = MathTex(r"27 + 273 = 300 \text{ K}, \quad 127 + 273 = 400 \text{ K}").scale(0.95).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\frac{100 \times 3}{300} = \frac{150 \times V_2}{400}").scale(1.05).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"V_2 = \frac{400}{150} = 2{,}67 \text{ dm}^3").scale(1.05).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_n = Tex("Celsius gives nonsense — kelvin first").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_n))
        self.wait(3)

        # --- Band 6 (subtopic_4): the ideal gas law ---
        self.next_band(6)
        b6_f = MathTex(r"pV = nRT, \quad R = 8{,}31 \text{ J/(K mol)}").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_f))
        self.wait(2.5)
        b6_l1 = Tex(r"Units: Pa, m$^3$, K — strictly").scale(1.05).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"50 \text{ dm}^3 = 0{,}05 \text{ m}^3").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"p = \frac{nRT}{V} = \frac{2 \times 8{,}31 \times 300}{0{,}05}").scale(1.05).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"p = 99\,720 \text{ Pa} = 99{,}7 \text{ kPa}").scale(1.05).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_n = Tex("Sanity check: everyday pressures near 100 kPa").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_n))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): a room full of super balls ---
        self.next_band(7)
        b7_t = Tex("A room full of super balls").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Pressure = the drumroll of tiny taps").scale(1.05).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("on the container walls").scale(1.05).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.wait(1.5)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Temperature = the crowd's liveliness").scale(1.05).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex(r"All motion stops at $-273\,^\circ$C:").scale(1.0).shift(band_shift(7) + DOWN * 1.3)
        b7_l5 = MathTex(r"25\,^\circ C = 298 \text{ K}").scale(1.05).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l4))
        self.wait(1.5)
        self.play(Write(b7_l5))
        self.wait(2)
        b7_l6 = Tex("Ideal gas = the nearly-true pretence").scale(1.0).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l6))
        self.wait(3)

        # --- Band 8 (subtopic_6): squeeze the bottle ---
        self.next_band(8)
        b8_t = Tex("Squeeze the bottle — Boyle in your hands").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Same crowd, half the space:").scale(1.05).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("drumroll doubles — pressure doubles").scale(1.05).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = MathTex(r"100 \times 2 = 400 \times 0{,}5 = 200").scale(1.05).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("The see-saw: product stays constant —").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        b8_l5 = Tex("check the fine print: same T, same gas").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l4))
        self.wait(1.5)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): one equation for every balloon ---
        self.next_band(9)
        b9_t = Tex("One equation for every balloon").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Three dials move together:").scale(1.05).shift(band_shift(9) + UP * 1.2)
        b9_f1 = MathTex(r"\frac{pV}{T} = \text{constant (kelvin only!)}").scale(1.05).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.wait(1.5)
        self.play(Write(b9_f1))
        self.wait(2.5)
        b9_f2 = MathTex(r"pV = nRT").scale(1.3).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_f2))
        self.play(Create(SurroundingRectangle(b9_f2, color=GREEN)))
        self.wait(2.5)
        b9_l2 = Tex("Count invisible molecules with a gauge,").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        b9_l3 = Tex("a jug and a thermometer").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l2))
        self.wait(1.5)
        self.play(Write(b9_l3))
        self.wait(4)
