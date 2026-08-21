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

# Band-layout whiteboard scene for "Plate Boundaries and Plate Movement"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). The
# convection loop, subduction cross-section and boundary sketches are built
# from Line/Arrow/Circle/Tex.
# Subtopic durations (s): 225/220/230/235/185/190/195 of 1480.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class PlateBoundariesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): Pangaea and the four proofs ---
        title = Tex("Plate Boundaries and Plate Movement").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        p1 = Tex(r"1912, Wegener: PANGAEA $\rightarrow$").scale(0.95).shift(UP * 1.4)
        p1b = Tex(r"Laurasia + Gondwana, 200 my ago").scale(0.95).shift(UP * 0.8)
        self.play(Write(p1))
        self.play(Write(p1b))
        self.wait(2)
        e1 = Tex(r"FIT: S. America nests into Africa").scale(0.9).shift(UP * 0.0)
        e2 = Tex(r"FOSSILS: Mesosaurus — Karoo + Brazil").scale(0.9).shift(DOWN * 0.6)
        e3 = Tex(r"ROCKS: Cape Fold $\rightarrow$ Argentina").scale(0.9).shift(DOWN * 1.2)
        e4 = Tex(r"CLIMATE: Dwyka tillite, Barkly West scratches").scale(0.9).shift(DOWN * 1.8)
        self.play(Write(e1))
        self.wait(1.5)
        self.play(Write(e2))
        self.wait(1.5)
        self.play(Write(e3))
        self.wait(1.5)
        self.play(Write(e4))
        self.wait(2)
        e5 = Tex(r"Rejected: no MECHANISM").scale(0.95).shift(DOWN * 2.7)
        self.play(Write(e5))
        self.play(Create(SurroundingRectangle(e5, color=RED)))
        self.wait(3)

        # --- Band 1 (subtopic_2): the convection engine ---
        self.next_band(1)
        b1t = Tex("The engine: mantle convection").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        loop_up = Arrow(band_shift(1) + DOWN * 1.6, band_shift(1) + UP * 0.4, color=RED)
        loop_l = Arrow(band_shift(1) + UP * 0.5 + LEFT * 0.4, band_shift(1) + UP * 0.5 + LEFT * 3.0, color=ORANGE)
        loop_r = Arrow(band_shift(1) + UP * 0.5 + RIGHT * 0.4, band_shift(1) + UP * 0.5 + RIGHT * 3.0, color=ORANGE)
        sink_l = Arrow(band_shift(1) + UP * 0.3 + LEFT * 3.2, band_shift(1) + DOWN * 1.7 + LEFT * 3.2, color=BLUE)
        sink_r = Arrow(band_shift(1) + UP * 0.3 + RIGHT * 3.2, band_shift(1) + DOWN * 1.7 + RIGHT * 3.2, color=BLUE)
        self.play(Create(loop_up))
        self.play(Create(loop_l), Create(loop_r))
        self.play(Create(sink_l), Create(sink_r))
        v1 = Tex(r"SOLID rock, plastic creep —").scale(0.9).shift(band_shift(1) + DOWN * 2.3)
        v1b = Tex(r"centimetres per year").scale(0.9).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(v1))
        self.play(Write(v1b))
        self.wait(2)
        v2 = Tex(r"RIDGE PUSH: slide off the high crest").scale(0.9).shift(band_shift(1) + UP * 1.4)
        v3 = Tex(r"SLAB PULL: sinking edge hauls the plate").scale(0.9).shift(band_shift(1) + UP * 0.9)
        self.play(Write(v2))
        self.wait(2)
        self.play(Write(v3))
        self.play(Create(SurroundingRectangle(v3, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): sea-floor spreading proof ---
        self.next_band(2)
        b2t = Tex("Sea-floor spreading: the receipts").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        floor = Line(band_shift(2) + LEFT * 5.0 + DOWN * 0.2, band_shift(2) + RIGHT * 5.0 + DOWN * 0.2, color=WHITE)
        ridge = Line(band_shift(2) + UP * 0.6, band_shift(2) + DOWN * 0.2, color=RED)
        self.play(Create(floor), Create(ridge))
        s1 = Tex(r"AGE: newborn at the ridge,").scale(0.9).shift(band_shift(2) + UP * 1.4)
        s1b = Tex(r"older outward — max 200 my").scale(0.9).shift(band_shift(2) + UP * 0.9)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2.5)
        m1 = Tex(r"STRIPES: field flips locked in lava,").scale(0.9).shift(band_shift(2) + DOWN * 1.0)
        m1b = Tex(r"mirrored on both sides — a barcode").scale(0.9).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(m1))
        self.play(Write(m1b))
        self.play(Create(SurroundingRectangle(m1b, color=GREEN)))
        self.wait(2)
        m2 = Tex(r"South Atlantic: 2–5 cm/yr wider").scale(0.9).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(m2))
        self.wait(3)

        # --- Band 3 (subtopic_3): divergent and transform ---
        self.next_band(3)
        b3t = Tex("Apart, and past").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        d1 = Tex(r"DIVERGENT = constructive: new crust").scale(0.9).shift(band_shift(3) + UP * 1.3)
        d2 = Tex(r"Ocean: mid-ocean ridge — Iceland, Ascension").scale(0.85).shift(band_shift(3) + UP * 0.7)
        d3 = Tex(r"Continent: East African Rift — scarps,").scale(0.85).shift(band_shift(3) + UP * 0.1)
        d3b = Tex(r"ribbon lakes, Kilimanjaro").scale(0.85).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.wait(2)
        self.play(Write(d3))
        self.play(Write(d3b))
        self.wait(2)
        t1 = Tex(r"TRANSFORM = conservative: San Andreas —").scale(0.85).shift(band_shift(3) + DOWN * 1.4)
        t1b = Tex(r"straight scar, offset streams,").scale(0.85).shift(band_shift(3) + DOWN * 2.0)
        t1c = Tex(r"no volcanoes, violent quakes").scale(0.85).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(t1))
        self.play(Write(t1b))
        self.play(Write(t1c))
        self.play(Create(SurroundingRectangle(t1c, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_4): subduction cross-section ---
        self.next_band(4)
        b4t = Tex("Oceanic meets continental").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        cont = Line(band_shift(4) + RIGHT * 0.5 + UP * 0.3, band_shift(4) + RIGHT * 5.0 + UP * 0.3, color=WHITE)
        ocean = Line(band_shift(4) + LEFT * 5.0 + DOWN * 0.1, band_shift(4) + LEFT * 0.5 + DOWN * 0.1, color=BLUE)
        slab = Arrow(band_shift(4) + LEFT * 0.5 + DOWN * 0.1, band_shift(4) + RIGHT * 1.2 + DOWN * 2.2, color=BLUE)
        self.play(Create(ocean), Create(cont))
        self.play(Create(slab))
        k1 = Tex(r"Denser $3{,}0$ dives under $2{,}7$").scale(0.9).shift(band_shift(4) + UP * 1.4)
        self.play(Write(k1))
        self.wait(2)
        k2 = Tex(r"TRENCH offshore + FOLD MOUNTAINS").scale(0.9).shift(band_shift(4) + DOWN * 1.2)
        k2b = Tex(r"+ COMPOSITE VOLCANOES —").scale(0.9).shift(band_shift(4) + DOWN * 1.8)
        k2c = Tex(r"Peru-Chile Trench and the Andes").scale(0.9).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(k2))
        self.play(Write(k2b))
        self.play(Write(k2c))
        self.play(Create(SurroundingRectangle(k2c, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): the other two collisions ---
        self.next_band(5)
        b5t = Tex("The other two collisions").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        o1 = Tex(r"Ocean vs ocean: older, colder,").scale(0.9).shift(band_shift(5) + UP * 1.2)
        o1b = Tex(r"denser one dives — Mariana Trench,").scale(0.9).shift(band_shift(5) + UP * 0.6)
        o1c = Tex(r"island arcs: Aleutians, Indonesia").scale(0.9).shift(band_shift(5) + UP * 0.0)
        self.play(Write(o1))
        self.play(Write(o1b))
        self.play(Write(o1c))
        self.wait(2.5)
        c1 = Tex(r"Continent vs continent: neither sinks —").scale(0.9).shift(band_shift(5) + DOWN * 1.0)
        c1b = Tex(r"Himalayas, still rising —").scale(0.9).shift(band_shift(5) + DOWN * 1.6)
        c1c = Tex(r"big quakes, NO volcanoes").scale(0.9).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(c1))
        self.play(Write(c1b))
        self.play(Write(c1c))
        self.play(Create(SurroundingRectangle(c1c, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the world pattern ---
        self.next_band(6)
        b6t = Tex("The world pattern").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        w1 = Tex(r"Quakes + volcanoes trace the boundaries:").scale(0.9).shift(band_shift(6) + UP * 1.2)
        w2 = Tex(r"Ring of Fire, Mediterranean–Himalaya belt,").scale(0.9).shift(band_shift(6) + UP * 0.6)
        w3 = Tex(r"mid-ocean ridges").scale(0.9).shift(band_shift(6) + UP * 0.0)
        self.play(Write(w1))
        self.play(Write(w2))
        self.play(Write(w3))
        self.wait(2.5)
        w4 = Tex(r"South Africa: mid-plate — few natural").scale(0.9).shift(band_shift(6) + DOWN * 1.0)
        w4b = Tex(r"quakes; goldfield tremors are mining").scale(0.9).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(w4))
        self.play(Write(w4b))
        self.wait(2)
        w5 = Tex(r"Traps: plate = lithosphere; denser dives;").scale(0.85).shift(band_shift(6) + DOWN * 2.5)
        w5b = Tex(r"continent-on-continent: no volcanoes").scale(0.85).shift(band_shift(6) + DOWN * 3.1)
        self.play(Write(w5))
        self.play(Write(w5b))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the torn photograph ---
        self.next_band(7)
        b7t = Tex("The torn photograph").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        tear = Line(band_shift(7) + UP * 1.5, band_shift(7) + DOWN * 0.7, color=YELLOW)
        half_l = Rectangle(width=2.8, height=2.2).shift(band_shift(7) + LEFT * 1.6 + UP * 0.4)
        half_r = Rectangle(width=2.8, height=2.2).shift(band_shift(7) + RIGHT * 1.6 + UP * 0.4)
        self.play(Create(half_l), Create(half_r), Create(tear))
        f1 = Tex(r"Edges match: the coastline fit").scale(0.9).shift(band_shift(7) + DOWN * 1.2)
        f2 = Tex(r"Picture continues: fossils, rocks, ice").scale(0.9).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(f1))
        self.wait(2)
        self.play(Write(f2))
        self.play(Create(SurroundingRectangle(f2, color=GREEN)))
        self.wait(2)
        f3 = Tex(r"1912: no pusher named — laughed off").scale(0.9).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(f3))
        self.wait(3)

        # --- Band 8 (subtopic_6): the skin on the milk ---
        self.next_band(8)
        b8t = Tex("The skin on the milk").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        m1 = Tex(r"Warm milk rises, spreads, cools, sinks —").scale(0.9).shift(band_shift(8) + UP * 1.2)
        m1b = Tex(r"a slow wheel: convection").scale(0.9).shift(band_shift(8) + UP * 0.6)
        self.play(Write(m1))
        self.play(Write(m1b))
        self.wait(2)
        m2 = Tex(r"The skin = the plate, dragged around").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(m2))
        self.play(Create(SurroundingRectangle(m2, color=GREEN)))
        self.wait(2)
        m3 = Tex(r"Ridge bump: gravity toboggan;").scale(0.9).shift(band_shift(8) + DOWN * 1.2)
        m3b = Tex(r"belt over the table edge: slab pull").scale(0.9).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(m3))
        self.play(Write(m3b))
        self.wait(2)
        m4 = Tex(r"Sea floor: mirrored barcode of field flips").scale(0.9).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(m4))
        self.wait(3)

        # --- Band 9 (subtopic_7): three ways plates meet ---
        self.next_band(9)
        b9t = Tex("Three ways plates meet").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        v1 = Tex(r"APART — constructive: ridges,").scale(0.9).shift(band_shift(9) + UP * 1.2)
        v1b = Tex(r"rift valleys, ribbon lakes").scale(0.9).shift(band_shift(9) + UP * 0.6)
        self.play(Write(v1))
        self.play(Write(v1b))
        self.wait(2)
        v2 = Tex(r"TOGETHER — destructive: trench + Andes;").scale(0.9).shift(band_shift(9) + DOWN * 0.3)
        v2b = Tex(r"arcs like Indonesia; Himalayas —").scale(0.9).shift(band_shift(9) + DOWN * 0.9)
        v2c = Tex(r"no volcanoes when continents meet").scale(0.9).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(v2))
        self.play(Write(v2b))
        self.play(Write(v2c))
        self.play(Create(SurroundingRectangle(v2c, color=GREEN)))
        self.wait(2)
        v3 = Tex(r"PAST — conservative: straight scar,").scale(0.9).shift(band_shift(9) + DOWN * 2.4)
        v3b = Tex(r"offset fences, brutal shallow quakes").scale(0.9).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(v3))
        self.play(Write(v3b))
        self.wait(4)
