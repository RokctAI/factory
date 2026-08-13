from manim import *

# Band-layout whiteboard scene for gravitational-potential-energy
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects only; add-only lifecycle; the 2 kg brick problem
# worked line by line with the script's exact numbers and units; the
# reference-level sketch hand-built from Lines/Rectangles/Tex.
# Time apportioned to subtopics.json (225/235/235/250/180/175/175 of 1475 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GravitationalPotentialEnergySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): energy stored by position ---
        title = Tex("Gravitational Potential Energy").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        a1 = Tex("Energy: the capacity to do work (joule, J)").scale(1.0).shift(UP * 1.0)
        self.play(Write(a1))
        self.wait(2)
        a2 = Tex("$E_p$: energy stored by POSITION").scale(1.05).shift(UP * 0.1)
        self.play(Write(a2))
        self.wait(2)
        a3 = MathTex(r"E_p = mgh").scale(1.3).shift(DOWN * 0.9)
        self.play(Write(a3))
        self.play(Create(SurroundingRectangle(a3, color=GREEN)))
        self.wait(2.5)
        a4 = Tex("$mg$ = weight; $\\times\\, h$ = the lifting bill").scale(1.0).shift(DOWN * 1.9)
        self.play(Write(a4))
        self.wait(2)
        a5 = Tex("A scalar: joules never point anywhere").scale(1.0).shift(DOWN * 2.8)
        self.play(Write(a5))
        self.wait(3)

        # --- Band 1 (subtopic_2): pricing the 5 m lift ---
        self.next_band(1)
        b1_t = Tex("2 kg brick lifted 5 m").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_1 = MathTex(r"m = 2\ \text{kg}, \; g = 9{,}8\ \text{m·s}^{-2}, \; h = 5\ \text{m}").scale(0.95).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_1))
        self.wait(2)
        b1_2 = MathTex(r"E_p = mgh = 2 \times 9{,}8 \times 5").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_2))
        self.wait(2)
        b1_3 = MathTex(r"2 \times 9{,}8 = 19{,}6 \; \text{(the weight, N)}").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_3))
        self.wait(2)
        b1_4 = MathTex(r"E_p = 19{,}6 \times 5 = 98\ \text{J}").scale(1.1).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_4))
        self.play(Create(SurroundingRectangle(b1_4, color=GREEN)))
        self.wait(2.5)
        b1_5 = Tex(r"Units: N $\times$ m = N·m = J $\checkmark$").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the second platform ---
        self.next_band(2)
        b2_t = Tex("Up to 12 m: the further gain").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_1 = MathTex(r"E_p(12) = 2 \times 9{,}8 \times 12 = 235{,}2\ \text{J}").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_1))
        self.wait(2.5)
        b2_2 = MathTex(r"\Delta E_p = 235{,}2 - 98 = 137{,}2\ \text{J}").scale(1.05).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_2))
        self.wait(2.5)
        b2_3 = Tex("Shorter road: only the extra 7 m").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_3))
        self.wait(1.5)
        b2_4 = MathTex(r"2 \times 9{,}8 \times 7 = 137{,}2\ \text{J}").scale(1.05).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_4))
        self.play(Create(SurroundingRectangle(b2_4, color=GREEN)))
        self.wait(2)
        b2_5 = Tex("Differences care only about height differences").scale(0.9).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_5))
        self.wait(3)

        # --- Band 3 (subtopic_3): the reference level, drawn ---
        self.next_band(3)
        b3_t = Tex("Where does zero live?").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        d = band_shift(3) + DOWN * 0.4
        ground = Line(d + LEFT * 4.2, d + RIGHT * 4.2)
        g_lab = Tex("ground: $h = 0$").scale(0.85).move_to(d + RIGHT * 2.7 + DOWN * 0.4)
        plat = Line(d + UP * 1.8 + LEFT * 2.0, d + UP * 1.8 + RIGHT * 0.4)
        p_lab = Tex("platform: 5 m").scale(0.85).move_to(d + UP * 2.2 + RIGHT * 2.0)
        brick = Rectangle(width=0.7, height=0.45).move_to(d + UP * 2.05 + LEFT * 1.2)
        base = DashedLine(d + DOWN * 1.4 + LEFT * 4.2, d + DOWN * 1.4 + RIGHT * 4.2)
        b_lab = Tex("basement: $-3$ m").scale(0.85).move_to(d + DOWN * 1.8 + RIGHT * 2.4)
        self.play(Create(ground), Write(g_lab))
        self.wait(1.5)
        self.play(Create(plat), Write(p_lab), Create(brick))
        self.wait(1.5)
        self.play(Create(base), Write(b_lab))
        self.wait(2)
        b3_1 = Tex("From the ground: $h = 5$, $E_p = 98$ J").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_1))
        self.wait(3)

        # --- Band 4 (subtopic_3): two bookkeepers agree on differences ---
        self.next_band(4)
        b4_t = Tex("Two bookkeepers, one payout").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_1 = MathTex(r"\text{Basement: } h = 8, \; E_p = 2 \times 9{,}8 \times 8 = 156{,}8\ \text{J}").scale(0.9).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_1))
        self.wait(2.5)
        b4_2 = Tex("Both correct — relative to their own zero").scale(0.95).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_2))
        self.wait(2)
        b4_3 = MathTex(r"\text{Fall: } 156{,}8 - 58{,}8 = 98\ \text{J} = 98 - 0 \; \checkmark").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_3))
        self.play(Create(SurroundingRectangle(b4_3, color=GREEN)))
        self.wait(2.5)
        b4_4 = Tex("Declare your zero; below it $E_p$ is negative").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_4))
        self.wait(2)
        b4_5 = Tex("Never mix reference levels mid-problem").scale(0.95).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_5))
        self.wait(3)

        # --- Band 5 (subtopic_4): the four-step method ---
        self.next_band(5)
        b5_t = Tex("The method, four steps").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_1 = Tex("1. List $m$, $g$, $h$ — converting as you list").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_2 = Tex("2. Declare the reference level").scale(1.0).shift(band_shift(5) + UP * 0.3)
        b5_3 = Tex("3. Substitute into $E_p = mgh$, carry units").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        b5_4 = Tex("4. Sense-check; changes use $\\Delta h$ directly").scale(1.0).shift(band_shift(5) + DOWN * 1.3)
        for m in (b5_1, b5_2, b5_3, b5_4):
            self.play(Write(m))
            self.wait(1.8)
        b5_5 = Tex("500 g = 0,5 kg; 250 cm = 2,5 m").scale(0.95).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the traps ---
        self.next_band(6)
        b6_t = Tex("The classic traps").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_trap = MathTex(r"E_p = 19{,}6 \times 9{,}8 \times 5 \; \text{(weight as } m\text{!)}").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_trap))
        self.play(Create(strike(b6_trap)))
        self.wait(2)
        b6_1 = MathTex(r"\text{Given weight 19,6 N: } m = \frac{19{,}6}{9{,}8} = 2\ \text{kg}").scale(0.95).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_1))
        self.play(Create(SurroundingRectangle(b6_1, color=GREEN)))
        self.wait(2.5)
        b6_2 = Tex("Slope: $h$ is VERTICAL rise only —").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        b6_3 = Tex("10 m ramp rising 3 m charges for 3").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_2))
        self.wait(1.5)
        self.play(Write(b6_3))
        self.wait(2)
        b6_4 = Tex("No direction on energy; $g = 9{,}8$, never 10").scale(0.95).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the bank account in the sky ---
        self.next_band(7)
        b7_t = Tex("The bank account in the sky").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_1 = Tex("Water tower: pump deposits all night,").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_2 = Tex("the tap withdraws in the morning").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_1))
        self.wait(2)
        self.play(Write(b7_2))
        self.wait(2)
        b7_3 = Tex("Lifting = depositing; falling = payout").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_3))
        self.wait(2)
        b7_4 = MathTex(r"E_p = mgh: \; \text{weight} \times \text{height}").scale(1.05).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_4))
        self.play(Create(SurroundingRectangle(b7_4, color=GREEN)))
        self.wait(2)
        b7_5 = Tex("A joule: one apple lifted one metre").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the brick's bank balance ---
        self.next_band(8)
        b8_t = Tex("The brick's bank balance").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_1 = MathTex(r"\text{Weight: } 2 \times 9{,}8 = 19{,}6\ \text{N}").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_1))
        self.wait(2)
        b8_2 = MathTex(r"\text{Deposit: } 19{,}6 \times 5 = 98\ \text{J}").scale(1.05).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_2))
        self.play(Create(SurroundingRectangle(b8_2, color=GREEN)))
        self.wait(2.5)
        b8_3 = MathTex(r"\text{Top-up: } 19{,}6 \times 7 = 137{,}2\ \text{J}").scale(1.0).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_3))
        self.wait(2)
        b8_4 = MathTex(r"\text{Check: } 235{,}2 - 98 = 137{,}2 \; \checkmark").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_4))
        self.wait(2)
        b8_5 = Tex("Hard hats: 235 J pays out in full if it falls").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_5))
        self.wait(3)

        # --- Band 9 (subtopic_7): choosing where zero is ---
        self.next_band(9)
        b9_t = Tex("Choosing where zero is").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_1 = Tex("Ground says 5 m; basement says 8 m").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_1))
        self.wait(2)
        b9_2 = Tex("98 J vs 156,8 J — both right, own zero").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_2))
        self.wait(2)
        b9_3 = Tex("Nature only pays out DIFFERENCES").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_3))
        self.play(Create(SurroundingRectangle(b9_3, color=GREEN)))
        self.wait(2)
        b9_4 = Tex("Declare zero once; lowest point is friendly;").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        b9_5 = Tex("below zero = overdrawn, and that is fine").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_4))
        self.wait(2)
        self.play(Write(b9_5))
        self.wait(4)
