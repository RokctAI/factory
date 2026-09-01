# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene for the Friction and Inclined Planes duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (210/240/230/250/185/175/180
# of 1470 s). Exporter-safe mobjects only; add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FrictionInclinedPlanesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the normal force, free-body diagram ---
        title = Tex("Friction and Inclined Planes").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Normal force $N$: perpendicular to the surface").scale(1.0).shift(UP * 1.4)
        self.play(Write(b0_l1))
        self.wait(2.5)
        dot = Dot(DOWN * 0.6)
        aN = Arrow(DOWN * 0.6, UP * 0.9, buff=0, color=YELLOW)
        lN = MathTex(r"N").scale(1.0).shift(UP * 1.0 + RIGHT * 0.5)
        aW = Arrow(DOWN * 0.6, DOWN * 2.1, buff=0, color=YELLOW)
        lW = MathTex(r"w = mg").scale(1.0).shift(DOWN * 2.0 + RIGHT * 1.2)
        self.play(FadeIn(dot))
        self.play(Create(aN), Write(lN))
        self.play(Create(aW), Write(lW))
        self.wait(2.5)
        b0_l2 = Tex("Level floor, nothing else vertical: $N = mg$").scale(0.95).shift(DOWN * 2.9 + LEFT * 1.2)
        self.play(Write(b0_l2))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): N is not always mg ---
        self.next_band(1)
        b1_title = Tex(r"Rope pulls 100 N at 30$^\circ$ above horizontal").scale(1.05).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"N + F\sin\theta - mg = 0").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"N = 490 - 100 \times 0{,}5 = 440\ \text{N}").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = MathTex(r"\text{Pushed down at } 30^\circ: N = 490 + 50 = 540\ \text{N}").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex("Same crate, three different normal forces").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Friction comes from $N$ — get $N$ right first").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l5))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): static vs kinetic ---
        self.next_band(2)
        b2_title = Tex("Two kinds of friction").scale(1.15).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Static: self-adjusting, up to a limit").scale(1.0).shift(band_shift(2) + UP * 1.3)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"f_s^{max} = \mu_s N").scale(1.2).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=BLUE)))
        self.wait(2.5)
        b2_l3 = Tex("Kinetic: constant, once sliding").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"f_k = \mu_k N, \quad \mu_s > \mu_k").scale(1.15).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=BLUE)))
        self.wait(2.5)
        b2_l5 = Tex("No unit; independent of contact area").scale(0.95).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): the 150 N / 200 N test ---
        self.next_band(3)
        b3_title = Tex(r"50 kg crate: $\mu_s = 0{,}4$, $\mu_k = 0{,}3$").scale(1.05).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"N = 50 \times 9{,}8 = 490\ \text{N}").scale(1.0).shift(band_shift(3) + UP * 1.4)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"f_s^{max} = 0{,}4 \times 490 = 196\ \text{N}").scale(1.0).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex(r"Push 150 N $<$ 196 N: stays, $f_s = 150$ N").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_trap = MathTex(r"f = 196\ \text{N}").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_trap))
        self.play(Create(strike(b3_trap)))
        self.wait(2)
        b3_l4 = MathTex(r"\text{Push } 200 > 196: \; f_k = 0{,}3 \times 490 = 147\ \text{N}").scale(0.95).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = MathTex(r"a = \frac{200 - 147}{50} = 1{,}06\ \text{m/s}^2").scale(1.0).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the incline free-body diagram ---
        self.next_band(4)
        b4_title = Tex("On a slope: rotate the axes").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        base = Line(LEFT * 4.2 + DOWN * 1.2, RIGHT * 1.8 + DOWN * 1.2).shift(band_shift(4))
        slope = Line(LEFT * 4.2 + DOWN * 1.2, RIGHT * 1.8 + UP * 1.8).shift(band_shift(4))
        lang = MathTex(r"\theta").scale(0.9).shift(band_shift(4) + LEFT * 2.9 + DOWN * 0.85)
        self.play(Create(base), Create(slope), Write(lang))
        d = Dot(band_shift(4) + LEFT * 1.2 + UP * 0.3)
        self.play(FadeIn(d))
        aW = Arrow(LEFT * 1.2 + UP * 0.3, LEFT * 1.2 + DOWN * 1.5, buff=0, color=YELLOW).shift(band_shift(4))
        lW = MathTex(r"mg").scale(0.9).shift(band_shift(4) + LEFT * 0.6 + DOWN * 1.3)
        self.play(Create(aW), Write(lW))
        self.wait(1.5)
        aN = Arrow(LEFT * 1.2 + UP * 0.3, LEFT * 2.0 + UP * 1.9, buff=0, color=YELLOW).shift(band_shift(4))
        lN = MathTex(r"N").scale(0.9).shift(band_shift(4) + LEFT * 2.4 + UP * 2.2)
        self.play(Create(aN), Write(lN))
        self.wait(1.5)
        aF = Arrow(LEFT * 1.2 + UP * 0.3, RIGHT * 0.2 + UP * 1.0, buff=0, color=RED).shift(band_shift(4))
        lF = MathTex(r"f").scale(0.9).shift(band_shift(4) + RIGHT * 0.6 + UP * 1.3)
        self.play(Create(aF), Write(lF))
        self.wait(2)
        b4_l1 = MathTex(r"\text{Along slope: } mg\sin\theta").scale(1.0).shift(band_shift(4) + RIGHT * 2.5 + DOWN * 0.2)
        b4_l2 = MathTex(r"\text{Into slope: } mg\cos\theta").scale(1.0).shift(band_shift(4) + RIGHT * 2.5 + DOWN * 1.0)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("Weight points straight down, always").scale(0.95).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l3))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): N on a slope ---
        self.next_band(5)
        b5_l1 = MathTex(r"\text{Perpendicular balance: } N = mg\cos\theta").scale(1.05).shift(band_shift(5) + UP * 2.0)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=BLUE)))
        self.wait(2.5)
        b5_l2 = Tex("On an incline $N$ is ALWAYS less than $mg$").scale(1.0).shift(band_shift(5) + UP * 0.9)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_trap = MathTex(r"N = mg \text{ on a slope}").scale(1.0).shift(band_shift(5) + DOWN * 0.1)
        self.play(Write(b5_trap))
        self.play(Create(strike(b5_trap)))
        self.wait(2)
        b5_l3 = MathTex(r"f = \mu\,mg\cos\theta, \text{ not } \mu\,mg").scale(1.05).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex("Declare the positive direction before starting").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): components and the slipping test ---
        self.next_band(6)
        b6_title = Tex(r"20 kg on a 30$^\circ$ ramp: $\mu_s = 0{,}55$, $\mu_k = 0{,}25$").scale(1.0).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"w = 20 \times 9{,}8 = 196\ \text{N}").scale(1.0).shift(band_shift(6) + UP * 1.4)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"mg\sin\theta = 196 \times 0{,}5 = 98\ \text{N}").scale(1.0).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"N = mg\cos\theta = 196 \times 0{,}866 = 169{,}7\ \text{N}").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"f_s^{max} = 0{,}55 \times 169{,}7 = 93{,}3\ \text{N}").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex(r"98 N $>$ 93,3 N — the crate slides").scale(1.0).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): sliding down, dragged up ---
        self.next_band(7)
        b7_l1 = MathTex(r"f_k = 0{,}25 \times 169{,}7 = 42{,}4\ \text{N up-slope}").scale(0.95).shift(band_shift(7) + UP * 2.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"a = \frac{98 - 42{,}4}{20} = 2{,}78\ \text{m/s}^2 \text{ down}").scale(1.0).shift(band_shift(7) + UP * 0.9)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("Dragged UP at constant $v$: net force zero").scale(0.95).shift(band_shift(7) + DOWN * 0.2)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Friction reverses — now DOWN the slope").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = MathTex(r"T = 98 + 42{,}4 = 140{,}4\ \text{N}").scale(1.05).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): the tangent shortcut ---
        self.next_band(8)
        b8_title = Tex("On the point of slipping").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"mg\sin\theta = \mu_s\,mg\cos\theta").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\tan\theta = \mu_s \quad \text{(mass cancels)}").scale(1.1).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=BLUE)))
        self.wait(2.5)
        b8_l3 = MathTex(r"\tan 30^\circ = 0{,}577 > 0{,}55 \Rightarrow \text{slides}").scale(1.0).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("True for 20 kg or 200 kg — mass is gone").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l4))
        self.wait(2.5)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): grip, and why it runs out ---
        self.next_band(9)
        b9_title = Tex("Grip, and why it runs out").scale(1.2).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("The wardrobe matches you, push for push").scale(0.95).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Until the grip limit — then it lurches free").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{Limit: } 0{,}4 \times 490 = 196\ \text{N}").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Push 150 N: friction is 150 N, not 196 N").scale(0.95).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = MathTex(r"\text{Push } 200: \; a = \frac{200 - 147}{50} = 1{,}06\ \text{m/s}^2").scale(0.95).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_6): gravity split into two piles ---
        self.next_band(10)
        b10_title = Tex("Gravity split into two piles").scale(1.2).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Sliding pile: weight $\times \sin\theta$ (down the slope)").scale(0.95).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex(r"Pressing pile: weight $\times \cos\theta$ (into the ramp)").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"196\ \text{N}: \; 98\ \text{N slide}, \; 169{,}7\ \text{N press}").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("The ramp pushes back with the SMALLER number").scale(0.95).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("Steeper hill, less grip").scale(1.0).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_7): will it slide? ---
        self.next_band(11)
        b11_title = Tex("Will it slide? The quick test").scale(1.15).shift(band_shift(11) + UP * 2.3)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex(r"Sliding pile 98 N vs grip 93,3 N — gravity wins").scale(0.95).shift(band_shift(11) + UP * 1.3)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"a = \frac{98 - 42{,}4}{20} = 2{,}78\ \text{m/s}^2 \text{ down}").scale(1.0).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = Tex("Pulled up steadily: friction turns around").scale(0.95).shift(band_shift(11) + DOWN * 0.8)
        self.play(Write(b11_l3))
        self.wait(2)
        b11_l4 = MathTex(r"98 + 42{,}4 = 140{,}4\ \text{N to beat}").scale(1.0).shift(band_shift(11) + DOWN * 1.7)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        self.wait(2.5)
        b11_l5 = Tex(r"No mass needed: $\tan\theta > \mu_s$ means it slides").scale(0.95).shift(band_shift(11) + DOWN * 2.8)
        self.play(Write(b11_l5))
        self.wait(4)
