from manim import *

# Band-layout whiteboard scene (see AUTHORING-SPEC / quadratics-by-factorisation
# worked example). One band per teaching beat, camera moves down, nothing is
# ever removed. Covers all seven subtopics of the session duo:
# Part 1 — Expert (subtopics 1-4), Part 2 — Simplifier (subtopics 5-7),
# band time apportioned to subtopics.json (210/240/220/260/190/190/210 of 1520 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FormalDefinitionAndInversesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the formal definition
        title = Tex("Functions and Their Inverses").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("A function: every input has exactly one output").scale(1.1).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2.5)
        d2 = MathTex(r"y = 2x + 3: \quad 1 \Rightarrow 5 \text{ only}").scale(1.15).shift(DOWN * 0.1)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"y^2 = x: \quad 9 \Rightarrow 3 \text{ or } -3").scale(1.15).shift(DOWN * 1.1)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex("Two outputs — not a function").scale(1.1).shift(DOWN * 2.1)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): vertical line test, many-to-one is legal
        self.next_band(1)
        b1_title = Tex("The vertical line test").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        # Sideways parabola (opens right) as a short polyline chain
        c = band_shift(1) + UP * 0.6 + LEFT * 2.0
        arm_top = VGroup(
            Line(c, c + RIGHT * 0.5 + UP * 1.0, stroke_width=5),
            Line(c + RIGHT * 0.5 + UP * 1.0, c + RIGHT * 1.6 + UP * 1.7, stroke_width=5),
        )
        arm_bot = VGroup(
            Line(c, c + RIGHT * 0.5 + DOWN * 1.0, stroke_width=5),
            Line(c + RIGHT * 0.5 + DOWN * 1.0, c + RIGHT * 1.6 + DOWN * 1.7, stroke_width=5),
        )
        self.play(Create(arm_top), Create(arm_bot))
        self.wait(1.5)
        vline = Line(c + RIGHT * 1.0 + UP * 2.2, c + RIGHT * 1.0 + DOWN * 2.2,
                     color=YELLOW, stroke_width=4)
        p1 = Dot(c + RIGHT * 1.0 + UP * 1.32, color=RED)
        p2 = Dot(c + RIGHT * 1.0 + DOWN * 1.32, color=RED)
        self.play(Create(vline))
        self.play(FadeIn(p1), FadeIn(p2))
        self.wait(1.5)
        b1_l1 = Tex("Cut twice — fails the test").scale(1.1).shift(band_shift(1) + RIGHT * 2.9 + UP * 0.6)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"y = x^2: \;\; 3 \Rightarrow 9, \;\; -3 \Rightarrow 9").scale(1.05).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Many-to-one is legal; one-to-many is not").scale(1.1).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l3))
        self.wait(3)

        # --- Band 2 (subtopic_2): the swap-and-solve routine
        self.next_band(2)
        b2_title = Tex(r"The inverse: swap $x$ and $y$, solve for $y$").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"y = 2x + 3").scale(1.15).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{Swap: } x = 2y + 3").scale(1.15).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"2y = x - 3").scale(1.15).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"y = \frac{x - 3}{2}").scale(1.15).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex(r"Check: $1 \Rightarrow 5$, inverse $5 \Rightarrow 1$").scale(1.05).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): any straight line, gradient flips, notation
        self.next_band(3)
        b3_title = Tex(r"Inverse of $y = 3x - 6$").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Swap: } x = 3y - 6").scale(1.15).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"y = \frac{x + 6}{3} = \tfrac{1}{3}x + 2").scale(1.15).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex(r"Gradient 3 becomes gradient $\tfrac{1}{3}$").scale(1.1).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = MathTex(r"f^{-1}(x) \text{ is a label, NOT } \frac{1}{f(x)}").scale(1.1).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): reflection in the line y = x
        self.next_band(4)
        b4_title = Tex(r"The mirror: reflection in $y = x$").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"(1;\, 5) \Rightarrow (5;\, 1)").scale(1.15).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        # Mini diagram: the diagonal mirror and one reflected pair of points
        m = band_shift(4) + DOWN * 0.9
        mirror = Line(m + DL * 1.6, m + UR * 1.6, color=YELLOW, stroke_width=4)
        mlabel = MathTex(r"y = x").scale(0.9).shift(m + UR * 1.6 + RIGHT * 0.8)
        pa = Dot(m + LEFT * 1.3 + UP * 1.0, color=BLUE)
        pb = Dot(m + RIGHT * 1.0 + DOWN * 1.3, color=RED)
        link = DashedLine(pa.get_center(), pb.get_center(), stroke_width=3)
        self.play(Create(mirror), Write(mlabel))
        self.wait(1.5)
        self.play(FadeIn(pa))
        self.play(Create(link), FadeIn(pb))
        self.wait(2)
        b4_l2 = Tex("The inverse graph is the mirror image").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l2))
        self.wait(3)

        # --- Band 5 (subtopic_3): sketch via swapped intercepts, domain-range trade
        self.next_band(5)
        b5_title = Tex(r"Sketch the inverse of $y = 3x - 6$").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"(0;\, -6) \Rightarrow (-6;\, 0)").scale(1.1).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"(2;\, 0) \Rightarrow (0;\, 2)").scale(1.1).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Intercepts trade jobs under reflection").scale(1.1).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("Domain and range trade places:").scale(1.1).shift(band_shift(5) + DOWN * 1.7)
        b5_l5 = MathTex(r"\text{range } y > 0 \;\Rightarrow\; \text{domain } x > 0").scale(1.05).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the trap — inverse of y = x^2
        self.next_band(6)
        b6_title = Tex(r"The trap: inverse of $y = x^2$").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Swap: } x = y^2").scale(1.15).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"y = \pm\sqrt{x}").scale(1.15).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Two outputs — NOT a function").scale(1.1).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Horizontal line test on the original:").scale(1.05).shift(band_shift(6) + DOWN * 1.9)
        b6_l5 = Tex("cuts once only — then the inverse is a function").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the repair — restrict the domain
        self.next_band(7)
        b7_title = Tex("The repair: restrict the domain").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"x \geq 0: \quad f^{-1}(x) = \sqrt{x}").scale(1.15).shift(band_shift(7) + UP * 1.0)
        b7_l2 = MathTex(r"x \leq 0: \quad f^{-1}(x) = -\sqrt{x}").scale(1.15).shift(band_shift(7))
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("One arm of the parabola at a time — one-to-one").scale(1.05).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3))
        self.wait(3)

        # --- Band 8 (subtopic_4): worked case with a coefficient
        self.next_band(8)
        b8_title = Tex(r"Inverse of $y = 2x^2$, domain $x \leq 0$").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\text{Swap: } x = 2y^2").scale(1.1).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"y^2 = \frac{x}{2} \;\Rightarrow\; y = \pm\sqrt{\tfrac{x}{2}}").scale(1.1).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex(r"Old domain $x \leq 0$ becomes the range: choose minus").scale(1.0).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = MathTex(r"f^{-1}(x) = -\sqrt{\tfrac{x}{2}}").scale(1.15).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = MathTex(r"\text{Check: } -2 \Rightarrow 8, \quad -\sqrt{4} = -2").scale(1.05).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): one ticket, one prize
        self.next_band(9)
        b9_title = Tex("One ticket, one prize").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Vending machine: one code in, one snack out").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"y^2 = x: \; \text{code } 9 \text{ drops } 3 \text{ and } -3").scale(1.05).shift(band_shift(9) + UP * 0.1)
        b9_l3 = Tex("A broken machine — not a function").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"y = x^2: \; 3 \Rightarrow 9 \text{ and } -3 \Rightarrow 9").scale(1.05).shift(band_shift(9) + DOWN * 1.8)
        b9_l5 = Tex("Still working: one snack per press").scale(1.05).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_6): running the machine backwards
        self.next_band(10)
        b10_title = Tex("Running the machine backwards").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"y = 2x + 3 \;\Rightarrow\; \text{swap: } x = 2y + 3").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"y = \frac{x - 3}{2}").scale(1.15).shift(band_shift(10) + UP * 0.0)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex("Opposite operations, opposite order:").scale(1.05).shift(band_shift(10) + DOWN * 1.1)
        b10_l4 = Tex(r"$\times 2$ then $+3$ undone by $-3$ then $\div 2$").scale(1.05).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = MathTex(r"\text{Trial: } 5 \Rightarrow \frac{5 - 3}{2} = 1").scale(1.05).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_7): the mirror and the machine that shrugs
        self.next_band(11)
        b11_title = Tex("The mirror and the machine that shrugs").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex(r"Reflect in $y = x$: $(1;\, 5)$ becomes $(5;\, 1)$").scale(1.05).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = Tex(r"Snack 9: code 3 or $-3$? The machine shrugs").scale(1.05).shift(band_shift(11) + UP * 0.1)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = Tex("Fix: unplug half the machine").scale(1.05).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l3))
        self.wait(2)
        b11_l4 = MathTex(r"x \geq 0 \Rightarrow y = \sqrt{x}").scale(1.1).shift(band_shift(11) + DOWN * 1.8)
        b11_l5 = MathTex(r"x \leq 0 \Rightarrow y = -\sqrt{x}").scale(1.1).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11_l4))
        self.wait(2)
        self.play(Write(b11_l5))
        self.play(Create(SurroundingRectangle(b11_l5, color=GREEN)))
        self.wait(4)
