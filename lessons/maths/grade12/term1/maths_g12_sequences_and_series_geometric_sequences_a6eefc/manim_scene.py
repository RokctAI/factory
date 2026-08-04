from manim import *

class GeometricSequencesScene(Scene):
    def construct(self):
        # Subtopic 1: Introduction and the General Formula
        title = Text("Geometric Sequences", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        ratio_def = MathTex(r"r = \frac{T_2}{T_1} = \frac{T_3}{T_2}").next_to(title, DOWN, buff=1)
        self.play(Write(ratio_def))
        self.wait(3)

        formula = MathTex(r"T_n = a \cdot r^{n-1}").next_to(ratio_def, DOWN, buff=1)
        self.play(Write(formula))
        self.wait(3)

        formula_desc = Text("a = first term, r = constant ratio, n = position", font_size=24).next_to(formula, DOWN, buff=0.5)
        self.play(Write(formula_desc))
        self.wait(4)

        self.play(FadeOut(ratio_def), FadeOut(formula), FadeOut(formula_desc))

        # Subtopic 2: Solving the Example Problem
        problem_text = Text("Find the 10th term of 2; 6; 18; ...", font_size=36).next_to(title, DOWN, buff=1)
        self.play(Write(problem_text))
        self.wait(3)

        a_val = MathTex(r"a = 2").next_to(problem_text, DOWN, buff=0.5).align_to(problem_text, LEFT)
        self.play(Write(a_val))
        self.wait(2)

        r_calc = MathTex(r"r = \frac{6}{2} = 3 \quad \left( \frac{18}{6} = 3 \right)").next_to(a_val, DOWN, buff=0.5).align_to(a_val, LEFT)
        self.play(Write(r_calc))
        self.wait(3)

        n_val = MathTex(r"n = 10").next_to(r_calc, DOWN, buff=0.5).align_to(r_calc, LEFT)
        self.play(Write(n_val))
        self.wait(2)

        self.play(FadeOut(problem_text), FadeOut(a_val), FadeOut(r_calc), FadeOut(n_val))

        sub_formula = MathTex(r"T_n = a \cdot r^{n-1}").next_to(title, DOWN, buff=1)
        self.play(Write(sub_formula))
        self.wait(2)

        sub_step1 = MathTex(r"T_{10} = 2 \cdot (3)^{10-1}").next_to(sub_formula, DOWN, buff=0.5)
        self.play(Write(sub_step1))
        self.wait(3)

        sub_step2 = MathTex(r"T_{10} = 2 \cdot (3)^9").next_to(sub_step1, DOWN, buff=0.5)
        self.play(Write(sub_step2))
        self.wait(3)

        sub_step3 = MathTex(r"T_{10} = 2 \cdot 19683").next_to(sub_step2, DOWN, buff=0.5)
        self.play(Write(sub_step3))
        self.wait(2)

        final_ans = MathTex(r"T_{10} = 39366").next_to(sub_step3, DOWN, buff=0.5)
        self.play(Write(final_ans))
        self.wait(4)

        self.play(FadeOut(sub_formula), FadeOut(sub_step1), FadeOut(sub_step2), FadeOut(sub_step3), FadeOut(final_ans))

        # Subtopic 3: Exam Techniques for Geometric Sequences
        exam_tips_title = Text("Exam Techniques", font_size=36).next_to(title, DOWN, buff=1)
        self.play(Write(exam_tips_title))
        self.wait(2)

        tip1 = Text("1. Test first 3 terms: arithmetic vs geometric", font_size=28).next_to(exam_tips_title, DOWN, buff=0.5).align_to(exam_tips_title, LEFT)
        self.play(Write(tip1))
        self.wait(3)

        tip2 = Text("2. Exponent applies only to r", font_size=28).next_to(tip1, DOWN, buff=0.5).align_to(tip1, LEFT)
        self.play(Write(tip2))
        self.wait(3)

        tip2_math = MathTex(r"a \cdot r^{n-1} \neq (a \cdot r)^{n-1}").next_to(tip2, DOWN, buff=0.5)
        self.play(Write(tip2_math))
        self.wait(4)

        self.play(FadeOut(exam_tips_title), FadeOut(tip1), FadeOut(tip2), FadeOut(tip2_math), FadeOut(title))
        self.wait(2)
