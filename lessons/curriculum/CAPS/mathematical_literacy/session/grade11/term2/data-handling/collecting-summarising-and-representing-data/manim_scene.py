from manim import *

# Band layout: one frame-height band per teaching beat; the camera moves down,
# nothing is removed. Exporter-supported mobjects only (Tex/MathTex/Line/
# Rectangle/SurroundingRectangle); single-string Write reveals throughout.
#
# Covers all seven subtopics (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# band time roughly proportional to subtopics.json
# (215/220/225/230/195/195/195 of 1475 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CollectingSummarisingDataSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): sharp question, population, sample ---
        title = Tex("Collecting, Summarising, Representing Data").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        q_bad = Tex(r"``Do learners spend too much on airtime?''").scale(1.0).shift(UP * 1.1)
        self.play(Write(q_bad))
        self.play(Create(strike(q_bad)))
        self.wait(2)
        q_good = Tex(r"``How many rand a week on airtime and data?''").scale(1.0).shift(UP * 0.1)
        self.play(Write(q_good))
        self.play(Create(SurroundingRectangle(q_good, color=GREEN)))
        self.wait(2.5)
        l1 = Tex(r"Population: all 1\,240 learners (census $=$ ask all)").scale(0.95).shift(DOWN * 0.9)
        l2 = Tex("Sample: 60 learners standing for the whole").scale(0.95).shift(DOWN * 1.8)
        self.play(Write(l1)); self.wait(2.5)
        self.play(Write(l2)); self.wait(2.5)

        # --- Band 1 (subtopic_1): bias and the instrument ---
        self.next_band(1)
        b1_title = Tex("Representative, random, or biased?").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_wrong = Tex("60 friends from grade 11 — seniors carry more money").scale(0.95).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2.5)
        b1_l1 = Tex("Random: every learner has an equal chance").scale(1.0).shift(band_shift(1) + UP * 0.1)
        b1_l2 = Tex("Draw 60 names from the register, or every 20th name").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l1)); self.wait(2.5)
        self.play(Write(b1_l2)); self.wait(2.5)
        b1_l3 = Tex("Questionnaire: cheap, many blanks. Interview: deep, slow.").scale(0.9).shift(band_shift(1) + DOWN * 1.8)
        b1_l4 = Tex("Choose the instrument AND defend it in a sentence").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l3)); self.wait(2.5)
        self.play(Write(b1_l4)); self.wait(2.5)

        # --- Band 2 (subtopic_2): class intervals and the frequency table ---
        self.next_band(2)
        b2_title = Tex("Sixty raw answers into a frequency table").scale(1.1).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_wrong = Tex(r"``R20 to R40'' then ``R40 to R60'' — R40 has two homes!").scale(0.9).shift(band_shift(2) + UP * 1.8)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2.5)
        tbl = Rectangle(width=9.6, height=2.6).shift(band_shift(2) + UP * 0.1)
        self.play(Create(tbl))
        b2_r1 = Tex(r"Interval: 0-- \; 20-- \; 40-- \; 60-- \; 80+").scale(1.0).shift(band_shift(2) + UP * 0.6)
        b2_r2 = Tex(r"Frequency: 8 \quad 19 \quad 21 \quad 7 \quad 5").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_r1)); self.wait(2)
        self.play(Write(b2_r2)); self.wait(2.5)
        b2_l1 = MathTex(r"8 + 19 + 21 + 7 + 5 = 60 \;\checkmark").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = Tex("Grouping trades exact detail for visible shape").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l2)); self.wait(2.5)

        # --- Band 3 (subtopic_3): mean, median, mode, range ---
        self.next_band(3)
        b3_title = Tex(r"Sorted: 20, 25, 25, 30, 35, 40, 45, 50, 90").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\text{Mean: } 360 \div 9 = R40").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{Median (5th of 9): } R35").scale(1.05).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"\text{Mode: } R25; \quad \text{Range: } 90 - 20 = R70").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l1)); self.wait(2.5)
        self.play(Write(b3_l2)); self.wait(2.5)
        self.play(Write(b3_l3)); self.wait(2.5)
        b3_l4 = Tex("Sort BEFORE finding the median").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l4)); self.wait(2.5)

        # --- Band 4 (subtopic_3): the outlier, and the machine backwards ---
        self.next_band(4)
        b4_title = Tex("Why the mean and median argue").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"The R90 outlier drags the MEAN up; the median stays").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1)); self.wait(2.5)
        b4_l2 = MathTex(r"\text{Without the } 90: \; 270 \div 8 = R33{,}75").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2)); self.wait(2.5)
        b4_l3 = Tex("With outliers, the MEDIAN is the honest typical value").scale(0.95).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = MathTex(r"\text{Backwards: mean } 40 \Rightarrow \text{total } 9 \times 40 = 360").scale(0.9).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4)); self.wait(2.5)

        # --- Band 5 (subtopic_4): the three graphs ---
        self.next_band(5)
        b5_title = Tex("Three pictures carry the term").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Multiple bar graph: compare two datasets per category").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("Line graph: trend over time; broken line for jumps").scale(0.95).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex("Scatter plot: do two quantities move together?").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l1)); self.wait(2.5)
        self.play(Write(b5_l2)); self.wait(2.5)
        self.play(Write(b5_l3)); self.wait(2.5)
        b5_l4 = Tex("Read: title, then SCALE, then values").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): graphs that lie ---
        self.next_band(6)
        b6_title = Tex("Graphs that lie without a false number").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Axis starting at R35: R40 towers over R36").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex(r"``The difference is R4, though it looks triple''").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1)); self.wait(2.5)
        self.play(Write(b6_l2)); self.wait(2.5)
        b6_l3 = Tex("Watch uneven axes, inflated picture areas, squeezed months").scale(0.9).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3)); self.wait(2.5)
        b6_l4 = Tex(r"Verdict: spending clusters R20--R60, so stock R29 vouchers").scale(0.9).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): asking the right people ---
        self.next_band(7)
        b7_title = Tex("A question a calculator could answer").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2.5)
        b7_l1 = Tex("Name the group, the quantity and the unit").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1)); self.wait(3)
        b7_l2 = Tex("Census: perfect and impossible before Friday").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2)); self.wait(3)
        b7_l3 = Tex("Asking your grade 11 friends leans rich — bias").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3)); self.wait(3)
        b7_l4 = Tex("Cure: 60 names from the register, chosen at random").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3.5)

        # --- Band 8 (subtopic_6): sixty answers into one table ---
        self.next_band(8)
        b8_title = Tex("Eat the chaos one bite at a time").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex(r"Bins: R0--, R20--, R40--, R60--, R80 and up").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1)); self.wait(3)
        b8_l2 = Tex(r"``To under R40'', next starts AT R40 — one home each").scale(0.95).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2)); self.wait(3)
        b8_l3 = MathTex(r"8 + 19 + 21 + 7 + 5 = 60 \;\checkmark").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(3)
        b8_l4 = Tex("Shape gained, detail lost — say both halves").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4)); self.wait(3.5)

        # --- Band 9 (subtopic_7): three middles, one spread, one trick ---
        self.next_band(9)
        b9_title = Tex("Share-out, queue, favourite").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = MathTex(r"\text{Mean } 360 \div 9 = 40; \;\; \text{median } 35; \;\; \text{mode } 25").scale(0.88).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1)); self.wait(3)
        b9_l2 = Tex("The mean shook hands with the R90; the median never met it").scale(0.9).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2)); self.wait(3)
        b9_l3 = MathTex(r"\text{Range: } 90 - 20 = R70").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3)); self.wait(3)
        b9_l4 = Tex("Axis check: where does the vertical axis START?").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(3)
        b9_l5 = Tex("The picture cannot lie to someone who quotes it").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5)); self.wait(4)
