from manim import *

# Band-layout whiteboard scene for the fluvial-processes duo on meanders,
# oxbow lakes and longitudinal profiles. Exporter-safe primitives only
# (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/VGroup); add-only lifecycle;
# camera moves down one frame-height per band. The longitudinal profile is
# a chained-Line concave curve, the meander bend is a chained-Line loop with
# Arrows for the fast/slow current — built element by element in script order.
#
# Subtopic shares (subtopics.json, total 1500 s):
# 240/230/230/235 expert, 200/185/180 simplifier. Bands 0-7 = Part 1
# (two per expert subtopic), bands 8-10 = fresh Part 2 bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MeandersOxbowProfilesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the graded longitudinal profile ---
        title = Tex("The Longitudinal Profile").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex(r"Side view of a river, source to mouth").scale(1.05).shift(UP * 1.4)
        self.play(Write(d1))
        self.wait(2)
        # Graded profile: smooth concave curve from chained lines
        g1 = Line(LEFT * 5.0 + UP * 0.6, LEFT * 2.6 + DOWN * 1.0, color=YELLOW, stroke_width=5)
        g2 = Line(LEFT * 2.6 + DOWN * 1.0, RIGHT * 0.4 + DOWN * 1.9, color=YELLOW, stroke_width=5)
        g3 = Line(RIGHT * 0.4 + DOWN * 1.9, RIGHT * 5.0 + DOWN * 2.3, color=YELLOW, stroke_width=5)
        src = Dot(LEFT * 5.0 + UP * 0.6, color=WHITE)
        src_lab = Tex(r"source").scale(0.85).shift(LEFT * 5.0 + UP * 1.1)
        mth = Dot(RIGHT * 5.0 + DOWN * 2.3, color=WHITE)
        mth_lab = Tex(r"mouth").scale(0.85).shift(RIGHT * 4.9 + DOWN * 1.8)
        self.play(Create(src), Write(src_lab))
        self.play(Create(g1))
        self.play(Create(g2))
        self.play(Create(g3))
        self.play(Create(mth), Write(mth_lab))
        self.wait(2)
        sea = DashedLine(LEFT * 5.2 + DOWN * 2.3, RIGHT * 5.2 + DOWN * 2.3, color=BLUE)
        sea_lab = Tex(r"sea = permanent base level").scale(0.9).shift(DOWN * 2.9 + LEFT * 2.4)
        self.play(Create(sea), Write(sea_lab))
        self.wait(2)
        gr = Tex(r"GRADED: smooth, concave, no steps").scale(0.95).shift(RIGHT * 2.2 + UP * 0.6)
        self.play(Write(gr))
        self.play(Create(SurroundingRectangle(gr, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): ungraded profile + cross-sections ---
        self.next_band(1)
        b1_t = Tex("Ungraded: the unfinished profile").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        # Ungraded: step (waterfall) and flat (dam)
        u1 = Line(band_shift(1) + LEFT * 5.0 + UP * 1.0, band_shift(1) + LEFT * 3.0 + UP * 0.2,
                  color=YELLOW, stroke_width=5)
        u2 = Line(band_shift(1) + LEFT * 3.0 + UP * 0.2, band_shift(1) + LEFT * 3.0 + DOWN * 0.9,
                  color=YELLOW, stroke_width=5)
        u3 = Line(band_shift(1) + LEFT * 3.0 + DOWN * 0.9, band_shift(1) + LEFT * 0.4 + DOWN * 0.9,
                  color=YELLOW, stroke_width=5)
        u4 = Line(band_shift(1) + LEFT * 0.4 + DOWN * 0.9, band_shift(1) + RIGHT * 4.8 + DOWN * 1.9,
                  color=YELLOW, stroke_width=5)
        wf_lab = Tex(r"waterfall (hard rock)").scale(0.85).shift(band_shift(1) + LEFT * 1.4 + UP * 0.6)
        dam_lab = Tex(r"dam: temporary base level").scale(0.85).shift(band_shift(1) + LEFT * 1.6 + DOWN * 1.5)
        self.play(Create(u1))
        self.play(Create(u2), Write(wf_lab))
        self.play(Create(u3), Write(dam_lab))
        self.play(Create(u4))
        self.wait(2.5)
        cs = Tex(r"Cross-sections: deep V near source (cuts down),").scale(0.95).shift(band_shift(1) + DOWN * 2.5)
        cs2 = Tex(r"wide flat floor near mouth (cuts sideways)").scale(0.95).shift(band_shift(1) + DOWN * 3.2)
        self.play(Write(cs))
        self.wait(2)
        self.play(Write(cs2))
        self.wait(3)

        # --- Band 2 (subtopic_2): the meander bend, two banks ---
        self.next_band(2)
        b2_t = Tex("A meander: two banks, two jobs").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        # Plan view of one bend: chained lines sweeping right
        m1 = Line(band_shift(2) + LEFT * 4.6 + DOWN * 2.2, band_shift(2) + LEFT * 2.6 + DOWN * 0.6,
                  color=BLUE, stroke_width=5)
        m2 = Line(band_shift(2) + LEFT * 2.6 + DOWN * 0.6, band_shift(2) + LEFT * 0.2 + UP * 0.2,
                  color=BLUE, stroke_width=5)
        m3 = Line(band_shift(2) + LEFT * 0.2 + UP * 0.2, band_shift(2) + RIGHT * 2.2 + DOWN * 0.6,
                  color=BLUE, stroke_width=5)
        m4 = Line(band_shift(2) + RIGHT * 2.2 + DOWN * 0.6, band_shift(2) + RIGHT * 4.2 + DOWN * 2.2,
                  color=BLUE, stroke_width=5)
        self.play(Create(m1), Create(m2))
        self.play(Create(m3), Create(m4))
        self.wait(1.5)
        fast = Arrow(band_shift(2) + LEFT * 1.6 + UP * 1.4, band_shift(2) + RIGHT * 1.4 + UP * 1.4,
                     buff=0, color=RED)
        fast_lab = Tex(r"outer bank: FAST — undercut slope").scale(0.9).shift(band_shift(2) + UP * 1.9)
        self.play(Create(fast), Write(fast_lab))
        self.wait(2)
        slow = Arrow(band_shift(2) + LEFT * 1.0 + DOWN * 1.4, band_shift(2) + RIGHT * 0.8 + DOWN * 1.4,
                     buff=0, color=GREEN)
        slow_lab = Tex(r"inner bank: SLOW — slip-off slope").scale(0.9).shift(band_shift(2) + DOWN * 2.0)
        self.play(Create(slow), Write(slow_lab))
        self.wait(2)
        sent = Tex(r"Fast erodes outside; slow deposits inside").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(sent))
        self.play(Create(SurroundingRectangle(sent, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): where meanders live + migration ---
        self.next_band(3)
        b3_t = Tex("Where the loops live, and how they move").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        w1 = Tex(r"Lower course: gentle gradient, big volume —").scale(1.0).shift(band_shift(3) + UP * 1.2)
        w1b = Tex(r"lateral erosion outweighs vertical").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(w1))
        self.play(Write(w1b))
        self.wait(2.5)
        w2 = Tex(r"Every flood: outer bank cut outward + downstream,").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        w2b = Tex(r"slip-off slope follows behind").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(w2))
        self.play(Write(w2b))
        self.wait(2.5)
        w3 = Tex(r"Loops grow, swing, migrate — planing the").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        w3b = Tex(r"valley sides into a wide floodplain").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(w3))
        self.play(Write(w3b))
        self.wait(3)

        # --- Band 4 (subtopic_3): neck narrows, flood breaks through ---
        self.next_band(4)
        b4_t = Tex("From meander to oxbow lake").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        # Tight loop with a narrow neck: two limbs converging
        limb1 = Line(band_shift(4) + LEFT * 4.4 + DOWN * 1.6, band_shift(4) + LEFT * 1.4 + UP * 0.2,
                     color=BLUE, stroke_width=5)
        limb2 = Line(band_shift(4) + LEFT * 1.4 + UP * 0.2, band_shift(4) + UP * 1.2,
                     color=BLUE, stroke_width=5)
        limb3 = Line(band_shift(4) + UP * 1.2, band_shift(4) + RIGHT * 1.4 + UP * 0.2,
                     color=BLUE, stroke_width=5)
        limb4 = Line(band_shift(4) + RIGHT * 1.4 + UP * 0.2, band_shift(4) + RIGHT * 4.4 + DOWN * 1.6,
                     color=BLUE, stroke_width=5)
        self.play(Create(limb1), Create(limb2))
        self.play(Create(limb3), Create(limb4))
        self.wait(1.5)
        neck_a1 = Arrow(band_shift(4) + LEFT * 2.6 + DOWN * 0.9, band_shift(4) + LEFT * 0.9 + DOWN * 0.7,
                        buff=0, color=RED)
        neck_a2 = Arrow(band_shift(4) + RIGHT * 2.6 + DOWN * 0.9, band_shift(4) + RIGHT * 0.9 + DOWN * 0.7,
                        buff=0, color=RED)
        neck_lab = Tex(r"erosion narrows the NECK from both sides").scale(0.9).shift(band_shift(4) + DOWN * 1.6)
        self.play(Create(neck_a1), Create(neck_a2))
        self.play(Write(neck_lab))
        self.wait(2.5)
        cut = Line(band_shift(4) + LEFT * 0.9 + DOWN * 0.4, band_shift(4) + RIGHT * 0.9 + DOWN * 0.4,
                   color=RED, stroke_width=6)
        cut_lab = Tex(r"flood breaks through: the shortcut opens").scale(0.9).shift(band_shift(4) + DOWN * 2.5)
        self.play(Create(cut), Write(cut_lab))
        self.wait(2)
        seal = Tex(r"Deposition seals both ends of the old loop").scale(0.9).shift(band_shift(4) + DOWN * 3.3)
        self.play(Write(seal))
        self.wait(3)

        # --- Band 5 (subtopic_3): the eight-step paragraph answer ---
        self.next_band(5)
        b5_t = Tex("The eight-step exam paragraph").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        e1 = Tex(r"1. Outer banks eroded \; 2. Inner banks built").scale(0.95).shift(band_shift(5) + UP * 1.2)
        e2 = Tex(r"3. Neck narrows \; 4. Flood breaks through").scale(0.95).shift(band_shift(5) + UP * 0.4)
        e3 = Tex(r"5. Shortcut becomes main channel").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        e4 = Tex(r"6. Deposition seals the ends").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        e5 = Tex(r"7. Cut-off loop = OXBOW LAKE").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        e6 = Tex(r"8. Dries and silts to a meander scar").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(e1))
        self.wait(2)
        self.play(Write(e2))
        self.wait(2)
        self.play(Write(e3))
        self.wait(1.5)
        self.play(Write(e4))
        self.wait(1.5)
        self.play(Write(e5))
        self.play(Create(SurroundingRectangle(e5, color=GREEN)))
        self.wait(2)
        self.play(Write(e6))
        self.wait(3)

        # --- Band 6 (subtopic_4): reading sketches and photographs ---
        self.next_band(6)
        b6_t = Tex("Reading the sketch and the photo").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        p1 = Tex(r"Profile: step = waterfall; flat pond = dam;").scale(0.95).shift(band_shift(6) + UP * 1.2)
        p1b = Tex(r"dashed line at the sea = permanent base level").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(p1))
        self.play(Write(p1b))
        self.wait(2.5)
        p2 = Tex(r"Smooth concave sweep, no steps $\Rightarrow$ graded").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(p2))
        self.wait(2)
        p3 = Tex(r"Photo: steep raw bank = outer, fast, undercut;").scale(0.95).shift(band_shift(6) + DOWN * 1.4)
        p3b = Tex(r"gentle sand bar = inner, slow, slip-off").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(p3))
        self.play(Write(p3b))
        self.wait(2.5)
        p4 = Tex(r"Account for the slope = name the water speed").scale(0.95).shift(band_shift(6) + DOWN * 3.1)
        self.play(Write(p4))
        self.play(Create(SurroundingRectangle(p4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): map signatures + look-alike questions ---
        self.next_band(7)
        b7_t = Tex("Map signatures and look-alikes").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        s1 = Tex(r"Meanders: wide blue loops, contours far back").scale(0.95).shift(band_shift(7) + UP * 1.2)
        s2 = Tex(r"Oxbow: detached blue/marsh crescent beside them").scale(0.95).shift(band_shift(7) + UP * 0.4)
        s3 = Tex(r"Incised meanders: loops in gorges, contours tight").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.wait(2)
        self.play(Write(s3))
        self.wait(2.5)
        q1 = Tex(r"Meander question: speed, erode, deposit, grow").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        q2 = Tex(r"Oxbow question: all that + neck, flood, seal").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(q1))
        self.wait(2)
        self.play(Write(q2))
        self.wait(2)
        q3 = Tex(r"The oxbow answer CONTAINS the meander answer").scale(0.95).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(q3))
        self.play(Create(SurroundingRectangle(q3, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the slide from the mountain to the sea ---
        self.next_band(8)
        b8_t = Tex("The slide from the mountain to the sea").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        s8a = Tex(r"Good slide = graded: one smooth swoop").scale(1.0).shift(band_shift(8) + UP * 1.2)
        s8b = Tex(r"Unfinished slide = ungraded: ledge + flat pan").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(s8a))
        self.wait(2)
        self.play(Write(s8b))
        self.wait(2)
        s8c = Tex(r"Ledge = waterfall; pan = dam (temporary)").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(s8c))
        self.wait(2)
        s8d = Tex(r"The sea is the floor: permanent base level").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(s8d))
        self.play(Create(SurroundingRectangle(s8d, color=GREEN)))
        self.wait(2)
        s8e = Tex(r"Knife-cut V up top; spade-scoop flat floor below").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(s8e))
        self.wait(3)

        # --- Band 9 (subtopic_6): the taxi around the corner ---
        self.next_band(9)
        b9_t = Tex("The taxi around the corner").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        t1 = Tex(r"Far-window passenger: long path, FAST").scale(1.0).shift(band_shift(9) + UP * 1.2)
        t2 = Tex(r"Inside passenger: short path, SLOW").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(t1))
        self.wait(2)
        self.play(Write(t2))
        self.wait(2)
        t3 = Tex(r"Fast lane digs the cliff (undercut slope)").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        t4 = Tex(r"Slow lane drops the beach (slip-off slope)").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(t3))
        self.wait(2)
        self.play(Write(t4))
        self.play(Create(SurroundingRectangle(t4, color=GREEN)))
        self.wait(2)
        t5 = Tex(r"Each flood shifts the coils — the wandering").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        t5b = Tex(r"loops sweep the floodplain flat").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(t5))
        self.play(Write(t5b))
        self.wait(3)

        # --- Band 10 (subtopic_7): the shortcut through the empty plot ---
        self.next_band(10)
        b10_t = Tex("The shortcut through the empty plot").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        x1 = Tex(r"Two crews trench the neck from both sides").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(x1))
        self.wait(2)
        x2 = Tex(r"Big flood punches through — shortcut open").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(x2))
        self.wait(2)
        x3 = Tex(r"Sand gates seal the loop's two ends").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(x3))
        self.wait(2)
        x4 = Tex(r"Horseshoe of still water = OXBOW LAKE").scale(1.05).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(x4))
        self.play(Create(SurroundingRectangle(x4, color=GREEN)))
        self.wait(2)
        x5 = Tex(r"It shrinks, silts, reeds close in: meander scar").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(x5))
        self.wait(2)
        x6 = Tex(r"Tell the eight steps in order — full marks").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(x6))
        self.wait(4)
