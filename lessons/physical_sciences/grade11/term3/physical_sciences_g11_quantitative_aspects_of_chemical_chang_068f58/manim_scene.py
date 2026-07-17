from manim import *

class StoichiometryScene(Scene):
    def construct(self):
        # Subtopic 1: The Principle of Stoichiometry and the Balanced Equation
        title = Text("Law of Conservation of Mass", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        problem_text = Text("Find mass of CO₂ when 8 g CH₄ burns in excess O₂", font_size=24).next_to(title, DOWN)
        self.play(Write(problem_text))
        self.wait(2)

        unbalanced_eq = MathTex(r"\text{CH}_4 + \text{O}_2 \rightarrow \text{CO}_2 + \text{H}_2\text{O}").shift(UP*1)
        self.play(Write(unbalanced_eq))
        self.wait(3)

        # Balancing animation
        balanced_eq = MathTex(r"\text{CH}_4 + 2\text{O}_2 \rightarrow \text{CO}_2 + 2\text{H}_2\text{O}").shift(UP*1)
        self.play(Transform(unbalanced_eq, balanced_eq))
        self.wait(2)

        # Emphasize molar ratio
        ratio = MathTex(r"1 : 2 : 1 : 2").next_to(balanced_eq, DOWN, buff=0.5)
        self.play(Write(ratio))
        self.wait(3)
        self.play(FadeOut(ratio))

        # Subtopic 2: Moles to Moles: The Molar Ratio
        formula_n = MathTex(r"n = \frac{m}{M}").shift(LEFT*3 + DOWN*0.5)
        self.play(Write(formula_n))
        self.wait(2)

        molar_mass_ch4 = MathTex(r"M(\text{CH}_4) = 12 + 4(1) = 16 \text{ g\cdot mol}^{-1}").next_to(formula_n, DOWN, aligned_edge=LEFT)
        self.play(Write(molar_mass_ch4))
        self.wait(2)

        sub_n = MathTex(r"n(\text{CH}_4) = \frac{8}{16}").next_to(molar_mass_ch4, DOWN, aligned_edge=LEFT)
        self.play(Write(sub_n))
        self.wait(2)

        ans_n = MathTex(r"n(\text{CH}_4) = 0,5 \text{ mol}").next_to(sub_n, DOWN, aligned_edge=LEFT)
        self.play(Write(ans_n))
        self.wait(3)

        bridge = MathTex(r"\text{Ratio CH}_4 : \text{CO}_2 = 1 : 1").shift(RIGHT*3 + DOWN*0.5)
        self.play(Write(bridge))
        self.wait(2)

        n_co2 = MathTex(r"n(\text{CO}_2) = 0,5 \text{ mol}").next_to(bridge, DOWN, aligned_edge=LEFT)
        self.play(Write(n_co2))
        self.wait(3)

        self.play(FadeOut(formula_n, molar_mass_ch4, sub_n, ans_n, bridge))

        # Subtopic 3: Converting to Mass and Securing the Marks
        n_co2.generate_target()
        n_co2.target.shift(LEFT*6 + UP*1)
        self.play(MoveToTarget(n_co2))

        formula_m = MathTex(r"m = n \times M").next_to(n_co2, DOWN, aligned_edge=LEFT)
        self.play(Write(formula_m))
        self.wait(2)

        molar_mass_co2 = MathTex(r"M(\text{CO}_2) = 12 + 2(16) = 44 \text{ g\cdot mol}^{-1}").next_to(formula_m, DOWN, aligned_edge=LEFT)
        self.play(Write(molar_mass_co2))
        self.wait(2)

        sub_m = MathTex(r"m(\text{CO}_2) = 0,5 \times 44").next_to(molar_mass_co2, DOWN, aligned_edge=LEFT)
        self.play(Write(sub_m))
        self.wait(2)

        ans_m = MathTex(r"m(\text{CO}_2) = 22 \text{ g}").next_to(sub_m, DOWN, aligned_edge=LEFT)
        ans_m.set_color(YELLOW)
        self.play(Write(ans_m))
        self.wait(3)

        # Final summary
        summary = VGroup(
            Text("1. Balance equation", font_size=20),
            Text("2. Convert to moles", font_size=20),
            Text("3. Use molar ratio", font_size=20),
            Text("4. Convert to final mass", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT*3 + DOWN*1)
        self.play(Write(summary))
        self.wait(4)

        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)
