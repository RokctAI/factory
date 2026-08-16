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

# Band-layout whiteboard scene for the fluvial-processes duo on river
# rejuvenation and river capture. Exporter-safe primitives only
# (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/VGroup); add-only lifecycle;
# camera moves down one frame-height per band. The knickpoint profile,
# valley-in-a-valley cross-section and capture plan are chained-Line
# diagrams with Arrows and Tex labels, built element by element.
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
        title = Tex("Rejuvenation: A River Made Young Again").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        g1 = Tex(r"Graded profile: smooth concave curve,").scale(1.0).shift(UP * 1.3)
        g1b = Tex(r"erosion $\approx$ deposition along its length").scale(1.0).shift(UP * 0.5)
        self.play(Write(g1))
        self.play(Write(g1b))
        self.wait(2.5)
        g2 = Tex(r"Base level: lowest level a river can erode to").scale(1.0).shift(DOWN * 0.5)
        g3 = Tex(r"— ultimately SEA LEVEL").scale(1.0).shift(DOWN * 1.3)
        self.play(Write(g2))
        self.wait(2)
        self.play(Write(g3))
        self.wait(2)
        g4 = Tex(r"Rejuvenation: energy regained, the river").scale(1.0).shift(DOWN * 2.2)
        g4b = Tex(r"cuts DOWNWARD like a young river again").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(g4))
        self.play(Write(g4b))
        self.play(Create(SurroundingRectangle(g4b, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the two families of causes ---
        self.next_band(1)
        b1_t = Tex("Two families of causes").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        c1 = Tex(r"1. Base level DROPS (eustatic): ice-age sea").scale(1.0).shift(band_shift(1) + UP * 1.2)
        c1b = Tex(r"falls, mouth hangs high, lower reach steepens").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(c1))
        self.play(Write(c1b))
        self.wait(2.5)
        c2 = Tex(r"2. Land RISES (tectonic/isostatic): plateau").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        c2b = Tex(r"uplift steepens every gradient").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(c2))
        self.play(Write(c2b))
        self.wait(2.5)
        c3 = Tex(r"(+ extra discharge, e.g. after capture)").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(c3))
        self.wait(2)
        c4 = Tex(r"Knickpoint retreats upstream like an opening zip").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(c4))
        self.play(Create(SurroundingRectangle(c4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): signatures 1-2 — knickpoint + terraces ---
        self.next_band(2)
        b2_t = Tex("Signatures 1--2: knickpoint, terraces").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        # Profile with a step: old gentle curve, sharp knickpoint, new lower curve
        k1 = Line(band_shift(2) + LEFT * 5.0 + UP * 1.0, band_shift(2) + LEFT * 1.0 + UP * 0.4,
                  color=YELLOW, stroke_width=5)
        k2 = Line(band_shift(2) + LEFT * 1.0 + UP * 0.4, band_shift(2) + LEFT * 0.4 + DOWN * 0.8,
                  color=YELLOW, stroke_width=5)
        k3 = Line(band_shift(2) + LEFT * 0.4 + DOWN * 0.8, band_shift(2) + RIGHT * 4.8 + DOWN * 1.4,
                  color=YELLOW, stroke_width=5)
        kd = Dot(band_shift(2) + LEFT * 1.0 + UP * 0.4, color=RED)
        k_lab = Tex(r"KNICKPOINT: waterfall (Augrabies)").scale(0.9).shift(band_shift(2) + RIGHT * 2.2 + UP * 0.6)
        k_arr = Arrow(band_shift(2) + LEFT * 0.6 + UP * 1.4, band_shift(2) + LEFT * 2.4 + UP * 1.4,
                      buff=0, color=RED)
        k_arr_lab = Tex(r"retreats upstream").scale(0.8).shift(band_shift(2) + LEFT * 1.5 + UP * 1.8)
        self.play(Create(k1))
        self.play(Create(k2), Create(k3))
        self.play(Create(kd), Write(k_lab))
        self.play(Create(k_arr), Write(k_arr_lab))
        self.wait(2.5)
        t1 = Tex(r"Terraces: the river slices its own floodplain —").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        t2 = Tex(r"paired flat benches, a staircase, oldest on top").scale(0.95).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(t1))
        self.wait(2)
        self.play(Write(t2))
        self.wait(3)

        # --- Band 3 (subtopic_2): valley-in-a-valley + incised meanders ---
        self.next_band(3)
        b3_t = Tex("Signatures 3--4: nested valley, sunken loops").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        # Cross-section: broad old valley with young V incised in its floor
        o1 = Line(band_shift(3) + LEFT * 5.0 + UP * 1.2, band_shift(3) + LEFT * 2.4 + DOWN * 0.6,
                  color=WHITE, stroke_width=4)
        o2 = Line(band_shift(3) + LEFT * 2.4 + DOWN * 0.6, band_shift(3) + LEFT * 0.8 + DOWN * 0.6,
                  color=WHITE, stroke_width=4)
        o3 = Line(band_shift(3) + RIGHT * 0.8 + DOWN * 0.6, band_shift(3) + RIGHT * 2.4 + DOWN * 0.6,
                  color=WHITE, stroke_width=4)
        o4 = Line(band_shift(3) + RIGHT * 2.4 + DOWN * 0.6, band_shift(3) + RIGHT * 5.0 + UP * 1.2,
                  color=WHITE, stroke_width=4)
        v1 = Line(band_shift(3) + LEFT * 0.8 + DOWN * 0.6, band_shift(3) + DOWN * 1.8,
                  color=YELLOW, stroke_width=5)
        v2 = Line(band_shift(3) + DOWN * 1.8, band_shift(3) + RIGHT * 0.8 + DOWN * 0.6,
                  color=YELLOW, stroke_width=5)
        n_lab = Tex(r"young V in the old valley floor").scale(0.9).shift(band_shift(3) + UP * 0.2)
        tr_lab = Tex(r"benches = terraces").scale(0.85).shift(band_shift(3) + LEFT * 3.3 + DOWN * 1.2)
        self.play(Create(o1), Create(o2), Create(o3), Create(o4))
        self.play(Create(v1), Create(v2))
        self.play(Write(n_lab), Write(tr_lab))
        self.wait(2.5)
        im1 = Tex(r"Incised meanders: loops sunk into rock gorges").scale(0.95).shift(band_shift(3) + DOWN * 2.4)
        im2 = Tex(r"Entrenched: symmetric; ingrown: one gentle side").scale(0.95).shift(band_shift(3) + DOWN * 3.2)
        self.play(Write(im1))
        self.wait(2)
        self.play(Write(im2))
        self.wait(3)

        # --- Band 4 (subtopic_3): the capture mechanism ---
        self.next_band(4)
        b4_t = Tex("River capture: the theft of a river").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        # Two parallel rivers with a watershed between them
        strong = Line(band_shift(4) + LEFT * 4.6 + UP * 1.0, band_shift(4) + RIGHT * 4.6 + UP * 0.4,
                      color=BLUE, stroke_width=5)
        strong_lab = Tex(r"strong river: steeper, softer rock").scale(0.85).shift(band_shift(4) + UP * 1.5 + RIGHT * 1.6)
        weak = Line(band_shift(4) + LEFT * 4.6 + DOWN * 1.8, band_shift(4) + RIGHT * 4.6 + DOWN * 2.2,
                    color=BLUE, stroke_width=5)
        weak_lab = Tex(r"weak river").scale(0.85).shift(band_shift(4) + DOWN * 1.4 + RIGHT * 3.6)
        wsh = DashedLine(band_shift(4) + LEFT * 4.6 + DOWN * 0.6, band_shift(4) + RIGHT * 4.6 + DOWN * 0.8,
                         color=GREY)
        wsh_lab = Tex(r"watershed").scale(0.8).shift(band_shift(4) + LEFT * 3.6 + DOWN * 0.2)
        self.play(Create(strong), Write(strong_lab))
        self.play(Create(wsh), Write(wsh_lab))
        self.play(Create(weak), Write(weak_lab))
        self.wait(2)
        head = Arrow(band_shift(4) + LEFT * 1.4 + UP * 0.7, band_shift(4) + LEFT * 2.6 + DOWN * 1.9,
                     buff=0, color=RED)
        head_lab = Tex(r"headward erosion gnaws the divide").scale(0.85).shift(band_shift(4) + DOWN * 0.1 + RIGHT * 1.8)
        self.play(Create(head), Write(head_lab))
        self.wait(2.5)
        brk = Tex(r"Breakthrough: water takes the steeper, lower").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        brk2 = Tex(r"exit — the upper course drains to the thief").scale(0.95).shift(band_shift(4) + DOWN * 3.6)
        self.play(Write(brk))
        self.play(Write(brk2))
        self.wait(3)

        # --- Band 5 (subtopic_3): the five-piece vocabulary ---
        self.next_band(5)
        b5_t = Tex("Five labels on the capture diagram").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        v5a = Tex(r"1. Captor stream — the thief, now swollen").scale(0.95).shift(band_shift(5) + UP * 1.2)
        v5b = Tex(r"2. Captured stream — the stolen upper course").scale(0.95).shift(band_shift(5) + UP * 0.4)
        v5c = Tex(r"3. Elbow of capture — the unnatural $90^\circ$ bend").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        v5d = Tex(r"4. Misfit stream — too small for its valley").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        v5e = Tex(r"5. Wind gap — dry valley with no river in it").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(v5a))
        self.wait(2)
        self.play(Write(v5b))
        self.wait(2)
        self.play(Write(v5c))
        self.wait(2)
        self.play(Write(v5d))
        self.wait(2)
        self.play(Write(v5e))
        self.wait(2)
        v5f = Tex(r"After: captor rejuvenates; victim silts + swamps").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(v5f))
        self.play(Create(SurroundingRectangle(v5f, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): significance for people ---
        self.next_band(6)
        b6_t = Tex("What it means for people").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        h1 = Tex(r"Captor side: more water for irrigation, towns —").scale(0.95).shift(band_shift(6) + UP * 1.2)
        h1b = Tex(r"but an incising river undermines bridges").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(h1))
        self.play(Write(h1b))
        self.wait(2.5)
        h2 = Tex(r"Victim side: boreholes drop, schemes shrink").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        h3 = Tex(r"Wind gap: a ready-made pass for road and rail").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(h2))
        self.wait(2)
        self.play(Write(h3))
        self.wait(2)
        h4 = Tex(r"Terraces: flat, fertile, flood-free — old towns").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        h5 = Tex(r"Gorges: dam sites + scenery, but lethal floods").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(h4))
        self.wait(2)
        self.play(Write(h5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the identification drill ---
        self.next_band(7)
        b7_t = Tex("Reading it off the map").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        m1 = Tex(r"Long profile: sharp step = knickpoint").scale(0.95).shift(band_shift(7) + UP * 1.2)
        m2 = Tex(r"Cross-section: V nested in broad valley + benches").scale(0.95).shift(band_shift(7) + UP * 0.4)
        m3 = Tex(r"Contours: stacked flats beside river = terraces;").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        m3b = Tex(r"tight loops crowded both banks = incised meander").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(m1))
        self.wait(2)
        self.play(Write(m2))
        self.wait(2)
        self.play(Write(m3))
        self.play(Write(m3b))
        self.wait(2.5)
        m4 = Tex(r"Capture: elbow bend + dry notch (wind gap)").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        m4b = Tex(r"+ thin stream in an oversized valley (misfit)").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Write(m4b))
        self.play(Create(SurroundingRectangle(m4b, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the old river wins the lottery ---
        self.next_band(8)
        b8_t = Tex("The old river wins the lottery").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        p1 = Tex(r"Graded = the settled pensioner: lazy curve,").scale(1.0).shift(band_shift(8) + UP * 1.2)
        p1b = Tex(r"finish line = base level = the sea").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(p1))
        self.play(Write(p1b))
        self.wait(2.5)
        p2 = Tex(r"Sea falls OR land rises: the gap to the").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        p2b = Tex(r"finish line widens — steeper, faster, powerful").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(p2))
        self.play(Write(p2b))
        self.wait(2.5)
        p3 = Tex(r"Re-juvenation: made young again").scale(1.05).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(p3))
        self.play(Create(SurroundingRectangle(p3, color=GREEN)))
        self.wait(2)
        p4 = Tex(r"Digging starts at the bottom, crawls upstream").scale(0.95).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(p4))
        self.wait(3)

        # --- Band 9 (subtopic_6): four clues the river got young ---
        self.next_band(9)
        b9_t = Tex("Four clues the river got young").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        q1 = Tex(r"1. Waterfall on the stairs — the knickpoint,").scale(0.95).shift(band_shift(9) + UP * 1.2)
        q1b = Tex(r"chewing upstream (Augrabies)").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(q1))
        self.play(Write(q1b))
        self.wait(2.5)
        q2 = Tex(r"2. Old floors left as shelves — paired terraces,").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        q2b = Tex(r"bunk beds on both walls, oldest on top").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(q2))
        self.play(Write(q2b))
        self.wait(2.5)
        q3 = Tex(r"3. Valley-in-a-valley: young V in the old floor").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(q3))
        self.wait(2)
        q4 = Tex(r"4. The sunken snake: incised meanders (Blyde)").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(q4))
        self.play(Create(SurroundingRectangle(q4, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the neighbour who stole the pipe ---
        self.next_band(10)
        b10_t = Tex("The neighbour who stole the pipe").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        r1 = Tex(r"Strong river's arm reaches back: headward").scale(1.0).shift(band_shift(10) + UP * 1.2)
        r1b = Tex(r"erosion tunnels through the boundary wall").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(r1))
        self.play(Write(r1b))
        self.wait(2.5)
        r2 = Tex(r"Breakthrough: the weak river's top half").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        r2b = Tex(r"pours into the thief — piracy complete").scale(1.0).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(r2))
        self.play(Write(r2b))
        self.wait(2.5)
        r3 = Tex(r"Exhibits: captor, captured, elbow ($90^\circ$").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        r3b = Tex(r"confession), misfit trickle, dry wind gap").scale(0.95).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(r3))
        self.play(Write(r3b))
        self.play(Create(SurroundingRectangle(r3b, color=GREEN)))
        self.wait(2.5)
        r4 = Tex(r"Thief rejuvenates; victim's valley swamps").scale(0.95).shift(band_shift(10) + DOWN * 3.3)
        self.play(Write(r4))
        self.wait(4)
