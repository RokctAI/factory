from manim import *

class NewtonsSecondLawScene(Scene):
    def construct(self):
        # Whiteboard style setup
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)

        # Introduction
        title = Text("Newton's Second Law", font_size=48, weight=BOLD).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Subtopic 1: Stating Newton's Second Law
        statement1 = Text("Net force causes acceleration", font_size=36).shift(UP * 1.5)
        self.play(FadeIn(statement1))
        self.wait(2)

        statement2 = Text("Acceleration is in the direction of the net force", font_size=32).next_to(statement1, DOWN)
        self.play(FadeIn(statement2))
        self.wait(2)

        statement3 = Text("a ∝ F_net  and  a ∝ 1/m", font_size=32).next_to(statement2, DOWN)
        self.play(FadeIn(statement3))
        self.wait(2)

        formula = MathTex(r"F_{\text{net}} = m \cdot a", font_size=48).next_to(statement3, DOWN, buff=0.8)
        self.play(Write(formula))
        self.wait(2)

        formula_box = SurroundingRectangle(formula, color=BLUE, buff=0.2)
        self.play(Create(formula_box))
        self.wait(2)

        # Clear for Subtopic 2
        self.play(FadeOut(statement1), FadeOut(statement2), FadeOut(statement3), FadeOut(formula), FadeOut(formula_box))

        # Subtopic 2: Applying Newton's Second Law
        problem_text1 = Text("A 5 kg crate on a frictionless horizontal surface", font_size=28).shift(UP * 1.5)
        problem_text2 = Text("is pulled by a horizontal force of 20 N.", font_size=28).next_to(problem_text1, DOWN)
        problem_text3 = Text("Calculate its acceleration.", font_size=28).next_to(problem_text2, DOWN)

        self.play(Write(problem_text1), Write(problem_text2), Write(problem_text3))
        self.wait(3)

        # Draw Free Body Diagram
        crate = Rectangle(width=2, height=1.5, color=BLACK, fill_color=LIGHT_GREY, fill_opacity=0.5).shift(DOWN * 1.5)
        mass_label = MathTex(r"5\text{ kg}", font_size=32).move_to(crate.get_center())

        self.play(Create(crate), Write(mass_label))
        self.wait(2)

        force_arrow = Arrow(start=crate.get_right(), end=crate.get_right() + RIGHT * 2, color=RED, buff=0)
        force_label = MathTex(r"20\text{ N}", font_size=32, color=RED).next_to(force_arrow, UP, buff=0.1)

        self.play(GrowArrow(force_arrow), Write(force_label))
        self.wait(2)

        # Identify givens
        givens = VGroup(
            MathTex(r"m = 5\text{ kg}", font_size=32),
            MathTex(r"F_{\text{net}} = 20\text{ N}", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL).shift(DOWN * 2)

        self.play(FadeIn(givens))
        self.wait(2)

        # Calculation steps (CAPS style)
        step1 = MathTex(r"F_{\text{net}} = m \cdot a", font_size=36).to_corner(UR).shift(DOWN * 2 + LEFT * 2)
        self.play(Write(step1))
        self.wait(2)

        step2 = MathTex(r"20 = 5 \cdot a", font_size=36).next_to(step1, DOWN, aligned_edge=LEFT)
        self.play(Write(step2))
        self.wait(2)

        step3 = MathTex(r"a = \frac{20}{5}", font_size=36).next_to(step2, DOWN, aligned_edge=LEFT)
        self.play(Write(step3))
        self.wait(1)

        step4 = MathTex(r"a = 4\text{ m}\cdot\text{s}^{-2}", font_size=36, color=BLUE).next_to(step3, DOWN, aligned_edge=LEFT)
        self.play(Write(step4))
        self.wait(2)

        accel_arrow = Arrow(start=crate.get_top() + LEFT, end=crate.get_top() + RIGHT, color=BLUE, buff=0).shift(UP * 0.5)
        accel_label = MathTex(r"a = 4\text{ m}\cdot\text{s}^{-2}", font_size=32, color=BLUE).next_to(accel_arrow, UP, buff=0.1)

        self.play(GrowArrow(accel_arrow), Write(accel_label))
        self.wait(3)

        # Clear for Subtopic 3
        self.play(
            FadeOut(problem_text1), FadeOut(problem_text2), FadeOut(problem_text3),
            FadeOut(crate), FadeOut(mass_label), FadeOut(force_arrow), FadeOut(force_label),
            FadeOut(givens), FadeOut(step1), FadeOut(step2), FadeOut(step3), FadeOut(step4),
            FadeOut(accel_arrow), FadeOut(accel_label)
        )

        # Subtopic 3: Summary
        summary_title = Text("Summary", font_size=40, weight=BOLD).shift(UP * 2)
        self.play(Write(summary_title))

        point1 = Text("• F_net = m · a", font_size=32).next_to(summary_title, DOWN, buff=0.5).align_to(summary_title, LEFT)
        self.play(FadeIn(point1))
        self.wait(1)

        point2 = Text("• Acceleration is proportional to net force", font_size=32).next_to(point1, DOWN, buff=0.3).align_to(point1, LEFT)
        self.play(FadeIn(point2))
        self.wait(1)

        point3 = Text("• Acceleration is inversely proportional to mass", font_size=32).next_to(point2, DOWN, buff=0.3).align_to(point2, LEFT)
        self.play(FadeIn(point3))
        self.wait(1)

        point4 = Text("• Always show: Formula, Substitution, Answer with Unit", font_size=32, color=BLUE).next_to(point3, DOWN, buff=0.3).align_to(point3, LEFT)
        self.play(FadeIn(point4))
        self.wait(3)

        self.play(FadeOut(summary_title), FadeOut(point1), FadeOut(point2), FadeOut(point3), FadeOut(point4), FadeOut(title))
        self.wait(1)
