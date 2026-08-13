from manim import *

# Band-layout whiteboard scene (reference: quadratics-by-factorisation).
# One band per teaching beat, add-only lifecycle, camera moves down between
# bands. Covers all seven subtopics: Part 1 Expert (the exponential function,
# the logarithm defined, the log graph, solving for the exponent) then
# Part 2 Simplifier (doubling on repeat, the question the log asks, mirror
# twins across the diagonal). Band dwell proportional to subtopics.json
# (220/240/230/240/190/200/210 of 1530 s). Curves drawn as short Line
# chains — exporter-supported primitives only.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ExponentialLogFunctionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): y = b^x and its three facts ---
        title = Tex("Exponential and Logarithmic Functions").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"y = b^x, \quad b > 0, \; b \neq 1").scale(1.2).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"2^0 = 1, \quad 2^3 = 8, \quad 2^{-2} = 0{,}25").scale(1.1).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"Always through $(0; 1)$; outputs always positive").scale(1.0).shift(DOWN * 0.8)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex(r"Horizontal asymptote: $y = 0$").scale(1.05).shift(DOWN * 1.7)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = MathTex(r"\text{Domain: } x \in \mathbb{R}, \quad \text{range: } y > 0").scale(1.05).shift(DOWN * 2.7)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the graph, and the base's direction ---
        self.next_band(1)
        b1_title = Tex("The base decides the direction").scale(1.15).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        og = band_shift(1) + DOWN * 1.7 + LEFT * 0.6
        ax_x = Arrow(og + LEFT * 2.4, og + RIGHT * 3.0, buff=0, stroke_width=3)
        ax_y = Arrow(og + DOWN * 0.4, og + UP * 3.4, buff=0, stroke_width=3)
        self.play(Create(ax_x), Create(ax_y))
        pts = [(-2.0, 0.25), (-1.0, 0.5), (0.0, 1.0), (1.0, 2.0), (2.0, 4.0), (2.8, 7.0)]
        world = [og + RIGHT * (x * 0.9) + UP * (y * 0.42) for x, y in pts]
        curve = VGroup(*[Line(world[i], world[i + 1], color=BLUE)
                         for i in range(len(world) - 1)])
        for seg in curve:
            self.play(Create(seg), run_time=0.4)
        d01 = Dot(og + UP * 0.42, radius=0.06, color=YELLOW)
        l01 = MathTex("(0; 1)").scale(0.7).move_to(og + UP * 0.42 + RIGHT * 0.75)
        self.play(Create(d01), Write(l01))
        self.wait(2)
        b1_l1 = Tex(r"$b > 1$: rises — each step right multiplies by $b$").scale(1.0).shift(band_shift(1) + UP * 1.6 + LEFT * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"0 < b < 1 \text{ falls: } \left(\tfrac{1}{2}\right)^x = 2^{-x}").scale(1.0).shift(band_shift(1) + DOWN * 3.2)
        self.play(Write(b1_l2))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the logarithm defined ---
        self.next_band(2)
        b2_title = Tex(r"2 to the WHAT gives 8? The log is the answer").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"y = \log_b x \iff x = b^y").scale(1.25).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = MathTex(r"\log_2 8 = 3, \quad \log_{10} 1000 = 3").scale(1.1).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\log_2 1 = 0 \text{ — log of 1 is 0 in every base}").scale(1.0).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("Two costumes, one fact — convert freely").scale(1.05).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): negative logs and the boundaries ---
        self.next_band(3)
        b3_title = Tex("Negative logs, and two boundaries").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\log_2 0{,}125 = -3 \; \text{ since } 2^{-3} = \tfrac{1}{8}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"\log_{1/2} 8 = -3 \; \text{ — a fractional base flips signs}").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{Base: } b > 0, \; b \neq 1. \quad \text{Input: } x > 0").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = MathTex(r"\log_2(-4): \; 2^y = -4 \text{ has no answer}").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.play(Create(strike(b3_l4)))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the log graph ---
        self.next_band(4)
        b4_title = Tex(r"$y = \log_b x$: the exponential reflected in $y = x$").scale(1.0).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_title))
        self.wait(1.5)
        og4 = band_shift(4) + DOWN * 0.6 + LEFT * 2.3
        ax4_x = Arrow(og4 + LEFT * 0.5, og4 + RIGHT * 5.2, buff=0, stroke_width=3)
        ax4_y = Arrow(og4 + DOWN * 1.7, og4 + UP * 2.3, buff=0, stroke_width=3)
        wall = DashedLine(og4 + DOWN * 1.6, og4 + UP * 2.1, color=YELLOW)
        self.play(Create(ax4_x), Create(ax4_y))
        self.play(Create(wall))
        lpts = [(0.25, -2.0), (0.5, -1.0), (1.0, 0.0), (2.0, 1.0), (4.0, 2.0), (8.0, 3.0)]
        world4 = [og4 + RIGHT * (x * 0.55) + UP * (y * 0.5) for x, y in lpts]
        for i in range(len(world4) - 1):
            self.play(Create(Line(world4[i], world4[i + 1], color=BLUE)), run_time=0.4)
        a10 = Dot(og4 + RIGHT * 0.55, radius=0.06, color=YELLOW)
        l10 = MathTex("(1; 0)").scale(0.7).move_to(og4 + RIGHT * 0.85 + DOWN * 0.35)
        l83 = MathTex("(8; 3)").scale(0.7).move_to(world4[-1] + UP * 0.35)
        self.play(Create(a10), Write(l10), Write(l83))
        self.wait(2)
        b4_l1 = MathTex(r"\text{Domain: } x > 0, \quad \text{range: } y \in \mathbb{R}").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("Never touches the $y$ axis — the classic lost mark").scale(0.95).shift(band_shift(4) + UP * 1.6 + RIGHT * 1.8)
        self.play(Write(b4_l2))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): solving for the exponent ---
        self.next_band(5)
        b5_title = Tex("The unknown in the exponent").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"5 \cdot 2^x = 80: \; 2^x = 2^4, \; x = 4").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2.5)
        b5_l2 = MathTex(r"3^x = 20: \; x = \log_3 20 = \frac{\log 20}{\log 3}").scale(1.05).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"x = 2{,}73").scale(1.15).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = MathTex(r"\text{Sanity: } 3^2 = 9 < 20 < 27 = 3^3 \;\checkmark").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the log IS the inverse ---
        self.next_band(6)
        b6_title = Tex("The log IS the inverse of the exponential").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"y = 3^x \xrightarrow{\text{swap}} x = 3^y").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"\Rightarrow y = \log_3 x").scale(1.15).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex("Mirrored across $y = x$ — the graphs confirm it").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"1{,}08^n = 2: \; n = \tfrac{\log 2}{\log 1{,}08} \approx 9{,}01").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): doubling on repeat ---
        self.next_band(7)
        b7_title = Tex("Doubling on repeat").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"\text{Chain: } 1, 2, 4, 8 \to 2^x \text{ after } x \text{ h}").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex(r"Hour 0: one person — through $(0; 1)$").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"Backwards: $\tfrac{1}{2}, \tfrac{1}{4}, \tfrac{1}{8}$ — never zero").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex(r"Cooling tea: base $\tfrac{1}{2}$ — same shape, falling").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Start at one, hug the floor, never touch it").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): the question the log asks ---
        self.next_band(8)
        b8_title = Tex("The log asks: how many steps?").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\log_2 8 = 3: \text{ hours until 8 people}").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\log_2 32 = 5, \quad \log_{10} 1000 = 3, \quad \log_2 1 = 0").scale(1.0).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"\log_2 0{,}25 = -2 \text{ — two steps in reverse}").scale(1.0).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("No steps reach zero or negative — refuse the question").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): mirror twins across the diagonal ---
        self.next_band(9)
        b9_title = Tex("Mirror twins across the diagonal").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("3 h, 8 people $\\leftrightarrow$ 8 people, 3 h").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"(0; 1) \to (1; 0), \quad \text{floor } y = 0 \to \text{wall } x = 0").scale(1.0).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Domain and range trade places across the mirror").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"\text{Sketch: } (1; 0), \; (2; 1), \; (8; 3), \text{ dash the wall}").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("The wall is never touched — strictly right of the $y$ axis").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.wait(4)
