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

# Band-layout whiteboard scene for the session duo "Trig Equations and General
# Solutions" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics
# 5-7). One band per teaching beat, add-only lifecycle, camera moves down.
# Only exporter-supported mobjects; write-only reveals, no sub-part
# transforms. Band dwell times follow subtopics.json
# (220/235/225/260/190/200/200 of 1530 s); Level 6 rescales to real audio.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TrigEquationsGeneralSolutionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): one equation, infinitely many answers
        title = Tex("Trig Equations and General Solutions").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        d1 = MathTex(r"\sin x = 0{,}5: \quad x = 30^\circ \;\text{— but not only!}").scale(1.05).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = MathTex(r"\sin(180^\circ - 30^\circ) = \sin 30^\circ").scale(1.0).shift(DOWN * 0.0)
        self.play(Write(d2))
        self.wait(2)
        d2b = MathTex(r"\Rightarrow \; x = 150^\circ \text{ too}").scale(1.0).shift(DOWN * 0.85)
        self.play(Write(d2b))
        self.wait(2)
        d3 = MathTex(r"\text{Full turns repeat it: } 390^\circ, -330^\circ, \dots").scale(1.05).shift(DOWN * 1.75)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex("Infinitely many answers — no list can hold them").scale(1.05).shift(DOWN * 2.6)
        self.play(Write(d4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the fixed four-step method
        self.next_band(1)
        b1_title = Tex("The method, same every time").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("1. Reference angle from the positive value").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("2. Sign of the value chooses the two quadrants").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("3. Write the solutions in the first turn").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = MathTex(r"4. \; + \, k \times \text{period}, \quad k \in \mathbb{Z}").scale(1.05).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_rule = Tex("Calculator answers once; quadrants double it;").scale(1.0).shift(band_shift(1) + DOWN * 2.5)
        b1_rule2 = Tex("the period multiplies it forever").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_rule))
        self.play(Write(b1_rule2))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the general solution formulae
        self.next_band(2)
        b2_title = Tex("General solutions for sine and cosine").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\sin x = \text{value, ref. angle } \alpha:").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"x = \alpha + k360^\circ \text{ or } 180^\circ - \alpha + k360^\circ").scale(0.85).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = MathTex(r"\cos x = \text{value, ref. angle } \alpha:").scale(1.05).shift(band_shift(2) + DOWN * 1.0)
        b2_l4 = MathTex(r"x = \pm\alpha + k \times 360^\circ").scale(1.1).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        b2_rule = Tex("Two families each, repeating every full turn").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_rule))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): cosine worked example
        self.next_band(3)
        b3_title = Tex(r"Solve $2\cos x - 1 = 0$").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\cos x = 0{,}5").scale(1.15).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{Reference angle: } 60^\circ, \text{ value positive}").scale(1.05).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"x = \pm 60^\circ + k360^\circ, \; k \in \mathbb{Z}").scale(1.1).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = MathTex(r"\text{Test: } 60^\circ, -60^\circ, 420^\circ \text{ all work}").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_2): negative value — the sign discipline
        self.next_band(4)
        b4_title = Tex(r"Solve $2\sin x + 1{,}2 = 0$").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_wrong = MathTex(r"\sin^{-1}(-0{,}6) = -36{,}87^\circ \;\text{then quadrants too}").scale(0.95).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2)
        b4_l1 = MathTex(r"\sin x = -0{,}6, \quad \text{ref. angle } 36{,}87^\circ").scale(1.05).shift(band_shift(4) + UP * 0.3)
        b4_l2 = MathTex(r"\text{Sine negative: Q3 and Q4}").scale(1.05).shift(band_shift(4) + DOWN * 0.6)
        b4_l3 = MathTex(r"\text{Q3: } 180^\circ + 36{,}87^\circ = 216{,}87^\circ").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        b4_l4 = MathTex(r"\text{Q4: } 360^\circ - 36{,}87^\circ = 323{,}13^\circ").scale(1.0).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = MathTex(r"x = 216{,}87^\circ \text{ or } 323{,}13^\circ, \; +k360^\circ").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): tangent's short period
        self.next_band(5)
        b5_title = Tex(r"Tangent repeats every $180^\circ$").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\tan x = 1: \;\; x = 45^\circ + k \times 180^\circ").scale(1.1).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2)
        b5_l2 = MathTex(r"\text{One family holds } 45^\circ \text{ and } 225^\circ").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"\tan x = -2{,}5: \quad \text{ref. angle } 68{,}2^\circ").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = MathTex(r"\text{Q2: } 180^\circ - 68{,}2^\circ = 111{,}8^\circ").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        b5_l5 = MathTex(r"x = 111{,}8^\circ + k \times 180^\circ").scale(1.1).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_3): tidying first, defending the division
        self.next_band(6)
        b6_title = Tex(r"Solve $\sin x = \cos x$").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\div \cos x: \quad \tan x = 1").scale(1.1).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"x = 45^\circ + k \times 180^\circ").scale(1.1).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        b6_l3 = Tex(r"Defence: if $\cos x = 0$ then $\sin x = \pm 1$,").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        b6_l4 = Tex(r"and $\pm 1 = 0$ is impossible — division safe").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_rule = Tex("Never divide by an expression in $x$ undefended").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_rule))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): harvesting an interval
        self.next_band(7)
        b7_title = Tex(r"$\sin x = 0{,}5$ on $[-360^\circ; 360^\circ]$").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"x = 30^\circ + k360^\circ \text{ or } 150^\circ + k360^\circ").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"30^\circ \checkmark \; 390^\circ \times \; -330^\circ \checkmark").scale(0.9).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"150^\circ \checkmark \; -210^\circ \checkmark").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"x \in \{-330^\circ; -210^\circ; 30^\circ; 150^\circ\}").scale(1.05).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        b7_rule = Tex("Two crossings per turn, two turns: four solutions").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_rule))
        self.wait(3)

        # --- Band 8 (subtopic_4): the hidden quadratic
        self.next_band(8)
        b8_title = Tex(r"Solve $2\sin^2 x - \sin x - 1 = 0$, $x \in [0^\circ; 360^\circ]$").scale(1.0).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\text{Let } s = \sin x: \quad 2s^2 - s - 1 = 0").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"(2s+1)(s-1) = 0 \Rightarrow s = -\tfrac{1}{2} \text{ or } 1").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"\sin x = -\tfrac{1}{2}: \;\; x = 210^\circ \text{ or } 330^\circ").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = MathTex(r"\sin x = 1: \;\; x = 90^\circ \;\text{(boundary — one door)}").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = MathTex(r"x \in \{90^\circ; 210^\circ; 330^\circ\}").scale(1.1).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the taxi on a loop
        self.next_band(9)
        b9_title = Tex("The taxi on a loop").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Seen at 7:00, loop takes an hour: 8, 9, 10 ... and 6, 5").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"\text{Every sighting} = 7\text{:}00 + k \text{ hours}").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\sin x = 0{,}5: \;\; x = 30^\circ + k \times 360^\circ").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex(r"$k$ counts full loops — forward or rewind").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        b9_l5 = Tex(r"Tangent's loop is tighter: $180^\circ$, half a turn").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.wait(2.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_6): two doors into the hall
        self.next_band(10)
        b10_title = Tex("Two doors into the hall").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Big wheel passes half-height going up AND coming down").scale(0.95).shift(band_shift(10) + UP * 1.1)
        b10_l2 = MathTex(r"30^\circ \text{ up}, \; 150^\circ \text{ down}").scale(1.0).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Cosine's doors are twins: $\pm\alpha + k \times 360^\circ$").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"Negative value? Size from $+0{,}6$, placing from the wheel").scale(0.95).shift(band_shift(10) + DOWN * 1.7)
        b10_l5 = Tex(r"Peak $\sin x = 1$: doors merge — $90^\circ + k360^\circ$").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l4))
        self.wait(2.5)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): harvesting the stretch
        self.next_band(11)
        b11_title = Tex("Harvesting the stretch you were given").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex(r"Permit $[-360^\circ; 360^\circ]$: run $k$, keep what fits").scale(0.95).shift(band_shift(11) + UP * 1.1)
        b11_l2 = MathTex(r"\text{Haul: } -330^\circ, -210^\circ, 30^\circ, 150^\circ").scale(1.05).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11_l1))
        self.wait(2.5)
        self.play(Write(b11_l2))
        self.play(Create(SurroundingRectangle(b11_l2, color=GREEN)))
        self.wait(2.5)
        b11_l3 = Tex(r"Nickname the padlock: $s = \sin x$ makes").scale(1.0).shift(band_shift(11) + DOWN * 0.8)
        b11_l4 = MathTex(r"2s^2 - s - 1 = (2s + 1)(s - 1) = 0").scale(1.05).shift(band_shift(11) + DOWN * 1.7)
        self.play(Write(b11_l3))
        self.wait(2)
        self.play(Write(b11_l4))
        self.wait(2.5)
        b11_l5 = Tex(r"Guard: $\sin x = 2$ is impossible — reject in writing").scale(1.0).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11_l5))
        self.wait(4)
