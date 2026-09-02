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

# Band-layout whiteboard scene: sequential vertical bands, one per teaching
# beat, camera moves down between bands, add-only lifecycle. Exporter-safe
# mobjects only. This practice-run session has seven question subtopics
# (Q1-Q7, no simplifier part in script.md); each question gets its own
# band(s), worked line by line with the mark-earning steps on the board.
# Band time apportioned to subtopics.json
# (235/210/245/245/255/220/270 of 1680 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Paper2PracticeRunSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(16)

        # --- Band 0 (Q1): mean and standard deviation
        title = Tex("Practice Paper Run — Geometry Side").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_q = Tex("Q1 — ten marks:").scale(1.1).shift(UP * 1.2)
        self.play(Write(b0_q))
        b0_data = MathTex(r"18;\,41;\,48;\,55;\,59;\,63;\,66;\,71;\,78;\,91").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0_data))
        self.wait(2)
        b0_mean = MathTex(r"\bar{x} = \frac{590}{10} = 59").scale(1.15).shift(DOWN * 0.7)
        self.play(Write(b0_mean))
        self.wait(2.5)
        b0_sd = MathTex(r"\sigma = 19{,}33 \;\; \text{(calculator stats mode)}").scale(1.1).shift(DOWN * 1.9)
        self.play(Write(b0_sd))
        self.wait(3)

        # --- Band 1 (Q1): five-number summary, the fence, the interval count
        self.next_band(1)
        b1_t = Tex("Five-number summary and the fence").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = MathTex(r"18; \; Q_1 = 48; \; \text{med} = 61; \; Q_3 = 71; \; 91").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        # box and whisker: number line from 18 to 91 mapped onto 5.6 units
        o = band_shift(1) + UP * 0.1
        axis = Line(o + LEFT * 3.0, o + RIGHT * 3.0, stroke_width=3)
        self.play(Create(axis))
        # scale: value v maps to LEFT*3 + RIGHT*(v-18)/73*6
        box = Rectangle(width=6 * (71 - 48) / 73, height=0.8, color=YELLOW).move_to(
            o + LEFT * 3.0 + RIGHT * (6 * ((48 + 71) / 2 - 18) / 73))
        med = Line(o + LEFT * 3.0 + RIGHT * (6 * (61 - 18) / 73) + DOWN * 0.4,
                   o + LEFT * 3.0 + RIGHT * (6 * (61 - 18) / 73) + UP * 0.4, color=RED, stroke_width=4)
        wl = Line(o + LEFT * 3.0, o + LEFT * 3.0 + RIGHT * (6 * (48 - 18) / 73), color=YELLOW, stroke_width=3)
        wr = Line(o + LEFT * 3.0 + RIGHT * (6 * (71 - 18) / 73), o + RIGHT * 3.0, color=YELLOW, stroke_width=3)
        self.play(Create(box), Create(wl), Create(wr))
        self.play(Create(med))
        self.wait(2.5)
        b1_l2 = MathTex(r"\text{Fence: } 48 - 1{,}5(23) = 13{,}5 < 18 \Rightarrow \text{no outlier}").scale(0.95).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = MathTex(r"[39{,}7;\,78{,}3]: \; 8 \text{ of the } 10 \text{ inside}").scale(0.95).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l3))
        self.wait(3)

        # --- Band 2 (Q2): the regression line and r
        self.next_band(2)
        b2_t = Tex("Q2 — hours of practice vs test \\%").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = MathTex(r"(2;35),(4;45),(6;50),(8;62),(10;68),(12;79)").scale(0.85).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\hat{y} = 26{,}4 + 4{,}3x \quad (4)").scale(1.1).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = MathTex(r"r = 0{,}996: \text{ very strong, positive, linear}").scale(0.95).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = MathTex(r"x = 9: \; \hat{y} \approx 65\% \; \text{(interpolation } \checkmark\text{)}").scale(0.95).shift(band_shift(2) + DOWN * 1.7)
        b2_l5 = MathTex(r"x = 20: \text{ extrapolation — and } \% \le 100").scale(0.95).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l4))
        self.wait(2.5)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (Q3): the analytical triangle — right angle at Q
        self.next_band(3)
        b3_t = MathTex(r"\text{Q3: } P(-4;1), \; Q(2;5), \; R(6;-1)").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = MathTex(r"m_{PQ} = \frac{5-1}{2+4} = \frac{2}{3}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"m_{QR} = \frac{-1-5}{6-2} = -\frac{3}{2}").scale(1.05).shift(band_shift(3) + UP * 0.0)
        b3_l3 = MathTex(r"\tfrac{2}{3} \times \left(-\tfrac{3}{2}\right) = -1 \;\Rightarrow\; \hat{Q} = 90^\circ").scale(1.0).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = MathTex(r"PQ = \sqrt{6^2 + 4^2} = \sqrt{52} = 2\sqrt{13}").scale(1.0).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (Q3): the midpoint as circumcentre + inclination
        self.next_band(4)
        b4_t = MathTex(r"\text{3.4: } M = \left(\tfrac{-4+6}{2};\,\tfrac{1-1}{2}\right) = (1;\,0)").scale(1.0).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = Tex(r"$\hat{Q} = 90^\circ$ $\Rightarrow$ $PR$ is a diameter (converse, semicircle)").scale(0.9).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"MP = MQ = MR = \sqrt{26}").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{3.5: } \tan\theta = -\tfrac{3}{2} \Rightarrow -56{,}31^\circ + 180^\circ").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        b4_l4 = MathTex(r"\theta = 123{,}69^\circ").scale(1.1).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (Q4): completing the square on the circle
        self.next_band(5)
        b5_t = MathTex(r"\text{Q4: } x^2 + y^2 + 8x - 6y = 0").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = MathTex(r"(x^2 + 8x + 16) + (y^2 - 6y + 9) = 16 + 9").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"(x+4)^2 + (y-3)^2 = 25").scale(1.1).shift(band_shift(5) + UP * 0.0)
        b5_l3 = MathTex(r"\text{Centre } (-4;\,3), \;\; r = 5 \quad (4)").scale(1.05).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = MathTex(r"(-1;\,7): \; 3^2 + 4^2 = 25 \; \checkmark \text{ on the circle}").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (Q4): the tangent at (-1; 7) and the external point
        self.next_band(6)
        b6_t = Tex("4.3: tangent $\\perp$ radius at the contact point").scale(1.0).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        o6 = band_shift(6) + UP * 0.4
        circ = Circle(radius=1.3, color=BLUE).move_to(o6)
        rad = Line(o6, o6 + RIGHT * 0.78 + UP * 1.04, color=YELLOW, stroke_width=3)
        tang = Line(o6 + RIGHT * 0.78 + UP * 1.04 + LEFT * 1.56 + UP * 1.17,
                    o6 + RIGHT * 0.78 + UP * 1.04 + RIGHT * 1.56 + DOWN * 1.17,
                    color=GREEN, stroke_width=3)
        self.play(Create(circ))
        self.play(Create(rad))
        self.play(Create(tang))
        self.wait(2)
        b6_l1 = MathTex(r"m_{\text{rad}} = \tfrac{7-3}{-1+4} = \tfrac{4}{3} \;\Rightarrow\; m_{\text{tan}} = -\tfrac{3}{4}").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        b6_l2 = MathTex(r"y - 7 = -\tfrac{3}{4}(x + 1)").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        b6_l3 = MathTex(r"\text{From } (4;9): \; \sqrt{100 - 25} = 5\sqrt{3} \approx 8{,}66").scale(0.95).shift(band_shift(6) + DOWN * 3.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(3)

        # --- Band 7 (Q5): sin 15 degrees, exactly
        self.next_band(7)
        b7_t = MathTex(r"\text{Q5.1: } \sin 15^\circ = \sin(45^\circ - 30^\circ)").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = MathTex(r"\sin 45^\circ \cos 30^\circ - \cos 45^\circ \sin 30^\circ").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\tfrac{\sqrt{2}}{2}\cdot\tfrac{\sqrt{3}}{2} - \tfrac{\sqrt{2}}{2}\cdot\tfrac{1}{2}").scale(1.0).shift(band_shift(7) + UP * 0.1)
        b7_l3 = MathTex(r"\sin 15^\circ = \frac{\sqrt{6} - \sqrt{2}}{4} \quad (4)").scale(1.05).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        b7_l4 = Tex("Exact surd — no calculator decimal earns here").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (Q5): the identity and the chosen face
        self.next_band(8)
        b8_t = MathTex(r"\text{5.2: } \frac{1 - \cos 2x}{\sin 2x} = \tan x").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = MathTex(r"1 - \cos 2x = 1 - (1 - 2\sin^2 x) = 2\sin^2 x").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"\frac{2\sin^2 x}{2\sin x \cos x} = \frac{\sin x}{\cos x} = \tan x").scale(1.0).shift(band_shift(8) + UP * 0.0)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{5.3: } \sin x = -\tfrac{\sqrt{3}}{2}: \; \text{ref } 60^\circ, \text{ Q3 and Q4}").scale(0.9).shift(band_shift(8) + DOWN * 1.1)
        b8_l4 = MathTex(r"x = 240^\circ + k\,360^\circ \text{ or } x = 300^\circ + k\,360^\circ, \; k \in \mathbb{Z}").scale(0.85).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l3))
        self.wait(2.5)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (Q5): double angles from the 5-12-13 triangle
        self.next_band(9)
        b9_t = MathTex(r"\text{5.4: } \cos x = \tfrac{5}{13}, \; x \text{ acute}").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"\sin x = \tfrac{12}{13} \;\; \text{(5-12-13 triangle)}").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"\sin 2x = 2\cdot\tfrac{12}{13}\cdot\tfrac{5}{13} = \tfrac{120}{169}").scale(1.0).shift(band_shift(9) + UP * 0.0)
        b9_l3 = MathTex(r"\cos 2x = \tfrac{25}{169} - \tfrac{144}{169} = -\tfrac{119}{169}").scale(1.0).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        b9_l4 = Tex("Negative $\\cos 2x$: $2x$ has passed $90^\\circ$").scale(0.9).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (Q6): sine rule, cosine rule, area rule
        self.next_band(10)
        b10_t = MathTex(r"\text{Q6.1: } a = 15, \; \hat{A} = 70^\circ, \; \hat{B} = 44^\circ").scale(1.0).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = MathTex(r"b = \frac{15 \sin 44^\circ}{\sin 70^\circ} \approx 11{,}09").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.play(Create(SurroundingRectangle(b10_l1, color=GREEN)))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{6.2: } c^2 = 64 + 121 - 2(8)(11)\cos 50^\circ = 71{,}87").scale(0.9).shift(band_shift(10) + UP * 0.1)
        b10_l3 = MathTex(r"c \approx 8{,}48; \quad \text{Area} = \tfrac{1}{2}(8)(11)\sin 50^\circ \approx 33{,}71").scale(0.9).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l2))
        self.wait(2.5)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(3)

        # --- Band 11 (Q6): the flagpole
        self.next_band(11)
        b11_t = Tex("6.3: the flagpole — one right triangle").scale(1.05).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(1.5)
        o11 = band_shift(11) + DOWN * 0.6
        ground = Line(o11 + LEFT * 2.6, o11 + RIGHT * 1.4, stroke_width=3)
        pole = Line(o11 + RIGHT * 1.4, o11 + RIGHT * 1.4 + UP * 2.2, color=YELLOW, stroke_width=4)
        sight = Line(o11 + LEFT * 2.6, o11 + RIGHT * 1.4 + UP * 2.2, color=BLUE, stroke_width=2)
        self.play(Create(ground), Create(pole))
        self.play(Create(sight))
        self.wait(2)
        b11_l1 = MathTex(r"h = 32 \tan 42^\circ \approx 28{,}81 \text{ m}").scale(1.05).shift(band_shift(11) + DOWN * 2.6)
        self.play(Write(b11_l1))
        self.play(Create(SurroundingRectangle(b11_l1, color=GREEN)))
        b11_l2 = Tex("Units on the answer — always").scale(0.9).shift(band_shift(11) + DOWN * 3.3)
        self.play(Write(b11_l2))
        self.wait(3)

        # --- Band 12 (Q7): the rider — tan-chord twice
        self.next_band(12)
        b12_t = Tex("Q7: tangent $DAE$, chords $AB$ and $AC$").scale(1.0).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12_t))
        self.wait(2)
        o12 = band_shift(12) + UP * 0.2
        circ2 = Circle(radius=1.4, color=BLUE).move_to(o12 + UP * 1.4 * 0 + UP * 1.4)
        tang2 = Line(o12 + LEFT * 3.0, o12 + RIGHT * 3.0, color=GREEN, stroke_width=3)
        chord1 = Line(o12, o12 + LEFT * 0.9 + UP * 2.5, color=YELLOW, stroke_width=3)
        chord2 = Line(o12, o12 + RIGHT * 1.1 + UP * 2.3, color=YELLOW, stroke_width=3)
        self.play(Create(circ2), Create(tang2))
        self.play(Create(chord1), Create(chord2))
        self.wait(2)
        b12_l1 = MathTex(r"\hat{ACB} = 35^\circ \;\; \text{(tan chord thm)}").scale(0.95).shift(band_shift(12) + DOWN * 1.4)
        b12_l2 = MathTex(r"\hat{ABC} = 72^\circ \;\; \text{(tan chord thm)}").scale(0.95).shift(band_shift(12) + DOWN * 2.2)
        b12_l3 = MathTex(r"\hat{BAC} = 180^\circ - 35^\circ - 72^\circ = 73^\circ").scale(0.95).shift(band_shift(12) + DOWN * 3.0)
        self.play(Write(b12_l1))
        self.wait(2.5)
        self.play(Write(b12_l2))
        self.wait(2.5)
        self.play(Write(b12_l3))
        self.play(Create(SurroundingRectangle(b12_l3, color=GREEN)))
        self.wait(3)

        # --- Band 13 (Q7): the tan-chord proof as a performance
        self.next_band(13)
        b13_t = Tex("7.4: the proof — construction first").scale(1.05).shift(band_shift(13) + UP * 2.2)
        self.play(Write(b13_t))
        self.wait(2)
        b13_l1 = Tex(r"Draw diameter $AOF$; join $FB$ \quad (construction)").scale(0.9).shift(band_shift(13) + UP * 1.2)
        b13_l2 = Tex(r"Tangent $\perp$ diameter: $90^\circ$ at $A$").scale(0.9).shift(band_shift(13) + UP * 0.3)
        b13_l3 = Tex(r"$\hat{ABF} = 90^\circ$ \; (angle in semicircle)").scale(0.9).shift(band_shift(13) + DOWN * 0.6)
        b13_l4 = Tex(r"Two subtractions from $90^\circ$ meet: tan-chord angle $= \hat{AFB}$").scale(0.85).shift(band_shift(13) + DOWN * 1.5)
        b13_l5 = Tex(r"$\hat{AFB} = \hat{ACB}$ \; (same segment) — proved").scale(0.9).shift(band_shift(13) + DOWN * 2.4)
        self.play(Write(b13_l1))
        self.wait(2.5)
        self.play(Write(b13_l2))
        self.wait(2.5)
        self.play(Write(b13_l3))
        self.wait(2.5)
        self.play(Write(b13_l4))
        self.wait(2.5)
        self.play(Write(b13_l5))
        self.play(Create(SurroundingRectangle(b13_l5, color=GREEN)))
        self.wait(2)
        b13_l6 = Tex(r"87 marks walked — reasons paid like currency").scale(0.95).shift(band_shift(13) + DOWN * 3.3)
        self.play(Write(b13_l6))
        self.wait(4)
