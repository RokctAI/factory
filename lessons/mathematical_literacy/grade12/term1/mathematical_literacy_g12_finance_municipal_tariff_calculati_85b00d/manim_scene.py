from manim import *

class MunicipalTariffScene(Scene):
    def construct(self):
        # Set up a whiteboard style background
        self.camera.background_color = WHITE

        # Subtopic 1: Reading the Municipal Bill (Context and Estimate)
        title = Text("Municipal Electricity Bill", color=BLACK, font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Draw a simplified bill
        bill_rect = Rectangle(width=6, height=4, color=BLACK, fill_opacity=0.1, fill_color=LIGHT_GREY)
        bill_rect.next_to(title, DOWN, buff=0.5)

        basic_fee_text = Text("Basic Fee: R120,00", color=BLACK, font_size=24)
        basic_fee_text.next_to(bill_rect.get_top(), DOWN, buff=0.5).align_to(bill_rect.get_left(), LEFT).shift(RIGHT * 0.5)

        tariff_text = Text("Usage Tariff: R1,85 / kWh", color=BLACK, font_size=24)
        tariff_text.next_to(basic_fee_text, DOWN, buff=0.5).align_to(basic_fee_text, LEFT)

        usage_text = Text("Current Usage: 450 kWh", color=BLACK, font_size=24)
        usage_text.next_to(tariff_text, DOWN, buff=0.5).align_to(tariff_text, LEFT)

        self.play(Create(bill_rect))
        self.play(Write(basic_fee_text))
        self.wait(1)
        self.play(Write(tariff_text))
        self.wait(1)
        self.play(Write(usage_text))
        self.wait(3)

        # Highlight basic fee
        hl_box_basic = SurroundingRectangle(basic_fee_text, color=RED)
        self.play(Create(hl_box_basic))
        self.wait(2)

        # Highlight tariff and usage
        hl_box_usage = SurroundingRectangle(VGroup(tariff_text, usage_text), color=BLUE)
        self.play(ReplacementTransform(hl_box_basic, hl_box_usage))
        self.wait(3)
        self.play(FadeOut(hl_box_usage))

        # Estimate section (mental math)
        estimate_title = Text("Rough Estimate", color=BLACK, font_size=32)
        estimate_title.next_to(bill_rect, RIGHT, buff=1)

        est_usage_eq = MathTex(r"2 \times 450 = 900", color=BLACK)
        est_usage_eq.next_to(estimate_title, DOWN, buff=0.5)

        est_total_eq = MathTex(r"900 + 120 = 1020", color=BLACK)
        est_total_eq.next_to(est_usage_eq, DOWN, buff=0.5)

        est_note = Text("Ans < R1020", color=RED, font_size=28)
        est_note.next_to(est_total_eq, DOWN, buff=0.5)

        self.play(Write(estimate_title))
        self.wait(1)
        self.play(Write(est_usage_eq))
        self.wait(1)
        self.play(Write(est_total_eq))
        self.wait(1)
        self.play(Write(est_note))
        self.wait(4)

        # Clear board for exact calculation
        self.play(
            FadeOut(estimate_title), FadeOut(est_usage_eq), FadeOut(est_total_eq), FadeOut(est_note),
            FadeOut(title), FadeOut(bill_rect), FadeOut(basic_fee_text), FadeOut(tariff_text), FadeOut(usage_text)
        )
        self.wait(1)

        # Subtopic 2: Calculating the Usage Cost
        usage_title = Text("Step 1: Usage Cost", color=BLACK, font_size=40)
        usage_title.to_edge(UP)
        self.play(Write(usage_title))
        self.wait(1)

        formula_usage = MathTex(r"\text{Usage Cost} = \text{Usage (kWh)} \times \text{Tariff}", color=BLACK)
        formula_usage.next_to(usage_title, DOWN, buff=1)
        self.play(Write(formula_usage))
        self.wait(2)

        sub_usage = MathTex(r"\text{Usage Cost} = 450 \times 1,85", color=BLACK)
        sub_usage.next_to(formula_usage, DOWN, buff=0.5)
        self.play(Write(sub_usage))
        self.wait(2)

        ans_usage_raw = MathTex(r"= 832,5", color=BLACK)
        ans_usage_raw.next_to(sub_usage, DOWN, buff=0.5)
        self.play(Write(ans_usage_raw))
        self.wait(2)

        # Rounding to money format
        ans_usage_final = MathTex(r"= \text{R}832,50", color=BLUE)
        ans_usage_final.move_to(ans_usage_raw)
        self.play(ReplacementTransform(ans_usage_raw, ans_usage_final))
        self.wait(3)

        self.play(FadeOut(usage_title), FadeOut(formula_usage), FadeOut(sub_usage), FadeOut(ans_usage_final))
        self.wait(1)

        # Subtopic 3: Calculating the Total Bill
        total_title = Text("Step 2: Total Bill", color=BLACK, font_size=40)
        total_title.to_edge(UP)
        self.play(Write(total_title))
        self.wait(1)

        formula_total = MathTex(r"\text{Total Bill} = \text{Basic Fee} + \text{Usage Cost}", color=BLACK)
        formula_total.next_to(total_title, DOWN, buff=1)
        self.play(Write(formula_total))
        self.wait(2)

        sub_total = MathTex(r"\text{Total Bill} = \text{R}120,00 + \text{R}832,50", color=BLACK)
        sub_total.next_to(formula_total, DOWN, buff=0.5)
        self.play(Write(sub_total))
        self.wait(2)

        ans_total = MathTex(r"= \text{R}952,50", color=GREEN)
        ans_total.next_to(sub_total, DOWN, buff=0.5)
        self.play(Write(ans_total))
        self.wait(3)

        # Final highlight
        hl_final = SurroundingRectangle(ans_total, color=GREEN)
        self.play(Create(hl_final))
        self.wait(3)

        self.play(FadeOut(total_title), FadeOut(formula_total), FadeOut(sub_total), FadeOut(ans_total), FadeOut(hl_final))
        self.wait(1)
