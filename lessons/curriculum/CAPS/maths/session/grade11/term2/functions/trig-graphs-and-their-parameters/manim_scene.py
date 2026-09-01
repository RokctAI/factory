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

import math

from manim import *

# Band-layout whiteboard scene for the session duo "Trig Graphs and Their
# Parameters" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier:
# subtopics 5-7). One band per teaching beat, add-only lifecycle, camera
# moves down. Only exporter-supported mobjects; curves drawn as chained Line
# segments; write-only reveals. Band dwell times follow subtopics.json
# (240/235/235/255/200/190/205 of 1560 s); Level 6 rescales to real audio.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def sine_polyline(origin, width, amp, color=YELLOW):
    """One full sine wave as a chain of Line segments (exporter-safe)."""
    pts = []
    for i in range(13):
        deg = 360 * i / 12
        x = origin[0] + width * i / 12
        y = origin[1] + amp * math.sin(math.radians(deg))
        pts.append([x, y, 0])
    return VGroup(*[Line(pts[i], pts[i + 1], color=color, stroke_width=4)
                    for i in range(len(pts) - 1)])


class TrigGraphsParametersSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the mother wave, drawn
        title = Tex("Trig Graphs and Their Parameters").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        ax = Arrow(LEFT * 3.2, RIGHT * 3.2, buff=0, stroke_width=3).shift(DOWN * 1.0)
        ay = Arrow(DOWN * 2.3, UP * 0.4, buff=0, stroke_width=3).shift(LEFT * 3.0)
        self.play(Create(ax), Create(ay))
        wave = sine_polyline([-3.0, -1.0], 5.8, 0.9)
        self.play(Create(wave), run_time=2)
        self.wait(1.5)
        w1 = MathTex(r"y = \sin x: 0, 1, 0, -1, 0 \text{ every } 90^\circ").scale(0.85).shift(UP * 0.9)
        self.play(Write(w1))
        self.wait(2.5)
        w2 = Tex(r"Amplitude 1; period $360^\circ$ — repeats forever").scale(0.95).shift(DOWN * 2.7)
        self.play(Write(w2))
        self.wait(2)
        w3 = Tex(r"Cosine: same wave, photographed at its peak").scale(0.95).shift(DOWN * 3.3)
        self.play(Write(w3))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): tangent the rebel, and anchors
        self.next_band(1)
        b1_title = Tex("Tangent is the rebel").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\tan 0^\circ = 0, \tan 45^\circ = 1, \tan 90^\circ: \text{n/a}").scale(0.95).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex(r"Vertical asymptotes at $90^\circ + k \times 180^\circ$").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"\text{Period } 180^\circ; \text{ no amplitude}").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex("Sketching craft: five anchor points per period,").scale(0.95).shift(band_shift(1) + DOWN * 1.7)
        b1_l5 = Tex("anchors first, smooth curve after").scale(0.95).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): a and q at work
        self.next_band(2)
        b2_title = Tex(r"Read $y = 2\sin x + 1$ as a work order").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Tension: heights double — swing $-2$ to $2$").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex(r"Crane: lift 1 — swing $-1$ to $3$, middle line $y = 1$").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{Max } 3 \text{ at } 90^\circ, \text{min } -1 \text{ at } 270^\circ").scale(0.9).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"\text{Range: } [-1; 3] \;\text{— waves touch their peaks}").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): running the machine backwards
        self.next_band(3)
        b3_title = Tex(r"From sketch to equation: max 3, min $-1$").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"q = \frac{3 + (-1)}{2} = 1 \;\text{(middle = average)}").scale(1.05).shift(band_shift(3) + UP * 1.0)
        b3_l2 = MathTex(r"a = \frac{3 - (-1)}{2} = 2 \;\text{(half the full swing)}").scale(1.05).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex(r"Negative $a$ flips the wave: $-\sin x$ dives first").scale(1.0).shift(band_shift(3) + DOWN * 1.1)
        b3_l4 = Tex("The flip moves the maxima, never the amplitude").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l3))
        self.wait(2.5)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the period rule
        self.next_band(4)
        b4_title = Tex(r"$k$ squeezes the wave: period $= \dfrac{360^\circ}{k}$").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\cos 2x: \frac{360^\circ}{2} = 180^\circ \text{ — two waves}").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"\sin \tfrac{1}{2}x: \frac{360^\circ}{1/2} = 720^\circ").scale(0.95).shift(band_shift(4) + UP * 0.1)
        b4_l3 = MathTex(r"\tan 2x: \text{period } 90^\circ, \text{ walls } 45^\circ + k90^\circ").scale(0.88).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2.5)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex(r"$k$ changes the period ONLY — heights untouched").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): compressed anchors
        self.next_band(5)
        b5_title = Tex(r"Sketch $y = \cos 2x$: divide every anchor by $k$").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\text{Max } 0^\circ, \text{min } 90^\circ").scale(1.05).shift(band_shift(5) + UP * 1.0)
        b5_l2 = MathTex(r"\text{zero } 135^\circ, \; \text{max } 180^\circ").scale(1.05).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("The cosine skeleton at half spacing —").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        b5_l4 = Tex("plot the compressed anchors, then curve smoothly").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): horizontal shifts
        self.next_band(6)
        b6_title = Tex(r"Shift: $y = \sin(x - 30^\circ)$ moves RIGHT").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Bracket-zero habit: at $x = 30^\circ$ the bracket is 0,").scale(0.95).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex(r"so the wave starts its climb at $30^\circ$").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(3)
        b6_l3 = MathTex(r"\text{Anchors: } 30^\circ, 120^\circ, 210^\circ, 300^\circ").scale(0.9).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"\cos x = \sin(x + 90^\circ)").scale(1.1).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        b6_l5 = Tex(r"Cosine is sine shifted $90^\circ$ to the left").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l5))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): the summit sketch
        self.next_band(7)
        b7_title = Tex(r"Summit sketch: $y = 2\cos(x - 60^\circ)$").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("1. Shape: cosine skeleton").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = MathTex(r"2. \; 60^\circ \text{ right: } 60^\circ, 150^\circ, 240^\circ").scale(0.9).shift(band_shift(7) + UP * 0.3)
        b7_l3 = Tex(r"3. Stretch: peaks at $2$, dips at $-2$").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"4. \text{ Check: } y(0) = 2\cos(-60^\circ) = 2 \times \tfrac{1}{2} = 1").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l5 = Tex("Anchors, shift, stretch, check — the order that never fails").scale(0.9).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the heartbeat on the screen
        self.next_band(8)
        b8_title = Tex("The heartbeat on the screen").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Amplitude: middle to peak. Period: one full repeat").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex(r"$a$ is the volume knob; $q$ carries the monitor up a shelf").scale(0.95).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Top 3, bottom $-1$: middle 1, half-swing 2").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = MathTex(r"y = 2\sin x + 1").scale(1.15).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l3))
        self.wait(2.5)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        b8_l5 = Tex("A picture became an equation in two divisions").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the fast-forward button
        self.next_band(9)
        b9_title = Tex("The fast-forward button").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"$\sin 2x$: the same song at double speed —").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"a full wave in $180^\circ$, but NOT louder").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(3)
        b9_l3 = Tex("Speed and volume are different knobs").scale(1.05).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex(r"Count waves in the window: two $\Rightarrow k = 2$").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        b9_l5 = Tex(r"Recipe: middle $\to q$, half-swing $\to a$, waves $\to k$").scale(0.95).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l4))
        self.wait(2.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the same song, started later
        self.next_band(10)
        b10_title = Tex("The same song, started later").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"$\sin(x - 30^\circ)$: pressed play $30^\circ$ late").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("Refuse the sign — ask where the bracket equals zero").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Cosine is sine started $90^\circ$ early — one song, two starts").scale(0.95).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"$2\cos(x - 60^\circ)$: hum, start late, volume up —").scale(0.95).shift(band_shift(10) + DOWN * 1.6)
        b10_l5 = MathTex(r"\text{then play the first note: } y(0) = 1 \;\checkmark").scale(1.0).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l4))
        self.wait(2.5)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
