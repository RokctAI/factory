from manim import *

# Band-layout whiteboard scene for "Transverse Waves and Their Quantities"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects only; write-only reveals; camera moves down band by
# band. Band time apportioned to subtopics.json
# (215/225/250/220/180/190/190 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TransverseWavesQuantitiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): pulse to wave ---
        title = Tex("Transverse Waves and Their Quantities").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Pulse: a single disturbance that travels").scale(1.05).shift(UP * 1.1)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("particles move perpendicular to travel").scale(1.0).shift(UP * 0.2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("repeat the flick: a train of pulses = a WAVE").scale(1.0).shift(DOWN * 0.7)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("energy is transferred; matter is not").scale(1.0).shift(DOWN * 1.7)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        b0_l5 = Tex("meeting pulses add with signs, then pass on").scale(0.95).shift(DOWN * 2.7)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_2): the labelled wave picture ---
        self.next_band(1)
        b1_t = Tex("Crest, trough, amplitude, wavelength").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        rest = DashedLine(band_shift(1) + LEFT * 4.5 + UP * 0.3, band_shift(1) + RIGHT * 4.5 + UP * 0.3)
        self.play(Create(rest))
        # two full waves as a polyline
        pts = [LEFT * 4.0 + UP * 0.3, LEFT * 3.0 + UP * 1.3, LEFT * 2.0 + UP * 0.3,
               LEFT * 1.0 + DOWN * 0.7, RIGHT * 0.0 + UP * 0.3, RIGHT * 1.0 + UP * 1.3,
               RIGHT * 2.0 + UP * 0.3, RIGHT * 3.0 + DOWN * 0.7, RIGHT * 4.0 + UP * 0.3]
        wave = VGroup(*[Line(band_shift(1) + pts[i], band_shift(1) + pts[i + 1], color=BLUE)
                        for i in range(len(pts) - 1)])
        self.play(Create(wave))
        self.wait(1.5)
        crest_lab = Tex("crest").scale(0.8).shift(band_shift(1) + LEFT * 3.0 + UP * 1.8)
        trough_lab = Tex("trough").scale(0.8).shift(band_shift(1) + LEFT * 1.0 + DOWN * 1.2)
        self.play(Write(crest_lab), Write(trough_lab))
        self.wait(1.5)
        amp = Arrow(band_shift(1) + RIGHT * 1.0 + UP * 0.3, band_shift(1) + RIGHT * 1.0 + UP * 1.3,
                    buff=0, color=GREEN)
        amp_lab = Tex("$A$").scale(0.9).shift(band_shift(1) + RIGHT * 1.5 + UP * 0.8)
        self.play(Create(amp), Write(amp_lab))
        lam = Arrow(band_shift(1) + LEFT * 3.0 + DOWN * 1.6, band_shift(1) + RIGHT * 1.0 + DOWN * 1.6,
                    buff=0, color=YELLOW)
        lam_lab = MathTex(r"\lambda \;\text{(crest to crest)}").scale(0.9).shift(band_shift(1) + LEFT * 1.0 + DOWN * 2.2)
        self.play(Create(lam), Write(lam_lab))
        self.wait(2)
        b1_l1 = Tex("crest-to-trough is TWO amplitudes").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l1))
        self.wait(3)

        # --- Band 2 (subtopic_2): in phase, out of phase ---
        self.next_band(2)
        b2_t = Tex("In phase, out of phase").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("$\\lambda$: distance between successive points").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("IN PHASE — same displacement, same motion").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("out of phase: crest against trough,").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        b2_l4 = Tex("an odd number of half wavelengths apart").scale(1.0).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("$A$ across the travel; $\\lambda$ along it").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): period, frequency, float example ---
        self.next_band(3)
        b3_t = Tex("Timing: period and frequency").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("$T$: time for ONE wave to pass, in s").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("$f$: waves per second, in Hz").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"f = \frac{1}{T} \qquad T = \frac{1}{f}").scale(1.15).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"f = \frac{15}{5} = 3\;\text{Hz}").scale(1.05).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = MathTex(r"T = \frac{1}{3} = 0{,}33\;\text{s}").scale(1.05).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the wave equation, both ways ---
        self.next_band(4)
        b4_t = Tex("The wave equation").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"v = f\lambda").scale(1.3).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"3\;\text{cm} = 0{,}03\;\text{m}").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(1.5)
        b4_l3 = MathTex(r"v = (20)(0{,}03) = 0{,}6\;\text{m·s}^{-1}").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = MathTex(r"f = \frac{1}{0{,}5} = 2\;\text{Hz}").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = MathTex(r"\lambda = \frac{v}{f} = \frac{1{,}5}{2} = 0{,}75\;\text{m}").scale(1.05).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): the four traps ---
        self.next_band(5)
        b5_t = Tex("The traps that cost marks").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"v = (20)(3) \quad \text{(cm not converted)}").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.play(Create(strike(b5_l1)))
        self.wait(2)
        b5_l2 = Tex("amplitude read crest-to-trough: double!").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(strike(b5_l2)))
        self.wait(2)
        b5_l3 = MathTex(r"T = 0{,}25\;\text{s} \;\Rightarrow\; f = 4\;\text{Hz}").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("units next to every number stop the swap").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): graphs and the speed misconception ---
        self.next_band(6)
        b6_t = Tex("Read the horizontal axis first").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex(r"vs POSITION: repeat distance is $\lambda$").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("vs TIME: repeat interval is $T$").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("``higher $f$ means faster wave''").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.play(Create(strike(b6_l3)))
        self.wait(2)
        b6_l4 = Tex("source sets $f$; medium sets $v$;").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        b6_l5 = Tex("the wavelength adjusts").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the wave in the stands ---
        self.next_band(7)
        b7_t = Tex("The wave in the stands").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("people go UP and DOWN; the wave goes").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("SIDEWAYS round the ground: transverse").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("one ripple: a pulse; over and over: a wave").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("what travelled was the ENERGY, not people").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the skipping rope measurements ---
        self.next_band(8)
        b8_t = Tex("Measuring with a skipping rope").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("amplitude: rest line to hump-top —").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("NOT top to bottom, that is two").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("wavelength: hump-top to next hump-top").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("period: how long one hump takes;").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = Tex("frequency: how many pass per second").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = MathTex(r"4 \text{ per second} \;\Rightarrow\; \tfrac{1}{4}\;\text{s each}").scale(1.0).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_7): one sum that does everything ---
        self.next_band(9)
        b9_t = Tex("One sum that does everything").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("humps per second $\\times$ length of each").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"v = (20)(0{,}03) = 0{,}6\;\text{m·s}^{-1}").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2)
        b9_l3 = MathTex(r"T = 0{,}5\;\text{s} \;\Rightarrow\; f = 2\;\text{Hz}").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"\lambda = \frac{1{,}5}{2} = 0{,}75\;\text{m}").scale(1.05).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("convert first, multiply second, check axis").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l5))
        self.wait(4)
