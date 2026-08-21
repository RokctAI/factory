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

# Band-layout whiteboard scene for equations-of-motion (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe mobjects,
# add-only lifecycle, one band per teaching beat.
# Time apportioned to subtopics.json (220/230/230/260/170/180/170 of 1460 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EquationsOfMotionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the cast of five ---
        title = Tex("Equations of Motion").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"v_i, \; v_f, \; a, \; \Delta t, \; \Delta x").scale(1.2).shift(UP * 0.7)
        self.play(Write(d1))
        self.wait(2.5)
        d2 = Tex("Five characters describe any straight-line trip").scale(1.0).shift(DOWN * 0.4)
        self.play(Write(d2))
        self.wait(2)
        d3 = Tex("Licence word: UNIFORM acceleration").scale(1.05).shift(DOWN * 1.5)
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the four equations, each missing one ---
        self.next_band(1)
        b1t = Tex("Four equations, each missing one character").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"v_f = v_i + a\Delta t \quad (\text{no } \Delta x)").scale(0.95).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1a))
        self.wait(2)
        b1b = MathTex(r"\Delta x = v_i \Delta t + \tfrac{1}{2} a \Delta t^2 \quad (\text{no } v_f)").scale(0.95).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1b))
        self.wait(2)
        b1c = MathTex(r"v_f^2 = v_i^2 + 2a\Delta x \quad (\text{no } \Delta t)").scale(0.95).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1c))
        self.wait(2)
        b1d = MathTex(r"\Delta x = \tfrac{v_i + v_f}{2} \Delta t \quad (\text{no } a)").scale(0.95).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1d))
        self.wait(2)
        b1e = Tex("Exclude the absent character — that is the rule").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1e))
        self.play(Create(SurroundingRectangle(b1e, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the data audit and the choice ---
        self.next_band(2)
        b2t = Tex("The data audit").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = MathTex(r"v_i = 8 \text{ m/s}, \; v_f = 20 \text{ m/s}, \; \Delta x = 210 \text{ m}").scale(0.95).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2a))
        self.wait(2.5)
        b2b = Tex("Wanted: $a$. Absent: $\\Delta t$.").scale(1.05).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = MathTex(r"\Rightarrow \; v_f^2 = v_i^2 + 2a\Delta x").scale(1.1).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2c))
        self.play(Create(SurroundingRectangle(b2c, color=GREEN)))
        self.wait(2.5)
        b2d = Tex("Chosen by absence, not by luck").scale(1.0).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_2): substitute and solve ---
        self.next_band(3)
        b3t = Tex("Substitute and solve").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = MathTex(r"20^2 = 8^2 + 2a(210)").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3a))
        self.wait(2)
        b3b = MathTex(r"400 = 64 + 420a").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3b))
        self.wait(2)
        b3c = MathTex(r"336 = 420a \;\Rightarrow\; a = 0{,}8 \text{ m/s}^2").scale(1.05).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3c))
        self.play(Create(SurroundingRectangle(b3c, color=GREEN)))
        self.wait(2.5)
        b3d = Tex("Direction stated; size sensible — an ordinary pull-away").scale(0.9).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3d))
        self.wait(3)

        # --- Band 4 (subtopic_3): the time, road one ---
        self.next_band(4)
        b4t = Tex("The time — road one").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = MathTex(r"v_f = v_i + a\Delta t").scale(1.05).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4a))
        self.wait(2)
        b4b = MathTex(r"20 = 8 + 0{,}8\,\Delta t").scale(1.05).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4b))
        self.wait(2)
        b4c = MathTex(r"\Delta t = \frac{12}{0{,}8} = 15 \text{ s}").scale(1.1).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4c))
        self.play(Create(SurroundingRectangle(b4c, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): road two, the check ---
        self.next_band(5)
        b5t = Tex("Road two — the check").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = MathTex(r"\bar{v} = \frac{8 + 20}{2} = 14 \text{ m/s}").scale(1.05).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5a))
        self.wait(2.5)
        b5b = MathTex(r"210 = 14\,\Delta t \;\Rightarrow\; \Delta t = 15 \text{ s}").scale(1.05).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5b))
        self.play(Create(SurroundingRectangle(b5b, color=GREEN)))
        self.wait(2.5)
        b5c = Tex("Original data only — errors cannot hide").scale(1.0).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5c))
        self.wait(2)
        b5d = Tex("Two roads agreeing: the strongest check").scale(1.0).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5d))
        self.wait(3)

        # --- Band 6 (subtopic_4): the five-step method ---
        self.next_band(6)
        b6t = Tex("The method, five steps").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("1. Confirm uniform acceleration").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6b = Tex("2. List given, wanted, absent — convert units").scale(1.0).shift(band_shift(6) + UP * 0.3)
        b6c = Tex("3. Choose by the absent character").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        b6d = Tex("4. Substitute, solve, state units and direction").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        b6e = Tex("5. Sense-check; verify by a second road").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        for m in (b6a, b6b, b6c, b6d, b6e):
            self.play(Write(m))
            self.wait(1.8)
        self.wait(2)

        # --- Band 7 (subtopic_4): the traps ---
        self.next_band(7)
        b7t = Tex("The traps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = MathTex(r"72 \text{ km/h} \neq 72 \text{ m/s}").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.wait(2)
        b7b = MathTex(r"72 \div 3{,}6 = 20 \text{ m/s}").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7b))
        self.play(Create(SurroundingRectangle(b7b, color=GREEN)))
        self.wait(2)
        b7c = Tex("Half-squared velocities: 20 instead of 400").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7c))
        self.play(Create(strike(b7c)))
        self.wait(2)
        b7d = Tex("Braking: $a$ carries a minus sign").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7d))
        self.wait(2)
        b7e = Tex("Choose by absence, never by memory").scale(1.0).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7e))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): five facts about any trip ---
        self.next_band(8)
        b8t = Tex("Five facts about any trip").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Starting speed, final speed").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex("Rate of gaining speed, time, distance").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("Permission word: `uniformly'").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8c))
        self.play(Create(SurroundingRectangle(b8c, color=GREEN)))
        self.wait(2)
        b8d = Tex("Each equation is missing exactly one fact").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8d))
        self.wait(3)

        # --- Band 9 (subtopic_6): the one fact you don't need ---
        self.next_band(9)
        b9t = Tex("The one fact you don't need").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Given: 8 m/s, 20 m/s, 210 m. Wanted: $a$.").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = Tex("Nobody mentioned the TIME").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9b))
        self.wait(2)
        b9c = MathTex(r"400 = 64 + 420a \;\Rightarrow\; a = 0{,}8 \text{ m/s}^2").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9c))
        self.play(Create(SurroundingRectangle(b9c, color=GREEN)))
        self.wait(2.5)
        b9d = Tex("0,8 of fresh speed each second — believable").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9d))
        self.wait(3)

        # --- Band 10 (subtopic_7): checking the fare two ways ---
        self.next_band(10)
        b10t = Tex("Checking the fare two ways").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = MathTex(r"\text{Road 1: } 20 = 8 + 0{,}8\,\Delta t \Rightarrow 15 \text{ s}").scale(0.95).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = MathTex(r"\text{Road 2: } 210 = 14\,\Delta t \Rightarrow 15 \text{ s}").scale(0.95).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10b))
        self.play(Create(SurroundingRectangle(b10b, color=GREEN)))
        self.wait(2.5)
        b10c = Tex("Count your change twice — two agreeing counts").scale(0.95).shift(band_shift(10) + DOWN * 1.0)
        self.play(Write(b10c))
        self.wait(2)
        b10d = MathTex(r"\text{km/h} \div 3{,}6 = \text{m/s}; \text{ braking } a < 0").scale(0.95).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10d))
        self.wait(4)
