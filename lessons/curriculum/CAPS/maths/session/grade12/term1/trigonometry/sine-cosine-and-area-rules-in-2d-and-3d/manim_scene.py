from manim import *

# Band-layout whiteboard scene (see AUTHORING-SPEC / quadratics-by-factorisation
# worked example). One band per teaching beat, camera moves down, nothing is
# ever removed. Covers all seven subtopics of the session duo:
# Part 1 — Expert (subtopics 1-4), Part 2 — Simplifier (subtopics 5-7),
# band time apportioned to subtopics.json (220/230/250/260/190/200/220 of 1570 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SineCosineAndAreaRulesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the labelling convention
        title = Tex("Sine, Cosine and Area Rules").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        # Triangle ABC: A apex, B bottom-left, C bottom-right
        pA = UP * 1.0
        pB = DOWN * 1.2 + LEFT * 2.2
        pC = DOWN * 1.2 + RIGHT * 2.2
        tri = VGroup(Line(pA, pB, stroke_width=5), Line(pB, pC, stroke_width=5),
                     Line(pC, pA, stroke_width=5))
        self.play(Create(tri))
        lA = MathTex(r"A").scale(1.0).move_to(pA + UP * 0.4)
        lB = MathTex(r"B").scale(1.0).move_to(pB + DL * 0.35)
        lC = MathTex(r"C").scale(1.0).move_to(pC + DR * 0.35)
        la = MathTex(r"a").scale(1.0).move_to(DOWN * 1.6)
        lb = MathTex(r"b").scale(1.0).move_to((pA + pC) / 2 + UR * 0.35)
        lc = MathTex(r"c").scale(1.0).move_to((pA + pB) / 2 + UL * 0.35)
        self.play(Write(lA), Write(lB), Write(lC))
        self.wait(1.5)
        self.play(Write(la), Write(lb), Write(lc))
        self.wait(2)
        d1 = Tex("Side $a$ lies OPPOSITE angle $A$").scale(1.05).shift(DOWN * 2.5)
        self.play(Write(d1))
        self.wait(3)

        # --- Band 1 (subtopic_1): the three rules and the stocktake
        self.next_band(1)
        b1_title = Tex("The three rules — count your data").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}").scale(1.05).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Sine rule: a complete pair $+$ one more piece").scale(0.95).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"a^2 = b^2 + c^2 - 2bc\cos A").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Cosine rule: two sides $+$ included angle, or 3 sides").scale(0.9).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = MathTex(r"\text{Area} = \tfrac{1}{2}ab\sin C \;\; \text{(included angle)}").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the sine rule at work
        self.next_band(2)
        b2_title = Tex(r"$A = 40^\circ$, $B = 60^\circ$, $a = 10$: find $b$").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\frac{b}{\sin B} = \frac{a}{\sin A}").scale(1.05).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"b = \frac{10 \sin 60^\circ}{\sin 40^\circ}").scale(1.05).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"b = 13{,}47 \text{ units}").scale(1.1).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex(r"Sanity: $B > A$, so $b > 10$ $\checkmark$").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = MathTex(r"C = 180^\circ - 40^\circ - 60^\circ = 80^\circ \text{ (free)}").scale(0.9).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the ambiguous case
        self.next_band(3)
        b3_title = Tex("Finding an ANGLE with the sine rule").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("The calculator returns the acute answer only").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex("But sine is also positive in quadrant II").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"\theta \quad \text{or} \quad 180^\circ - \theta").scale(1.15).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex(r"Keep the obtuse option if it fits under $180^\circ$").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): cosine rule job one — the third side
        self.next_band(4)
        b4_title = Tex(r"Sides 7 and 9, included angle $60^\circ$").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"a^2 = 7^2 + 9^2 - 2(7)(9)\cos 60^\circ").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"= 49 + 81 - 126 \times \tfrac{1}{2} = 130 - 63").scale(1.05).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"a^2 = 67 \;\Rightarrow\; a = \sqrt{67} \approx 8{,}19").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex(r"Pythagoras plus a correction — at $90^\circ$").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        b4_l5 = Tex("the cosine is zero and the correction vanishes").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): job two — an angle from three sides; area
        self.next_band(5)
        b5_title = Tex(r"Sides 5, 7, 8: angle opposite the 5").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\cos A = \frac{b^2 + c^2 - a^2}{2bc}").scale(1.05).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\cos A = \frac{49 + 64 - 25}{2(7)(8)} = \frac{88}{112} = \frac{11}{14}").scale(0.95).shift(band_shift(5) + DOWN * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"A = 38{,}21^\circ").scale(1.1).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex("A negative cosine announces an obtuse angle").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = MathTex(r"\text{Area} = \tfrac{1}{2}(7)(9)\sin 60^\circ \approx 27{,}28").scale(1.0).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): 3D step one — the ground triangle
        self.next_band(6)
        b6_title = Tex("3D: solve the ground triangle first").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        # Ground triangle: B left, C right, A apex (tower base)
        gB = band_shift(6) + DOWN * 0.1 + LEFT * 2.4
        gC = band_shift(6) + DOWN * 0.1 + RIGHT * 2.4
        gA = band_shift(6) + UP * 1.4
        gtri = VGroup(Line(gB, gC, stroke_width=5), Line(gB, gA, stroke_width=5),
                      Line(gC, gA, stroke_width=5))
        self.play(Create(gtri))
        g1 = MathTex(r"A").scale(0.9).move_to(gA + UP * 0.35)
        g2 = MathTex(r"70^\circ").scale(0.8).move_to(gB + RIGHT * 0.75 + UP * 0.25)
        g3 = MathTex(r"50^\circ").scale(0.8).move_to(gC + LEFT * 0.75 + UP * 0.25)
        g4 = MathTex(r"100 \text{ m}").scale(0.8).move_to(band_shift(6) + DOWN * 0.5)
        self.play(Write(g1), Write(g2), Write(g3), Write(g4))
        self.wait(2.5)
        b6_l1 = MathTex(r"\hat{A} = 180^\circ - 70^\circ - 50^\circ = 60^\circ").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"AB = \frac{100\sin 50^\circ}{\sin 60^\circ} = 88{,}46 \text{ m}").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): 3D step two — the vertical triangle
        self.next_band(7)
        b7_title = Tex("Cross the bridge into the vertical triangle").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        # Vertical triangle: right angle at base of tower
        vB = band_shift(7) + DOWN * 0.4 + LEFT * 2.4
        vA = band_shift(7) + DOWN * 0.4 + RIGHT * 1.6
        vT = band_shift(7) + UP * 1.3 + RIGHT * 1.6
        vtri = VGroup(Line(vB, vA, stroke_width=5), Line(vA, vT, stroke_width=5),
                      Line(vB, vT, stroke_width=5))
        self.play(Create(vtri))
        v1 = MathTex(r"25^\circ").scale(0.8).move_to(vB + RIGHT * 1.0 + UP * 0.28)
        v2 = MathTex(r"88{,}46").scale(0.8).move_to(band_shift(7) + DOWN * 0.8 + LEFT * 0.4)
        v3 = MathTex(r"h").scale(0.9).move_to(vA + UP * 0.85 + RIGHT * 0.35)
        rt = Square(side_length=0.28, stroke_width=3).move_to(vA + UP * 0.14 + LEFT * 0.14)
        self.play(Write(v1), Write(v2), Write(v3), Create(rt))
        self.wait(2.5)
        b7_l1 = MathTex(r"h = 88{,}46 \tan 25^\circ").scale(1.05).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"h = 41{,}25 \text{ m}").scale(1.1).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): which tool comes out of the box
        self.next_band(8)
        b8_title = Tex("Which tool comes out of the box").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Sine rule: the matching-pairs tool").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Cosine rule: the wedge tool — sides and hinge").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Area rule: the paint estimate — $\tfrac{1}{2}ab\sin C$").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Little $a$ always faces capital $A$ across the room").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        b8_l5 = Tex("— mispair them and every rule misfires").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the field you cannot walk across
        self.next_band(9)
        b9_title = Tex("A field you cannot walk across").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Fences 7 and 9 from one post, opening $60^\circ$").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"x^2 = 49 + 81 - 63 = 67").scale(1.05).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"x = \sqrt{67} \approx 8{,}19 \text{ units}").scale(1.05).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex(r"At $90^\circ$ the hinge gives pure Pythagoras;").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        b9_l5 = Tex("narrower shortens, wider stretches the far side").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the flagpole — two pages, one spine
        self.next_band(10)
        b10_title = Tex("The flagpole and its two triangles").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("No 3D triangles — two flat pages of an open book").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Lying page: the ground data; standing page: the height").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("The spine they share: $AB$, base distance to the pole").scale(0.95).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("Solve the data-rich page FIRST").scale(1.05).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.wait(3)

        # --- Band 11 (subtopic_7): the flagpole solved
        self.next_band(11)
        b11_title = Tex("Carry the spine up").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = MathTex(r"AB = \frac{100\sin 50^\circ}{\sin 60^\circ} = 88{,}46").scale(1.0).shift(band_shift(11) + UP * 1.0)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"\text{Standing page: } h = 88{,}46\tan 25^\circ").scale(1.0).shift(band_shift(11) + UP * 0.0)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = MathTex(r"h = 41{,}25 \text{ m}").scale(1.1).shift(band_shift(11) + DOWN * 1.0)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2.5)
        b11_l4 = Tex("Spine, data page, answer page — every time").scale(1.0).shift(band_shift(11) + DOWN * 2.0)
        self.play(Write(b11_l4))
        self.wait(4)
