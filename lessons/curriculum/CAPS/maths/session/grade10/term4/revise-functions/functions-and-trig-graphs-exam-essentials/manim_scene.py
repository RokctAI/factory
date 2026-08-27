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

# Band layout: one frame-height band per teaching beat; the camera moves down
# to fresh space and earlier work stays on the canvas. Only exporter-supported
# mobjects; curves are drawn as short Line segment chains; every line of
# working is a single-string MathTex revealed with Write — no sub-part
# transforms.
#
# Mirrors script.md across all seven subtopics (Part 1 — Expert: 1-4;
# Part 2 — Simplifier: 5-7), band time roughly proportional to subtopics.json
# (230/240/240/250/180/190/170 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class FunctionsTrigGraphsEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the family album and the elevator q
        title = Tex("Functions and Trig Graphs: Exam Essentials").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"y = ax + q \quad y = ax^2 + q \quad y = \tfrac{a}{x} + q").scale(0.95).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = MathTex(r"y = a b^x + q \quad y = a\sin x + q").scale(0.95).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"$q$ is the elevator: the whole graph rides up").scale(1.05).shift(DOWN * 0.9)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex(r"$x^2 + 2$: bowl raised to $(0; 2)$; midline of").scale(1.0).shift(DOWN * 1.8)
        b0_l5 = Tex(r"$\sin x + 1$ runs along $y = 1$").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the volume knob a
        self.next_band(1)
        b1_title = Tex("$a$ is the volume knob, with a twist").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex(r"Bigger $a$: narrower bowl, taller wave").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex(r"On waves, $a$ is the AMPLITUDE: midline to peak").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex(r"Negative $a$ flips: bowls become domes").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = MathTex(r"y = -2\sin x + 1:").scale(1.1).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4))
        self.wait(1.5)
        b1_l5 = Tex(r"flipped, amplitude 2, midline at 1").scale(1.05).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the parabola routine
        self.next_band(2)
        b2_title = Tex(r"Parabola routine: $y = x^2 - 9$").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"x = 0: \; y = -9 \quad \to \quad (0; -9)").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"y = 0: \; (x-3)(x+3) = 0").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"x = 3 \quad \text{or} \quad x = -3").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex(r"Turning point $(0; -9)$; upright bowl ($a > 0$)").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = MathTex(r"\text{Range: } y \ge -9").scale(1.05).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the line and the intersection
        self.next_band(3)
        b3_title = Tex(r"Where does $y = x - 3$ cut the parabola?").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"x^2 - 9 = x - 3").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"x^2 - x - 6 = 0").scale(1.1).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"(x-3)(x+2) = 0 \Rightarrow x = 3 \text{ or } -2").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"(3; 0) \quad \text{and} \quad (-2; -5)").scale(1.1).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex(r"Parabola below the line: $-2 < x < 3$").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the hyperbola
        self.next_band(4)
        b4_title = Tex(r"Hyperbola: $y = \dfrac{6}{x} + 1$").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        vline = DashedLine(UP * 1.2, DOWN * 1.2).shift(band_shift(4) + LEFT * 3.0)
        hline = DashedLine(LEFT * 3.0, LEFT * 0.8).shift(band_shift(4) + UP * 0.0)
        self.play(Create(vline), Create(hline))
        b4_lab = Tex(r"$x = 0$ and $y = 1$: draw them dotted FIRST").scale(0.95).shift(band_shift(4) + RIGHT * 1.4 + UP * 1.2)
        self.play(Write(b4_lab))
        self.wait(2.5)
        b4_l1 = MathTex(r"(2; 4), \; (6; 2), \; (-1; -5)").scale(1.0).shift(band_shift(4) + RIGHT * 1.4 + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"y = 0: \; \tfrac{6}{x} = -1 \Rightarrow x = -6").scale(1.0).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Domain: $x \neq 0$. \; Range: $y \neq 1$").scale(1.05).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the exponential
        self.next_band(5)
        b5_title = Tex(r"Exponential: $y = 2^x + 1$").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"One asymptote: $y = 1$, the $q$ value").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"2^x > 0 \text{ always, so } y > 1 \text{ forever}").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"(0; 2), \; (1; 3), \; (2; 5), \; (-2; 1\tfrac{1}{4})").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"\text{Range: } y > 1").scale(1.1).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex(r"Fingerprint: $x$ downstairs = 2 asymptotes;").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): trig fingerprints with the sine wave
        self.next_band(6)
        b6_title = Tex(r"Trig graphs, $0^\circ$ to $360^\circ$").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        axis = Line(LEFT * 3.2, RIGHT * 3.2).shift(band_shift(6) + UP * 0.4)
        self.play(Create(axis))
        pts = [(0, 0), (45, 0.71), (90, 1), (135, 0.71), (180, 0),
               (225, -0.71), (270, -1), (315, -0.71), (360, 0)]
        segs = VGroup(*[
            Line(LEFT * 3.2 + RIGHT * (x1 / 60.0) + UP * (0.4 + y1),
                 LEFT * 3.2 + RIGHT * (x2 / 60.0) + UP * (0.4 + y2),
                 color=YELLOW).shift(band_shift(6))
            for (x1, y1), (x2, y2) in zip(pts, pts[1:])
        ])
        self.play(Create(segs), run_time=2)
        lbl_90 = MathTex(r"90^\circ").scale(0.8).shift(band_shift(6) + LEFT * 1.7 + UP * 0.0)
        lbl_270 = MathTex(r"270^\circ").scale(0.8).shift(band_shift(6) + RIGHT * 1.3 + UP * 0.8)
        self.play(Write(lbl_90), Write(lbl_270))
        self.wait(2)
        b6_l1 = Tex(r"Sine: 0, peak 1 at $90^\circ$, dip $-1$ at $270^\circ$").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex(r"Cosine: same wave, STARTS at its peak").scale(0.95).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex(r"Tangent: unbounded; asymptotes $90^\circ$, $270^\circ$").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l3))
        self.wait(3)

        # --- Band 7 (subtopic_4): the dials on the wave
        self.next_band(7)
        b7_title = Tex(r"$y = 2\sin x + 1$: dials on the wave").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"\text{Max} = 1 + 2 = 3 \text{ at } 90^\circ").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"\text{Min} = 1 - 2 = -1 \text{ at } 270^\circ").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"\text{Range: } -1 \le y \le 3").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex(r"$q$ changes heights, never timing").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex(r"$\sin x = \tfrac{1}{2}$: the line cuts the wave twice").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the volume knob and the lift
        self.next_band(8)
        b8_title = Tex("The volume knob and the lift").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"$+q$ carries the whole picture upstairs;").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"the forbidden height rides the lift too").scale(1.05).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(3)
        b8_l3 = Tex(r"Turn $a$ up: steeper, narrower, taller").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex(r"Negative $a$: the flip switch").scale(1.05).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex(r"Read the dials ALOUD before sketching").scale(1.05).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): reading a graph like a story
        self.next_band(9)
        b9_title = Tex("Reading a graph: four verbs").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"LOCATE: intercepts, turning points, asymptotes").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"COMPARE: below the line from $-2$ to $3$").scale(0.95).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{MEASURE: } (-3) - (-9) = 6 \text{ units at } x = 0").scale(0.95).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex(r"COUNT: crossings of a horizontal line — two").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex(r"The graph is the evidence — read from it").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the sketching checklist
        self.next_band(10)
        b10_title = Tex("The sketching checklist").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"1. Name the family from the fingerprint").scale(0.95).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex(r"2. Read the dials: $a$ and $q$").scale(0.95).shift(band_shift(10) + UP * 0.6)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex(r"3. Draw the skeleton: dotted asymptotes, midline").scale(0.95).shift(band_shift(10) + DOWN * 0.1)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex(r"4. Compute the anchors: intercepts, key angles").scale(0.95).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex(r"5. Sweep the curve — never cross a dotted line").scale(0.95).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l5))
        self.wait(2)
        b10_l6 = Tex(r"6. State domain and range if asked").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
