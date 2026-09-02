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

# Band-layout whiteboard scene for "Vectors and Scalars" (Part 1 — Expert:
# subtopics 1-4; Part 2 — Simplifier: subtopics 5-7). Exporter-safe mobjects
# only, add-only lifecycle, one band per teaching beat. Band time apportioned
# to subtopics.json (210/230/230/270/170/180/170 of 1460 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class VectorsAndScalarsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): two kinds of quantities ---
        title = Tex("Vectors and Scalars").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Scalar: magnitude $+$ unit — complete").scale(1.1).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = Tex("mass, time, temperature, distance, energy").scale(1.0).shift(UP * 0.0)
        self.play(Write(d2))
        self.wait(2)
        d3 = Tex("Vector: magnitude AND direction").scale(1.1).shift(DOWN * 1.1)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex("The test: is a direction NEEDED?").scale(1.1).shift(DOWN * 2.2)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): two kinds of arithmetic ---
        self.next_band(1)
        b1t = Tex("Why the split? Different arithmetic").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"4 \text{ kg} + 3 \text{ kg} = 7 \text{ kg, always}").scale(1.1).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1a))
        self.wait(2.5)
        b1b = Tex(r"Vectors can strengthen, partly cancel, vanish").scale(1.05).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = MathTex(r"40 \text{ N} + 70 \text{ N} \neq 110 \text{ N (necessarily)}").scale(1.05).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1c))
        self.wait(2)
        b1d = Tex("Scalar arithmetic on vectors: the deep error").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1d))
        self.wait(3)

        # --- Band 2 (subtopic_2): classifying the five ---
        self.next_band(2)
        b2t = Tex("Classify the five — with reasons").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("Displacement: from-to $\\Rightarrow$ VECTOR").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2a))
        self.wait(2)
        b2b = Tex("Speed: speedometer, no pointing $\\Rightarrow$ SCALAR").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2b))
        self.wait(2)
        b2c = Tex("Force: gate pushed open $\\neq$ pulled shut $\\Rightarrow$ VECTOR").scale(0.95).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2c))
        self.wait(2)
        b2d = Tex("Energy: joules aim nowhere $\\Rightarrow$ SCALAR").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2d))
        self.wait(2)
        b2e = Tex("Velocity: speed $+$ direction $\\Rightarrow$ VECTOR").scale(1.0).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2e))
        self.wait(3)

        # --- Band 3 (subtopic_2): the famous pairs on one loop ---
        self.next_band(3)
        b3t = Tex("The famous pairs: one 600 m loop").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = MathTex(r"\text{Distance} = 600 \text{ m}").scale(1.1).shift(band_shift(3) + UP * 1.0)
        self.play(Write(b3a))
        self.wait(2)
        b3b = MathTex(r"\text{Displacement} = 0 \text{ (start = finish)}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3b))
        self.play(Create(SurroundingRectangle(b3b, color=GREEN)))
        self.wait(2.5)
        b3c = MathTex(r"\text{Av. speed} = \frac{600}{150} = 4 \text{ m/s}").scale(1.05).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3c))
        self.wait(2)
        b3d = MathTex(r"\text{Av. velocity} = \frac{0}{150} = 0 \text{ m/s}").scale(1.05).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3d))
        self.wait(3)

        # --- Band 4 (subtopic_3): the two forces, drawn and signed ---
        self.next_band(4)
        b4t = Tex("40 N east meets 70 N west").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        c = band_shift(4) + UP * 0.7
        dot = Dot(c, radius=0.1)
        self.play(Create(dot))
        a1 = Arrow(c, c + RIGHT * 2.0, buff=0, color=GREEN, stroke_width=6)
        l1 = MathTex(r"40 \text{ N east}").scale(0.95).move_to(c + RIGHT * 2.5 + UP * 0.5)
        self.play(Create(a1), Write(l1))
        self.wait(1.5)
        a2 = Arrow(c, c + LEFT * 3.5, buff=0, color=RED, stroke_width=6)
        l2 = MathTex(r"70 \text{ N west}").scale(0.95).move_to(c + LEFT * 3.8 + UP * 0.5)
        self.play(Create(a2), Write(l2))
        self.wait(2)
        b4a = Tex("Resultant: the one rope doing the same job").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4a))
        self.wait(2.5)
        b4b = Tex("Declare: let east be positive").scale(1.05).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4b))
        self.wait(2)
        b4c = MathTex(r"+40 \text{ N} \quad \text{and} \quad -70 \text{ N}").scale(1.1).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4c))
        self.wait(3)

        # --- Band 5 (subtopic_3): the arithmetic and the answer ---
        self.next_band(5)
        b5t = Tex("Add, then translate back").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5w = MathTex(r"40 + 70 = 110 \text{ N}").scale(1.1).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5w))
        self.play(Create(strike(b5w)))
        self.wait(2)
        b5a = MathTex(r"(+40) + (-70) = -30 \text{ N}").scale(1.15).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5a))
        self.wait(2.5)
        b5b = MathTex(r"\text{Resultant} = 30 \text{ N west}").scale(1.2).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5b))
        self.play(Create(SurroundingRectangle(b5b, color=GREEN)))
        self.wait(2.5)
        b5c = Tex("Checks: follows the larger force;").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        b5d = MathTex(r"\text{magnitude} = 70 - 40 = 30 \text{ N}").scale(1.0).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5c))
        self.play(Write(b5d))
        self.wait(3)

        # --- Band 6 (subtopic_4): the four-step toolkit ---
        self.next_band(6)
        b6t = Tex("The toolkit, four steps").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("1. Declare a positive direction").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.wait(2)
        b6b = Tex("2. Rewrite each vector as a signed number").scale(1.05).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6b))
        self.wait(2)
        b6c = Tex("3. Add algebraically").scale(1.05).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6c))
        self.wait(2)
        b6d = Tex("4. Translate the sign back into a direction").scale(1.05).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6d))
        self.wait(2)
        b6e = Tex("A dozen forces are handled exactly like two").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6e))
        self.wait(3)

        # --- Band 7 (subtopic_4): the special cases ---
        self.next_band(7)
        b7t = Tex("Special cases as landmarks").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = MathTex(r"\text{Same way: } 40 + 70 = 110 \text{ N east}").scale(1.05).shift(band_shift(7) + UP * 1.0)
        self.play(Write(b7a))
        self.wait(2.5)
        b7b = MathTex(r"\text{Opposite: } 70 - 40 = 30 \text{ N west}").scale(1.05).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7b))
        self.wait(2.5)
        b7c = MathTex(r"\text{Equal and opposite: resultant} = 0").scale(1.05).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7c))
        self.play(Create(SurroundingRectangle(b7c, color=GREEN)))
        self.wait(2.5)
        b7d = Tex("Zero resultant $=$ equilibrium (Newton I)").scale(1.05).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7d))
        self.wait(3)

        # --- Band 8 (subtopic_4): the error museum ---
        self.next_band(8)
        b8t = Tex("The error museum").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("1. Adding magnitudes, ignoring directions").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.play(Create(strike(b8a)))
        self.wait(2)
        b8b = Tex("2. `30 N' — incomplete; `30 N west' — physics").scale(1.0).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("3. Swapping sign conventions midway").scale(1.05).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex("4. Classifying by vibe, not by the test").scale(1.05).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8d))
        self.wait(2)
        b8e = Tex("NEEDING a direction is the test").scale(1.05).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8e))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): does it need a `which way'? ---
        self.next_band(9)
        b9t = Tex("Does it need a `which way'?").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("`4 km away' $\\to$ which way? Needed.").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = Tex("`R30 airtime' $\\to$ no direction. Done.").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex("`600 J of energy southward'").scale(1.05).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9c))
        self.play(Create(strike(b9c)))
        self.wait(2)
        b9d = Tex("The sentence test: attach a direction, listen").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9d))
        self.play(Create(SurroundingRectangle(b9d, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_6): the lap around the block ---
        self.next_band(10)
        b10t = Tex("The lap around the block").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("How far did you jog? 600 m — distance").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = Tex("Where are you now? At the gate: 0 m").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10b))
        self.wait(2.5)
        b10c = MathTex(r"\text{speed} = \frac{600}{150} = 4 \text{ m/s}, \; v = 0").scale(1.0).shift(band_shift(10) + DOWN * 1.0)
        self.play(Write(b10c))
        self.wait(2.5)
        b10d = Tex("Straight down the road: 600 m south, 4 m/s south").scale(0.95).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(b10d))
        self.wait(3)

        # --- Band 11 (subtopic_7): two teams on one rope ---
        self.next_band(11)
        b11t = Tex("Two teams on one rope").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11t))
        self.wait(2)
        b11a = Tex("Tug-of-war: 40 N one side, 70 N the other").scale(1.0).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11a))
        self.wait(2)
        b11b = Tex("40 of the 70 are busy cancelling; 30 are spare").scale(1.0).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11b))
        self.wait(2.5)
        b11c = MathTex(r"(+40) + (-70) = -30 \text{ N}").scale(1.1).shift(band_shift(11) + DOWN * 0.7)
        self.play(Write(b11c))
        self.wait(2)
        b11d = MathTex(r"= 30 \text{ N west}").scale(1.15).shift(band_shift(11) + DOWN * 1.6)
        self.play(Write(b11d))
        self.play(Create(SurroundingRectangle(b11d, color=GREEN)))
        self.wait(2)
        b11e = Tex("`30 N' is half an answer — finish the sentence").scale(1.0).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11e))
        self.wait(4)
