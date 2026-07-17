from manim import *

class VatCalculationsScene(Scene):
    def construct(self):
        # Set up a whiteboard background (optional, keeping it simple dark theme for better visibility of colors)
        self.camera.background_color = "#1E1E1E"

        # --- Subtopic 1: What is VAT? ---
        title = Tex("VAT: Value Added Tax", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Introduce the TV concept
        tv_box = Rectangle(width=4, height=3, color=WHITE).shift(LEFT * 3)
        tv_label = Tex("TV", font_size=40).move_to(tv_box.get_center())
        price_tag = VGroup(
            Tex("R6 899", font_size=36, color=GREEN),
            Tex("Incl. VAT @ 15\\%", font_size=24)
        ).arrange(DOWN).next_to(tv_box, DOWN)

        self.play(Create(tv_box), Write(tv_label))
        self.wait(1)
        self.play(Write(price_tag))
        self.wait(3)

        # Explain breakdown conceptually
        price_incl_text = Tex("Price Incl. VAT = ", font_size=36).shift(RIGHT * 2 + UP * 1)
        breakdown_group = VGroup(
            Tex("Shop's Money", font_size=32, color=BLUE),
            Tex("+", font_size=32),
            Tex("Gov't VAT", font_size=32, color=RED)
        ).arrange(RIGHT).next_to(price_incl_text, DOWN)

        self.play(Write(price_incl_text))
        self.wait(1)
        self.play(Write(breakdown_group))
        self.wait(4)

        self.play(FadeOut(tv_box, tv_label, price_tag, price_incl_text, breakdown_group))

        # --- Subtopic 2: The Golden Rule of VAT ---
        rule_title = Tex("The Golden Rule", font_size=42, color=YELLOW).next_to(title, DOWN).shift(DOWN*0.5)
        self.play(Write(rule_title))
        self.wait(2)

        rule_eq1 = MathTex(r"\text{Price Excl VAT} = 100\%", font_size=36, color=BLUE).shift(UP * 0.5)
        rule_eq2 = MathTex(r"+ \text{VAT} = 15\%", font_size=36, color=RED).next_to(rule_eq1, DOWN, aligned_edge=LEFT)
        line = Line(start=rule_eq2.get_left() + LEFT*0.2 + DOWN*0.2, end=rule_eq2.get_right() + RIGHT*0.2 + DOWN*0.2)
        rule_eq3 = MathTex(r"\text{Price Incl VAT} = 115\%", font_size=36, color=GREEN).next_to(line, DOWN, aligned_edge=LEFT)

        self.play(Write(rule_eq1))
        self.wait(2)
        self.play(Write(rule_eq2))
        self.wait(1)
        self.play(Create(line), Write(rule_eq3))
        self.wait(4)

        warning = Tex("Don't just subtract 15\\% from the final price!", font_size=32, color=RED).next_to(rule_eq3, DOWN).shift(DOWN*0.5)
        self.play(Write(warning))
        self.wait(3)

        self.play(FadeOut(rule_title, rule_eq1, rule_eq2, line, rule_eq3, warning))

        # --- Subtopic 3: Calculating Price Excluding VAT ---
        calc_title = Tex("Calculating Price Excl. VAT", font_size=42, color=YELLOW).next_to(title, DOWN).shift(DOWN*0.5)
        self.play(Write(calc_title))
        self.wait(2)

        given_info = Tex("Price Incl. VAT = R6 899 (which is $115\\%$)", font_size=36).shift(UP*1)
        self.play(Write(given_info))
        self.wait(2)

        step1 = MathTex(r"\text{Price Excl VAT} \times 115\% = \text{R6 899}", font_size=36)
        step2 = MathTex(r"\text{Price Excl VAT} \times 1,15 = \text{R6 899}", font_size=36).next_to(step1, DOWN)
        step3 = MathTex(r"\text{Price Excl VAT} = \text{R6 899} \div 1,15", font_size=36).next_to(step2, DOWN)

        self.play(Write(step1))
        self.wait(2)
        self.play(Write(step2))
        self.wait(2)
        self.play(Write(step3))
        self.wait(3)

        ans_unrounded = MathTex(r"= \text{R5 999,130434...}", font_size=36).next_to(step3, DOWN)
        ans_rounded = MathTex(r"= \text{R5 999,13}", font_size=36, color=BLUE).next_to(ans_unrounded, DOWN)

        self.play(Write(ans_unrounded))
        self.wait(2)
        self.play(Write(ans_rounded))
        self.wait(3)

        self.play(FadeOut(calc_title, given_info, step1, step2, step3, ans_unrounded, ans_rounded))

        # --- Subtopic 4: Calculating the VAT Amount ---
        vat_title = Tex("Calculating VAT Amount", font_size=42, color=YELLOW).next_to(title, DOWN).shift(DOWN*0.5)
        self.play(Write(vat_title))
        self.wait(2)

        method1_title = Tex("Method 1: Subtraction", font_size=36, color=ORANGE).shift(UP*1 + LEFT*2)
        self.play(Write(method1_title))

        vat_eq = MathTex(r"\text{VAT Amount} = \text{Incl. VAT} - \text{Excl. VAT}", font_size=32).next_to(method1_title, DOWN, aligned_edge=LEFT)
        vat_sub = MathTex(r"= \text{R6 899,00} - \text{R5 999,13}", font_size=32).next_to(vat_eq, DOWN, aligned_edge=LEFT)
        vat_ans = MathTex(r"= \text{R899,87}", font_size=36, color=RED).next_to(vat_sub, DOWN, aligned_edge=LEFT)

        self.play(Write(vat_eq))
        self.wait(1)
        self.play(Write(vat_sub))
        self.wait(2)
        self.play(Write(vat_ans))
        self.wait(3)

        # --- Subtopic 5: Checking Our Work ---
        method2_title = Tex("Method 2: Check (15\\% of base)", font_size=36, color=ORANGE).shift(UP*1 + RIGHT*2)
        self.play(Write(method2_title))

        check_eq = MathTex(r"\text{VAT Amount} = 15\% \times \text{Excl. VAT}", font_size=32).next_to(method2_title, DOWN, aligned_edge=LEFT)
        check_sub = MathTex(r"= 0,15 \times \text{R5 999,13}", font_size=32).next_to(check_eq, DOWN, aligned_edge=LEFT)
        check_ans_unrounded = MathTex(r"= \text{R899,8695}", font_size=32).next_to(check_sub, DOWN, aligned_edge=LEFT)
        check_ans = MathTex(r"= \text{R899,87}", font_size=36, color=RED).next_to(check_ans_unrounded, DOWN, aligned_edge=LEFT)

        self.play(Write(check_eq))
        self.wait(1)
        self.play(Write(check_sub))
        self.wait(2)
        self.play(Write(check_ans_unrounded))
        self.wait(1)
        self.play(Write(check_ans))
        self.wait(3)

        # Conclude
        box1 = SurroundingRectangle(vat_ans, color=GREEN)
        box2 = SurroundingRectangle(check_ans, color=GREEN)
        self.play(Create(box1), Create(box2))
        self.wait(4)

        self.play(FadeOut(Group(*self.mobjects)))
