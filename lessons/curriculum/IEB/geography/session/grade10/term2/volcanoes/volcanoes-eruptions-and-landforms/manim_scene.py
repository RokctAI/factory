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

# Band-layout whiteboard scene for "Volcanoes: Eruptions and Landforms"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). Volcano
# anatomy, plateau stacks and koppie profiles are built from
# Line/Circle/Rectangle/Tex.
# Subtopic durations (s): 220/240/250/240/180/180/190 of 1500.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class VolcanoesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): magma, lava, viscosity ---
        title = Tex("Volcanoes: Eruptions and Landforms").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        v1 = Tex(r"MAGMA below ground = LAVA at surface").scale(0.95).shift(UP * 1.2)
        self.play(Write(v1))
        self.wait(2)
        v2 = Tex(r"Made at: divergent (decompression),").scale(0.9).shift(UP * 0.4)
        v2b = Tex(r"convergent (slab water), hot spots").scale(0.9).shift(DOWN * 0.2)
        v2c = Tex(r"(Hawaii, Tristan da Cunha 1961)").scale(0.9).shift(DOWN * 0.8)
        self.play(Write(v2))
        self.play(Write(v2b))
        self.play(Write(v2c))
        self.wait(2.5)
        v3 = Tex(r"Low silica: hot, runny, gas escapes —").scale(0.9).shift(DOWN * 1.7)
        v3b = Tex(r"EFFUSIVE; high silica: stiff cork —").scale(0.9).shift(DOWN * 2.3)
        v3c = Tex(r"EXPLOSIVE pyroclastics").scale(0.9).shift(DOWN * 2.9)
        self.play(Write(v3))
        self.play(Write(v3b))
        self.play(Write(v3c))
        self.play(Create(SurroundingRectangle(v3c, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): anatomy of a volcano ---
        self.next_band(1)
        b1t = Tex("The anatomy, bottom up").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        chamber = Circle(radius=0.7, color=RED).shift(band_shift(1) + DOWN * 2.2 + LEFT * 2.5)
        vent = Line(band_shift(1) + DOWN * 1.6 + LEFT * 2.5, band_shift(1) + UP * 0.9 + LEFT * 2.5, color=ORANGE)
        cone_l = Line(band_shift(1) + DOWN * 0.6 + LEFT * 4.3, band_shift(1) + UP * 0.9 + LEFT * 2.7, color=WHITE)
        cone_r = Line(band_shift(1) + UP * 0.9 + LEFT * 2.3, band_shift(1) + DOWN * 0.6 + LEFT * 0.7, color=WHITE)
        self.play(Create(chamber))
        a1 = Tex(r"magma chamber: the reservoir").scale(0.85).shift(band_shift(1) + DOWN * 2.2 + RIGHT * 2.3)
        self.play(Write(a1))
        self.wait(1.5)
        self.play(Create(vent), Create(cone_l), Create(cone_r))
        a2 = Tex(r"vent up the middle, crater on top,").scale(0.85).shift(band_shift(1) + DOWN * 0.6 + RIGHT * 2.5)
        a2b = Tex(r"cone stacked around, parasitic cones aside").scale(0.85).shift(band_shift(1) + DOWN * 1.2 + RIGHT * 2.5)
        self.play(Write(a2))
        self.play(Write(a2b))
        self.wait(2.5)
        a3 = Tex(r"Chamber drained $\Rightarrow$ summit collapses:").scale(0.9).shift(band_shift(1) + UP * 1.3)
        a3b = Tex(r"CALDERA — Crater Lake, 10 km wide").scale(0.9).shift(band_shift(1) + UP * 0.7 + RIGHT * 0.4)
        self.play(Write(a3))
        self.play(Write(a3b))
        self.play(Create(SurroundingRectangle(a3b, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the four types ---
        self.next_band(2)
        b2t = Tex("Four builds, four profiles").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        t1 = Tex(r"SHIELD: runny basalt, wide + gentle — Kilauea").scale(0.85).shift(band_shift(2) + UP * 1.2)
        t2 = Tex(r"COMPOSITE: ash then lava, tall + steep —").scale(0.85).shift(band_shift(2) + UP * 0.5)
        t2b = Tex(r"Pinatubo, Mount St Helens — the deadly type").scale(0.85).shift(band_shift(2) + DOWN * 0.1)
        self.play(Write(t1))
        self.wait(2)
        self.play(Write(t2))
        self.play(Write(t2b))
        self.play(Create(SurroundingRectangle(t2b, color=GREEN)))
        self.wait(2)
        t3 = Tex(r"CINDER CONE: loose fragments, small + steep —").scale(0.85).shift(band_shift(2) + DOWN * 1.0)
        t3b = Tex(r"Par\'icutin grew in a field from 1943").scale(0.85).shift(band_shift(2) + DOWN * 1.6)
        t4 = Tex(r"DOME: lava too stiff to travel, bulges + rebuilds").scale(0.85).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(t3))
        self.play(Write(t3b))
        self.wait(2)
        self.play(Write(t4))
        self.wait(3)

        # --- Band 3 (subtopic_3): extrusive landforms ---
        self.next_band(3)
        b3t = Tex("Extrusive: built in the open").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        e1 = Tex(r"Cones, craters, lava flows —").scale(0.9).shift(band_shift(3) + UP * 1.2)
        e1b = Tex(r"and fissure-fed LAVA PLATEAUX").scale(0.9).shift(band_shift(3) + UP * 0.6)
        self.play(Write(e1))
        self.play(Write(e1b))
        self.wait(2)
        p1 = Rectangle(width=4.6, height=0.4).shift(band_shift(3) + DOWN * 0.4)
        p2 = Rectangle(width=4.0, height=0.4).shift(band_shift(3) + DOWN * 0.0 + LEFT * 0.3)
        p3 = Rectangle(width=3.4, height=0.4).shift(band_shift(3) + UP * 0.4 + LEFT * 0.6)
        self.play(Create(p1), Create(p2), Create(p3))
        e2 = Tex(r"Drakensberg + Lesotho: stacked basalt").scale(0.85).shift(band_shift(3) + DOWN * 1.3)
        e2b = Tex(r"sheets, 180 my old — ramparts and stairs").scale(0.85).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(e2))
        self.play(Write(e2b))
        self.play(Create(SurroundingRectangle(e2b, color=GREEN)))
        self.wait(2)
        e3 = Tex(r"Hot springs: Badplaas, Goudini").scale(0.85).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(e3))
        self.wait(3)

        # --- Band 4 (subtopic_3): intrusive landforms ---
        self.next_band(4)
        b4t = Tex("Intrusive: frozen underground").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        i1 = Tex(r"BATHOLITH: deep granite mass —").scale(0.85).shift(band_shift(4) + UP * 1.3)
        i1b = Tex(r"Cape Peninsula domes, Boulders Beach").scale(0.85).shift(band_shift(4) + UP * 0.7)
        i2 = Tex(r"LOPOLITH: saucer — Bushveld Complex,").scale(0.85).shift(band_shift(4) + UP * 0.0)
        i2b = Tex(r"world's platinum store; LACCOLITH: blister").scale(0.85).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(i1))
        self.play(Write(i1b))
        self.wait(2)
        self.play(Write(i2))
        self.play(Write(i2b))
        self.wait(2)
        i3 = Tex(r"SILL between layers $\Rightarrow$ dolerite koppie lids,").scale(0.85).shift(band_shift(4) + DOWN * 1.5)
        i3b = Tex(r"Valley of Desolation; DYKE across $\Rightarrow$ straight ridge").scale(0.8).shift(band_shift(4) + DOWN * 2.1)
        i4 = Tex(r"NECK/PLUG: kimberlite pipes — Cullinan, Venetia").scale(0.8).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(i3))
        self.play(Write(i3b))
        self.wait(2)
        self.play(Write(i4))
        self.play(Create(SurroundingRectangle(i4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): hazards ---
        self.next_band(5)
        b5t = Tex("Hazards, ranked by lethality").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        h1 = Tex(r"Lava: slow — walk away").scale(0.9).shift(band_shift(5) + UP * 1.2)
        h2 = Tex(r"PYROCLASTIC FLOW: glowing avalanche —").scale(0.9).shift(band_shift(5) + UP * 0.5)
        h2b = Tex(r"St Pierre 1902, minutes").scale(0.9).shift(band_shift(5) + DOWN * 0.1)
        self.play(Write(h1))
        self.wait(2)
        self.play(Write(h2))
        self.play(Write(h2b))
        self.play(Create(SurroundingRectangle(h2b, color=RED)))
        self.wait(2)
        h3 = Tex(r"Ash: roofs, crops, lungs, aviation —").scale(0.85).shift(band_shift(5) + DOWN * 1.0)
        h3b = Tex(r"Eyjafjallaj\"okull 2010").scale(0.85).shift(band_shift(5) + DOWN * 1.6)
        h4 = Tex(r"LAHARS: valley mudflows — Armero 1985;").scale(0.85).shift(band_shift(5) + DOWN * 2.4)
        h4b = Tex(r"plus gases, landslides, tsunamis, cooling").scale(0.85).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(h3))
        self.play(Write(h3b))
        self.wait(2)
        self.play(Write(h4))
        self.play(Write(h4b))
        self.wait(3)

        # --- Band 6 (subtopic_4): benefits and management ---
        self.next_band(6)
        b6t = Tex("Why people stay, how they survive").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        g1 = Tex(r"Fertile ash soils: Java, Vesuvius slopes").scale(0.85).shift(band_shift(6) + UP * 1.2)
        g2 = Tex(r"Geothermal: Iceland, Kenya's Olkaria").scale(0.85).shift(band_shift(6) + UP * 0.6)
        g3 = Tex(r"Minerals: Bushveld platinum, diamonds; tourism").scale(0.85).shift(band_shift(6) + UP * 0.0)
        self.play(Write(g1))
        self.wait(1.5)
        self.play(Write(g2))
        self.wait(1.5)
        self.play(Write(g3))
        self.wait(2)
        g4 = Tex(r"Volcanoes warn: quake swarms, swelling,").scale(0.85).shift(band_shift(6) + DOWN * 0.9)
        g4b = Tex(r"gas, heat $\Rightarrow$ alerts, hazard maps, zoning").scale(0.85).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(g4))
        self.play(Write(g4b))
        self.wait(2)
        g5 = Tex(r"Pinatubo 1991: tens of thousands evacuated").scale(0.9).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(g5))
        self.play(Create(SurroundingRectangle(g5, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): why the pap pot spits ---
        self.next_band(7)
        b7t = Tex("Why the pap pot spits").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        s1 = Tex(r"Thin soup: bubbles slip out — blip, blip").scale(0.9).shift(band_shift(7) + UP * 1.2)
        s2 = Tex(r"Stiff pap: steam trapped — angry PLOP").scale(0.9).shift(band_shift(7) + UP * 0.5)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.wait(2)
        s3 = Tex(r"Runny magma oozes rivers;").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        s3b = Tex(r"thick magma corks the pipe — detonates").scale(0.9).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(s3))
        self.play(Write(s3b))
        self.play(Create(SurroundingRectangle(s3b, color=GREEN)))
        self.wait(2)
        s4 = Tex(r"Silica decides; the plates choose the pot;").scale(0.85).shift(band_shift(7) + DOWN * 1.9)
        s4b = Tex(r"magma inside, lava outside").scale(0.85).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(s4))
        self.play(Write(s4b))
        self.wait(3)

        # --- Band 8 (subtopic_6): syrup, lasagne, sand heap ---
        self.next_band(8)
        b8t = Tex("Syrup, lasagne, sand heap").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        y1 = Tex(r"Syrup on a plate: wide + low — SHIELD").scale(0.9).shift(band_shift(8) + UP * 1.2)
        y2 = Tex(r"Lasagne: mince (ash) under pasta (lava),").scale(0.9).shift(band_shift(8) + UP * 0.5)
        y2b = Tex(r"layer on layer — COMPOSITE, the killer").scale(0.9).shift(band_shift(8) + DOWN * 0.1)
        self.play(Write(y1))
        self.wait(2)
        self.play(Write(y2))
        self.play(Write(y2b))
        self.play(Create(SurroundingRectangle(y2b, color=GREEN)))
        self.wait(2)
        y3 = Tex(r"Sand heap: small, steep, loose — CINDER CONE").scale(0.9).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(y3))
        self.wait(2)
        y4 = Tex(r"Same plumbing: tank, pipe, funnel;").scale(0.85).shift(band_shift(8) + DOWN * 1.9)
        y4b = Tex(r"empty the tank $\Rightarrow$ caldera").scale(0.85).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(y4))
        self.play(Write(y4b))
        self.wait(3)

        # --- Band 9 (subtopic_7): what the volcano leaves behind ---
        self.next_band(9)
        b9t = Tex("What the volcano leaves behind").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        l1 = Tex(r"Out in the open: fissure basalt stacked —").scale(0.85).shift(band_shift(9) + UP * 1.2)
        l1b = Tex(r"Drakensberg ramparts, Lesotho roof").scale(0.85).shift(band_shift(9) + UP * 0.6)
        self.play(Write(l1))
        self.play(Write(l1b))
        self.wait(2)
        l2 = Tex(r"Underground: dolerite lids on Karoo koppies,").scale(0.85).shift(band_shift(9) + DOWN * 0.3)
        l2b = Tex(r"Valley of Desolation columns, straight dyke ridges").scale(0.8).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(l2))
        self.play(Write(l2b))
        self.wait(2)
        l3 = Tex(r"Deepest of all: kimberlite pipes with diamonds").scale(0.85).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(l3))
        self.wait(2)
        l4 = Tex(r"Watch, map, plan, practise —").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        l4b = Tex(r"Pinatubo walked its people to safety").scale(0.95).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(l4))
        self.play(Write(l4b))
        self.play(Create(SurroundingRectangle(l4b, color=GREEN)))
        self.wait(4)
