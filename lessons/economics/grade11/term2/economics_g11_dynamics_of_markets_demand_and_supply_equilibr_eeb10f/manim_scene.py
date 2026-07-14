from manim import *

class EconomicsEquilibriumScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)

        # Title
        title = Text("Demand and Supply Equilibrium", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"color": BLACK, "include_numbers": False},
            x_length=6,
            y_length=6,
        ).shift(DOWN * 0.5)

        x_label = Text("Quantity (kg)", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("Price (R)", font_size=24).next_to(axes.y_axis, UP)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(2)

        # Demand Curve 1
        d1_curve = axes.plot(lambda x: 8 - 0.7 * x, x_range=[1, 9], color=BLUE)
        d1_label = Text("D1", font_size=24, color=BLUE).next_to(d1_curve.points[-1], RIGHT)

        self.play(Create(d1_curve))
        self.play(Write(d1_label))
        self.wait(2)

        # Supply Curve 1
        s1_curve = axes.plot(lambda x: 1 + 0.7 * x, x_range=[1, 9], color=RED)
        s1_label = Text("S1", font_size=24, color=RED).next_to(s1_curve.points[-1], RIGHT)

        self.play(Create(s1_curve))
        self.play(Write(s1_label))
        self.wait(2)

        # Initial Equilibrium E1
        e1_dot = Dot(axes.c2p(5, 4.5), color=BLACK)
        e1_label = Text("E1", font_size=24).next_to(e1_dot, UP)

        self.play(Create(e1_dot), Write(e1_label))
        self.wait(1)

        # Dashed lines for initial price and quantity
        p1_line = DashedLine(axes.c2p(0, 4.5), axes.c2p(5, 4.5), color=GRAY)
        q1_line = DashedLine(axes.c2p(5, 0), axes.c2p(5, 4.5), color=GRAY)

        p1_label = MathTex(r"P_1", font_size=30).next_to(axes.c2p(0, 4.5), LEFT)
        q1_label = MathTex(r"Q_1", font_size=30).next_to(axes.c2p(5, 0), DOWN)

        self.play(Create(p1_line), Create(q1_line))
        self.play(Write(p1_label), Write(q1_label))
        self.wait(3)

        # Shift in Demand (Income increases)
        d2_curve = axes.plot(lambda x: 10 - 0.7 * x, x_range=[1, 9], color=BLUE)
        d2_label = Text("D2", font_size=24, color=BLUE).next_to(d2_curve.points[-1], RIGHT)

        shift_arrow = Arrow(axes.c2p(6, 3.8), axes.c2p(7.5, 3.8), color=BLUE, buff=0)

        self.play(Create(shift_arrow))
        self.play(Create(d2_curve))
        self.play(Write(d2_label))
        self.wait(2)

        # New Equilibrium E2
        # Intersection: 10 - 0.7x = 1 + 0.7x -> 1.4x = 9 -> x = 6.42, y = 5.5
        e2_dot = Dot(axes.c2p(6.42, 5.5), color=BLACK)
        e2_label = Text("E2", font_size=24).next_to(e2_dot, UP)

        self.play(Create(e2_dot), Write(e2_label))
        self.wait(1)

        # Dashed lines for new price and quantity
        p2_line = DashedLine(axes.c2p(0, 5.5), axes.c2p(6.42, 5.5), color=GRAY)
        q2_line = DashedLine(axes.c2p(6.42, 0), axes.c2p(6.42, 5.5), color=GRAY)

        p2_label = MathTex(r"P_2", font_size=30).next_to(axes.c2p(0, 5.5), LEFT)
        q2_label = MathTex(r"Q_2", font_size=30).next_to(axes.c2p(6.42, 0), DOWN)

        self.play(Create(p2_line), Create(q2_line))
        self.play(Write(p2_label), Write(q2_label))
        self.wait(3)

        # Highlight Changes
        price_arrow = Arrow(axes.c2p(0, 4.5), axes.c2p(0, 5.5), color=GREEN, buff=0.1).shift(LEFT*0.5)
        quant_arrow = Arrow(axes.c2p(5, 0), axes.c2p(6.42, 0), color=GREEN, buff=0.1).shift(DOWN*0.5)

        self.play(Create(price_arrow), Create(quant_arrow))
        self.wait(3)

        # Clear screen for signoff
        self.play(FadeOut(Group(
            axes, x_label, y_label,
            d1_curve, d1_label, s1_curve, s1_label,
            e1_dot, e1_label, p1_line, q1_line, p1_label, q1_label,
            d2_curve, d2_label, shift_arrow,
            e2_dot, e2_label, p2_line, q2_line, p2_label, q2_label,
            price_arrow, quant_arrow
        )))

        summary = Text("Higher Equilibrium Price\nHigher Equilibrium Quantity", font_size=32).move_to(ORIGIN)
        self.play(Write(summary))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(summary))
        self.wait(1)
