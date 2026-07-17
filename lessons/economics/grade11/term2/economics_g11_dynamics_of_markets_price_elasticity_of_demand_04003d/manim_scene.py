from manim import *

class PriceElasticityScene(Scene):
    def construct(self):
        # Subtopic 1: The Taxi Fare Reality Check
        title = Text("Price Elasticity of Demand", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        taxi_example = Text("Taxi Fare: R15 \u2192 R20", font_size=36, color=YELLOW)
        self.play(FadeIn(taxi_example))
        self.wait(2)

        reaction_text = Text("Reaction = Elasticity", font_size=36, color=BLUE).next_to(taxi_example, DOWN)
        self.play(Write(reaction_text))
        self.wait(2)

        self.play(FadeOut(taxi_example), FadeOut(reaction_text))

        # Subtopic 2: Defining Price Elasticity of Demand
        definition = Text(
            "Responsiveness of Quantity Demanded\nto a change in Price",
            font_size=32,
            line_spacing=1.5
        )
        self.play(Write(definition))
        self.wait(2)

        law_of_demand = Text("Price \u2191 , Qd \u2193", font_size=36, color=RED).next_to(definition, DOWN, buff=1)
        self.play(FadeIn(law_of_demand))
        self.wait(2)

        self.play(FadeOut(definition), FadeOut(law_of_demand))

        # Subtopic 3: The Elasticity Formula
        formula_title = Text("The Formula", font_size=40, color=BLUE).next_to(title, DOWN, buff=1)
        self.play(Write(formula_title))

        ped_formula = MathTex(r"PED = \frac{\% \Delta Qd}{\% \Delta P}", font_size=48)
        self.play(FadeIn(ped_formula))
        self.wait(2)

        q_change_formula = MathTex(r"\% \Delta Qd = \frac{\text{Change in Qd}}{\text{Original Qd}} \times 100", font_size=36).next_to(ped_formula, DOWN, buff=0.5)
        p_change_formula = MathTex(r"\% \Delta P = \frac{\text{Change in P}}{\text{Original P}} \times 100", font_size=36).next_to(q_change_formula, DOWN, buff=0.5)

        self.play(Write(q_change_formula), Write(p_change_formula))
        self.wait(2)

        self.play(FadeOut(formula_title), FadeOut(ped_formula), FadeOut(q_change_formula), FadeOut(p_change_formula))

        # Subtopic 4: Solving the Calculation
        problem_title = Text("Example Calculation", font_size=40, color=BLUE).next_to(title, DOWN, buff=1)
        self.play(Write(problem_title))

        prices = Text("P1 = R10, P2 = R12  \u2192  Change = R2", font_size=32)
        quantities = Text("Q1 = 100, Q2 = 80  \u2192  Change = 20", font_size=32).next_to(prices, DOWN, buff=0.5)

        calc_group = VGroup(prices, quantities).move_to(ORIGIN)
        self.play(FadeIn(prices))
        self.wait(1)
        self.play(FadeIn(quantities))
        self.wait(2)

        perc_p = MathTex(r"\% \Delta P = \frac{2}{10} \times 100 = 20\%", font_size=36).next_to(quantities, DOWN, buff=0.5)
        perc_q = MathTex(r"\% \Delta Qd = \frac{20}{100} \times 100 = 20\%", font_size=36).next_to(perc_p, DOWN, buff=0.5)

        self.play(Write(perc_p))
        self.wait(1)
        self.play(Write(perc_q))
        self.wait(2)

        ped_calc = MathTex(r"PED = \frac{20\%}{20\%} = 1", font_size=48, color=YELLOW).next_to(perc_q, DOWN, buff=0.5)
        self.play(Write(ped_calc))
        self.wait(2)

        self.play(FadeOut(problem_title), FadeOut(prices), FadeOut(quantities), FadeOut(perc_p), FadeOut(perc_q), FadeOut(ped_calc))

        # Subtopic 5: Classifying Elasticity Categories
        class_title = Text("Classifying Elasticity", font_size=40, color=BLUE).next_to(title, DOWN, buff=1)
        self.play(Write(class_title))

        elastic = Text("PED > 1 : PRICE ELASTIC (Big reaction)", font_size=32).next_to(class_title, DOWN, buff=0.5)
        inelastic = Text("PED < 1 : PRICE INELASTIC (Small reaction)", font_size=32).next_to(elastic, DOWN, buff=0.5)
        unitary = Text("PED = 1 : UNITARY ELASTICITY (Equal reaction)", font_size=32, color=YELLOW).next_to(inelastic, DOWN, buff=0.5)

        self.play(FadeIn(elastic))
        self.wait(1)
        self.play(FadeIn(inelastic))
        self.wait(1)
        self.play(FadeIn(unitary))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(class_title), FadeOut(elastic), FadeOut(inelastic), FadeOut(unitary))
        self.wait(1)
