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

# Band-layout whiteboard scene for "Folds, faults and the landforms they
# make" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Fold cross-sections, fault blocks and the rift-valley profile are built
# element by element from Line/Arrow/Dot/Tex (curves approximated as short
# Line chains). Subtopic durations (s): 210/240/240/235/185/190/190 of 1490.

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
        title = Tex("Folding and Faulting").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        f1 = Tex(r"Compression: squeeze — convergent").scale(1.05).shift(UP * 1.2)
        f2 = Tex(r"Tension: stretch — divergent").scale(1.05).shift(UP * 0.3)
        f3 = Tex(r"Shearing: slide — transform").scale(1.05).shift(DOWN * 0.6)
        self.play(Write(f1))
        self.wait(2)
        self.play(Write(f2))
        self.wait(2)
        self.play(Write(f3))
        self.wait(2)
        f4 = Tex(r"Squeeze, stretch, slide").scale(1.1).shift(DOWN * 1.7)
        self.play(Write(f4))
        self.play(Create(SurroundingRectangle(f4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): bend or break ---
        self.next_band(1)
        b1t = Tex("Bend or break? Three conditions").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        c1 = Tex(r"Depth: deep = plastic; shallow = brittle").scale(0.95).shift(band_shift(1) + UP * 1.2)
        c2 = Tex(r"Rate: slow bends; sudden snaps").scale(0.95).shift(band_shift(1) + UP * 0.4)
        c3 = Tex(r"Rock: strata bend; granite fractures").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2)
        c4 = Tex(r"Elastic $\Rightarrow$ plastic $\Rightarrow$ fractured").scale(1.05).shift(band_shift(1) + DOWN * 1.4)
        c5 = Tex(r"fold \quad then \quad fault").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(c4))
        self.play(Create(SurroundingRectangle(c4, color=GREEN)))
        self.wait(2)
        self.play(Write(c5))
        self.wait(3)

        # --- Band 2 (subtopic_2): anticline and syncline cross-section ---
        self.next_band(2)
        b2t = Tex("Anticline and syncline").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        # wavy stratum: up-down-up-down polyline
        pts = [
            band_shift(2) + LEFT * 5.0 + DOWN * 1.6,
            band_shift(2) + LEFT * 3.4 + UP * 0.4,
            band_shift(2) + LEFT * 1.8 + DOWN * 1.6,
            band_shift(2) + LEFT * 0.2 + UP * 0.4,
            band_shift(2) + RIGHT * 1.4 + DOWN * 1.6,
        ]
        for a, b in zip(pts, pts[1:]):
            self.play(Create(Line(a, b, color=BLUE)), run_time=0.7)
        self.wait(1.5)
        arr_l = Arrow(band_shift(2) + LEFT * 6.0 + DOWN * 0.6, band_shift(2) + LEFT * 5.2 + DOWN * 0.6, buff=0, color=RED)
        arr_r = Arrow(band_shift(2) + RIGHT * 2.6 + DOWN * 0.6, band_shift(2) + RIGHT * 1.8 + DOWN * 0.6, buff=0, color=RED)
        self.play(Create(arr_l), Create(arr_r))
        sq = Tex("compression from both sides").scale(0.85).shift(band_shift(2) + RIGHT * 3.4 + UP * 0.6)
        self.play(Write(sq))
        self.wait(1.5)
        an = Dot(band_shift(2) + LEFT * 3.4 + UP * 0.4, color=YELLOW)
        an_l = Tex("anticline crest").scale(0.8).shift(band_shift(2) + LEFT * 3.4 + UP * 1.0)
        self.play(FadeIn(an), Write(an_l))
        sy = Dot(band_shift(2) + LEFT * 1.8 + DOWN * 1.6, color=YELLOW)
        sy_l = Tex("syncline trough").scale(0.8).shift(band_shift(2) + LEFT * 1.8 + DOWN * 2.2)
        self.play(FadeIn(sy), Write(sy_l))
        self.wait(2)
        old = Tex(r"Oldest rock at the anticline's core").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(old))
        self.wait(3)

        # --- Band 3 (subtopic_2): fold family + inversion ---
        self.next_band(3)
        b3t = Tex("The fold family, by pressure").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        g1 = Tex(r"Simple $\to$ asymmetrical $\to$ overfold").scale(1.0).shift(band_shift(3) + UP * 1.2)
        g2 = Tex(r"$\to$ recumbent $\to$ overthrust (nappe)").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(g1))
        self.wait(2)
        self.play(Write(g2))
        self.wait(2)
        g3 = Tex(r"Overthrust: folding becomes faulting").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(g3))
        self.wait(2)
        g4 = Tex(r"Anticlines always form the peaks").scale(0.95).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(g4))
        self.play(Create(strike(g4)))
        g5 = Tex(r"Cracked crests erode: INVERSION").scale(1.0).shift(band_shift(3) + DOWN * 2.3)
        g5b = Tex(r"OF RELIEF — syncline stands high").scale(1.0).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(g5))
        self.play(Write(g5b))
        self.play(Create(SurroundingRectangle(VGroup(g5, g5b), color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): fault anatomy and types ---
        self.next_band(4)
        b4t = Tex("Faults: fracture PLUS movement").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        plane = Line(band_shift(4) + LEFT * 3.8 + DOWN * 2.4, band_shift(4) + LEFT * 1.8 + UP * 0.6, color=RED)
        pl_l = Tex("fault plane").scale(0.8).shift(band_shift(4) + LEFT * 3.6 + UP * 0.9)
        self.play(Create(plane), Write(pl_l))
        hw = Tex("hanging wall above").scale(0.8).shift(band_shift(4) + LEFT * 0.4 + DOWN * 0.4)
        fw = Tex("footwall below").scale(0.8).shift(band_shift(4) + LEFT * 4.4 + DOWN * 1.4)
        self.play(Write(hw), Write(fw))
        self.wait(2)
        t1 = Tex(r"Normal: tension, hanging wall DOWN").scale(0.95).shift(band_shift(4) + RIGHT * 1.4 + UP * 1.2)
        t2 = Tex(r"Reverse: compression, hanging wall UP").scale(0.95).shift(band_shift(4) + RIGHT * 1.4 + UP * 0.4)
        t3 = Tex(r"Shear: sideways offset, San Andreas").scale(0.95).shift(band_shift(4) + RIGHT * 1.4 + DOWN * 0.4 + LEFT * 0.1)
        self.play(Write(t1))
        self.wait(2)
        self.play(Write(t2))
        self.wait(2)
        self.play(Write(t3))
        self.wait(2)
        th = Tex(r"Throw = vertical; heave = horizontal").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(th))
        self.wait(3)

        # --- Band 5 (subtopic_3): rift valley and block mountain ---
        self.next_band(5)
        b5t = Tex("Graben, horst and steps").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        # rift valley profile: high-scarp-floor-scarp-high
        r_pts = [
            band_shift(5) + LEFT * 5.0 + UP * 0.6,
            band_shift(5) + LEFT * 3.4 + UP * 0.6,
            band_shift(5) + LEFT * 2.9 + DOWN * 1.2,
            band_shift(5) + LEFT * 0.7 + DOWN * 1.2,
            band_shift(5) + LEFT * 0.2 + UP * 0.6,
            band_shift(5) + RIGHT * 1.4 + UP * 0.6,
        ]
        for a, b in zip(r_pts, r_pts[1:]):
            self.play(Create(Line(a, b)), run_time=0.6)
        rv_l = Tex("rift valley (graben): dropped block,").scale(0.85).shift(band_shift(5) + RIGHT * 2.2 + DOWN * 0.6 + LEFT * 0.2)
        rv_l2 = Tex("steep straight scarps — East Africa").scale(0.85).shift(band_shift(5) + RIGHT * 2.1 + DOWN * 1.2)
        self.play(Write(rv_l))
        self.play(Write(rv_l2))
        self.wait(2.5)
        h1 = Tex(r"Horst: raised block = block mountain,").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        h2 = Tex(r"flat top, steep sides — Ruwenzori").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(h1))
        self.play(Write(h2))
        self.wait(2)
        st_l = Tex(r"Step faulting: a giant staircase").scale(0.95).shift(band_shift(5) + UP * 1.3)
        self.play(Write(st_l))
        self.wait(3)

        # --- Band 6 (subtopic_4): the Cape Fold Mountains ---
        self.next_band(6)
        b6t = Tex("The Cape Fold Mountains").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        k1 = Tex(r"Cape Supergroup quartzitic sandstone").scale(0.95).shift(band_shift(6) + UP * 1.2)
        k2 = Tex(r"Squeezed 250–280 million years ago,").scale(0.95).shift(band_shift(6) + UP * 0.4)
        k2b = Tex(r"as Gondwana assembled").scale(0.95).shift(band_shift(6) + DOWN * 0.2)
        self.play(Write(k1))
        self.wait(2)
        self.play(Write(k2))
        self.play(Write(k2b))
        self.wait(2)
        k3 = Tex(r"Parallel ranges: Cederberg, Hex River;").scale(0.9).shift(band_shift(6) + DOWN * 1.0)
        k3b = Tex(r"Langeberg, Swartberg, Outeniqua").scale(0.9).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(k3))
        self.play(Write(k3b))
        self.wait(2)
        k4 = Tex(r"Valleys: grapes, wine, fruit; passes").scale(0.9).shift(band_shift(6) + DOWN * 2.4)
        k4b = Tex(r"cross the ridges — Bain's Kloof").scale(0.9).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(k4))
        self.play(Write(k4b))
        self.wait(3)

        # --- Band 7 (subtopic_4): describing structures in words ---
        self.next_band(7)
        b7t = Tex("Describe in a fixed order").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(1.5)
        o1 = Tex(r"Force $\to$ response $\to$ shape $\to$ landform").scale(1.05).shift(band_shift(7) + UP * 1.2)
        self.play(Write(o1))
        self.play(Create(SurroundingRectangle(o1, color=GREEN)))
        self.wait(2)
        o2 = Tex(r"Rift valley: tension, two normal faults,").scale(0.9).shift(band_shift(7) + UP * 0.2)
        o2b = Tex(r"central block sank, flat floor + scarps").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(o2))
        self.play(Write(o2b))
        self.wait(2.5)
        o3 = Tex(r"Block mountain: faulted sides, raised").scale(0.9).shift(band_shift(7) + DOWN * 1.2)
        o3b = Tex(r"block, straight edges, level summit").scale(0.9).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(o3))
        self.play(Write(o3b))
        self.wait(2.5)
        o4 = Tex(r"Anticline: compression, arch, oldest").scale(0.9).shift(band_shift(7) + DOWN * 2.5)
        o4b = Tex(r"rock at the core, limbs dip away").scale(0.9).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(o4))
        self.play(Write(o4b))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): push the rug, pull the rug ---
        self.next_band(8)
        b8t = Tex("Push the rug, pull the rug").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        rg1 = Tex(r"Push a rug: ridges and hollows —").scale(1.0).shift(band_shift(8) + UP * 1.2)
        rg1b = Tex(r"fold mountains from a squeeze").scale(1.0).shift(band_shift(8) + UP * 0.6)
        self.play(Write(rg1))
        self.play(Write(rg1b))
        self.wait(2)
        rg2 = Tex(r"Pull it: it stretches and tears — tension").scale(1.0).shift(band_shift(8) + DOWN * 0.3)
        rg3 = Tex(r"Slide it: shearing at a transform edge").scale(1.0).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(rg2))
        self.wait(2)
        self.play(Write(rg3))
        self.wait(2)
        rg4 = Tex(r"Warm Prestik bends; cold chocolate").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        rg4b = Tex(r"snaps — depth, speed, rock type").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(rg4))
        self.play(Write(rg4b))
        self.play(Create(SurroundingRectangle(rg4b, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): hills, hollows, surprise valley ---
        self.next_band(9)
        b9t = Tex("Hills, hollows and the surprise valley").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        s1 = Tex(r"Up-bump = anticline (frown);").scale(1.0).shift(band_shift(9) + UP * 1.2)
        s1b = Tex(r"down-dip = syncline (smile)").scale(1.0).shift(band_shift(9) + UP * 0.6)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2)
        s2 = Tex(r"Gentle, leaning, overhanging,").scale(1.0).shift(band_shift(9) + DOWN * 0.3)
        s2b = Tex(r"lying down, torn — the fold story").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(s2))
        self.play(Write(s2b))
        self.wait(2)
        s3 = Tex(r"Bent newspaper cracks on the outside:").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        s3b = Tex(r"the arch erodes, the trough survives").scale(0.95).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(s3))
        self.play(Write(s3b))
        s4 = Tex(r"= inversion of relief").scale(1.0).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(s4))
        self.play(Create(SurroundingRectangle(s4, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the broken chocolate slab ---
        self.next_band(10)
        b10t = Tex("The broken chocolate slab").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        c1 = Tex(r"Pull apart, one drops: normal fault").scale(0.95).shift(band_shift(10) + UP * 1.2)
        c2 = Tex(r"Push together, one rides up: reverse").scale(0.95).shift(band_shift(10) + UP * 0.4)
        c3 = Tex(r"Slide past: shear — offset fences").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2)
        c4 = Tex(r"Middle drops = rift valley;").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        c4b = Tex(r"middle stands = block mountain").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(c4))
        self.play(Write(c4b))
        self.wait(2)
        c5 = Tex(r"Curved and wavy = folded;").scale(1.0).shift(band_shift(10) + DOWN * 2.7)
        c5b = Tex(r"straight and stepped = faulted").scale(1.0).shift(band_shift(10) + DOWN * 3.3)
        self.play(Write(c5))
        self.play(Write(c5b))
        self.play(Create(SurroundingRectangle(VGroup(c5, c5b), color=GREEN)))
        self.wait(4)
