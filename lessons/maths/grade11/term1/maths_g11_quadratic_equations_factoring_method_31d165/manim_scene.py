from manim import *

# BAND LAYOUT reference implementation (see manim_exporter.py):
# content is laid out in sequential vertical bands along a long virtual
# canvas — one band per teaching step, each sized to be framed full-screen
# on a phone. Nothing is ever faded out or overwritten; at each step the
# camera moves down to clean space and earlier work stays on the canvas.

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k (k=0 is the
    default frame; each band is one frame-height further down)."""
    return DOWN * BAND * k


class QuadraticFactoring(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # --- Band 0: Review and Introduction ---
        title = Tex("Factoring Quadratic Equations").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        expansion_text = Tex(r"Expansion: $(x+1)(x+2) \rightarrow x^2 + 3x + 2$").scale(1.1).shift(UP * 0.5)
        factoring_text = Tex(r"Factoring: $x^2 + 3x + 2 \rightarrow (x+1)(x+2)$").scale(1.1).shift(DOWN * 0.7)
        self.play(Write(expansion_text))
        self.wait(3)
        self.play(Write(factoring_text))
        self.wait(4)

        # --- Band 1: Standard form ---
        self.next_band(1)
        std_form_title = Tex("Standard Form").scale(1.2).shift(band_shift(1) + UP * 1.5)
        std_form = MathTex("a", "x^2 + ", "b", "x + ", "c", " = 0").scale(1.4).shift(band_shift(1))
        self.play(Write(std_form_title), Write(std_form))
        self.wait(3)

        # --- Band 2: The example problem and its coefficients ---
        self.next_band(2)
        eq_title = Tex("Example Problem").scale(1.2).shift(band_shift(2) + UP * 2)
        eq = MathTex("2", "x^2 + ", "5", "x + ", "3", " = 0").scale(1.4).shift(band_shift(2) + UP * 0.8)
        self.play(Write(eq_title), Write(eq))
        self.wait(2)
        coef_a = MathTex("a = 2").scale(1.1).shift(band_shift(2) + LEFT * 3 + DOWN * 0.5)
        coef_b = MathTex("b = 5").scale(1.1).shift(band_shift(2) + DOWN * 0.5)
        coef_c = MathTex("c = 3").scale(1.1).shift(band_shift(2) + RIGHT * 3 + DOWN * 0.5)
        self.play(Write(coef_a), Write(coef_b), Write(coef_c))
        self.wait(3)
        target_prod = MathTex(r"a \times c = 2 \times 3 = 6").scale(1.1).shift(band_shift(2) + LEFT * 2 + DOWN * 1.8)
        target_sum = MathTex("b = 5").scale(1.1).shift(band_shift(2) + RIGHT * 2.5 + DOWN * 1.8)
        self.play(Write(target_prod), Write(target_sum))
        self.wait(4)

        # --- Band 3: Finding the factor pair ---
        self.next_band(3)
        factors_text = Tex("Factors of 6 that add to 5:").scale(1.2).shift(band_shift(3) + UP * 1.3)
        factors_1 = Tex(r"$1 \times 6 = 6$, \quad $1 + 6 = 7$ \quad (No)").scale(1.1).shift(band_shift(3))
        factors_2 = Tex(r"$2 \times 3 = 6$, \quad $2 + 3 = 5$ \quad (Yes!)").scale(1.1).shift(band_shift(3) + DOWN * 1)
        self.play(Write(factors_text))
        self.wait(1)
        self.play(Write(factors_1))
        self.wait(2)
        self.play(Write(factors_2))
        self.wait(3)

        # --- Band 4: Split the middle term and group ---
        self.next_band(4)
        split_title = Tex("Split the middle term").scale(1.2).shift(band_shift(4) + UP * 1.8)
        eq_split = MathTex("2x^2 + ", "2x + 3x", " + 3 = 0").scale(1.3).shift(band_shift(4) + UP * 0.6)
        self.play(Write(split_title), Write(eq_split))
        self.wait(3)
        group_full = MathTex("(2x^2 + 2x)", " + ", "(3x + 3)", " = 0").scale(1.3).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(group_full))
        self.wait(3)

        # --- Band 5: Factor each group, spot the common binomial ---
        self.next_band(5)
        gcf_title = Tex("Factor out the GCF of each group").scale(1.1).shift(band_shift(5) + UP * 1.8)
        factor_full = MathTex("2x", "(x + 1)", " + ", "3", "(x + 1)", " = 0").scale(1.3).shift(band_shift(5) + UP * 0.5)
        self.play(Write(gcf_title), Write(factor_full))
        self.wait(3)
        self.play(factor_full[1].animate.set_color(YELLOW),
                  factor_full[4].animate.set_color(YELLOW))
        self.wait(2)
        final_factored = MathTex("(x + 1)", "(2x + 3)", " = 0").scale(1.4).shift(band_shift(5) + DOWN * 1.2)
        final_factored[0].set_color(YELLOW)
        self.play(Write(final_factored))
        self.wait(4)

        # --- Band 6: Zero-product property — solve both factors ---
        self.next_band(6)
        zpp_title = Tex("Zero-Product Property").scale(1.2).shift(band_shift(6) + UP * 2)
        self.play(Write(zpp_title))
        self.wait(3)
        eq1 = MathTex("x + 1 = 0").scale(1.2).shift(band_shift(6) + LEFT * 3 + UP * 0.5)
        eq2 = MathTex("2x + 3 = 0").scale(1.2).shift(band_shift(6) + RIGHT * 3 + UP * 0.5)
        self.play(Write(eq1), Write(eq2))
        self.wait(3)
        sol1 = MathTex("x = -1").scale(1.2).shift(band_shift(6) + LEFT * 3 + DOWN * 0.7)
        self.play(Write(sol1))
        self.wait(2)
        step1_eq2 = MathTex("2x = -3").scale(1.2).shift(band_shift(6) + RIGHT * 3 + DOWN * 0.7)
        sol2 = MathTex("x = -\\frac{3}{2}").scale(1.2).shift(band_shift(6) + RIGHT * 3 + DOWN * 1.9)
        self.play(Write(step1_eq2))
        self.wait(2)
        self.play(Write(sol2))
        self.wait(3)
        box1 = SurroundingRectangle(sol1, color=GREEN)
        box2 = SurroundingRectangle(sol2, color=GREEN)
        self.play(Create(box1), Create(box2))
        self.wait(5)

        # --- Band 7: Check the answers ---
        self.next_band(7)
        check_title = Tex("Check").scale(1.2).shift(band_shift(7) + UP * 1.3)
        check_text = Tex(r"$2(-1)^2 + 5(-1) + 3 = 2 - 5 + 3 = 0 \quad \checkmark$").scale(1.1).shift(band_shift(7))
        self.play(Write(check_title))
        self.play(Write(check_text))
        self.wait(4)
