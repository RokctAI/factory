from manim import *

class QuadraticFactoring(Scene):
    def construct(self):
        # Subtopic: Review and Introduction
        title = Tex("Factoring Quadratic Equations").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Brief review: Expansion vs Factoring
        expansion_text = Tex(r"Expansion: $(x+1)(x+2) \rightarrow x^2 + 3x + 2$").shift(UP)
        factoring_text = Tex(r"Factoring: $x^2 + 3x + 2 \rightarrow (x+1)(x+2)$")
        self.play(Write(expansion_text))
        self.wait(3)
        self.play(Write(factoring_text))
        self.wait(4)
        self.play(FadeOut(expansion_text), FadeOut(factoring_text))

        # Standard form
        std_form_title = Tex("Standard Form:").shift(UP*1.5)
        std_form = MathTex("a", "x^2 + ", "b", "x + ", "c", " = 0")
        self.play(Write(std_form_title), Write(std_form))
        self.wait(3)
        self.play(FadeOut(std_form_title), FadeOut(std_form), FadeOut(title))

        # Subtopic: Standard Form and Identifying Coefficients
        eq_title = Tex("Example Problem:").to_edge(UP)
        eq = MathTex("2", "x^2 + ", "5", "x + ", "3", " = 0")
        self.play(Write(eq_title), Write(eq))
        self.wait(2)

        # Move equation up
        self.play(eq.animate.shift(UP * 2))

        # Identify a, b, c
        coef_a = MathTex("a = 2").shift(LEFT * 3)
        coef_b = MathTex("b = 5")
        coef_c = MathTex("c = 3").shift(RIGHT * 3)

        self.play(Write(coef_a), Write(coef_b), Write(coef_c))
        self.wait(3)

        # Target product and sum
        target_prod = MathTex(r"a \times c = 2 \times 3 = 6").shift(DOWN * 1.5 + LEFT * 2)
        target_sum = MathTex("b = 5").shift(DOWN * 1.5 + RIGHT * 2)

        self.play(Write(target_prod), Write(target_sum))
        self.wait(4)

        # Finding factors
        factors_text = Tex("Factors of 6:").shift(DOWN * 2.5)
        factors_1 = Tex("$1 \times 6 = 6$, $1 + 6 = 7$ (No)").shift(DOWN * 3)
        factors_2 = Tex("$2 \times 3 = 6$, $2 + 3 = 5$ (Yes!)").shift(DOWN * 3.5)

        self.play(Write(factors_text))
        self.wait(1)
        self.play(Write(factors_1))
        self.wait(2)
        self.play(Write(factors_2))
        self.wait(3)

        # Clear screen for next step, keeping original equation
        self.play(
            FadeOut(coef_a), FadeOut(coef_b), FadeOut(coef_c),
            FadeOut(target_prod), FadeOut(target_sum),
            FadeOut(factors_text), FadeOut(factors_1), FadeOut(factors_2)
        )

        # Subtopic: Factoring by Grouping
        # Rewrite equation splitting middle term
        eq_split = MathTex("2x^2 + ", "2x + 3x", " + 3 = 0").shift(UP)
        self.play(Transform(eq, eq_split))
        self.wait(3)

        # Grouping
        group_1 = MathTex("(2x^2 + 2x)", " + ").shift(LEFT * 1.5)
        group_2 = MathTex("(3x + 3)", " = 0").shift(RIGHT * 1.5)
        group_full = VGroup(group_1, group_2).shift(DOWN)

        self.play(Write(group_full))
        self.wait(3)

        # Factor out GCF from each group
        factor_1 = MathTex("2x", "(x + 1)", " + ").shift(LEFT * 1.5 + DOWN * 1.5)
        factor_2 = MathTex("3", "(x + 1)", " = 0").shift(RIGHT * 1.5 + DOWN * 1.5)
        factor_full = VGroup(factor_1, factor_2)

        self.play(Write(factor_full))
        self.wait(3)

        # Highlight common binomial
        self.play(factor_1[1].animate.set_color(YELLOW), factor_2[1].animate.set_color(YELLOW))
        self.wait(2)

        # Final factored form
        final_factored = MathTex("(x + 1)", "(2x + 3)", " = 0").shift(DOWN * 3)
        final_factored[0].set_color(YELLOW)
        self.play(Write(final_factored))
        self.wait(4)

        # Clear screen for next step
        self.play(
            FadeOut(eq), FadeOut(group_full), FadeOut(factor_full),
            final_factored.animate.shift(UP * 5)
        )

        # Subtopic: The Zero-Product Property
        zpp_title = Tex("Zero-Product Property").shift(UP * 0.5)
        self.play(Write(zpp_title))
        self.wait(3)

        # Setting up two equations
        eq1 = MathTex("x + 1 = 0").shift(LEFT * 3 + DOWN * 1.5)
        eq2 = MathTex("2x + 3 = 0").shift(RIGHT * 3 + DOWN * 1.5)

        self.play(Write(eq1), Write(eq2))
        self.wait(3)

        # Solving eq1
        sol1 = MathTex("x = -1").shift(LEFT * 3 + DOWN * 2.5)
        self.play(Write(sol1))
        self.wait(2)

        # Solving eq2
        step1_eq2 = MathTex("2x = -3").shift(RIGHT * 3 + DOWN * 2.5)
        sol2 = MathTex("x = -\\frac{3}{2}").shift(RIGHT * 3 + DOWN * 3.5)
        self.play(Write(step1_eq2))
        self.wait(2)
        self.play(Write(sol2))
        self.wait(3)

        # Highlight final answers
        box1 = SurroundingRectangle(sol1, color=GREEN)
        box2 = SurroundingRectangle(sol2, color=GREEN)
        self.play(Create(box1), Create(box2))
        self.wait(5)

        # Check step (optional visual, keep short)
        check_text = Tex(r"Check: $2(-1)^2 + 5(-1) + 3 = 2 - 5 + 3 = 0 \quad \checkmark$").shift(DOWN * 4.5)
        self.play(Write(check_text))
        self.wait(4)

        # End of scene
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)
