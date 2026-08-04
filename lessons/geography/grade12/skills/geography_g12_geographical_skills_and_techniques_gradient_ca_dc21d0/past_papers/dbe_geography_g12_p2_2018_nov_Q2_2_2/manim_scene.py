from manim import *

# Auto-generated past-paper worked example.
# Source: DBE NSC Grade 12 Geography P2, November 2018, Q2.2.2
# (c) Department of Basic Education, 2018.
class PastPaperWorkedExample(Scene):
    def construct(self):
        head = Tex(r"Past paper: DBE Nov 2018 Geography P2 Q2.2.2").to_edge(UP)
        self.play(Write(head)); self.wait(1)
        formula = MathTex(r"\text{Average gradient} = \frac{\text{vertical interval (VI)}}{\text{horizontal equivalent (HE)}}").scale(0.8).shift(UP * 1.8)
        self.play(Write(formula)); self.wait(2)
        vi = MathTex(r"VI = 1057.9\,\text{m} - 820\,\text{m} = 237.9\,\text{m}").scale(0.85).shift(UP * 0.6)
        self.play(Write(vi)); self.wait(2)
        he = MathTex(r"HE = 3.9\,\text{cm} \times 50000 = 1950\,\text{m}").scale(0.85).shift(DOWN * 0.4)
        self.play(Write(he)); self.wait(2)
        grad = MathTex(r"\text{Gradient} = \frac{237.9}{1950}").scale(0.85).shift(DOWN * 1.4)
        self.play(Write(grad)); self.wait(2)
        ans = MathTex(r"= 1 : 8.2").scale(1.0).shift(DOWN * 2.4)
        self.play(Write(ans)); self.wait(3)
