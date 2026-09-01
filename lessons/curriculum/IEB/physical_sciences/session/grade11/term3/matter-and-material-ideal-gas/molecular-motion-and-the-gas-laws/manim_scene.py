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

# Band-layout whiteboard scene for the molecular motion and gas laws session
# duo. Covers all seven subtopics (Part 1 Expert: 1-4, Part 2 Simplifier:
# 5-7), band time proportional to subtopics.json
# (235/225/250/250/200/200/210 of 1570 s). Add-only lifecycle; worked
# calculations appear line by line with the script's exact numbers and SA
# decimal commas.

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
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the kinetic model ---
        title = Tex("The Kinetic Model of a Gas").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Particles in continuous, rapid, RANDOM motion").scale(0.95).shift(UP * 1.2)
        b0_l2 = Tex("Elastic collisions — no kinetic energy lost").scale(0.95).shift(UP * 0.4)
        b0_l3 = Tex("Mostly empty space; negligible forces").scale(0.95).shift(DOWN * 0.4)
        self.play(Write(b0_l1))
        self.wait(1.5)
        self.play(Write(b0_l2))
        self.wait(1.5)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Pressure = hail of wall collisions").scale(1.0).shift(DOWN * 1.4)
        b0_l5 = Tex("Temperature = average kinetic energy").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(b0_l4))
        self.wait(1.5)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the average, and the kelvin scale ---
        self.next_band(1)
        b1_t = Tex("A distribution, and a true zero").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = Tex("Molecules span a SPREAD of speeds;").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("heating shifts the whole spread faster").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.wait(1.5)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex(r"Motion ceases at $-273\,^\circ$C: absolute zero").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"T_K = T_C + 273").scale(1.15).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = MathTex(r"30\,^\circ C = 303 \text{ K}").scale(1.0).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): ideal vs real gases ---
        self.next_band(2)
        b2_t = Tex("Ideal gas: the useful fiction").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("Pretends: zero molecular volume,").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("zero forces between collisions").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.wait(1.5)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("HIGH pressure: molecular volume matters").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("LOW temperature: attractions get a grip").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Most ideal: low p, high T — He and $H_2$").scale(0.95).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): Boyle's law from the practical ---
        self.next_band(3)
        b3_t = Tex("Boyle's law from the results table").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = MathTex(r"80 \times 3{,}0 = 240 \quad 120 \times 2{,}0 = 240").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"240 \times 1{,}0 = 240 \quad 480 \times 0{,}5 = 240").scale(0.95).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("The product pV is CONSTANT").scale(1.05).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = MathTex(r"p_1V_1 = p_2V_2 \quad \text{(fixed gas, constant T)}").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Half the space: walls hit twice as often").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the graphs and the calculation ---
        self.next_band(4)
        b4_t = Tex("Three graphs, one calculation").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_t))
        self.wait(2)
        # p vs V hyperbola sketch
        orig = band_shift(4) + LEFT * 5.2 + DOWN * 1.6
        ax1 = Arrow(orig, orig + UP * 3.0, buff=0, stroke_width=3)
        ax2 = Arrow(orig, orig + RIGHT * 3.4, buff=0, stroke_width=3)
        c1 = Line(orig + UP * 2.6 + RIGHT * 0.4, orig + UP * 1.2 + RIGHT * 1.1, color=BLUE, stroke_width=4)
        c2 = Line(orig + UP * 1.2 + RIGHT * 1.1, orig + UP * 0.55 + RIGHT * 2.0, color=BLUE, stroke_width=4)
        c3 = Line(orig + UP * 0.55 + RIGHT * 2.0, orig + UP * 0.3 + RIGHT * 3.1, color=BLUE, stroke_width=4)
        g1_lab = Tex("p vs V: falling curve").scale(0.75).shift(band_shift(4) + LEFT * 3.4 + DOWN * 2.2)
        self.play(Create(ax1), Create(ax2))
        self.play(Create(c1), Create(c2), Create(c3))
        self.play(Write(g1_lab))
        self.wait(2)
        # p vs 1/V straight line
        orig2 = band_shift(4) + RIGHT * 0.6 + DOWN * 1.6
        ax3 = Arrow(orig2, orig2 + UP * 3.0, buff=0, stroke_width=3)
        ax4 = Arrow(orig2, orig2 + RIGHT * 3.4, buff=0, stroke_width=3)
        line = Line(orig2, orig2 + UP * 2.6 + RIGHT * 3.0, color=YELLOW, stroke_width=4)
        g2_lab = Tex("p vs 1/V: straight through origin").scale(0.75).shift(band_shift(4) + RIGHT * 2.4 + DOWN * 2.2)
        self.play(Create(ax3), Create(ax4))
        self.play(Create(line))
        self.play(Write(g2_lab))
        self.wait(2)
        b4_c1 = MathTex(r"80 \times 3 = p_2 \times 0{,}75").scale(1.0).shift(band_shift(4) + UP * 1.3 + RIGHT * 2.6)
        b4_c2 = MathTex(r"p_2 = 320 \text{ kPa}").scale(1.05).shift(band_shift(4) + UP * 0.4 + RIGHT * 2.6)
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
        b5_l1 = MathTex(r"47 + 273 = 320 \text{ K}, \quad 87 + 273 = 360 \text{ K}").scale(0.95).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\frac{90 \times 4}{320} = \frac{135 \times V_2}{360}").scale(1.05).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"V_2 = \frac{1{,}125 \times 360}{135} = 3 \text{ dm}^3").scale(1.05).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_n = Tex("Celsius breaks the ratios — kelvin first").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
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
        b6_l2 = MathTex(r"40 \text{ dm}^3 = 0{,}04 \text{ m}^3").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"p = \frac{nRT}{V} = \frac{1{,}5 \times 8{,}31 \times 350}{0{,}04}").scale(1.05).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"p = 109\,069 \text{ Pa} \approx 109{,}1 \text{ kPa}").scale(1.05).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_n = Tex("Sanity: everyday pressures sit near 100 kPa").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_n))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): a room full of super balls ---
        self.next_band(7)
        b7_t = Tex("A room full of super balls").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Pressure = the drizzle of tiny knocks").scale(1.05).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("on the container walls").scale(1.05).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.wait(1.5)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Temperature = the swarm's liveliness").scale(1.05).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex(r"All motion frozen at $-273\,^\circ$C:").scale(1.0).shift(band_shift(7) + DOWN * 1.3)
        b7_l5 = MathTex(r"30\,^\circ C = 303 \text{ K}").scale(1.05).shift(band_shift(7) + DOWN * 2.2)
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
        b8_l1 = Tex("Same swarm, half the space:").scale(1.05).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("knocks double — pressure doubles").scale(1.05).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = MathTex(r"80 \times 3 = 320 \times 0{,}75 = 240").scale(1.05).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("The product stands still — the balancing act").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Fine print: fixed gas, constant temperature").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): one equation for every balloon ---
        self.next_band(9)
        b9_t = Tex("One equation for every balloon").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Hot car: faster balls knock harder").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"\frac{pV}{T} = \text{constant} \quad \text{(kelvin only!)}").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"pV = nRT").scale(1.25).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("Four dials — any three reveal the fourth").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("A molecule census by gauge and thermometer").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5))
        self.wait(4)
