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

# Band-layout whiteboard scene for the session duo "Trig Graphs and Their
# Parameters" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier:
# subtopics 5-7). One band per teaching beat, add-only lifecycle, camera
# moves down. Only exporter-supported mobjects; write-only reveals. Band
# dwell times follow subtopics.json (240/235/235/255/200/190/205 of 1560 s);
# Level 6 rescales to real audio, so proportion is what matters.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TrigGraphsParametersSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the mother graphs
        title = Tex("Trig Graphs and Their Parameters").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        d1 = Tex(r"Sine: amplitude 1, period $360^\circ$ — starts climbing at 0").scale(0.95).shift(UP * 0.9)
        d2 = Tex(r"Cosine: same wave, opens at its maximum").scale(0.95).shift(UP * 0.0)
        d3 = Tex(r"Tangent: period $180^\circ$, walls at $90^\circ + k \cdot 180^\circ$, no amplitude").scale(0.9).shift(DOWN * 0.9)
        self.play(Write(d1))
        self.wait(2.5)
        self.play(Write(d2))
        self.wait(2.5)
        self.play(Write(d3))
        self.wait(2.5)
        d4 = Tex("Anchors first, smooth curve after — the whole craft").scale(0.95).shift(DOWN * 1.9)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): a and q
        self.next_band(1)
        b1_title = MathTex(r"y = 3\sin x - 1").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Stretch: swings $\pm 3$; lower by 1: from 2 down to $-4$").scale(0.95).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"\text{Max } 2 \text{ at } 90^\circ; \quad \text{min } -4 \text{ at } 270^\circ").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = MathTex(r"q = \frac{\text{max} + \text{min}}{2} = -1, \quad a = \frac{\text{max} - \text{min}}{2} = 3").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = Tex("Reading a sketch backwards: two divisions").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_3): the period control k
        self.next_band(2)
        b2_title = Tex("The period control $k$").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{New period} = \frac{360^\circ}{k} \; (\text{tan: } \frac{180^\circ}{k})").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = MathTex(r"\sin 3x: 120^\circ \quad \cos\tfrac{x}{2}: 720^\circ \quad \tan 3x: 60^\circ").scale(0.95).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex(r"$\tan 3x$ walls: $30^\circ$ plus multiples of $60^\circ$").scale(0.95).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = Tex(r"$k$ changes the period ONLY — heights untouched").scale(0.95).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_4): shifts and the combined sketch
        self.next_band(3)
        b3_title = MathTex(r"y = 2\sin(x - 30^\circ)").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Bracket-zero: the wave starts climbing at $30^\circ$").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex(r"Anchors: climb $30^\circ$, peak $120^\circ$, zero $210^\circ$, trough $300^\circ$").scale(0.9).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex(r"Then double the heights: peaks 2, troughs $-2$").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = MathTex(r"\text{Check } x = 0: \; 2\sin(-30^\circ) = -1").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex(r"$\cos x = \sin(x + 90^\circ)$ — one wave, two names").scale(0.95).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): the heartbeat
        self.next_band(4)
        b4_title = Tex("The heartbeat on the screen").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex("Two numbers pin any wave: swing height and beat length").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex(r"Top 2, bottom $-4$: middle $-1$, half-swing 3").scale(0.95).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"\Rightarrow y = 3\sin x - 1").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l2))
        self.wait(2.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex("Tangent: no peaks, only walls — never on a monitor").scale(0.9).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_6): fast-forward
        self.next_band(5)
        b5_title = Tex("The fast-forward button").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"$\sin 3x$: triple speed — a full verse in $120^\circ$").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex(r"Faster is NOT louder: still swings 1 to $-1$").scale(0.95).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex(r"Count cycles in the window: three waves $\Rightarrow k = 3$").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = Tex(r"Recipe: middle $\to q$, half-swing $\to a$, cycles $\to k$").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l3))
        self.wait(2.5)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_7): started later
        self.next_band(6)
        b6_title = Tex("The same song, started later").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"$\sin(x - 45^\circ)$: pressed play $45^\circ$ late — all right").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex(r"Cosine $=$ sine started $90^\circ$ early — the same recording").scale(0.95).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"$2\sin(x - 30^\circ)$: hum, delay 30, volume 2").scale(0.95).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = MathTex(r"\text{First note: } 2\sin(-30^\circ) = -1 \; \checkmark").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l3))
        self.wait(2.5)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2.5)
        b6_l5 = Tex("Volume, shelf, speed, start time — four knobs, read one at a time").scale(0.85).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l5))
        self.wait(4)
