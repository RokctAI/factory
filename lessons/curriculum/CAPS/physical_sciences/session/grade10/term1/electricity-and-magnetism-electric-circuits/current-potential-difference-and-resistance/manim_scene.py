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

# Band-layout whiteboard scene for the session duo "Current, Potential
# Difference and Resistance" (Part 1 Expert subtopics 1-4, Part 2 Simplifier
# subtopics 5-7). Exporter-safe vocabulary only: Tex/MathTex/Line/Arrow/Dot/
# Circle/Rectangle/SurroundingRectangle/VGroup, write-only reveals, camera
# moves down band by band. Band time is apportioned to subtopics.json
# (230/235/230/240/180/180/190 of 1485 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CurrentPdResistanceSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): current defined ---
        title = Tex("Current, Potential Difference, Resistance").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Current: rate of flow of charge").scale(1.15).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"I = \frac{Q}{\Delta t}").scale(1.3).shift(DOWN * 0.2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex(r"$I$ in A, $Q$ in C, $\Delta t$ in s").scale(1.1).shift(DOWN * 1.4)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = MathTex(r"1\;\text{A} = 1\;\text{C per second}").scale(1.1).shift(DOWN * 2.4)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): both worked examples + direction ---
        self.next_band(1)
        b1_t = Tex("Work the definition both ways").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"I = \frac{Q}{\Delta t} = \frac{30}{10}").scale(1.1).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"I = 3\;\text{A}").scale(1.15).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = Tex(r"Charger: 0,5 A for 2 min $= 120$ s").scale(1.05).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"Q = I \times \Delta t = 0{,}5 \times 120 = 60\;\text{C}").scale(1.05).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex(r"Conventional current: $+$ to $-$ outside").scale(1.05).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): V = W/Q worked ---
        self.next_band(2)
        b2_t = Tex("Potential difference: energy per coulomb").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"V = \frac{W}{Q}").scale(1.3).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"1\;\text{V} = 1\;\text{J per C}").scale(1.1).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"V = \frac{24}{8} = 3\;\text{V}").scale(1.1).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = MathTex(r"W = V \times Q = 12 \times 5 = 60\;\text{J}").scale(1.05).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): emf vs terminal pd ---
        self.next_band(3)
        b3_t = Tex("Emf vs terminal potential difference").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("Emf: reading with NO current flowing").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("the open-circuit promise per coulomb").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Terminal pd: reading while delivering").scale(1.05).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"\text{terminal pd} < \text{emf}").scale(1.1).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex(r"9 V on the shelf, 8,5 V driving a motor").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the circuit diagram, built element by element ---
        self.next_band(4)
        b4_t = Tex("Ammeter in series, voltmeter in parallel").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        # battery on the top wire
        battery = Rectangle(width=1.2, height=0.5).shift(band_shift(4) + UP * 1.2)
        bat_lab = Tex("battery").scale(0.8).shift(band_shift(4) + UP * 1.85)
        self.play(Create(battery), Write(bat_lab))
        self.wait(1.5)
        # loop wires
        w1 = Line(band_shift(4) + UP * 1.2 + LEFT * 0.6, band_shift(4) + UP * 1.2 + LEFT * 3.0)
        w2 = Line(band_shift(4) + UP * 1.2 + LEFT * 3.0, band_shift(4) + DOWN * 1.2 + LEFT * 3.0)
        w3 = Line(band_shift(4) + DOWN * 1.2 + LEFT * 3.0, band_shift(4) + DOWN * 1.2 + LEFT * 0.7)
        w4 = Line(band_shift(4) + UP * 1.2 + RIGHT * 0.6, band_shift(4) + UP * 1.2 + RIGHT * 3.0)
        w5 = Line(band_shift(4) + UP * 1.2 + RIGHT * 3.0, band_shift(4) + RIGHT * 3.0 + UP * 0.35)
        self.play(Create(w1), Create(w2), Create(w3))
        self.play(Create(w4), Create(w5))
        self.wait(1.5)
        # ammeter spliced into the right-hand wire (series)
        ammeter = Circle(radius=0.35, color=WHITE).shift(band_shift(4) + RIGHT * 3.0)
        am_lab = Tex("A").scale(0.9).shift(band_shift(4) + RIGHT * 3.0)
        w6 = Line(band_shift(4) + RIGHT * 3.0 + DOWN * 0.35, band_shift(4) + RIGHT * 3.0 + DOWN * 1.2)
        w7 = Line(band_shift(4) + RIGHT * 3.0 + DOWN * 1.2, band_shift(4) + RIGHT * 0.7 + DOWN * 1.2)
        self.play(Create(ammeter), Write(am_lab))
        self.play(Create(w6), Create(w7))
        self.wait(2)
        # resistor on the bottom wire
        resistor = Rectangle(width=1.4, height=0.5).shift(band_shift(4) + DOWN * 1.2)
        r_lab = Tex("R").scale(0.9).shift(band_shift(4) + DOWN * 0.6)
        self.play(Create(resistor), Write(r_lab))
        self.wait(1.5)
        # voltmeter across the resistor (parallel)
        voltmeter = Circle(radius=0.35, color=WHITE).shift(band_shift(4) + DOWN * 2.5)
        v_lab = Tex("V").scale(0.9).shift(band_shift(4) + DOWN * 2.5)
        v1 = Line(band_shift(4) + DOWN * 1.45 + LEFT * 0.7, band_shift(4) + DOWN * 2.5 + LEFT * 0.35)
        v2 = Line(band_shift(4) + DOWN * 1.45 + RIGHT * 0.7, band_shift(4) + DOWN * 2.5 + RIGHT * 0.35)
        self.play(Create(v1), Create(v2))
        self.play(Create(voltmeter), Write(v_lab))
        self.wait(2)
        # conventional current arrow on the top-left wire
        cur = Arrow(band_shift(4) + UP * 0.7 + LEFT * 1.2, band_shift(4) + UP * 0.7 + LEFT * 2.4, buff=0, color=YELLOW)
        cur_lab = Tex("I").scale(0.8).shift(band_shift(4) + UP * 0.35 + LEFT * 1.8)
        self.play(Create(cur), Write(cur_lab))
        self.wait(3)

        # --- Band 5 (subtopic_3): the connection rules and the swap disaster ---
        self.next_band(5)
        b5_t = Tex("The meter rules").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("Ammeter: in series, very LOW resistance").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Voltmeter: in parallel, very HIGH resistance").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Voltmeter in series: circuit throttled").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.play(Create(strike(b5_l3)))
        self.wait(2)
        b5_l4 = Tex("Ammeter in parallel: short circuit!").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.play(Create(strike(b5_l4)))
        self.wait(2)
        b5_l5 = Tex("Always quote the unit you read").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): resistance and the collision picture ---
        self.next_band(6)
        b6_t = Tex("Resistance: opposition to charge flow").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"1\;\Omega : 1\;\text{V drives } 1\;\text{A}").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        # wire cross-section: lattice ions as dots, electron path as arrow
        wire = Rectangle(width=5.0, height=1.4).shift(band_shift(6) + DOWN * 0.3)
        self.play(Create(wire))
        ions = VGroup(*[
            Dot(band_shift(6) + DOWN * 0.3 + RIGHT * x + UP * y, radius=0.07, color=BLUE)
            for x in (-1.8, -0.6, 0.6, 1.8) for y in (0.4, -0.4)
        ])
        self.play(Create(ions))
        self.wait(1.5)
        e_arrow = Arrow(band_shift(6) + DOWN * 0.3 + LEFT * 2.9, band_shift(6) + DOWN * 0.3 + RIGHT * 2.9,
                        buff=0, color=YELLOW)
        self.play(Create(e_arrow))
        b6_l2 = Tex("electrons collide with vibrating ions").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("each collision transfers energy: HEAT").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l3))
        self.wait(3)

        # --- Band 7 (subtopic_4): the three factors ---
        self.next_band(7)
        b7_t = Tex("Three factors control resistance").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex(r"Longer wire $\Rightarrow$ more collisions, $R$ up").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex(r"Thicker wire $\Rightarrow$ more lanes, $R$ down").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"Hotter metal $\Rightarrow$ wilder ions, $R$ up").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Copper for wiring, nichrome for heating").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Long, thin, hot: high $R$").scale(1.1).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the water pump on the roof ---
        self.next_band(8)
        b8_t = Tex("The water pump on the roof").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Pump = battery: lifts every litre").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("1,5 V cell: 1,5 J packed into every coulomb").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Water returns to the pump — charge").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = Tex("is never used up, only its ENERGY").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(VGroup(b8_l3, b8_l4), color=GREEN)))
        self.wait(2.5)
        b8_l5 = Tex("Emf the promise, terminal pd the delivery").scale(1.0).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): counting heads at the gate ---
        self.next_band(9)
        b9_t = Tex("Counting heads at the gate").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Current = supporters through per second").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"\frac{30\;\text{C}}{10\;\text{s}} = 3\;\text{A}").scale(1.1).shift(band_shift(9) + UP * 0.0)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"0{,}5 \times 120 = 60\;\text{C}").scale(1.05).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Nobody vanishes in the turnstile:").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        b9_l5 = Tex("same current both sides of the bulb").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the narrow corridor ---
        self.next_band(10)
        b10_t = Tex("The narrow corridor").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Bumping through the crowd = collisions").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("Longer corridor: more bumps").scale(1.0).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(1.5)
        b10_l3 = Tex("Narrower corridor: more crowding").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(1.5)
        b10_l4 = Tex("Jittery crowd (hot): harder to cross").scale(1.0).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Long, thin and hot: maximum $R$").scale(1.05).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
