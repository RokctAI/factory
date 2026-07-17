from manim import *

class ResistorsInParallelScene(Scene):
    def construct(self):
        # Whiteboard background
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)

        # Intro text
        title = Text("Resistors in Parallel", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Draw a simple circuit with 3 parallel resistors
        # V battery, R1, R2, R3

        # A simple visual representation of parallel branches
        branch_text = Text("Multiple pathways for current", font_size=24, color=BLUE).next_to(title, DOWN)
        self.play(FadeIn(branch_text))

        battery = MathTex(r"V = 12 \text{ V}").move_to(LEFT * 4)

        # Resistors
        r1_label = MathTex(r"R_1 = 2 \, \Omega").move_to(RIGHT * 2 + UP * 1.5)
        r2_label = MathTex(r"R_2 = 3 \, \Omega").move_to(RIGHT * 2)
        r3_label = MathTex(r"R_3 = 6 \, \Omega").move_to(RIGHT * 2 + DOWN * 1.5)

        self.play(Write(battery))
        self.play(Write(r1_label))
        self.play(Write(r2_label))
        self.play(Write(r3_label))
        self.wait(3)

        # Transition to formula
        self.play(FadeOut(branch_text), FadeOut(battery), FadeOut(r1_label), FadeOut(r2_label), FadeOut(r3_label))

        formula_title = Text("Parallel Resistance Formula", font_size=32).next_to(title, DOWN)
        self.play(Write(formula_title))

        formula = MathTex(r"\frac{1}{R_p} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}").move_to(UP * 0.5)
        self.play(Write(formula))
        self.wait(3)

        # Example calculation: Step 1 (Total Resistance)
        sub_title_1 = Text("Step 1: Calculate equivalent resistance", font_size=24, color=BLUE).next_to(formula, DOWN)
        self.play(Write(sub_title_1))

        sub_step = MathTex(r"\frac{1}{R_p} = \frac{1}{2} + \frac{1}{3} + \frac{1}{6}").next_to(sub_title_1, DOWN)
        self.play(Write(sub_step))
        self.wait(2)

        lcd_step = MathTex(r"\frac{1}{R_p} = \frac{3}{6} + \frac{2}{6} + \frac{1}{6}").next_to(sub_step, DOWN)
        self.play(Write(lcd_step))
        self.wait(2)

        sum_step = MathTex(r"\frac{1}{R_p} = \frac{6}{6} = 1").next_to(lcd_step, DOWN)
        self.play(Write(sum_step))
        self.wait(2)

        invert_text = Text("Invert to find final resistance!", font_size=24, color=RED).to_edge(RIGHT)
        self.play(Write(invert_text))

        final_rp = MathTex(r"R_p = 1 \, \Omega").next_to(sum_step, DOWN)
        self.play(Write(final_rp))
        self.wait(3)

        # Transition to Step 2 (Total Current)
        self.play(
            FadeOut(formula_title), FadeOut(formula), FadeOut(sub_title_1),
            FadeOut(sub_step), FadeOut(lcd_step), FadeOut(sum_step),
            FadeOut(invert_text), FadeOut(final_rp)
        )

        sub_title_2 = Text("Step 2: Calculate total current", font_size=24, color=BLUE).next_to(title, DOWN)
        self.play(Write(sub_title_2))

        knowns = MathTex(r"R_p = 1 \, \Omega \quad V = 12 \text{ V}").move_to(UP * 1.5)
        self.play(Write(knowns))
        self.wait(2)

        ohm_law = MathTex(r"R = \frac{V}{I}").next_to(knowns, DOWN)
        self.play(Write(ohm_law))
        self.wait(2)

        ohm_sub = MathTex(r"1 = \frac{12}{I}").next_to(ohm_law, DOWN)
        self.play(Write(ohm_sub))
        self.wait(2)

        ohm_rearrange = MathTex(r"I = \frac{12}{1}").next_to(ohm_sub, DOWN)
        self.play(Write(ohm_rearrange))
        self.wait(2)

        final_I = MathTex(r"I = 12 \text{ A}").next_to(ohm_rearrange, DOWN)
        box = SurroundingRectangle(final_I, color=GREEN)
        self.play(Write(final_I), Create(box))

        self.wait(4)

        # Cleanup
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)
