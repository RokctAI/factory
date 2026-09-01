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

# Band-layout whiteboard scene for the Magnetic Fields and Faraday's Law duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (240/230/230/235/185/175/195
# of 1490 s). Exporter-safe mobjects only (fields from Circles/Arrows/Lines);
# add-only lifecycle; camera bands.

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
        wire = Line(LEFT * 3.2 + DOWN * 0.6, LEFT * 3.2 + UP * 0.9, stroke_width=6)
        cur = Arrow(LEFT * 3.2 + DOWN * 0.55, LEFT * 3.2 + UP * 0.85, buff=0, color=YELLOW)
        c1 = Circle(radius=0.45, color=BLUE).shift(LEFT * 3.2 + UP * 0.15)
        c2 = Circle(radius=0.85, color=BLUE).shift(LEFT * 3.2 + UP * 0.15)
        lw = Tex("field circles the wire").scale(0.85).shift(LEFT * 0.4 + UP * 0.15)
        self.play(Create(wire), Create(cur))
        self.play(Create(c1), Create(c2), Write(lw))
        self.wait(2.5)
        b0_l2 = Tex("Right Hand Rule: thumb along the current,").scale(0.95).shift(DOWN * 1.5)
        b0_l3 = Tex("curled fingers give the field direction").scale(0.95).shift(DOWN * 2.2)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(VGroup(b0_l2, b0_l3), color=BLUE)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): loops, solenoids, electromagnets ---
        self.next_band(1)
        b1_title = Tex("Loops and solenoids").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        coils = VGroup(*[Circle(radius=0.4, color=WHITE).shift(RIGHT * (0.9 * i) + LEFT * 3.4 + UP * 1.0)
                         for i in range(6)])
        coils.shift(band_shift(1))
        axis = Arrow(LEFT * 4.4 + UP * 1.0, RIGHT * 2.6 + UP * 1.0, buff=0, color=YELLOW).shift(band_shift(1))
        lN = Tex("N").scale(0.95).shift(band_shift(1) + RIGHT * 3.1 + UP * 1.0)
        lS = Tex("S").scale(0.95).shift(band_shift(1) + LEFT * 5.0 + UP * 1.0)
        self.play(Create(coils))
        self.play(Create(axis), Write(lN), Write(lS))
        self.wait(2)
        b1_l1 = Tex("Fingers with the winding current;").scale(0.95).shift(band_shift(1) + DOWN * 0.2)
        b1_l2 = Tex("thumb points to the NORTH end").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Iron core: stronger. Current off: lets go —").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        b1_l4 = Tex("scrapyard cranes, relays, electric bells").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): magnetic flux ---
        self.next_band(2)
        b2_title = Tex("Magnetic flux: field through a surface").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\phi = BA\cos\theta").scale(1.3).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=BLUE)))
        self.wait(2.5)
        b2_l2 = Tex(r"$\theta$ is against the NORMAL, not the surface").scale(0.95).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex(r"Field along the normal: $\cos 0 = 1$, maximum").scale(0.95).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex(r"Field in the plane: $\cos 90^\circ = 0$, nothing").scale(0.95).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex(r"Unit: weber; 1 Wb $=$ 1 T$\cdot$m$^2$").scale(0.95).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): flux worked ---
        self.next_band(3)
        b3_title = Tex(r"Coil of 0,05 m$^2$ in a 0,4 T field").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\phi = 0{,}4 \times 0{,}05 \times \cos 0").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\phi = 0{,}02\ \text{Wb}").scale(1.1).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = MathTex(r"\text{Tilt to } 60^\circ: \; 0{,}4 \times 0{,}05 \times 0{,}5").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"\phi = 0{,}01\ \text{Wb — half, from angle alone}").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("A rotating coil changes flux — a generator").scale(0.95).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): Faraday's law ---
        self.next_band(4)
        b4_title = Tex("Faraday: motion, not presence").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        mag = Rectangle(width=1.4, height=0.6).shift(band_shift(4) + LEFT * 3.6 + UP * 1.1)
        lmag = Tex("N").scale(0.85).shift(band_shift(4) + LEFT * 3.1 + UP * 1.1)
        amove = Arrow(LEFT * 2.7 + UP * 1.1, LEFT * 1.5 + UP * 1.1, buff=0, color=YELLOW).shift(band_shift(4))
        coil2 = VGroup(*[Circle(radius=0.35, color=WHITE).shift(RIGHT * (0.55 * i) + LEFT * 0.6 + UP * 1.1)
                         for i in range(4)])
        coil2.shift(band_shift(4))
        lcoil = Tex("coil").scale(0.8).shift(band_shift(4) + RIGHT * 0.3 + UP * 2.0)
        self.play(Create(mag), Write(lmag))
        self.play(Create(amove), Create(coil2), Write(lcoil))
        self.wait(2)
        b4_l1 = Tex("Moving in: needle kicks. Held still: zero.").scale(0.95).shift(band_shift(4) + DOWN * 0.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("emf $\\propto$ rate of change of magnetic flux").scale(1.0).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=BLUE)))
        self.wait(2.5)
        b4_l3 = Tex("Faster change, stronger magnet, more turns:").scale(0.95).shift(band_shift(4) + DOWN * 2.1)
        b4_l4 = Tex("bigger emf").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the opposition ---
        self.next_band(5)
        b5_title = Tex("The induced current OPPOSES the change").scale(1.1).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Push a north pole in: the face turns NORTH,").scale(0.95).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("repelling the arrival").scale(0.95).shift(band_shift(5) + UP * 0.6)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Pull it out: the face turns SOUTH, clinging").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex("Your work against the fight becomes").scale(0.95).shift(band_shift(5) + DOWN * 1.4)
        b5_l5 = Tex("the electrical energy — nothing is free").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the emf calculation ---
        self.next_band(6)
        b6_title = Tex(r"200 turns, 0,03 m$^2$; B: 0,2 to 0,8 T in 0,5 s").scale(1.0).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{emf} = N\frac{\Delta\phi}{\Delta t}").scale(1.15).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=BLUE)))
        self.wait(2.5)
        b6_l2 = MathTex(r"\phi_i = 0{,}2 \times 0{,}03 = 0{,}006\ \text{Wb}").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"\phi_f = 0{,}8 \times 0{,}03 = 0{,}024\ \text{Wb}").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"\Delta\phi = 0{,}024 - 0{,}006 = 0{,}018\ \text{Wb}").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = MathTex(r"\text{emf} = \frac{200 \times 0{,}018}{0{,}5} = 7{,}2\ \text{V}").scale(1.05).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the current, and the traps ---
        self.next_band(7)
        b7_l0 = Tex(r"Closed circuit of 3,6 $\Omega$:").scale(0.95).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_l0))
        self.wait(1.5)
        b7_l1 = MathTex(r"I = \frac{7{,}2}{3{,}6} = 2\ \text{A}").scale(1.05).shift(band_shift(7) + UP * 1.5)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(2.5)
        b7_trap = Tex(r"using $B$ instead of $\Delta\phi$").scale(1.0).shift(band_shift(7) + UP * 0.8)
        self.play(Write(b7_trap))
        self.play(Create(strike(b7_trap)))
        self.wait(2)
        b7_l2 = Tex("Compute both fluxes, then subtract").scale(0.95).shift(band_shift(7) + DOWN * 0.1)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"Never forget $N$, or $\cos\theta$ off the normal").scale(0.95).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex(r"Area in m$^2$ — convert cm before multiplying").scale(0.95).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.wait(2.5)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the compass that flinched ---
        self.next_band(8)
        b8_title = Tex("The compass that flinched").scale(1.2).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("1820: current on, the needle jumps —").scale(0.95).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("a wire moving a magnet without touching it").scale(0.95).shift(band_shift(8) + UP * 0.6)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Coil the wire: a bar magnet made of electricity").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Unlike any bar magnet, it switches OFF —").scale(0.95).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = Tex("the crane carries the car, then lets go").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): rain through the bucket ---
        self.next_band(9)
        b9_title = Tex("How much field fits through the window?").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Field is rain; the loop is a bucket rim").scale(0.95).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"Facing the rain: full catch. Edge-on: nothing").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"0{,}02 \to 0{,}01 \to 0\ \text{Wb as it tilts}").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Nature only pays when the count CHANGES").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): change makes electricity ---
        self.next_band(10)
        b10_title = Tex("Change makes electricity").scale(1.2).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Eleven years of resting magnets: zero").scale(0.95).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Faraday: MOVE it — current every time").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Faster change and more turns: bigger push").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("The current always fights the change —").scale(0.95).shift(band_shift(10) + DOWN * 1.4)
        b10_l5 = Tex("you pay in effort, nature pays in current").scale(0.95).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex("Every power station: coils spinning in fields").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
