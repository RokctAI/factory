from manim import *

# BAND LAYOUT: content is laid out in sequential vertical bands along a long
# virtual canvas — one band per teaching step, each one frame-height tall.
# Nothing is ever faded out or overwritten; the camera moves down to clean
# space and earlier work stays on the canvas. Only exporter-supported mobjects
# (Tex/MathTex/Text -> text, Line/Arrow -> line, Rectangle -> rect, Dot,
# Circle) are used, with write-only reveals — no sub-part transforms.
#
# The scene mirrors script.md across all seven subtopics of the session duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# band time proportional to subtopics.json (220/220/235/220/190/185/200 of
# 1470 s). Level 6 rescales primitive times to the real audio, so only the
# proportions matter.

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a wrong line, teacher-style."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CollectingOrganisingSummarisingDataSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the data cycle, stage by stage ---
        title = Tex("Collecting, Organising and Summarising Data").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        cyc_t = Tex("The data cycle — fixed order:").scale(1.1).shift(UP * 1.4)
        self.play(Write(cyc_t))
        self.wait(1.5)
        c1 = Tex("1. Pose a question \\quad 2. Collect").scale(1.1).shift(UP * 0.5)
        c2 = Tex("3. Organise and classify").scale(1.1).shift(DOWN * 0.4)
        c3 = Tex("4. Summarise and represent").scale(1.1).shift(DOWN * 1.3)
        c4 = Tex("5. Analyse \\quad 6. Report an answer").scale(1.1).shift(DOWN * 2.2)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(1.5)
        self.play(Write(c3))
        self.wait(1.5)
        self.play(Write(c4))
        self.wait(3)

        # --- Band 1 (subtopic_1): a usable question, data types, bias ---
        self.next_band(1)
        b1_t = Tex("A question worth asking").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_bad = Tex("``Is the clinic slow?''").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_bad))
        self.play(Create(strike(b1_bad)))
        self.wait(2)
        b1_good = Tex("``How many minutes does a patient wait?''").scale(1.05).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_good))
        self.play(Create(SurroundingRectangle(b1_good, color=GREEN)))
        self.wait(2.5)
        b1_num = Tex("Numerical: discrete (counts),").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        b1_num2 = Tex("continuous (47,5 min) — Categorical: labels").scale(1.05).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_num))
        self.wait(1.5)
        self.play(Write(b1_num2))
        self.wait(2)
        b1_src = Tex("Primary: you collect. Secondary: the register.").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        b1_bias = Tex("Guard against bias — spread the sample.").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_src))
        self.wait(2)
        self.play(Write(b1_bias))
        self.wait(3)

        # --- Band 2 (subtopic_2): order the raw data first ---
        self.next_band(2)
        b2_t = Tex("Organise: order the raw data").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_raw_t = Tex("Raw, in collection order (minutes):").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_raw1 = MathTex(r"45,\;120,\;25,\;50,\;35,\;45,\;20,\;90").scale(1.0).shift(band_shift(2) + UP * 0.4)
        b2_raw2 = MathTex(r"30,\;55,\;45,\;25,\;60,\;140,\;40").scale(1.0).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(b2_raw_t))
        self.play(Write(b2_raw1))
        self.play(Write(b2_raw2))
        self.wait(2.5)
        b2_ord_t = Tex("Ordered, smallest to largest:").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        b2_ord1 = MathTex(r"20,\;25,\;25,\;30,\;35,\;40,\;45,\;45").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        b2_ord2 = MathTex(r"45,\;50,\;55,\;60,\;90,\;120,\;140").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_ord_t))
        self.play(Write(b2_ord1))
        self.play(Write(b2_ord2))
        self.wait(3)

        # --- Band 3 (subtopic_2): the frequency table, row by row ---
        self.next_band(3)
        b3_t = Tex("Frequency table — class intervals").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        # Table skeleton: border rect + column divider + header rule.
        tbl = Rectangle(width=7.0, height=4.6).shift(band_shift(3) + DOWN * 0.6)
        vdiv = Line(UP * 2.3, DOWN * 2.3).shift(band_shift(3) + DOWN * 0.6 + RIGHT * 1.6)
        hrule = Line(LEFT * 3.5, RIGHT * 3.5).shift(band_shift(3) + UP * 1.05)
        self.play(Create(tbl))
        self.play(Create(vdiv), Create(hrule))
        h1 = Tex("Interval (min)").scale(0.95).shift(band_shift(3) + UP * 1.35 + LEFT * 1.5)
        h2 = Tex("Freq.").scale(0.95).shift(band_shift(3) + UP * 1.35 + RIGHT * 2.5)
        self.play(Write(h1), Write(h2))
        self.wait(1.5)
        rows = [
            (r"0\text{--}29", "3"),
            (r"30\text{--}59", "8"),
            (r"60\text{--}89", "1"),
            (r"90\text{--}119", "1"),
            (r"120\text{--}149", "2"),
        ]
        for i, (iv, fr) in enumerate(rows):
            y = 0.5 - 0.75 * i
            cell_i = MathTex(iv).scale(0.95).shift(band_shift(3) + UP * y + LEFT * 1.5)
            cell_f = MathTex(fr).scale(0.95).shift(band_shift(3) + UP * y + RIGHT * 2.5)
            self.play(Write(cell_i), Write(cell_f))
            self.wait(1.2)
        b3_chk = MathTex(r"3 + 8 + 1 + 1 + 2 = 15 \;\checkmark").scale(1.05).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(b3_chk))
        self.play(Create(SurroundingRectangle(b3_chk, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): mean and median ---
        self.next_band(4)
        b4_t = Tex("Summarise: mean and median").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Total} = 825 \text{ minutes}").scale(1.1).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"\text{Mean} = \frac{825}{15} = 55 \text{ minutes}").scale(1.1).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{Median position} = \frac{15 + 1}{2} = 8").scale(1.05).shift(band_shift(4) + DOWN * 1.0)
        b4_l4 = MathTex(r"\text{8th ordered value} = 45 \text{ minutes}").scale(1.05).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        b4_note = Tex("Even count: mean of the two middle values").scale(1.0).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_note))
        self.wait(3)

        # --- Band 5 (subtopic_3): mode and range ---
        self.next_band(5)
        b5_t = Tex("Mode and range").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Mode: } 45 \text{ appears } 3 \text{ times} = 45 \text{ min}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Only the mode works for categorical data").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"\text{Range} = 140 - 20 = 120 \text{ minutes}").scale(1.1).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_h1 = Tex("Show the substitution, keep the unit,").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        b5_h2 = Tex("round only at the end.").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_h1))
        self.play(Write(b5_h2))
        self.wait(3)

        # --- Band 6 (subtopic_4): outliers pull the mean ---
        self.next_band(6)
        b6_t = Tex("Why mean and median disagree").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Mean } 55 \quad \text{vs} \quad \text{median } 45").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("Outliers 90, 120, 140 pull the mean up;").scale(1.05).shift(band_shift(6) + UP * 0.2)
        b6_l3 = Tex("the median barely notices them.").scale(1.05).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Extreme values present? Quote the MEDIAN").scale(1.05).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        b6_l5 = Tex("(that is why income is reported as a median)").scale(0.95).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): match the summary to the question ---
        self.next_band(7)
        b7_t = Tex("Which summary answers which question?").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("Typical wait? median: 45 min").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Total time? mean: } 55 \times 15 = 825 \text{ min}").scale(1.0).shift(band_shift(7) + UP * 0.2)
        b7_l3 = Tex("Most common item? mode").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = Tex("Unpredictability? range: 120 min").scale(1.05).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Report: numbers, interpretation, recommendation").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): a question the numbers can answer ---
        self.next_band(8)
        b8_t = Tex("Ask a question numbers can answer").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("``Do we spend too much?''").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.play(Create(strike(b8_l1)))
        self.wait(2)
        b8_l2 = Tex("``How many rands did each person").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("spend on airtime last month?''").scale(1.05).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("What (rands), on whom, and when").scale(1.05).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Spread who you ask; never let it lean").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): sorting the washing ---
        self.next_band(9)
        b9_t = Tex("Sorting the washing").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Order first, then pile:").scale(1.05).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(1.5)
        b9_l2 = Tex("Under 30 min: 3 people").scale(1.05).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex("30 to 59 min: 8 people — the big pile").scale(1.05).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex("Then 1, 1, and 2 long waits").scale(1.05).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9_l2))
        self.wait(1.5)
        self.play(Write(b9_l3))
        self.wait(1.5)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = MathTex(r"3 + 8 + 1 + 1 + 2 = 15 \;\checkmark").scale(1.05).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        b9_l6 = Tex("Piles must never overlap").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_7): middle, most, average, stretch ---
        self.next_band(10)
        b10_t = Tex("Middle, most, average and stretch").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = MathTex(r"\text{Average (mean): } \frac{825}{15} = 55 \text{ min}").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("Middle (median): 8th in line — 45 min").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("Most-often (mode): 45 min").scale(1.05).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = MathTex(r"\text{Stretch (range): } 140 - 20 = 120 \text{ min}").scale(1.05).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Long waits drag the mean up, not the median").scale(1.0).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
