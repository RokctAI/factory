from manim import *

class InflationLesson(Scene):
    def construct(self):
        # SUBTOPIC 1: The Taxi Rank Reality (What is Inflation?)
        title = Text("Inflation: The Taxi Rank Reality", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Taxi Fare
        fare_text_old = Text("Taxi Fare Yesterday: R20", font_size=36, color=BLUE).shift(UP*1)
        fare_text_new = Text("Taxi Fare Today: R22", font_size=36, color=RED).shift(UP*0)
        self.play(Write(fare_text_old))
        self.wait(1)
        self.play(Write(fare_text_new))
        self.wait(2)

        inflation_def = Text("Inflation: Sustained & significant increase in general price level", font_size=28).shift(DOWN*1.5)
        self.play(Write(inflation_def))
        self.wait(3)

        self.play(FadeOut(fare_text_old), FadeOut(fare_text_new), FadeOut(inflation_def), FadeOut(title))

        # SUBTOPIC 2: The Spaza Shop Basket (CPI)
        title_cpi = Text("The Consumer Price Index (CPI)", font_size=40).to_edge(UP)
        self.play(Write(title_cpi))

        basket = Square(side_length=2, color=YELLOW).shift(UP*0.5)
        basket_text = Text("Basket of Goods\n(Bread, Mealie Meal, Taxi Fare)", font_size=24).move_to(basket)
        self.play(Create(basket), Write(basket_text))
        self.wait(2)

        cost_old = Text("Last Year: R1000", font_size=32).next_to(basket, DOWN*2 + LEFT)
        cost_new = Text("This Year: R1060", font_size=32).next_to(basket, DOWN*2 + RIGHT)
        self.play(Write(cost_old))
        self.wait(1)
        self.play(Write(cost_new))
        self.wait(2)

        index_old = Text("Index: 100", font_size=32, color=GREEN).next_to(cost_old, DOWN)
        index_new = Text("Index: 106", font_size=32, color=RED).next_to(cost_new, DOWN)
        self.play(Write(index_old))
        self.wait(1)
        self.play(Write(index_new))
        self.wait(3)

        self.play(FadeOut(basket), FadeOut(basket_text), FadeOut(cost_old), FadeOut(cost_new), FadeOut(index_old), FadeOut(index_new), FadeOut(title_cpi))

        # SUBTOPIC 3: The Math on the Streets (Calculating Inflation Rate)
        title_math = Text("Calculating Inflation Rate", font_size=40).to_edge(UP)
        self.play(Write(title_math))

        problem = Text("CPI rises from 120 to 126 over one year.", font_size=32).shift(UP*2)
        self.play(Write(problem))
        self.wait(2)

        formula = MathTex(
            r"\text{Inflation Rate} = \frac{\text{New CPI} - \text{Old CPI}}{\text{Old CPI}} \times 100"
        ).shift(UP*0.5)
        self.play(Write(formula))
        self.wait(3)

        sub_formula = MathTex(
            r"= \frac{126 - 120}{120} \times 100"
        ).next_to(formula, DOWN)
        self.play(Write(sub_formula))
        self.wait(2)

        step1 = MathTex(
            r"= \frac{6}{120} \times 100"
        ).next_to(sub_formula, DOWN)
        self.play(Write(step1))
        self.wait(2)

        step2 = MathTex(
            r"= 0.05 \times 100"
        ).next_to(step1, DOWN)
        self.play(Write(step2))
        self.wait(2)

        final_answer = MathTex(
            r"= 5\%"
        ).next_to(step2, DOWN)
        final_answer.set_color(GREEN)
        self.play(Write(final_answer))
        self.wait(4)

        self.play(FadeOut(Group(*self.mobjects)))
