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

# Band-layout whiteboard scene for "Inside the Earth" (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). The layered-earth
# cross-section is concentric Circles with Tex labels; the farm-dam rafts
# and shadow-zone sketches are built from Line/Rectangle/Tex.
# Subtopic durations (s): 225/230/245/235/185/180/190 of 1490.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class InsideTheEarthSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the layered earth ---
        title = Tex("Inside the Earth").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        crust = Circle(radius=2.4, color=WHITE).shift(DOWN * 0.9 + LEFT * 3.0)
        mantle = Circle(radius=1.8, color=ORANGE).shift(DOWN * 0.9 + LEFT * 3.0)
        outer = Circle(radius=1.0, color=RED).shift(DOWN * 0.9 + LEFT * 3.0)
        inner = Circle(radius=0.45, color=YELLOW).shift(DOWN * 0.9 + LEFT * 3.0)
        self.play(Create(crust))
        c_l = Tex(r"crust: 5–70 km, under 1\%").scale(0.85).shift(UP * 1.3 + RIGHT * 3.0)
        self.play(Write(c_l))
        self.wait(1.5)
        self.play(Create(mantle))
        m_l = Tex(r"mantle: 2 900 km, 84\% —").scale(0.85).shift(UP * 0.5 + RIGHT * 3.0)
        m_l2 = Tex(r"SOLID peridotite").scale(0.85).shift(DOWN * 0.1 + RIGHT * 3.0)
        self.play(Write(m_l), Write(m_l2))
        self.wait(2)
        self.play(Create(outer))
        o_l = Tex(r"outer core: LIQUID Fe-Ni,").scale(0.85).shift(DOWN * 0.9 + RIGHT * 3.1)
        o_l2 = Tex(r"the planet's dynamo").scale(0.85).shift(DOWN * 1.5 + RIGHT * 3.1)
        self.play(Write(o_l), Write(o_l2))
        self.wait(2)
        self.play(Create(inner))
        i_l = Tex(r"inner core: solid, 5–6 000$^\circ$C —").scale(0.85).shift(DOWN * 2.4 + RIGHT * 3.0)
        i_l2 = Tex(r"pressure wins the argument").scale(0.85).shift(DOWN * 3.0 + RIGHT * 3.0)
        self.play(Write(i_l), Write(i_l2))
        self.wait(3)

        # --- Band 1 (subtopic_1): discontinuities and asthenosphere ---
        self.next_band(1)
        b1t = Tex("Boundaries and the creeping band").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        d1 = Tex(r"Moho: base of crust — waves accelerate").scale(0.95).shift(band_shift(1) + UP * 1.2)
        d2 = Tex(r"Gutenberg: mantle–core, 2 900 km").scale(0.95).shift(band_shift(1) + UP * 0.4)
        d3 = Tex(r"Lehmann: outer–inner core, 5 150 km").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.wait(2)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex(r"Asthenosphere (100–250 km): plastic,").scale(0.95).shift(band_shift(1) + DOWN * 1.4)
        d4b = Tex(r"creeps like hot road tar — plates move").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(d4))
        self.play(Write(d4b))
        self.play(Create(SurroundingRectangle(d4b, color=GREEN)))
        d5 = Tex(r"Going down: temperature, pressure, density rise").scale(0.85).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(d5))
        self.wait(3)

        # --- Band 2 (subtopic_2): sial vs sima ---
        self.next_band(2)
        b2t = Tex("Continental vs oceanic crust").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        s1 = Tex(r"SIAL: 30–70 km, granitic, $2{,}7$,").scale(0.95).shift(band_shift(2) + UP * 1.2)
        s1b = Tex(r"ancient — Barberton, 3 billion yr").scale(0.95).shift(band_shift(2) + UP * 0.6)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2.5)
        s2 = Tex(r"SIMA: 5–10 km, basaltic, $3{,}0$,").scale(0.95).shift(band_shift(2) + DOWN * 0.2)
        s2b = Tex(r"never older than 200 my").scale(0.95).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(s2))
        self.play(Write(s2b))
        self.wait(2.5)
        s3 = Tex(r"Denser sima subducts — buoyancy").scale(0.95).shift(band_shift(2) + DOWN * 1.7)
        s3b = Tex(r"doing its work").scale(0.95).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(s3))
        self.play(Write(s3b))
        self.play(Create(SurroundingRectangle(s3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): lithosphere vs crust ---
        self.next_band(3)
        b3t = Tex("A plate is NOT just crust").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        l1 = Tex(r"By composition: crust, mantle, core").scale(0.95).shift(band_shift(3) + UP * 1.2)
        l2 = Tex(r"By behaviour: rigid lithosphere").scale(0.95).shift(band_shift(3) + UP * 0.4)
        l2b = Tex(r"over plastic asthenosphere").scale(0.95).shift(band_shift(3) + DOWN * 0.2)
        self.play(Write(l1))
        self.wait(2)
        self.play(Write(l2))
        self.play(Write(l2b))
        self.wait(2)
        l3 = Tex(r"Lithosphere = crust + rigid upper").scale(1.0).shift(band_shift(3) + DOWN * 1.1)
        l3b = Tex(r"mantle, about 100 km — the plates").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(l3))
        self.play(Write(l3b))
        self.play(Create(SurroundingRectangle(VGroup(l3, l3b), color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): seismic evidence ---
        self.next_band(4)
        b4t = Tex("How we know: the shadow zones").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        w1 = Tex(r"P-waves: squeeze — cross anything").scale(0.95).shift(band_shift(4) + UP * 1.2)
        w2 = Tex(r"S-waves: sideways whip — die in liquid").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(w1))
        self.wait(2)
        self.play(Write(w2))
        self.wait(2)
        w3 = Tex(r"Beyond $103^\circ$: S-waves missing entirely").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        w4 = Tex(r"$\Rightarrow$ outer core is LIQUID").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(w3))
        self.wait(2)
        self.play(Write(w4))
        self.play(Create(SurroundingRectangle(w4, color=GREEN)))
        self.wait(2)
        w5 = Tex(r"P-waves refract: quiet band 103–$143^\circ$").scale(0.9).shift(band_shift(4) + DOWN * 2.1)
        w5b = Tex(r"fixes core depth; faint arrivals inside").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        w5c = Tex(r"betray a solid inner core").scale(0.9).shift(band_shift(4) + DOWN * 3.3)
        self.play(Write(w5))
        self.play(Write(w5b))
        self.play(Write(w5c))
        self.wait(3)

        # --- Band 5 (subtopic_3): supporting evidence ---
        self.next_band(5)
        b5t = Tex("Three independent supports").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        c1 = Tex(r"Density: planet averages $5{,}5$;").scale(0.95).shift(band_shift(5) + UP * 1.2)
        c1b = Tex(r"surface rock only $2{,}7$ — metal below").scale(0.95).shift(band_shift(5) + UP * 0.6)
        self.play(Write(c1))
        self.play(Write(c1b))
        self.wait(2.5)
        c2 = Tex(r"Magnetism: a planetary field demands").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        c2b = Tex(r"circulating liquid metal").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(c2))
        self.play(Write(c2b))
        self.wait(2.5)
        c3 = Tex(r"Iron meteorites: core fragments of").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        c3b = Tex(r"shattered planetary bodies").scale(0.95).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(c3))
        self.play(Write(c3b))
        self.wait(3)

        # --- Band 6 (subtopic_4): the description order and the traps ---
        self.next_band(6)
        b6t = Tex("Describe in order, dodge the traps").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        r1 = Tex(r"Name, depth, composition, state, feature").scale(0.95).shift(band_shift(6) + UP * 1.2)
        self.play(Write(r1))
        self.play(Create(SurroundingRectangle(r1, color=GREEN)))
        self.wait(2)
        t1 = Tex(r"The mantle is an ocean of lava").scale(0.95).shift(band_shift(6) + UP * 0.2)
        self.play(Write(t1))
        self.play(Create(strike(t1)))
        t1f = Tex(r"Solid rock; only the asthenosphere creeps").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(t1f))
        self.wait(2)
        t2 = Tex(r"Hottest, so the centre must be liquid").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(t2))
        self.play(Create(strike(t2)))
        t2f = Tex(r"Pressure wins: the inner core is solid").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(t2f))
        self.wait(2)
        t3 = Tex(r"Plate = lithosphere; sial thick + light,").scale(0.9).shift(band_shift(6) + DOWN * 2.7)
        t3b = Tex(r"sima thin + dense").scale(0.9).shift(band_shift(6) + DOWN * 3.3)
        self.play(Write(t3))
        self.play(Write(t3b))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the peach ---
        self.next_band(7)
        b7t = Tex("The earth is a peach").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        a1 = Tex(r"Skin = crust: thinner than the fuzz").scale(1.0).shift(band_shift(7) + UP * 1.2)
        a2 = Tex(r"Flesh = mantle: most of the fruit, solid —").scale(1.0).shift(band_shift(7) + UP * 0.4)
        a2b = Tex(r"chocolate slumps, still chocolate").scale(1.0).shift(band_shift(7) + DOWN * 0.2)
        self.play(Write(a1))
        self.wait(2)
        self.play(Write(a2))
        self.play(Write(a2b))
        self.wait(2)
        a3 = Tex(r"Stone = core: liquid outside (compass!),").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        a3b = Tex(r"solid centre — pressure wins").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(a3))
        self.play(Write(a3b))
        self.wait(2)
        a4 = Tex(r"Skin, flesh, stone — crust, mantle, core").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(a4))
        self.play(Create(SurroundingRectangle(a4, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the cork raft and the roof sheet ---
        self.next_band(8)
        b8t = Tex("The cork raft and the roof sheet").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        water = Line(band_shift(8) + LEFT * 5.0 + DOWN * 0.4, band_shift(8) + RIGHT * 5.0 + DOWN * 0.4, color=BLUE)
        self.play(Create(water))
        cork = Rectangle(width=2.6, height=1.1).shift(band_shift(8) + LEFT * 2.6 + DOWN * 0.35)
        cork_l = Tex("thick + light: rides high").scale(0.8).shift(band_shift(8) + LEFT * 2.6 + UP * 0.9)
        self.play(Create(cork), Write(cork_l))
        sheet = Rectangle(width=2.6, height=0.35).shift(band_shift(8) + RIGHT * 2.6 + DOWN * 0.5)
        sheet_l = Tex("thin + heavy: floats low").scale(0.8).shift(band_shift(8) + RIGHT * 2.6 + UP * 0.4)
        self.play(Create(sheet), Write(sheet_l))
        self.wait(2)
        r1 = Tex(r"Cork = continents ($2{,}7$, ancient)").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        r2 = Tex(r"Roof sheet = sea floor ($3{,}0$, young)").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex(r"Push them together: the iron dives — subduction").scale(0.9).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(r3))
        self.play(Create(SurroundingRectangle(r3, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): thumping the watermelon ---
        self.next_band(9)
        b9t = Tex("Thumping the watermelon").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        k1 = Tex(r"Deepest hole: 12 km of 6 371 —").scale(0.95).shift(band_shift(9) + UP * 1.2)
        k1b = Tex(r"so thump it and judge the sound").scale(0.95).shift(band_shift(9) + UP * 0.6)
        self.play(Write(k1))
        self.play(Write(k1b))
        self.wait(2)
        k2 = Tex(r"P-wave squeeze: crosses anything").scale(0.95).shift(band_shift(9) + DOWN * 0.2)
        k3 = Tex(r"S-wave sweep: bathwater just glides —").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        k3b = Tex(r"liquid carries no sideways shake").scale(0.95).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(k2))
        self.wait(2)
        self.play(Write(k3))
        self.play(Write(k3b))
        self.wait(2)
        k4 = Tex(r"Far side records NO S-waves:").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        k4b = Tex(r"the liquid core, found by silence").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(k4))
        self.play(Write(k4b))
        self.play(Create(SurroundingRectangle(k4b, color=GREEN)))
        self.wait(4)
