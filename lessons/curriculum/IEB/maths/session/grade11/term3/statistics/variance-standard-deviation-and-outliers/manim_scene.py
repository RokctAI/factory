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

# Band-layout whiteboard scene for the session duo "Variance, Standard
# Deviation and Outliers" (Part 1 — Expert: subtopics 1-4; Part 2 —
# Simplifier: subtopics 5-7). One band per teaching beat, add-only lifecycle,
# camera moves down between bands. Only exporter-supported mobjects;
# write-only reveals. Band dwell times follow subtopics.json
# (225/230/220/230/190/195/195 of 1485 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class VarianceStdDevOutliersSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the five number summary ---
        title = Tex("Variance, Standard Deviation and Outliers").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"38,\,42,\,45,\,47,\,49,\,51,\,52,\,54,\,56,\,86").scale(0.95).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"\text{Median} = \tfrac{49+51}{2} = 50").scale(1.0).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = MathTex(r"Q_1 = 45 \quad Q_3 = 54").scale(1.0).shift(DOWN * 0.8)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = MathTex(r"\text{Summary: } 38;\;45;\;50;\;54;\;86").scale(1.05).shift(DOWN * 1.7)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the box-and-whisker, drawn ---
        self.next_band(1)
        b1_title = Tex("The box-and-whisker map").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        bc = band_shift(1) + DOWN * 0.4
        # scale: mark 38..86 -> x positions; 1 mark = 0.14 units, centred near 60
        def mx(v):
            return bc + RIGHT * ((v - 62) * 0.14)
        axis = Line(mx(34), mx(90))
        self.play(Create(axis))
        box = Rectangle(width=(54 - 45) * 0.14, height=1.2).move_to(mx((45 + 54) / 2) + UP * 1.2)
        med = Line(mx(50) + UP * 0.6, mx(50) + UP * 1.8)
        wl = Line(mx(38) + UP * 1.2, mx(45) + UP * 1.2)
        wr = Line(mx(54) + UP * 1.2, mx(86) + UP * 1.2)
        self.play(Create(box))
        self.play(Create(med))
        self.play(Create(wl), Create(wr))
        self.wait(2)
        d_min = Dot(mx(38) + UP * 1.2, radius=0.06)
        d_max = Dot(mx(86) + UP * 1.2, radius=0.06)
        self.play(Create(d_min), Create(d_max))
        self.wait(2)
        b1_l1 = MathTex(r"\text{Range} = 86 - 38 = 48 \quad \text{IQR} = 54 - 45 = 9").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Right whisker: 32 marks. Left: 7. Hold that thought.").scale(0.9).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l2))
        self.wait(3)

        # --- Band 2 (subtopic_2): the five-step recipe ---
        self.next_band(2)
        b2_title = Tex("Standard deviation: five steps").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Goals: } 3,\,5,\,8,\,10,\,14 \quad \bar{x} = \tfrac{40}{5} = 8").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{Deviations: } -5,\,-3,\,0,\,2,\,6 \;\;(\text{sum} = 0)").scale(1.0).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{Squares: } 25,\,9,\,0,\,4,\,36 \;\Rightarrow\; \text{sum} = 74").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = MathTex(r"\sigma^2 = \tfrac{74}{5} = 14{,}8 \qquad \sigma = \sqrt{14{,}8} \approx 3{,}85").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)
        b2_l5 = Tex("Root returns to real units: goals, not goals$^2$").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_3): symmetric and skewed ---
        self.next_band(3)
        b3_title = Tex("Shape: the mean chases the tail").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\bar{x} = \tfrac{520}{10} = 52 \quad \text{median} = 50").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"\bar{x} > \text{median} \;\Rightarrow\; \text{positively skewed}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Named after the TAIL, not the hump").scale(1.0).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("Evidence in a sentence: quote mean vs median, or whiskers").scale(0.9).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_4): the outlier fences ---
        self.next_band(4)
        b4_title = Tex("Outliers: build the fences").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"1{,}5 \times \text{IQR} = 1{,}5 \times 9 = 13{,}5").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\text{Fences: } 45 - 13{,}5 = 31{,}5 \quad 54 + 13{,}5 = 67{,}5").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"86 > 67{,}5 \;\Rightarrow\; 86 \text{ is an outlier}").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex(r"With 86: $\bar{x} = 52$, $\sigma \approx 12{,}5$. Without: $\approx 48{,}2$, $\approx 5{,}5$").scale(0.85).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("Fragile: mean, $\\sigma$. Robust: median, IQR.").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): five landmarks on one road ---
        self.next_band(5)
        b5_title = Tex("Five landmarks on one road").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Ten houses from number 38 to number 86").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex("Box = the neighbourhood, 45 to 54, nine marks wide").scale(0.95).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Road out to the last house: 32 lonely marks").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("Range is hostage to the mansion; IQR stays put").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_6): the average distance from home ---
        self.next_band(6)
        b6_title = Tex("The average distance from home").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Striker: 3, 5, 8, 10, 14 goals — home base 8").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\text{Raw distances average to } 0 \text{ — always}").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.play(Create(strike(b6_l2)))
        self.wait(2.5)
        b6_l3 = MathTex(r"\text{Square first: } \tfrac{25+9+0+4+36}{5} = 14{,}8").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"\sqrt{14{,}8} \approx 3{,}85 \text{ goals from home}").scale(1.05).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2.5)
        b6_l5 = Tex("Rival: same mean 8, $\\sigma = 1{,}5$ — the safer pick").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_7): the mansion and the fences ---
        self.next_band(7)
        b7_title = Tex("The mansion and the fences").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Fences at 1,5 neighbourhood-widths past the box:").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"31{,}5 \;\text{and}\; 67{,}5 \quad — \quad 86 \text{ is past the fence}").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex(r"Mansion hauls: mean $48 \to 52$, $\sigma$ $5{,}5 \to 12{,}5$").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("Median counts heads — barely notices; IQR immobile").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Outlier present? Report median and IQR, and say why").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.wait(4)
