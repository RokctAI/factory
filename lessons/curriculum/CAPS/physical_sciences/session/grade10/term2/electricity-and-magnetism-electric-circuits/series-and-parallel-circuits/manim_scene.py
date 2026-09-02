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

# Band-layout whiteboard scene for the series-and-parallel-circuits session
# duo (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only: Tex/MathTex/Text, Line/Arrow, Dot, Circle,
# Rectangle/SurroundingRectangle, VGroup. Add-only lifecycle; the camera
# moves down one frame-height per band and earlier work stays on canvas.
# Band time is apportioned to subtopics.json (220/230/230/270/180/180/180
# of 1490 s); Level 6 rescales to the real audio, so proportion is what counts.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SeriesAndParallelCircuitsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): charge, energy, the three quantities ---
        title = Tex("Series and Parallel Circuits").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        q1 = MathTex(r"I = \frac{Q}{\Delta t} \; \text{(A: 1 C per second)}").scale(1.1).shift(UP * 1.0)
        self.play(Write(q1))
        self.wait(2.5)
        q2 = MathTex(r"V = \frac{W}{Q} \; \text{(1 V = 1 J per C)}").scale(1.1).shift(DOWN * 0.2)
        self.play(Write(q2))
        self.wait(2.5)
        q3 = Tex("Charge circulates; ENERGY is spent").scale(1.1).shift(DOWN * 1.4)
        self.play(Write(q3))
        self.wait(2)
        q4 = Tex("Chemical $\\rightarrow$ electrical $\\rightarrow$ heat, light").scale(1.05).shift(DOWN * 2.4)
        self.play(Write(q4))
        self.wait(3)

        # --- Band 1 (subtopic_1): resistance + the two instrument rules ---
        self.next_band(1)
        b1_t = Tex("Resistance and the two meters").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_1 = Tex(r"$R$ (ohm): opposition to charge flow").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_1))
        self.wait(2)
        b1_2 = Tex("Longer / hotter wire: more $R$").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_3 = Tex("Thicker wire, copper: less $R$").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_2))
        self.wait(1.5)
        self.play(Write(b1_3))
        self.wait(2)
        b1_4 = Tex("Ammeter: in SERIES, low $R$").scale(1.1).shift(band_shift(1) + DOWN * 1.6)
        b1_5 = Tex("Voltmeter: in PARALLEL, high $R$").scale(1.1).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_4))
        self.wait(2)
        self.play(Write(b1_5))
        self.wait(3)

        # --- Band 2 (subtopic_2): Ohm's law + the series circuit, drawn ---
        self.next_band(2)
        b2_t = Tex("Ohm's law and the series loop").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_ohm = MathTex(r"V = IR \quad I = \frac{V}{R} \quad R = \frac{V}{I}").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_ohm))
        self.wait(2.5)
        # circuit: battery at bottom, two resistors on the top wire, one loop
        c = band_shift(2) + DOWN * 1.2
        bat = Rectangle(width=1.4, height=0.6).move_to(c + DOWN * 1.4)
        bat_l = Tex("12 V").scale(0.9).move_to(c + DOWN * 1.4)
        r1 = Rectangle(width=1.2, height=0.5).move_to(c + UP * 1.0 + LEFT * 1.5)
        r1_l = Tex("4 $\\Omega$").scale(0.9).move_to(c + UP * 1.7 + LEFT * 1.5)
        r2 = Rectangle(width=1.2, height=0.5).move_to(c + UP * 1.0 + RIGHT * 1.5)
        r2_l = Tex("8 $\\Omega$").scale(0.9).move_to(c + UP * 1.7 + RIGHT * 1.5)
        wires = VGroup(
            Line(c + DOWN * 1.4 + LEFT * 0.7, c + DOWN * 1.4 + LEFT * 3.0),
            Line(c + DOWN * 1.4 + LEFT * 3.0, c + UP * 1.0 + LEFT * 3.0),
            Line(c + UP * 1.0 + LEFT * 3.0, c + UP * 1.0 + LEFT * 2.1),
            Line(c + UP * 1.0 + LEFT * 0.9, c + UP * 1.0 + RIGHT * 0.9),
            Line(c + UP * 1.0 + RIGHT * 2.1, c + UP * 1.0 + RIGHT * 3.0),
            Line(c + UP * 1.0 + RIGHT * 3.0, c + DOWN * 1.4 + RIGHT * 3.0),
            Line(c + DOWN * 1.4 + RIGHT * 3.0, c + DOWN * 1.4 + RIGHT * 0.7),
        )
        self.play(Create(bat), Write(bat_l))
        self.wait(1)
        self.play(Create(wires))
        self.wait(1)
        self.play(Create(r1), Write(r1_l))
        self.play(Create(r2), Write(r2_l))
        self.wait(1.5)
        i_arrow = Arrow(c + DOWN * 2.3 + RIGHT * 1.0, c + DOWN * 2.3 + LEFT * 1.0, buff=0)
        i_lab = Tex("one loop: same $I$ everywhere").scale(0.95).shift(c + DOWN * 2.9)
        self.play(Create(i_arrow), Write(i_lab))
        self.wait(3)

        # --- Band 3 (subtopic_2): the series numbers, line by line ---
        self.next_band(3)
        b3_t = Tex("Series: work the numbers").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_1 = MathTex(r"R_s = 4 + 8 = 12\ \Omega").scale(1.15).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_1))
        self.wait(2)
        b3_2 = MathTex(r"I = \frac{V}{R} = \frac{12}{12} = 1\ \text{A}").scale(1.15).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3_2))
        self.wait(2.5)
        b3_3 = MathTex(r"V_1 = IR_1 = 1 \times 4 = 4\ \text{V}").scale(1.1).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_3))
        self.wait(2)
        b3_4 = MathTex(r"V_2 = 1 \times 8 = 8\ \text{V}").scale(1.1).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_4))
        self.wait(2)
        b3_5 = MathTex(r"4 + 8 = 12\ \text{V} \; \checkmark").scale(1.1).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_5))
        self.play(Create(SurroundingRectangle(b3_5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the parallel circuit, drawn ---
        self.next_band(4)
        b4_t = Tex("Parallel: two paths, two junctions").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        p = band_shift(4) + DOWN * 0.6
        pbat = Rectangle(width=1.4, height=0.6).move_to(p + DOWN * 1.8)
        pbat_l = Tex("12 V").scale(0.9).move_to(p + DOWN * 1.8)
        jA = Dot(p + UP * 0.4 + LEFT * 2.6)
        jB = Dot(p + UP * 0.4 + RIGHT * 2.6)
        pr1 = Rectangle(width=1.2, height=0.5).move_to(p + UP * 1.4)
        pr1_l = Tex("4 $\\Omega$").scale(0.9).move_to(p + UP * 2.05)
        pr2 = Rectangle(width=1.2, height=0.5).move_to(p + DOWN * 0.6)
        pr2_l = Tex("8 $\\Omega$").scale(0.9).move_to(p + DOWN * 0.0)
        pwires = VGroup(
            Line(p + DOWN * 1.8 + LEFT * 0.7, p + DOWN * 1.8 + LEFT * 2.6),
            Line(p + DOWN * 1.8 + LEFT * 2.6, p + UP * 0.4 + LEFT * 2.6),
            Line(p + UP * 0.4 + LEFT * 2.6, p + UP * 1.4 + LEFT * 2.6),
            Line(p + UP * 1.4 + LEFT * 2.6, p + UP * 1.4 + LEFT * 0.6),
            Line(p + UP * 1.4 + RIGHT * 0.6, p + UP * 1.4 + RIGHT * 2.6),
            Line(p + UP * 1.4 + RIGHT * 2.6, p + UP * 0.4 + RIGHT * 2.6),
            Line(p + UP * 0.4 + LEFT * 2.6, p + DOWN * 0.6 + LEFT * 2.6),
            Line(p + DOWN * 0.6 + LEFT * 2.6, p + DOWN * 0.6 + LEFT * 0.6),
            Line(p + DOWN * 0.6 + RIGHT * 0.6, p + DOWN * 0.6 + RIGHT * 2.6),
            Line(p + DOWN * 0.6 + RIGHT * 2.6, p + UP * 0.4 + RIGHT * 2.6),
            Line(p + UP * 0.4 + RIGHT * 2.6, p + DOWN * 1.8 + RIGHT * 2.6),
            Line(p + DOWN * 1.8 + RIGHT * 2.6, p + DOWN * 1.8 + RIGHT * 0.7),
        )
        self.play(Create(pbat), Write(pbat_l))
        self.play(Create(jA), Create(jB))
        self.wait(1)
        self.play(Create(pwires))
        self.wait(1)
        self.play(Create(pr1), Write(pr1_l))
        self.play(Create(pr2), Write(pr2_l))
        self.wait(1.5)
        b4_r = Tex("Same 12 V across EVERY branch").scale(1.05).shift(p + DOWN * 2.7)
        self.play(Write(b4_r))
        self.wait(3)

        # --- Band 5 (subtopic_3): reciprocal formula, the invert step ---
        self.next_band(5)
        b5_t = Tex("Total resistance in parallel").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_1 = MathTex(r"\frac{1}{R_p} = \frac{1}{4} + \frac{1}{8}").scale(1.15).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_1))
        self.wait(2)
        b5_2 = MathTex(r"= \frac{2}{8} + \frac{1}{8} = \frac{3}{8}").scale(1.15).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_2))
        self.wait(2)
        b5_trap = MathTex(r"R_p = \frac{3}{8}\ \Omega \; \text{(forgot to invert!)}").scale(1.05).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_trap))
        self.play(Create(strike(b5_trap)))
        self.wait(2)
        b5_3 = MathTex(r"R_p = \frac{8}{3} = 2{,}67\ \Omega").scale(1.15).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_3))
        self.play(Create(SurroundingRectangle(b5_3, color=GREEN)))
        self.wait(2)
        b5_4 = Tex("Always less than the smallest branch").scale(1.0).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_4))
        self.wait(3)

        # --- Band 6 (subtopic_3): the parallel currents ---
        self.next_band(6)
        b6_t = Tex("Parallel: the currents").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_1 = MathTex(r"I = \frac{V}{R} = \frac{12}{2{,}67} = 4{,}5\ \text{A}").scale(1.1).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_1))
        self.wait(2.5)
        b6_2 = MathTex(r"I_1 = \frac{12}{4} = 3\ \text{A}").scale(1.1).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_2))
        self.wait(2)
        b6_3 = MathTex(r"I_2 = \frac{12}{8} = 1{,}5\ \text{A}").scale(1.1).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_3))
        self.wait(2)
        b6_4 = MathTex(r"3 + 1{,}5 = 4{,}5\ \text{A} \; \checkmark").scale(1.1).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_4))
        self.play(Create(SurroundingRectangle(b6_4, color=GREEN)))
        self.wait(2)
        b6_5 = Tex("Smaller $R$ takes the larger current").scale(1.0).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the two rule sets, side by side ---
        self.next_band(7)
        b7_t = Tex("Series against parallel").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_1 = Tex("SERIES: same $I$; $V$'s add; $R$'s add").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_1))
        self.wait(2.5)
        b7_2 = Tex("one break kills everything").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_2))
        self.wait(2)
        b7_3 = Tex("PARALLEL: same $V$; $I$'s add").scale(1.05).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_3))
        self.wait(2)
        b7_4 = Tex("reciprocals add; total $<$ smallest").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_4))
        self.wait(2)
        b7_5 = MathTex(r"\text{Same parts: } 1\ \text{A vs } 4{,}5\ \text{A}").scale(1.05).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_5))
        self.play(Create(SurroundingRectangle(b7_5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): error museum + the house ---
        self.next_band(8)
        b8_t = Tex("The error museum").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_1 = Tex("Equal $I$ in parallel branches").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_1))
        self.play(Create(strike(b8_1)))
        self.wait(2)
        b8_2 = Tex("Same PATH, same $I$; same JUNCTIONS, same $V$").scale(0.95).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_2))
        self.wait(2.5)
        b8_3 = Tex("Convert mA to A; never omit units").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_3))
        self.wait(2)
        b8_4 = Tex("House: PARALLEL, 230 V per branch").scale(1.05).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_4))
        self.wait(2)
        b8_5 = Tex("More appliances: $R$ falls, $I$ climbs").scale(1.0).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): one road through town ---
        self.next_band(9)
        b9_t = Tex("One road through town").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_1 = Tex("Taxis = charge; 12 V = 12 J per load").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_1))
        self.wait(2.5)
        b9_2 = Tex("One road: same traffic everywhere").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_2))
        self.wait(2)
        b9_3 = MathTex(r"R_s = 4 + 8 = 12\ \Omega, \quad I = 1\ \text{A}").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_3))
        self.wait(2.5)
        b9_4 = MathTex(r"4\ \text{V} + 8\ \text{V} = 12\ \text{V}").scale(1.05).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_4))
        self.play(Create(SurroundingRectangle(b9_4, color=GREEN)))
        self.wait(2)
        b9_5 = Tex("Close the road anywhere: all stop").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_5))
        self.wait(3)

        # --- Band 10 (subtopic_6): two roads, two queues ---
        self.next_band(10)
        b10_t = Tex("Two roads, two queues").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_1 = Tex("Every route drops the FULL 12 V").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_1))
        self.wait(2.5)
        b10_2 = MathTex(r"\frac{12}{4} = 3\ \text{A}, \quad \frac{12}{8} = 1{,}5\ \text{A}").scale(1.05).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_2))
        self.wait(2.5)
        b10_3 = MathTex(r"3 + 1{,}5 = 4{,}5\ \text{A total}").scale(1.05).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_3))
        self.wait(2)
        b10_4 = MathTex(r"\tfrac{1}{4} + \tfrac{1}{8} = \tfrac{3}{8} \; \text{(upside-down)}").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_4))
        self.wait(2.5)
        b10_5 = MathTex(r"\text{Flip back: } R_p = \tfrac{8}{3} = 2{,}67\ \Omega").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_5))
        self.play(Create(SurroundingRectangle(b10_5, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): why your house is wired the clever way ---
        self.next_band(11)
        b11_t = Tex("Why your house is wired in parallel").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_1a = MathTex(r"\text{1 road: } 12\ \Omega,\ 1\ \text{A}").scale(1.0).shift(band_shift(11) + UP * 1.3)
        self.play(Write(b11_1a))
        self.wait(1.5)
        b11_1b = MathTex(r"\text{2 roads: } 2{,}67\ \Omega,\ 4{,}5\ \text{A}").scale(1.0).shift(band_shift(11) + UP * 0.5)
        self.play(Write(b11_1b))
        self.wait(2)
        b11_2 = Tex("Each plug on its own branch: full 230 V").scale(1.0).shift(band_shift(11) + DOWN * 0.4)
        self.play(Write(b11_2))
        self.wait(2.5)
        b11_3 = Tex("Kettle off, lights stay on").scale(1.05).shift(band_shift(11) + DOWN * 1.2)
        self.play(Write(b11_3))
        self.wait(2)
        b11_4 = Tex("Price: every branch raises total $I$").scale(1.0).shift(band_shift(11) + DOWN * 2.0)
        self.play(Write(b11_4))
        self.wait(2)
        b11_5 = Tex("Wall switch: in SERIES with its light").scale(1.0).shift(band_shift(11) + DOWN * 2.9)
        self.play(Write(b11_5))
        self.play(Create(SurroundingRectangle(b11_5, color=GREEN)))
        self.wait(4)
