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

# Band-layout whiteboard scene for the rejuvenation / river-capture duo
# lesson. Exporter-safe primitives only (Tex/Line/Arrow/Dot/Circle/
# Rectangle/VGroup); add-only lifecycle; camera moves down one
# frame-height per band. Profiles, terraces and the capture plan are
# hand-built from Line chains and Arrows in script order.
#
# Subtopic shares (subtopics.json, total 1595 s):
# 235/250/245/245 expert, 200/205/215 simplifier. Bands 0-7 = Part 1
# (two per expert subtopic), bands 8-10 = fresh Part 2 bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RejuvenationRiverCaptureSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): graded profile, base level, definition ---
        title = Tex("Rejuvenation: made young again").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        # Graded concave profile
        p1 = Line(LEFT * 5.0 + UP * 1.0, LEFT * 2.8 + DOWN * 0.6, color=BLUE, stroke_width=5)
        p2 = Line(LEFT * 2.8 + DOWN * 0.6, RIGHT * 0.2 + DOWN * 1.5, color=BLUE, stroke_width=5)
        p3 = Line(RIGHT * 0.2 + DOWN * 1.5, RIGHT * 5.0 + DOWN * 1.8, color=BLUE, stroke_width=5)
        self.play(Create(p1), Create(p2), Create(p3))
        self.wait(2)
        base = Line(LEFT * 5.2 + DOWN * 1.8, RIGHT * 5.2 + DOWN * 1.8, color=YELLOW, stroke_width=3)
        base_lab = Tex(r"base level = the sea, the floor of erosion").scale(0.9).shift(DOWN * 2.5)
        self.play(Create(base))
        self.play(Write(base_lab))
        self.wait(2)
        d1 = Tex(r"Graded: energy and load in balance").scale(0.95).shift(UP * 1.6)
        self.play(Write(d1))
        self.wait(2)
        d2 = Tex(r"Rejuvenation: energy returns, cutting resumes").scale(0.95).shift(DOWN * 3.2)
        self.play(Write(d2))
        self.play(Create(SurroundingRectangle(d2, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the two families of causes ---
        self.next_band(1)
        b1_t = Tex("Two families of causes").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        c1 = Tex(r"1. Sea FALLS (eustatic): ice age locks up water").scale(0.95).shift(band_shift(1) + UP * 1.2)
        c2 = Tex(r"2. Land RISES (tectonic/isostatic uplift)").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(c1))
        self.wait(2.5)
        self.play(Write(c2))
        self.wait(2.5)
        c3 = Tex(r"Either way: gap to base level widens,").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        c3b = Tex(r"profile steepens, energy returns").scale(0.95).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(c3))
        self.play(Write(c3b))
        self.wait(2)
        c4 = Tex(r"(+ local trigger: increased discharge)").scale(0.9).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(c4))
        self.wait(2)
        c5 = Tex(r"Knickpoint migrates upstream like an opening zip").scale(0.9).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(c5))
        self.play(Create(SurroundingRectangle(c5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): signatures 1-2 — knickpoint + terraces ---
        self.next_band(2)
        b2_t = Tex("Signature 1: knickpoint; 2: terraces").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        # Profile with a step (knickpoint waterfall)
        k1 = Line(band_shift(2) + LEFT * 5.0 + UP * 0.8, band_shift(2) + LEFT * 1.6 + UP * 0.3, color=BLUE, stroke_width=5)
        k2 = Line(band_shift(2) + LEFT * 1.6 + UP * 0.3, band_shift(2) + LEFT * 1.6 + DOWN * 0.9, color=BLUE, stroke_width=5)
        k3 = Line(band_shift(2) + LEFT * 1.6 + DOWN * 0.9, band_shift(2) + RIGHT * 4.8 + DOWN * 1.6, color=BLUE, stroke_width=5)
        k_lab = Tex(r"knickpoint waterfall (Howick Falls)").scale(0.85).shift(band_shift(2) + LEFT * 1.4 + UP * 1.1)
        k_arr = Arrow(band_shift(2) + LEFT * 0.6 + DOWN * 0.1, band_shift(2) + LEFT * 2.8 + DOWN * 0.1, buff=0, color=RED)
        k_arr_lab = Tex(r"retreats upstream").scale(0.8).shift(band_shift(2) + LEFT * 1.7 + DOWN * 0.45)
        self.play(Create(k1), Create(k2), Create(k3))
        self.play(Write(k_lab))
        self.wait(2)
        self.play(Create(k_arr), Write(k_arr_lab))
        self.wait(2)
        t_lab = Tex(r"Terraces: old floodplain left as paired benches").scale(0.9).shift(band_shift(2) + DOWN * 2.3)
        t_lab2 = Tex(r"staircase of old floors, oldest on top").scale(0.9).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(t_lab))
        self.play(Write(t_lab2))
        self.play(Create(SurroundingRectangle(t_lab, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): valley-in-a-valley + incised meanders ---
        self.next_band(3)
        b3_t = Tex("Signature 3: valley-in-a-valley; 4: incised meanders").scale(1.0).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        # Cross-section: broad old valley with inner V
        o1 = Line(band_shift(3) + LEFT * 4.8 + UP * 1.2, band_shift(3) + LEFT * 2.4 + DOWN * 0.4, color=WHITE, stroke_width=4)
        o2 = Line(band_shift(3) + LEFT * 2.4 + DOWN * 0.4, band_shift(3) + LEFT * 0.8 + DOWN * 0.4, color=WHITE, stroke_width=4)
        v1 = Line(band_shift(3) + LEFT * 0.8 + DOWN * 0.4, band_shift(3) + DOWN * 1.6, color=RED, stroke_width=4)
        v2 = Line(band_shift(3) + DOWN * 1.6, band_shift(3) + RIGHT * 0.8 + DOWN * 0.4, color=RED, stroke_width=4)
        o3 = Line(band_shift(3) + RIGHT * 0.8 + DOWN * 0.4, band_shift(3) + RIGHT * 2.4 + DOWN * 0.4, color=WHITE, stroke_width=4)
        o4 = Line(band_shift(3) + RIGHT * 2.4 + DOWN * 0.4, band_shift(3) + RIGHT * 4.8 + UP * 1.2, color=WHITE, stroke_width=4)
        vv_lab = Tex(r"young V nested in old broad valley").scale(0.9).shift(band_shift(3) + DOWN * 2.3)
        ter_lab = Tex(r"benches = terraces").scale(0.8).shift(band_shift(3) + LEFT * 1.6 + UP * 0.2)
        self.play(Create(o1), Create(o2), Create(o3), Create(o4))
        self.wait(2)
        self.play(Create(v1), Create(v2))
        self.play(Write(vv_lab), Write(ter_lab))
        self.wait(2.5)
        im = Tex(r"Incised meanders: loops sunk in rock (Oribi Gorge)").scale(0.9).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(im))
        self.play(Create(SurroundingRectangle(im, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the capture mechanism ---
        self.next_band(4)
        b4_t = Tex("River capture: the mechanism").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        # Two parallel rivers and a divide
        strong = Line(band_shift(4) + LEFT * 4.6 + UP * 0.9, band_shift(4) + RIGHT * 4.6 + UP * 0.9, color=BLUE, stroke_width=6)
        weak = Line(band_shift(4) + LEFT * 4.6 + DOWN * 1.5, band_shift(4) + RIGHT * 4.6 + DOWN * 1.5, color=BLUE, stroke_width=3)
        ridge = Line(band_shift(4) + LEFT * 4.6 + DOWN * 0.3, band_shift(4) + RIGHT * 4.6 + DOWN * 0.3, color=GREY, stroke_width=3)
        s_lab = Tex(r"strong river: steeper, softer rock, more rain").scale(0.8).shift(band_shift(4) + UP * 1.5)
        w_lab = Tex(r"weak river").scale(0.8).shift(band_shift(4) + DOWN * 2.1 + LEFT * 3.6)
        r_lab = Tex(r"watershed").scale(0.75).shift(band_shift(4) + DOWN * 0.05 + RIGHT * 3.8)
        self.play(Create(strong), Write(s_lab))
        self.play(Create(ridge), Write(r_lab))
        self.play(Create(weak), Write(w_lab))
        self.wait(2)
        arm = Arrow(band_shift(4) + LEFT * 1.0 + UP * 0.8, band_shift(4) + LEFT * 1.6 + DOWN * 1.4, buff=0, color=RED)
        arm_lab = Tex(r"headward erosion bores through the divide").scale(0.85).shift(band_shift(4) + DOWN * 2.8)
        self.play(Create(arm))
        self.play(Write(arm_lab))
        self.wait(2)
        cap = Tex(r"Breakthrough: upper course diverts to the captor").scale(0.85).shift(band_shift(4) + UP * 2.9)
        self.play(Write(cap))
        self.play(Create(SurroundingRectangle(cap, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the five-piece vocabulary ---
        self.next_band(5)
        b5_t = Tex("Five labels on the capture diagram").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        f1 = Tex(r"1. Captor stream — the thief, enlarged").scale(0.95).shift(band_shift(5) + UP * 1.2)
        f2 = Tex(r"2. Captured stream — rerouted upper course").scale(0.95).shift(band_shift(5) + UP * 0.4)
        f3 = Tex(r"3. Elbow of capture — the right-angle confession").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        f4 = Tex(r"4. Misfit stream — tiny river, huge valley").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        f5 = Tex(r"5. Wind gap — dry valley through the ridge").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(f1))
        self.wait(2)
        self.play(Write(f2))
        self.wait(2)
        self.play(Write(f3))
        self.wait(2)
        self.play(Write(f4))
        self.wait(2)
        self.play(Write(f5))
        self.play(Create(SurroundingRectangle(f5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): significance for people ---
        self.next_band(6)
        b6_t = Tex("What it means for people").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        h1 = Tex(r"Captor side: water assurance, hydropower —").scale(0.9).shift(band_shift(6) + UP * 1.2)
        h1b = Tex(r"but an incising river undermines bridges").scale(0.9).shift(band_shift(6) + UP * 0.5)
        self.play(Write(h1))
        self.play(Write(h1b))
        self.wait(2.5)
        h2 = Tex(r"Victim side: shrinking river, sagging boreholes").scale(0.9).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(h2))
        self.wait(2)
        h3 = Tex(r"Wind gap: free pass for roads and rail").scale(0.9).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(h3))
        self.wait(2)
        h4 = Tex(r"Terraces: flat, fertile, flood-free — towns follow").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        h5 = Tex(r"Gorges: dam sites + scenery, but locked-away water").scale(0.9).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(h4))
        self.wait(2)
        self.play(Write(h5))
        self.play(Create(SurroundingRectangle(h4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the identification drill ---
        self.next_band(7)
        b7_t = Tex("Reading the evidence").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        r1 = Tex(r"Profile: step in the concave sweep = knickpoint").scale(0.9).shift(band_shift(7) + UP * 1.2)
        r2 = Tex(r"Cross-section: nested V + benches = rejuvenation").scale(0.9).shift(band_shift(7) + UP * 0.4)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex(r"Map: stacked flat strips edged by tight contours").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        r4 = Tex(r"Loops in crowded contours = incised meanders").scale(0.9).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(r3))
        self.wait(2)
        self.play(Write(r4))
        self.wait(2)
        r5 = Tex(r"Capture: elbow + dry gap + misfit — two clues confirm").scale(0.9).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(r5))
        self.play(Create(SurroundingRectangle(r5, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the old river wins the lottery ---
        self.next_band(8)
        b8_t = Tex("The old river wins the lottery").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        x1 = Tex(r"Young: cuts down. Old: wanders. Graded: settled").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(x1))
        self.wait(2)
        x2 = Tex(r"Finish line = base level = the sea").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(x2))
        self.wait(2)
        x3 = Tex(r"Sea drops or land lifts $\rightarrow$ higher above the line").scale(0.9).shift(band_shift(8) + DOWN * 0.4)
        x4 = Tex(r"Steeper $\rightarrow$ faster $\rightarrow$ powerful again").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(x3))
        self.wait(2)
        self.play(Write(x4))
        self.play(Create(SurroundingRectangle(x4, color=GREEN)))
        self.wait(2)
        x5 = Tex(r"Digging starts at the mouth and crawls upstream").scale(0.9).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(x5))
        self.wait(3)

        # --- Band 9 (subtopic_6): four clues the river got young ---
        self.next_band(9)
        b9_t = Tex("Four clues the river got young").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        y1 = Tex(r"1. Waterfall on the move (Howick knickpoint)").scale(0.95).shift(band_shift(9) + UP * 1.2)
        y2 = Tex(r"2. Old floors as balconies: paired terraces").scale(0.95).shift(band_shift(9) + UP * 0.4)
        y3 = Tex(r"3. Valley inside a valley (nested V)").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        y4 = Tex(r"4. The snake that sank: incised meanders").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(y1))
        self.wait(2)
        self.play(Write(y2))
        self.wait(2)
        self.play(Write(y3))
        self.wait(2)
        self.play(Write(y4))
        self.play(Create(SurroundingRectangle(y4, color=GREEN)))
        self.wait(2)
        y5 = Tex(r"Four clues, one verdict: youth restored").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(y5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the neighbour who stole the pipe ---
        self.next_band(10)
        b10_t = Tex("The neighbour who stole the pipe").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        z1 = Tex(r"Strong neighbour digs backwards through the wall").scale(0.9).shift(band_shift(10) + UP * 1.2)
        self.play(Write(z1))
        self.wait(2)
        z2 = Tex(r"Breakthrough: the upper course changes owners").scale(0.9).shift(band_shift(10) + UP * 0.4)
        self.play(Write(z2))
        self.wait(2)
        z3 = Tex(r"Exhibits: captor, captured, elbow, misfit, wind gap").scale(0.9).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(z3))
        self.play(Create(SurroundingRectangle(z3, color=GREEN)))
        self.wait(2.5)
        z4 = Tex(r"Elbow = signed confession on the map").scale(0.9).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(z4))
        self.wait(2)
        z5 = Tex(r"Thief rejuvenates; victim's valley silts and swamps").scale(0.9).shift(band_shift(10) + DOWN * 2.1)
        z5b = Tex(r"People inherit both outcomes").scale(0.9).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(z5))
        self.play(Write(z5b))
        self.wait(4)
