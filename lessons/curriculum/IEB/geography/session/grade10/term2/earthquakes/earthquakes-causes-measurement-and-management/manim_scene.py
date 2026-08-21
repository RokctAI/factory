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

# Band-layout whiteboard scene for "Earthquakes: Causes, Measurement and
# Management" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# The focus/epicentre section, triangulation circles and splash-ripple
# sketches are built from Line/Circle/Dot/Arrow/Tex.
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
        title = Tex("Earthquakes: Cause, Measure, Manage").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        ground = Line(LEFT * 5.0 + UP * 0.6, RIGHT * 5.0 + UP * 0.6, color=WHITE)
        self.play(Create(ground))
        focus = Dot(DOWN * 1.6 + LEFT * 1.0, color=RED)
        epi = Dot(UP * 0.6 + LEFT * 1.0, color=YELLOW)
        link = Line(DOWN * 1.6 + LEFT * 1.0, UP * 0.6 + LEFT * 1.0, color=GREY)
        self.play(Create(focus))
        f_l = Tex(r"FOCUS: rupture starts here").scale(0.85).shift(DOWN * 1.6 + RIGHT * 2.6)
        self.play(Write(f_l))
        self.wait(1.5)
        self.play(Create(link), Create(epi))
        e_l = Tex(r"EPICENTRE: surface point above").scale(0.85).shift(UP * 1.2 + RIGHT * 2.6)
        self.play(Write(e_l))
        self.wait(2)
        r1 = Tex(r"Elastic rebound: strain stores like a").scale(0.9).shift(DOWN * 2.5 + LEFT * 0.4)
        r1b = Tex(r"drawn bow, fault slips, rock springs back").scale(0.9).shift(DOWN * 3.1 + LEFT * 0.4)
        self.play(Write(r1))
        self.play(Write(r1b))
        self.play(Create(SurroundingRectangle(r1b, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): depth and where they happen ---
        self.next_band(1)
        b1t = Tex("Depth is destiny").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        d1 = Tex(r"Shallow: 0–70 km — the killers").scale(0.95).shift(band_shift(1) + UP * 1.2)
        d2 = Tex(r"Intermediate: 70–300 km").scale(0.95).shift(band_shift(1) + UP * 0.5)
        d3 = Tex(r"Deep: 300–700 km, subduction only").scale(0.95).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.wait(1.5)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex(r"Belts: Ring of Fire, Med–Himalaya, ridges").scale(0.9).shift(band_shift(1) + DOWN * 1.2)
        d5 = Tex(r"SA: mid-plate — mining tremors;").scale(0.9).shift(band_shift(1) + DOWN * 2.0)
        d5b = Tex(r"Orkney 2014, magnitude $5{,}5$").scale(0.9).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(d4))
        self.wait(2)
        self.play(Write(d5))
        self.play(Write(d5b))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three waves ---
        self.next_band(2)
        b2t = Tex("Three waves, fixed order").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        w1 = Tex(r"P: squeeze, $\sim$6 km/s, crosses anything").scale(0.9).shift(band_shift(2) + UP * 1.2)
        w2 = Tex(r"S: sideways whip, half speed,").scale(0.9).shift(band_shift(2) + UP * 0.4)
        w2b = Tex(r"drowns in liquid").scale(0.9).shift(band_shift(2) + DOWN * 0.2)
        w3 = Tex(r"Surface: slowest, largest —").scale(0.9).shift(band_shift(2) + DOWN * 1.0)
        w3b = Tex(r"the demolition crew").scale(0.9).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(w1))
        self.wait(2)
        self.play(Write(w2))
        self.play(Write(w2b))
        self.wait(2)
        self.play(Write(w3))
        self.play(Write(w3b))
        self.play(Create(SurroundingRectangle(w3b, color=GREEN)))
        self.wait(2)
        w4 = Tex(r"Seismogram: twitch, kick, wide swing").scale(0.9).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(w4))
        self.wait(3)

        # --- Band 3 (subtopic_2): triangulation ---
        self.next_band(3)
        b3t = Tex("Triangulation").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        t1 = Tex(r"S-minus-P gap grows with distance").scale(0.95).shift(band_shift(3) + UP * 1.2)
        self.play(Write(t1))
        self.wait(2)
        c1 = Circle(radius=1.5, color=BLUE).shift(band_shift(3) + LEFT * 2.2 + DOWN * 0.8)
        c2 = Circle(radius=1.2, color=GREEN).shift(band_shift(3) + RIGHT * 1.6 + DOWN * 1.3)
        c3 = Circle(radius=1.1, color=YELLOW).shift(band_shift(3) + DOWN * 0.1 + RIGHT * 0.1)
        self.play(Create(c1))
        self.play(Create(c2))
        self.play(Create(c3))
        cross = Dot(band_shift(3) + LEFT * 0.7 + DOWN * 0.9, color=RED)
        self.play(Create(cross))
        t2 = Tex(r"Three stations, three circles,").scale(0.9).shift(band_shift(3) + DOWN * 2.5 + LEFT * 1.8)
        t2b = Tex(r"one crossing point").scale(0.9).shift(band_shift(3) + DOWN * 3.1 + LEFT * 1.8)
        self.play(Write(t2))
        self.play(Write(t2b))
        self.play(Create(SurroundingRectangle(t2b, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): Richter and the log calculation ---
        self.next_band(4)
        b4t = Tex("Richter: one number, log scale").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        m1 = Tex(r"Magnitude = energy at the focus,").scale(0.9).shift(band_shift(4) + UP * 1.2)
        m1b = Tex(r"ONE value per earthquake").scale(0.9).shift(band_shift(4) + UP * 0.6)
        self.play(Write(m1))
        self.play(Write(m1b))
        self.wait(2)
        m2 = Tex(r"Each step: $\times$10 motion, $\times$32 energy").scale(0.95).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(m2))
        self.play(Create(SurroundingRectangle(m2, color=GREEN)))
        self.wait(2)
        m3 = Tex(r"8 vs 6: $10\times10 = 100\times$ motion,").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        m3b = Tex(r"$32\times32 \approx 1\,000\times$ energy").scale(0.95).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(m3))
        self.play(Write(m3b))
        self.wait(2)
        m4 = Tex(r"Record: $9{,}5$, Chile 1960").scale(0.9).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(m4))
        self.wait(3)

        # --- Band 5 (subtopic_3): Mercalli ---
        self.next_band(5)
        b5t = Tex("Mercalli: many numbers").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        i1 = Tex(r"Intensity = observed effects, I–XII").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(i1))
        self.wait(2)
        i2 = Tex(r"II: felt by a few at rest").scale(0.9).shift(band_shift(5) + UP * 0.4)
        i3 = Tex(r"V: sleepers wake, crockery breaks").scale(0.9).shift(band_shift(5) + DOWN * 0.2)
        i4 = Tex(r"VIII: chimneys and weak walls fall").scale(0.9).shift(band_shift(5) + DOWN * 0.8)
        i5 = Tex(r"XII: damage total").scale(0.9).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(i2))
        self.play(Write(i3))
        self.play(Write(i4))
        self.play(Write(i5))
        self.wait(2.5)
        i6 = Tex(r"One event, many intensities —").scale(0.9).shift(band_shift(5) + DOWN * 2.3)
        i6b = Tex(r"soft ground amplifies, bedrock spares").scale(0.9).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(i6))
        self.play(Write(i6b))
        self.play(Create(SurroundingRectangle(i6b, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): effects, primary and secondary ---
        self.next_band(6)
        b6t = Tex("Primary, then secondary").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        p1 = Tex(r"PRIMARY: rupture, collapsing structures").scale(0.9).shift(band_shift(6) + UP * 1.2)
        self.play(Write(p1))
        self.wait(2)
        p2 = Tex(r"SECONDARY: fires, landslides,").scale(0.9).shift(band_shift(6) + UP * 0.3)
        p2b = Tex(r"liquefaction (Christchurch 2011),").scale(0.9).shift(band_shift(6) + DOWN * 0.3)
        p2c = Tex(r"floods, disease, homelessness").scale(0.9).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(p2))
        self.play(Write(p2b))
        self.play(Write(p2c))
        self.wait(2.5)
        p3 = Tex(r"Sea-floor throw $\Rightarrow$ TSUNAMI —").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        p3b = Tex(r"Indian Ocean 2004").scale(0.9).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(p3))
        self.play(Write(p3b))
        self.wait(3)

        # --- Band 7 (subtopic_4): vulnerability and preparedness ---
        self.next_band(7)
        b7t = Tex("Vulnerability decides the toll").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(1.5)
        v1 = Tex(r"Chile $8{,}8$ vs Haiti $7{,}0$, 2010:").scale(0.9).shift(band_shift(7) + UP * 1.2)
        v1b = Tex(r"$\sim$500$\times$ the energy, far fewer deaths").scale(0.9).shift(band_shift(7) + UP * 0.6)
        self.play(Write(v1))
        self.play(Write(v1b))
        self.play(Create(SurroundingRectangle(v1b, color=GREEN)))
        self.wait(2.5)
        v2 = Tex(r"Buildings, density, wealth, timing, ground").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(v2))
        self.wait(2)
        v3 = Tex(r"Prepare: base isolation, bracing;").scale(0.85).shift(band_shift(7) + DOWN * 1.3)
        v3b = Tex(r"zoning off faults and soft ground;").scale(0.85).shift(band_shift(7) + DOWN * 1.9)
        v3c = Tex(r"drills, kits, seconds of warning").scale(0.85).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(v3))
        self.play(Write(v3b))
        self.play(Write(v3c))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): snapping the branch ---
        self.next_band(8)
        b8t = Tex("Snapping the branch").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        s1 = Tex(r"Bend, bend, CRACK — both halves").scale(0.95).shift(band_shift(8) + UP * 1.2)
        s1b = Tex(r"spring straight, palms sting").scale(0.95).shift(band_shift(8) + UP * 0.6)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2)
        s2 = Tex(r"Slow bend = years of loading;").scale(0.9).shift(band_shift(8) + DOWN * 0.3)
        s2b = Tex(r"snap = fault slips; sting = shaking").scale(0.9).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(s2))
        self.play(Write(s2b))
        self.play(Create(SurroundingRectangle(s2b, color=GREEN)))
        self.wait(2)
        s3 = Tex(r"Focus underground, epicentre above;").scale(0.9).shift(band_shift(8) + DOWN * 1.8)
        s3b = Tex(r"firecracker under the lid: shallow is deadly").scale(0.9).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(s3))
        self.play(Write(s3b))
        self.wait(3)

        # --- Band 9 (subtopic_6): starter's gun and cell towers ---
        self.next_band(9)
        b9t = Tex("The starter's gun and the towers").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        g1 = Tex(r"Three runners: P squeeze, S whip,").scale(0.9).shift(band_shift(9) + UP * 1.2)
        g1b = Tex(r"surface roller — never a tie").scale(0.9).shift(band_shift(9) + UP * 0.6)
        self.play(Write(g1))
        self.play(Write(g1b))
        self.wait(2)
        g2 = Tex(r"Smoke now, bang later:").scale(0.9).shift(band_shift(9) + DOWN * 0.3)
        g2b = Tex(r"the gap announces the distance").scale(0.9).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(g2))
        self.play(Write(g2b))
        self.wait(2)
        g3 = Tex(r"Like cell towers finding a phone:").scale(0.9).shift(band_shift(9) + DOWN * 1.8)
        g3b = Tex(r"three circles, one crossing — epicentre").scale(0.9).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(g3))
        self.play(Write(g3b))
        self.play(Create(SurroundingRectangle(g3b, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): one splash, many ripples ---
        self.next_band(10)
        b10t = Tex("One splash, many ripples").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        splash = Dot(band_shift(10) + UP * 0.9 + LEFT * 2.8, color=BLUE)
        rip1 = Circle(radius=0.5, color=BLUE).shift(band_shift(10) + UP * 0.9 + LEFT * 2.8)
        rip2 = Circle(radius=1.0, color=BLUE).shift(band_shift(10) + UP * 0.9 + LEFT * 2.8)
        self.play(Create(splash), Create(rip1), Create(rip2))
        q1 = Tex(r"Splash = Richter: one number").scale(0.9).shift(band_shift(10) + UP * 1.2 + RIGHT * 2.6)
        q1b = Tex(r"Ripples = Mercalli: one per shore").scale(0.9).shift(band_shift(10) + UP * 0.6 + RIGHT * 2.6)
        self.play(Write(q1))
        self.play(Write(q1b))
        self.wait(2)
        q2 = Tex(r"Two steps: $100\times$ shaking, $1\,000\times$ energy").scale(0.9).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(q2))
        self.play(Create(SurroundingRectangle(q2, color=GREEN)))
        self.wait(2)
        q3 = Tex(r"Buildings kill, not quakes:").scale(0.9).shift(band_shift(10) + DOWN * 1.5)
        q3b = Tex(r"codes, drills, solid ground win —").scale(0.9).shift(band_shift(10) + DOWN * 2.1)
        q3c = Tex(r"drop, cover, hold on").scale(0.9).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(q3))
        self.play(Write(q3b))
        self.play(Write(q3c))
        self.wait(4)
