from manim import *

class VatCalculationScene(Scene):
    def construct(self):
        # Subtopic 1: The Spaza Shop Cash Box (Intro to VAT)
        # Introduction title
        title = Text("Value Added Tax (VAT) Calculations").scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Spaza shop conceptual display
        item = Text("Maize Meal").scale(0.7).shift(UP*1.5 + LEFT*2)
        price_tag = Text("R2 875 (Incl. VAT)").scale(0.7).next_to(item, DOWN)
        self.play(FadeIn(item), Write(price_tag))
        self.wait(3)

        # Move to calculation setup
        self.play(FadeOut(item), FadeOut(title))
        self.play(price_tag.animate.shift(UP*2 + RIGHT*2))

        # Subtopic 2: Extracting the VAT (The Calculation)
        calc_title = Text("Extracting the VAT").scale(0.8).to_edge(UP)
        self.play(Write(calc_title))
        self.wait(1)

        # Explanation of 115%
        excl_text = Text("Exclusive = 100%").scale(0.6).shift(LEFT*3 + UP*0.5)
        vat_text = Text("VAT = 15%").scale(0.6).next_to(excl_text, DOWN)
        incl_text = Text("Inclusive = 115%").scale(0.6).next_to(vat_text, DOWN)

        self.play(Write(excl_text))
        self.wait(1)
        self.play(Write(vat_text))
        self.wait(1)
        self.play(Write(incl_text))
        self.wait(2)

        # Formula and Calculation
        formula_text = MathTex(r"\text{Amount} \times \frac{\text{Want}}{\text{Have}}").scale(0.7).shift(RIGHT*3 + UP*0.5)
        self.play(Write(formula_text))
        self.wait(2)

        vat_calc = MathTex(r"\text{R2 875} \times \frac{15}{115} = \text{R375} \text{ (VAT)}").scale(0.7).next_to(formula_text, DOWN*1.5)
        self.play(Write(vat_calc))
        self.wait(2)

        excl_calc = MathTex(r"\text{R2 875} - \text{R375} = \text{R2 500} \text{ (Exclusive)}").scale(0.7).next_to(vat_calc, DOWN*1.5)
        self.play(Write(excl_calc))
        self.wait(3)

        # Clear screen for T-accounts
        self.play(
            FadeOut(calc_title), FadeOut(price_tag), FadeOut(excl_text),
            FadeOut(vat_text), FadeOut(incl_text), FadeOut(formula_text),
            FadeOut(vat_calc), FadeOut(excl_calc)
        )

        # Subtopic 3: Formal Ledger Accounts (Double Entry)
        ledger_title = Text("General Ledger").scale(0.8).to_edge(UP)
        self.play(Write(ledger_title))

        # T-Account drawing function
        def draw_t_account(name, position):
            acc_name = Text(name).scale(0.5).move_to(position + UP*1.2)
            hline = Line(position + LEFT*2 + UP*0.8, position + RIGHT*2 + UP*0.8)
            vline = Line(position + UP*0.8, position + DOWN*1.5)
            dr = Text("Dr").scale(0.4).next_to(hline, UP, aligned_edge=LEFT).shift(RIGHT*0.2)
            cr = Text("Cr").scale(0.4).next_to(hline, UP, aligned_edge=RIGHT).shift(LEFT*0.2)

            group = VGroup(acc_name, hline, vline, dr, cr)
            return group

        # Draw T-Accounts
        bank_acc = draw_t_account("Bank", LEFT*4)
        sales_acc = draw_t_account("Sales", ORIGIN)
        vat_acc = draw_t_account("VAT Control", RIGHT*4)

        self.play(Create(bank_acc), Create(sales_acc), Create(vat_acc))
        self.wait(2)

        # Post figures
        # Debit Bank
        bank_entry = Text("Sales/VAT 2 875").scale(0.4).move_to(LEFT*5 + UP*0.5)
        self.play(Write(bank_entry))
        self.wait(2)

        # Credit Sales
        sales_entry = Text("Bank 2 500").scale(0.4).move_to(RIGHT*1 + UP*0.5)
        self.play(Write(sales_entry))
        self.wait(2)

        # Credit VAT Control
        vat_entry = Text("Bank 375").scale(0.4).move_to(RIGHT*5 + UP*0.5)
        self.play(Write(vat_entry))
        self.wait(2)

        # Highlight balancing
        self.play(bank_entry.animate.set_color(GREEN))
        self.play(sales_entry.animate.set_color(YELLOW), vat_entry.animate.set_color(YELLOW))
        self.wait(2)

        # Ethics message
        ethics = Text("Always pay collected VAT to SARS!").scale(0.6).set_color(RED).to_edge(DOWN)
        self.play(Write(ethics))
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))
