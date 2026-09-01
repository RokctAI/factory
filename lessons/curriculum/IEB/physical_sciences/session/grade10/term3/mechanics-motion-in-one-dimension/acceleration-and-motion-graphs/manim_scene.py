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

# Band-layout whiteboard scene for "Acceleration and Motion Graphs" (Part 1 —
# Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7). Exporter-safe
# mobjects only, add-only lifecycle, one band per teaching beat across 12
# bands. Band time is apportioned to subtopics.json durations
# (235/225/240/250/185/175/170 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AccelerationAndMotionGraphsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): acceleration defined ---
        title = Tex("Acceleration and Motion Graphs").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"a = \frac{\Delta v}{\Delta t}").scale(1.3).shift(UP * 0.6)
        self.play(Write(d1))
        self.play(Create(SurroundingRectangle(d1, color=GREEN)))
        self.wait(2.5)
        d2 = Tex("Unit: metres per second, per second — m/s$^2$").scale(1.0).shift(DOWN * 0.7)
        self.play(Write(d2))
        self.wait(2)
        d3 = Tex("2,5 m/s$^2$: velocity grows 2,5 m/s every second").scale(0.95).shift(DOWN * 1.8)
        self.play(Write(d3))
        self.wait(3)

        # --- Band 1 (subtopic_1): phase 1 and the cruise ---
        self.next_band(1)
        b1t = Tex("Phase 1 and the cruise").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"a = \frac{15 - 0}{6} = 2{,}5 \text{ m/s}^2").scale(1.1).shift(band_shift(1) + UP * 0.9)
        self.play(Write(b1a))
        self.play(Create(SurroundingRectangle(b1a, color=GREEN)))
        self.wait(2.5)
        b1b = Tex("0; 2,5; 5; 7,5; \\dots\\ 15 — uniform").scale(1.0).shift(band_shift(1) + DOWN * 0.3)
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = MathTex(r"\text{Cruise: } \Delta v = 0 \Rightarrow a = 0").scale(1.05).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1c))
        self.wait(2)
        b1d = Tex("Constant velocity $=$ zero acceleration").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1d))
        self.wait(3)

        # --- Band 2 (subtopic_1): braking and the sign ---
        self.next_band(2)
        b2t = Tex("Braking, and what the sign means").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = MathTex(r"a = \frac{0 - 15}{10} = -1{,}5 \text{ m/s}^2").scale(1.1).shift(band_shift(2) + UP * 0.9)
        self.play(Write(b2a))
        self.play(Create(SurroundingRectangle(b2a, color=GREEN)))
        self.wait(2.5)
        b2b = Tex("1,5 m/s of speed drained each second").scale(1.0).shift(band_shift(2) + DOWN * 0.2)
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = Tex("The sign belongs to the FRAME").scale(1.05).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2c))
        self.wait(2)
        b2d = Tex("Read signs against the declared positive").scale(1.0).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_2): position-time reading rules ---
        self.next_band(3)
        b3t = Tex("Position-time: gradient IS velocity").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("Steep: fast. Shallow: slow. Flat: parked.").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3a))
        self.wait(2.5)
        b3b = Tex("Straight slope: constant velocity").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3b))
        self.wait(2)
        b3c = Tex("Curve: changing gradient — acceleration").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3c))
        self.wait(2)
        b3d = Tex("Downward slope: negative velocity").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3d))
        self.wait(3)

        # --- Band 4 (subtopic_2): the bus's position-time picture ---
        self.next_band(4)
        b4t = Tex("The bus on position-time axes").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        o = band_shift(4) + DOWN * 2.2 + LEFT * 4.5
        ax_x = Line(o, o + RIGHT * 9.0, stroke_width=3)
        ax_y = Line(o, o + UP * 3.6, stroke_width=3)
        self.play(Create(ax_x), Create(ax_y))
        self.wait(1)
        seg1 = ArcBetweenPoints(o, o + RIGHT * 2.0 + UP * 0.9, angle=-0.5, color=GREEN, stroke_width=5)
        self.play(Create(seg1))
        l1 = Tex("steepening curve").scale(0.7).move_to(o + RIGHT * 1.4 + UP * 1.5)
        self.play(Write(l1))
        self.wait(2)
        seg2 = Line(o + RIGHT * 2.0 + UP * 0.9, o + RIGHT * 6.5 + UP * 2.9, color=YELLOW, stroke_width=5)
        self.play(Create(seg2))
        l2 = Tex("straight slope: cruise").scale(0.7).move_to(o + RIGHT * 4.0 + UP * 2.6)
        self.play(Write(l2))
        self.wait(2)
        seg3 = ArcBetweenPoints(o + RIGHT * 6.5 + UP * 2.9, o + RIGHT * 8.5 + UP * 3.4, angle=-0.45, color=RED, stroke_width=5)
        self.play(Create(seg3))
        l3 = Tex("flattening: braking").scale(0.7).move_to(o + RIGHT * 7.3 + UP * 2.6)
        self.play(Write(l3))
        self.wait(3)

        # --- Band 5 (subtopic_3): velocity-time graph, gradients ---
        self.next_band(5)
        b5t = Tex("Velocity-time: first payment, gradients").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        o5 = band_shift(5) + DOWN * 2.2 + LEFT * 4.5
        ax5x = Line(o5, o5 + RIGHT * 9.0, stroke_width=3)
        ax5y = Line(o5, o5 + UP * 3.4, stroke_width=3)
        self.play(Create(ax5x), Create(ax5y))
        self.wait(1)
        p1 = Line(o5, o5 + RIGHT * 1.2 + UP * 3.0, color=GREEN, stroke_width=5)
        p2 = Line(o5 + RIGHT * 1.2 + UP * 3.0, o5 + RIGHT * 7.0 + UP * 3.0, color=YELLOW, stroke_width=5)
        p3 = Line(o5 + RIGHT * 7.0 + UP * 3.0, o5 + RIGHT * 9.0, color=RED, stroke_width=5)
        self.play(Create(p1))
        g1 = MathTex(r"\frac{15}{6} = 2{,}5").scale(0.8).move_to(o5 + RIGHT * 0.4 + UP * 3.3)
        self.play(Write(g1))
        self.wait(2)
        self.play(Create(p2))
        g2 = MathTex(r"0").scale(0.9).move_to(o5 + RIGHT * 4.0 + UP * 3.4)
        self.play(Write(g2))
        self.wait(2)
        self.play(Create(p3))
        g3 = MathTex(r"\frac{-15}{10} = -1{,}5").scale(0.8).move_to(o5 + RIGHT * 8.6 + UP * 2.0)
        self.play(Write(g3))
        self.wait(3)

        # --- Band 6 (subtopic_3): area = displacement, 570 m ---
        self.next_band(6)
        b6t = Tex("Second payment: area $=$ displacement").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = MathTex(r"\text{Triangle: } \tfrac{1}{2} \times 6 \times 15 = 45 \text{ m}").scale(1.0).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6a))
        self.wait(2.5)
        b6b = MathTex(r"\text{Rectangle: } 30 \times 15 = 450 \text{ m}").scale(1.0).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = MathTex(r"\text{Triangle: } \tfrac{1}{2} \times 10 \times 15 = 75 \text{ m}").scale(1.0).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6c))
        self.wait(2.5)
        b6d = MathTex(r"\text{Total} = 45 + 450 + 75 = 570 \text{ m}").scale(1.1).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6d))
        self.play(Create(SurroundingRectangle(b6d, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): acceleration-time steps ---
        self.next_band(7)
        b7t = Tex("Acceleration-time: flat steps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        o7 = band_shift(7) + DOWN * 0.6 + LEFT * 4.5
        ax7 = Line(o7, o7 + RIGHT * 9.0, stroke_width=3)
        self.play(Create(ax7))
        s1 = Line(o7 + UP * 1.4, o7 + RIGHT * 1.2 + UP * 1.4, color=GREEN, stroke_width=5)
        s2 = Line(o7 + RIGHT * 1.2, o7 + RIGHT * 7.0, color=YELLOW, stroke_width=5)
        s3 = Line(o7 + RIGHT * 7.0 + DOWN * 0.9, o7 + RIGHT * 9.0 + DOWN * 0.9, color=RED, stroke_width=5)
        self.play(Create(s1))
        m1 = MathTex(r"+2{,}5").scale(0.8).move_to(o7 + RIGHT * 0.6 + UP * 1.9)
        self.play(Write(m1))
        self.wait(2)
        self.play(Create(s2))
        m2 = MathTex(r"0").scale(0.8).move_to(o7 + RIGHT * 4.0 + UP * 0.4)
        self.play(Write(m2))
        self.wait(2)
        self.play(Create(s3))
        m3 = MathTex(r"-1{,}5").scale(0.8).move_to(o7 + RIGHT * 8.0 + DOWN * 1.4)
        self.play(Write(m3))
        self.wait(3)

        # --- Band 8 (subtopic_4): the family links and the traps ---
        self.next_band(8)
        b8t = Tex("One motion, three graphs").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Gradients travel DOWN the family").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex("Areas travel UP the family").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("Rising v-t line $=$ moving away").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8c))
        self.play(Create(strike(b8c)))
        self.wait(2)
        b8d = Tex("Rising v-t line $=$ speeding up").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8d))
        self.play(Create(SurroundingRectangle(b8d, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): the speedometer's diary ---
        self.next_band(9)
        b9t = Tex("The speedometer's diary").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Acceleration: how fast the NEEDLE moves").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = Tex("Climbing needle: $+2{,}5$ per second, per second").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex("Resting needle at 15: moving fast, $a = 0$").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9c))
        self.play(Create(SurroundingRectangle(b9c, color=GREEN)))
        self.wait(2.5)
        b9d = Tex("Sinking needle: $-1{,}5$ — you tip forward").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9d))
        self.wait(3)

        # --- Band 10 (subtopic_6): the journey as a silhouette ---
        self.next_band(10)
        b10t = Tex("The journey as a silhouette").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        o10 = band_shift(10) + DOWN * 2.0 + LEFT * 4.5
        axx = Line(o10, o10 + RIGHT * 9.0, stroke_width=3)
        self.play(Create(axx))
        r1 = Line(o10, o10 + RIGHT * 1.2 + UP * 2.6, color=GREEN, stroke_width=5)
        r2 = Line(o10 + RIGHT * 1.2 + UP * 2.6, o10 + RIGHT * 7.0 + UP * 2.6, color=YELLOW, stroke_width=5)
        r3 = Line(o10 + RIGHT * 7.0 + UP * 2.6, o10 + RIGHT * 9.0, color=RED, stroke_width=5)
        self.play(Create(r1))
        self.play(Create(r2))
        self.play(Create(r3))
        self.wait(2)
        b10a = Tex("Ramp up, plateau, ramp down").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10a))
        self.wait(2)
        b10b = Tex("Height is speed, never how far").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10b))
        self.play(Create(SurroundingRectangle(b10b, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): the area that pays out in metres ---
        self.next_band(11)
        b11t = Tex("The area that pays out in metres").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11t))
        self.wait(2)
        b11a = MathTex(r"\text{Plateau: } 15 \times 30 = 450 \text{ m}").scale(1.0).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11a))
        self.wait(2.5)
        b11b = MathTex(r"\text{Pull-away: } \tfrac{1}{2} \times 6 \times 15 = 45 \text{ m}").scale(1.0).shift(band_shift(11) + UP * 0.1)
        self.play(Write(b11b))
        self.wait(2.5)
        b11c = MathTex(r"\text{Braking: } \tfrac{1}{2} \times 10 \times 15 = 75 \text{ m}").scale(1.0).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11c))
        self.wait(2.5)
        b11d = MathTex(r"45 + 450 + 75 = 570 \text{ m}").scale(1.15).shift(band_shift(11) + DOWN * 2.0)
        self.play(Write(b11d))
        self.play(Create(SurroundingRectangle(b11d, color=GREEN)))
        self.wait(4)
