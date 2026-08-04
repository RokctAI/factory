from manim import *

# BAND LAYOUT reference implementation (see manim_exporter.py):
# one band per algebraic step — the previous Transform-chain rewrote a
# single equation in place, which serialized every step onto the same
# spot in the exported primitives. Bands give each step its own space on
# a long virtual canvas; the camera pans down, old work stays visible at
# the frame edge, and every step is phone-full-screen legible.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CompletingTheSquare(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Opening intro beat: topic stays full-screen (player-side) while
        # the tutor speaks the intro; the first board write defines the
        # manifest's topic_display duration. See the factoring reference
        # scene for the full rationale.
        self.wait(4)

        # --- Band 0: title + the equation we are solving ---
        title = Tex("Completing the Square").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(3)
        eq1 = MathTex(r"x^2 + 6x + 2 = 0").scale(1.5)
        self.play(Write(eq1))
        self.wait(6)  # covers the verbal algorithm explanation

        # --- Band 1: move the constant across ---
        self.next_band(1)
        step1_label = Tex("Move the constant").scale(1.1).shift(band_shift(1) + UP * 1.4)
        eq2 = MathTex(r"x^2 + 6x = -2").scale(1.5).shift(band_shift(1))
        self.play(Write(step1_label), Write(eq2))
        self.wait(3)

        # --- Band 2: the critical move — add (b/2)^2 to both sides ---
        self.next_band(2)
        step2_label = Tex(r"Halve the $x$ coefficient, square it, add to BOTH sides").scale(0.9).shift(band_shift(2) + UP * 1.8)
        half = MathTex(r"\tfrac{6}{2} = 3, \quad 3^2 = 9").scale(1.2).shift(band_shift(2) + UP * 0.7)
        eq3 = MathTex(r"x^2 + 6x + (3)^2 = -2 + (3)^2").scale(1.3).shift(band_shift(2) + DOWN * 0.5)
        eq4 = MathTex(r"x^2 + 6x + 9 = 7").scale(1.3).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(step2_label))
        self.play(Write(half))
        self.wait(3)
        self.play(Write(eq3))
        self.wait(3)
        self.play(Write(eq4))
        self.wait(3)

        # --- Band 3: factorise the perfect square ---
        self.next_band(3)
        step3_label = Tex("The left side is now a perfect square").scale(1.0).shift(band_shift(3) + UP * 1.4)
        eq5 = MathTex(r"(x + 3)^2 = 7").scale(1.5).shift(band_shift(3))
        self.play(Write(step3_label), Write(eq5))
        self.wait(4)

        # --- Band 4: square root both sides and solve ---
        self.next_band(4)
        eq6 = MathTex(r"x + 3 = \pm \sqrt{7}").scale(1.4).shift(band_shift(4) + UP * 1)
        eq7 = MathTex(r"x = -3 \pm \sqrt{7}").scale(1.4).shift(band_shift(4) - UP * 0.3)
        self.play(Write(eq6))
        self.wait(4)
        self.play(Write(eq7))
        self.wait(3)

        # --- Band 5: the two solutions, boxed ---
        self.next_band(5)
        sol1 = MathTex(r"x = -3 + \sqrt{7}").scale(1.3).shift(band_shift(5) + LEFT * 2.8)
        sol2 = MathTex(r"x = -3 - \sqrt{7}").scale(1.3).shift(band_shift(5) + RIGHT * 2.8)
        self.play(Write(sol1), Write(sol2))
        box1 = SurroundingRectangle(sol1, color=GREEN)
        box2 = SurroundingRectangle(sol2, color=GREEN)
        self.play(Create(box1), Create(box2))
        self.wait(5)
