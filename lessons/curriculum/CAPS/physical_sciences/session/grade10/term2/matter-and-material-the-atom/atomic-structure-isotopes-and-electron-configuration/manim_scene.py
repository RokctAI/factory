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

# Band-layout whiteboard scene for atomic-structure-isotopes-and-electron-
# configuration (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects only; add-only lifecycle; Aufbau diagram hand-built
# from Rectangles + Arrows, atom sketch from Circles + Dots.
# Time apportioned to subtopics.json (230/235/235/245/180/180/190 of 1495 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AtomicStructureIsotopesConfigSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the three particles ---
        title = Tex("Atomic Structure and Configuration").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        a1 = Tex("Gold foil: most sailed through, a few").scale(1.0).shift(UP * 1.0)
        a2 = Tex("bounced back — a tiny, dense NUCLEUS").scale(1.0).shift(UP * 0.2)
        self.play(Write(a1))
        self.play(Write(a2))
        self.wait(2.5)
        a3 = Tex("Proton: charge $+1$, mass 1 (nucleus)").scale(1.0).shift(DOWN * 0.8)
        self.play(Write(a3))
        self.wait(1.8)
        a4 = Tex("Neutron: charge 0, mass 1 (nucleus)").scale(1.0).shift(DOWN * 1.6)
        self.play(Write(a4))
        self.wait(1.8)
        a5 = Tex("Electron: $-1$, mass $\\approx \\tfrac{1}{2000}$ (outside)").scale(1.0).shift(DOWN * 2.4)
        self.play(Write(a5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the atom drawn + neutrality ---
        self.next_band(1)
        b1_t = Tex("Mostly empty space").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        c = band_shift(1) + DOWN * 0.4
        nuc = Dot(c, radius=0.16)
        nuc_lab = Tex("nucleus: all the mass, all the $+$").scale(0.85).move_to(c + DOWN * 2.4)
        lvl1 = Circle(radius=0.9).move_to(c)
        lvl2 = Circle(radius=1.6).move_to(c)
        e1 = Dot(c + RIGHT * 0.9, radius=0.07)
        e2 = Dot(c + LEFT * 0.9, radius=0.07)
        e3 = Dot(c + UP * 1.6, radius=0.07)
        self.play(Create(nuc), Write(nuc_lab))
        self.wait(1.5)
        self.play(Create(lvl1), Create(lvl2))
        self.play(Create(e1), Create(e2), Create(e3))
        self.wait(2)
        b1_1 = Tex("Stadium-sized atom: nucleus = a pea").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_1))
        self.wait(2)
        b1_2 = Tex("Neutral atom: electrons $=$ protons").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_2))
        self.play(Create(SurroundingRectangle(b1_2, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): Z, A and the notation ---
        self.next_band(2)
        b2_t = Tex("Atomic number, mass number").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_1 = Tex("$Z$ = protons = the element's identity").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_1))
        self.wait(2)
        b2_2 = Tex("$A$ = protons $+$ neutrons").scale(1.0).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_2))
        self.wait(2)
        b2_3 = MathTex(r"{}^{23}_{11}\text{Na}").scale(1.4).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_3))
        self.wait(2)
        b2_4 = Tex("11 protons; $23 - 11 = 12$ neutrons;").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        b2_5 = Tex("11 electrons if neutral").scale(1.0).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_4))
        self.wait(2)
        self.play(Write(b2_5))
        self.play(Create(SurroundingRectangle(b2_5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): ions ---
        self.next_band(3)
        b3_t = Tex("Ions: electrons move, never protons").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_1 = MathTex(r"\text{Na}^{+}: 11\ \text{p}, \; 10\ \text{e}^- \; \text{(lost one)}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_1))
        self.wait(2.5)
        b3_2 = MathTex(r"\text{Cl}^{-}: 17\ \text{p}, \; 18\ \text{e}^- \; \text{(gained one)}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_2))
        self.wait(2.5)
        b3_trap = Tex("$2+$ means two electrons GAINED").scale(1.0).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_trap))
        self.play(Create(strike(b3_trap)))
        self.wait(2)
        b3_3 = Tex("$2+$ means two electrons LOST").scale(1.05).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_3))
        self.play(Create(SurroundingRectangle(b3_3, color=GREEN)))
        self.wait(2)
        b3_4 = Tex("Cation $+$ (lost); anion $-$ (gained)").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_4))
        self.wait(3)

        # --- Band 4 (subtopic_3): isotopes and the weighted average ---
        self.next_band(4)
        b4_t = Tex("Isotopes: same $Z$, different $A$").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_1 = Tex("Cl-35: 17 p, 18 n; Cl-37: 17 p, 20 n").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_1))
        self.wait(2)
        b4_2 = Tex("Same electrons: chemically identical").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_2))
        self.wait(2)
        b4_3 = MathTex(r"75\%\ \text{Cl-35}, \quad 25\%\ \text{Cl-37}").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_3))
        self.wait(2)
        b4_4 = MathTex(r"0{,}75 \times 35 = 26{,}25").scale(1.05).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_4))
        self.wait(2)
        b4_5 = MathTex(r"0{,}25 \times 37 = 9{,}25").scale(1.05).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_5))
        self.wait(2)
        b4_6 = MathTex(r"26{,}25 + 9{,}25 = 35{,}5").scale(1.1).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_6))
        self.play(Create(SurroundingRectangle(b4_6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): levels, orbitals, three rules ---
        self.next_band(5)
        b5_t = Tex("Energy levels and orbitals").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_1 = Tex("Orbital: most likely region, max 2 $e^-$").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_1))
        self.wait(2)
        b5_2 = Tex("s holds 2; the three p's together hold 6").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_2))
        self.wait(2)
        b5_3 = MathTex(r"\text{Order: } 1s,\ 2s,\ 2p,\ 3s,\ 3p,\ 4s").scale(1.05).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_3))
        self.play(Create(SurroundingRectangle(b5_3, color=GREEN)))
        self.wait(2.5)
        b5_4 = Tex("Aufbau: lowest energy first").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        b5_5 = Tex("Pairs spin opposite; spread singly first").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_4))
        self.wait(2)
        self.play(Write(b5_5))
        self.wait(3)

        # --- Band 6 (subtopic_4): sodium's Aufbau diagram + sp notation ---
        self.next_band(6)
        b6_t = Tex("Sodium: 11 electrons checked in").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)

        def orbital_box(center, n_up, n_down):
            g = VGroup(Rectangle(width=0.8, height=0.8).move_to(center))
            if n_up:
                g.add(Arrow(center + LEFT * 0.15 + DOWN * 0.28,
                            center + LEFT * 0.15 + UP * 0.28, buff=0,
                            stroke_width=3, max_tip_length_to_length_ratio=0.25))
            if n_down:
                g.add(Arrow(center + RIGHT * 0.15 + UP * 0.28,
                            center + RIGHT * 0.15 + DOWN * 0.28, buff=0,
                            stroke_width=3, max_tip_length_to_length_ratio=0.25))
            return g
        base = band_shift(6) + LEFT * 3.0
        box1s = orbital_box(base + DOWN * 1.6, 1, 1)
        lab1s = Tex("1s").scale(0.8).move_to(base + DOWN * 1.6 + LEFT * 1.0)
        box2s = orbital_box(base + DOWN * 0.5, 1, 1)
        lab2s = Tex("2s").scale(0.8).move_to(base + DOWN * 0.5 + LEFT * 1.0)
        box2p = VGroup(orbital_box(base + UP * 0.6, 1, 1),
                       orbital_box(base + UP * 0.6 + RIGHT * 1.0, 1, 1),
                       orbital_box(base + UP * 0.6 + RIGHT * 2.0, 1, 1))
        lab2p = Tex("2p").scale(0.8).move_to(base + UP * 0.6 + LEFT * 1.0)
        box3s = orbital_box(base + UP * 1.7, 1, 0)
        lab3s = Tex("3s").scale(0.8).move_to(base + UP * 1.7 + LEFT * 1.0)
        self.play(Create(box1s), Write(lab1s))
        self.wait(1.2)
        self.play(Create(box2s), Write(lab2s))
        self.wait(1.2)
        self.play(Create(box2p), Write(lab2p))
        self.wait(1.5)
        self.play(Create(box3s), Write(lab3s))
        self.wait(2)
        b6_1 = MathTex(r"\text{Na}: 1s^2\,2s^2\,2p^6\,3s^1").scale(1.05).shift(band_shift(6) + RIGHT * 3.2 + UP * 1.0)
        self.play(Write(b6_1))
        self.play(Create(SurroundingRectangle(b6_1, color=GREEN)))
        self.wait(2)
        b6_2 = MathTex(r"\text{Cl}: 1s^2\,2s^2\,2p^6\,3s^2\,3p^5").scale(0.95).shift(band_shift(6) + RIGHT * 3.2 + UP * 0.0)
        self.play(Write(b6_2))
        self.wait(2)
        b6_3 = MathTex(r"\text{Ca}: ...\,3p^6\,4s^2").scale(0.95).shift(band_shift(6) + RIGHT * 3.2 + DOWN * 0.9)
        self.play(Write(b6_3))
        self.wait(2)
        b6_4 = Tex("Check: superscripts add back to $Z$").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the stadium and the pea ---
        self.next_band(7)
        b7_t = Tex("The stadium and the pea").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_1 = Tex("Atom = stadium; nucleus = pea on the spot").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_1))
        self.wait(2)
        b7_2 = Tex("The pea: ALL the mass, all the $+$").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_2))
        self.wait(2)
        b7_3 = Tex("Stands: featherweight electrons, the $-$").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_3))
        self.wait(2)
        b7_4 = Tex("Opposites attract: the glue of the atom").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_4))
        self.wait(2)
        b7_5 = Tex("Bounce off the foil = proof of the pea").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_5))
        self.play(Create(SurroundingRectangle(b7_5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): twins with heavier backpacks ---
        self.next_band(8)
        b8_t = Tex("Twins with heavier backpacks").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_1 = Tex("Same face (17 p), same jokes (17 $e^-$)").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_1))
        self.wait(2)
        b8_2 = Tex("Backpacks differ: 18 vs 20 neutrons").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_2))
        self.wait(2)
        b8_3 = Tex("75 of 100 light, 25 heavy — school marks:").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_3))
        self.wait(2)
        b8_4 = MathTex(r"0{,}75(35) + 0{,}25(37) = 35{,}5").scale(1.05).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_4))
        self.play(Create(SurroundingRectangle(b8_4, color=GREEN)))
        self.wait(2.5)
        b8_5 = Tex("No atom weighs 35,5 — the crowd averages it").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_5))
        self.wait(3)

        # --- Band 9 (subtopic_7): filling the hotel ---
        self.next_band(9)
        b9_t = Tex("Filling the hotel from the ground floor").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_1 = Tex("Floors = levels; rooms = orbitals, sleep 2").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_1))
        self.wait(2)
        b9_2 = Tex("Cheapest room first: 1s 2s 2p 3s 3p then 4s").scale(0.95).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_2))
        self.wait(2)
        b9_3 = Tex("Roommates spin opposite; strangers spread").scale(0.95).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_3))
        self.wait(2)
        b9_4 = MathTex(r"\text{Na}: 1s^2\,2s^2\,2p^6\,3s^1 \; (= 11)").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_4))
        self.play(Create(SurroundingRectangle(b9_4, color=GREEN)))
        self.wait(2.5)
        b9_5 = Tex("Top-floor guests = valence $e^-$ = chemistry").scale(0.95).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_5))
        self.wait(4)
