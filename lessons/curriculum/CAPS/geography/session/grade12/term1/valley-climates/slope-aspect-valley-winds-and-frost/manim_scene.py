from manim import *

# Band-layout whiteboard scene for the valley-climates session duo
# (slope aspect, valley winds and frost). Exporter-safe primitives only
# (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/VGroup); add-only lifecycle;
# the camera moves down one frame-height per band. Valley cross-sections
# are hand-built V-profiles from Line pairs, winds are straight Arrows,
# labels are Tex — assembled element by element in script order.
#
# Subtopic shares (subtopics.json, total 1550 s):
# 225/235/240/250 expert, 195/195/210 simplifier. Bands 0-7 = Part 1
# (two per expert subtopic), bands 8-10 = fresh Part 2 bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ValleyClimatesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): aspect — the Southern Hemisphere geometry ---
        title = Tex("Slope Aspect: Which Side Gets the Sun").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        a1 = Tex(r"Aspect = the direction a slope faces").scale(1.05).shift(UP * 1.3)
        self.play(Write(a1))
        self.wait(2)
        # East-west valley cross-section: two slopes, sun in the NORTHERN sky
        slope_l = Line(LEFT * 5.0 + UP * 0.3, DOWN * 2.2, color=WHITE, stroke_width=5)
        slope_r = Line(DOWN * 2.2, RIGHT * 5.0 + UP * 0.3, color=WHITE, stroke_width=5)
        self.play(Create(slope_l), Create(slope_r))
        self.wait(1.5)
        sun = Circle(radius=0.4, color=YELLOW).shift(RIGHT * 4.6 + UP * 2.6)
        sun_lab = Tex(r"midday sun: NORTH sky").scale(0.85).shift(RIGHT * 2.2 + UP * 3.0)
        self.play(Create(sun), Write(sun_lab))
        self.wait(1.5)
        ray1 = Arrow(RIGHT * 4.2 + UP * 2.3, LEFT * 2.6 + DOWN * 0.7, buff=0, color=YELLOW)
        self.play(Create(ray1))
        self.wait(1.5)
        lab_n = Tex(r"north-facing: high angle, WARM").scale(0.9).shift(LEFT * 3.1 + DOWN * 2.6)
        lab_s = Tex(r"south-facing: glancing, COOL").scale(0.9).shift(RIGHT * 3.3 + DOWN * 2.6)
        self.play(Write(lab_n))
        self.wait(2)
        self.play(Write(lab_s))
        self.wait(3)

        # --- Band 1 (subtopic_1): consequences + precision points ---
        self.next_band(1)
        b1_t = Tex("Reading the two walls").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        c1 = Tex(r"North-facing: dry, grassy, snow melts first,").scale(1.0).shift(band_shift(1) + UP * 1.2)
        c1b = Tex(r"vineyards and peach orchards").scale(1.0).shift(band_shift(1) + UP * 0.4)
        c2 = Tex(r"South-facing: damp, green, forest in kloofs,").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        c2b = Tex(r"timber and dairy pasture").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(c1))
        self.play(Write(c1b))
        self.wait(2.5)
        self.play(Write(c2))
        self.play(Write(c2b))
        self.wait(2.5)
        c3 = Tex(r"Contrast greatest: in WINTER, in E--W valleys").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(c3))
        self.play(Create(SurroundingRectangle(c3, color=GREEN)))
        self.wait(2)
        c4 = Tex(r"Northern Hemisphere: the answer flips").scale(1.0).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(c4))
        self.wait(3)

        # --- Band 2 (subtopic_2): anabatic wind (day) ---
        self.next_band(2)
        b2_t = Tex("Day: the anabatic (upslope) wind").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        v2l = Line(band_shift(2) + LEFT * 5.0 + UP * 0.6, band_shift(2) + DOWN * 2.0,
                   color=WHITE, stroke_width=5)
        v2r = Line(band_shift(2) + DOWN * 2.0, band_shift(2) + RIGHT * 5.0 + UP * 0.6,
                   color=WHITE, stroke_width=5)
        self.play(Create(v2l), Create(v2r))
        self.wait(1)
        up_l = Arrow(band_shift(2) + LEFT * 1.6 + DOWN * 1.2,
                     band_shift(2) + LEFT * 3.8 + UP * 0.4, buff=0, color=RED)
        up_r = Arrow(band_shift(2) + RIGHT * 1.6 + DOWN * 1.2,
                     band_shift(2) + RIGHT * 3.8 + UP * 0.4, buff=0, color=RED)
        self.play(Create(up_l), Create(up_r))
        self.wait(1.5)
        an1 = Tex(r"Sun heats the SIDES; warm air slides up").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(an1))
        self.wait(2)
        an2 = Tex(r"Anabatic ascends — both start with A").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(an2))
        self.play(Create(SurroundingRectangle(an2, color=GREEN)))
        self.wait(2)
        an3 = Tex(r"Rising air builds cumulus on the ridges").scale(0.95).shift(band_shift(2) + DOWN * 3.4)
        self.play(Write(an3))
        self.wait(3)

        # --- Band 3 (subtopic_2): katabatic wind (night) + pooling ---
        self.next_band(3)
        b3_t = Tex("Night: the katabatic (drainage) wind").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        v3l = Line(band_shift(3) + LEFT * 5.0 + UP * 0.6, band_shift(3) + DOWN * 2.0,
                   color=WHITE, stroke_width=5)
        v3r = Line(band_shift(3) + DOWN * 2.0, band_shift(3) + RIGHT * 5.0 + UP * 0.6,
                   color=WHITE, stroke_width=5)
        self.play(Create(v3l), Create(v3r))
        self.wait(1)
        dn_l = Arrow(band_shift(3) + LEFT * 3.8 + UP * 0.3,
                     band_shift(3) + LEFT * 1.2 + DOWN * 1.5, buff=0, color=BLUE)
        dn_r = Arrow(band_shift(3) + RIGHT * 3.8 + UP * 0.3,
                     band_shift(3) + RIGHT * 1.2 + DOWN * 1.5, buff=0, color=BLUE)
        self.play(Create(dn_l), Create(dn_r))
        self.wait(1.5)
        k1 = Tex(r"Slopes radiate heat away; cold dense air").scale(1.0).shift(band_shift(3) + UP * 1.3)
        k1b = Tex(r"slides downhill under gravity").scale(1.0).shift(band_shift(3) + UP * 0.6)
        self.play(Write(k1))
        self.play(Write(k1b))
        self.wait(2.5)
        pool = Rectangle(width=3.2, height=0.7, color=BLUE).shift(band_shift(3) + DOWN * 1.9)
        pool_lab = Tex(r"cold air POOLS on the floor").scale(0.9).shift(band_shift(3) + DOWN * 2.9)
        self.play(Create(pool))
        self.play(Write(pool_lab))
        self.wait(2)
        k2 = Tex(r"Strongest: clear, calm winter nights").scale(0.95).shift(band_shift(3) + DOWN * 3.5)
        self.play(Write(k2))
        self.wait(3)

        # --- Band 4 (subtopic_3): the inversion and the thermal belt ---
        self.next_band(4)
        b4_t = Tex("One clear winter night, layer by layer").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        v4l = Line(band_shift(4) + LEFT * 5.0 + UP * 1.0, band_shift(4) + DOWN * 2.4,
                   color=WHITE, stroke_width=5)
        v4r = Line(band_shift(4) + DOWN * 2.4, band_shift(4) + RIGHT * 5.0 + UP * 1.0,
                   color=WHITE, stroke_width=5)
        self.play(Create(v4l), Create(v4r))
        self.wait(1)
        cold = Rectangle(width=4.0, height=1.0, color=BLUE).shift(band_shift(4) + DOWN * 2.0)
        cold_lab = Tex(r"floor: coldest, below zero").scale(0.9).shift(band_shift(4) + DOWN * 3.1)
        self.play(Create(cold), Write(cold_lab))
        self.wait(2)
        belt_l = Dot(band_shift(4) + LEFT * 3.2 + UP * 0.0, color=GREEN)
        belt_r = Dot(band_shift(4) + RIGHT * 3.2 + UP * 0.0, color=GREEN)
        belt_lab = Tex(r"THERMAL BELT: warm mid-slope shelf").scale(0.95).shift(band_shift(4) + UP * 0.6)
        self.play(Create(belt_l), Create(belt_r))
        self.play(Write(belt_lab))
        self.wait(2)
        inv = Tex(r"Cold below warm = temperature INVERSION").scale(1.0).shift(band_shift(4) + UP * 1.4)
        self.play(Write(inv))
        self.play(Create(SurroundingRectangle(inv, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): frost pocket, radiation fog, smoke trap ---
        self.next_band(5)
        b5_t = Tex("What the cold pond breeds").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        h1 = Tex(r"Frost pocket: ponded air below $0^\circ$C —").scale(1.0).shift(band_shift(5) + UP * 1.2)
        h1b = Tex(r"floor whitens, mid-slope stays frost-free").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(h1))
        self.play(Write(h1b))
        self.wait(2.5)
        h2 = Tex(r"Radiation fog: cool moist air to dew point —").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        h2b = Tex(r"thickest at dawn, burns off from the top").scale(1.0).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(h2))
        self.play(Write(h2b))
        self.wait(2.5)
        h3 = Tex(r"Inversion lid traps smoke and dust —").scale(1.0).shift(band_shift(5) + DOWN * 2.2)
        h3b = Tex(r"valley towns wear grey winter blankets").scale(1.0).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(h3))
        self.play(Write(h3b))
        self.wait(3)

        # --- Band 6 (subtopic_4): farming the physics ---
        self.next_band(6)
        b6_t = Tex("Farming: map the crops onto the physics").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        f1 = Tex(r"Frost-sensitive fruit + vines $\rightarrow$ THERMAL BELT").scale(0.95).shift(band_shift(6) + UP * 1.2)
        f2 = Tex(r"(Hex River, Elgin: orchards stripe mid-slope)").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(f1))
        self.play(Write(f2))
        self.wait(2.5)
        f3 = Tex(r"Floor trap: one June frost kills the blossom").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(f3))
        self.play(Create(strike(f3)))
        self.wait(2)
        f4 = Tex(r"Hardy crops (pasture, lucerne) take the floor").scale(0.95).shift(band_shift(6) + DOWN * 1.4)
        f5 = Tex(r"Grapes: warm north wall; timber: south wall").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(f4))
        self.wait(2)
        self.play(Write(f5))
        self.wait(2)
        f6 = Tex(r"Frost fight: wind machines stir the inversion").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(f6))
        self.wait(3)

        # --- Band 7 (subtopic_4): settlement and planning ---
        self.next_band(7)
        b7_t = Tex("Settlement and sensible planning").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        s1 = Tex(r"Farmhouses + old towns: lower slopes, above").scale(1.0).shift(band_shift(7) + UP * 1.2)
        s1b = Tex(r"flood line and frost — on the thermal belt").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2.5)
        s2 = Tex(r"Roads + rail: flat floor, accept the fog risk").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(s2))
        self.wait(2)
        s3 = Tex(r"Failure: low-cost housing on the valley floor —").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        s3b = Tex(r"coldest, foggiest, flood- and smoke-trapped").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(s3))
        self.play(Write(s3b))
        self.wait(2.5)
        s4 = Tex(r"Fix: homes mid-slope, industry out of the pond").scale(0.95).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(s4))
        self.play(Create(SurroundingRectangle(s4, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the sunny wall and the shady wall ---
        self.next_band(8)
        b8_t = Tex("The sunny wall and the shady wall").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        p1 = Tex(r"SA midday sun hangs in the NORTHERN sky").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(p1))
        self.wait(2)
        p2 = Tex(r"Palm flat to the heater = north-facing slope").scale(1.0).shift(band_shift(8) + UP * 0.4)
        p3 = Tex(r"Palm edge-on = south-facing slope").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(p2))
        self.wait(2)
        self.play(Write(p3))
        self.wait(2)
        p4 = Tex(r"Braai side: warm, dry, vines and grass").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        p5 = Tex(r"Fridge side: cool, damp, forest and snow").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(p4))
        self.wait(2)
        self.play(Write(p5))
        self.wait(2)
        p6 = Tex(r"Biggest gap in winter; flips in the north").scale(1.0).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(p6))
        self.play(Create(SurroundingRectangle(p6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the bathtub of cold air ---
        self.next_band(9)
        b9_t = Tex("The bathtub that fills with cold air").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        v9l = Line(band_shift(9) + LEFT * 4.6 + UP * 1.0, band_shift(9) + DOWN * 1.8,
                   color=WHITE, stroke_width=5)
        v9r = Line(band_shift(9) + DOWN * 1.8, band_shift(9) + RIGHT * 4.6 + UP * 1.0,
                   color=WHITE, stroke_width=5)
        self.play(Create(v9l), Create(v9r))
        self.wait(1)
        t1 = Arrow(band_shift(9) + LEFT * 3.4 + UP * 0.6,
                   band_shift(9) + LEFT * 1.0 + DOWN * 1.1, buff=0, color=BLUE)
        t2 = Arrow(band_shift(9) + RIGHT * 3.4 + UP * 0.6,
                   band_shift(9) + RIGHT * 1.0 + DOWN * 1.1, buff=0, color=BLUE)
        tub = Rectangle(width=3.0, height=0.8, color=BLUE).shift(band_shift(9) + DOWN * 1.5)
        self.play(Create(t1), Create(t2))
        self.play(Create(tub))
        self.wait(1.5)
        q1 = Tex(r"Two taps, one tub: cold air pours in all night").scale(0.95).shift(band_shift(9) + UP * 1.3)
        self.play(Write(q1))
        self.wait(2)
        q2 = Tex(r"Day: anabatic UP; night: katabatic DOWN").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(q2))
        self.play(Create(SurroundingRectangle(q2, color=GREEN)))
        self.wait(2)
        q3 = Tex(r"Warm shelf above the water line = thermal belt").scale(0.95).shift(band_shift(9) + DOWN * 3.3)
        self.play(Write(q3))
        self.wait(3)

        # --- Band 10 (subtopic_7): frost on the floor, money on the shelf ---
        self.next_band(10)
        b10_t = Tex("Frost on the floor, money on the shelf").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        r1 = Tex(r"Tub below zero = frost pocket (freezer)").scale(1.0).shift(band_shift(10) + UP * 1.2)
        r2 = Tex(r"Moist tub cooled = radiation fog at dawn").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex(r"Money (fruit, vines, houses) $\rightarrow$ the SHELF").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(r3))
        self.play(Create(SurroundingRectangle(r3, color=GREEN)))
        self.wait(2)
        r4 = Tex(r"Floor: hardy crops, roads — and the fog").scale(1.0).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(r4))
        self.wait(2)
        r5 = Tex(r"Tragedy: cheap housing in the cold, smoky tub").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        r6 = Tex(r"Fix: homes on the belt; fans stir the tub").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(r5))
        self.wait(2)
        self.play(Write(r6))
        self.wait(4)
