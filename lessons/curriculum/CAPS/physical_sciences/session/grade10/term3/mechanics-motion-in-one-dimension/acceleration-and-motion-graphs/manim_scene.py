from manim import *

# Band-layout whiteboard scene for the session duo "Acceleration and Motion
# Graphs" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7).
# All content is exporter-safe (Tex/MathTex/Line/Arrow/Dot/Rectangle/VGroup),
# add-only lifecycle, one band per teaching beat, camera moves down between
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
        title = Tex("Acceleration and Motion Graphs").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"a = \frac{\Delta v}{\Delta t}").scale(1.3).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = MathTex(r"\Delta v = v_f - v_i").scale(1.15).shift(DOWN * 0.3)
        self.play(Write(d2))
        self.wait(2)
        d3 = Tex(r"Unit: m/s per second $= \text{m/s}^2$").scale(1.1).shift(DOWN * 1.4)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex(r"$2 \text{ m/s}^2$: gain 2 m/s every second").scale(1.1).shift(DOWN * 2.5)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): phase 1 and the cruise ---
        self.next_band(1)
        b1t = Tex("Phase 1: rest to 20 m/s in 10 s").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"\Delta v = 20 - 0 = 20 \text{ m/s}").scale(1.15).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1a))
        self.wait(2)
        b1b = MathTex(r"a = \frac{20}{10} = 2 \text{ m/s}^2").scale(1.15).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(b1b))
        self.play(Create(SurroundingRectangle(b1b, color=GREEN)))
        self.wait(2.5)
        b1c = Tex(r"Speedometer: 0, 2, 4, 6, ... 20").scale(1.1).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1c))
        self.wait(2)
        b1d = MathTex(r"\text{Cruise: } \Delta v = 0 \Rightarrow a = 0").scale(1.1).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1d))
        self.wait(3)

        # --- Band 2 (subtopic_1): braking and the sign ---
        self.next_band(2)
        b2t = Tex("Phase 3: 20 m/s to rest in 5 s").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = MathTex(r"\Delta v = 0 - 20 = -20 \text{ m/s}").scale(1.15).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2a))
        self.wait(2)
        b2b = MathTex(r"a = \frac{-20}{5} = -4 \text{ m/s}^2").scale(1.15).shift(band_shift(2) + DOWN * 0.2)
        self.play(Write(b2b))
        self.play(Create(SurroundingRectangle(b2b, color=GREEN)))
        self.wait(2.5)
        b2c = Tex("Negative $a$ here: 4 m/s lost each second").scale(1.05).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2c))
        self.wait(2)
        b2d = Tex("Read signs against the declared frame").scale(1.05).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_2): position-time reading rules ---
        self.next_band(3)
        b3t = Tex("Position-time: gradient $=$ velocity").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = MathTex(r"\text{gradient} = \frac{\Delta x}{\Delta t} = v").scale(1.15).shift(band_shift(3) + UP * 1.0)
        self.play(Write(b3a))
        self.wait(2.5)
        b3b = Tex("Steep: fast \\quad Shallow: slow").scale(1.1).shift(band_shift(3) + DOWN * 0.1)
        self.play(Write(b3b))
        self.wait(2)
        b3c = Tex("Flat line: stationary").scale(1.1).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3c))
        self.wait(2)
        b3d = Tex("Curve: changing gradient — acceleration").scale(1.1).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3d))
        self.wait(2)
        b3e = Tex("Downward slope: negative velocity").scale(1.1).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3e))
        self.wait(3)

        # --- Band 4 (subtopic_2): the car's position-time picture ---
        self.next_band(4)
        b4t = Tex("The car's position-time graph").scale(1.2).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4t))
        self.wait(1.5)
        o4 = band_shift(4) + LEFT * 4.7 + DOWN * 2.4
        ax4x = Arrow(o4, o4 + RIGHT * 8.6, buff=0, stroke_width=4)
        ax4y = Arrow(o4, o4 + UP * 4.6, buff=0, stroke_width=4)
        lx4 = MathTex(r"t").scale(1.0).move_to(o4 + RIGHT * 8.9)
        ly4 = MathTex(r"x").scale(1.0).move_to(o4 + UP * 4.9)
        self.play(Create(ax4x), Create(ax4y))
        self.play(Write(lx4), Write(ly4))
        self.wait(1.5)
        # steepening curve (phase 1) as a short segment chain
        c4 = VGroup(
            Line(o4, o4 + RIGHT * 0.8 + UP * 0.12, stroke_width=5, color=YELLOW),
            Line(o4 + RIGHT * 0.8 + UP * 0.12, o4 + RIGHT * 1.5 + UP * 0.42, stroke_width=5, color=YELLOW),
            Line(o4 + RIGHT * 1.5 + UP * 0.42, o4 + RIGHT * 2.0 + UP * 0.8, stroke_width=5, color=YELLOW),
        )
        self.play(Create(c4), run_time=1.5)
        lab4a = Tex("curve: speeding up").scale(0.9).move_to(o4 + RIGHT * 2.1 + DOWN * 0.5)
        self.play(Write(lab4a))
        self.wait(2)
        s4 = Line(o4 + RIGHT * 2.0 + UP * 0.8, o4 + RIGHT * 6.0 + UP * 4.0, stroke_width=5, color=YELLOW)
        self.play(Create(s4))
        lab4b = Tex("straight: cruise").scale(0.9).move_to(o4 + RIGHT * 5.6 + UP * 2.2)
        self.play(Write(lab4b))
        self.wait(2)
        f4 = VGroup(
            Line(o4 + RIGHT * 6.0 + UP * 4.0, o4 + RIGHT * 6.6 + UP * 4.35, stroke_width=5, color=YELLOW),
            Line(o4 + RIGHT * 6.6 + UP * 4.35, o4 + RIGHT * 7.2 + UP * 4.5, stroke_width=5, color=YELLOW),
        )
        self.play(Create(f4), run_time=1.2)
        lab4c = Tex("flattens: braking").scale(0.9).move_to(o4 + RIGHT * 6.6 + UP * 5.0)
        self.play(Write(lab4c))
        self.wait(3)

        # --- Band 5 (subtopic_3): velocity-time graph, gradients ---
        self.next_band(5)
        b5t = Tex("Velocity-time: gradient $=$ acceleration").scale(1.15).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5t))
        self.wait(2)
        o5 = band_shift(5) + LEFT * 4.7 + DOWN * 2.3
        ax5x = Arrow(o5, o5 + RIGHT * 8.6, buff=0, stroke_width=4)
        ax5y = Arrow(o5, o5 + UP * 4.2, buff=0, stroke_width=4)
        lx5 = MathTex(r"t \text{ (s)}").scale(0.9).move_to(o5 + RIGHT * 8.7 + UP * 0.5)
        ly5 = MathTex(r"v \text{ (m/s)}").scale(0.9).move_to(o5 + UP * 4.5 + RIGHT * 1.2)
        self.play(Create(ax5x), Create(ax5y))
        self.play(Write(lx5), Write(ly5))
        self.wait(1.5)
        # ramp up to (10 s, 20 m/s), plateau to 30 s, ramp down to 35 s
        r5a = Line(o5, o5 + RIGHT * 2.0 + UP * 3.0, stroke_width=5, color=YELLOW)
        r5b = Line(o5 + RIGHT * 2.0 + UP * 3.0, o5 + RIGHT * 6.0 + UP * 3.0, stroke_width=5, color=YELLOW)
        r5c = Line(o5 + RIGHT * 6.0 + UP * 3.0, o5 + RIGHT * 7.0, stroke_width=5, color=YELLOW)
        m5a = MathTex(r"20").scale(0.85).move_to(o5 + LEFT * 0.4 + UP * 3.0)
        m5b = MathTex(r"10").scale(0.85).move_to(o5 + RIGHT * 2.0 + DOWN * 0.4)
        m5c = MathTex(r"30").scale(0.85).move_to(o5 + RIGHT * 6.0 + DOWN * 0.4)
        m5d = MathTex(r"35").scale(0.85).move_to(o5 + RIGHT * 7.2 + DOWN * 0.4)
        self.play(Create(r5a))
        g5a = MathTex(r"\text{grad} = \tfrac{20}{10} = 2").scale(0.9).move_to(o5 + RIGHT * 0.9 + UP * 3.6)
        self.play(Write(g5a), Write(m5a), Write(m5b))
        self.wait(2)
        self.play(Create(r5b))
        g5b = MathTex(r"\text{grad} = 0").scale(0.9).move_to(o5 + RIGHT * 4.0 + UP * 3.6)
        self.play(Write(g5b), Write(m5c))
        self.wait(2)
        self.play(Create(r5c))
        g5c = MathTex(r"\text{grad} = \tfrac{-20}{5} = -4").scale(0.9).move_to(o5 + RIGHT * 8.0 + UP * 2.2)
        self.play(Write(g5c), Write(m5d))
        self.wait(3)

        # --- Band 6 (subtopic_3): area = displacement, 550 m ---
        self.next_band(6)
        b6t = Tex("Area under $v$-$t$ $=$ displacement").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = MathTex(r"A_1 = \tfrac{1}{2} \times 10 \times 20 = 100 \text{ m}").scale(1.1).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6a))
        self.wait(2)
        b6b = MathTex(r"A_2 = 20 \times 20 = 400 \text{ m}").scale(1.1).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6b))
        self.wait(2)
        b6c = MathTex(r"A_3 = \tfrac{1}{2} \times 5 \times 20 = 50 \text{ m}").scale(1.1).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6c))
        self.wait(2)
        b6d = MathTex(r"\Delta x = 100 + 400 + 50 = 550 \text{ m}").scale(1.15).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6d))
        self.play(Create(SurroundingRectangle(b6d, color=GREEN)))
        self.wait(2.5)
        b6e = Tex("One picture: gradient AND area pay").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6e))
        self.wait(3)

        # --- Band 7 (subtopic_4): acceleration-time steps ---
        self.next_band(7)
        b7t = Tex("Acceleration-time: flat steps").scale(1.2).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7t))
        self.wait(2)
        o7 = band_shift(7) + LEFT * 4.7 + DOWN * 0.8
        ax7x = Arrow(o7, o7 + RIGHT * 8.6, buff=0, stroke_width=4)
        ax7y = Arrow(o7 + DOWN * 2.4, o7 + UP * 2.2, buff=0, stroke_width=4)
        lx7 = MathTex(r"t").scale(0.9).move_to(o7 + RIGHT * 8.9)
        ly7 = MathTex(r"a").scale(0.9).move_to(o7 + UP * 2.5 + RIGHT * 0.3)
        self.play(Create(ax7x), Create(ax7y))
        self.play(Write(lx7), Write(ly7))
        self.wait(1.5)
        s7a = Line(o7 + UP * 1.0, o7 + RIGHT * 2.0 + UP * 1.0, stroke_width=5, color=YELLOW)
        s7b = Line(o7 + RIGHT * 2.0, o7 + RIGHT * 6.0, stroke_width=5, color=YELLOW)
        s7c = Line(o7 + RIGHT * 6.0 + DOWN * 2.0, o7 + RIGHT * 7.0 + DOWN * 2.0, stroke_width=5, color=YELLOW)
        n7a = MathTex(r"+2").scale(0.9).move_to(o7 + RIGHT * 1.0 + UP * 1.5)
        n7b = MathTex(r"0").scale(0.9).move_to(o7 + RIGHT * 4.0 + UP * 0.5)
        n7c = MathTex(r"-4").scale(0.9).move_to(o7 + RIGHT * 6.5 + DOWN * 2.5)
        self.play(Create(s7a), Write(n7a))
        self.wait(1.5)
        self.play(Create(s7b), Write(n7b))
        self.wait(1.5)
        self.play(Create(s7c), Write(n7c))
        self.wait(3)

        # --- Band 8 (subtopic_4): the family links and the traps ---
        self.next_band(8)
        b8t = Tex("One motion, three graphs").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"Gradients travel down: $x \to v \to a$").scale(1.1).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex(r"Areas travel up: $a \to \Delta v$, $v \to \Delta x$").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = Tex("Trap: rising $v$-$t$ line $=$ moving away").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8c))
        self.play(Create(strike(b8c)))
        self.wait(2)
        b8d = Tex("Rising $v$-$t$ line $=$ speeding up").scale(1.05).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8d))
        self.play(Create(SurroundingRectangle(b8d, color=GREEN)))
        self.wait(2)
        b8e = Tex(r"$v$-$t$ gradient of 2 is $2 \text{ m/s}^2$, not m/s").scale(1.0).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8e))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): the speedometer's diary ---
        self.next_band(9)
        b9t = Tex("The speedometer's diary").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Needle climbs: 0, 2, 4, 6 ... 20").scale(1.1).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2)
        b9b = MathTex(r"a = \frac{20}{10} = 2 \text{ m/s}^2").scale(1.1).shift(band_shift(9) + UP * 0.0)
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex("Needle rests at 20: $a = 0$, not parked").scale(1.05).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9c))
        self.wait(2.5)
        b9d = MathTex(r"\text{Needle falls: } a = \frac{-20}{5} = -4 \text{ m/s}^2").scale(1.05).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(b9d))
        self.play(Create(SurroundingRectangle(b9d, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_6): the journey as a silhouette ---
        self.next_band(10)
        b10t = Tex("The journey as a picture").scale(1.2).shift(band_shift(10) + UP * 2.5)
        self.play(Write(b10t))
        self.wait(2)
        o10 = band_shift(10) + LEFT * 4.7 + DOWN * 1.9
        ax10x = Arrow(o10, o10 + RIGHT * 8.6, buff=0, stroke_width=4)
        ax10y = Arrow(o10, o10 + UP * 3.8, buff=0, stroke_width=4)
        self.play(Create(ax10x), Create(ax10y))
        r10a = Line(o10, o10 + RIGHT * 2.0 + UP * 2.8, stroke_width=5, color=YELLOW)
        r10b = Line(o10 + RIGHT * 2.0 + UP * 2.8, o10 + RIGHT * 6.0 + UP * 2.8, stroke_width=5, color=YELLOW)
        r10c = Line(o10 + RIGHT * 6.0 + UP * 2.8, o10 + RIGHT * 7.0, stroke_width=5, color=YELLOW)
        self.play(Create(r10a))
        l10a = Tex("ramp up: accelerator").scale(0.9).move_to(o10 + RIGHT * 0.6 + UP * 3.3)
        self.play(Write(l10a))
        self.wait(2)
        self.play(Create(r10b))
        l10b = Tex("plateau: cruising").scale(0.9).move_to(o10 + RIGHT * 4.0 + UP * 3.3)
        self.play(Write(l10b))
        self.wait(2)
        self.play(Create(r10c))
        l10c = Tex("ramp down: brake").scale(0.9).move_to(o10 + RIGHT * 7.6 + UP * 1.6)
        self.play(Write(l10c))
        self.wait(2)
        l10d = Tex("Height $=$ how fast, never how far").scale(1.05).move_to(band_shift(10) + DOWN * 2.9)
        self.play(Write(l10d))
        self.wait(3)

        # --- Band 11 (subtopic_7): the area that pays out in metres ---
        self.next_band(11)
        b11t = Tex("The area that pays out in metres").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11t))
        self.wait(2)
        b11a = MathTex(r"\text{Plateau: } 20 \times 20 = 400 \text{ m}").scale(1.1).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11a))
        self.wait(2)
        b11b = MathTex(r"\text{Pull-away: } \tfrac{1}{2} \times 10 \times 20 = 100 \text{ m}").scale(1.05).shift(band_shift(11) + UP * 0.1)
        self.play(Write(b11b))
        self.wait(2)
        b11c = MathTex(r"\text{Braking: } \tfrac{1}{2} \times 5 \times 20 = 50 \text{ m}").scale(1.05).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11c))
        self.wait(2)
        b11d = MathTex(r"100 + 400 + 50 = 550 \text{ m}").scale(1.15).shift(band_shift(11) + DOWN * 1.9)
        self.play(Write(b11d))
        self.play(Create(SurroundingRectangle(b11d, color=GREEN)))
        self.wait(2)
        b11e = Tex("Sketch the graph — let the shape think").scale(1.05).shift(band_shift(11) + DOWN * 2.9)
        self.play(Write(b11e))
        self.wait(4)
