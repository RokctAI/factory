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

# Band-layout whiteboard scene for the Magnetic Fields and Faraday's Law duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (240/230/230/235/185/175/195
# of 1490 s). Exporter-safe mobjects only (wires and coils drawn from Lines,
# Circles and Tex labels); add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MagneticFieldsFaradaysLawSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): Oersted and the Right Hand Rule ---
        title = Tex("Magnetic Fields and Faraday's Law").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("A current wraps itself in a magnetic field").scale(1.0).shift(UP * 1.4)
        self.play(Write(b0_l1))
        self.wait(2.5)
        wire = Line(LEFT * 3.0 + DOWN * 0.4, RIGHT * 3.0 + DOWN * 0.4, color=YELLOW)
        c1 = Circle(radius=0.4, color=BLUE).shift(LEFT * 1.5 + DOWN * 0.4)
        c2 = Circle(radius=0.7, color=BLUE).shift(LEFT * 1.5 + DOWN * 0.4)
        c3 = Circle(radius=0.4, color=BLUE).shift(RIGHT * 1.5 + DOWN * 0.4)
        c4 = Circle(radius=0.7, color=BLUE).shift(RIGHT * 1.5 + DOWN * 0.4)
        self.play(Create(wire))
        self.play(Create(c1), Create(c2), Create(c3), Create(c4))
        self.wait(2)
        b0_l2 = Tex("Concentric circles, tighter near the wire").scale(0.9).shift(DOWN * 1.7)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Right hand: thumb = current, fingers = field").scale(0.95).shift(DOWN * 2.7)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=BLUE)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): loops, solenoids, electromagnets ---
        self.next_band(1)
        b1_title = Tex("Loop, solenoid, electromagnet").scale(1.1).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        loops = VGroup(*[Circle(radius=0.45, color=YELLOW).shift(RIGHT * (0.55 * i - 1.65))
                         for i in range(6)])
        loops.shift(band_shift(1) + UP * 0.9)
        self.play(Create(loops))
        axis = Arrow(LEFT * 3.2 + UP * 0.9, RIGHT * 3.2 + UP * 0.9, buff=0, color=GREEN)
        axis.shift(band_shift(1))
        self.play(Create(axis))
        lN = Tex("N").scale(0.9).shift(band_shift(1) + RIGHT * 3.6 + UP * 0.9)
        lS = Tex("S").scale(0.9).shift(band_shift(1) + LEFT * 3.6 + UP * 0.9)
        self.play(Write(lN), Write(lS))
        self.wait(2)
        b1_l1 = Tex("Inside: strong, uniform, along the axis").scale(0.9).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Curl fingers with the winding current: thumb finds north").scale(0.85).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Iron core strengthens it — and it switches OFF").scale(0.9).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): magnetic flux ---
        self.next_band(2)
        b2_title = Tex("Magnetic flux: field through a surface").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\Phi = BA\cos\theta").scale(1.3).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=BLUE)))
        self.wait(2.5)
        b2_l2 = Tex(r"$\theta$ measured from the NORMAL, never the surface").scale(0.9).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\theta = 0^\circ: \; \cos\theta = 1 \; \text{(maximum)}").scale(0.95).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"\theta = 90^\circ: \; \cos\theta = 0 \; \text{(nothing through)}").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Unit: the weber — one tesla square metre").scale(0.9).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): flux worked ---
        self.next_band(3)
        b3_title = Tex(r"Coil: 0,02 m$^2$ in a 0,6 T field").scale(1.05).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Along the normal: } 0{,}6 \times 0{,}02 \times 1 = 0{,}012\ \text{Wb}").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"\text{Normal at } 60^\circ: \; 0{,}6 \times 0{,}02 \times 0{,}5 = 0{,}006\ \text{Wb}").scale(0.95).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Same coil, same field — half the flux from tilt alone").scale(0.9).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex("A generator is a coil changing its tilt forever").scale(0.9).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): Faraday's law ---
        self.next_band(4)
        b4_title = Tex("Faraday: motion, not presence").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Magnet in: needle kicks").scale(0.9).shift(band_shift(4) + UP * 1.3)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("Magnet still: zero").scale(0.9).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("Magnet out: kicks the other way").scale(0.9).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("emf $\\propto$ rate of change of flux").scale(1.0).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=BLUE)))
        self.wait(2.5)
        b4_l5 = Tex("Faster change, stronger magnet, more turns: bigger emf").scale(0.85).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the opposition ---
        self.next_band(5)
        b5_title = Tex("The induced current OPPOSES the change").scale(1.05).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.play(Create(SurroundingRectangle(b5_title, color=GREEN)))
        self.wait(2)
        b5_l1 = Tex("North pole approaches: face turns NORTH — pushes back").scale(0.85).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex("Magnet withdraws: face turns SOUTH — clings").scale(0.85).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Helping instead would mean energy from nothing").scale(0.9).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex("Your work against the opposition IS the electrical energy").scale(0.85).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the emf calculation ---
        self.next_band(6)
        b6_title = MathTex(r"\varepsilon = -N\,\frac{\Delta\Phi}{\Delta t}").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.play(Create(SurroundingRectangle(b6_title, color=BLUE)))
        self.wait(2.5)
        b6_l1 = Tex(r"150 turns, 0,04 m$^2$, field 0,1 T $\rightarrow$ 0,5 T in 0,4 s").scale(0.85).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\Phi_i = 0{,}1 \times 0{,}04 = 0{,}004\ \text{Wb}").scale(0.95).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"\Phi_f = 0{,}5 \times 0{,}04 = 0{,}02\ \text{Wb}").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"\Delta\Phi = 0{,}02 - 0{,}004 = 0{,}016\ \text{Wb}").scale(0.95).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = MathTex(r"\varepsilon = \frac{150 \times 0{,}016}{0{,}4} = 6\ \text{V}").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): the current, and the traps ---
        self.next_band(7)
        b7_l1 = MathTex(r"I = \frac{\varepsilon}{R} = \frac{6}{2{,}4} = 2{,}5\ \text{A}").scale(1.1).shift(band_shift(7) + UP * 2.0)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(2.5)
        b7_l2 = Tex("Trap 1: forgetting N — 150 turns, 150 times the emf").scale(0.85).shift(band_shift(7) + UP * 0.8)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Trap 2: using B where $\Delta\Phi$ belongs — subtract fluxes").scale(0.85).shift(band_shift(7) + DOWN * 0.2)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex(r"Trap 3: dropping $\cos\theta$ off the normal").scale(0.85).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Trap 4: areas must be square METRES before multiplying").scale(0.85).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the compass that flinched ---
        self.next_band(8)
        b8_title = Tex("The compass that flinched — 1820").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Current on: the needle jumps. Off: it rests").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Every current wears a magnetic coat").scale(0.95).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=BLUE)))
        self.wait(2.5)
        b8_l3 = Tex("Coil the wire: a bar magnet made of electricity").scale(0.9).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("With a switch — the crane can let go").scale(0.9).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): rain through the bucket ---
        self.next_band(9)
        b9_title = Tex("How much field fits through the window?").scale(1.05).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Rain = field strength").scale(0.9).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Bucket mouth = area").scale(0.9).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Tilt = the cosine factor, one down to zero").scale(0.9).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Edge-on: not a drop, however hard it pours").scale(0.9).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("Nature pays only when the count CHANGES").scale(0.95).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): change makes electricity ---
        self.next_band(10)
        b10_title = Tex("Change makes electricity").scale(1.2).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Eleven years of resting magnets: zero").scale(0.9).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Moving magnet: current, every time").scale(0.9).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex("Faster change and more turns: bigger push").scale(0.9).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("The current always fights back — that is the price").scale(0.9).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("Power stations: coils spinning in fields, all day long").scale(0.9).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l5))
        self.wait(4)
