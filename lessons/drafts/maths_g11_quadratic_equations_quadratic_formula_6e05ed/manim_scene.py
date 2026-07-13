from manim import *

class QuadraticFormulaScene(Scene):
    def construct(self):
        # Subtopic 1: Limitations of Factorisation
        eq_standard = MathTex("a", "x^2", "+", "b", "x", "+", "c", "=", "0").scale(1.2)
        self.play(Write(eq_standard))
        self.wait(2)

        eq_example = MathTex("3", "x^2", "-", "2", "x", "-", "4", "=", "0").scale(1.2)
        self.play(Transform(eq_standard, eq_example))
        self.wait(2)

        # Subtopic 2: The Quadratic Formula
        self.play(eq_standard.animate.to_edge(UP))

        formula = MathTex("x", "=", "\\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}").scale(1.5)
        self.play(Write(formula))
        self.wait(3)

        # Subtopic 3: Applying the Formula
        self.play(formula.animate.shift(UP * 2))

        coeffs = MathTex("a = 3, \\quad b = -2, \\quad c = -4").scale(1.2)
        coeffs.next_to(formula, DOWN, buff=0.5)
        self.play(Write(coeffs))
        self.wait(2)

        sub_1 = MathTex("x", "=", "\\frac{-(-2) \\pm \\sqrt{(-2)^2 - 4(3)(-4)}}{2(3)}").scale(1.2)
        sub_1.next_to(coeffs, DOWN, buff=0.5)
        self.play(Write(sub_1))
        self.wait(2)

        sub_2 = MathTex("x", "=", "\\frac{2 \\pm \\sqrt{4 - (-48)}}{6}").scale(1.2)
        sub_2.move_to(sub_1)
        self.play(Transform(sub_1, sub_2))
        self.wait(2)

        sub_3 = MathTex("x", "=", "\\frac{2 \\pm \\sqrt{52}}{6}").scale(1.2)
        sub_3.move_to(sub_1)
        self.play(Transform(sub_1, sub_3))
        self.wait(2)

        sub_4 = MathTex("x", "=", "\\frac{2 \\pm 2\\sqrt{13}}{6}").scale(1.2)
        sub_4.move_to(sub_1)
        self.play(Transform(sub_1, sub_4))
        self.wait(2)

        sub_5 = MathTex("x", "=", "\\frac{2(1 \\pm \\sqrt{13})}{6}").scale(1.2)
        sub_5.move_to(sub_1)
        self.play(Transform(sub_1, sub_5))
        self.wait(2)

        sub_6 = MathTex("x", "=", "\\frac{1 \\pm \\sqrt{13}}{3}").scale(1.2)
        sub_6.move_to(sub_1)
        self.play(Transform(sub_1, sub_6))
        self.wait(3)

        final_solutions = MathTex("x = \\frac{1 + \\sqrt{13}}{3} \\quad \\text{or} \\quad x = \\frac{1 - \\sqrt{13}}{3}").scale(1.2)
        final_solutions.move_to(sub_1)
        self.play(Transform(sub_1, final_solutions))
        self.wait(4)
