from manim import *

class MechanicalEnergyScene(Scene):
    def construct(self):
        # Subtopic 1: Introduction to Mechanical Energy
        title = Tex("Conservation of Mechanical Energy").to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        ek_eq = MathTex(r"E_k = \frac{1}{2}mv^2")
        ep_eq = MathTex(r"E_p = mgh")
        emech_eq = MathTex(r"E_{mech} = E_k + E_p").shift(DOWN * 1.5)

        VGroup(ek_eq, ep_eq).arrange(RIGHT, buff=2).shift(UP * 0.5)

        self.play(Write(ek_eq))
        self.wait(2)
        self.play(Write(ep_eq))
        self.wait(2)
        self.play(Write(emech_eq))
        self.wait(3)

        self.play(FadeOut(ek_eq), FadeOut(ep_eq), FadeOut(emech_eq))

        # Subtopic 2: The Principle of Conservation
        principle_text = Text("Isolated System: No external non-conservative forces", font_size=32).shift(UP * 0.5)
        self.play(Write(principle_text))
        self.wait(3)

        principle_eq1 = MathTex(r"E_{mech, i} = E_{mech, f}").shift(DOWN * 0.5)
        self.play(Write(principle_eq1))
        self.wait(2)

        principle_eq2 = MathTex(r"(E_k + E_p)_i = (E_k + E_p)_f").shift(DOWN * 1.5)
        self.play(Write(principle_eq2))
        self.wait(2)

        principle_eq3 = MathTex(r"\frac{1}{2}mv_i^2 + mgh_i = \frac{1}{2}mv_f^2 + mgh_f").shift(DOWN * 2.5)
        self.play(Write(principle_eq3))
        self.wait(4)

        self.play(FadeOut(principle_text), FadeOut(principle_eq1), FadeOut(principle_eq2), FadeOut(principle_eq3), FadeOut(title))

        # Subtopic 3: Solving the Falling Ball Problem
        problem_title = Tex("Example: A dropped ball").to_edge(UP)
        self.play(Write(problem_title))

        # Draw free-body / scenario (ball dropping)
        ground = Line(LEFT*2, RIGHT*2, color=WHITE).shift(DOWN*2 + LEFT*4)
        ball = Circle(radius=0.3, color=BLUE, fill_opacity=1).shift(UP*2 + LEFT*4)
        height_line = DashedLine(ball.get_center() + RIGHT*0.5, ground.get_center() + RIGHT*0.5, color=YELLOW)
        height_label = MathTex(r"h_i = 5 \text{ m}").next_to(height_line, RIGHT)
        mass_label = MathTex(r"m = 2 \text{ kg}").next_to(ball, LEFT)
        vi_label = MathTex(r"v_i = 0 \text{ m\cdot s}^{-1}").next_to(ball, UP)

        self.play(Create(ground), Create(ball), Create(height_line), Write(height_label), Write(mass_label), Write(vi_label))
        self.wait(3)

        # Working out
        eq1 = MathTex(r"(E_k + E_p)_i = (E_k + E_p)_f").shift(UP*1.5 + RIGHT*2)
        eq2 = MathTex(r"\frac{1}{2}mv_i^2 + mgh_i = \frac{1}{2}mv_f^2 + mgh_f").next_to(eq1, DOWN)

        self.play(Write(eq1))
        self.wait(2)
        self.play(Write(eq2))
        self.wait(3)

        # Explicit substitution
        eq3 = MathTex(r"\frac{1}{2}(2)(0)^2 + (2)(9,8)(5) = \frac{1}{2}(2)v_f^2 + (2)(9,8)(0)").next_to(eq2, DOWN)
        self.play(Write(eq3))
        self.wait(4)

        eq4 = MathTex(r"0 + 98 = v_f^2 + 0").next_to(eq3, DOWN)
        self.play(Write(eq4))
        self.wait(2)

        eq5 = MathTex(r"98 = v_f^2").next_to(eq4, DOWN)
        self.play(Write(eq5))
        self.wait(3)

        self.play(FadeOut(eq1), FadeOut(eq2), FadeOut(eq3), FadeOut(eq4))
        self.play(eq5.animate.shift(UP*4))

        # Subtopic 4: Final Calculation and Mark Sheet Advice
        ball_final = ball.copy().shift(DOWN*3.7) # Just above ground
        vf_label = MathTex(r"v_f = ?").next_to(ball_final, RIGHT)
        self.play(Transform(ball, ball_final), Write(vf_label))
        self.wait(2)

        eq6 = MathTex(r"v_f = \sqrt{98}").next_to(eq5, DOWN)
        self.play(Write(eq6))
        self.wait(2)

        eq7 = MathTex(r"v_f = 9,90 \text{ m\cdot s}^{-1}").next_to(eq6, DOWN)
        self.play(Write(eq7))
        self.wait(3)

        # Mark allocation highlighting
        box_form = SurroundingRectangle(eq1, color=GREEN) # Wait, eq1 was faded out. Let's just create a summary mark display.

        self.play(FadeOut(eq5), FadeOut(eq6), FadeOut(eq7), FadeOut(ground), FadeOut(ball), FadeOut(height_line), FadeOut(height_label), FadeOut(mass_label), FadeOut(vi_label), FadeOut(vf_label), FadeOut(problem_title))

        mark_title = Tex("Mark Allocation").to_edge(UP)
        self.play(Write(mark_title))

        mark1 = MathTex(r"\checkmark \text{ Formula: } (E_k + E_p)_i = (E_k + E_p)_f")
        mark2 = MathTex(r"\checkmark \text{ LHS substitution: } \frac{1}{2}(2)(0)^2 + (2)(9,8)(5)")
        mark3 = MathTex(r"\checkmark \text{ RHS substitution: } \frac{1}{2}(2)v_f^2 + (2)(9,8)(0)")
        mark4 = MathTex(r"\checkmark \text{ Final answer with unit: } 9,90 \text{ m\cdot s}^{-1}")

        marks = VGroup(mark1, mark2, mark3, mark4).arrange(DOWN, aligned_edge=LEFT).shift(DOWN*0.5)

        for mark in marks:
            self.play(Write(mark))
            self.wait(2)

        self.wait(3)
        self.play(FadeOut(mark_title), FadeOut(marks))
        self.wait(1)
