from manim import *

class GradientCalculation(Scene):
    def construct(self):
        # Subtopic 1: The Concept of Gradient and the Formula
        title = Text("Gradient Calculation").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        formula_text = Text("Gradient Formula:").next_to(title, DOWN, buff=0.5)
        self.play(Write(formula_text))

        formula_math = MathTex(r"\text{Gradient} = \frac{\text{Vertical Interval (VI)}}{\text{Horizontal Equivalent (HE)}}")
        formula_math.next_to(formula_text, DOWN, buff=0.5)
        self.play(Write(formula_math))
        self.wait(2)

        target_format = Text("Target Format: 1:X").next_to(formula_math, DOWN, buff=0.5)
        self.play(Write(target_format))
        self.wait(2)

        self.play(FadeOut(formula_text), FadeOut(formula_math), FadeOut(target_format))

        # Example Problem Text
        example_text = Text(
            "Calculate gradient between:\nTrig beacon 251 (1200m) and Spot height (900m)\nDistance: 4.5km",
            font_size=24
        ).to_edge(UL)
        self.play(Write(example_text))
        self.wait(1)

        # Draw cross section
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[800, 1300, 100],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True}
        ).scale(0.8).to_edge(DR)

        labels = axes.get_axis_labels(x_label="Distance (km)", y_label="Elevation (m)")
        self.play(Create(axes), Write(labels))

        # Points
        p_trig = axes.c2p(0, 1200)
        p_spot = axes.c2p(4.5, 900)

        trig_dot = Dot(p_trig, color=RED)
        spot_dot = Dot(p_spot, color=BLUE)

        trig_label = Text("Trig 251 (1200m)", font_size=20).next_to(trig_dot, UP)
        spot_label = Text("Spot Height (900m)", font_size=20).next_to(spot_dot, RIGHT)

        self.play(FadeIn(trig_dot, trig_label), FadeIn(spot_dot, spot_label))

        line = Line(p_trig, p_spot, color=YELLOW)
        self.play(Create(line))
        self.wait(2)

        # Subtopic 2: Reading Elevations and Calculating Vertical Interval
        vi_title = Text("1. Vertical Interval (VI)").to_edge(L).shift(UP*1)
        self.play(Write(vi_title))

        vi_formula = MathTex(r"\text{VI} = 1200\text{m} - 900\text{m}").next_to(vi_title, DOWN, aligned_edge=LEFT)
        self.play(Write(vi_formula))

        vi_result = MathTex(r"\text{VI} = 300\text{m}").next_to(vi_formula, DOWN, aligned_edge=LEFT)
        self.play(Write(vi_result))

        # Show on diagram
        vi_line = Line(axes.c2p(4.5, 1200), p_spot, color=RED, stroke_width=4)
        vi_brace = Brace(vi_line, direction=RIGHT)
        vi_brace_text = vi_brace.get_text("300m").scale(0.6)
        self.play(Create(vi_line), Create(vi_brace), Write(vi_brace_text))
        self.wait(2)

        # Subtopic 3: Determining the Horizontal Equivalent (HE)
        he_title = Text("2. Horizontal Equivalent (HE)").next_to(vi_result, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(he_title))

        he_given = Text("Given Distance = 4.5km", font_size=32).next_to(he_title, DOWN, aligned_edge=LEFT)
        self.play(Write(he_given))

        he_line = Line(p_trig, axes.c2p(4.5, 1200), color=BLUE, stroke_width=4)
        he_brace = Brace(he_line, direction=UP)
        he_brace_text = he_brace.get_text("4.5km").scale(0.6)
        self.play(Create(he_line), Create(he_brace), Write(he_brace_text))
        self.wait(2)

        # Subtopic 4: Unit Conversion
        conv_title = Text("3. Unit Conversion").next_to(he_given, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(conv_title))

        conv_formula = MathTex(r"\text{HE} = 4.5\text{km} \times 1000").next_to(conv_title, DOWN, aligned_edge=LEFT)
        self.play(Write(conv_formula))

        conv_result = MathTex(r"\text{HE} = 4500\text{m}").next_to(conv_formula, DOWN, aligned_edge=LEFT)
        self.play(Write(conv_result))

        # Update brace text
        new_he_brace_text = he_brace.get_text("4500m").scale(0.6)
        self.play(Transform(he_brace_text, new_he_brace_text))
        self.wait(2)

        self.play(
            FadeOut(vi_title, vi_formula, he_title, he_given, conv_title, conv_formula),
            vi_result.animate.to_edge(L).shift(UP*1),
            conv_result.animate.next_to(vi_result.generate_target(), DOWN, aligned_edge=LEFT, buff=0.2)
        )

        # Subtopic 5: Final Calculation and Interpretation
        final_title = Text("4. Final Calculation").next_to(conv_result, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(final_title))

        grad_calc = MathTex(r"\text{Gradient} = \frac{300}{4500}").next_to(final_title, DOWN, aligned_edge=LEFT)
        self.play(Write(grad_calc))

        grad_step2 = MathTex(r"= \frac{300 \div 300}{4500 \div 300}").next_to(grad_calc, DOWN, aligned_edge=LEFT)
        self.play(Write(grad_step2))

        grad_step3 = MathTex(r"= \frac{1}{15}").next_to(grad_step2, DOWN, aligned_edge=LEFT)
        self.play(Write(grad_step3))

        final_answer = Text("Gradient = 1:15", color=GREEN).next_to(grad_step3, DOWN, aligned_edge=LEFT)
        self.play(Write(final_answer))
        self.wait(2)

        interpretation = Text("For every 15m horizontal, 1m vertical change.", font_size=20).next_to(final_answer, DOWN, aligned_edge=LEFT)
        self.play(Write(interpretation))
        self.wait(3)
