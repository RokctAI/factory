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

# Band-layout whiteboard scene for the session duo "Internal Resistance and
# Networks" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only; circuits are hand-built from Rectangles,
# Lines and Tex labels. Eleven bands, camera moves inline.
# Band dwell time follows subtopics.json (235/240/240/235/190/195/195 of 1530).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class InternalResistanceNetworksSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # --- Band 0 (subtopic_1): the two rules of combination
        title = Tex("Internal Resistance and Networks").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"\text{Series: } R_{tot} = R_1 + R_2 + R_3").scale(1.0).shift(UP * 1.1)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = MathTex(r"\text{Parallel: } \frac{1}{R_{tot}} = \frac{1}{R_1} + \frac{1}{R_2}").scale(1.0).shift(UP * 0.0)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Pair shortcut: product over sum").scale(0.95).shift(DOWN * 1.0)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Alarm: parallel answer must undercut").scale(0.95).shift(DOWN * 1.9)
        b0_l5 = Tex("its smallest branch").scale(0.95).shift(DOWN * 2.7)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): collapse a network — 12 // 6 in series with 5
        self.next_band(1)
        b1_title = Tex("Collapse: 12 // 6, then $+\\,5$").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"12 \,//\, 6 = \frac{12 \times 6}{12 + 6} = \frac{72}{18} = 4\ \Omega").scale(1.0).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex("4 $<$ 6: alarm silent, step accepted").scale(0.95).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"R_{tot} = 5 + 4 = 9\ \Omega").scale(1.05).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = Tex("Universal opening: melt the parallel clusters,").scale(0.9).shift(band_shift(1) + DOWN * 1.9)
        b1_l5 = Tex("then add along the series backbone").scale(0.9).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): emf, internal resistance, the master equation
        self.next_band(2)
        b2_title = Tex("Inside the battery").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        # Battery drawn as a rectangle with hidden r inside.
        c2 = band_shift(2) + UP * 0.9
        batt = Rectangle(width=3.6, height=1.4).move_to(c2)
        r_in = Rectangle(width=0.8, height=0.4).move_to(c2 + RIGHT * 0.9)
        lab_eps = MathTex(r"\varepsilon").scale(0.9).move_to(c2 + LEFT * 0.9)
        lab_r = Tex("r").scale(0.8).move_to(c2 + RIGHT * 0.9)
        self.play(Create(batt))
        self.play(Write(lab_eps), Create(r_in), Write(lab_r))
        self.wait(2)
        b2_l1 = MathTex(r"\varepsilon = IR_{ext} + Ir").scale(1.1).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = Tex("$IR_{ext}$: terminal voltage — spent outside").scale(0.9).shift(band_shift(2) + DOWN * 1.5)
        b2_l3 = Tex("$Ir$: lost volts — heat inside the casing").scale(0.9).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(3)

        # --- Band 3 (subtopic_2): worked budget — 9 V, r = 0,5, R = 4
        self.next_band(3)
        b3_title = Tex("Budget: 9 V, $r = 0,5\\ \\Omega$, $R = 4\\ \\Omega$").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"I = \frac{9}{4 + 0,5} = \frac{9}{4,5} = 2\ \text{A}").scale(1.0).shift(band_shift(3) + UP * 1.0)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"V_{term} = 2 \times 4 = 8\ \text{V}").scale(1.0).shift(band_shift(3) + UP * 0.1)
        b3_l3 = MathTex(r"\text{lost volts} = 2 \times 0,5 = 1\ \text{V}").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"8 + 1 = 9\ \text{V} = \varepsilon").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)
        b3_l5 = Tex("Switch open: $I = 0$, meter reads full emf").scale(0.9).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): full circuit — draw it, collapse the outside
        self.next_band(4)
        b4_title = Tex("Full circuit: 18 V, $r = 1\\ \\Omega$").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("2 $\\Omega$ in series with 10 // 15").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"10 \,//\, 15 = \frac{150}{25} = 6\ \Omega").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"R_{ext} = 2 + 6 = 8\ \Omega").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"R_{loop} = 8 + 1 = 9\ \Omega").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): solve the loop, walk back in, audit
        self.next_band(5)
        b5_title = Tex("Solve, walk back in, audit").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"I = \frac{18}{9} = 2\ \text{A} \quad V_{term} = 18 - 2(1) = 16\ \text{V}").scale(0.9).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"V_{2\Omega} = 2 \times 2 = 4\ \text{V} \quad V_{pair} = 16 - 4 = 12\ \text{V}").scale(0.9).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"I_{10} = \frac{12}{10} = 1,2\ \text{A} \quad I_{15} = \frac{12}{15} = 0,8\ \text{A}").scale(0.9).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"1,2 + 0,8 = 2\ \text{A}\ \checkmark").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex("The audit catches errors before the marker does").scale(0.85).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the V-I graph reads the battery
        self.next_band(6)
        b6_title = Tex("The graph that reads a battery").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        c6 = band_shift(6) + DOWN * 0.6
        ax_v = Line(c6 + LEFT * 3.2 + DOWN * 1.6, c6 + LEFT * 3.2 + UP * 1.8)
        ax_i = Line(c6 + LEFT * 3.2 + DOWN * 1.6, c6 + RIGHT * 3.2 + DOWN * 1.6)
        self.play(Create(ax_v), Create(ax_i))
        lab_v = Tex("$V_{term}$").scale(0.7).shift(c6 + LEFT * 3.8 + UP * 1.6)
        lab_i = Tex("$I$").scale(0.7).shift(c6 + RIGHT * 3.5 + DOWN * 1.6)
        self.play(Write(lab_v), Write(lab_i))
        graph = Line(c6 + LEFT * 3.2 + UP * 1.4, c6 + RIGHT * 2.8 + DOWN * 1.2)
        self.play(Create(graph))
        self.wait(2)
        b6_l1 = MathTex(r"V_{term} = \varepsilon - Ir").scale(0.95).shift(c6 + RIGHT * 1.6 + UP * 1.2)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = Tex("Intercept: emf. Gradient: $-r$.").scale(0.9).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l2))
        self.wait(3)

        # --- Band 7 (subtopic_4): loading and power
        self.next_band(7)
        b7_title = Tex("Loading and power").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("More parallel lamps: $R_{ext}\\downarrow$, $I\\uparrow$,").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("$Ir\\uparrow$, $V_{term}\\downarrow$ — four links, in order").scale(0.95).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = MathTex(r"P = VI = I^2R = \frac{V^2}{R}").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"P_{2\Omega} = 2^2 \times 2 = 8\ \text{W} \quad P_{r} = 2^2 \times 1 = 4\ \text{W}").scale(0.85).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = MathTex(r"8 + 24 + 4 = 36\ \text{W} = \varepsilon I").scale(0.9).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_5): the battery charges a toll
        self.next_band(8)
        b8_title = Tex("The battery charges a toll").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Emf: the push the depot promises").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Toll at the gate: $I \\times r$").scale(0.95).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex("Delivery outside: the terminal voltage").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("No traffic, no charge: idle battery").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        b8_l5 = Tex("shows its full promise").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("Old cell: promise intact, toll extortionate").scale(0.9).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): one river, many channels
        self.next_band(9)
        b9_title = Tex("One river, many channels").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Series: obstacles in a line — difficulties add").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Parallel: channels around islands —").scale(0.95).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("every NEW channel eases the total flow").scale(0.95).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Series shares the PUSH (voltage splits)").scale(0.95).shift(band_shift(9) + DOWN * 1.6)
        b9_l5 = Tex("Parallel shares the FLOW (same voltage)").scale(0.95).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("Name the shared quantity BEFORE calculating").scale(0.9).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_7): the night the headlights dimmed
        self.next_band(10)
        b10_title = Tex("The night the headlights dimmed").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Key turns: starter joins as a greedy").scale(0.95).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("low-resistance parallel branch").scale(0.95).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("1. $R_{ext}\\downarrow$ \\ 2. $I\\uparrow$ \\ 3. $Ir\\uparrow$ \\ 4. $V_{term}\\downarrow$").scale(0.95).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(3)
        b10_l4 = Tex("Same chain: the overloaded multiplug").scale(0.95).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Mechanic's test: idle reads the promise,").scale(0.9).shift(band_shift(10) + DOWN * 2.4)
        b10_l6 = Tex("cranking reads the battery").scale(0.9).shift(band_shift(10) + DOWN * 3.2)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(4)
