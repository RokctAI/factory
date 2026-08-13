from manim import *

# Band-layout whiteboard scene for the CAPS Grade 12 Geography session
# "Mapwork Paper Practice Run" (DBE November 2018, Pietermaritzburg extract).
# Bands cover all seven subtopics with dwell time proportional to
# subtopics.json (180/220/220/280/220/260/240 of 1620 s) — the gradient
# calculation (subtopic_4) carries the largest share and gets two bands.
# All diagrams (spur contours, valley frost pocket, buffer) are hand-built
# from exporter-safe primitives only (Tex/MathTex/Line/Arrow/Dot/Circle/
# Rectangle/VGroup); add-only lifecycle, camera moves down between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MapworkPaperPracticeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # --- Band 0 (subtopic_1): meeting the Pietermaritzburg extract ---
        title = Tex("Mapwork Practice: Pietermaritzburg 2018").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"A city in a bowl, ringed by higher country").scale(1.0).shift(UP * 0.9)
        b0_l2 = Tex(r"Town Hill and World's View to the NW;").scale(1.0).shift(UP * 0.2)
        b0_l3 = Tex(r"trig station at 1057,9 m; Msunduzi below").scale(1.0).shift(DOWN * 0.5)
        for m in (b0_l1, b0_l2, b0_l3):
            self.play(Write(m))
            self.wait(1.8)
        b0_l4 = Tex(r"Read the margin first: 1:50 000 scale,").scale(1.0).shift(DOWN * 1.4)
        b0_l5 = Tex(r"20 m contour interval, declination note").scale(1.0).shift(DOWN * 2.1)
        self.play(Write(b0_l4)); self.wait(1.6)
        self.play(Write(b0_l5)); self.wait(1.5)
        b0_l6 = Tex(r"Today: Section B skills, question by question").scale(0.95).shift(DOWN * 2.9)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_2): Question 1 — fifteen multiple-choice marks ---
        self.next_band(1)
        b1_t = Tex("Q1: fifteen marks of automatic skills").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex(r"Map codes: the 2930 degree square,").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex(r"letters walking a grid of sixteen").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1)); self.wait(1.6)
        self.play(Write(b1_l2)); self.wait(1.8)
        b1_l3 = Tex(r"Contours: close $=$ steep, wide $=$ gentle,").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        b1_l4 = Tex(r"V pointing uphill $=$ river valley").scale(1.0).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1_l3)); self.wait(1.6)
        self.play(Write(b1_l4)); self.wait(1.8)
        b1_l5 = Tex(r"True bearing: zero on true north,").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        b1_l6 = Tex(r"read clockwise --- $120^\circ$ lies south-east").scale(1.0).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l5)); self.wait(1.6)
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_3): Q2.1 — references and the spur ---
        self.next_band(2)
        b2_t = Tex("Q2.1: index, coordinates, the spur").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex(r"Coordinates: line west, then line south;").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex(r"degrees, minutes, seconds --- then S and E").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1)); self.wait(1.8)
        self.play(Write(b2_l2)); self.wait(2)
        # spur: nested contour Vs pointing right, trail riding the crest
        sc2 = band_shift(2) + DOWN * 1.5
        spur = VGroup(
            Line(sc2 + LEFT * 3.4 + UP * 1.0, sc2 + RIGHT * 0.6, color=YELLOW, stroke_width=3),
            Line(sc2 + RIGHT * 0.6, sc2 + LEFT * 3.4 + DOWN * 1.0, color=YELLOW, stroke_width=3),
            Line(sc2 + LEFT * 3.4 + UP * 0.6, sc2 + LEFT * 0.6, color=YELLOW, stroke_width=3),
            Line(sc2 + LEFT * 0.6, sc2 + LEFT * 3.4 + DOWN * 0.6, color=YELLOW, stroke_width=3),
        )
        for seg in spur:
            self.play(Create(seg), run_time=0.5)
        trail = Line(sc2 + LEFT * 3.4, sc2 + RIGHT * 0.2, color=RED, stroke_width=4)
        self.play(Create(trail))
        l_spur = Tex(r"spur: high ground between valleys,\\the trail rides its back").scale(0.9).shift(sc2 + RIGHT * 3.4)
        self.play(Write(l_spur))
        self.wait(3)

        # --- Band 3 (subtopic_4): the gradient calculation, memo style ---
        self.next_band(3)
        b3_t = Tex("Q2.2: average gradient, O to P").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_f = MathTex(r"\text{Gradient} = \frac{\text{VI}}{\text{HE}}").scale(1.15).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_f)); self.wait(2)
        b3_l1 = MathTex(r"\text{VI} = 1057{,}9 - 820 = 237{,}9\ \text{m}").scale(1.1).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1)); self.wait(2)
        b3_l2 = MathTex(r"\text{HE} = 3{,}9\ \text{cm} \times 500 = 1950\ \text{m}").scale(1.1).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l2)); self.wait(2)
        b3_l3 = MathTex(r"\text{Gradient} = \frac{237{,}9}{1950}").scale(1.1).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l3)); self.wait(2)
        b3_l4 = MathTex(r"= 1 : 8{,}2").scale(1.2).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_4): how the memo marked it ---
        self.next_band(4)
        b4_t = Tex("Marked like the memo: five steps").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex(r"VI, map distance, HE, substitution, ratio").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1)); self.wait(2)
        b4_l2 = Tex(r"Tolerance: 3,8--4 cm; answer 1:7,9--1:8,4").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2)); self.wait(2)
        b4_wrong = Tex(r"A bare ratio, no working shown").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(1.8)
        b4_l3 = Tex(r"Method marks only protect working on the page").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = Tex(r"Trail route: winds along the spur in curves,").scale(0.95).shift(band_shift(4) + DOWN * 2.3)
        b4_l5 = Tex(r"avoiding the contour-crowded faces").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l4)); self.wait(1.5)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_5): cross-sections and vertical exaggeration ---
        self.next_band(5)
        b5_t = Tex("Q2.3: vertical exaggeration").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_f = MathTex(r"\text{VE} = \frac{\text{vertical scale}}{\text{horizontal scale}}").scale(1.02).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_f)); self.wait(2)
        b5_l1 = MathTex(r"= \frac{1/10\,000}{1/50\,000}").scale(1.1).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l1)); self.wait(2)
        b5_l2 = MathTex(r"= \frac{50\,000}{10\,000} = 5\ \text{times}").scale(1.1).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2)
        b5_l3 = Tex(r"Say TIMES --- not 5, not 1:5").scale(1.05).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l3)); self.wait(1.8)
        b5_l4 = Tex(r"Why: true-scale hills flatten to nothing").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_6): the frost pocket at M, drawn ---
        self.next_band(6)
        b6_t = Tex("Q3: why farmers at M fear clear nights").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        sc6 = band_shift(6) + DOWN * 0.6
        # valley cross-profile: two slopes meeting a flat floor
        vp = VGroup(
            Line(sc6 + LEFT * 4.2 + UP * 1.8, sc6 + LEFT * 1.2 + DOWN * 0.6, stroke_width=4),
            Line(sc6 + LEFT * 1.2 + DOWN * 0.6, sc6 + RIGHT * 1.2 + DOWN * 0.6, stroke_width=4),
            Line(sc6 + RIGHT * 1.2 + DOWN * 0.6, sc6 + RIGHT * 4.2 + UP * 1.8, stroke_width=4),
        )
        for seg in vp:
            self.play(Create(seg), run_time=0.6)
        a1 = Arrow(sc6 + LEFT * 3.4 + UP * 1.3, sc6 + LEFT * 1.9 + UP * 0.1, color=BLUE, buff=0.1)
        a2 = Arrow(sc6 + RIGHT * 3.4 + UP * 1.3, sc6 + RIGHT * 1.9 + UP * 0.1, color=BLUE, buff=0.1)
        l_kat = Tex(r"katabatic drainage").scale(0.85).shift(sc6 + UP * 1.9)
        self.play(Create(a1), Create(a2), Write(l_kat))
        self.wait(1.8)
        d_m = Dot(sc6 + DOWN * 0.6, color=BLUE)
        l_m = Tex(r"cold air ponds at M: frost pocket").scale(0.85).shift(sc6 + DOWN * 1.2)
        self.play(Create(d_m), Write(l_m))
        self.wait(1.8)
        d_tb = Dot(sc6 + LEFT * 2.6 + UP * 0.6, color=GREEN)
        l_tb = Tex(r"thermal belt").scale(0.85).shift(sc6 + LEFT * 3.5 + UP * 0.3)
        self.play(Create(d_tb), Write(l_tb))
        self.wait(1.5)
        b6_l1 = Tex(r"Inversion: warm air rests above the cold pool").scale(0.95).shift(sc6 + DOWN * 2.0)
        self.play(Write(b6_l1))
        self.wait(3)

        # --- Band 7 (subtopic_6): aspect and stream order ---
        self.next_band(7)
        b7_t = Tex("Aspect, settlement, stream order").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex(r"Southern Hemisphere: north-facing slope").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"drinks the midday sun --- warmer, richer suburbs").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1)); self.wait(1.6)
        self.play(Write(b7_l2)); self.wait(1.8)
        b7_l3 = Tex(r"Shadowed south-facing slope: colder, damper,").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex(r"denser, lower-income housing").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3)); self.wait(1.6)
        self.play(Write(b7_l4)); self.wait(1.8)
        b7_l5 = Tex(r"Order: two firsts make a second;").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        b7_l6 = Tex(r"only two seconds make a third").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5)); self.wait(1.5)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_7): GIS for the closing marks ---
        self.next_band(8)
        b8_t = Tex("Q4: GIS --- four ideas").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = Tex(r"Spatial data locates; attribute data").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"describes --- the river's line vs its name").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1)); self.wait(1.6)
        self.play(Write(b8_l2)); self.wait(1.8)
        b8_l3 = Tex(r"Scale matches the question; layers stack").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3)); self.wait(1.8)
        # buffering sketch: river line with a buffer rectangle around it
        sc8 = band_shift(8) + DOWN * 1.6
        river = Line(sc8 + LEFT * 3.2, sc8 + RIGHT * 3.2, color=BLUE, stroke_width=4)
        buf = Rectangle(width=6.8, height=1.0, color=GREEN).shift(sc8)
        self.play(Create(river))
        self.play(Create(buf))
        l_buf = Tex(r"buffer the Msunduzi 100 m: flood-risk homes").scale(0.85).shift(sc8 + DOWN * 1.1)
        self.play(Write(l_buf))
        self.wait(3)

        # --- Band 9: the habit the whole paper teaches ---
        self.next_band(9)
        b9_t = Tex("Mapwork marks are method marks").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex(r"Formula before numbers, working before").scale(1.05).shift(band_shift(9) + UP * 1.0)
        b9_l2 = Tex(r"answers, units always, evidence for claims").scale(1.05).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1)); self.wait(1.8)
        self.play(Write(b9_l2)); self.wait(2)
        b9_l3 = Tex(r"1 : 8,2 with working shown $=$ 5/5").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex(r"Section B: the most predictable marks you own").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.wait(4)
