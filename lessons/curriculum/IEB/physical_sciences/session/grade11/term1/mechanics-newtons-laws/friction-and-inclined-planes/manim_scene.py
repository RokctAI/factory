# Copyright (c) 2026 RokctAI
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

# Band-layout whiteboard scene for the Friction and Inclined Planes duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (210/240/230/250/185/175/180
# of 1470 s). Exporter-safe mobjects only; add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class FrictionInclinesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the normal force ---
        title = Tex("Friction and Inclined Planes").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Normal force N: surface push,").scale(1.0).shift(UP * 1.1)
        b0_l2 = Tex("PERPENDICULAR to the surface").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(VGroup(b0_l1, b0_l2), color=BLUE)))
        self.wait(2.5)
        b0_l3 = Tex("$N = mg$ is a special case, not a rule").scale(0.95).shift(DOWN * 0.8)
        self.play(Write(b0_l3))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): three normal forces ---
        self.next_band(1)
        b1_title = Tex("40 kg box, 80 N rope at 25$^\\circ$").scale(1.05).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{no rope: } N = 40 \times 9{,}8 = 392\ \text{N}").scale(0.95).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"\text{rope up: } N = 392 - 80\sin 25^\circ = 358{,}2\ \text{N}").scale(0.95).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"\text{rope down: } N = 392 + 33{,}8 = 425{,}8\ \text{N}").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex("Friction is built on N — get N right first").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): two frictions ---
        self.next_band(2)
        b2_title = Tex("Static vs kinetic friction").scale(1.15).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"f_s \le \mu_s N \quad\text{(self-adjusting, has a ceiling)}").scale(0.95).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"f_k = \mu_k N \quad\text{(constant while sliding)}").scale(0.95).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=BLUE)))
        self.wait(2.5)
        b2_l3 = Tex(r"$\mu_s > \mu_k$: starting is harder than keeping going").scale(0.95).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("No units; contact area irrelevant").scale(0.95).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): the 60 kg crate ---
        self.next_band(3)
        b3_title = Tex(r"60 kg crate: $\mu_s = 0{,}5$, $\mu_k = 0{,}35$").scale(1.0).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"N = 588\ \text{N}, \quad f_{s,max} = 0{,}5 \times 588 = 294\ \text{N}").scale(0.9).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex("Push 250 N: stays put, friction = 250 N").scale(0.95).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{Push } 320: f_k = 205{,}8, \; F_{net} = 114{,}2\ \text{N}").scale(0.9).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"a = 114{,}2 \div 60 = 1{,}9\ \text{m}\cdot\text{s}^{-2}").scale(0.95).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): rotating the axes ---
        self.next_band(4)
        b4_title = Tex("On a slope: rotate the axes").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        ramp = Line(LEFT * 3.2 + DOWN * 1.8, RIGHT * 2.2 + UP * 0.4, color=WHITE).shift(band_shift(4))
        base = Line(LEFT * 3.2 + DOWN * 1.8, RIGHT * 2.2 + DOWN * 1.8, color=WHITE).shift(band_shift(4))
        self.play(Create(ramp), Create(base))
        aW = Arrow(LEFT * 0.5 + DOWN * 0.7, LEFT * 0.5 + DOWN * 2.5, buff=0, color=YELLOW).shift(band_shift(4))
        lW = MathTex(r"mg").scale(0.9).shift(band_shift(4) + LEFT * 0.1 + DOWN * 2.2)
        self.play(Create(aW), Write(lW))
        self.wait(2)
        b4_l1 = MathTex(r"F_{g\parallel} = mg\sin\theta \quad F_{g\perp} = mg\cos\theta").scale(0.95).shift(band_shift(4) + RIGHT * 2.2 + UP * 1.4)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=BLUE)))
        self.wait(2.5)
        b4_l2 = MathTex(r"N = mg\cos\theta < mg").scale(0.95).shift(band_shift(4) + RIGHT * 2.6 + UP * 0.3)
        self.play(Write(b4_l2))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): consequences ---
        self.next_band(5)
        b5_l1 = Tex("Steeper slope: smaller N, weaker grip").scale(1.0).shift(band_shift(5) + UP * 1.8)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\text{friction on a slope} = \mu \, mg\cos\theta,\ \text{never } \mu \, mg").scale(0.9).shift(band_shift(5) + UP * 0.7)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("Declare the positive direction before line one").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_l3))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): toolbox setup ---
        self.next_band(6)
        b6_title = Tex(r"15 kg toolbox, 35$^\circ$ ramp, $\mu_s = 0{,}6$, $\mu_k = 0{,}25$").scale(0.9).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"w = 147\ \text{N}").scale(1.0).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"F_{g\parallel} = 147\sin 35^\circ = 84{,}3\ \text{N}").scale(0.95).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"F_{g\perp} = 147\cos 35^\circ = 120{,}4\ \text{N} = N").scale(0.95).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex("Normal force well below the 147 N weight").scale(0.9).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): slide, accelerate, drag up ---
        self.next_band(7)
        b7_l1 = MathTex(r"f_{s,max} = 0{,}6 \times 120{,}4 = 72{,}2\ \text{N} < 84{,}3\ \text{N}").scale(0.9).shift(band_shift(7) + UP * 2.0)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("So it slides").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=RED)))
        self.wait(2)
        b7_l3 = MathTex(r"f_k = 30{,}1\ \text{N}, \; a = \frac{84{,}3 - 30{,}1}{15} = 3{,}61\ \text{m}\cdot\text{s}^{-2}").scale(0.9).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"\text{drag up, constant } v: T = 84{,}3 + 30{,}1 = 114{,}4\ \text{N}").scale(0.9).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l5 = MathTex(r"\text{slips when } \tan\theta > \mu_s: \; 0{,}700 > 0{,}6").scale(0.9).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): grip runs out ---
        self.next_band(8)
        b8_title = Tex("Grip, and why it runs out").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Standing still: friction MATCHES your shove").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Every surface pair has a ceiling of grip").scale(0.95).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Past the ceiling: weaker sliding friction").scale(0.95).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Friction = grippiness $\\times$ pressed-together-ness").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): gravity's two shares ---
        self.next_band(9)
        b9_title = Tex("Gravity split into two shares").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("One share pulls DOWN THE SLOPE").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("One share presses INTO THE SURFACE").scale(0.95).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"147 \times \sin 35^\circ = 84{,}3\ \text{N down-slope}").scale(0.95).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"147 \times \cos 35^\circ = 120{,}4\ \text{N pressing}").scale(0.95).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("The ramp answers with the SMALLER number").scale(0.95).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the contest ---
        self.next_band(10)
        b10_title = Tex("Will it slide? The quick test").scale(1.1).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"\text{downhill pull } 84{,}3\ \text{N vs grip } 72{,}2\ \text{N}").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Gravity wins — it slides").scale(1.0).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=RED)))
        self.wait(2.5)
        b10_l3 = MathTex(r"a = \frac{84{,}3 - 30{,}1}{15} = 3{,}61\ \text{m}\cdot\text{s}^{-2}").scale(0.95).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.wait(3)

        # --- Band 11 (subtopic_7): uphill and the shortcut ---
        self.next_band(11)
        b11_l1 = Tex("Hauling UP: friction swaps sides").scale(1.0).shift(band_shift(11) + UP * 2.0)
        self.play(Write(b11_l1))
        self.wait(2)
        b11_l2 = MathTex(r"T = 84{,}3 + 30{,}1 = 114{,}4\ \text{N}").scale(1.0).shift(band_shift(11) + UP * 1.0)
        self.play(Write(b11_l2))
        self.play(Create(SurroundingRectangle(b11_l2, color=GREEN)))
        self.wait(2.5)
        b11_l3 = MathTex(r"\text{Mass-free test: slides when } \tan\theta > \mu_s").scale(0.95).shift(band_shift(11) + DOWN * 0.1)
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = Tex("Split, answer the smaller share, oppose the motion").scale(0.9).shift(band_shift(11) + DOWN * 1.2)
        self.play(Write(b11_l4))
        self.wait(4)
