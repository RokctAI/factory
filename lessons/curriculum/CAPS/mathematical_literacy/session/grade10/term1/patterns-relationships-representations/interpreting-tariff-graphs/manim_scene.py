from manim import *

# BAND LAYOUT: sequential vertical bands, one frame-height each; the camera
# moves down between teaching steps and nothing is ever removed. Only
# exporter-supported mobjects (Tex/MathTex, Line/Arrow, Dot,
# SurroundingRectangle) with write-only reveals — no sub-part transforms.
# The tariff graph is hand-built from Arrows (axes), Lines (the two tariff
# lines) and Dots/Tex (labels) — no Axes/NumberPlane.
#
# Mirrors script.md across the seven subtopics of the duo (Part 1 — Expert:
# subtopics 1-4; Part 2 — Simplifier: 5-7); band time proportional to
# subtopics.json.

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


class InterpretingTariffGraphsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the two tariff options ---
        title = Tex("Interpreting Tariff Graphs").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Option A: no fixed fee, R2,00 per kWh").scale(1.05).shift(UP * 1.0)
        l02 = Tex("Option B: R150 fixed + R1,50 per kWh").scale(1.05).shift(UP * 0.1)
        self.play(Write(l01))
        self.wait(2)
        self.play(Write(l02))
        self.wait(2.5)
        l03 = Tex("Read the axes first: usage (kWh) across,").scale(1.0).shift(DOWN * 1.0)
        l04 = Tex("monthly cost (rands) up").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(l03))
        self.play(Write(l04))
        self.wait(2)
        l05 = Tex("The intercept is always the fixed cost").scale(1.05).shift(DOWN * 2.8)
        self.play(Write(l05))
        self.play(Create(SurroundingRectangle(l05, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the graph itself ---
        self.next_band(1)
        b1_t = Tex("Two lines, one set of axes").scale(1.15).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_t))
        self.wait(1.5)
        origin = band_shift(1) + DOWN * 2.6 + LEFT * 3.2
        y_ax = Arrow(origin, origin + UP * 4.2, buff=0)
        x_ax = Arrow(origin, origin + RIGHT * 6.6, buff=0)
        x_lab = Tex("kWh").scale(0.8).shift(origin + RIGHT * 6.6 + DOWN * 0.35)
        y_lab = Tex("Rand").scale(0.8).shift(origin + UP * 4.2 + RIGHT * 0.6)
        self.play(Create(x_ax), Create(y_ax))
        self.play(Write(x_lab), Write(y_lab))
        self.wait(1.5)
        # Scale: 100 kWh = 1.0 across; R100 = 0.3 up.
        line_a = Line(origin, origin + RIGHT * 6.0 + UP * 3.6)
        lab_a = Tex("A").scale(0.9).shift(origin + RIGHT * 5.6 + UP * 3.7)
        self.play(Create(line_a), Write(lab_a))
        b1_l1 = Tex("A starts at 0: use nothing, pay nothing").scale(0.9).shift(band_shift(1) + UP * 1.7)
        self.play(Write(b1_l1))
        self.wait(2)
        line_b = Line(origin + UP * 0.45, origin + RIGHT * 6.0 + UP * 3.15)
        lab_b = Tex("B").scale(0.9).shift(origin + RIGHT * 6.3 + UP * 3.1)
        self.play(Create(line_b), Write(lab_b))
        dot_b0 = Dot(origin + UP * 0.45, radius=0.07)
        b1_r150 = Tex("R150").scale(0.7).shift(origin + UP * 0.45 + LEFT * 0.6)
        self.play(Create(dot_b0), Write(b1_r150))
        b1_l2 = Tex("B starts at R150: the fixed charge").scale(0.9).shift(band_shift(1) + UP * 0.9 + RIGHT * 2.2)
        self.play(Write(b1_l2))
        self.wait(2)
        cross = Dot(origin + RIGHT * 3.0 + UP * 1.8, radius=0.08, color=YELLOW)
        self.play(Create(cross))
        b1_l3 = Tex("They cross — the decision lives there").scale(0.9).shift(origin + RIGHT * 3.4 + UP * 0.6)
        self.play(Write(b1_l3))
        self.wait(3)

        # --- Band 2 (subtopic_2): gradient = price per unit ---
        self.next_band(2)
        b2_t = Tex("Gradient: what ``steeper'' means in rands").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("On A, from 100 to 200 kWh:").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{rise } = 400 - 200 = 200").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"\frac{200}{100} = 2 \;\; \text{(R2,00 per kWh)}").scale(1.1).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("A: intercept 0, gradient 2").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        b2_l5 = Tex("B: intercept 150, gradient 1,5").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l4))
        self.wait(1.5)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_3): break-even, read and verified ---
        self.next_band(3)
        b3_t = Tex("Break-even: read it, then prove it").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("Crossing: 300 kWh at R600").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"A: \; 300 \times 2 = 600").scale(1.05).shift(band_shift(3) + UP * 0.3)
        b3_l3 = MathTex(r"B: \; 150 + 300 \times 1{,}5 = 150 + 450 = 600").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Left of 300: A cheaper (no entrance fee)").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        b3_l5 = Tex("Right of 300: B cheaper (50c saved per unit)").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_4): the 450 kWh question ---
        self.next_band(4)
        b4_t = Tex("Which is cheaper at 450 kWh?").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("450 is past break-even — expect B").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"A: \; 450 \times 2 = 900").scale(1.1).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"B: \; 150 + 450 \times 1{,}5 = 150 + 675 = 825").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex("Option B is cheaper by R900 $-$ R825 = R75").scale(1.05).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex("Always state the saving, not just the winner").scale(0.95).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): the six-step exam method ---
        self.next_band(5)
        b5_t = Tex("The exam method").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        steps = [
            "1. Read the axes: variables, units, scale",
            "2. Intercept = fixed cost, names each line",
            "3. Gradient = price per unit",
            "4. Crossing = break-even; verify by calc",
            "5. Zones: name the winner on each side",
            "6. Read vertically, confirm with arithmetic",
        ]
        for i, s in enumerate(steps):
            m = Tex(s).scale(0.95).shift(band_shift(5) + UP * (1.2 - 0.8 * i))
            self.play(Write(m))
            self.wait(1.6)
        b5_end = Tex("Then sense-check against life").scale(1.0).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_end))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): day pass vs membership ---
        self.next_band(6)
        b6_t = Tex("The day pass and the membership").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("A: no joining fee, R2,00 each visit").scale(1.05).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("B: R150 to join, then R1,50 each").scale(1.05).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("At zero units: A owes R0, B owes R150").scale(1.05).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("The starting height IS the joining fee").scale(1.05).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("Exam name: the vertical intercept").scale(1.0).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_6): how fast your money leaves ---
        self.next_band(7)
        b7_t = Tex("How fast your money leaves").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Two taps filling one bucket —").scale(1.05).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("A empties your pocket at R2,00 a unit").scale(1.05).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Read the price off the line:").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = MathTex(r"\frac{400 - 200}{200 - 100} = \frac{200}{100} = 2").scale(1.05).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("Say steepness in rands per unit").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_7): where the lines swap places ---
        self.next_band(8)
        b8_t = Tex("Where the lines swap places").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("R150 to make back, saving 50c a unit:").scale(1.0).shift(band_shift(8) + UP * 1.3)
        b8_l2 = MathTex(r"150 \div 0{,}50 = 300 \text{ units}").scale(1.05).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Under 300: A wins. Over 300: B wins.").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("At 450: A = R900, B = R825 — B by R75").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = MathTex(r"\text{Check: } 450 \times 0{,}50 - 150 = 225 - 150 = 75").scale(0.95).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.wait(4)
