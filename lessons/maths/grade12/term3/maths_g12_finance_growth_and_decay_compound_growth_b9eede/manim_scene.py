from manim import *

class CompoundGrowthScene(Scene):
    def construct(self):
        # Subtopic 1: The Logic of Growth on Growth
        title = Tex("Compound Growth").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        concept = Tex("Growth on top of growth").next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(concept))
        self.wait(2)

        self.play(FadeOut(concept))

        # Subtopic 2: Year 1: The First Step
        problem = Tex("Invest R5000 at 8\\% p.a. for 3 years").next_to(title, DOWN, buff=0.5)
        self.play(Write(problem))
        self.wait(2)

        year1_title = Tex("Year 1:").to_edge(LEFT).shift(UP*1)
        self.play(Write(year1_title))

        year1_start = MathTex(r"\text{Start: } R5000").next_to(year1_title, RIGHT, buff=0.5)
        self.play(Write(year1_start))
        self.wait(1)

        year1_interest = MathTex(r"\text{Interest: } R5000 \times 0,08 = R400").next_to(year1_start, DOWN, aligned_edge=LEFT)
        self.play(Write(year1_interest))
        self.wait(1)

        year1_end = MathTex(r"\text{End: } R5000 + R400 = R5400").next_to(year1_interest, DOWN, aligned_edge=LEFT)
        self.play(Write(year1_end))
        self.wait(2)

        # Subtopic 3: Year 2 and 3: The Snowball Effect
        year2_title = Tex("Year 2:").to_edge(LEFT).shift(DOWN*1.5)
        self.play(Write(year2_title))

        year2_start = MathTex(r"\text{Start: } R5400").next_to(year2_title, RIGHT, buff=0.5)
        self.play(Write(year2_start))
        self.wait(1)

        year2_interest = MathTex(r"\text{Interest: } R5400 \times 0,08 = R432").next_to(year2_start, DOWN, aligned_edge=LEFT)
        self.play(Write(year2_interest))
        self.wait(1)

        year2_end = MathTex(r"\text{End: } R5400 + R432 = R5832").next_to(year2_interest, DOWN, aligned_edge=LEFT)
        self.play(Write(year2_end))
        self.wait(2)

        # Clear screen for Year 3 to make space
        self.play(
            FadeOut(year1_title), FadeOut(year1_start), FadeOut(year1_interest), FadeOut(year1_end),
            FadeOut(year2_title), FadeOut(year2_start), FadeOut(year2_interest), FadeOut(year2_end)
        )

        year3_title = Tex("Year 3:").to_edge(LEFT).shift(UP*1)
        self.play(Write(year3_title))

        year3_start = MathTex(r"\text{Start: } R5832").next_to(year3_title, RIGHT, buff=0.5)
        self.play(Write(year3_start))
        self.wait(1)

        year3_interest = MathTex(r"\text{Interest: } R5832 \times 0,08 = R466,56").next_to(year3_start, DOWN, aligned_edge=LEFT)
        self.play(Write(year3_interest))
        self.wait(1)

        year3_end = MathTex(r"\text{End: } R5832 + R466,56 = R6298,56").next_to(year3_interest, DOWN, aligned_edge=LEFT)
        self.play(Write(year3_end))
        self.wait(2)

        # Subtopic 4: The Fast Way: The Formula
        self.play(
            FadeOut(year3_title), FadeOut(year3_start), FadeOut(year3_interest), FadeOut(year3_end),
            FadeOut(problem)
        )

        formula_title = Tex("The Shortcut (Formula)").next_to(title, DOWN, buff=0.5)
        self.play(Write(formula_title))
        self.wait(1)

        formula = MathTex(r"A = P(1 + i)^n").scale(1.5).next_to(formula_title, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(2)

        sub_formula1 = MathTex(r"A = 5000(1 + 0,08)^3").next_to(formula, DOWN, buff=0.5)
        self.play(Write(sub_formula1))
        self.wait(1)

        sub_formula2 = MathTex(r"A = 5000(1,08)^3").next_to(sub_formula1, DOWN, buff=0.2)
        self.play(Write(sub_formula2))
        self.wait(1)

        final_answer = MathTex(r"A = R6298,56").next_to(sub_formula2, DOWN, buff=0.2)
        self.play(Write(final_answer))
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))
