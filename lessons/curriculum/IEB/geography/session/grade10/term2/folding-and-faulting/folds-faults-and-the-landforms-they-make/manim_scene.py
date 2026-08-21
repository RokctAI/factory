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

# Band-layout whiteboard scene for "Folds, Faults and the Landforms They
# Make" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Fold waves, fault blocks and the rift/horst sketches are built from
# Line/Arrow/Rectangle/Tex.
# Subtopic durations (s): 210/240/240/235/185/190/190 of 1490.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FoldsAndFaultsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): three forces ---
        title = Tex("Folds, Faults and Their Landforms").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        f1 = Tex(r"COMPRESSION: squeeze — convergent").scale(0.95).shift(UP * 1.0)
        f2 = Tex(r"TENSION: stretch — divergent").scale(0.95).shift(UP * 0.2)
        f3 = Tex(r"SHEARING: slide — transform").scale(0.95).shift(DOWN * 0.6)
        a1 = Arrow(LEFT * 4.6 + UP * 1.0, LEFT * 3.2 + UP * 1.0, color=RED)
        a2 = Arrow(LEFT * 3.2 + UP * 0.2, LEFT * 4.6 + UP * 0.2, color=BLUE)
        self.play(Write(f1), Create(a1))
        self.wait(2)
        self.play(Write(f2), Create(a2))
        self.wait(2)
        self.play(Write(f3))
        self.wait(2)
        s1 = Tex(r"Squeeze, stretch, slide —").scale(0.95).shift(DOWN * 1.6)
        s1b = Tex(r"three forces, three boundaries").scale(0.95).shift(DOWN * 2.2)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.play(Create(SurroundingRectangle(s1b, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): bend or break ---
        self.next_band(1)
        b1t = Tex("Bend, or break?").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        c1 = Tex(r"DEPTH: hot + confined $\rightarrow$ plastic bend;").scale(0.9).shift(band_shift(1) + UP * 1.2)
        c1b = Tex(r"cold + shallow $\rightarrow$ brittle snap").scale(0.9).shift(band_shift(1) + UP * 0.6)
        c2 = Tex(r"RATE: slow creep bends, sudden force breaks").scale(0.9).shift(band_shift(1) + DOWN * 0.2)
        c3 = Tex(r"ROCK TYPE: bedded shale bends, granite cracks").scale(0.9).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(c1))
        self.play(Write(c1b))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2)
        c4 = Tex(r"Elastic $\rightarrow$ plastic $\rightarrow$ fractured $\rightarrow$ displaced").scale(0.9).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(c4))
        self.play(Create(SurroundingRectangle(c4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): anticline and syncline cross-section ---
        self.next_band(2)
        b2t = Tex("Anticline and syncline").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        w1 = Line(band_shift(2) + LEFT * 4.5 + DOWN * 0.8, band_shift(2) + LEFT * 2.5 + UP * 0.6, color=WHITE)
        w2 = Line(band_shift(2) + LEFT * 2.5 + UP * 0.6, band_shift(2) + LEFT * 0.5 + DOWN * 0.8, color=WHITE)
        w3 = Line(band_shift(2) + LEFT * 0.5 + DOWN * 0.8, band_shift(2) + RIGHT * 1.5 + UP * 0.6, color=WHITE)
        w4 = Line(band_shift(2) + RIGHT * 1.5 + UP * 0.6, band_shift(2) + RIGHT * 3.5 + DOWN * 0.8, color=WHITE)
        self.play(Create(w1), Create(w2), Create(w3), Create(w4))
        l1 = Tex(r"arch = ANTICLINE, crest on top").scale(0.85).shift(band_shift(2) + UP * 1.3 + LEFT * 2.5)
        l2 = Tex(r"trough = SYNCLINE").scale(0.85).shift(band_shift(2) + DOWN * 1.5 + LEFT * 0.5)
        self.play(Write(l1))
        self.wait(2)
        self.play(Write(l2))
        self.wait(2)
        l3 = Tex(r"Sloping sides = LIMBS, shared;").scale(0.9).shift(band_shift(2) + DOWN * 2.3)
        l3b = Tex(r"eroded anticline: OLDEST rock at the core").scale(0.9).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(l3))
        self.play(Write(l3b))
        self.play(Create(SurroundingRectangle(l3b, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): fold family + inversion ---
        self.next_band(3)
        b3t = Tex("The fold family, then the surprise").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        g1 = Tex(r"Symmetrical $\rightarrow$ asymmetrical $\rightarrow$ overfold").scale(0.9).shift(band_shift(3) + UP * 1.2)
        g1b = Tex(r"$\rightarrow$ recumbent $\rightarrow$ OVERTHRUST (nappe)").scale(0.9).shift(band_shift(3) + UP * 0.6)
        self.play(Write(g1))
        self.play(Write(g1b))
        self.wait(2.5)
        g2 = Tex(r"Overthrust = folding becomes faulting").scale(0.9).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(g2))
        self.wait(2)
        g3 = Tex(r"Anticline crest: stretched + cracked $\rightarrow$ eroded;").scale(0.85).shift(band_shift(3) + DOWN * 1.2)
        g3b = Tex(r"syncline: squeezed tight $\rightarrow$ survives").scale(0.85).shift(band_shift(3) + DOWN * 1.8)
        g4 = Tex(r"INVERSION OF RELIEF: arch becomes valley").scale(0.9).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(g3))
        self.play(Write(g3b))
        self.wait(2)
        self.play(Write(g4))
        self.play(Create(SurroundingRectangle(g4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): fault anatomy and types ---
        self.next_band(4)
        b4t = Tex("Faults: the anatomy and the types").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        plane = Line(band_shift(4) + LEFT * 1.5 + DOWN * 1.6, band_shift(4) + RIGHT * 1.0 + UP * 0.8, color=YELLOW)
        self.play(Create(plane))
        n1 = Tex(r"HANGING WALL above the plane,").scale(0.85).shift(band_shift(4) + UP * 1.3 + RIGHT * 2.6)
        n1b = Tex(r"FOOTWALL below; THROW vertical,").scale(0.85).shift(band_shift(4) + UP * 0.7 + RIGHT * 2.6)
        n1c = Tex(r"HEAVE horizontal").scale(0.85).shift(band_shift(4) + UP * 0.1 + RIGHT * 2.6)
        self.play(Write(n1))
        self.play(Write(n1b))
        self.play(Write(n1c))
        self.wait(2.5)
        n2 = Tex(r"NORMAL: tension, hanging wall DOWN — scarp").scale(0.85).shift(band_shift(4) + DOWN * 1.4)
        n3 = Tex(r"REVERSE: compression, hanging wall UP — thrust").scale(0.85).shift(band_shift(4) + DOWN * 2.0)
        n4 = Tex(r"SHEAR: sideways offset — San Andreas").scale(0.85).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(n2))
        self.wait(2)
        self.play(Write(n3))
        self.wait(2)
        self.play(Write(n4))
        self.wait(3)

        # --- Band 5 (subtopic_3): rift valley and block mountain ---
        self.next_band(5)
        b5t = Tex("Graben and horst").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        gl = Rectangle(width=1.8, height=1.4).shift(band_shift(5) + LEFT * 3.4 + UP * 0.4)
        gm = Rectangle(width=1.8, height=1.4).shift(band_shift(5) + LEFT * 1.6 + DOWN * 0.4)
        gr = Rectangle(width=1.8, height=1.4).shift(band_shift(5) + RIGHT * 0.2 + UP * 0.4)
        self.play(Create(gl), Create(gm), Create(gr))
        h1 = Tex(r"Middle block DROPS = GRABEN —").scale(0.85).shift(band_shift(5) + UP * 1.4 + RIGHT * 2.9)
        h1b = Tex(r"rift valley: East African Rift").scale(0.85).shift(band_shift(5) + UP * 0.8 + RIGHT * 2.9)
        self.play(Write(h1))
        self.play(Write(h1b))
        self.wait(2.5)
        h2 = Tex(r"Middle block STANDS = HORST —").scale(0.85).shift(band_shift(5) + DOWN * 1.5)
        h2b = Tex(r"block mountain: Black Forest and Vosges").scale(0.85).shift(band_shift(5) + DOWN * 2.1)
        h3 = Tex(r"Parallel drops = STEP FAULTING staircase").scale(0.85).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(h2))
        self.play(Write(h2b))
        self.wait(2)
        self.play(Write(h3))
        self.wait(3)

        # --- Band 6 (subtopic_4): the Cape Fold Mountains ---
        self.next_band(6)
        b6t = Tex("The Cape Fold Mountains").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        k1 = Tex(r"Cape Supergroup quartzite, squeezed").scale(0.9).shift(band_shift(6) + UP * 1.2)
        k1b = Tex(r"250–280 my ago building Gondwana").scale(0.9).shift(band_shift(6) + UP * 0.6)
        self.play(Write(k1))
        self.play(Write(k1b))
        self.wait(2.5)
        k2 = Tex(r"Two trends: N–S (Olifants River, Piketberg),").scale(0.85).shift(band_shift(6) + DOWN * 0.3)
        k2b = Tex(r"W–E (Riviersonderend, Tsitsikamma) — knot at Ceres").scale(0.85).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(k2))
        self.play(Write(k2b))
        self.wait(2.5)
        k3 = Tex(r"Valleys farm fruit and wine: Tulbagh, Robertson;").scale(0.85).shift(band_shift(6) + DOWN * 1.8)
        k3b = Tex(r"roads cross at passes: Michell's, Tradouw,").scale(0.85).shift(band_shift(6) + DOWN * 2.4)
        k3c = Tex(r"Meiringspoort").scale(0.85).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(k3))
        self.play(Write(k3b))
        self.play(Write(k3c))
        self.wait(3)

        # --- Band 7 (subtopic_4): describing structures in words ---
        self.next_band(7)
        b7t = Tex("Structures into sentences").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(1.5)
        d1 = Tex(r"Order: force, response, shape, landform").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(d1))
        self.play(Create(SurroundingRectangle(d1, color=GREEN)))
        self.wait(2)
        d2 = Tex(r"Rift valley: tension, two normal faults,").scale(0.85).shift(band_shift(7) + UP * 0.2)
        d2b = Tex(r"central block sinks, flat floor + facing scarps").scale(0.85).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(d2))
        self.play(Write(d2b))
        self.wait(2)
        d3 = Tex(r"Block mountain: straight steep sides, level top").scale(0.85).shift(band_shift(7) + DOWN * 1.3)
        d4 = Tex(r"Anticline: compression, arch, limbs dip away,").scale(0.85).shift(band_shift(7) + DOWN * 2.1)
        d4b = Tex(r"oldest rock at the core").scale(0.85).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(d3))
        self.wait(2)
        self.play(Write(d4))
        self.play(Write(d4b))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the dough and the rusk ---
        self.next_band(8)
        b8t = Tex("The dough and the rusk").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        r1 = Tex(r"Press dough inward: ridges rise — compression").scale(0.9).shift(band_shift(8) + UP * 1.2)
        r2 = Tex(r"Pull it: thins and tears — tension").scale(0.9).shift(band_shift(8) + UP * 0.5)
        r3 = Tex(r"Drag hands opposite ways: shearing").scale(0.9).shift(band_shift(8) + DOWN * 0.2)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2)
        self.play(Write(r3))
        self.wait(2)
        r4 = Tex(r"Dough bends = FOLDING;").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        r4b = Tex(r"dry rusk snaps = FAULTING").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(r4))
        self.play(Write(r4b))
        self.play(Create(SurroundingRectangle(r4b, color=GREEN)))
        r5 = Tex(r"Depth, speed, material decide").scale(0.85).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(r5))
        self.wait(3)

        # --- Band 9 (subtopic_6): hills, hollows, surprise valley ---
        self.next_band(9)
        b9t = Tex("Hills, hollows, surprise valley").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        h1 = Tex(r"Hump = anticline; dip = syncline;").scale(0.9).shift(band_shift(9) + UP * 1.2)
        h1b = Tex(r"one wavy line, limbs shared").scale(0.9).shift(band_shift(9) + UP * 0.6)
        self.play(Write(h1))
        self.play(Write(h1b))
        self.wait(2)
        h2 = Tex(r"Even, leaning, overhanging,").scale(0.9).shift(band_shift(9) + DOWN * 0.3)
        h2b = Tex(r"lying down, torn").scale(0.9).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(h2))
        self.play(Write(h2b))
        self.wait(2)
        h3 = Tex(r"Magazine spine creases outside the bend:").scale(0.85).shift(band_shift(9) + DOWN * 1.8)
        h3b = Tex(r"cracked arch erodes — arch becomes valley").scale(0.85).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(h3))
        self.play(Write(h3b))
        self.play(Create(SurroundingRectangle(h3b, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the shifting paving slabs ---
        self.next_band(10)
        b10t = Tex("The shifting paving slabs").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        p1 = Tex(r"One slab sinks: normal fault — scarp").scale(0.9).shift(band_shift(10) + UP * 1.2)
        p2 = Tex(r"Root jacks one up and over: reverse").scale(0.9).shift(band_shift(10) + UP * 0.5)
        p3 = Tex(r"Painted line offset sideways: shear").scale(0.9).shift(band_shift(10) + DOWN * 0.2)
        self.play(Write(p1))
        self.wait(2)
        self.play(Write(p2))
        self.wait(2)
        self.play(Write(p3))
        self.wait(2)
        p4 = Tex(r"Middle slab sinks: rift valley;").scale(0.9).shift(band_shift(10) + DOWN * 1.1)
        p4b = Tex(r"middle stands: block mountain; row: staircase").scale(0.9).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(p4))
        self.play(Write(p4b))
        self.wait(2)
        p5 = Tex(r"Curves bent; straight lines broke").scale(1.0).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(p5))
        self.play(Create(SurroundingRectangle(p5, color=GREEN)))
        self.wait(4)
