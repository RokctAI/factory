from manim import *

# Auto-generated past-paper worked example.
# Source: DBE Grade 11 Physical Sciences P1, November 2018, Q4.1
# (c) Department of Basic Education, 2018.
class PastPaperWorkedExample(Scene):
    def construct(self):
        head = Tex(r"Past paper: DBE Nov 2018 P1 Q4.1").to_edge(UP)
        self.play(Write(head)); self.wait(1)
        ask = Tex(r"State Newton's Second Law of Motion in words. (2)").scale(0.8).shift(UP * 1.5)
        self.play(Write(ask)); self.wait(2)
        l1 = Tex(r"When a \textbf{net force} acts on an object, the object").scale(0.7)
        l2 = Tex(r"\textbf{accelerates} in the \textbf{direction of the force}.").scale(0.7).shift(DOWN * 0.5)
        l3 = Tex(r"The acceleration is \textbf{directly proportional to the net force}").scale(0.7).shift(DOWN * 1.2)
        l4 = Tex(r"and \textbf{inversely proportional to the mass}.").scale(0.7).shift(DOWN * 1.7)
        for l in (l1, l2, l3, l4):
            self.play(Write(l)); self.wait(1)
        warn = Tex(r"Memo: $-1$ mark if a key phrase is missing.").scale(0.6).shift(DOWN * 2.8)
        self.play(Write(warn)); self.wait(3)
