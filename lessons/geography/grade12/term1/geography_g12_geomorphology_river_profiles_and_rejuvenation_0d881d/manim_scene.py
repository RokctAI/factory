from manim import *

class GeographyLesson(Scene):
    def construct(self):
        # Setup title
        title = Text("River Profiles and Rejuvenation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # -- Subtopic: Introduction to River Profiles --
        intro_text_long = Text("Longitudinal Profile", font_size=24).shift(UP*2)
        intro_text_trans = Text("Transverse Profile", font_size=24).shift(DOWN*1)
        self.play(Write(intro_text_long))

        axes_long = Axes(x_range=[0, 10, 1], y_range=[0, 10, 1], x_length=6, y_length=3).next_to(intro_text_long, DOWN)
        axes_labels_long = axes_long.get_axis_labels(x_label="Distance", y_label="Elevation")
        long_profile_curve = axes_long.plot(lambda x: 8 * (0.8 ** x), color=BLUE)
        self.play(Create(axes_long), Create(axes_labels_long))
        self.play(Create(long_profile_curve))
        self.wait(2)

        self.play(Write(intro_text_trans))
        axes_trans = Axes(x_range=[0, 10, 1], y_range=[0, 10, 1], x_length=6, y_length=2).next_to(intro_text_trans, DOWN)
        trans_profile_curve = axes_trans.plot(lambda x: 4 * (x - 5)**2 / 25, x_range=[0, 10], color=BLUE)
        self.play(Create(axes_trans))
        self.play(Create(trans_profile_curve))
        self.wait(2)

        base_level_text = Text("Base Level = Sea Level", font_size=20, color=YELLOW).next_to(axes_long, RIGHT)
        self.play(Write(base_level_text))
        self.wait(2)

        self.play(FadeOut(intro_text_long, intro_text_trans, axes_long, axes_labels_long, long_profile_curve, axes_trans, trans_profile_curve, base_level_text))

        # -- Subtopic: Graded vs Ungraded River Profiles --
        graded_text = Text("Graded Profile (Dynamic Equilibrium)", font_size=28).shift(UP*2)
        axes_graded = Axes(x_range=[0, 10, 1], y_range=[0, 10, 1], x_length=8, y_length=4).next_to(graded_text, DOWN)
        graded_curve = axes_graded.plot(lambda x: 8 * (0.75 ** x), color=GREEN)
        self.play(Write(graded_text))
        self.play(Create(axes_graded), Create(graded_curve))
        self.wait(2)

        self.play(FadeOut(graded_text, graded_curve))
        ungraded_text = Text("Ungraded Profile", font_size=28).shift(UP*2)
        self.play(Write(ungraded_text))

        # Create an ungraded profile with knickpoints
        points = [(0, 8), (2, 7), (2.5, 5), (5, 4), (5.5, 2), (10, 0)]
        ungraded_curve = VMobject(color=RED)
        ungraded_curve.set_points_as_corners([axes_graded.c2p(x, y) for x, y in points])
        self.play(Create(ungraded_curve))

        knickpoint_labels = VGroup(
            Text("Knickpoint (Waterfall)", font_size=18).next_to(axes_graded.c2p(2.5, 6), RIGHT),
            Text("Knickpoint (Rapids)", font_size=18).next_to(axes_graded.c2p(5.5, 3), RIGHT)
        )
        self.play(Write(knickpoint_labels))
        self.wait(2)

        self.play(FadeOut(ungraded_text, axes_graded, ungraded_curve, knickpoint_labels))

        # -- Subtopic: The Process of River Rejuvenation & Constructing the Diagram --
        rejuv_text = Text("River Rejuvenation", font_size=28).shift(UP*3)
        self.play(Write(rejuv_text))

        # Cross-section
        # Initial broad flood plain
        initial_plain = VMobject(color=WHITE)
        initial_points = [(-4, 1), (-2, 0), (2, 0), (4, 1)]
        initial_plain.set_points_smoothly([axes_graded.c2p(x+5, y+3) for x, y in initial_points]) # Offset roughly center

        # Need coordinates mapped to screen space directly for easier cross section
        initial_plain = VMobject(color=WHITE)
        initial_plain.set_points_as_corners([
            [-4, 1, 0], [-2, 0, 0], [2, 0, 0], [4, 1, 0]
        ])

        self.play(Create(initial_plain))
        floodplain_label = Text("Broad Flood Plain", font_size=20).next_to(initial_plain, UP)
        self.play(Write(floodplain_label))
        self.wait(2)

        # New base level
        new_base_level = DashedLine(start=[-4, -2, 0], end=[4, -2, 0], color=BLUE)
        base_level_label = Text("New Base Level (Uplift/Eustatic drop)", font_size=18, color=BLUE).next_to(new_base_level, DOWN)
        self.play(Create(new_base_level), Write(base_level_label))
        self.wait(2)

        # Rejuvenated profile cutting down
        rejuv_profile = VMobject(color=RED)
        rejuv_points = [
            [-4, 1, 0], [-2, 0, 0], # old terrace
            [-1.5, -1.5, 0], [1.5, -1.5, 0], # steep new gorge
            [2, 0, 0], [4, 1, 0] # old terrace
        ]
        rejuv_profile.set_points_as_corners(rejuv_points)

        self.play(Transform(initial_plain, rejuv_profile))
        self.wait(2)

        # Labels
        terrace_label1 = Text("River Terrace", font_size=16, color=YELLOW).next_to([-3, 0, 0], UP)
        terrace_label2 = Text("River Terrace", font_size=16, color=YELLOW).next_to([3, 0, 0], UP)
        incised_label = Text("Incised / Entrenched Meander", font_size=16, color=GREEN).next_to([0, -1.5, 0], UP)

        self.play(Write(terrace_label1), Write(terrace_label2))
        self.play(Write(incised_label))
        self.wait(3)

        self.play(FadeOut(initial_plain, floodplain_label, new_base_level, base_level_label, terrace_label1, terrace_label2, incised_label, rejuv_text, title))

        signoff = Text("Dr Molefe. Study well.", font_size=36)
        self.play(Write(signoff))
        self.wait(2)
