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

# Band-layout whiteboard scene for "Applying Conservation of Mechanical
# Energy" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics
# 5-7). Exporter-safe mobjects only, add-only lifecycle; every worked example
# reproduced line by line with the script's numbers. Band time apportioned to
# subtopics.json (220/240/240/250/190/190/180 of 1510 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ApplyingConservationOfEnergySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the working tool ---
        title = Tex("Applying Conservation of Mechanical Energy").scale(1.05).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"E_{k1} + E_{p1} = E_{k2} + E_{p2}").scale(1.3).shift(UP * 0.8)
        self.play(Write(d1))
        self.play(Create(SurroundingRectangle(d1, color=GREEN)))
        self.wait(2.5)
        d2 = Tex("Valid while friction and air resistance are absent").scale(0.95).shift(DOWN * 0.4)
        self.play(Write(d2))
        self.wait(2.5)
        d3 = Tex("Never needed: time, acceleration, the path").scale(0.95).shift(DOWN * 1.4)
        self.play(Write(d3))
        self.wait(3)

        # --- Band 1 (subtopic_1): the four moves and the zeros ---
        self.next_band(1)
        b1t = Tex("Four moves, and the zeros").scale(1.2).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("1. Choose the two points \\quad 2. Set $h=0$ at the lower").scale(0.85).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1a))
        self.wait(2.5)
        b1b = Tex("3. Write ALL four terms — zeros explicitly \\quad 4. Solve").scale(0.85).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = Tex("Dropped: $E_{k1}=0$ \\quad Peak: $E_{k}=0$").scale(0.95).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1c))
        self.wait(2.5)
        b1d = Tex("Bottom of swing on reference: $E_p=0$").scale(0.95).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1d))
        self.play(Create(SurroundingRectangle(b1d, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the vertical throw ---
        self.next_band(2)
        b2t = Tex("The vertical throw: 14 m/s up").scale(1.15).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2t))
        self.wait(2)
        b2a = MathTex(r"\tfrac{1}{2}m(14)^2 = mg h").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2a))
        self.wait(2.5)
        b2b = MathTex(r"98 = 9{,}8\,h \;\Rightarrow\; h = 10 \text{ m}").scale(1.1).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2b))
        self.play(Create(SurroundingRectangle(b2b, color=GREEN)))
        self.wait(2.5)
        b2c = Tex("Mirror symmetry: same speed at same height,").scale(0.9).shift(band_shift(2) + DOWN * 1.0)
        b2d = Tex("up or down — back to the hand at 14 m/s").scale(0.9).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2c))
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_2): the pendulum ---
        self.next_band(3)
        b3t = Tex("The pendulum: released 0,45 m up").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3t))
        self.wait(2)
        # pendulum sketch: pivot, string, bob at release and at bottom
        piv = Dot(band_shift(3) + UP * 1.4)
        s1 = Line(band_shift(3) + UP * 1.4, band_shift(3) + DOWN * 0.4 + LEFT * 1.4)
        bob1 = Circle(radius=0.18).shift(band_shift(3) + DOWN * 0.4 + LEFT * 1.4)
        s2 = Line(band_shift(3) + UP * 1.4, band_shift(3) + DOWN * 0.8)
        bob2 = Circle(radius=0.18).shift(band_shift(3) + DOWN * 0.8)
        self.play(Create(piv), Create(s1), Create(bob1))
        self.play(Create(s2), Create(bob2))
        self.wait(2)
        b3a = MathTex(r"v^2 = 2 \times 9{,}8 \times 0{,}45 = 8{,}82").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3a))
        self.wait(2.5)
        b3b = MathTex(r"v = 2{,}97 \text{ m/s}").scale(1.1).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3b))
        self.play(Create(SurroundingRectangle(b3b, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the coaster — account at the top ---
        self.next_band(4)
        b4t = Tex("The coaster: 500 kg, 20 m crest, 4 m/s").scale(1.05).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4t))
        self.wait(2)
        b4a = MathTex(r"E_{k1} = \tfrac{1}{2} \times 500 \times 4^2 = 4\,000 \text{ J}").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4a))
        self.wait(2.5)
        b4b = MathTex(r"E_{p1} = 500 \times 9{,}8 \times 20 = 98\,000 \text{ J}").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4b))
        self.wait(2.5)
        b4c = MathTex(r"E_M = 4\,000 + 98\,000 = 102\,000 \text{ J}").scale(1.05).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4c))
        self.play(Create(SurroundingRectangle(b4c, color=GREEN)))
        self.wait(2.5)
        b4d = Tex("Locked in for the whole ride — friction ignored").scale(0.9).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4d))
        self.wait(3)

        # --- Band 5 (subtopic_3): solve at the bottom, and the trap ---
        self.next_band(5)
        b5t = Tex("At the bottom").scale(1.2).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5t))
        self.wait(2)
        b5a = MathTex(r"\tfrac{1}{2} \times 500 \times v^2 = 102\,000").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5a))
        self.wait(2.5)
        b5b = MathTex(r"v^2 = 408 \;\Rightarrow\; v = 20{,}20 \text{ m/s}").scale(1.1).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5b))
        self.play(Create(SurroundingRectangle(b5b, color=GREEN)))
        self.wait(2.5)
        b5c = Tex("Trap: drop the 4 000 J and get 19,80 m/s —").scale(0.9).shift(band_shift(5) + DOWN * 1.0)
        b5d = Tex("wrong, but plausible enough to keep").scale(0.9).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5c))
        self.play(Write(b5d))
        self.wait(2.5)
        b5e = Tex("Moving at point one $\\Rightarrow E_{k1} \\ne 0$").scale(0.95).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5e))
        self.wait(3)

        # --- Band 6 (subtopic_3): the halfway check ---
        self.next_band(6)
        b6t = Tex("Any point surrenders its speed").scale(1.15).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6t))
        self.wait(2)
        b6a = MathTex(r"\text{At } 8 \text{ m: } E_p = 500 \times 9{,}8 \times 8 = 39\,200 \text{ J}").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.wait(2.5)
        b6b = MathTex(r"E_k = 102\,000 - 39\,200 = 62\,800 \text{ J}").scale(0.95).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = MathTex(r"v^2 = 251{,}2 \;\Rightarrow\; v = 15{,}85 \text{ m/s}").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6c))
        self.play(Create(SurroundingRectangle(b6c, color=GREEN)))
        self.wait(2.5)
        b6d = Tex("The ledger reads speed off every height").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6d))
        self.wait(3)

        # --- Band 7 (subtopic_4): the incline and path independence ---
        self.next_band(7)
        b7t = Tex("The water slide: 3,2 m high").scale(1.15).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7t))
        self.wait(2)
        # incline sketch
        gnd = Line(band_shift(7) + DOWN * 1.0 + LEFT * 4.0, band_shift(7) + DOWN * 1.0 + RIGHT * 3.0)
        ramp = Line(band_shift(7) + UP * 0.8 + LEFT * 3.2, band_shift(7) + DOWN * 1.0 + RIGHT * 0.6)
        self.play(Create(gnd), Create(ramp))
        self.wait(2)
        b7a = MathTex(r"v^2 = 2 \times 9{,}8 \times 3{,}2 = 62{,}72").scale(1.0).shift(band_shift(7) + UP * 1.4)
        self.play(Write(b7a))
        self.wait(2.5)
        b7b = MathTex(r"v = 7{,}92 \text{ m/s}").scale(1.1).shift(band_shift(7) + RIGHT * 2.4 + UP * 0.3)
        self.play(Write(b7b))
        self.play(Create(SurroundingRectangle(b7b, color=GREEN)))
        self.wait(2.5)
        b7c = Tex("Cliff, chute or corkscrew: same 7,92 m/s").scale(0.9).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("Steeper $=$ sooner, never faster").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7d))
        self.wait(3)

        # --- Band 8 (subtopic_4): the boundary of the tool ---
        self.next_band(8)
        b8t = Tex("The boundary of the tool").scale(1.2).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Friction or air resistance enters the question...").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8a))
        self.wait(2)
        b8b = MathTex(r"E_{k1} + E_{p1} = E_{k2} + E_{p2}").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8b))
        self.play(Create(strike(b8b)))
        self.wait(2.5)
        b8c = Tex("Grade 10 answer: $E_M$ decreased — it went to heat").scale(0.9).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8c))
        self.wait(2.5)
        b8d = Tex("Calculating the loss: work-energy theorem, later grades").scale(0.85).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8d))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): the swing knows your height ---
        self.next_band(9)
        b9t = Tex("The swing knows your height").scale(1.2).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Pulled back and up: height money loaded").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = Tex("Bottom of the arc: all speed money — stomach drop").scale(0.9).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex("Far side: SAME height as release — never higher").scale(0.9).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9c))
        self.play(Create(SurroundingRectangle(b9c, color=GREEN)))
        self.wait(2.5)
        b9d = Tex("Unpushed swing dies: air skims a coin each pass").scale(0.9).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9d))
        self.wait(2)
        b9e = MathTex(r"0{,}45 \text{ m} \Rightarrow v = 2{,}97 \text{ m/s at the bottom}").scale(0.9).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9e))
        self.wait(3)

        # --- Band 10 (subtopic_6): only the drop counts ---
        self.next_band(10)
        b10t = Tex("Only the drop counts").scale(1.2).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("Steep slide vs lazy flume, both 3,2 m high").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = Tex("Both arrive at 7,92 m/s — steep is only SOONER").scale(0.95).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10b))
        self.play(Create(SurroundingRectangle(b10b, color=GREEN)))
        self.wait(2.5)
        b10c = Tex("The ledger prices height and speed — nothing else").scale(0.9).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10c))
        self.wait(2.5)
        b10d = Tex("Coaster: 4 000 + 98 000 = 102 000 J $\\Rightarrow$ 20,20 m/s").scale(0.85).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10d))
        self.wait(2)
        b10e = Tex("Count every coin carried over the crest").scale(0.9).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10e))
        self.wait(3)

        # --- Band 11 (subtopic_7): why the second hill is lower ---
        self.next_band(11)
        b11t = Tex("Why the second hill is always lower").scale(1.1).shift(band_shift(11) + UP * 2.3)
        self.play(Write(b11t))
        self.wait(2)
        # skyline: descending hills as line segments
        sky = VGroup(
            Line(band_shift(11) + DOWN * 1.2 + LEFT * 4.5, band_shift(11) + UP * 0.9 + LEFT * 3.0),
            Line(band_shift(11) + UP * 0.9 + LEFT * 3.0, band_shift(11) + DOWN * 1.2 + LEFT * 1.5),
            Line(band_shift(11) + DOWN * 1.2 + LEFT * 1.5, band_shift(11) + UP * 0.3 + LEFT * 0.2),
            Line(band_shift(11) + UP * 0.3 + LEFT * 0.2, band_shift(11) + DOWN * 1.2 + RIGHT * 1.1),
            Line(band_shift(11) + DOWN * 1.2 + RIGHT * 1.1, band_shift(11) + DOWN * 0.2 + RIGHT * 2.2),
            Line(band_shift(11) + DOWN * 0.2 + RIGHT * 2.2, band_shift(11) + DOWN * 1.2 + RIGHT * 3.3),
        )
        self.play(Create(sky))
        self.wait(2.5)
        b11a = Tex("The whole budget is banked at the first crest").scale(0.9).shift(band_shift(11) + UP * 1.4)
        self.play(Write(b11a))
        self.wait(2.5)
        b11b = Tex("Friction taxes every metre — hills shrink extra").scale(0.9).shift(band_shift(11) + DOWN * 1.9)
        self.play(Write(b11b))
        self.wait(2)
        b11c = Tex("`Ignore friction and air resistance' IS the seal").scale(0.9).shift(band_shift(11) + DOWN * 2.8)
        self.play(Write(b11c))
        self.play(Create(SurroundingRectangle(b11c, color=GREEN)))
        self.wait(4)
