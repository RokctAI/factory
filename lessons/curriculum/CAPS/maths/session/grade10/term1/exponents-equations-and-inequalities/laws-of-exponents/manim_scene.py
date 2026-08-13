from manim import *

# Band-layout whiteboard scene (see lessons/scripts/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing removed.
# Write-only reveals on single-string Tex/MathTex keep the export clean. Bands
# cover all seven subtopics (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# dwell time proportional to subtopics.json (220/240/220/260/170/170/170 of
# 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LawsOfExponentsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the four laws
        title = Tex("Laws of Exponents").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"x^3 \times x^2 = x^5 \quad \text{(same base: add)}").scale(1.05).shift(UP * 0.9)
        l2 = MathTex(r"\frac{x^5}{x^2} = x^3 \quad \text{(same base: subtract)}").scale(1.05).shift(DOWN * 0.1)
        l3 = MathTex(r"(x^3)^2 = x^6 \quad \text{(power on power: multiply)}").scale(1.05).shift(DOWN * 1.2)
        l4 = MathTex(r"(2x)^2 = 4x^2 \quad \text{(EVERY factor squared)}").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(l1))
        self.wait(2)
        self.play(Write(l2))
        self.wait(2)
        self.play(Write(l3))
        self.wait(2)
        self.play(Write(l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): zero and negative exponents
        self.next_band(1)
        b1_title = Tex("Two special definitions").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\frac{x^3}{x^3} = 1 = x^{3-3} = x^0").scale(1.1).shift(band_shift(1) + UP * 1.0)
        b1_l2 = MathTex(r"x^0 = 1 \quad (x \neq 0)").scale(1.15).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = MathTex(r"x^{-2} = \frac{1}{x^2}").scale(1.15).shift(band_shift(1) + DOWN * 1.2)
        b1_l4 = Tex(r"A position instruction, not a negative number").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the expression — bracket first
        self.next_band(2)
        b2_title = Tex(r"Simplify: $\frac{(2x^3y)^2 \times 4x^{-2}}{8xy^2}$").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"(2x^3y)^2 = 4x^6y^2").scale(1.1).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"4x^6y^2 \times 4x^{-2} = 16x^4y^2").scale(1.1).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\frac{16x^4y^2}{8xy^2} = 2 \, x^{4-1} \, y^{2-2}").scale(1.05).shift(band_shift(2) + DOWN * 1.1)
        b2_l4 = MathTex(r"= 2x^3").scale(1.2).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): the number test
        self.next_band(3)
        b3_title = Tex(r"Check with $x = 1, \; y = 1$").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Original: } \frac{2^2 \times 4}{8} = \frac{16}{8} = 2").scale(1.1).shift(band_shift(3) + UP * 1.0)
        b3_l2 = MathTex(r"\text{Answer: } 2(1)^3 = 2 \;\checkmark").scale(1.1).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("One law per line — slow is smooth,").scale(1.05).shift(band_shift(3) + DOWN * 1.1)
        b3_l4 = Tex("and smooth earns full marks").scale(1.05).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the exponential equation
        self.next_band(4)
        b4_title = Tex(r"Solve: $3^{x+1} = 27$").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"27 = 3^3").scale(1.1).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"3^{x+1} = 3^3").scale(1.15).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"x + 1 = 3").scale(1.15).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"x = 2").scale(1.2).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        b4_l5 = MathTex(r"\text{Check: } 3^{2+1} = 27 \;\checkmark").scale(1.05).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the variations
        self.next_band(5)
        b5_title = Tex("Same move, different costume").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"3^{x+1} = 1 = 3^0 \;\Rightarrow\; x = -1").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"3^{x+1} = \tfrac{1}{27} = 3^{-3} \;\Rightarrow\; x = -4").scale(1.05).shift(band_shift(5) + UP * 0.1)
        b5_l3 = MathTex(r"5^{x+1} = 125 = 5^3 \;\Rightarrow\; x = 2").scale(1.05).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_wrong = MathTex(r"\div 3: \;\; x + 1 = 9").scale(1.05).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        b5_rule = Tex("The safe road is the base-matching road").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_rule))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the error museum
        self.next_band(6)
        b6_title = Tex("The error museum").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_e1 = MathTex(r"(2x^3y)^2 = 2x^6y^2").scale(1.0).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_e1))
        self.play(Create(strike(b6_e1)))
        self.wait(1.5)
        b6_e2 = MathTex(r"x^2 \times y^3 = xy^5").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_e2))
        self.play(Create(strike(b6_e2)))
        self.wait(1.5)
        b6_e3 = MathTex(r"4x^{-2} = -4x^2").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_e3))
        self.play(Create(strike(b6_e3)))
        b6_e3c = MathTex(r"4x^{-2} = \frac{4}{x^2}").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_e3c))
        self.wait(1.5)
        b6_e4 = MathTex(r"3^{x+1} = 3(x+1)").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_e4))
        self.play(Create(strike(b6_e4)))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): exponents just count
        self.next_band(7)
        b7_title = Tex("Exponents just count how many times").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"x^3 \times x^2: \; 3 + 2 = 5 \text{ bodies} \;\Rightarrow\; x^5").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\frac{x^5}{x^2}: \text{ cancel 1-for-1} \Rightarrow x^3").scale(1.0).shift(band_shift(7) + UP * 0.0)
        b7_l3 = MathTex(r"(x^3)^2: \text{ repeat the pile} \Rightarrow x^6").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = MathTex(r"x^0 = 1, \qquad x^{-3} = \frac{1}{x^3}").scale(1.05).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l4))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): everyone in the taxi pays
        self.next_band(8)
        b8_title = Tex("Everyone in the taxi pays the fare").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"(2x^3y)^2: \text{ all three passengers squared}").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"= 4x^6y^2").scale(1.1).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex(r"Sort the washing: numbers, $x$'s, $y$'s").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = MathTex(r"\frac{16x^4y^2}{8xy^2} = 2x^3").scale(1.1).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        b8_l5 = Tex(r"Check at $x=1, y=1$: both give 2").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): same language on both sides
        self.next_band(9)
        b9_title = Tex("Speak both sides in the same language").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"3^{x+1} = 27 \;\Rightarrow\; 3^{x+1} = 3^3").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"x + 1 = 3 \;\Rightarrow\; x = 2").scale(1.1).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2)
        b9_l3 = MathTex(r"= 1? \; 3^0. \quad = \tfrac{1}{27}? \; 3^{-3}. \quad 125? \; 5^3").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_wrong = MathTex(r"3^{x+1} = 3(x+1)").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_wrong))
        self.play(Create(strike(b9_wrong)))
        b9_l4 = Tex("The counter counts multiplications — it never multiplies").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l4))
        self.wait(4)
