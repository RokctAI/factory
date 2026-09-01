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

# Band-layout whiteboard scene for "Describing Motion" (Part 1 — Expert:
# subtopics 1-4; Part 2 — Simplifier: subtopics 5-7). Exporter-safe mobjects
# only, add-only lifecycle, one band per teaching beat. Band time apportioned
# to subtopics.json (225/230/235/255/180/175/175 of 1475 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DescribingMotionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): frame of reference and position ---
        title = Tex("Describing Motion").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Position: location relative to a reference point").scale(1.0).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = Tex("Frame $=$ reference point $+$ positive direction").scale(1.0).shift(UP * 0.0)
        self.play(Write(d2))
        self.play(Create(SurroundingRectangle(d2, color=GREEN)))
        self.wait(2.5)
        d3 = Tex("Declare it: `let north be positive'").scale(1.0).shift(DOWN * 1.1)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex("Never switch frames midway").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the walk on a number line ---
        self.next_band(1)
        b1t = Tex("The walk on a number line").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        c = band_shift(1) + UP * 0.6
        line = Line(c + LEFT * 4.5, c + RIGHT * 4.5, stroke_width=4)
        self.play(Create(line))
        z = Dot(c + LEFT * 3.0, radius=0.09)
        lz = MathTex(r"0").scale(0.9).move_to(c + LEFT * 3.0 + DOWN * 0.5)
        self.play(Create(z), Write(lz))
        self.wait(1.5)
        a1 = Arrow(c + LEFT * 3.0, c + RIGHT * 3.0, buff=0, color=GREEN, stroke_width=6)
        l1 = MathTex(r"+60 \text{ m}").scale(0.9).move_to(c + RIGHT * 0.0 + UP * 0.6)
        self.play(Create(a1), Write(l1))
        self.wait(2)
        a2 = Arrow(c + RIGHT * 3.0 + DOWN * 0.9, c + RIGHT * 1.0 + DOWN * 0.9, buff=0, color=RED, stroke_width=6)
        l2 = MathTex(r"-20 \text{ m}").scale(0.9).move_to(c + RIGHT * 2.0 + DOWN * 1.5)
        self.play(Create(a2), Write(l2))
        self.wait(2)
        b1a = MathTex(r"\text{Final position} = +40 \text{ m (north)}").scale(1.05).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1a))
        self.play(Create(SurroundingRectangle(b1a, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): distance vs displacement, worked ---
        self.next_band(2)
        b2t = Tex("Distance versus displacement").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = MathTex(r"D = 60 + 20 = 80 \text{ m (path, scalar)}").scale(1.0).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2a))
        self.wait(2.5)
        b2b = MathTex(r"\Delta x = +60 - 20 = 40 \text{ m north (vector)}").scale(1.0).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2b))
        self.play(Create(SurroundingRectangle(b2b, color=GREEN)))
        self.wait(2.5)
        b2c = Tex("80 m of walking, 40 m of net change").scale(1.0).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2c))
        self.wait(2)
        b2d = Tex("`40 m' with no direction: incomplete").scale(1.0).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_2): the lap extreme ---
        self.next_band(3)
        b3t = Tex("The lap extreme").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = MathTex(r"\text{Lap of a 300 m track: } D = 300 \text{ m}").scale(1.0).shift(band_shift(3) + UP * 1.0)
        self.play(Write(b3a))
        self.wait(2.5)
        b3b = MathTex(r"\Delta x = 0 \text{ (start = finish)}").scale(1.05).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3b))
        self.play(Create(SurroundingRectangle(b3b, color=GREEN)))
        self.wait(2.5)
        b3c = Tex("Agreement only when direction never changes").scale(1.0).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3c))
        self.wait(2)
        b3d = Tex("60 m north, stop: both give 60").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3d))
        self.wait(3)

        # --- Band 4 (subtopic_3): average speed and average velocity ---
        self.next_band(4)
        b4t = Tex("Two averages from one walk").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = MathTex(r"\text{Av. speed} = \frac{D}{t} = \frac{80}{80} = 1{,}0 \text{ m/s}").scale(1.0).shift(band_shift(4) + UP * 0.9)
        self.play(Write(b4a))
        self.wait(2.5)
        b4b = MathTex(r"\text{Av. velocity} = \frac{\Delta x}{\Delta t} = \frac{40}{80} = 0{,}5 \text{ m/s north}").scale(1.0).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4b))
        self.play(Create(SurroundingRectangle(b4b, color=GREEN)))
        self.wait(2.5)
        b4c = Tex("Different questions: ground eaten vs net change").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4c))
        self.wait(2)
        b4d = Tex("Read the question's noun first").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4d))
        self.wait(3)

        # --- Band 5 (subtopic_3): the lap in 75 s ---
        self.next_band(5)
        b5t = Tex("The lap, timed").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = MathTex(r"\text{Av. speed} = \frac{300}{75} = 4 \text{ m/s}").scale(1.05).shift(band_shift(5) + UP * 0.9)
        self.play(Write(b5a))
        self.wait(2.5)
        b5b = MathTex(r"\text{Av. velocity} = \frac{0}{75} = 0 \text{ m/s}").scale(1.05).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(b5b))
        self.play(Create(SurroundingRectangle(b5b, color=GREEN)))
        self.wait(2.5)
        b5c = Tex("Speed keeps the effort; velocity keeps the outcome").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5c))
        self.wait(3)

        # --- Band 6 (subtopic_4): the four-step method ---
        self.next_band(6)
        b6t = Tex("The method, four steps").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("1. Declare the frame, in writing").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.wait(2)
        b6b = Tex("2. Track positions as signed numbers").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6b))
        self.wait(2)
        b6c = Tex("3. Distance along the path; $\\Delta x$ from endpoints").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6c))
        self.wait(2)
        b6d = Tex("4. Divide by TOTAL time; direction on vectors").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6d))
        self.wait(3)

        # --- Band 7 (subtopic_4): the traps ---
        self.next_band(7)
        b7t = Tex("The classic traps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("1. Speed served when velocity was asked").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7a))
        self.play(Create(strike(b7a)))
        self.wait(2)
        b7b = Tex("2. $\\Delta x$ built by adding path lengths").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7b))
        self.wait(2)
        b7c = Tex("3. Vector answers missing directions").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("4. Wrong time: rests count in the total").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7d))
        self.wait(2)
        b7e = Tex("5. Undeclared or switched frames").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7e))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): where are you, relative to what ---
        self.next_band(8)
        b8t = Tex("Where are you, relative to what").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("`From the bus stop, three houses to the river'").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2.5)
        b8b = Tex("Bus stop $=$ 0; towards the river $=$ positive").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = Tex("Spaza shop: $+3$; soccer field: $-2$").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex("Minus is a direction, not a punishment").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8d))
        self.play(Create(SurroundingRectangle(b8d, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the odometer and the pigeon ---
        self.next_band(9)
        b9t = Tex("The odometer and the pigeon").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Odometer: every metre of the route — distance").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = Tex("Pigeon: straight home, start to finish — displacement").scale(0.95).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = MathTex(r"\text{Walk: odometer } 80 \text{ m; pigeon } 40 \text{ m north}").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9c))
        self.play(Create(SurroundingRectangle(b9c, color=GREEN)))
        self.wait(2.5)
        b9d = Tex("Full lap: odometer 300 m; pigeon stays home").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9d))
        self.wait(3)

        # --- Band 10 (subtopic_7): two speedometers for one walk ---
        self.next_band(10)
        b10t = Tex("Two speedometers for one walk").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = MathTex(r"\text{Odometer over time: } \frac{80}{80} = 1{,}0 \text{ m/s}").scale(1.0).shift(band_shift(10) + UP * 1.0)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = MathTex(r"\text{Pigeon over time: } \frac{40}{80} = 0{,}5 \text{ m/s north}").scale(1.0).shift(band_shift(10) + UP * 0.0)
        self.play(Write(b10b))
        self.play(Create(SurroundingRectangle(b10b, color=GREEN)))
        self.wait(2.5)
        b10c = Tex("Factor of two: a quarter of the walk undone").scale(1.0).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10c))
        self.wait(2)
        b10d = Tex("Divide by the WHOLE time — breaks included").scale(1.0).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(b10d))
        self.wait(4)
