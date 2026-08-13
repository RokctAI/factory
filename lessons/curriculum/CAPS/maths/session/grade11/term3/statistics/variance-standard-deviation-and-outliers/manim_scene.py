from manim import *

# Band-layout whiteboard scene (reference: quadratics-by-factorisation).
# One band per teaching beat, add-only lifecycle, camera moves down between
# bands. Covers all seven subtopics: Part 1 Expert (five number summary and
# box-and-whisker, variance and standard deviation, symmetric and skewed
# data, identifying outliers) then Part 2 Simplifier (five landmarks on one
# road, the average distance from home, the mansion and the fences).
# Band dwell proportional to subtopics.json (225/230/220/230/190/195/195
# of 1485 s). Box plot built from Line/Rectangle primitives only.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class VarianceStdDevOutliersSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the five number summary ---
        title = Tex("Variance, Standard Deviation and Outliers").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"44,\,48,\,50,\,52,\,53,\,55,\,56,\,58,\,60,\,84").scale(1.05).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"\text{Median} = \tfrac{53 + 55}{2} = 54").scale(1.1).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = MathTex(r"Q_1 = 50 \quad (\text{median of bottom five})").scale(1.05).shift(DOWN * 0.8)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = MathTex(r"Q_3 = 58 \quad (\text{median of top five})").scale(1.05).shift(DOWN * 1.7)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = MathTex(r"\text{Summary: } 44,\; 50,\; 54,\; 58,\; 84").scale(1.1).shift(DOWN * 2.7)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the box-and-whisker, range vs IQR ---
        self.next_band(1)
        b1_title = Tex("The box-and-whisker diagram").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        o = band_shift(1) + DOWN * 0.2 + LEFT * 3.0

        def bx(v):
            return o + RIGHT * (v - 40) * 0.12

        axis = Line(bx(38), bx(92))
        self.play(Create(axis))
        ticks = VGroup(*[MathTex(str(v)).scale(0.6).move_to(bx(v) + DOWN * 0.4)
                         for v in [40, 50, 60, 70, 80, 90]])
        self.play(Write(ticks))
        self.wait(1.5)
        box = Rectangle(width=(58 - 50) * 0.12, height=1.0, color=BLUE).move_to(bx(54) + UP * 1.0)
        med = Line(bx(54) + UP * 0.5, bx(54) + UP * 1.5, color=YELLOW)
        wl = Line(bx(44) + UP * 1.0, bx(50) + UP * 1.0)
        wr = Line(bx(58) + UP * 1.0, bx(84) + UP * 1.0)
        self.play(Create(box))
        self.play(Create(med))
        self.play(Create(wl), Create(wr))
        self.wait(2.5)
        b1_l1 = MathTex(r"\text{Range} = 84 - 44 = 40 \;\; (\text{fragile})").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"IQR = 58 - 50 = 8 \;\; (\text{middle half})").scale(1.0).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("One whisker stretches 26 marks — hold that").scale(1.0).shift(band_shift(1) + DOWN * 3.4)
        self.play(Write(b1_l3))
        self.wait(2)

        # --- Band 2 (subtopic_2): standard deviation — the first steps ---
        self.next_band(2)
        b2_title = Tex("Standard deviation: 4, 6, 7, 9, 14 goals").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Mean: } \bar{x} = \tfrac{40}{5} = 8").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"\text{Deviations: } -4,\; -2,\; -1,\; 1,\; 6").scale(1.1).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\text{They sum to } 0 \text{ — always}").scale(1.05).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("So square them to kill the signs").scale(1.05).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): variance, then root back to units ---
        self.next_band(3)
        b3_title = Tex("Square, average, root").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Squares: } 16,\; 4,\; 1,\; 1,\; 36").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\text{Variance} = \tfrac{58}{5} = 11{,}6").scale(1.1).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"\sigma = \sqrt{11{,}6} \approx 3{,}41 \text{ goals}").scale(1.15).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Variance is in goals$^2$ — root back to real units").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Show the table; the calculator only confirms").scale(1.0).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the mean chases the tail ---
        self.next_band(4)
        b4_title = Tex("Symmetric or skewed? Name the tail").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Mean} = \tfrac{560}{10} = 56, \quad \text{median} = 54").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\text{mean} > \text{median} \;\Rightarrow\; \text{positively skewed}").scale(1.05).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex("The mean chases the tail — the 84 drags it").scale(1.05).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("Long RIGHT tail $=$ positive; LEFT $=$ negative").scale(1.05).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the box plot as evidence ---
        self.next_band(5)
        b5_title = Tex("Read the box plot as evidence").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Right whisker nearly five times the left").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("The picture shouts what the numbers whispered").scale(1.05).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Skewness describes SHAPE, not quality").scale(1.05).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("Justify in writing: quote mean vs median").scale(1.05).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the fences ---
        self.next_band(6)
        b6_title = Tex("Outliers by rule: build the fences").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"IQR = 8, \quad 1{,}5 \times 8 = 12").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"\text{Lower fence: } 50 - 12 = 38").scale(1.1).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"\text{Upper fence: } 58 + 12 = 70").scale(1.1).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"84 > 70 \;\Rightarrow\; 84 \text{ is an outlier}").scale(1.1).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2.5)
        b6_l5 = Tex("Write the conclusion as an inequality").scale(1.0).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.wait(2)

        # --- Band 7 (subtopic_4): fragile vs robust ---
        self.next_band(7)
        b7_title = Tex("What one outlier does to each tool").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{With } 84: \; \bar{x} = 56, \;\; \sigma \approx 10{,}4").scale(1.1).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"\text{Without: } \bar{x} \approx 52{,}9, \;\; \sigma \approx 4{,}7").scale(1.1).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Median barely moves; IQR not at all").scale(1.05).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Mean and $\\sigma$: precise but fragile").scale(1.05).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Median and IQR: blunt but robust — report them").scale(1.05).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): five landmarks on one road ---
        self.next_band(8)
        b8_title = Tex("Five landmarks on one road").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Ten houses, sorted: number 44 to number 84").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Start, quarter, halfway, three-quarter, end").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("The box $=$ the neighbourhood, 50 to 58").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Range 40 is hostage to the mansion").scale(1.05).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = MathTex(r"IQR = 8 \text{ — stays put, whatever gets built}").scale(1.0).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the average distance from home ---
        self.next_band(9)
        b9_title = Tex("The average distance from home").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Five matches: 4, 6, 7, 9, 14 — home base 8").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Signed distances cancel to 0 — every time").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Square first: big strays shout — 6 becomes 36").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"\tfrac{58}{5} = 11{,}6, \quad \sqrt{11{,}6} \approx 3{,}41").scale(1.1).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex(r"Rival: same mean, $\sigma = 1{,}2$ — the safer pick").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the mansion and the fences ---
        self.next_band(10)
        b10_title = Tex("The mansion and the fences").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"\text{Fences: } 50 - 12 = 38 \text{ and } 58 + 12 = 70").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"84 > 70: \text{ the mansion is an outlier}").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex(r"It drags the mean: $53 \to 56$").scale(1.05).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex(r"And hoists $\sigma$: about $4{,}7 \to 10{,}4$").scale(1.05).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Mansion on the road? Use median and IQR — say why").scale(1.0).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l5))
        self.wait(4)
