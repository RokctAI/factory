from manim import *

class QuadraticFactoringScene(Scene):
    def construct(self):
        # Setup title
        title = Text("Quadratic Equations: Factoring Method").to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Subtopic 1: The Architecture of the Quadratic Equation
        std_form = MathTex(r"ax^2 + bx + c = 0").shift(UP*1.5)
        self.play(Write(std_form))
        self.wait(3)

        example_eq = MathTex(r"2x^2 + 5x + 3 = 0").next_to(std_form, DOWN, buff=1)
        self.play(Write(example_eq))
        self.wait(3)

        coef_a = MathTex(r"a = 2")
        coef_b = MathTex(r"b = 5")
        coef_c = MathTex(r"c = 3")

        coefs = VGroup(coef_a, coef_b, coef_c).arrange(RIGHT, buff=1).next_to(example_eq, DOWN, buff=1)

        self.play(Write(coefs))
        self.wait(3)

        self.play(FadeOut(std_form), FadeOut(coefs))
        self.play(example_eq.animate.shift(UP*2.5))
        self.wait(1)

        # Subtopic 2: The AC Method
        ac_text = MathTex(r"ac = 2 \times 3 = 6")
        b_text = MathTex(r"b = 5")
        ac_group = VGroup(ac_text, b_text).arrange(DOWN, aligned_edge=LEFT).next_to(example_eq, DOWN, buff=0.5).align_to(example_eq, LEFT)

        self.play(Write(ac_group))
        self.wait(3)

        factors_text = Text("Factors of 6:").scale(0.8).next_to(ac_group, RIGHT, buff=1)
        self.play(Write(factors_text))

        factor_pairs_1 = MathTex(r"1, 6 \rightarrow 1 + 6 = 7 \neq 5").scale(0.8).next_to(factors_text, DOWN, aligned_edge=LEFT)
        self.play(Write(factor_pairs_1))
        self.wait(2)

        factor_pairs_2 = MathTex(r"2, 3 \rightarrow 2 + 3 = 5").scale(0.8).next_to(factor_pairs_1, DOWN, aligned_edge=LEFT)
        self.play(Write(factor_pairs_2))
        self.wait(3)

        split_eq = MathTex(r"2x^2 + 2x + 3x + 3 = 0").next_to(factor_pairs_2, DOWN, buff=1).align_to(example_eq, LEFT)
        self.play(Write(split_eq))
        self.wait(3)

        self.play(FadeOut(ac_group), FadeOut(factors_text), FadeOut(factor_pairs_1), FadeOut(factor_pairs_2), FadeOut(example_eq))
        self.play(split_eq.animate.shift(UP*3))
        self.wait(1)

        # Subtopic 3: Factorisation by Grouping
        group1 = MathTex(r"(2x^2 + 2x)").next_to(split_eq, DOWN, buff=0.5).align_to(split_eq, LEFT)
        group2 = MathTex(r"+ (3x + 3) = 0").next_to(group1, RIGHT)
        self.play(Write(group1), Write(group2))
        self.wait(3)

        factor_group1 = MathTex(r"2x(x + 1)").next_to(group1, DOWN, buff=0.5).align_to(group1, LEFT)
        self.play(Write(factor_group1))
        self.wait(2)

        factor_group2 = MathTex(r"+ 3(x + 1) = 0").next_to(factor_group1, RIGHT)
        self.play(Write(factor_group2))
        self.wait(3)

        common_factor = MathTex(r"(x + 1)(2x + 3) = 0").next_to(factor_group1, DOWN, buff=0.5).align_to(factor_group1, LEFT)
        self.play(Write(common_factor))
        self.wait(3)

        self.play(FadeOut(split_eq), FadeOut(group1), FadeOut(group2), FadeOut(factor_group1), FadeOut(factor_group2))
        self.play(common_factor.animate.shift(UP*3))
        self.wait(1)

        # Subtopic 4: The Zero Product Property
        case1 = MathTex(r"x + 1 = 0").next_to(common_factor, DOWN, buff=1).align_to(common_factor, LEFT)
        case2 = MathTex(r"2x + 3 = 0").next_to(case1, RIGHT, buff=2)

        self.play(Write(case1), Write(case2))
        self.wait(3)

        sol1 = MathTex(r"x = -1").next_to(case1, DOWN, buff=0.5)
        self.play(Write(sol1))
        self.wait(2)

        sol2_step = MathTex(r"2x = -3").next_to(case2, DOWN, buff=0.5)
        sol2 = MathTex(r"x = -\frac{3}{2}").next_to(sol2_step, DOWN, buff=0.5)

        self.play(Write(sol2_step))
        self.wait(2)
        self.play(Write(sol2))
        self.wait(3)

        final_box1 = SurroundingRectangle(sol1, color=YELLOW)
        final_box2 = SurroundingRectangle(sol2, color=YELLOW)
        self.play(Create(final_box1), Create(final_box2))
        self.wait(5)
