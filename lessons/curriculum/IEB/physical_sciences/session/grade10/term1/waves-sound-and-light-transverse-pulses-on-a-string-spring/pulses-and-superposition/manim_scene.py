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

# Band-layout whiteboard scene for "Pulses and Superposition" (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe mobjects
# only; write-only reveals; camera moves down band by band. Band time
# apportioned to subtopics.json (230/230/235/235/180/180/190 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PulsesSuperpositionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the pulse, drawn ---
        title = Tex("Pulses and Superposition").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("A pulse: ONE disturbance on the move").scale(1.05).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        # spring with a single hump (polyline) on a rest line
        rest1 = Line(LEFT * 4.5 + DOWN * 0.3, LEFT * 1.8 + DOWN * 0.3)
        hump = VGroup(
            Line(LEFT * 1.8 + DOWN * 0.3, LEFT * 0.9 + UP * 0.9, color=BLUE),
            Line(LEFT * 0.9 + UP * 0.9, RIGHT * 0.0 + DOWN * 0.3, color=BLUE),
        )
        rest2 = Line(RIGHT * 0.0 + DOWN * 0.3, RIGHT * 4.5 + DOWN * 0.3)
        self.play(Create(rest1), Create(rest2))
        self.play(Create(hump))
        trav = Arrow(RIGHT * 0.9 + UP * 0.7, RIGHT * 2.3 + UP * 0.7, buff=0, color=YELLOW)
        trav_lab = Tex("pulse travels").scale(0.8).shift(RIGHT * 1.6 + UP * 1.2)
        self.play(Create(trav), Write(trav_lab))
        self.wait(1.5)
        tape = Dot(LEFT * 3.1 + DOWN * 0.3, color=RED)
        up_ar = Arrow(LEFT * 3.1 + DOWN * 0.2, LEFT * 3.1 + UP * 0.8, buff=0, color=RED)
        tape_lab = Tex("tape lifts, then settles").scale(0.8).shift(LEFT * 3.1 + DOWN * 1.1)
        self.play(Create(tape), Create(up_ar), Write(tape_lab))
        self.wait(2)
        b0_l2 = Tex("medium moves at RIGHT ANGLES to travel").scale(1.0).shift(DOWN * 2.0)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the medium stays; the speed rule ---
        self.next_band(1)
        b1_t = Tex("What travels, and what stays home").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("the tape never creeps toward the far end").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("energy is transferred through the medium,").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("the medium itself stays put").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(VGroup(b1_l2, b1_l3), color=GREEN)))
        self.wait(2.5)
        b1_l4 = MathTex(r"v = \frac{8}{4} = 2\;\text{m·s}^{-1}").scale(1.1).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("set by the MEDIUM — hard jerk or soft").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): amplitude, measured properly ---
        self.next_band(2)
        b2_t = Tex("Amplitude: max displacement from rest").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        rest = DashedLine(band_shift(2) + LEFT * 4.0 + UP * 0.2, band_shift(2) + RIGHT * 4.0 + UP * 0.2)
        rest_lab = Tex("rest position").scale(0.8).shift(band_shift(2) + LEFT * 3.2 + UP * 0.7)
        self.play(Create(rest), Write(rest_lab))
        hump2 = VGroup(
            Line(band_shift(2) + LEFT * 1.4 + UP * 0.2, band_shift(2) + LEFT * 0.4 + UP * 1.7, color=BLUE),
            Line(band_shift(2) + LEFT * 0.4 + UP * 1.7, band_shift(2) + RIGHT * 0.6 + UP * 0.2, color=BLUE),
        )
        self.play(Create(hump2))
        amp = Arrow(band_shift(2) + RIGHT * 1.4 + UP * 0.2, band_shift(2) + RIGHT * 1.4 + UP * 1.7,
                    buff=0, color=GREEN)
        amp_lab = MathTex(r"0{,}4\;\text{m}").scale(0.9).shift(band_shift(2) + RIGHT * 2.4 + UP * 0.95)
        self.play(Create(amp), Write(amp_lab))
        self.wait(2)
        b2_l1 = Tex("up is positive; a dip 0,25 m below rest").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        b2_l2 = Tex("is negative displacement, amplitude 0,25 m").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("never measured dip-to-crest").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l3))
        self.play(Create(strike(b2_l3)))
        self.wait(3)

        # --- Band 3 (subtopic_2): amplitude is energy, not speed ---
        self.next_band(3)
        b3_t = Tex("Amplitude is the receipt for ENERGY").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("harder jerk, more energy, taller hump").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("giant and ripple travel SIDE BY SIDE").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"t = \frac{5}{2} = 2{,}5\;\text{s}").scale(1.1).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex("friction bleeds energy: amplitude shrinks,").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        b3_l5 = Tex("speed does not change").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the principle, with sums ---
        self.next_band(4)
        b4_t = Tex("The principle of superposition").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("same point, same instant: displacements").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("add ALGEBRAICALLY — signs included").scale(1.0).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"+0{,}4 + 0{,}2 = 0{,}6\;\text{m}").scale(1.1).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = MathTex(r"+0{,}4 + (-0{,}1) = 0{,}3\;\text{m}").scale(1.1).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): pulses survive the meeting ---
        self.next_band(5)
        b5_t = Tex("After the overlap: both pulses survive").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("each emerges with its own shape,").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("amplitude and direction — untouched").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(VGroup(b5_l1, b5_l2), color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("a shared moment of space, not a crash").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("two stages: DURING — add with signs;").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        b5_l5 = Tex("AFTER — redraw both, unchanged").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): constructive interference ---
        self.next_band(6)
        b6_t = Tex("Constructive: same direction, reinforced").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"0{,}4 + 0{,}2 = 0{,}6\;\text{m tall}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2)
        b6_l2 = MathTex(r"(-0{,}15) + (-0{,}15) = -0{,}3\;\text{m}").scale(1.05).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("two troughs are ALSO constructive:").scale(1.0).shift(band_shift(6) + DOWN * 1.0)
        b6_l4 = Tex("the disturbances build each other up").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): destructive, and the flat-spring trick ---
        self.next_band(7)
        b7_t = Tex("Destructive: opposite directions cancel").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"0{,}4 + (-0{,}1) = 0{,}3\;\text{m}").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"0{,}3 + (-0{,}3) = 0").scale(1.05).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex("spring momentarily FLAT — but flat").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        b7_l4 = Tex("is not empty: both re-emerge whole").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("signs in, one sum, restore both pulses").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the washing line ---
        self.next_band(8)
        b8_t = Tex("One flick of the washing line").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("one hump runs the whole line, past every peg").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("each peg hops up and settles back —").scale(1.0).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex("the line itself never leaves the yard").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = MathTex(r"10\;\text{m in } 5\;\text{s} = 2\;\text{m every second}").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("faster pulse? winch the line tighter").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): two bumps meet ---
        self.next_band(9)
        b9_t = Tex("When two bumps meet in the middle").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"25\;\text{cm} + 15\;\text{cm} = 40\;\text{cm}").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.play(Create(SurroundingRectangle(b9_l1, color=GREEN)))
        self.wait(2)
        b9_l2 = Tex("the rope obeys both flicks at once").scale(1.0).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("then: through each other like two songs").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        b9_l4 = Tex("crossing the same room, unmixed").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("two scenes: add, then stroll on unchanged").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): adding heights with signs ---
        self.next_band(10)
        b10_t = Tex("Adding heights with signs").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("up meets down: staircase arithmetic").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = MathTex(r"+30 - 10 = +20\;\text{cm}").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2)
        b10_l3 = MathTex(r"+20 - 20 = 0 \;\; \text{dead flat}").scale(1.05).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("flat is NOT empty: hump and dip pop out,").scale(1.0).shift(band_shift(10) + DOWN * 1.8)
        b10_l5 = Tex("both perfect, both still travelling").scale(1.0).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
