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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (230/210/220/240/190/180/200 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RatioRateProportionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): ratio and sharing
        title = Tex("Ratio, Rate and Proportion").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"500\text{ g} : 2\text{ kg} = 500 : 2\,000 = 1 : 4").scale(1.1).shift(UP * 1.2)
        self.play(Write(l1))
        self.wait(2.5)
        l2 = Tex(r"Share R2 400 in the ratio $5 : 3 : 2$").scale(1.1).shift(UP * 0.3)
        l3 = MathTex(r"5 + 3 + 2 = 10 \text{ parts} \qquad 2\,400 \div 10 = 240").scale(1.05).shift(DOWN * 0.6)
        l4 = MathTex(r"5 \times 240 = 1\,200,\; 3 \times 240 = 720,\; 2 \times 240 = 480").scale(1.0).shift(DOWN * 1.5)
        l5 = MathTex(r"1\,200 + 720 + 480 = 2\,400 \;\checkmark").scale(1.05).shift(DOWN * 2.4)
        for m in (l2, l3, l4, l5):
            self.play(Write(m))
            self.wait(2.2)
        self.play(Create(SurroundingRectangle(l5, color=GREEN)))
        self.wait(2)

        # --- Band 1 (subtopic_1): the reverse share
        self.next_band(1)
        b1_title = Tex("Working back from one share").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Ratio $3 : 7$, smaller share R450").scale(1.1).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"450 \div 3 = 150 \text{ per part}").scale(1.1).shift(band_shift(1) + UP * 0.3)
        b1_l3 = MathTex(r"7 \times 150 = 1\,050 \qquad 10 \times 150 = 1\,500").scale(1.1).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = Tex(r"Part-to-whole: 5 parts of 10 $= \tfrac{1}{2}$ of the total").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(2)

        # --- Band 2 (subtopic_2): rate
        self.next_band(2)
        b2_title = Tex("Rate: different kinds, units kept").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{speed} = \frac{180\text{ km}}{2{,}5\text{ h}} = 72\text{ km/h}").scale(1.1).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"72 \times 3{,}5 = 252\text{ km} \qquad 180 \div 60 = 3\text{ h}").scale(1.05).shift(band_shift(2) + UP * 0.1)
        b2_l3 = MathTex(r"34 \div 2 = 17\text{ R/L} \qquad 27 \div 1{,}5 = 18\text{ R/L}").scale(1.05).shift(band_shift(2) + DOWN * 0.9)
        b2_l4 = MathTex(r"72 \div 3{,}6 = 20\text{ m/s}").scale(1.05).shift(band_shift(2) + DOWN * 1.9)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_3): direct proportion
        self.next_band(3)
        b3_title = Tex("Direct proportion: constant ratio").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"3 \text{ loaves} = \text{R}51 \;\Rightarrow\; 51 \div 3 = 17 \text{ per loaf}").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"7 \times 17 = 119 \qquad \text{or} \qquad \frac{51}{3} = \frac{x}{7} \Rightarrow x = 119").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"25\text{ L} = \text{R}575 \Rightarrow 23\text{ R/L} \Rightarrow 40\text{ L} = \text{R}920").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l1))
        self.wait(2.3)
        self.play(Write(b3_l2))
        self.wait(2.3)
        self.play(Write(b3_l3))
        self.wait(2)
        ax = Line(band_shift(3) + LEFT * 5.5 + DOWN * 2.8, band_shift(3) + LEFT * 2.0 + DOWN * 2.8)
        ay = Line(band_shift(3) + LEFT * 5.5 + DOWN * 2.8, band_shift(3) + LEFT * 5.5 + DOWN * 1.3)
        ln = Line(band_shift(3) + LEFT * 5.5 + DOWN * 2.8, band_shift(3) + LEFT * 2.3 + DOWN * 1.4, color=YELLOW)
        lab = Tex("straight line through the origin").scale(0.9).shift(band_shift(3) + RIGHT * 1.5 + DOWN * 2.2)
        self.play(Create(ax), Create(ay))
        self.play(Create(ln), Write(lab))
        self.wait(2.5)

        # --- Band 4 (subtopic_4): indirect proportion
        self.next_band(4)
        b4_title = Tex("Indirect proportion: constant product").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"6 \text{ workers} \times 10 \text{ days} = 60 \text{ worker-days}").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"4 \text{ workers}: 60 \div 4 = 15 \text{ days} \qquad 12: 60 \div 12 = 5").scale(1.0).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"60 \times 3 = 180\text{ km} \Rightarrow 180 \div 90 = 2\text{ h}").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        for m in (b4_l1, b4_l2, b4_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        ax2 = Line(band_shift(4) + LEFT * 5.5 + DOWN * 2.8, band_shift(4) + LEFT * 2.0 + DOWN * 2.8)
        ay2 = Line(band_shift(4) + LEFT * 5.5 + DOWN * 2.8, band_shift(4) + LEFT * 5.5 + DOWN * 1.3)
        curve = VGroup(
            Line(band_shift(4) + LEFT * 5.2 + DOWN * 1.4, band_shift(4) + LEFT * 4.8 + DOWN * 2.0, color=YELLOW),
            Line(band_shift(4) + LEFT * 4.8 + DOWN * 2.0, band_shift(4) + LEFT * 4.0 + DOWN * 2.4, color=YELLOW),
            Line(band_shift(4) + LEFT * 4.0 + DOWN * 2.4, band_shift(4) + LEFT * 2.3 + DOWN * 2.65, color=YELLOW),
        )
        lab2 = Tex("falls, never touches the axes").scale(0.9).shift(band_shift(4) + RIGHT * 1.5 + DOWN * 2.2)
        self.play(Create(ax2), Create(ay2))
        self.play(Create(curve), Write(lab2))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): the diagnostic question and the traps
        self.next_band(5)
        b5_title = Tex("Direct or indirect? Ask first").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"First quantity up, second UP $\to$ direct: output $\div$ input constant").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"First quantity up, second DOWN $\to$ indirect: output $\times$ input constant").scale(0.95).shift(band_shift(5) + UP * 0.3)
        b5_l3 = Tex(r"Trap 1: four workers finishing sooner than six").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = Tex(r"Trap 2: $7$ loaves $= 51 + 4$ \quad Trap 3: a rate with no units").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=YELLOW)), Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): sharing the prize fairly
        self.next_band(6)
        b6_title = Tex("Sharing the prize fairly").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"R2 400, split $5 : 3 : 2$ — count the parts: 10").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex(r"Price one pile: $2\,400 \div 10 = $ R240").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex(r"Hand out: R1 200, R720, R480 — add back: R2 400").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex(r"Units trap: 500 g : 2 kg $\ne$ 500 : 2; it is 500 : 2 000 $= 1 : 4$").scale(0.95).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(2)

        # --- Band 7 (subtopic_6): per
        self.next_band(7)
        b7_title = Tex("Per: the little word that makes a rate").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"2 L for R34 $\to 34 \div 2 = $ R17 per litre").scale(1.0).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex(r"1,5 L for R27 $\to 27 \div 1{,}5 = $ R18 per litre").scale(1.0).shift(band_shift(7) + UP * 0.4)
        b7_l3 = Tex(r"180 km in 2,5 h $\to 180 \div 2{,}5 = 72$ km per hour").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex(r"Forwards: $72 \times 3{,}5 = 252$ km \quad Back: $180 \div 60 = 3$ h").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        b7_l5 = Tex("Divide so the second thing becomes ONE; keep the units").scale(0.95).shift(band_shift(7) + DOWN * 2.3)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4, b7_l5):
            self.play(Write(m))
            self.wait(2)
        self.wait(1.5)

        # --- Band 8 (subtopic_7): more gives more, or more gives less?
        self.next_band(8)
        b8_title = Tex("More gives more, or more gives less?").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Bread: up with up $\to 51 \div 3 = 17$, $7 \times 17 = 119$").scale(1.0).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex(r"Painters: up with down $\to 6 \times 10 = 60$, $60 \div 4 = 15$ days").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex(r"Driving: $60 \times 3 = 180$ km, $180 \div 90 = 2$ h").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex("Up with up: divide, then multiply").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        b8_l5 = Tex("Up with down: multiply, then divide").scale(1.0).shift(band_shift(8) + DOWN * 2.3)
        for m in (b8_l1, b8_l2, b8_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(VGroup(b8_l4, b8_l5), color=YELLOW)))
        self.wait(4)
