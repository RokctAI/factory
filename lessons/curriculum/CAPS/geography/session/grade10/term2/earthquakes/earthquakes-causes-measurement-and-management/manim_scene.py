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

# Band-layout whiteboard scene for "Earthquakes: causes, measurement and
# management" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Focus/epicentre section, triangulation circles and the wave story are
# hand-built from Line/Arrow/Dot/Circle/Tex; the Richter log calculation is
# worked line by line with the script's numbers.
# Subtopic durations (s): 220/225/230/255/185/180/195 of 1490.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EarthquakesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): elastic rebound, focus and epicentre ---
        title = Tex("Earthquakes: Cause and Measurement").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        e1 = Tex(r"Strain loads the rock; friction locks it;").scale(0.95).shift(UP * 1.4)
        e2 = Tex(r"it slips, snaps back: ELASTIC REBOUND").scale(0.95).shift(UP * 0.8)
        self.play(Write(e1))
        self.play(Write(e2))
        self.wait(2.5)
        gnd = Line(LEFT * 5.0 + DOWN * 0.4, RIGHT * 2.0 + DOWN * 0.4, stroke_width=6)
        self.play(Create(gnd))
        foc = Dot(LEFT * 1.6 + DOWN * 2.6, color=RED)
        foc_l = Tex("focus: rupture begins here").scale(0.85).shift(RIGHT * 2.5 + DOWN * 2.6)
        self.play(FadeIn(foc), Write(foc_l))
        self.wait(2)
        link = Line(LEFT * 1.6 + DOWN * 2.6, LEFT * 1.6 + DOWN * 0.4)
        epi = Dot(LEFT * 1.6 + DOWN * 0.4, color=YELLOW)
        epi_l = Tex("epicentre: surface point above").scale(0.85).shift(RIGHT * 2.7 + DOWN * 1.2)
        self.play(Create(link), FadeIn(epi), Write(epi_l))
        self.wait(3)

        # --- Band 1 (subtopic_1): depth and where they happen ---
        self.next_band(1)
        b1t = Tex("Depth decides destruction").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        d1 = Tex(r"Shallow: 0–70 km — most destructive").scale(1.0).shift(band_shift(1) + UP * 1.2)
        d2 = Tex(r"Intermediate: 70–300 km").scale(1.0).shift(band_shift(1) + UP * 0.4)
        d3 = Tex(r"Deep: 300–700 km, subduction only").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.wait(1.5)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex(r"Aftershocks finish weakened buildings").scale(0.95).shift(band_shift(1) + DOWN * 1.3)
        d5 = Tex(r"SA: Ceres–Tulbagh 1969; mining tremors").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(d4))
        self.wait(2)
        self.play(Write(d5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three waves ---
        self.next_band(2)
        b2t = Tex("Three seismic waves, fixed order").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        w1 = Tex(r"P: push-pull, fastest ($\approx$ 6 km/s),").scale(0.95).shift(band_shift(2) + UP * 1.2)
        w1b = Tex(r"first, passes through everything").scale(0.95).shift(band_shift(2) + UP * 0.6)
        w2 = Tex(r"S: sideways shake, half the speed,").scale(0.95).shift(band_shift(2) + DOWN * 0.2)
        w2b = Tex(r"second, blocked by liquids").scale(0.95).shift(band_shift(2) + DOWN * 0.8)
        w3 = Tex(r"Surface (L): slowest, largest swing,").scale(0.95).shift(band_shift(2) + DOWN * 1.6)
        w3b = Tex(r"does most of the damage").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(w1))
        self.play(Write(w1b))
        self.wait(2)
        self.play(Write(w2))
        self.play(Write(w2b))
        self.wait(2)
        self.play(Write(w3))
        self.play(Write(w3b))
        self.wait(2)
        w4 = Tex(r"Seismogram: quiet, P jump, S jump, roll").scale(0.9).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(w4))
        self.wait(3)

        # --- Band 3 (subtopic_2): triangulation ---
        self.next_band(3)
        b3t = Tex("Locating the epicentre").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        b3a = Tex(r"S-minus-P gap grows with distance —").scale(0.95).shift(band_shift(3) + UP * 1.3)
        b3a2 = Tex(r"like lightning, then thunder").scale(0.95).shift(band_shift(3) + UP * 0.7)
        self.play(Write(b3a))
        self.play(Write(b3a2))
        self.wait(2)
        s1 = Dot(band_shift(3) + LEFT * 3.0 + DOWN * 1.4, color=YELLOW)
        c1 = Circle(radius=1.6, color=BLUE).shift(band_shift(3) + LEFT * 3.0 + DOWN * 1.4)
        self.play(FadeIn(s1), Create(c1))
        s2 = Dot(band_shift(3) + RIGHT * 0.4 + DOWN * 2.2, color=YELLOW)
        c2 = Circle(radius=1.5, color=BLUE).shift(band_shift(3) + RIGHT * 0.4 + DOWN * 2.2)
        self.play(FadeIn(s2), Create(c2))
        s3 = Dot(band_shift(3) + LEFT * 1.2 + UP * 0.1, color=YELLOW)
        c3 = Circle(radius=1.4, color=BLUE).shift(band_shift(3) + LEFT * 1.2 + UP * 0.1)
        self.play(FadeIn(s3), Create(c3))
        self.wait(1.5)
        epi3 = Dot(band_shift(3) + LEFT * 1.5 + DOWN * 1.2, color=RED)
        epi3_l = Tex("three circles, one crossing point").scale(0.9).shift(band_shift(3) + RIGHT * 3.2 + DOWN * 0.8)
        self.play(FadeIn(epi3), Write(epi3_l))
        tri = Tex("= TRIANGULATION").scale(0.95).shift(band_shift(3) + RIGHT * 3.2 + DOWN * 1.6)
        self.play(Write(tri))
        self.play(Create(SurroundingRectangle(tri, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): Richter and the log calculation ---
        self.next_band(4)
        b4t = Tex("Richter measures MAGNITUDE (energy)").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        r1 = Tex(r"One quake = ONE Richter value").scale(1.0).shift(band_shift(4) + UP * 1.2)
        r2 = Tex(r"Each step: $\times 10$ amplitude, $\times 32$ energy").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex(r"Magnitude 7 is slightly stronger than 5").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(r3))
        self.play(Create(strike(r3)))
        self.wait(2)
        r4 = MathTex(r"10 \times 10 = 100 \times \text{ ground movement}").scale(1.0).shift(band_shift(4) + DOWN * 1.4)
        r5 = MathTex(r"32 \times 32 \approx 1\,000 \times \text{ energy}").scale(1.0).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(r4))
        self.wait(2)
        self.play(Write(r5))
        self.play(Create(SurroundingRectangle(r5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): Mercalli ---
        self.next_band(5)
        b5t = Tex("Mercalli measures INTENSITY (effects)").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        m1 = Tex(r"I to XII, Roman numerals, observed").scale(1.0).shift(band_shift(5) + UP * 1.2)
        m2 = Tex(r"IV: windows rattle; VII: hard to stand;").scale(0.95).shift(band_shift(5) + UP * 0.4)
        m2b = Tex(r"X: masonry destroyed").scale(0.95).shift(band_shift(5) + DOWN * 0.2)
        self.play(Write(m1))
        self.wait(2)
        self.play(Write(m2))
        self.play(Write(m2b))
        self.wait(2)
        m3 = Tex(r"One quake, MANY Mercalli values —").scale(1.0).shift(band_shift(5) + DOWN * 1.1)
        m3b = Tex(r"ground, depth and buildings differ").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(m3))
        self.play(Write(m3b))
        self.wait(2)
        m4 = Tex(r"Richter: the quake. Mercalli: the experience").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(m4))
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): effects, primary and secondary ---
        self.next_band(6)
        b6t = Tex("Primary and secondary effects").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        p1 = Tex(r"Primary: ground rupture, collapse of").scale(0.95).shift(band_shift(6) + UP * 1.2)
        p1b = Tex(r"buildings, bridges, pipelines").scale(0.95).shift(band_shift(6) + UP * 0.6)
        self.play(Write(p1))
        self.play(Write(p1b))
        self.wait(2)
        p2 = Tex(r"Secondary: fires, landslides,").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        p2b = Tex(r"liquefaction, floods, disease").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(p2))
        self.play(Write(p2b))
        self.wait(2)
        p3 = Tex(r"Sea-floor displacement lifts the water:").scale(0.95).shift(band_shift(6) + DOWN * 1.8)
        p3b = Tex(r"TSUNAMI at jet speed").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(p3))
        self.play(Write(p3b))
        self.play(Create(SurroundingRectangle(p3b, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): vulnerability and preparedness ---
        self.next_band(7)
        b7t = Tex("Why the same magnitude kills differently").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(1.5)
        v1 = Tex(r"Vulnerability: building quality, density,").scale(0.95).shift(band_shift(7) + UP * 1.2)
        v1b = Tex(r"wealth, time of day, ground conditions").scale(0.95).shift(band_shift(7) + UP * 0.6)
        self.play(Write(v1))
        self.play(Write(v1b))
        self.wait(2.5)
        v2 = Tex(r"Prediction is unreliable — so PREPARE:").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        self.play(Write(v2))
        self.wait(2)
        v3 = Tex(r"Engineering: base isolators, bracing").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        v4 = Tex(r"Planning: zoning + inspected codes").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        v5 = Tex(r"People: drop, cover, hold on; drills").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(v3))
        self.wait(1.5)
        self.play(Write(v4))
        self.wait(1.5)
        self.play(Write(v5))
        self.play(Create(SurroundingRectangle(v5, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): bending the ruler ---
        self.next_band(8)
        b8t = Tex("Bending the ruler until it goes").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        u1 = Tex(r"Bend, store, SNAP — elastic rebound").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(u1))
        self.play(Create(SurroundingRectangle(u1, color=GREEN)))
        self.wait(2)
        u2 = Tex(r"Focus: where the snap happened, below").scale(1.0).shift(band_shift(8) + UP * 0.2)
        u3 = Tex(r"Epicentre: the soccer field above it").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(u2))
        self.wait(2)
        self.play(Write(u3))
        self.wait(2)
        u4 = Tex(r"Shout from a deep shaft: barely heard").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        u5 = Tex(r"Shallow quakes arrive undiluted").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(u4))
        self.wait(2)
        self.play(Write(u5))
        u6 = Tex(r"Aftershocks finish cracked buildings").scale(0.9).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(u6))
        self.wait(3)

        # --- Band 9 (subtopic_6): thunder and three friends ---
        self.next_band(9)
        b9t = Tex("Thunder, and three friends with phones").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        t1 = Tex(r"P: fast squeeze; S: sideways ripple;").scale(0.95).shift(band_shift(9) + UP * 1.2)
        t1b = Tex(r"surface: slow roll that wrecks").scale(0.95).shift(band_shift(9) + UP * 0.6)
        self.play(Write(t1))
        self.play(Write(t1b))
        self.wait(2)
        t2 = Tex(r"Flash then bang: the wait = distance").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(t2))
        self.wait(2)
        cc1 = Circle(radius=1.1, color=BLUE).shift(band_shift(9) + LEFT * 3.0 + DOWN * 1.9)
        cc2 = Circle(radius=1.0, color=BLUE).shift(band_shift(9) + LEFT * 0.9 + DOWN * 2.3)
        cc3 = Circle(radius=1.0, color=BLUE).shift(band_shift(9) + LEFT * 1.9 + DOWN * 1.0)
        self.play(Create(cc1))
        self.play(Create(cc2))
        self.play(Create(cc3))
        px = Dot(band_shift(9) + LEFT * 1.9 + DOWN * 1.9, color=RED)
        t3 = Tex(r"three circles, one answer").scale(0.95).shift(band_shift(9) + RIGHT * 2.6 + DOWN * 1.7)
        self.play(FadeIn(px), Write(t3))
        self.play(Create(SurroundingRectangle(t3, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the amplifier and staying alive ---
        self.next_band(10)
        b10t = Tex("Two ways to score the same song").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        s1 = Tex(r"Richter = size of the amplifier: one number").scale(0.95).shift(band_shift(10) + UP * 1.2)
        s2 = Tex(r"Mercalli = how loud where YOU stood").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.wait(2)
        s3 = MathTex(r"7 \text{ vs } 5: \; 100 \times \text{ shaking}, \; 1\,000 \times \text{ energy}").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(s3))
        self.play(Create(SurroundingRectangle(s3, color=GREEN)))
        self.wait(2)
        s4 = Tex(r"Quakes don't kill; falling buildings do").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        s5 = Tex(r"Rubber pads, bracing, bedrock, zoning").scale(0.95).shift(band_shift(10) + DOWN * 2.3)
        s6 = Tex(r"Drop, cover, hold on — practise it").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(s4))
        self.wait(2)
        self.play(Write(s5))
        self.wait(2)
        self.play(Write(s6))
        self.wait(4)
