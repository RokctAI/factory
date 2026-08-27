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

# Band-layout whiteboard scene (see AUTHORING-SPEC / quadratics-by-factorisation
# worked example). One band per teaching beat, camera moves down, nothing is
# ever removed. Covers all seven subtopics of the session duo:
# Part 1 — Expert (subtopics 1-4), Part 2 — Simplifier (subtopics 5-7),
# band time apportioned to subtopics.json (240/230/245/245/190/195/195 of 1540 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ProportionalityAndSimilarityTheoremsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the theorem and its figure
        title = Tex("Proportionality and Similarity").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        # Triangle ABC with DE parallel to BC
        apex = UP * 1.0 + LEFT * 3.0
        bl = DOWN * 2.2 + LEFT * 4.6
        br = DOWN * 2.2 + LEFT * 1.0
        side_ab = Line(apex, bl, color=WHITE, stroke_width=5)
        side_ac = Line(apex, br, color=WHITE, stroke_width=5)
        side_bc = Line(bl, br, color=WHITE, stroke_width=5)
        d_pt = apex + (bl - apex) * 0.45
        e_pt = apex + (br - apex) * 0.45
        de = Line(d_pt, e_pt, color=YELLOW, stroke_width=5)
        self.play(Create(side_ab), Create(side_ac), Create(side_bc))
        self.play(Create(de))
        self.wait(2)
        t1 = MathTex(r"DE \parallel BC \;\Rightarrow\; \frac{AD}{DB} = \frac{AE}{EC}").scale(1.05).shift(UP * 0.4 + RIGHT * 3.0)
        self.play(Write(t1))
        self.play(Create(SurroundingRectangle(t1, color=GREEN)))
        self.wait(2.5)
        t2 = Tex("Converse holds; midpoint theorem is the 1:1 case").scale(0.9).shift(DOWN * 3.0)
        self.play(Write(t2))
        self.wait(3)

        # --- Band 1 (subtopic_1): the area proof
        self.next_band(1)
        b1_title = Tex("The area proof").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Construct $BE$ and $CD$").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"\frac{[ADE]}{[BDE]} = \frac{AD}{DB} \qquad \frac{[ADE]}{[CED]} = \frac{AE}{EC}").scale(0.95).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex(r"$[BDE] = [CED]$: same base $DE$, apexes on a parallel line").scale(0.9).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = MathTex(r"\therefore \; \frac{AD}{DB} = \frac{AE}{EC}").scale(1.05).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): ratios in figures
        self.next_band(2)
        b2_title = Tex(r"$AD = 8$, $DB = 6$, $AE = 12$: find $EC$").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\frac{8}{6} = \frac{12}{EC}").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"8 \, EC = 72 \;\Rightarrow\; EC = 9").scale(1.05).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{Check wholes: } \frac{8}{14} = \frac{12}{21} = \frac{4}{7}").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("Never equate part-to-part with part-to-whole").scale(0.95).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): equiangular implies similar
        self.next_band(3)
        b3_title = Tex("Equiangular triangles are similar").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Mark $H$ on $AB$ with $AH = DE$; $K$ on $AC$ with $AK = DF$").scale(0.85).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"\triangle AHK \equiv \triangle DEF \; (\text{SAS})").scale(0.95).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex(r"$\hat{AHK} = \hat{B}$: corresponding, so $HK \parallel BC$").scale(0.9).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = MathTex(r"\frac{DE}{AB} = \frac{DF}{AC} = \frac{EF}{BC}").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the letter order
        self.next_band(4)
        b4_title = Tex("The order IS the pairing").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\triangle ABC \sim \triangle DEF: \; A \leftrightarrow D, \; B \leftrightarrow E, \; C \leftrightarrow F").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\frac{AB}{DE} = \frac{BC}{EF} = \frac{AC}{DF}").scale(1.05).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex("Match equal angles first, then write the vertices in that order").scale(0.9).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3))
        self.wait(3)

        # --- Band 5 (subtopic_4): Pythagoras by similarity
        self.next_band(5)
        b5_title = Tex(r"Right angle at $A$; altitude $AD$ to $BC$").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\triangle ABD \sim \triangle CBA: \text{ right angle } + \hat{B}").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\frac{AB}{CB} = \frac{BD}{BA} \;\Rightarrow\; AB^2 = BD \times BC").scale(0.95).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = MathTex(r"\text{Mirror side: } AC^2 = CD \times CB").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"AB^2 + AC^2 = BC(BD + DC) = BC^2").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the altitude relation
        self.next_band(6)
        b6_title = Tex("The altitude relation").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"AD^2 = BD \times DC").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = MathTex(r"BD = 9, \; DC = 16: \; AD^2 = 144 \Rightarrow AD = 12").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Each leg squared $=$ hypotenuse $\\times$ its own projection").scale(0.9).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the ladder against the wall
        self.next_band(7)
        b7_title = Tex("The ladder against the wall").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        # Ladder figure: wall, ground, ladder, one parallel ray
        lc = band_shift(7) + DOWN * 0.4 + LEFT * 2.8
        wall = Line(lc, lc + UP * 2.2, color=GREY, stroke_width=6)
        ground = Line(lc, lc + RIGHT * 3.4, color=GREY, stroke_width=6)
        ladder = Line(lc + UP * 2.2, lc + RIGHT * 3.4, color=WHITE, stroke_width=5)
        rung_pt = lc + UP * 2.2 + (lc + RIGHT * 3.4 - (lc + UP * 2.2)) * 0.25
        ray = Line(rung_pt, lc + RIGHT * 3.4 * 0.25 + (lc + RIGHT * 3.4 - (lc + RIGHT * 3.4 * 0.25)) * 0.0,
                   color=YELLOW, stroke_width=4)
        self.play(Create(wall), Create(ground))
        self.play(Create(ladder))
        self.play(Create(ray), FadeIn(Dot(rung_pt, color=YELLOW)))
        self.wait(2)
        b7_l1 = Tex("A quarter up the ladder,").scale(0.95).shift(band_shift(7) + UP * 0.9 + RIGHT * 3.2)
        b7_l2 = Tex("a quarter along the shadow").scale(0.95).shift(band_shift(7) + UP * 0.1 + RIGHT * 3.2)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Parallel rays play no favourites — that is the theorem").scale(0.9).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l3))
        self.wait(3)

        # --- Band 8 (subtopic_5): honest matching
        self.next_band(8)
        b8_title = Tex("Match like with like").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("Upper piece : lower piece $=$ upper shadow : lower shadow").scale(0.9).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_wrong = MathTex(r"\frac{8}{6} = \frac{12}{21}").scale(1.0).shift(band_shift(8) + UP * 0.0)
        self.play(Write(b8_wrong))
        self.play(Create(strike(b8_wrong)))
        self.wait(2)
        b8_l2 = Tex("part-to-part against part-to-whole — never").scale(0.9).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Name every length — part or whole — before the fraction").scale(0.9).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l3))
        self.wait(3)

        # --- Band 9 (subtopic_6): the photograph
        self.next_band(9)
        b9_title = Tex("The photograph and its enlargement").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Enlargement: angles untouched, sides share one factor").scale(0.9).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("For triangles, equal angles ALONE guarantee the factor").scale(0.9).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{Person } 1{,}8 \text{ m}, \text{ shadow } 2{,}4 \text{ m}; \text{ pole shadow } 8 \text{ m}").scale(0.9).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"\text{Pole} = \frac{1{,}8}{2{,}4} \times 8 = 6 \text{ m}").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the folded corner
        self.next_band(10)
        b10_title = Tex("The folded corner — Pythagoras rebuilt").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Fold the right angle flat onto the hypotenuse").scale(0.95).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Each small triangle is a photograph of the whole").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex("Leg$^2$ $=$ hypotenuse $\\times$ its own piece, twice over").scale(0.9).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("Add: the two pieces reassemble into the hypotenuse").scale(0.9).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.wait(3)

        # --- Band 11 (subtopic_7): the bonus at the crease
        self.next_band(11)
        b11_title = Tex("The bonus at the crease").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = MathTex(r"\text{fold}^2 = \text{piece} \times \text{piece}").scale(1.05).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"9 \times 16 = 144 \;\Rightarrow\; \text{fold} = 12").scale(1.05).shift(band_shift(11) + UP * 0.1)
        self.play(Write(b11_l2))
        self.play(Create(SurroundingRectangle(b11_l2, color=GREEN)))
        self.wait(2.5)
        b11_l3 = Tex("Surveyors used this to raise a true perpendicular").scale(0.95).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l3))
        self.wait(4)
