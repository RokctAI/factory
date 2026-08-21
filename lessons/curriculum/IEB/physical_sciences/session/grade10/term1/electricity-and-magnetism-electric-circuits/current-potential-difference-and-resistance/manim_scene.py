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

# Band-layout whiteboard scene for "Current, Potential Difference and
# Resistance" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects only; write-only reveals; camera moves down band by
# band. Band time apportioned to subtopics.json
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): current defined ---
        title = Tex("Current, Potential Difference, Resistance").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("current: RATE of flow of charge").scale(1.0).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"I = \frac{Q}{\Delta t}").scale(1.3).shift(UP * 0.2)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2)
        b0_l3 = Tex("one ampere: one coulomb per second").scale(0.95).shift(DOWN * 0.9)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("current is never used up —").scale(0.95).shift(DOWN * 1.8)
        b0_l5 = Tex("charge delivers energy and moves on").scale(0.95).shift(DOWN * 2.5)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): both worked examples + direction ---
        self.next_band(1)
        b1_t = Tex("Both directions, plus THE direction").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"I = \frac{40}{8} = 5\;\text{A}").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)
        b1_l2 = MathTex(r"Q = I\Delta t = 0{,}3 \times 300 = 90\;\text{C}").scale(1.0).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = Tex("5 minutes became 300 s FIRST").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("conventional current: + around to $-$;").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        b1_l5 = Tex("electrons drift the other way").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): V = W/Q worked ---
        self.next_band(2)
        b2_t = Tex("The volt: joules per coulomb").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"V = \frac{W}{Q}").scale(1.3).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2)
        b2_l2 = MathTex(r"V = \frac{36}{6} = 6\;\text{V}").scale(1.05).shift(band_shift(2) + DOWN * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = MathTex(r"W = VQ = 12 \times 4 = 48\;\text{J}").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("a 1,5 V cell: 1,5 J into every coulomb").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): emf vs terminal pd ---
        self.next_band(3)
        b3_t = Tex("Emf versus terminal pd").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("emf: reading with NO current —").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("the promise, measured at rest").scale(0.95).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("terminal pd: reading UNDER LOAD —").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = Tex("always slightly less").scale(0.95).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(VGroup(b3_l3, b3_l4), color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("12 V on the shelf, 11,4 V driving lights:").scale(0.9).shift(band_shift(3) + DOWN * 2.0)
        b3_l6 = Tex("the difference is spent inside the battery").scale(0.9).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): the circuit diagram, built element by element ---
        self.next_band(4)
        b4_t = Tex("The two meters, wired properly").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_t))
        self.wait(1.5)
        # simple loop: battery left, resistor right, ammeter in line, voltmeter across
        top = Line(band_shift(4) + LEFT * 3.5 + UP * 1.2, band_shift(4) + RIGHT * 3.5 + UP * 1.2)
        bottom = Line(band_shift(4) + LEFT * 3.5 + DOWN * 1.2, band_shift(4) + RIGHT * 3.5 + DOWN * 1.2)
        left = Line(band_shift(4) + LEFT * 3.5 + UP * 1.2, band_shift(4) + LEFT * 3.5 + DOWN * 1.2)
        right = Line(band_shift(4) + RIGHT * 3.5 + UP * 1.2, band_shift(4) + RIGHT * 3.5 + DOWN * 1.2)
        self.play(Create(top), Create(bottom), Create(left), Create(right))
        batt = Tex("battery").scale(0.75).shift(band_shift(4) + LEFT * 4.4 + UP * 0.0)
        amm = Circle(radius=0.45, color=YELLOW).shift(band_shift(4) + UP * 1.2 + LEFT * 0.0)
        amm_lab = Tex("A").scale(0.8).shift(band_shift(4) + UP * 1.2)
        res = Tex("resistor").scale(0.75).shift(band_shift(4) + RIGHT * 4.5 + UP * 0.0)
        self.play(Write(batt), Create(amm), Write(amm_lab), Write(res))
        volt = Circle(radius=0.45, color=BLUE).shift(band_shift(4) + RIGHT * 2.2 + DOWN * 0.0)
        volt_lab = Tex("V").scale(0.8).shift(band_shift(4) + RIGHT * 2.2)
        v_l1 = Line(band_shift(4) + RIGHT * 2.2 + UP * 0.45, band_shift(4) + RIGHT * 3.5 + UP * 1.2)
        v_l2 = Line(band_shift(4) + RIGHT * 2.2 + DOWN * 0.45, band_shift(4) + RIGHT * 3.5 + DOWN * 1.2)
        self.play(Create(volt), Write(volt_lab), Create(v_l1), Create(v_l2))
        self.wait(2)
        b4_l1 = Tex("A in the line; V across the ends").scale(0.95).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the connection rules and the swap disaster ---
        self.next_band(5)
        b5_t = Tex("The rules, and the swap disaster").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("ammeter: series, VERY LOW resistance").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("voltmeter: parallel, VERY HIGH resistance").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(VGroup(b5_l1, b5_l2), color=GREEN)))
        self.wait(2)
        b5_l3 = Tex("voltmeter in series: circuit strangled").scale(0.95).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l3))
        self.play(Create(strike(b5_l3)))
        self.wait(2)
        b5_l4 = Tex("ammeter in parallel: short circuit").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l4))
        self.play(Create(strike(b5_l4)))
        self.wait(2)
        b5_l5 = Tex("read the scale, quote the unit").scale(0.9).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): resistance and the collision picture ---
        self.next_band(6)
        b6_t = Tex("Resistance: the collision story").scale(1.1).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_t))
        self.wait(1.5)
        # lattice of ions with an electron path
        ions = VGroup(*[Dot(band_shift(6) + LEFT * 3.0 + RIGHT * 1.5 * i + UP * (1.0 - 0.9 * j), color=BLUE)
                        for i in range(5) for j in range(2)])
        self.play(Create(ions))
        path = VGroup(
            Line(band_shift(6) + LEFT * 3.6 + UP * 0.6, band_shift(6) + LEFT * 2.2 + UP * 0.05, color=YELLOW),
            Line(band_shift(6) + LEFT * 2.2 + UP * 0.05, band_shift(6) + LEFT * 0.8 + UP * 0.7, color=YELLOW),
            Line(band_shift(6) + LEFT * 0.8 + UP * 0.7, band_shift(6) + RIGHT * 0.7 + UP * 0.0, color=YELLOW),
            Line(band_shift(6) + RIGHT * 0.7 + UP * 0.0, band_shift(6) + RIGHT * 2.2 + UP * 0.65, color=YELLOW),
            Line(band_shift(6) + RIGHT * 2.2 + UP * 0.65, band_shift(6) + RIGHT * 3.6 + UP * 0.1, color=YELLOW),
        )
        self.play(Create(path))
        self.wait(2)
        b6_l1 = Tex("electrons collide with vibrating ions —").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        b6_l2 = Tex("every collision hands over energy as HEAT").scale(0.95).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        b6_l3 = Tex("one ohm: one volt drives one ampere").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l3))
        self.wait(3)

        # --- Band 7 (subtopic_4): the three factors ---
        self.next_band(7)
        b7_t = Tex("The three dials of resistance").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("LENGTH: double it, double R").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("THICKNESS: fatter wire, more lanes, lower R").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("TEMPERATURE: hotter metal, more collisions, higher R").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex("copper for wiring; nichrome for kettles").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_l4))
        b7_l5 = Tex("long, thin, hot: high — short, thick, cool: low").scale(0.9).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the water pump on the roof ---
        self.next_band(8)
        b8_t = Tex("The water pump on the roof").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("pump lifts water: battery loads coulombs").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("volts: the size of each energy parcel").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2)
        b8_l3 = Tex("water is never used up — neither is charge").scale(0.95).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("flat battery: the lifting power gave out").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        b8_l5 = Tex("drag in the pump: why delivery < promise").scale(0.9).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): counting heads at the gate ---
        self.next_band(9)
        b9_t = Tex("Counting heads at the gate").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("current: clicks per second at the turnstile").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.play(Create(SurroundingRectangle(b9_l1, color=GREEN)))
        self.wait(2)
        b9_l2 = MathTex(r"40\ \text{coulombs in } 8\ \text{s} = 5\;\text{A}").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("nobody vanishes in the turnstile:").scale(0.95).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = Tex("same current both sides of the bulb").scale(0.95).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("the official arrow: + around to $-$").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the narrow corridor ---
        self.next_band(10)
        b10_t = Tex("The narrow corridor").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("bumping through the break-time crowd:").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("every bump costs energy — that is heat").scale(0.95).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("longer, narrower, jitterier: harder corridor").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = Tex("copper: the calm hallway — nichrome:").scale(0.95).shift(band_shift(10) + DOWN * 1.5)
        b10_l5 = Tex("the obstacle course, hot on purpose").scale(0.95).shift(band_shift(10) + DOWN * 2.3)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
