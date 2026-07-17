from manim import *

class CompletingTheSquare(Scene):
    def construct(self):
        # Setup title
        title = Text("Completing the Square", font_size=40)
        title.to_edge(UP)
        self.add(title)

        # Introduction and Importance - Empty board
        self.wait(3)

        # The Algorithm - Empty board for verbal explanation
        self.wait(3)

        # Applying the Method
        eq1 = MathTex(r"x^2 + 6x + 2 = 0")
        self.play(Write(eq1))
        self.wait(3)

        # Move constant
        eq2 = MathTex(r"x^2 + 6x = -2")
        self.play(Transform(eq1, eq2))
        self.wait(3)

        # The Critical Move
        # Halve the coefficient of x, square it, add to both sides
        # 6/2 = 3; 3^2 = 9
        eq3 = MathTex(r"x^2 + 6x + (3)^2 = -2 + (3)^2")
        self.play(Transform(eq1, eq3))
        self.wait(3)

        eq4 = MathTex(r"x^2 + 6x + 9 = -2 + 9")
        self.play(Transform(eq1, eq4))
        self.wait(2)

        eq5 = MathTex(r"x^2 + 6x + 9 = 7")
        self.play(Transform(eq1, eq5))
        self.wait(3)

        # Factorising and Solving
        eq6 = MathTex(r"(x + 3)^2 = 7")
        self.play(Transform(eq1, eq6))
        self.wait(4)

        eq7 = MathTex(r"x + 3 = \pm \sqrt{7}")
        self.play(Transform(eq1, eq7))
        self.wait(4)

        eq8 = MathTex(r"x = -3 \pm \sqrt{7}")
        self.play(Transform(eq1, eq8))
        self.wait(3)

        # Final solutions explicitly
        sol1 = MathTex(r"x = -3 + \sqrt{7}")
        sol1.shift(DOWN + LEFT * 2)
        sol2 = MathTex(r"\text{or } x = -3 - \sqrt{7}")
        sol2.next_to(sol1, RIGHT, buff=0.5)

        self.play(Write(sol1), Write(sol2))
        self.wait(5)
