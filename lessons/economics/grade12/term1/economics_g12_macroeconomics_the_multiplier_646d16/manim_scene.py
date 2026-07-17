from manim import *

class MultiplierLesson(Scene):
    def construct(self):
        # Subtopic 1: Introduction and Definition of the Multiplier
        title = Text("The Multiplier Effect", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        definition = Text(
            "An initial injection leads to a proportionately\nlarger final change in national income.",
            font_size=32
        )
        self.play(FadeIn(definition))
        self.wait(2)

        injection = Text("Injection (J)", color=GREEN).move_to(LEFT * 4)
        arrow = Arrow(start=LEFT * 2, end=RIGHT * 2, color=YELLOW)
        national_income = Text("National Income (Y)", color=ORANGE).move_to(RIGHT * 4)

        self.play(FadeOut(definition))
        self.play(Write(injection))
        self.play(GrowArrow(arrow))
        self.play(Write(national_income))
        self.wait(2)

        larger_arrow = Arrow(start=RIGHT * 4 + DOWN * 0.5, end=RIGHT * 4 + UP * 2, color=ORANGE, stroke_width=8)
        self.play(GrowArrow(larger_arrow))
        self.wait(2)

        self.play(FadeOut(injection, arrow, national_income, larger_arrow))

        # Subtopic 2: The Multiplier Formula and Marginal Propensities
        mpc_def = Text("Marginal Propensity to Consume (MPC)", font_size=36, color=YELLOW)
        self.play(Write(mpc_def))
        self.wait(1)
        self.play(mpc_def.animate.to_edge(UP).shift(DOWN))

        formula_k = MathTex(r"k = \frac{1}{1 - MPC}", font_size=60)
        self.play(Write(formula_k))
        self.wait(2)

        formula_mps = MathTex(r"k = \frac{1}{MPS}", font_size=60).next_to(formula_k, DOWN * 2)
        self.play(Write(formula_mps))
        self.wait(2)

        self.play(FadeOut(mpc_def, formula_k, formula_mps, title))

        # Subtopic 3: Working the Example Problem - Calculating the Multiplier
        problem_title = Text("Example Problem", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(problem_title))

        given_mpc = MathTex(r"MPC = 0,75", font_size=48).shift(UP * 2)
        given_inj = MathTex(r"\Delta J = \text{R}100\text{ million}", font_size=48).next_to(given_mpc, DOWN)

        self.play(Write(given_mpc))
        self.play(Write(given_inj))
        self.wait(2)

        calc_step1 = MathTex(r"k = \frac{1}{1 - MPC}", font_size=48).next_to(given_inj, DOWN * 1.5)
        self.play(Write(calc_step1))
        self.wait(1)

        calc_step2 = MathTex(r"k = \frac{1}{1 - 0,75}", font_size=48).next_to(given_inj, DOWN * 1.5)
        self.play(Transform(calc_step1, calc_step2))
        self.wait(1)

        calc_step3 = MathTex(r"k = \frac{1}{0,25}", font_size=48).next_to(given_inj, DOWN * 1.5)
        self.play(Transform(calc_step1, calc_step3))
        self.wait(1)

        calc_step4 = MathTex(r"k = 4", font_size=48, color=GREEN).next_to(given_inj, DOWN * 1.5)
        self.play(Transform(calc_step1, calc_step4))
        self.wait(2)

        self.play(FadeOut(given_mpc, given_inj, calc_step1, problem_title))

        # Subtopic 4: Total Change in National Income and Summary
        final_calc_title = Text("Total Change in National Income", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(final_calc_title))

        formula_dy = MathTex(r"\Delta Y = k \times \Delta J", font_size=48).shift(UP * 1.5)
        self.play(Write(formula_dy))
        self.wait(2)

        sub_dy = MathTex(r"\Delta Y = 4 \times 100", font_size=48).next_to(formula_dy, DOWN)
        self.play(Write(sub_dy))
        self.wait(1)

        final_answer = MathTex(r"\Delta Y = \text{R}400\text{ million}", font_size=60, color=GREEN).next_to(sub_dy, DOWN * 1.5)
        self.play(Write(final_answer))
        self.wait(3)

        box = SurroundingRectangle(final_answer, color=YELLOW, buff=0.2)
        self.play(Create(box))
        self.wait(2)

        self.play(FadeOut(final_calc_title, formula_dy, sub_dy, final_answer, box))

        summary = Text("k = 4  ->  R100m becomes R400m", font_size=48, color=BLUE)
        self.play(Write(summary))
        self.wait(3)
        self.play(FadeOut(summary))
