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

# Band-layout whiteboard scene for "Magnetic Declination and Area
# Calculation" (grade 12, term 1). All seven subtopics: Part 1 Expert (1-4),
# Part 2 Simplifier (5-7). Band time apportioned to subtopics.json
# (225/235/235/230/195/190/180 of 1490 s). Exporter-safe primitives only;
# the two-norths wedge and the worked calculations are hand-built from
# Line/Arrow/Dot/Tex, element by element.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MagneticDeclinationAreaSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): two norths and the wedge
        title = Tex("Magnetic Declination and Area").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        base = Dot(DOWN * 1.6)
        tn = Arrow(DOWN * 1.6, UP * 1.4, color=GREEN)
        tn_lab = Tex("true north").scale(0.85).shift(UP * 1.8 + RIGHT * 0.2)
        self.play(Create(base), Create(tn), Write(tn_lab))
        self.wait(2)
        mn = Arrow(DOWN * 1.6, UP * 1.1 + LEFT * 1.6, color=ORANGE)
        mn_lab = Tex("magnetic north").scale(0.85).shift(UP * 1.5 + LEFT * 2.6)
        self.play(Create(mn), Write(mn_lab))
        self.wait(2)
        wedge_lab = Tex(r"declination: the angle between,\\ west of true north").scale(0.85).shift(DOWN * 0.2 + LEFT * 3.4)
        self.play(Write(wedge_lab))
        self.wait(2.5)
        b0_l1 = Tex(r"Margin note: value in a stated year,").scale(0.9).shift(DOWN * 2.5)
        b0_l2 = Tex(r"annual change, direction of change").scale(0.9).shift(DOWN * 3.2)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the bearing rule and the sixty
        self.next_band(1)
        b1_title = Tex("Why it matters").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Map bearings are TRUE; the needle is MAGNETIC").scale(0.9).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"Magnetic bearing $=$ true bearing $+$").scale(0.95).shift(band_shift(1) + UP * 0.3)
        b1_l3 = Tex(r"declination (declination west)").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = Tex(r"Angles in degrees and minutes:").scale(0.95).shift(band_shift(1) + DOWN * 1.4)
        b1_l5 = Tex(r"60 minutes $=$ 1 degree — not time!").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(2.5)
        b1_l6 = Tex(r"Surveyors, navigators, rangers, hikers").scale(0.9).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): the declination calculation, in full
        self.next_band(2)
        b2_title = Tex("The calculation, line by line").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Given: 17$^\circ$53$'$ W in 2018, change 4$'$/yr W").scale(0.95).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"Years: $2026 - 2018 = 8$").scale(0.95).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"Change: $8 \times 4' = 32'$ westward").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex(r"Apply: $17^\circ 53' + 32' = 17^\circ 85'$").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex(r"Carry: $85' = 1^\circ 25'$").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        b2_l6 = Tex(r"Answer: 18$^\circ$25$'$ west of true north").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): add or subtract
        self.next_band(3)
        b3_title = Tex("Add or subtract?").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Westward drift on a westerly declination:").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"the angle WIDENS — add (the SA standard)").scale(0.95).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex(r"Eastward drift: the needle swings back").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = Tex(r"toward true north — subtract").scale(0.95).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex(r"Read the note's direction every time;").scale(0.95).shift(band_shift(3) + DOWN * 2.0)
        b3_l6 = Tex(r"check: westward drift $\Rightarrow$ bigger angle").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): area on the orthophoto, in full
        self.next_band(4)
        b4_title = Tex("Area on the orthophoto (1:10 000)").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        block = Rectangle(width=3.4, height=2.0).shift(band_shift(4) + UP * 0.2 + LEFT * 2.8)
        len_lab = Tex(r"4,2 cm").scale(0.8).shift(band_shift(4) + UP * 1.5 + LEFT * 2.8)
        br_lab = Tex(r"2,5 cm").scale(0.8).shift(band_shift(4) + UP * 0.2 + LEFT * 5.1)
        self.play(Create(block), Write(len_lab), Write(br_lab))
        self.wait(2)
        b4_l1 = Tex(r"Convert FIRST:").scale(0.95).shift(band_shift(4) + UP * 1.0 + RIGHT * 2.6)
        b4_l2 = Tex(r"$4{,}2 \times 10\,000 = 42\,000$ cm $= 420$ m").scale(0.85).shift(band_shift(4) + UP * 0.2 + RIGHT * 2.8)
        b4_l3 = Tex(r"$2{,}5 \times 10\,000 = 25\,000$ cm $= 250$ m").scale(0.85).shift(band_shift(4) + DOWN * 0.5 + RIGHT * 2.8)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex(r"Then multiply: $420 \times 250 = 105\,000$").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        b4_l5 = Tex(r"Area $=$ 105 000 square metres").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(2.5)
        b4_l6 = Tex(r"A band of answers is accepted — measure clean").scale(0.85).shift(band_shift(4) + DOWN * 3.3)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): topographic sheet and units
        self.next_band(5)
        b5_title = Tex("Topographic sheet (1:50 000)").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Every centimetre $=$ half a kilometre").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex(r"5 cm $\to$ 2,5 km; \quad 4 cm $\to$ 2 km").scale(0.95).shift(band_shift(5) + UP * 0.3)
        b5_l3 = Tex(r"$2{,}5 \times 2 = 5$ square kilometres").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex(r"Same recipe: convert, convert, multiply").scale(0.95).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex(r"Units: m$^2$ for orthophoto features,").scale(0.95).shift(band_shift(5) + DOWN * 2.3)
        b5_l6 = Tex(r"km$^2$ for big country — land on the unit asked").scale(0.9).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): the traps, named and struck
        self.next_band(6)
        b6_title = Tex("The traps, named").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        t1 = Tex(r"$17^\circ 85'$ left standing").scale(0.9).shift(band_shift(6) + UP * 1.2)
        self.play(Write(t1))
        self.play(Create(strike(t1)))
        self.wait(2)
        t2 = Tex(r"answer without ``west of true north''").scale(0.9).shift(band_shift(6) + UP * 0.3)
        self.play(Write(t2))
        self.play(Create(strike(t2)))
        self.wait(2)
        t3 = Tex(r"cm $\times$ cm, converted afterwards").scale(0.9).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(t3))
        self.play(Create(strike(t3)))
        self.wait(2)
        t4 = Tex(r"sides measured off two different sheets").scale(0.9).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(t4))
        self.play(Create(strike(t4)))
        self.wait(2)
        b6_l1 = Tex(r"Count years from the margin note's year;").scale(0.9).shift(band_shift(6) + DOWN * 2.5)
        b6_l2 = Tex(r"match the unit the question names").scale(0.9).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(3)

        # --- Band 7 (subtopic_4): the answer line and the bigger machine
        self.next_band(7)
        b7_title = Tex("The answer line").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Three lines: given values, operation,").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"answer with unit — and direction").scale(0.95).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex(r"Declination feeds every bearing question;").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex(r"area feeds land-use and settlement analysis").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex(r"All of mapwork is one skill: paper").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        b7_l6 = Tex(r"measurement $\to$ ground truth").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the compass that tells a small lie
        self.next_band(8)
        b8_title = Tex("The compass that tells a small lie").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Map arrow: true north; needle arrow:").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"magnetic north — a wedge between them").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"The wedge is the size of the lie —").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex(r"and it grows a few minutes every year").scale(0.95).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex(r"Translation: magnetic $=$ true $+$ declination").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2)
        b8_l6 = Tex(r"No translation $\to$ every 100 m walked").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        b8_l7 = Tex(r"drifts you further off the windmill").scale(0.95).shift(band_shift(8) + DOWN * 3.6)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): minutes that are not time
        self.next_band(9)
        b9_title = Tex("Minutes that are not time").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Clock rule: 60 minutes $=$ one whole").scale(0.95).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex(r"Gap: $2026 - 2018 = 8$ years").scale(0.95).shift(band_shift(9) + UP * 0.5)
        b9_l3 = Tex(r"Growth: $8 \times 4' = 32'$").scale(0.95).shift(band_shift(9) + DOWN * 0.2)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex(r"$53' + 32' = 85'$ — never leave 85 standing").scale(0.95).shift(band_shift(9) + DOWN * 1.1)
        b9_l5 = Tex(r"$85'$ rolls over: $1^\circ 25'$").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2.5)
        b9_l6 = Tex(r"2026 lie: 18$^\circ$25$'$ west of true north").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): the rugby field in your answer book
        self.next_band(10)
        b10_title = Tex("The rugby field in your answer book").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Tiling: un-shrink length, un-shrink breadth,").scale(0.95).shift(band_shift(10) + UP * 1.3)
        b10_l2 = Tex(r"THEN multiply").scale(1.0).shift(band_shift(10) + UP * 0.6)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"$4{,}2$ cm $\to$ 420 m; \quad $2{,}5$ cm $\to$ 250 m").scale(0.95).shift(band_shift(10) + DOWN * 0.3)
        b10_l4 = Tex(r"$420 \times 250 = 105\,000$ m$^2$").scale(1.0).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(3)
        b10_l5 = Tex(r"Sense check: rugby field $\approx$ 7 000 m$^2$ —").scale(0.95).shift(band_shift(10) + DOWN * 2.0)
        b10_l6 = Tex(r"our block is fifteen fields, believable").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(2.5)
        bad = Tex(r"$4{,}2 \times 2{,}5$ in cm first").scale(0.9).shift(band_shift(10) + DOWN * 3.5)
        self.play(Write(bad))
        self.play(Create(strike(bad)))
        self.wait(4)
