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

# Band-layout whiteboard scene (see AUTHORING conventions in
# lessons/scripts/CAPS/manim_exporter.py): sequential vertical bands, one per
# teaching beat, camera moves down between bands, nothing is ever removed.
# Only exporter-supported mobjects (Tex/MathTex/Line/Arrow/Dot/Circle/
# Rectangle) are used; every line of working is a single-string MathTex
# revealed with Write. Covers all seven subtopics of the session duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7),
# with band time apportioned to subtopics.json
# (240/230/245/245/190/195/195 of 1540 s).

BAND = config.frame_height


def band_shift(k):
    """World-space shift placing content in band k (one frame-height each)."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a wrong step."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ProportionalityAndSimilaritySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the proportionality theorem, stated
        title = Tex("Proportionality and Similarity").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex(r"A line parallel to one side of a triangle").scale(1.1).shift(UP * 0.9)
        s0_l2 = Tex(r"divides the other two sides proportionally").scale(1.1).shift(UP * 0.1)
        self.play(Write(s0_l1))
        self.play(Write(s0_l2))
        self.wait(2.5)
        s0_l3 = Tex(r"If $DE \parallel BC$:").scale(1.05).shift(DOWN * 1.1)
        s0_l4 = MathTex(r"\frac{AD}{DB} = \frac{AE}{EC}").scale(1.25).shift(DOWN * 2.2)
        self.play(Write(s0_l3))
        self.play(Write(s0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the standard figure, built line by line
        self.next_band(1)
        b1_title = Tex(r"The figure: $DE \parallel BC$, join $BE$ and $CD$").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        A = band_shift(1) + UP * 1.3
        B = band_shift(1) + DOWN * 1.7 + LEFT * 2.5
        C = band_shift(1) + DOWN * 1.7 + RIGHT * 2.5
        D = A + 0.4 * (B - A)
        E = A + 0.4 * (C - A)
        side_ab = Line(A, B)
        side_ac = Line(A, C)
        side_bc = Line(B, C)
        lab_a = MathTex("A").scale(1.0).move_to(A + UP * 0.35)
        lab_b = MathTex("B").scale(1.0).move_to(B + DOWN * 0.35 + LEFT * 0.15)
        lab_c = MathTex("C").scale(1.0).move_to(C + DOWN * 0.35 + RIGHT * 0.15)
        self.play(Create(side_ab), Create(side_ac), Create(side_bc))
        self.play(Write(lab_a), Write(lab_b), Write(lab_c))
        self.wait(2)
        de = Line(D, E, color=YELLOW)
        lab_d = MathTex("D").scale(0.9).move_to(D + LEFT * 0.35)
        lab_e = MathTex("E").scale(0.9).move_to(E + RIGHT * 0.35)
        self.play(Create(de), Write(lab_d), Write(lab_e))
        self.wait(2)
        be = Line(B, E, color=BLUE)
        cd = Line(C, D, color=BLUE)
        self.play(Create(be), Create(cd))
        self.wait(2)
        b1_note = Tex(r"The whole construction: two joins").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_note))
        self.wait(2.5)

        # --- Band 2 (subtopic_1): the area proof, line by line
        self.next_band(2)
        b2_title = Tex(r"Proof by areas ($\tfrac{1}{2}$ base $\times$ height)").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l0 = Tex(r"Write $[XYZ]$ for the area of $XYZ$").scale(0.95).shift(band_shift(2) + UP * 1.4)
        b2_l1 = MathTex(r"\frac{[ADE]}{[BDE]} = \frac{AD}{DB} \;\;\text{(height from } E)").scale(0.95).shift(band_shift(2) + UP * 0.5)
        b2_l2 = MathTex(r"\frac{[ADE]}{[CED]} = \frac{AE}{EC} \;\;\text{(height from } D)").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        b2_l3 = Tex(r"$BDE$, $CED$: same base $DE$, same parallels").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        b2_l4 = MathTex(r"\Rightarrow\; [BDE] = [CED]").scale(1.05).shift(band_shift(2) + DOWN * 2.1)
        b2_l5 = MathTex(r"\therefore\; \frac{AD}{DB} = \frac{AE}{EC}").scale(1.1).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l0))
        self.wait(1.5)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): worked ratio case
        self.next_band(3)
        b3_title = Tex(r"$DE \parallel BC$: $AD=6$, $DB=4$, $AE=9$. Find $EC$.").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\frac{AD}{DB} = \frac{AE}{EC}").scale(1.15).shift(band_shift(3) + UP * 1.0)
        b3_l2 = MathTex(r"\frac{6}{4} = \frac{9}{EC}").scale(1.15).shift(band_shift(3) + UP * 0.0)
        b3_l3 = MathTex(r"6\,EC = 36").scale(1.15).shift(band_shift(3) + DOWN * 0.9)
        b3_l4 = MathTex(r"EC = 6").scale(1.2).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = MathTex(r"\text{Check wholes: } \frac{6}{10} = \frac{9}{15} = \frac{3}{5}").scale(1.05).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_2): the part/whole trap, and the converse
        self.next_band(4)
        b4_title = Tex("Match part with part, whole with whole").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_wrong = MathTex(r"\frac{6}{4} = \frac{9}{15}\,?").scale(1.15).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2)
        b4_l0 = Tex(r"Part-to-part equated with part-to-whole — never").scale(0.95).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l0))
        self.wait(2)
        b4_l1 = Tex(r"Say what each segment is before you equate").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex(r"Converse: equal ratios $\Rightarrow$ parallel").scale(1.05).shift(band_shift(4) + DOWN * 1.4)
        b4_l3 = Tex(r"Reason: line divides two sides in proportion").scale(0.95).shift(band_shift(4) + DOWN * 2.2)
        b4_l4 = Tex(r"Midpoint theorem $=$ the $1:1$ special case").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): equiangular triangles are similar — the proof
        self.next_band(5)
        b5_title = Tex(r"Equiangular $\Rightarrow$ sides in proportion").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\text{On } AB \text{ mark } H: \; AH = DE").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l1b = MathTex(r"\text{On } AC \text{ mark } K: \; AK = DF").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l2 = MathTex(r"\triangle AHK \equiv \triangle DEF \;\; \text{(SAS)}").scale(1.05).shift(band_shift(5) + DOWN * 0.4)
        b5_l3 = MathTex(r"\hat{H} = \hat{E} = \hat{B} \;\Rightarrow\; HK \parallel BC").scale(1.05).shift(band_shift(5) + DOWN * 1.3)
        b5_l4 = MathTex(r"\frac{AH}{AB} = \frac{AK}{AC}").scale(1.05).shift(band_shift(5) + DOWN * 2.2)
        b5_l5 = MathTex(r"\Rightarrow\; \frac{DE}{AB} = \frac{DF}{AC}").scale(1.05).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l1b))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2.5)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_3): the order of the letters IS the pairing
        self.next_band(6)
        b6_title = Tex("Notation carries marks: order = pairing").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\triangle ABC \sim \triangle DEF").scale(1.2).shift(band_shift(6) + UP * 1.0)
        b6_l2 = MathTex(r"A \to D, \quad B \to E, \quad C \to F").scale(1.05).shift(band_shift(6) + UP * 0.0)
        b6_l3 = MathTex(r"\frac{AB}{DE} = \frac{BC}{EF} = \frac{AC}{DF}").scale(1.15).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l3b = Tex(r"Converse: sides in proportion $\Rightarrow$ equiangular").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l3b))
        self.wait(2)
        b6_l4 = Tex("Match equal angles first, then write the vertices").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): Pythagoras — the altitude figure
        self.next_band(7)
        b7_title = Tex(r"Right angle at $A$; altitude $AD$ to hypotenuse $BC$").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        Bp = band_shift(7) + DOWN * 1.6 + LEFT * 2.4
        Cp = band_shift(7) + DOWN * 1.6 + RIGHT * 2.4
        Ap = band_shift(7) + UP * 0.6 + LEFT * 0.96
        Dp = band_shift(7) + DOWN * 1.6 + LEFT * 0.96
        t_ab = Line(Ap, Bp)
        t_ac = Line(Ap, Cp)
        t_bc = Line(Bp, Cp)
        alt = Line(Ap, Dp, color=YELLOW)
        lab2_a = MathTex("A").scale(1.0).move_to(Ap + UP * 0.35)
        lab2_b = MathTex("B").scale(1.0).move_to(Bp + DOWN * 0.35 + LEFT * 0.1)
        lab2_c = MathTex("C").scale(1.0).move_to(Cp + DOWN * 0.35 + RIGHT * 0.1)
        lab2_d = MathTex("D").scale(0.9).move_to(Dp + DOWN * 0.35)
        self.play(Create(t_ab), Create(t_ac), Create(t_bc))
        self.play(Write(lab2_a), Write(lab2_b), Write(lab2_c))
        self.wait(2)
        self.play(Create(alt), Write(lab2_d))
        self.wait(2)
        b7_l1 = Tex(r"Right angle + shared $\hat{B}$: similar to the whole").scale(0.95).shift(band_shift(7) + DOWN * 2.3)
        b7_l2 = MathTex(r"\triangle ABD \sim \triangle CBA").scale(1.05).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(3)

        # --- Band 8 (subtopic_4): Pythagoras delivered by similarity
        self.next_band(8)
        b8_title = Tex("Pythagoras by similar triangles").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"\frac{AB}{CB} = \frac{BD}{BA} \;\Rightarrow\; AB^2 = BD \times BC").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"\text{Similarly: } AC^2 = CD \times CB").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"AB^2 + AC^2 = BC\,(BD + DC)").scale(1.1).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = MathTex(r"BD + DC = BC").scale(1.1).shift(band_shift(8) + DOWN * 1.7)
        b8_l5 = MathTex(r"\therefore\; AB^2 + AC^2 = BC^2").scale(1.2).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_4): the projection and altitude relations
        self.next_band(9)
        b9_title = Tex("The stepping stones have their own questions").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(1.5)
        b9_l1 = MathTex(r"AB^2 = BD \times BC").scale(1.1).shift(band_shift(9) + UP * 1.2)
        b9_l1b = Tex(r"(leg$^2$ = projection $\times$ hypotenuse)").scale(0.95).shift(band_shift(9) + UP * 0.4)
        b9_l2 = MathTex(r"AD^2 = BD \times DC \quad \text{(altitude)}").scale(1.05).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l1b))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"BD = 4, \; DC = 9: \quad AD^2 = 4 \times 9 = 36").scale(1.05).shift(band_shift(9) + DOWN * 1.5)
        b9_l4 = MathTex(r"AD = 6").scale(1.2).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 10 (subtopic_5): the ladder against the wall
        self.next_band(10)
        b10_title = Tex("The ladder against the wall").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Sun rays are parallel: halfway up the ladder").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex(r"lands halfway along the shadow").scale(1.05).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"ladder top : bottom $=$ shadow top : bottom").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex(r"Same base, tips on the same parallel: equal areas").scale(1.0).shift(band_shift(10) + DOWN * 2.0)
        b10_l5 = Tex(r"Part with part, whole with whole — always").scale(1.05).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_6): the photograph and its enlargement
        self.next_band(11)
        b11_title = Tex("The photograph and its enlargement").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex(r"Enlargement: angles survive, sides share one factor").scale(1.0).shift(band_shift(11) + UP * 1.1)
        b11_l2 = Tex(r"Triangles only: equal angles ALREADY give the factor").scale(1.0).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11_l1))
        self.wait(2.5)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = MathTex(r"\text{Person 2 m, shadow 3 m; pole shadow 9 m}").scale(1.0).shift(band_shift(11) + DOWN * 0.8)
        b11_l4 = MathTex(r"\text{pole} = \frac{2}{3} \times 9 = 6 \text{ m}").scale(1.1).shift(band_shift(11) + DOWN * 1.8)
        self.play(Write(b11_l3))
        self.wait(2)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        b11_l5 = Tex(r"Matching corners in matching order — always").scale(1.0).shift(band_shift(11) + DOWN * 2.9)
        self.play(Write(b11_l5))
        self.wait(3)

        # --- Band 12 (subtopic_7): the folded corner — Pythagoras rebuilt
        self.next_band(12)
        b12_title = Tex("The folded corner — Pythagoras rebuilt").scale(1.15).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12_title))
        self.wait(2)
        b12_l1 = Tex(r"Fold the right angle onto the hypotenuse:").scale(1.05).shift(band_shift(12) + UP * 1.1)
        b12_l2 = Tex(r"each small triangle is a photo of the whole").scale(1.05).shift(band_shift(12) + UP * 0.3)
        self.play(Write(b12_l1))
        self.play(Write(b12_l2))
        self.wait(2.5)
        b12_l3 = MathTex(r"\text{leg}^2 = \text{hyp} \times \text{its piece}").scale(1.05).shift(band_shift(12) + DOWN * 0.5)
        self.play(Write(b12_l3))
        self.wait(2)
        b12_l3b = MathTex(r"\text{add both} \;\Rightarrow\; \text{hyp}^2").scale(1.05).shift(band_shift(12) + DOWN * 1.3)
        self.play(Write(b12_l3b))
        self.wait(2.5)
        b12_l4 = MathTex(r"\text{Bonus: fold}^2 = 4 \times 9 = 36").scale(1.05).shift(band_shift(12) + DOWN * 2.1)
        b12_l5 = MathTex(r"\text{fold} = 6").scale(1.15).shift(band_shift(12) + DOWN * 2.9)
        self.play(Write(b12_l4))
        self.wait(2)
        self.play(Write(b12_l5))
        self.play(Create(SurroundingRectangle(b12_l5, color=GREEN)))
        self.wait(4)
