# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene for "Plate boundaries and plate movement"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). The
# convection cell, subduction cross-section and rift profile are hand-built
# from Line/Arrow/Dot/Circle/Tex, element by element with the script.
# Subtopic durations (s): 225/220/230/235/185/190/195 of 1480.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PlateTectonicsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): Pangaea and the four proofs ---
        title = Tex("Plate Boundaries and Plate Movement").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        w1 = Tex(r"Wegener 1912: Pangaea broke into").scale(1.0).shift(UP * 1.3)
        w1b = Tex(r"Laurasia + Gondwana, 200 mya").scale(1.0).shift(UP * 0.7)
        self.play(Write(w1))
        self.play(Write(w1b))
        self.wait(2)
        e1 = Tex(r"1. Fit: S America nests into Africa").scale(0.95).shift(DOWN * 0.2)
        e2 = Tex(r"2. Fossils: Mesosaurus, Glossopteris").scale(0.95).shift(DOWN * 0.9)
        e3 = Tex(r"3. Rocks: Cape Folds continue overseas").scale(0.95).shift(DOWN * 1.6)
        e4 = Tex(r"4. Climate: Dwyka tillite, polar coal").scale(0.95).shift(DOWN * 2.3)
        self.play(Write(e1))
        self.wait(2)
        self.play(Write(e2))
        self.wait(2)
        self.play(Write(e3))
        self.wait(2)
        self.play(Write(e4))
        self.wait(2)
        e5 = Tex(r"Rejected: no mechanism — yet").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(e5))
        self.wait(3)

        # --- Band 1 (subtopic_2): the convection engine ---
        self.next_band(1)
        b1t = Tex("The engine: mantle convection").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        # convection cell of straight arrows
        v_up = Arrow(band_shift(1) + LEFT * 3.4 + DOWN * 2.6, band_shift(1) + LEFT * 3.4 + DOWN * 0.6, buff=0, color=RED)
        v_side = Arrow(band_shift(1) + LEFT * 3.4 + DOWN * 0.6, band_shift(1) + LEFT * 0.8 + DOWN * 0.6, buff=0, color=RED)
        v_dn = Arrow(band_shift(1) + LEFT * 0.8 + DOWN * 0.6, band_shift(1) + LEFT * 0.8 + DOWN * 2.6, buff=0, color=BLUE)
        v_back = Arrow(band_shift(1) + LEFT * 0.8 + DOWN * 2.6, band_shift(1) + LEFT * 3.4 + DOWN * 2.6, buff=0, color=BLUE)
        self.play(Create(v_up))
        self.play(Create(v_side))
        self.play(Create(v_dn))
        self.play(Create(v_back))
        cell_l = Tex("hot rises, spreads, cools, sinks").scale(0.85).shift(band_shift(1) + RIGHT * 2.9 + DOWN * 1.4)
        self.play(Write(cell_l))
        self.wait(2)
        s1 = Tex(r"SOLID rock flowing plastically —").scale(0.95).shift(band_shift(1) + UP * 1.2)
        s1b = Tex(r"fingernail speed, not a lava lake").scale(0.95).shift(band_shift(1) + UP * 0.6)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2)
        s2 = Tex(r"Ridge push + slab pull do the work").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(s2))
        self.play(Create(SurroundingRectangle(s2, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): sea-floor spreading proof ---
        self.next_band(2)
        b2t = Tex("Sea-floor spreading: the two proofs").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        ridge = Line(band_shift(2) + DOWN * 2.6, band_shift(2) + DOWN * 0.8, color=RED)
        r_lab = Tex("ridge").scale(0.8).shift(band_shift(2) + DOWN * 0.5)
        self.play(Create(ridge), Write(r_lab))
        aw = Arrow(band_shift(2) + LEFT * 0.4 + DOWN * 1.7, band_shift(2) + LEFT * 2.6 + DOWN * 1.7, buff=0, color=YELLOW)
        ae = Arrow(band_shift(2) + RIGHT * 0.4 + DOWN * 1.7, band_shift(2) + RIGHT * 2.6 + DOWN * 1.7, buff=0, color=YELLOW)
        self.play(Create(aw), Create(ae))
        sp = Tex("new crust carried both ways").scale(0.85).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(sp))
        self.wait(2)
        p1 = Tex(r"1. Age: youngest at the ridge,").scale(0.95).shift(band_shift(2) + UP * 1.3)
        p1b = Tex(r"never older than 200 my").scale(0.95).shift(band_shift(2) + UP * 0.7)
        self.play(Write(p1))
        self.play(Write(p1b))
        self.wait(2)
        p2 = Tex(r"2. Magnetic stripes mirrored").scale(0.95).shift(band_shift(2) + UP * 0.0)
        p2b = Tex(r"either side — a tape recording").scale(0.95).shift(band_shift(2) + DOWN * 0.6 + RIGHT * 3.0)
        self.play(Write(p2))
        self.play(Write(p2b))
        self.wait(3)

        # --- Band 3 (subtopic_3): divergent and transform ---
        self.next_band(3)
        b3t = Tex("Divergent and transform boundaries").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        d1 = Tex(r"Divergent = constructive: new crust").scale(0.95).shift(band_shift(3) + UP * 1.3)
        d2 = Tex(r"Ocean: mid-ocean ridge, fissure lava,").scale(0.9).shift(band_shift(3) + UP * 0.6)
        d2b = Tex(r"shallow quakes — Iceland").scale(0.9).shift(band_shift(3) + UP * 0.0)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.play(Write(d2b))
        self.wait(2)
        d3 = Tex(r"Continent: East African Rift — floor").scale(0.9).shift(band_shift(3) + DOWN * 0.8)
        d3b = Tex(r"sinks, scarps, lakes, Kilimanjaro").scale(0.9).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(d3))
        self.play(Write(d3b))
        self.wait(2)
        d4 = Tex(r"Transform = conservative: slide past,").scale(0.9).shift(band_shift(3) + DOWN * 2.2)
        d4b = Tex(r"no volcanoes, violent shallow quakes").scale(0.9).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(d4))
        self.play(Write(d4b))
        self.wait(3)

        # --- Band 4 (subtopic_4): subduction cross-section ---
        self.next_band(4)
        b4t = Tex("Convergent: ocean meets continent").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        sea = Line(band_shift(4) + LEFT * 5.2 + UP * 0.4, band_shift(4) + LEFT * 1.4 + UP * 0.4, color=BLUE)
        cont = Line(band_shift(4) + LEFT * 1.0 + UP * 0.8, band_shift(4) + RIGHT * 4.6 + UP * 0.8, stroke_width=6)
        self.play(Create(sea), Create(cont))
        slab = Line(band_shift(4) + LEFT * 5.0 + UP * 0.2, band_shift(4) + LEFT * 1.4 + UP * 0.2, color=BLUE)
        dive = Line(band_shift(4) + LEFT * 1.4 + UP * 0.2, band_shift(4) + RIGHT * 1.6 + DOWN * 2.4, color=BLUE)
        self.play(Create(slab))
        self.play(Create(dive))
        tr = Dot(band_shift(4) + LEFT * 1.4 + UP * 0.3, color=YELLOW)
        tr_l = Tex("trench").scale(0.8).shift(band_shift(4) + LEFT * 1.6 + DOWN * 0.4)
        self.play(FadeIn(tr), Write(tr_l))
        self.wait(2)
        dens = Tex(r"denser plate ($3{,}0$ vs $2{,}7$) subducts").scale(0.9).shift(band_shift(4) + LEFT * 1.4 + DOWN * 1.6 + LEFT * 1.6)
        self.play(Write(dens))
        self.wait(2)
        volc = Arrow(band_shift(4) + RIGHT * 1.2 + UP * 0.9, band_shift(4) + RIGHT * 1.2 + UP * 2.0, buff=0, color=RED)
        volc_l = Tex("fold mountains + volcanoes").scale(0.85).shift(band_shift(4) + RIGHT * 3.3 + UP * 1.6)
        self.play(Create(volc), Write(volc_l))
        an = Tex(r"Nazca under S America: Andes").scale(0.9).shift(band_shift(4) + RIGHT * 1.8 + DOWN * 2.9 + LEFT * 0.4)
        self.play(Write(an))
        self.wait(3)

        # --- Band 5 (subtopic_4): the other two collisions ---
        self.next_band(5)
        b5t = Tex("The other convergent cases").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        o1 = Tex(r"Ocean vs ocean: older colder sinks —").scale(0.95).shift(band_shift(5) + UP * 1.2)
        o1b = Tex(r"Mariana Trench + island arc (Japan)").scale(0.95).shift(band_shift(5) + UP * 0.6)
        self.play(Write(o1))
        self.play(Write(o1b))
        self.wait(2.5)
        o2 = Tex(r"Continent vs continent: neither sinks,").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        o2b = Tex(r"rock crumples UP — Himalayas rising").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(o2))
        self.play(Write(o2b))
        self.wait(2.5)
        o3 = Tex(r"Continental collision has volcanoes").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(o3))
        self.play(Create(strike(o3)))
        o4 = Tex(r"No slab sinks, so no magma, none").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(o4))
        self.play(Create(SurroundingRectangle(o4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the world pattern ---
        self.next_band(6)
        b6t = Tex("The world pattern").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        p1 = Tex(r"Quakes and volcanoes trace boundaries:").scale(0.95).shift(band_shift(6) + UP * 1.2)
        p2 = Tex(r"Ring of Fire, Med–Himalaya belt, ridges").scale(0.95).shift(band_shift(6) + UP * 0.5)
        self.play(Write(p1))
        self.play(Write(p2))
        self.wait(2.5)
        p3 = Tex(r"SA sits mid-plate: few natural quakes;").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        p3b = Tex(r"Gauteng tremors are mining-induced").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(p3))
        self.play(Write(p3b))
        self.wait(2.5)
        p4 = Tex(r"Traps: plate = lithosphere; subduction").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        p4b = Tex(r"follows density, never size").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(p4))
        self.play(Write(p4b))
        self.play(Create(SurroundingRectangle(p4b, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the torn newspaper ---
        self.next_band(7)
        b7t = Tex("The torn newspaper").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        n1 = Tex(r"Ragged edge = the coastline fit").scale(1.0).shift(band_shift(7) + UP * 1.2)
        n2 = Tex(r"Sentences across the tear:").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(n1))
        self.wait(2)
        self.play(Write(n2))
        self.wait(1.5)
        n3 = Tex(r"Mesosaurus in the Karoo AND Brazil").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        n4 = Tex(r"Cape Folds continue in Argentina").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        n5 = Tex(r"Dwyka glacier rubble under the Karoo").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(n3))
        self.wait(2)
        self.play(Write(n4))
        self.wait(2)
        self.play(Write(n5))
        self.wait(2)
        n6 = Tex(r"Laughed at: he couldn't say what pushed").scale(0.9).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(n6))
        self.wait(3)

        # --- Band 8 (subtopic_6): the pot of pap ---
        self.next_band(8)
        b8t = Tex("The pot on the stove").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        q1 = Tex(r"Pap rises, spreads, cools, sinks —").scale(1.0).shift(band_shift(8) + UP * 1.2)
        q1b = Tex(r"the mantle does it at fingernail speed").scale(1.0).shift(band_shift(8) + UP * 0.6)
        self.play(Write(q1))
        self.play(Write(q1b))
        self.wait(2)
        q2 = Tex(r"The cooled skin = the lithosphere,").scale(1.0).shift(band_shift(8) + DOWN * 0.3)
        q2b = Tex(r"dragged along by the circulation").scale(1.0).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(q2))
        self.play(Write(q2b))
        self.wait(2)
        q3 = Tex(r"Push off the ridge hump; tablecloth").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        q3b = Tex(r"pull of the sinking slab").scale(0.95).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(q3))
        self.play(Write(q3b))
        self.wait(2)
        q4 = Tex(r"Sea floor kept the receipt: age + stripes").scale(0.95).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(q4))
        self.play(Create(SurroundingRectangle(q4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): three ways plates meet ---
        self.next_band(9)
        b9t = Tex("Three ways plates meet").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        m1 = Tex(r"Apart (constructive): ridge or rift,").scale(0.95).shift(band_shift(9) + UP * 1.2)
        m1b = Tex(r"new land — Iceland, East African Rift").scale(0.95).shift(band_shift(9) + UP * 0.6)
        self.play(Write(m1))
        self.play(Write(m1b))
        self.wait(2)
        m2 = Tex(r"Together (destructive): heavier dives —").scale(0.95).shift(band_shift(9) + DOWN * 0.2)
        m2b = Tex(r"trench, Andes, Japan; Himalayas up").scale(0.95).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(m2))
        self.play(Write(m2b))
        self.wait(2)
        m3 = Tex(r"Past (conservative): San Andreas —").scale(0.95).shift(band_shift(9) + DOWN * 1.6)
        m3b = Tex(r"no volcanoes, big jolts, offset roads").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(m3))
        self.play(Write(m3b))
        self.wait(2)
        m4 = Tex(r"Apart, together, past").scale(1.1).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(m4))
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(4)
