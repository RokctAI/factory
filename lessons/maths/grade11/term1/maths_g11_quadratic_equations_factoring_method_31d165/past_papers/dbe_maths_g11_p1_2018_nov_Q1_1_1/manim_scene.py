from manim import *

# Auto-generated past-paper worked example.
# Source: DBE Grade 11 Mathematics P1, November 2018, Q1.1.1
# (c) Department of Basic Education, 2018.
class PastPaperWorkedExample(Scene):
    def construct(self):
        head = Tex(r"Past paper: DBE Nov 2018 P1 Q1.1.1").to_edge(UP)
        self.play(Write(head)); self.wait(1)
        eq = MathTex(r"x(2x + 1) = 0")
        self.play(Write(eq)); self.wait(2)
        self.play(eq.animate.shift(UP * 2))
        note = Tex(r"Zero-product property: a product is 0 when a factor is 0").scale(0.7)
        self.play(Write(note)); self.wait(2)
        left = MathTex(r"x = 0").shift(LEFT * 2 + DOWN)
        right = MathTex(r"2x + 1 = 0 \Rightarrow x = -\tfrac{1}{2}").shift(RIGHT * 2 + DOWN)
        self.play(Write(left), Write(right)); self.wait(2)
        ans = MathTex(r"x = 0 \quad \text{or} \quad x = -\tfrac{1}{2}").shift(DOWN * 2.5)
        self.play(Write(ans)); self.wait(3)
