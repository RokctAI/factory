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

# Band-layout whiteboard scene for the Molecular Shapes and Polarity duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (250/240/230/240/185/185/195
# of 1525 s). Exporter-safe mobjects only (energy curve and molecules drawn
# from Lines, Circles, Dots and Tex labels); add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MolecularShapesPolaritySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): why atoms bond — the energy hollow ---
        title = Tex("Molecular Shapes and Polarity").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        # potential energy vs distance: polyline valley
        ax_x = Arrow(LEFT * 4.6 + DOWN * 1.2, RIGHT * 3.4 + DOWN * 1.2, buff=0)
        ax_y = Arrow(LEFT * 4.6 + DOWN * 2.6, LEFT * 4.6 + UP * 1.4, buff=0)
        lx = Tex("distance").scale(0.7).shift(RIGHT * 3.6 + DOWN * 1.6)
        ly = Tex("energy").scale(0.7).shift(LEFT * 4.6 + UP * 1.7)
        curve = VGroup(
            Line(LEFT * 4.2 + UP * 1.2, LEFT * 3.4 + DOWN * 0.6, color=YELLOW),
            Line(LEFT * 3.4 + DOWN * 0.6, LEFT * 2.4 + DOWN * 2.2, color=YELLOW),
            Line(LEFT * 2.4 + DOWN * 2.2, LEFT * 1.2 + DOWN * 1.6, color=YELLOW),
            Line(LEFT * 1.2 + DOWN * 1.6, RIGHT * 0.6 + DOWN * 1.35, color=YELLOW),
            Line(RIGHT * 0.6 + DOWN * 1.35, RIGHT * 3.0 + DOWN * 1.25, color=YELLOW),
        )
        self.play(Create(ax_x), Create(ax_y), Write(lx), Write(ly))
        self.play(Create(curve))
        self.wait(2)
        vmin = Dot(LEFT * 2.4 + DOWN * 2.2, color=GREEN)
        self.play(Create(vmin))
        b0_l1 = Tex("Minimum: bond length 74 pm, depth = bond energy").scale(0.8).shift(UP * 0.8)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex("Helium: full shells, no hollow, no bond").scale(0.85).shift(UP * 0.0)
        self.play(Write(b0_l2))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): Lewis diagrams ---
        self.next_band(1)
        b1_title = Tex("Lewis diagrams: every valence electron counted").scale(1.0).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Water: 2 bonding pairs, 2 lone pairs on O").scale(0.9).shift(band_shift(1) + UP * 1.3)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Ammonia: 3 bonds, 1 lone pair").scale(0.9).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Methane: 4 bonds, no lone pairs").scale(0.9).shift(band_shift(1) + DOWN * 0.3)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex(r"Multiple bonds: O$_2$ double, N$_2$ triple, HCN mixed").scale(0.85).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("Dative: one atom donates BOTH electrons").scale(0.9).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=BLUE)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): VSEPR shapes ---
        self.next_band(2)
        b2_title = Tex("Pairs repel: spread as far as possible").scale(1.05).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.play(Create(SurroundingRectangle(b2_title, color=BLUE)))
        self.wait(2)
        b2_l1 = Tex(r"2 groups: LINEAR, $180^\circ$ — CO$_2$").scale(0.9).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"3 groups: TRIGONAL PLANAR, $120^\circ$ — BF$_3$").scale(0.9).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"4 pairs: TETRAHEDRAL, $109{,}5^\circ$ — CH$_4$").scale(0.9).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l3))
        self.wait(2)
        # tetrahedron sketch: central dot with four bonds
        c = Dot(DOWN * 2.2, color=YELLOW).shift(band_shift(2))
        e1 = Line(DOWN * 2.2, DOWN * 1.2 + RIGHT * 0.0).shift(band_shift(2))
        e2 = Line(DOWN * 2.2, DOWN * 3.0 + LEFT * 1.0).shift(band_shift(2))
        e3 = Line(DOWN * 2.2, DOWN * 3.0 + RIGHT * 1.0).shift(band_shift(2))
        e4 = Line(DOWN * 2.2, DOWN * 2.6 + RIGHT * 0.35).shift(band_shift(2))
        self.play(Create(c), Create(e1), Create(e2), Create(e3), Create(e4))
        b2_l4 = Tex("The flat cross on paper is only a shadow").scale(0.8).shift(band_shift(2) + DOWN * 3.4)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): lone pairs and shrinking angles ---
        self.next_band(3)
        b3_title = Tex("Lone pairs: invisible corners").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Methane: 4 bonds — tetrahedral, $109{,}5^\circ$").scale(0.9).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex(r"Ammonia: 1 lone pair — pyramid, $\approx 107^\circ$").scale(0.9).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex(r"Water: 2 lone pairs — angular, $\approx 104{,}5^\circ$").scale(0.9).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Lone pairs sit closer and repel harder").scale(0.9).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Name the shape from visible atoms only").scale(0.9).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): electronegativity ---
        self.next_band(4)
        b4_title = Tex("Electronegativity: pull on the shared pair").scale(1.05).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("F 4,0 \\quad O 3,5 \\quad N, Cl 3,0 \\quad C 2,5 \\quad H 2,1 \\quad Na 0,9").scale(0.8).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex(r"$\Delta EN = 0$: non-polar covalent (Cl–Cl)").scale(0.9).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex(r"Moderate $\Delta EN$: polar covalent — H–F: $4{,}0 - 2{,}1 = 1{,}9$").scale(0.85).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex(r"$\delta-$ on the stronger puller, $\delta+$ on the weaker").scale(0.85).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex(r"$\Delta EN \gtrsim 2$: ionic — Na–Cl: $3{,}0 - 0{,}9 = 2{,}1$").scale(0.85).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=BLUE)))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the sliding scale ---
        self.next_band(5)
        b5_title = Tex("One slide, no wall").scale(1.15).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        slide = Arrow(LEFT * 4.5 + UP * 0.8, RIGHT * 4.5 + UP * 0.8, buff=0, color=YELLOW)
        slide.shift(band_shift(5))
        self.play(Create(slide))
        s1 = Tex("fair sharing").scale(0.75).shift(band_shift(5) + LEFT * 3.6 + UP * 1.4)
        s2 = Tex("unfair sharing").scale(0.75).shift(band_shift(5) + UP * 1.4)
        s3 = Tex("taking").scale(0.75).shift(band_shift(5) + RIGHT * 3.6 + UP * 1.4)
        self.play(Write(s1), Write(s2), Write(s3))
        self.wait(2.5)
        b5_l1 = Tex(r"Position marker: $\Delta EN$").scale(0.95).shift(band_shift(5) + DOWN * 0.2)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2.5)
        b5_l2 = Tex("C–H 0,4 faint; O–H 1,4 strong; Na–Cl 2,1 ionic").scale(0.85).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Rank, label the ends, classify — data sheet in hand").scale(0.85).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l3))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): polar bonds vs polar molecules ---
        self.next_band(6)
        b6_title = Tex("Polar bond $\\neq$ polar molecule").scale(1.1).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.play(Create(SurroundingRectangle(b6_title, color=BLUE)))
        self.wait(2)
        # CO2: linear, arrows opposing
        co2 = Tex(r"O $=$ C $=$ O").scale(0.95).shift(band_shift(6) + UP * 1.1)
        a1 = Arrow(ORIGIN + UP * 0.6, LEFT * 1.6 + UP * 0.6, buff=0, color=RED).shift(band_shift(6))
        a2 = Arrow(ORIGIN + UP * 0.6, RIGHT * 1.6 + UP * 0.6, buff=0, color=RED).shift(band_shift(6))
        self.play(Write(co2))
        self.play(Create(a1), Create(a2))
        b6_l1 = Tex("Linear: equal, opposite, cancelled — non-polar").scale(0.85).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex("Water: angular — the dipoles add").scale(0.85).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex(r"$\delta-$ oxygen end, $\delta+$ hydrogen side: polar").scale(0.85).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("Polar bonds AND an uncancelling shape").scale(0.9).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): bond length and bond energy ---
        self.next_band(7)
        b7_title = Tex("Shorter means stronger").scale(1.15).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Bond length: nucleus-to-nucleus at the minimum").scale(0.85).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("Bond energy: the cost of breaking it").scale(0.85).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"C–C $>$ C$=$C $>$ C$\equiv$C in length; reversed in strength").scale(0.85).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex(r"N$\equiv$N: the triple bond that calms the atmosphere").scale(0.85).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Bigger atoms: longer, weaker bonds down a group").scale(0.85).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): why atoms hold hands ---
        self.next_band(8)
        b8_title = Tex("Why atoms hold hands").scale(1.2).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Bonding pays in lowered energy — comfort").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("A marble settles in the hollow: bond length").scale(0.9).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Hollow depth: how hard to pull apart").scale(0.9).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Helium: already full, no hollow, drifts on alone").scale(0.9).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Nitrogen: a triple handshake, near-impossible to undo").scale(0.85).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): balloons tied at the centre ---
        self.next_band(9)
        b9_title = Tex("Balloons tied at the centre").scale(1.15).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Each balloon shoves the rest as far as it can").scale(0.9).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Two: a line. Three: a triangle. Four: a tetrahedron").scale(0.9).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Lone pairs are invisible balloons — still shoving").scale(0.9).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex(r"$109{,}5^\circ \rightarrow 107^\circ \rightarrow 104{,}5^\circ$ as balloons vanish").scale(0.9).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Count all the pairs; name only the visible atoms").scale(0.9).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): fair and unfair tug-of-war ---
        self.next_band(10)
        b10_title = Tex("Fair and unfair tug-of-war").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Equal pull: flag in the middle — non-polar").scale(0.9).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex(r"Unequal pull: $\delta-$ winner, $\delta+$ loser — a dipole").scale(0.9).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Gap of about 2: confiscation — ionic").scale(0.9).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"CO$_2$: straight line, pulls cancel — fair overall").scale(0.9).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Water: bent, pulls add — the polar molecule that runs the world").scale(0.8).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
