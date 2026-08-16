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

# Band-layout whiteboard scene for "Reading contour lines" (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). Contour rings are Circles,
# valley Vs and slope profiles are short Line chains, everything labelled with
# Tex as it is drawn. Add-only lifecycle; camera moves down band by band.
# Subtopic durations (s): 210/230/220/260/180/190/185 of 1475.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ReadingContourLinesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): what a contour line is ---
        title = Tex("Reading Contour Lines").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex(r"A line joining points of EQUAL height").scale(1.05).shift(UP * 1.5)
        self.play(Write(d1))
        self.wait(2)
        ring1 = Circle(radius=2.0, color=WHITE).shift(DOWN * 1.0 + LEFT * 3.2)
        ring2 = Circle(radius=1.4, color=WHITE).shift(DOWN * 1.0 + LEFT * 3.2)
        ring3 = Circle(radius=0.8, color=WHITE).shift(DOWN * 1.0 + LEFT * 3.2)
        lab1 = Tex("820").scale(0.7).shift(DOWN * 1.0 + LEFT * 3.2 + DOWN * 2.25)
        lab2 = Tex("840").scale(0.7).shift(DOWN * 1.0 + LEFT * 3.2 + DOWN * 1.65)
        lab3 = Tex("860").scale(0.7).shift(DOWN * 1.0 + LEFT * 3.2 + DOWN * 1.05)
        self.play(Create(ring1), Write(lab1))
        self.play(Create(ring2), Write(lab2))
        self.play(Create(ring3), Write(lab3))
        self.wait(2)
        spot = Dot(DOWN * 1.0 + LEFT * 3.2, color=YELLOW)
        spotl = Tex("913").scale(0.8).shift(DOWN * 0.6 + LEFT * 2.6)
        self.play(FadeIn(spot), Write(spotl))
        n1 = Tex(r"Interval: 20 m between lines").scale(0.95).shift(DOWN * 0.2 + RIGHT * 3.1)
        n2 = Tex(r"Spot height 913 = exact summit").scale(0.95).shift(DOWN * 1.0 + RIGHT * 3.2)
        self.play(Write(n1))
        self.wait(1.5)
        self.play(Write(n2))
        self.wait(3)

        # --- Band 1 (subtopic_1): the three rules ---
        self.next_band(1)
        b1t = Tex("Three rules of contour lines").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        r1 = Tex(r"1. Contours never cross").scale(1.1).shift(band_shift(1) + UP * 1.1)
        r2 = Tex(r"2. They never just end — loop or edge").scale(1.1).shift(band_shift(1) + UP * 0.2)
        r3 = Tex(r"3. Index contours: thicker, labelled").scale(1.1).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2)
        self.play(Write(r3))
        self.wait(2)
        r4 = Tex(r"Point between 820 and 840 lines:").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        r5 = Tex(r"height between 820 m and 840 m").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(r4))
        self.play(Write(r5))
        self.play(Create(SurroundingRectangle(r5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): spacing is gradient ---
        self.next_band(2)
        b2t = Tex("Closer lines = steeper slope").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        b2a = Tex(r"Rise is fixed: 20 m per interval").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2b = Tex(r"Run varies: the walk between lines").scale(1.0).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2a))
        self.wait(2)
        self.play(Write(b2b))
        self.wait(2)
        # gentle: widely spaced verticals; steep: crowded verticals
        g_lines = VGroup(*[
            Line(UP * 0.5, DOWN * 0.5).shift(band_shift(2) + DOWN * 1.2 + LEFT * (4.2 - i * 1.1))
            for i in range(4)
        ])
        g_lab = Tex("gentle").scale(0.9).shift(band_shift(2) + DOWN * 2.2 + LEFT * 2.6)
        self.play(Create(g_lines), Write(g_lab))
        self.wait(1.5)
        s_lines = VGroup(*[
            Line(UP * 0.5, DOWN * 0.5).shift(band_shift(2) + DOWN * 1.2 + RIGHT * (1.6 + i * 0.3))
            for i in range(4)
        ])
        s_lab = Tex("steep").scale(0.9).shift(band_shift(2) + DOWN * 2.2 + RIGHT * 2.1)
        self.play(Create(s_lines), Write(s_lab))
        self.wait(2)
        b2c = Tex(r"Same rise, shorter run = steeper").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2c))
        self.play(Create(SurroundingRectangle(b2c, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): concave vs convex ---
        self.next_band(3)
        b3t = Tex("Slope shapes from spacing").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        # concave profile: steep at top, flattening at foot (3 segments)
        cc1 = Line(band_shift(3) + LEFT * 4.3 + UP * 1.2, band_shift(3) + LEFT * 3.7 + DOWN * 0.2, color=BLUE)
        cc2 = Line(band_shift(3) + LEFT * 3.7 + DOWN * 0.2, band_shift(3) + LEFT * 2.7 + DOWN * 0.9, color=BLUE)
        cc3 = Line(band_shift(3) + LEFT * 2.7 + DOWN * 0.9, band_shift(3) + LEFT * 1.2 + DOWN * 1.2, color=BLUE)
        cc_lab = Tex(r"Concave: crowded at top,").scale(0.85).shift(band_shift(3) + LEFT * 2.9 + DOWN * 1.9)
        cc_lab2 = Tex(r"whole slope visible").scale(0.85).shift(band_shift(3) + LEFT * 2.9 + DOWN * 2.5)
        self.play(Create(cc1))
        self.play(Create(cc2))
        self.play(Create(cc3))
        self.play(Write(cc_lab))
        self.play(Write(cc_lab2))
        self.wait(2.5)
        # convex profile: gentle at top, steepening down
        cv1 = Line(band_shift(3) + RIGHT * 0.8 + UP * 1.2, band_shift(3) + RIGHT * 2.3 + UP * 0.9, color=YELLOW)
        cv2 = Line(band_shift(3) + RIGHT * 2.3 + UP * 0.9, band_shift(3) + RIGHT * 3.3 + UP * 0.2, color=YELLOW)
        cv3 = Line(band_shift(3) + RIGHT * 3.3 + UP * 0.2, band_shift(3) + RIGHT * 3.9 + DOWN * 1.2, color=YELLOW)
        cv_lab = Tex(r"Convex: crowded at bottom,").scale(0.85).shift(band_shift(3) + RIGHT * 2.9 + DOWN * 1.9)
        cv_lab2 = Tex(r"blind spot below the shoulder").scale(0.85).shift(band_shift(3) + RIGHT * 2.9 + DOWN * 2.5)
        self.play(Create(cv1))
        self.play(Create(cv2))
        self.play(Create(cv3))
        self.play(Write(cv_lab))
        self.play(Write(cv_lab2))
        self.wait(3)

        # --- Band 4 (subtopic_3): the V rule ---
        self.next_band(4)
        b4t = Tex("River valley: the V points uphill").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        # three V-shaped contours, tips pointing right (uphill), river flowing left
        for i, h in enumerate(["800", "820", "840"]):
            x = -1.6 + i * 1.7
            va = Line(band_shift(4) + RIGHT * (x - 1.2) + UP * 1.4, band_shift(4) + RIGHT * x + DOWN * 0.1)
            vb = Line(band_shift(4) + RIGHT * x + DOWN * 0.1, band_shift(4) + RIGHT * (x - 1.2) + DOWN * 1.6)
            vl = Tex(h).scale(0.7).shift(band_shift(4) + RIGHT * (x - 1.3) + UP * 1.7)
            self.play(Create(va), Create(vb), Write(vl), run_time=0.9)
        self.wait(2)
        riv = Arrow(band_shift(4) + RIGHT * 2.4 + DOWN * 0.1, band_shift(4) + LEFT * 4.0 + DOWN * 0.1,
                    buff=0, color=BLUE)
        rivl = Tex("river flows out of the open Vs").scale(0.9).shift(band_shift(4) + DOWN * 2.3)
        self.play(Create(riv))
        self.play(Write(rivl))
        self.wait(2)
        up_lab = Tex("uphill").scale(0.9).shift(band_shift(4) + RIGHT * 3.6 + UP * 1.5)
        self.play(Write(up_lab))
        self.wait(3)

        # --- Band 5 (subtopic_3): the spur trap ---
        self.next_band(5)
        b5t = Tex("The mirror-image trap: the spur").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        b5w = Tex(r"Bend + river? Must be a spur").scale(1.05).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5w))
        self.play(Create(strike(b5w)))
        self.wait(2)
        b5a = Tex(r"Valley: V points uphill, river inside").scale(1.05).shift(band_shift(5) + UP * 0.2)
        b5b = Tex(r"Spur: bulge points downhill, no river").scale(1.05).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5a))
        self.wait(2)
        self.play(Write(b5b))
        self.wait(2)
        b5c = Tex(r"Settle it with heights: flow must go").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        b5d = Tex(r"840 $\Rightarrow$ 820 $\Rightarrow$ 800, never up").scale(1.05).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5c))
        self.play(Write(b5d))
        self.play(Create(SurroundingRectangle(b5d, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the whole landscape ---
        self.next_band(6)
        b6t = Tex("Feature patterns to recognise").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        f1 = Tex(r"Hill: closed rings, rising inward").scale(1.0).shift(band_shift(6) + UP * 1.2)
        f2 = Tex(r"Ridge: stretched closed contours").scale(1.0).shift(band_shift(6) + UP * 0.4)
        f3 = Tex(r"Saddle: dip between two summits").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        f4 = Tex(r"Cliff: contours almost touching").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        f5 = Tex(r"Plain: hardly any contours").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(f1))
        self.wait(1.5)
        self.play(Write(f2))
        self.wait(1.5)
        self.play(Write(f3))
        self.wait(1.5)
        self.play(Write(f4))
        self.wait(1.5)
        self.play(Write(f5))
        self.wait(3)

        # --- Band 7 (subtopic_4): five-step exam method ---
        self.next_band(7)
        b7t = Tex("Question 3 method — five steps").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(1.5)
        s1 = Tex(r"1. Read the interval from the key (20 m)").scale(0.95).shift(band_shift(7) + UP * 1.2)
        s2 = Tex(r"2. Index contours: which way is up?").scale(0.95).shift(band_shift(7) + UP * 0.5)
        s3 = Tex(r"3. Identify features by pattern").scale(0.95).shift(band_shift(7) + DOWN * 0.2)
        s4 = Tex(r"4. Confirm with the heights").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        s5 = Tex(r"5. Answer with evidence: spacing + heights").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(s1))
        self.wait(1.5)
        self.play(Write(s2))
        self.wait(1.5)
        self.play(Write(s3))
        self.wait(1.5)
        self.play(Write(s4))
        self.wait(1.5)
        self.play(Write(s5))
        self.wait(2)
        b7ans = Tex(r"Name the feature, quote the evidence").scale(1.05).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7ans))
        self.play(Create(SurroundingRectangle(b7ans, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): walking the hill ---
        self.next_band(8)
        b8t = Tex("A contour is a level walk").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        k1 = Circle(radius=1.7, color=WHITE).shift(band_shift(8) + LEFT * 3.0 + DOWN * 0.7)
        k2 = Circle(radius=1.1, color=WHITE).shift(band_shift(8) + LEFT * 3.0 + DOWN * 0.7)
        k3 = Circle(radius=0.5, color=WHITE).shift(band_shift(8) + LEFT * 3.0 + DOWN * 0.7)
        self.play(Create(k1))
        self.play(Create(k2))
        self.play(Create(k3))
        b8a = Tex(r"A koppie in a stack of tyres,").scale(0.95).shift(band_shift(8) + RIGHT * 2.4 + UP * 0.9)
        b8a2 = Tex(r"each ring 20 m higher").scale(0.95).shift(band_shift(8) + RIGHT * 2.4 + UP * 0.3)
        self.play(Write(b8a))
        self.play(Write(b8a2))
        self.wait(2)
        b8b = Tex(r"Lines cannot cross: one spot,").scale(0.95).shift(band_shift(8) + RIGHT * 2.4 + DOWN * 0.7)
        b8b2 = Tex(r"one height").scale(0.95).shift(band_shift(8) + RIGHT * 2.4 + DOWN * 1.3)
        self.play(Write(b8b))
        self.play(Write(b8b2))
        self.wait(2)
        spot2 = Dot(band_shift(8) + LEFT * 3.0 + DOWN * 0.7, color=YELLOW)
        b8c = Tex(r"Dot 913: one person with a name tag").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(FadeIn(spot2))
        self.play(Write(b8c))
        self.play(Create(SurroundingRectangle(b8c, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): ramp vs staircase ---
        self.next_band(9)
        b9t = Tex("Squeezed lines, sore legs").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        ramp = Line(band_shift(9) + LEFT * 4.4 + DOWN * 1.6, band_shift(9) + LEFT * 0.6 + DOWN * 0.6, color=BLUE)
        ramp_l = Tex("ramp: gentle, lines far apart").scale(0.85).shift(band_shift(9) + LEFT * 2.5 + DOWN * 2.3)
        self.play(Create(ramp), Write(ramp_l))
        self.wait(2)
        st1 = Line(band_shift(9) + RIGHT * 1.6 + DOWN * 1.6, band_shift(9) + RIGHT * 2.2 + DOWN * 0.7, color=YELLOW)
        st2 = Line(band_shift(9) + RIGHT * 2.2 + DOWN * 0.7, band_shift(9) + RIGHT * 2.8 + UP * 0.2, color=YELLOW)
        stair_l = Tex("staircase: steep, lines squeezed").scale(0.85).shift(band_shift(9) + RIGHT * 2.7 + DOWN * 2.3)
        self.play(Create(st1), Create(st2), Write(stair_l))
        self.wait(2)
        b9a = Tex(r"Both climb 20 m — the run differs").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9a))
        self.play(Create(SurroundingRectangle(b9a, color=GREEN)))
        self.wait(2)
        b9b = Tex(r"Lines touching = cliff, not a misprint").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9b))
        self.wait(3)

        # --- Band 10 (subtopic_7): the stubborn walker ---
        self.next_band(10)
        b10t = Tex("Finding the river without the blue").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex(r"The stubborn walker stays at 840 m —").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10a2 = Tex(r"she detours up the valley to cross").scale(1.0).shift(band_shift(10) + UP * 0.6)
        self.play(Write(b10a))
        self.play(Write(b10a2))
        self.wait(2)
        wa = Line(band_shift(10) + LEFT * 3.6 + DOWN * 0.6, band_shift(10) + LEFT * 1.4 + DOWN * 1.4)
        wb = Line(band_shift(10) + LEFT * 1.4 + DOWN * 1.4, band_shift(10) + RIGHT * 0.8 + DOWN * 0.6)
        wl = Tex("her path: a V pointing upstream").scale(0.85).shift(band_shift(10) + LEFT * 1.4 + DOWN * 2.1)
        self.play(Create(wa))
        self.play(Create(wb))
        self.play(Write(wl))
        self.wait(2)
        b10b = Tex(r"Spur: bulge the other way, no water").scale(1.0).shift(band_shift(10) + RIGHT * 1.6 + UP * 0.0)
        self.play(Write(b10b))
        self.wait(2)
        b10c = Tex(r"Numbers settle it: 840, 820, 800").scale(1.0).shift(band_shift(10) + DOWN * 2.8 + LEFT * 1.0)
        b10d = Tex(r"= downstream").scale(1.0).shift(band_shift(10) + DOWN * 2.8 + RIGHT * 3.2)
        self.play(Write(b10c))
        self.play(Write(b10d))
        self.play(Create(SurroundingRectangle(VGroup(b10c, b10d), color=GREEN)))
        self.wait(4)
