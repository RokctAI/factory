from manim import *

class ArithmeticSequenceScene(Scene):
    def construct(self):
        # Subtopic 1: Introduction to Arithmetic Sequences and the General Formula
        title = Tex("Arithmetic Sequences").to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        def_text = Tex(r"Constant difference: $d$").shift(UP*1.5)
        first_term_text = Tex(r"First term: $a$").next_to(def_text, DOWN)

        self.play(Write(def_text))
        self.play(Write(first_term_text))
        self.wait(2)

        formula_title = Tex("General Formula:").next_to(first_term_text, DOWN, buff=1)
        formula = MathTex(r"T_n = a + (n - 1)d").next_to(formula_title, DOWN).scale(1.2)
        formula.set_color(YELLOW)

        self.play(Write(formula_title))
        self.play(Write(formula))
        self.wait(3)

        self.play(FadeOut(def_text), FadeOut(first_term_text), FadeOut(formula_title), FadeOut(formula))

        # Subtopic 2: Solving the Example Problem
        example_text = Tex(r"Example: Find the 20th term of $3; 7; 11; \dots$").next_to(title, DOWN, buff=0.5)
        self.play(Write(example_text))
        self.wait(2)

        diff1 = MathTex(r"T_2 - T_1 = 7 - 3 = 4").shift(UP*0.5)
        diff2 = MathTex(r"T_3 - T_2 = 11 - 7 = 4").next_to(diff1, DOWN)
        d_val = MathTex(r"\therefore d = 4").next_to(diff2, DOWN).set_color(BLUE)
        a_val = MathTex(r"a = 3").next_to(d_val, DOWN).set_color(BLUE)

        self.play(Write(diff1))
        self.play(Write(diff2))
        self.play(Write(d_val))
        self.play(Write(a_val))
        self.wait(2)

        self.play(FadeOut(diff1), FadeOut(diff2))

        # Group a_val and d_val and move them
        knowns = VGroup(a_val, d_val).arrange(RIGHT, buff=1).shift(UP*1)
        self.play(Transform(VGroup(a_val, d_val).copy(), knowns)) # copy because we are grouping
        self.remove(a_val, d_val)

        n_val = MathTex(r"n = 20").next_to(knowns, RIGHT, buff=1).set_color(BLUE)
        self.play(Write(n_val))
        self.wait(2)

        step1 = MathTex(r"T_n = a + (n - 1)d").next_to(knowns, DOWN, buff=1)
        step2 = MathTex(r"T_{20} = 3 + (20 - 1)(4)").next_to(step1, DOWN)
        step3 = MathTex(r"T_{20} = 3 + (19)(4)").next_to(step2, DOWN)
        step4 = MathTex(r"T_{20} = 3 + 76").next_to(step3, DOWN)
        step5 = MathTex(r"T_{20} = 79").next_to(step4, DOWN).set_color(GREEN)

        self.play(Write(step1))
        self.wait(1)
        self.play(Write(step2))
        self.wait(1)
        self.play(Write(step3))
        self.wait(1)
        self.play(Write(step4))
        self.wait(1)
        self.play(Write(step5))
        self.wait(3)

        self.play(FadeOut(example_text), FadeOut(knowns), FadeOut(n_val), FadeOut(step1), FadeOut(step2), FadeOut(step3), FadeOut(step4), FadeOut(step5))

        # Subtopic 3: Exam Technique and Distinction-Level Takeaway
        takeaway_title = Tex("Distinction-Level Takeaway").next_to(title, DOWN, buff=0.5)
        self.play(Write(takeaway_title))
        self.wait(2)

        takeaway_text = MathTex(r"T_n = a + (n - 1)d").shift(UP*0.5).scale(1.2)
        vars_text = Tex("System of variables: $a, d, n, T_n$").next_to(takeaway_text, DOWN)
        logic_text = Tex("Given any 3, solve for the 4th.").next_to(vars_text, DOWN)

        self.play(Write(takeaway_text))
        self.play(Write(vars_text))
        self.play(Write(logic_text))
        self.wait(3)

        self.play(FadeOut(takeaway_title), FadeOut(takeaway_text), FadeOut(vars_text), FadeOut(logic_text), FadeOut(title))
        self.wait(1)
