# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from manim import *

# Band-layout whiteboard scene for "Work and the Work-Energy Theorem"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only; free-body and ramp diagrams hand-built
# from Dot/Rectangle/Line/Arrow/Tex. Write-only reveals.
# Subtopic durations 230/230/235/245/190/195/195 of 1520 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class WorkEnergyTheoremSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the definition and the cosine families ---
        title = Tex("Work and the Work-Energy Theorem").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_eq = MathTex(r"W = F \, \Delta x \, \cos\theta \;\; [\text{J}]").scale(1.2).shift(UP * 1.1)
        self.play(Write(b0_eq))
        self.play(Create(SurroundingRectangle(b0_eq, color=GREEN)))
        self.wait(2.5)
        b0_l1 = Tex(r"$\theta = 0$: $\cos\theta = 1$ — positive, pumps energy in").scale(1.0).shift(UP * 0.0)
        b0_l2 = Tex(r"$\theta = 180$: $\cos\theta = -1$ — siphons energy out").scale(1.0).shift(DOWN * 0.9)
        b0_l3 = Tex(r"$\theta = 90$: $\cos\theta = 0$ — NO work at all").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Work is a SCALAR — size, no direction").scale(1.0).shift(DOWN * 2.8)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): one bag, three families of work ---
        self.next_band(1)
        b1_title = Tex("Compost bag: 60 N applied, 25 N friction, 8 m").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"W_{applied} = 60 \times 8 \times 1 = +480\ \text{J}").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"W_{friction} = 25 \times 8 \times (-1) = -200\ \text{J}").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"W_{N} = W_{w} = 0 \;\; (\cos 90 = 0)").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2.5)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_wrong = Tex("Wheeling a suitcase works on it").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_rule = Tex("Tiredness is not work — only force along motion").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_rule))
        self.play(Create(SurroundingRectangle(b1_rule, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): net work from the free-body diagram ---
        self.next_band(2)
        b2_title = Tex("Net work: the free-body inventory").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        c2 = band_shift(2) + LEFT * 3.5 + UP * 0.3
        body = Dot(c2, radius=0.12)
        self.play(FadeIn(body))
        a_app = Arrow(c2, c2 + RIGHT * 2.2, buff=0, color=GREEN)
        lab_app = Tex("60 N").scale(0.8).shift(c2 + RIGHT * 2.5 + UP * 0.35)
        a_fric = Arrow(c2, c2 + LEFT * 1.2, buff=0, color=RED)
        lab_fric = Tex("25 N").scale(0.8).shift(c2 + LEFT * 1.6 + UP * 0.35)
        a_n = Arrow(c2, c2 + UP * 1.4, buff=0, color=BLUE)
        lab_n = Tex("$N$").scale(0.8).shift(c2 + UP * 1.7 + RIGHT * 0.3)
        a_w = Arrow(c2, c2 + DOWN * 1.4, buff=0, color=BLUE)
        lab_w = Tex("$w$").scale(0.8).shift(c2 + DOWN * 1.7 + RIGHT * 0.3)
        self.play(Create(a_app), Write(lab_app))
        self.play(Create(a_fric), Write(lab_fric))
        self.play(Create(a_n), Write(lab_n))
        self.play(Create(a_w), Write(lab_w))
        self.wait(2)
        b2_l1 = MathTex(r"W_{net} = 480 - 200 + 0 + 0 = 280\ \text{J}").scale(1.0).shift(band_shift(2) + RIGHT * 2.7 + UP * 1.0)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{or: } F_{net} = 35\ \text{N}, \; 35 \times 8 = 280\ \text{J}").scale(0.95).shift(band_shift(2) + RIGHT * 2.7 + UP * 0.0)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("Every arrow pays a work term,").scale(1.0).shift(band_shift(2) + DOWN * 2.2)
        b2_l4 = Tex("even when the term is zero").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): the theorem, forward and in reverse ---
        self.next_band(3)
        b3_eq = MathTex(r"W_{net} = \Delta E_k = \tfrac{1}{2}mv_f^2 - \tfrac{1}{2}mv_i^2").scale(0.95).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_eq))
        self.play(Create(SurroundingRectangle(b3_eq, color=GREEN)))
        self.wait(2.5)
        b3_l1 = MathTex(r"280 = \tfrac{1}{2} \times 15 \times v_f^2").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"v_f = \sqrt{37{,}33} = 6{,}11\ \text{m·s}^{-1}").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex(r"Braking: 1 200 kg at 25 m$\cdot$s$^{-1}$, stops in 62,5 m").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = MathTex(r"\Delta E_k = -375\,000\ \text{J}").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = MathTex(r"-F \times 62{,}5 = -375\,000 \Rightarrow F = 6\,000\ \text{N}").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_4): the ramp, force balance ---
        self.next_band(4)
        b4_title = Tex(r"Ramp: 25 kg, 6 m, $30^\circ$, constant velocity").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        # Ramp sketch: slope line, crate, up-slope and down-slope arrows.
        base4 = band_shift(4) + LEFT * 5.2 + DOWN * 0.9
        ramp = Line(base4, base4 + RIGHT * 4.2 + UP * 2.4)
        ground = Line(base4, base4 + RIGHT * 4.2)
        self.play(Create(ground), Create(ramp))
        crate = Square(side_length=0.55).rotate(0.52).move_to(base4 + RIGHT * 2.1 + UP * 1.5)
        self.play(Create(crate))
        a_up = Arrow(base4 + RIGHT * 2.4 + UP * 1.7, base4 + RIGHT * 3.6 + UP * 2.4, buff=0, color=GREEN)
        lab_up = Tex("$F$").scale(0.8).shift(base4 + RIGHT * 3.9 + UP * 2.7)
        a_dn = Arrow(base4 + RIGHT * 1.8 + UP * 1.3, base4 + RIGHT * 0.6 + UP * 0.6, buff=0, color=RED)
        lab_dn = Tex("$f + mg\\sin\\theta$").scale(0.75).shift(base4 + RIGHT * 0.6 + UP * 1.3)
        self.play(Create(a_up), Write(lab_up))
        self.play(Create(a_dn), Write(lab_dn))
        self.wait(2)
        b4_l1 = MathTex(r"mg\sin\theta = 25 \times 9{,}8 \times 0{,}5 = 122{,}5\ \text{N}").scale(0.95).shift(band_shift(4) + RIGHT * 2.9 + UP * 0.6)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"F = 122{,}5 + 35 = 157{,}5\ \text{N}").scale(1.0).shift(band_shift(4) + RIGHT * 2.9 + DOWN * 0.4)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        b4_l3 = Tex("Constant velocity: net force zero").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l3))
        self.wait(3)

        # --- Band 5 (subtopic_4): the work audit over 6 m ---
        self.next_band(5)
        b5_title = Tex("The work audit over the 6 m").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"W_F = 157{,}5 \times 6 = +945\ \text{J}").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = MathTex(r"W_{gravity} = -122{,}5 \times 6 = -735\ \text{J}").scale(1.0).shift(band_shift(5) + UP * 0.3)
        b5_l3 = MathTex(r"W_{friction} = -35 \times 6 = -210\ \text{J}, \;\; W_N = 0").scale(0.95).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"W_{net} = 945 - 735 - 210 = 0\ \text{J}").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex("Constant $v$: $\\Delta E_k = 0$ — the check agrees").scale(0.95).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l5))
        self.wait(2)
        b5_l6 = Tex("Gravity's 735 J became $E_p$: rose 3 m").scale(0.95).shift(band_shift(5) + DOWN * 3.3)
        self.play(Write(b5_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): work is not effort ---
        self.next_band(6)
        b6_title = Tex("Work is not effort").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Hold a crate of tiles still: ZERO work").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("Carry it level down the corridor: still zero").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Lift it onto the trailer: positive work").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = Tex("Lower it gently: NEGATIVE — you drain it").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_rule = Tex("Along: $+$. Against: $-$. Sideways: 0.").scale(1.05).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_rule))
        self.play(Create(SurroundingRectangle(b6_rule, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): the energy bank account ---
        self.next_band(7)
        b7_title = Tex("The energy bank account").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Balance $= \\tfrac{1}{2}mv^2$; net work moves it").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("Double the speed: FOUR times the balance").scale(1.0).shift(band_shift(7) + UP * 0.2)
        b7_l3 = Tex("Same brakes: four times the stopping distance").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Given a DISTANCE: think work-energy").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        b7_l5 = Tex("Given a TIME: think impulse and momentum").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_7): why ramps feel easier ---
        self.next_band(8)
        b8_title = Tex("Why ramps feel easier").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_wrong = Tex("The plank reduces the work").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_wrong))
        self.play(Create(strike(b8_wrong)))
        self.wait(2)
        b8_l1 = Tex("A sixth of the force, six times the path:").scale(1.0).shift(band_shift(8) + UP * 0.1)
        b8_l2 = Tex("same work — a payment plan, not a discount").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Gravity bills the HEIGHT gained;").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        b8_l4 = Tex("friction bills every metre TRAVELLED").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(4)
