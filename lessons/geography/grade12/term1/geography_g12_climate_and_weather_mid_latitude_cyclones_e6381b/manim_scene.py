from manim import *

class MidLatitudeCyclone(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Title
        title = Text("Mid-Latitude Cyclone Stages", color=BLACK, font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Common elements setup
        equator_text = Text("Warm Air (Tropics)", color=RED, font_size=24).to_edge(UP, buff=1.5)
        polar_text = Text("Cold Air (Antarctica)", color=BLUE, font_size=24).to_edge(DOWN, buff=1.5)

        # 1. Initial Stage
        initial_title = Text("Initial Stage", color=BLACK, font_size=30).next_to(title, DOWN)
        self.play(Write(initial_title))

        polar_front = Line(LEFT*4, RIGHT*4, color=BLACK, stroke_width=4)
        front_label = Text("Polar Front", color=BLACK, font_size=20).next_to(polar_front, DOWN, buff=0.2)

        warm_arrow1 = Arrow(LEFT*3 + UP*0.5, RIGHT*3 + UP*0.5, color=RED, buff=0)
        warm_arrow2 = Arrow(LEFT*3 + UP*1.0, RIGHT*3 + UP*1.0, color=RED, buff=0)

        cold_arrow1 = Arrow(RIGHT*3 + DOWN*0.5, LEFT*3 + DOWN*0.5, color=BLUE, buff=0)
        cold_arrow2 = Arrow(RIGHT*3 + DOWN*1.0, LEFT*3 + DOWN*1.0, color=BLUE, buff=0)

        self.play(FadeIn(equator_text), FadeIn(polar_text))
        self.play(Create(polar_front), Write(front_label))
        self.play(GrowArrow(warm_arrow1), GrowArrow(warm_arrow2))
        self.play(GrowArrow(cold_arrow1), GrowArrow(cold_arrow2))
        self.wait(2)

        # Clean up for next stage
        self.play(FadeOut(warm_arrow1), FadeOut(warm_arrow2), FadeOut(cold_arrow1), FadeOut(cold_arrow2),
                  FadeOut(polar_front), FadeOut(front_label), FadeOut(initial_title))

        # 2. Wave Stage
        wave_title = Text("Wave Stage", color=BLACK, font_size=30).next_to(title, DOWN)
        self.play(Write(wave_title))

        # Draw the wave
        wave_path = VMobject(color=BLACK, stroke_width=4)
        wave_path.set_points_smoothly([LEFT*4, LEFT*1.5 + DOWN*0.5, RIGHT*0.5 + UP*1.5, RIGHT*4])

        low_pressure = Text("L", color=RED, font_size=40).move_to(RIGHT*0.5 + UP*1.5 + UP*0.5)

        # Curved arrows to show clockwise rotation
        warm_curve = CurvedArrow(LEFT*2 + UP*0.5, RIGHT*1.5 + UP*2, color=RED, angle=-PI/2)
        cold_curve = CurvedArrow(RIGHT*1 + DOWN*0.5, LEFT*2 + DOWN*1.5, color=BLUE, angle=-PI/2)

        self.play(Create(wave_path))
        self.play(Write(low_pressure))
        self.play(GrowArrow(warm_curve), GrowArrow(cold_curve))
        self.wait(2)

        self.play(FadeOut(wave_path), FadeOut(low_pressure), FadeOut(warm_curve), FadeOut(cold_curve), FadeOut(wave_title))

        # 3. Mature Stage
        mature_title = Text("Mature Stage", color=BLACK, font_size=30).next_to(title, DOWN)
        self.play(Write(mature_title))

        low_pressure_mature = Text("L", color=RED, font_size=40).move_to(UP*2)

        # Cold front (blue triangles)
        cold_front_line = Line(UP*1.5, LEFT*3 + DOWN*2, color=BLUE, stroke_width=4)
        tri1 = Polygon(LEFT*0.5 + UP*0.5, LEFT*1.5 + UP*0.5, LEFT*1 + UP*1.5, color=BLUE, fill_opacity=1).scale(0.3).move_to(LEFT*0.5 + UP*0.5)
        tri2 = Polygon(LEFT*0.5 + UP*0.5, LEFT*1.5 + UP*0.5, LEFT*1 + UP*1.5, color=BLUE, fill_opacity=1).scale(0.3).move_to(LEFT*1.5 + DOWN*0.5)
        tri3 = Polygon(LEFT*0.5 + UP*0.5, LEFT*1.5 + UP*0.5, LEFT*1 + UP*1.5, color=BLUE, fill_opacity=1).scale(0.3).move_to(LEFT*2.5 + DOWN*1.5)
        # Rotate triangles to point outward
        for tri in [tri1, tri2, tri3]:
            tri.rotate(PI/4)

        cold_front_group = VGroup(cold_front_line, tri1, tri2, tri3)

        # Warm front (red semicircles)
        warm_front_line = Line(UP*1.5, RIGHT*3 + DOWN*1, color=RED, stroke_width=4)
        semi1 = Arc(radius=0.3, start_angle=0, angle=PI, color=RED, fill_opacity=1).move_to(RIGHT*0.5 + UP*1)
        semi2 = Arc(radius=0.3, start_angle=0, angle=PI, color=RED, fill_opacity=1).move_to(RIGHT*1.5 + UP*0.2)
        semi3 = Arc(radius=0.3, start_angle=0, angle=PI, color=RED, fill_opacity=1).move_to(RIGHT*2.5 + DOWN*0.6)
        # Rotate semicircles
        for semi in [semi1, semi2, semi3]:
            semi.rotate(-PI/4)

        warm_front_group = VGroup(warm_front_line, semi1, semi2, semi3)

        # Warm sector and cold sector labels
        warm_sector = Text("Warm Sector", color=RED, font_size=24).move_to(DOWN*1)
        cold_sector = Text("Cold Sector", color=BLUE, font_size=24).move_to(LEFT*3 + UP*2)

        self.play(Write(low_pressure_mature))
        self.play(Create(cold_front_group))
        self.play(Create(warm_front_group))
        self.play(Write(warm_sector), Write(cold_sector))
        self.wait(2)

        # Animate cold front catching up
        self.play(
            cold_front_group.animate.move_to(LEFT*1 + DOWN*0.5),
            warm_sector.animate.shift(RIGHT*1 + UP*1).scale(0.5).set_opacity(0.5),
            run_time=2
        )
        self.wait(1)

        self.play(FadeOut(cold_front_group), FadeOut(warm_front_group), FadeOut(low_pressure_mature),
                  FadeOut(warm_sector), FadeOut(cold_sector), FadeOut(mature_title))

        # 4. Occluded Stage
        occluded_title = Text("Occluded Stage", color=BLACK, font_size=30).next_to(title, DOWN)
        self.play(Write(occluded_title))

        low_pressure_occluded = Text("L", color=RED, font_size=40).move_to(UP*2)

        # Occluded front (purple with alternating triangles and semicircles)
        occluded_front_line = Line(UP*1.5, DOWN*2, color=PURPLE, stroke_width=4)

        p_tri1 = Polygon(LEFT*0.5, RIGHT*0.5, UP*0.5, color=PURPLE, fill_opacity=1).scale(0.4).move_to(UP*0.5 + RIGHT*0.2).rotate(-PI/2)
        p_semi1 = Arc(radius=0.2, start_angle=0, angle=PI, color=PURPLE, fill_opacity=1).move_to(DOWN*0.5 + RIGHT*0.2).rotate(-PI/2)
        p_tri2 = Polygon(LEFT*0.5, RIGHT*0.5, UP*0.5, color=PURPLE, fill_opacity=1).scale(0.4).move_to(DOWN*1.5 + RIGHT*0.2).rotate(-PI/2)

        occluded_group = VGroup(occluded_front_line, p_tri1, p_semi1, p_tri2)

        warm_air_lifted = Text("Warm Air Lifted", color=RED, font_size=20).move_to(UP*2 + RIGHT*2)
        arrow_up = Arrow(DOWN*0.5, UP*1.5, color=RED).next_to(warm_air_lifted, LEFT)

        self.play(Write(low_pressure_occluded))
        self.play(Create(occluded_group))
        self.play(Write(warm_air_lifted), GrowArrow(arrow_up))
        self.wait(2)

        self.play(FadeOut(occluded_group), FadeOut(low_pressure_occluded), FadeOut(warm_air_lifted), FadeOut(arrow_up), FadeOut(occluded_title), FadeOut(equator_text), FadeOut(polar_text))

        # 5. Western Cape map simplified
        wc_title = Text("Western Cape Influence", color=BLACK, font_size=30).next_to(title, DOWN)
        self.play(Write(wc_title))

        # Simplified South Africa coast
        sa_coast = VMobject(color=BLACK, stroke_width=4)
        sa_coast.set_points_smoothly([RIGHT*3 + UP*2, RIGHT*2 + DOWN*1, LEFT*1 + DOWN*2, LEFT*2 + UP*1])
        sa_label = Text("South Africa", color=BLACK, font_size=24).move_to(RIGHT*1 + UP*1)
        wc_label = Text("Western Cape", color=BLACK, font_size=20).move_to(LEFT*0.5 + DOWN*1.5)

        # Cold front approaching from left
        cf_line = Line(UP*1, DOWN*3, color=BLUE, stroke_width=4).move_to(LEFT*4 + DOWN*1)
        cf_tri = Polygon(LEFT*0.5, RIGHT*0.5, UP*0.5, color=BLUE, fill_opacity=1).scale(0.4).move_to(LEFT*3.8 + DOWN*1).rotate(-PI/2)
        cf_group = VGroup(cf_line, cf_tri)

        westerly_wind = Arrow(LEFT*5 + DOWN*2, LEFT*3 + DOWN*2, color=GRAY)
        westerly_label = Text("Westerlies", color=GRAY, font_size=20).next_to(westerly_wind, UP, buff=0.1)

        self.play(Create(sa_coast), Write(sa_label), Write(wc_label))
        self.play(Create(cf_group), GrowArrow(westerly_wind), Write(westerly_label))

        # Animate movement
        self.play(
            cf_group.animate.move_to(LEFT*1.5 + DOWN*1),
            run_time=2
        )

        # Rain
        rain_lines = VGroup(*[Line(UP*0.2, DOWN*0.2, color=BLUE, stroke_width=2).move_to(LEFT*1 + DOWN*1.5 + RIGHT*(i*0.3) + UP*np.random.uniform(-0.5, 0.5)) for i in range(5)])
        self.play(Create(rain_lines))

        self.wait(3)
