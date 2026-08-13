from manim import *

# Band-layout whiteboard scene for the Interest, Banking and Inflation session
# duo. Part 1 — Expert: subtopics 1-4 (simple interest, compound interest,
# bank statement, inflation). Part 2 — Simplifier: subtopics 5-7 retell the
# same money story at the Umlazi kitchen table. Durations 215/215/225/230/
# 195/195/195 of 1470 s. Exporter-safe mobjects only (graph built from
# Arrows and chained Lines); add-only lifecycle; camera moves between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class InterestBankingInflationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): simple interest, year by year ---
        title = Tex("Interest, Banking and Inflation").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Simple interest: on the ORIGINAL only").scale(1.05).shift(UP * 1.1)
        b0_l2 = MathTex(r"8\;000 \times 0,075 = \text{R}600 \text{ each year}").scale(1.05).shift(UP * 0.2)
        b0_l3 = MathTex(r"3 \text{ years: } 600 \times 3 = \text{R1 800}").scale(1.05).shift(DOWN * 0.7)
        b0_l4 = MathTex(r"8\;000 + 1\;800 = \text{R9 800,00}").scale(1.1).shift(DOWN * 1.7)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2)); self.wait(2)
        self.play(Write(b0_l3)); self.wait(2)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the one-line formula check ---
        self.next_band(1)
        b1_title = Tex("The formula says the same thing").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"A = P(1 + r \times n)").scale(1.15).shift(band_shift(1) + UP * 1.0)
        b1_l2 = MathTex(r"8\;000 \times (1 + 0,075 \times 3)").scale(1.1).shift(band_shift(1) + UP * 0.0)
        b1_l3 = MathTex(r"= 8\;000 \times 1,225 = \text{R9 800,00}").scale(1.1).shift(band_shift(1) + DOWN * 0.9)
        b1_l4 = Tex("Equal R600 steps: a straight, tilted line").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b1_l4)); self.wait(3)

        # --- Band 2 (subtopic_2): compound interest, the year table ---
        self.next_band(2)
        b2_title = Tex("Compound: interest earns interest").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Year 1: } 8\;000 \times 1,075 = 8\;600,00").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{Year 2: } 8\;600 \times 1,075 = 9\;245,00").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"\text{Year 3: } 9\;245 \times 1,075 = 9\;938,38").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"9\;938,38 - 9\;800 = \text{R138,38 ahead}").scale(1.05).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2)); self.wait(2)
        self.play(Write(b2_l3)); self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        b2_note = Tex("107,5\\% each year: multiply by 1,075 again").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_note))
        self.wait(3)

        # --- Band 3 (subtopic_2): the widening gap, drawn ---
        self.next_band(3)
        b3_title = Tex("The straight line and the curve").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        origin = band_shift(3) + LEFT * 4.2 + DOWN * 2.4
        x_ax = Arrow(origin, origin + RIGHT * 5.6, buff=0, stroke_width=3)
        y_ax = Arrow(origin, origin + UP * 3.6, buff=0, stroke_width=3)
        x_lab = Tex("years").scale(0.8).next_to(x_ax.get_end(), DOWN, buff=0.15)
        y_lab = Tex("R").scale(0.8).next_to(y_ax.get_end(), LEFT, buff=0.15)
        self.play(Create(x_ax), Create(y_ax), Write(x_lab), Write(y_lab))
        self.wait(1)
        # Simple interest: straight line
        simple = Line(origin + UP * 0.8, origin + RIGHT * 5.0 + UP * 2.2, color=BLUE)
        s_lab = Tex("simple").scale(0.8).shift(band_shift(3) + RIGHT * 1.7 + DOWN * 0.7)
        self.play(Create(simple), Write(s_lab))
        self.wait(1.5)
        # Compound: polyline pulling away above the straight line
        c1 = Line(origin + UP * 0.8, origin + RIGHT * 2.0 + UP * 1.5, color=YELLOW)
        c2 = Line(origin + RIGHT * 2.0 + UP * 1.5, origin + RIGHT * 3.6 + UP * 2.4, color=YELLOW)
        c3 = Line(origin + RIGHT * 3.6 + UP * 2.4, origin + RIGHT * 5.0 + UP * 3.4, color=YELLOW)
        c_lab = Tex("compound").scale(0.8).shift(band_shift(3) + RIGHT * 1.4 + UP * 1.3)
        self.play(Create(c1))
        self.play(Create(c2))
        self.play(Create(c3), Write(c_lab))
        self.wait(2)
        b3_l1 = MathTex(r"\text{5 yrs: } 11\;000 \text{ vs } 8\;000 \times 1,075^5 = 11\;485,03").scale(0.9).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): Sipho's bank statement ---
        self.next_band(4)
        b4_title = Tex("The bank statement: a diary in date order").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        stmt = Rectangle(width=8.6, height=4.4).shift(band_shift(4) + DOWN * 0.7)
        self.play(Create(stmt))
        s_l1 = MathTex(r"\text{Opening balance: } 1\;240,75").scale(0.95).shift(band_shift(4) + UP * 0.9)
        s_l2 = MathTex(r"\text{Pay } +3\;850,00 \to 5\;090,75").scale(0.95).shift(band_shift(4) + UP * 0.1)
        s_l3 = MathTex(r"\text{Debit order } -450,00 \to 4\;640,75").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        s_l4 = MathTex(r"\text{ATM } -500,00; \text{ fee } -9,00 \to 4\;131,75").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        s_l5 = MathTex(r"\text{Admin fee } -6,50 \to \text{closing } 4\;125,25").scale(0.95).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(s_l1)); self.wait(2)
        self.play(Write(s_l2)); self.wait(2)
        self.play(Write(s_l3)); self.wait(2)
        self.play(Write(s_l4)); self.wait(2)
        self.play(Write(s_l5))
        self.play(Create(SurroundingRectangle(s_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the fee hunt and the check ---
        self.next_band(5)
        b5_title = Tex("Hunt the fees, prove the balance").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Fees: } 9,00 + 6,50 = \text{R15,50}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"\text{A year of that: } 15,50 \times 12 = \text{R186,00}").scale(1.05).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex("Closing = opening + credits $-$ debits").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = MathTex(r"1\;240,75 + 3\;850 - 450 - 500 - 9 - 6,50").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        b5_l5 = MathTex(r"= \text{R4 125,25}").scale(1.1).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        self.play(Write(b5_l3)); self.wait(2)
        self.play(Write(b5_l4)); self.wait(2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): inflation compounds the loaf ---
        self.next_band(6)
        b6_title = Tex("Inflation: compound growth against you").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"19,50 \times 1,06 = \text{R20,67}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"20,67 \times 1,06 = \text{R21,91}").scale(1.05).shift(band_shift(6) + UP * 0.2)
        b6_l3 = Tex("R100: five loaves today, four in two years").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = MathTex(r"1,06^{10} \approx 1,79 \text{: prices nearly double}").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        b6_l5 = MathTex(r"\text{R100 keeps only R55,84 of power}").scale(1.05).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l1)); self.wait(2)
        self.play(Write(b6_l2)); self.wait(2)
        self.play(Write(b6_l3)); self.wait(2)
        self.play(Write(b6_l4)); self.wait(2)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the raise that was a pay cut ---
        self.next_band(7)
        b7_title = Tex("An increase below inflation is a decrease").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"9\;000 \times 1,04 = \text{R9 360}").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Keeping up needed } 9\;000 \times 1,06 = 9\;540").scale(1.0).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"9\;540 - 9\;360 = \text{R180 a month behind}").scale(1.05).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = Tex("Ask: did it grow faster than prices?").scale(1.05).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l1)); self.wait(2.5)
        self.play(Write(b7_l2)); self.wait(2.5)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b7_l4)); self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the two workers ---
        self.next_band(8)
        b8_title = Tex("The two ways money grows").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex("Simple: a worker who only sees the R8 000").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"\text{Same R600 delivery, every year}").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("Compound: a worker who grows the whole pot").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = MathTex(r"600, \text{ then } 645, \text{ then } 693,38").scale(1.05).shift(band_shift(8) + DOWN * 1.6)
        b8_l5 = MathTex(r"\text{R9 938,38 vs R9 800: snowball wins}").scale(1.05).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l1)); self.wait(3)
        self.play(Write(b8_l2)); self.wait(3)
        self.play(Write(b8_l3)); self.wait(3)
        self.play(Write(b8_l4)); self.wait(3)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the statement on the kitchen table ---
        self.next_band(9)
        b9_title = Tex("The statement on the kitchen table").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = Tex("Nobody stole the R6,50 — it's the admin fee").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("R9,00: another bank's ATM charges more").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = MathTex(r"\text{Fees R15,50 a month — a taxi fare}").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = MathTex(r"\text{A year: R186 — school shoes}").scale(1.05).shift(band_shift(9) + DOWN * 1.7)
        b9_l5 = Tex("Rebuild the closing balance to the cent").scale(1.05).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l1)); self.wait(3)
        self.play(Write(b9_l2)); self.wait(3)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(3)
        self.play(Write(b9_l4)); self.wait(3)
        self.play(Write(b9_l5)); self.wait(3)

        # --- Band 10 (subtopic_7): the loaf of bread time machine ---
        self.next_band(10)
        b10_title = Tex("The loaf of bread time machine").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = MathTex(r"19,50 \to 20,67 \to 21,91").scale(1.1).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("The note stands still; its power melts").scale(1.05).shift(band_shift(10) + UP * 0.2)
        b10_l3 = Tex("Earning 7,5\\% against 6\\% inflation: gaining").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        b10_l4 = Tex("A 4\\% raise under 6\\% inflation: a polite pay cut").scale(1.0).shift(band_shift(10) + DOWN * 1.8)
        b10_l5 = Tex("Judge money by what it buys, not its number").scale(1.0).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l1))
        self.play(Create(SurroundingRectangle(b10_l1, color=GREEN)))
        self.wait(3)
        self.play(Write(b10_l2)); self.wait(3)
        self.play(Write(b10_l3)); self.wait(3)
        self.play(Write(b10_l4)); self.wait(3)
        self.play(Write(b10_l5)); self.wait(4)
