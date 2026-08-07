from manim import *

# Auto-generated past-paper worked example.
# Source: DBE Grade 11 Physical Sciences P1, November 2018, Q4.3
# (c) Department of Basic Education, 2018.
class PastPaperWorkedExample(Scene):
    def construct(self):
        head = Tex(r"Past paper: DBE Nov 2018 P1 Q4.3").to_edge(UP)
        self.play(Write(head)); self.wait(1)
        given = Tex(r"Graph of $\frac{1}{a}$ versus $m$ (constant net force), gradient $= 2$").scale(0.75).shift(UP * 1.8)
        self.play(Write(given)); self.wait(2)
        s1 = MathTex(r"F_{net} = ma \;\Rightarrow\; \frac{1}{a} = \frac{1}{F_{net}} \cdot m").shift(UP * 0.6)
        self.play(Write(s1)); self.wait(2)
        s2 = MathTex(r"\text{gradient} = \frac{1}{F_{net}} = \frac{2{,}5 - 0}{1{,}25 - 0} = 2").shift(DOWN * 0.6)
        self.play(Write(s2)); self.wait(2)
        ans = MathTex(r"F_{net} = \frac{1}{2} = 0{,}5\ \text{N}").shift(DOWN * 1.9)
        self.play(Write(ans)); self.wait(3)
