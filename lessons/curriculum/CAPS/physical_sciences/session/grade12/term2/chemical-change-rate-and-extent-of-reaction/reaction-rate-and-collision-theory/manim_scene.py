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

# Band-layout whiteboard scene for "Reaction Rate and Collision Theory"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only; the volume-time curves and the molecular
# energy distribution are hand-built from Arrow axes + Line segment chains.
# Subtopic durations 235/240/240/240/195/195/195 of 1540 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ReactionRateCollisionTheorySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): definition + rate calculation ---
        title = Tex("Reaction Rate and Collision Theory").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_def = MathTex(r"\text{rate} = \frac{\Delta n}{\Delta t} \;\; [\text{mol·s}^{-1}]").scale(1.1).shift(UP * 1.0)
        self.play(Write(b0_def))
        self.wait(2.5)
        b0_l1 = Tex(r"$CO_2$ escapes: mass drops 2,2 g in 50 s").scale(1.0).shift(UP * 0.1)
        b0_l2 = MathTex(r"n = \frac{2{,}2}{44} = 0{,}05\ \text{mol}").scale(1.05).shift(DOWN * 0.9)
        b0_l3 = MathTex(r"\text{rate} = \frac{0{,}05}{50} = 0{,}001\ \text{mol·s}^{-1}").scale(1.05).shift(DOWN * 2.0)
        self.play(Write(b0_l1))
        self.wait(2.5)
        self.play(Write(b0_l2))
        self.wait(2.5)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = Tex("Rate: how fast. Extent: how much in total.").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(b0_l4))
        self.wait(3.5)

        # --- Band 1 (subtopic_2): collision theory, first factors ---
        self.next_band(1)
        b1_title = Tex("Collision theory: the explanation engine").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Effective collision needs BOTH:").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("correct orientation, and energy $\\geq E_a$").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Nature: Mg fizzes in acid, Cu does not").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = Tex("Surface area: powder exposes particles —").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        b1_l5 = Tex("more collisions per second, faster").scale(1.0).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): concentration, temperature, catalyst ---
        self.next_band(2)
        b2_title = Tex("The stronger levers").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Concentration/pressure: more particles").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("per volume, more collisions per second").scale(1.0).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("Temperature: a larger FRACTION of").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        b2_l4 = Tex("collisions now carries at least $E_a$").scale(1.0).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)
        b2_l5 = Tex("Catalyst: faster, without being consumed").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l5))
        self.wait(2)
        b2_rule = Tex("Every answer ends: effective collisions/s").scale(0.95).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_rule))
        self.wait(3)

        # --- Band 3 (subtopic_3): measurement techniques ---
        self.next_band(3)
        b3_title = Tex("Measuring rate in the laboratory").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("1. Gas volume in a syringe, vs time").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("2. Mass loss on a balance, gas escaping").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex("3. Disappearing cross: thiosulfate clouds").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex("4. Colour change, timed or metered").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_warn = Tex("Cross: SHORT time $=$ FAST reaction").scale(1.0).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_warn))
        self.play(Create(SurroundingRectangle(b3_warn, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): powder vs chips, same plateau ---
        self.next_band(4)
        b4_title = Tex("Powder vs chips: same gas, faster start").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        o4 = band_shift(4) + LEFT * 4.8 + DOWN * 1.8
        ax4_t = Arrow(o4 + LEFT * 0.2, o4 + RIGHT * 7.6, buff=0, stroke_width=3)
        ax4_v = Arrow(o4 + DOWN * 0.2, o4 + UP * 3.6, buff=0, stroke_width=3)
        lab4_t = Tex("$t$").scale(0.9).shift(o4 + RIGHT * 7.8 + DOWN * 0.3)
        lab4_v = Tex("V(gas)").scale(0.85).shift(o4 + UP * 3.6 + LEFT * 0.9)
        self.play(Create(ax4_t), Create(ax4_v))
        self.play(Write(lab4_t), Write(lab4_v))
        self.wait(1.5)
        powder = VGroup(
            Line(o4, o4 + RIGHT * 1.0 + UP * 1.9, color=YELLOW),
            Line(o4 + RIGHT * 1.0 + UP * 1.9, o4 + RIGHT * 2.0 + UP * 2.5, color=YELLOW),
            Line(o4 + RIGHT * 2.0 + UP * 2.5, o4 + RIGHT * 3.0 + UP * 2.7, color=YELLOW),
            Line(o4 + RIGHT * 3.0 + UP * 2.7, o4 + RIGHT * 7.0 + UP * 2.7, color=YELLOW),
        )
        self.play(Create(powder), run_time=2)
        lab_p = Tex("powder").scale(0.85).shift(o4 + RIGHT * 1.1 + UP * 2.9)
        self.play(Write(lab_p))
        self.wait(1.5)
        chips = VGroup(
            Line(o4, o4 + RIGHT * 1.5 + UP * 0.9, color=BLUE),
            Line(o4 + RIGHT * 1.5 + UP * 0.9, o4 + RIGHT * 3.0 + UP * 1.7, color=BLUE),
            Line(o4 + RIGHT * 3.0 + UP * 1.7, o4 + RIGHT * 4.5 + UP * 2.4, color=BLUE),
            Line(o4 + RIGHT * 4.5 + UP * 2.4, o4 + RIGHT * 5.5 + UP * 2.7, color=BLUE),
            Line(o4 + RIGHT * 5.5 + UP * 2.7, o4 + RIGHT * 7.0 + UP * 2.7, color=BLUE),
        )
        self.play(Create(chips), run_time=2)
        lab_c = Tex("chips").scale(0.85).shift(o4 + RIGHT * 4.3 + UP * 1.3)
        self.play(Write(lab_c))
        self.wait(2)
        b4_note = Tex("Steeper start, SAME plateau: extent equal").scale(1.0).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_note))
        self.play(Create(SurroundingRectangle(b4_note, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): energy distribution + catalyst ---
        self.next_band(5)
        b5_title = Tex("Molecular energy distribution").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        o5 = band_shift(5) + LEFT * 4.8 + DOWN * 1.6
        ax5_e = Arrow(o5 + LEFT * 0.2, o5 + RIGHT * 7.6, buff=0, stroke_width=3)
        ax5_n = Arrow(o5 + DOWN * 0.2, o5 + UP * 3.4, buff=0, stroke_width=3)
        lab5_e = Tex("$E_k$").scale(0.85).shift(o5 + RIGHT * 7.8 + DOWN * 0.3)
        lab5_n = Tex("no. of particles").scale(0.75).shift(o5 + UP * 3.5 + RIGHT * 1.2)
        self.play(Create(ax5_e), Create(ax5_n))
        self.play(Write(lab5_e), Write(lab5_n))
        self.wait(1.5)
        hump = VGroup(
            Line(o5, o5 + RIGHT * 0.8 + UP * 1.4, color=YELLOW),
            Line(o5 + RIGHT * 0.8 + UP * 1.4, o5 + RIGHT * 1.7 + UP * 2.3, color=YELLOW),
            Line(o5 + RIGHT * 1.7 + UP * 2.3, o5 + RIGHT * 2.8 + UP * 1.7, color=YELLOW),
            Line(o5 + RIGHT * 2.8 + UP * 1.7, o5 + RIGHT * 4.2 + UP * 0.8, color=YELLOW),
            Line(o5 + RIGHT * 4.2 + UP * 0.8, o5 + RIGHT * 7.0 + UP * 0.25, color=YELLOW),
        )
        self.play(Create(hump), run_time=2.5)
        ea_line = DashedLine(o5 + RIGHT * 4.8, o5 + RIGHT * 4.8 + UP * 3.0, color=RED)
        lab_ea = MathTex(r"E_a").scale(0.9).shift(o5 + RIGHT * 4.8 + UP * 3.3)
        self.play(Create(ea_line))
        self.play(Write(lab_ea))
        self.wait(2)
        b5_l1 = Tex("Only the tail beyond $E_a$ can react").scale(0.95).shift(o5 + RIGHT * 6.2 + UP * 1.6)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex("Heat: curve flattens right, tail grows").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        b5_l3 = Tex("Catalyst: the LINE moves left, not the curve").scale(1.0).shift(band_shift(5) + DOWN * 3.4)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): catalyst on the PE diagram ---
        self.next_band(6)
        b6_title = Tex("Catalyst: new path, lower barrier").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Alternative pathway with lower $E_a$").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("Start, end and $\\Delta H$: unchanged").scale(1.05).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex("Not consumed: a small amount lasts —").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        b6_l4 = Tex("a catalytic converter works for years").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("The journey changes, never the destination").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): how fast is not how far ---
        self.next_band(7)
        b7_title = Tex("How fast is not how far").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Loose sugar, hot tea: dissolves in seconds").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("Cube in cold tea: minutes — SAME sweetness").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Rate differed; extent identical").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Reactions sprint at the start, limp at the end").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_6): bumper cars ---
        self.next_band(8)
        b8_title = Tex("Bumper cars: only hard hits count").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Hard enough $+$ right angle $=$ it counts").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("More cars on the floor: concentration").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("Smash the big car to bits: surface area").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = Tex("Turn up every motor: temperature —").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        b8_l5 = Tex("far more bumps cross the threshold").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex("Catalyst: lowers the bar, never used up").scale(1.0).shift(band_shift(8) + DOWN * 3.3)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): reading the story off the graph ---
        self.next_band(9)
        b9_title = Tex("The graph's three words").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("STEEPNESS is speed").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("The BEND is the slowdown: sprint, tire, stop").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("The PLATEAU height is the amount made").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_wrong = Tex("Faster means more product").scale(1.05).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_wrong))
        self.play(Create(strike(b9_wrong)))
        self.wait(2)
        b9_rule = Tex("Same chalk, same gas: plateaus match").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_rule))
        self.play(Create(SurroundingRectangle(b9_rule, color=GREEN)))
        self.wait(4)
