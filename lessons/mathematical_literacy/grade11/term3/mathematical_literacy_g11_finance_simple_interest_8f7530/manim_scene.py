from manim import *

class SimpleInterestScene(Scene):
    def construct(self):
        # Whiteboard setup
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)

        # Title
        title = Text("Simple Interest", font_size=48, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Subtopic 1: The Money in Your Hand (Setup the scenario)
        scenario_text = Text("Invest: R8 000\nRate: 6,5% p.a.\nTime: 3 years", font_size=36, line_spacing=1.5)
        scenario_text.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(scenario_text))
        self.wait(2)

        # Subtopic 2: The Till Slip Calculation (Finding the Interest)
        formula_text = Text("Formula: ", font_size=36)
        formula_math = MathTex(r"Simple\ Interest = P \times i \times n", font_size=36)
        formula_group = VGroup(formula_text, formula_math).arrange(RIGHT)
        formula_group.next_to(scenario_text, DOWN, buff=1.0)
        self.play(Write(formula_group))
        self.wait(2)

        # Break down variables
        vars_text = Text("P = R8 000\ni = 6,5% = 0,065\nn = 3", font_size=32, line_spacing=1.2)
        vars_text.next_to(formula_group, DOWN, buff=0.5).align_to(formula_group, LEFT)
        self.play(FadeIn(vars_text))
        self.wait(2)

        # Substitute and calculate
        sub_math = MathTex(r"Interest = 8\ 000 \times 0,065 \times 3", font_size=36)
        sub_math.next_to(vars_text, DOWN, buff=0.5).align_to(vars_text, LEFT)
        self.play(Write(sub_math))
        self.wait(2)

        ans_math = MathTex(r"Interest = R1\ 560,00", font_size=36, color=GREEN_E)
        ans_math.next_to(sub_math, DOWN, buff=0.3).align_to(sub_math, LEFT)
        self.play(Write(ans_math))
        self.wait(2)

        # Subtopic 3: The Final Count (Total Value)
        # Clear middle section to make room for final calculation
        self.play(
            FadeOut(formula_group),
            FadeOut(vars_text),
            FadeOut(sub_math),
            ans_math.animate.next_to(scenario_text, DOWN, buff=1.0)
        )

        total_formula = MathTex(r"A = P + I", font_size=36)
        total_formula.next_to(ans_math, DOWN, buff=0.5).align_to(ans_math, LEFT)
        self.play(Write(total_formula))
        self.wait(2)

        total_sub = MathTex(r"A = 8\ 000 + 1\ 560", font_size=36)
        total_sub.next_to(total_formula, DOWN, buff=0.3).align_to(total_formula, LEFT)
        self.play(Write(total_sub))
        self.wait(2)

        total_ans = MathTex(r"A = R9\ 560,00", font_size=42, color=BLUE_E)
        total_ans.next_to(total_sub, DOWN, buff=0.3).align_to(total_sub, LEFT)
        self.play(Write(total_ans))
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)
