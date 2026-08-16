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

# Band-layout whiteboard scene for "Volcanoes: eruptions and landforms"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). The
# volcano anatomy, sill/dyke sketch and koppie profile are hand-built from
# Line/Arrow/Dot/Circle/Rectangle/Tex, element by element with the script.
# Subtopic durations (s): 220/240/250/240/180/180/190 of 1500.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class VolcanoesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): magma, lava, viscosity ---
        title = Tex("Volcanoes: Eruptions and Landforms").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        m1 = Tex(r"Magma below ground; lava at surface").scale(1.0).shift(UP * 1.3)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Made at: divergent (pressure drops),").scale(0.95).shift(UP * 0.5)
        m2b = Tex(r"convergent (wet slab melts mantle),").scale(0.95).shift(DOWN * 0.1)
        m2c = Tex(r"hot spots (Hawaii, R\'eunion)").scale(0.95).shift(DOWN * 0.7)
        self.play(Write(m2))
        self.play(Write(m2b))
        self.play(Write(m2c))
        self.wait(2.5)
        m3 = Tex(r"Low silica: runny, gas escapes, EFFUSIVE").scale(0.95).shift(DOWN * 1.6)
        m4 = Tex(r"High silica: stiff plug, EXPLOSIVE").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(m3))
        self.wait(2)
        self.play(Write(m4))
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        m5 = Tex(r"Active, dormant, extinct").scale(0.9).shift(DOWN * 3.1)
        self.play(Write(m5))
        self.wait(3)

        # --- Band 1 (subtopic_2): anatomy of a volcano ---
        self.next_band(1)
        b1t = Tex("The structure, bottom up").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        gnd = Line(band_shift(1) + LEFT * 5.0 + DOWN * 1.0, band_shift(1) + RIGHT * 5.0 + DOWN * 1.0, stroke_width=6)
        self.play(Create(gnd))
        cham = Circle(radius=0.7, color=RED).shift(band_shift(1) + DOWN * 2.5)
        cham_l = Tex("magma chamber").scale(0.8).shift(band_shift(1) + DOWN * 2.5 + RIGHT * 3.0)
        self.play(Create(cham), Write(cham_l))
        self.wait(1.5)
        vent = Line(band_shift(1) + DOWN * 1.8, band_shift(1) + UP * 1.0, color=RED)
        vent_l = Tex("vent (pipe)").scale(0.8).shift(band_shift(1) + RIGHT * 2.2 + DOWN * 0.4)
        self.play(Create(vent), Write(vent_l))
        self.wait(1.5)
        c_left = Line(band_shift(1) + LEFT * 3.0 + DOWN * 1.0, band_shift(1) + LEFT * 0.3 + UP * 1.0)
        c_right = Line(band_shift(1) + RIGHT * 3.0 + DOWN * 1.0, band_shift(1) + RIGHT * 0.3 + UP * 1.0)
        cone_l = Tex("cone of erupted layers").scale(0.8).shift(band_shift(1) + LEFT * 3.4 + UP * 0.6)
        self.play(Create(c_left), Create(c_right), Write(cone_l))
        self.wait(1.5)
        cr = Tex("crater at the summit").scale(0.8).shift(band_shift(1) + UP * 1.5)
        self.play(Write(cr))
        self.wait(1.5)
        cal = Tex(r"Chamber empties, summit collapses:").scale(0.9).shift(band_shift(1) + DOWN * 3.0 + LEFT * 1.2)
        cal2 = Tex(r"CALDERA (Ngorongoro)").scale(0.9).shift(band_shift(1) + DOWN * 3.0 + RIGHT * 3.6)
        self.play(Write(cal), Write(cal2))
        self.wait(3)

        # --- Band 2 (subtopic_2): the four types ---
        self.next_band(2)
        b2t = Tex("Four volcano types").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        t1 = Tex(r"Shield: runny basalt, wide + gentle —").scale(0.95).shift(band_shift(2) + UP * 1.2)
        t1b = Tex(r"Mauna Loa, Marion Island").scale(0.95).shift(band_shift(2) + UP * 0.6)
        self.play(Write(t1))
        self.play(Write(t1b))
        self.wait(2)
        t2 = Tex(r"Composite: ash/lava layers, steep").scale(0.95).shift(band_shift(2) + DOWN * 0.2)
        t2b = Tex(r"cone — Fuji, Vesuvius: the dangerous ones").scale(0.95).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(t2))
        self.play(Write(t2b))
        self.wait(2)
        t3 = Tex(r"Cinder cone: loose fragments, steep,").scale(0.95).shift(band_shift(2) + DOWN * 1.6)
        t3b = Tex(r"small, big crater").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(t3))
        self.play(Write(t3b))
        self.wait(2)
        t4 = Tex(r"Dome: lava too stiff to flow, bulging").scale(0.95).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(t4))
        self.wait(3)

        # --- Band 3 (subtopic_3): extrusive landforms ---
        self.next_band(3)
        b3t = Tex("Extrusive: built at the surface").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        x1 = Tex(r"Fissure floods build lava plateaux").scale(0.95).shift(band_shift(3) + UP * 1.2)
        self.play(Write(x1))
        self.wait(2)
        # stepped Drakensberg rampart profile
        steps = [
            band_shift(3) + LEFT * 4.8 + DOWN * 1.8,
            band_shift(3) + LEFT * 3.4 + DOWN * 1.8,
            band_shift(3) + LEFT * 3.4 + DOWN * 1.0,
            band_shift(3) + LEFT * 2.0 + DOWN * 1.0,
            band_shift(3) + LEFT * 2.0 + DOWN * 0.2,
            band_shift(3) + LEFT * 0.4 + DOWN * 0.2,
        ]
        for a, b in zip(steps, steps[1:]):
            self.play(Create(Line(a, b)), run_time=0.5)
        st_l = Tex("stacked basalt flows: the Drakensberg").scale(0.85).shift(band_shift(3) + RIGHT * 2.4 + DOWN * 1.0)
        self.play(Write(st_l))
        self.wait(2)
        x2 = Tex(r"180 mya, Gondwana breaking up —").scale(0.9).shift(band_shift(3) + DOWN * 2.5 + LEFT * 1.4)
        x2b = Tex(r"flat-topped stepped ramparts").scale(0.9).shift(band_shift(3) + DOWN * 2.5 + RIGHT * 3.6)
        self.play(Write(x2), Write(x2b))
        x3 = Tex(r"Hot springs: Bela-Bela, Montagu").scale(0.9).shift(band_shift(3) + DOWN * 3.2)
        self.play(Write(x3))
        self.wait(3)

        # --- Band 4 (subtopic_3): intrusive landforms ---
        self.next_band(4)
        b4t = Tex("Intrusive: cooled underground").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        i1 = Tex(r"Batholith: deep granite mass — Paarl Rock").scale(0.9).shift(band_shift(4) + UP * 1.3)
        i2 = Tex(r"Lopolith: saucer — Bushveld Complex,").scale(0.9).shift(band_shift(4) + UP * 0.6)
        i2b = Tex(r"world's platinum and chromium").scale(0.9).shift(band_shift(4) + UP * 0.0)
        i3 = Tex(r"Laccolith: blister arching the strata").scale(0.9).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(i1))
        self.wait(2)
        self.play(Write(i2))
        self.play(Write(i2b))
        self.wait(2)
        self.play(Write(i3))
        self.wait(2)
        i4 = Tex(r"Sill: BETWEEN layers, horizontal;").scale(0.9).shift(band_shift(4) + DOWN * 1.5)
        i4b = Tex(r"dyke: ACROSS layers, a standing wall").scale(0.9).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(i4))
        self.play(Write(i4b))
        self.wait(2)
        i5 = Tex(r"Dolerite lid = Karoo koppie; kimberlite").scale(0.9).shift(band_shift(4) + DOWN * 2.9)
        i5b = Tex(r"pipes = Kimberley diamonds").scale(0.9).shift(band_shift(4) + DOWN * 3.5)
        self.play(Write(i5))
        self.play(Write(i5b))
        self.play(Create(SurroundingRectangle(i5b, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): hazards ---
        self.next_band(5)
        b5t = Tex("Hazards, ranked by what kills").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        h1 = Tex(r"Lava flows: destroy, seldom kill").scale(0.95).shift(band_shift(5) + UP * 1.2)
        h2 = Tex(r"Pyroclastic flows: superheated ash").scale(0.95).shift(band_shift(5) + UP * 0.4)
        h2b = Tex(r"avalanches — the true danger").scale(0.95).shift(band_shift(5) + DOWN * 0.2)
        self.play(Write(h1))
        self.wait(2)
        self.play(Write(h2))
        self.play(Write(h2b))
        self.play(Create(SurroundingRectangle(h2b, color=GREEN)))
        self.wait(2)
        h3 = Tex(r"Ash falls: roofs, crops, lungs, aviation").scale(0.95).shift(band_shift(5) + DOWN * 1.1)
        h4 = Tex(r"Lahars: ash + rain = valley mudflows").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(h3))
        self.wait(2)
        self.play(Write(h4))
        self.wait(2)
        h5 = Tex(r"Plus gases, landslides, tsunamis,").scale(0.9).shift(band_shift(5) + DOWN * 2.7)
        h5b = Tex(r"and a cooler climate for a year or two").scale(0.9).shift(band_shift(5) + DOWN * 3.3)
        self.play(Write(h5))
        self.play(Write(h5b))
        self.wait(3)

        # --- Band 6 (subtopic_4): benefits and management ---
        self.next_band(6)
        b6t = Tex("Why people stay — and management").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        g1 = Tex(r"Fertile soils: Java, Sicily, Ethiopia").scale(0.95).shift(band_shift(6) + UP * 1.2)
        g2 = Tex(r"Geothermal power: Iceland, Kenya").scale(0.95).shift(band_shift(6) + UP * 0.5)
        g3 = Tex(r"Minerals: Bushveld platinum, diamonds").scale(0.95).shift(band_shift(6) + DOWN * 0.2)
        self.play(Write(g1))
        self.wait(2)
        self.play(Write(g2))
        self.wait(2)
        self.play(Write(g3))
        self.wait(2)
        g4 = Tex(r"Volcanoes give warning: tremor swarms,").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        g4b = Tex(r"swelling ground, rising gases").scale(0.95).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(g4))
        self.play(Write(g4b))
        self.wait(2)
        g5 = Tex(r"Monitor, map hazards, plan, educate").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(g5))
        self.play(Create(SurroundingRectangle(g5, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): shaking the cooldrink ---
        self.next_band(7)
        b7t = Tex("Shaking the cooldrink").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        s1 = Tex(r"Dissolved gas wants out — the only").scale(1.0).shift(band_shift(7) + UP * 1.2)
        s1b = Tex(r"question is how runny the melt is").scale(1.0).shift(band_shift(7) + UP * 0.6)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2)
        s2 = Tex(r"Warm honey: bubbles escape, it oozes").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        s3 = Tex(r"Stiff pap: plugs its own pipe — BANG").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(s2))
        self.wait(2)
        self.play(Write(s3))
        self.wait(2)
        s4 = Tex(r"Runny = gentle + wide; thick = violent + steep").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(s4))
        self.play(Create(SurroundingRectangle(s4, color=GREEN)))
        s5 = Tex(r"Same rock, two addresses: magma / lava").scale(0.9).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(s5))
        self.wait(3)

        # --- Band 8 (subtopic_6): pancake and layer cake ---
        self.next_band(8)
        b8t = Tex("Pancake, layer cake, rubbish heap").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        p1 = Tex(r"Pancake = shield: wide, low, drivable").scale(0.95).shift(band_shift(8) + UP * 1.2)
        p2 = Tex(r"Layer cake = composite: crumbs (ash)").scale(0.95).shift(band_shift(8) + UP * 0.4)
        p2b = Tex(r"glued by icing (lava) — Fuji, Vesuvius").scale(0.95).shift(band_shift(8) + DOWN * 0.2)
        p3 = Tex(r"Rubbish heap = cinder cone: steep, small").scale(0.95).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(p1))
        self.wait(2)
        self.play(Write(p2))
        self.play(Write(p2b))
        self.wait(2)
        self.play(Write(p3))
        self.wait(2)
        p4 = Tex(r"Shared plumbing: store room, pipe, bowl").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        p5 = Tex(r"Store room empties $\Rightarrow$ top collapses:").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        p5b = Tex(r"caldera, like Ngorongoro").scale(0.95).shift(band_shift(8) + DOWN * 3.3)
        self.play(Write(p4))
        self.wait(2)
        self.play(Write(p5))
        self.play(Write(p5b))
        self.wait(3)

        # --- Band 9 (subtopic_7): what the volcano leaves behind ---
        self.next_band(9)
        b9t = Tex("What the volcano leaves behind").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        q1 = Tex(r"Cracks flooded SA in basalt sheets:").scale(0.95).shift(band_shift(9) + UP * 1.2)
        q1b = Tex(r"the Drakensberg's stepped skyline").scale(0.95).shift(band_shift(9) + UP * 0.6)
        self.play(Write(q1))
        self.play(Write(q1b))
        self.wait(2)
        # koppie: flat dolerite lid on eroding shale
        k_base = Line(band_shift(9) + LEFT * 4.8 + DOWN * 1.6, band_shift(9) + LEFT * 0.4 + DOWN * 1.6)
        k_l = Line(band_shift(9) + LEFT * 3.8 + DOWN * 1.6, band_shift(9) + LEFT * 3.2 + DOWN * 0.4)
        k_top = Line(band_shift(9) + LEFT * 3.2 + DOWN * 0.4, band_shift(9) + LEFT * 2.0 + DOWN * 0.4, stroke_width=6, color=YELLOW)
        k_r = Line(band_shift(9) + LEFT * 2.0 + DOWN * 0.4, band_shift(9) + LEFT * 1.4 + DOWN * 1.6)
        self.play(Create(k_base))
        self.play(Create(k_l), Create(k_r))
        self.play(Create(k_top))
        k_lab = Tex("koppie in a dolerite hat").scale(0.85).shift(band_shift(9) + RIGHT * 2.2 + DOWN * 1.0)
        self.play(Write(k_lab))
        self.wait(2)
        q2 = Tex(r"Kimberlite pipes brought the diamonds").scale(0.95).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(q2))
        self.wait(2)
        q3 = Tex(r"Watch, map, plan, practise").scale(1.05).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(q3))
        self.play(Create(SurroundingRectangle(q3, color=GREEN)))
        self.wait(4)
