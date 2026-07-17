from manim import *

class BreakEvenAnalysis(Scene):
    def construct(self):
        # 1. The Spaza Shop Cash Box (Fixed vs Variable)
        title = Text("Break-even Analysis").to_edge(UP)
        self.play(Write(title))

        fixed_cost_text = Text("Fixed Costs: R60 000 (Rent)").scale(0.8).shift(UP*2)
        variable_cost_text = Text("Variable Cost: R30 per unit").scale(0.8).next_to(fixed_cost_text, DOWN, buff=0.5)
        selling_price_text = Text("Selling Price: R50 per unit").scale(0.8).next_to(variable_cost_text, DOWN, buff=0.5)

        self.play(FadeIn(fixed_cost_text))
        self.wait(2)
        self.play(FadeIn(variable_cost_text))
        self.wait(2)
        self.play(FadeIn(selling_price_text))
        self.wait(2)

        self.play(
            FadeOut(fixed_cost_text),
            FadeOut(variable_cost_text),
            FadeOut(selling_price_text)
        )

        # 2. Making a Profit on One Item (Contribution Margin)
        cm_title = Text("Contribution Margin").scale(0.9).to_edge(UP*2)
        self.play(Write(cm_title))

        cm_formula = MathTex(
            r"\text{Selling Price} - \text{Variable Cost} = \text{Contribution per unit}"
        ).scale(0.8).shift(UP*1)
        self.play(Write(cm_formula))

        cm_calc = MathTex(
            r"\text{R50} - \text{R30} = \text{R20}"
        ).scale(0.9).next_to(cm_formula, DOWN, buff=0.5)
        self.play(Write(cm_calc))
        self.wait(2)

        self.play(
            FadeOut(cm_title),
            FadeOut(cm_formula),
            FadeOut(cm_calc)
        )

        # 3. Calculating the Break-even Point & 4. The Formal Exam Format
        be_title = Text("Break-even Point Formula").scale(0.9).to_edge(UP*2)
        self.play(Write(be_title))

        be_formula = MathTex(
            r"\frac{\text{Total Fixed Costs}}{\text{Selling Price} - \text{Variable Cost}}"
        ).scale(0.8).shift(UP*1)
        self.play(Write(be_formula))
        self.wait(2)

        be_subst = MathTex(
            r"= \frac{\text{R60 000}}{\text{R50} - \text{R30}}"
        ).scale(0.9).next_to(be_formula, DOWN, buff=0.5)
        self.play(Write(be_subst))
        self.wait(2)

        be_subst_2 = MathTex(
            r"= \frac{\text{R60 000}}{\text{R20}}"
        ).scale(0.9).next_to(be_subst, DOWN, buff=0.5)
        self.play(Write(be_subst_2))
        self.wait(2)

        be_final = MathTex(
            r"= 3\ 000 \text{ units}"
        ).scale(1.1).next_to(be_subst_2, DOWN, buff=0.5)
        be_final.set_color(YELLOW)
        self.play(Write(be_final))
        self.wait(3)

        self.play(
            FadeOut(be_title),
            FadeOut(be_formula),
            FadeOut(be_subst),
            FadeOut(be_subst_2),
            FadeOut(be_final)
        )

        # 5. Ethics and Internal Control
        ethics_title = Text("Internal Control").scale(0.9).to_edge(UP*2)
        ethics_desc = Text("Regular physical stock counts prevent theft.\nEvery stolen unit requires more sales to break even!").scale(0.6).shift(UP*0.5)

        self.play(Write(ethics_title))
        self.play(Write(ethics_desc))
        self.wait(3)

        self.play(
            FadeOut(ethics_title),
            FadeOut(ethics_desc),
            FadeOut(title)
        )
