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

# Band-layout whiteboard scene for the IEB Grade 11 Geography session duo
# "The Concept of Development". One band per teaching beat; the camera moves
# down, nothing is removed. Text-led topic with simple primitive accents.
# Subtopic shares follow subtopics.json: 215/230/225/220/185/195/205 of 1475 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ConceptOfDevelopmentIEBSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): development vs growth
        title = Tex("The Concept of Development").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("Development: improving quality of life —").scale(1.05).shift(UP * 1.1)
        s0_l2 = Tex("income, health, schooling, dignity").scale(1.05).shift(UP * 0.3)
        self.play(Write(s0_l1))
        self.play(Write(s0_l2))
        self.wait(2.5)
        s0_l3 = Tex("Growth: a larger pile of output —").scale(1.0).shift(DOWN * 0.6)
        s0_l3b = Tex("silent on who benefits").scale(1.0).shift(DOWN * 1.4)
        self.play(Write(s0_l3))
        self.play(Write(s0_l3b))
        self.wait(2.5)
        s0_l4 = Tex("Growth: necessary, NOT sufficient").scale(1.1).shift(DOWN * 2.4)
        self.play(Write(s0_l4))
        self.play(Create(SurroundingRectangle(s0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the paired terms and the labels
        self.next_band(1)
        b1_title = Tex("Vocabulary that earns marks").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("STANDARD OF LIVING: what income buys").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("QUALITY OF LIFE: the whole of life —").scale(1.0).shift(band_shift(1) + UP * 0.4)
        b1_l2b = Tex("a well-paid worker under smelter fumes").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Write(b1_l2b))
        self.wait(2.5)
        b1_l3 = Tex("MEDC: Canada, Netherlands, New Zealand").scale(0.95).shift(band_shift(1) + DOWN * 1.3)
        b1_l4 = Tex("LEDC: Niger, Mozambique, Nepal").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        b1_l5 = Tex("NIC: India, Malaysia, South Africa").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l3))
        self.wait(1.5)
        self.play(Write(b1_l4))
        self.wait(1.5)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): GDP, GNP, per capita
        self.next_band(2)
        b2_title = Tex("Measuring in money").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("GDP: follows the SOIL — inside borders").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("GNP: follows the PASSPORT — own firms").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("BMW Rosslyn: SA's GDP, Germany's GNP").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex(r"Per capita $=$ total $\div$ population").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        b2_l5 = Tex(r"SA $\approx \$6\,000$; Mozambique hundreds;").scale(0.95).shift(band_shift(2) + DOWN * 2.3)
        b2_l5b = Tex(r"Switzerland $\$90\,000$ — middle income").scale(0.95).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.play(Write(b2_l5b))
        self.wait(3)

        # --- Band 3 (subtopic_2): the Gini coefficient
        self.next_band(3)
        b3_title = Tex("The Gini coefficient: the cut").scale(1.15).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        # scale line 0 to 1 with markers
        g_line = Line(LEFT * 5.0 + UP * 1.2, RIGHT * 5.0 + UP * 1.2, color=WHITE).shift(band_shift(3))
        g0 = MathTex(r"0").scale(0.9).shift(band_shift(3) + LEFT * 5.0 + UP * 1.8)
        g1 = MathTex(r"1").scale(0.9).shift(band_shift(3) + RIGHT * 5.0 + UP * 1.8)
        self.play(Create(g_line), Write(g0), Write(g1))
        d_no = Dot(LEFT * 2.3 + UP * 1.2, color=BLUE).shift(band_shift(3))
        no_lab = Tex(r"Nordics $\approx 0{,}27$").scale(0.85).shift(band_shift(3) + LEFT * 2.3 + UP * 0.5)
        d_sa = Dot(RIGHT * 1.3 + UP * 1.2, color=RED).shift(band_shift(3))
        sa_lab = Tex(r"SA $\approx 0{,}63$").scale(0.85).shift(band_shift(3) + RIGHT * 1.3 + UP * 0.5)
        self.play(Create(d_no), Write(no_lab))
        self.wait(1.5)
        self.play(Create(d_sa), Write(sa_lab))
        self.wait(2)
        b3_l1 = Tex("0: all equal; 1: one earns everything").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("Per capita: size of each slice;").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        b3_l2b = Tex("Gini: how the knife actually cut").scale(1.0).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l2))
        self.play(Write(b3_l2b))
        self.play(Create(SurroundingRectangle(b3_l2b, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the social indicators
        self.next_band(4)
        b4_title = Tex("Beyond money: the social indicators").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Life expectancy: Japan $84+$; SA mid-60s,").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l1b = Tex("recovering since universal ARV treatment").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l1b))
        self.wait(2.5)
        b4_l2 = Tex(r"Infant mortality per $1\,000$ births:").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        b4_l2b = Tex(r"Finland $\approx 2$; worst $>60$; SA mid-20s").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l2))
        self.play(Write(b4_l2b))
        self.wait(2.5)
        b4_l3 = Tex("Most sensitive of all: a baby survives").scale(0.95).shift(band_shift(4) + DOWN * 2.2)
        b4_l3b = Tex("only when everything works at once").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l3))
        self.play(Write(b4_l3b))
        self.play(Create(SurroundingRectangle(b4_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the HDI
        self.next_band(5)
        b5_title = Tex("HDI: three dimensions, one score").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Health: life expectancy").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("Education: years of schooling").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("Income: GNI per capita").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l1))
        self.wait(1.5)
        self.play(Write(b5_l2))
        self.wait(1.5)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex(r"Switzerland $>0{,}95$; Niger $<0{,}45$;").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        b5_l5 = Tex(r"South Africa $\approx 0{,}71$").scale(1.1).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        b5_l6 = Tex("A top score cannot be bought").scale(0.95).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): Brandt line and the continuum
        self.next_band(6)
        b6_title = Tex("A continuum, not two boxes").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Brandt line (1980): rich North, poor South").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("But the photograph aged: Singapore and").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l2b = Tex("South Korea crossed the line").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.play(Write(b6_l2b))
        self.wait(2.5)
        b6_l3 = Tex("An unbroken line, every position filled —").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        b6_l3b = Tex("and it runs INSIDE countries too:").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        b6_l3c = Tex("Umhlanga and Inanda share a metro").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l3))
        self.play(Write(b6_l3b))
        self.play(Write(b6_l3c))
        self.wait(3)

        # --- Band 7 (subtopic_4): placing South Africa
        self.next_band(7)
        b7_title = Tex("Placing South Africa honestly").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("For: upper-middle income, industrial base,").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l1b = Tex(r"deep financial markets, HDI $\approx 0{,}71$").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l1b))
        self.wait(2.5)
        b7_l2 = Tex(r"Against: unemployment $>30\%$, Gini").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l2b = Tex(r"$\approx 0{,}63$, life expectancy in the 60s").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l2))
        self.play(Write(b7_l2b))
        self.wait(2.5)
        b7_l3 = Tex("Verdict: a developing NIC with pockets").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        b7_l3b = Tex("of MEDC wealth and LEDC deprivation").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l3))
        self.play(Write(b7_l3b))
        self.play(Create(SurroundingRectangle(b7_l3b, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): two streets in one town
        self.next_band(8)
        b8_title = Tex("Two streets in one town").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Street one: tar, taps, stocked clinic,").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l1b = Tex("study centre — development landed").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l1b))
        self.wait(2.5)
        b8_l2 = Tex("Street two: gravel, water by tanker —").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l2b = Tex("development lifts street two upward").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l2))
        self.play(Write(b8_l2b))
        self.wait(2.5)
        b8_l3 = Tex("Solar farm lifts output, dividends leave:").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        b8_l3b = Tex("rain that never reaches the taps").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l3))
        self.play(Write(b8_l3b))
        self.play(Create(SurroundingRectangle(b8_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the scoreboard problem
        self.next_band(9)
        b9_title = Tex("The scoreboard problem").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Total runs $=$ GDP; runs per player $=$").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l1b = Tex("per capita — divide by the squad").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l1b))
        self.wait(2.5)
        b9_l2 = Tex("Home ground: GDP; your contracted").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        b9_l2b = Tex("players anywhere: GNP — BMW bats for Germany").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l2))
        self.play(Write(b9_l2b))
        self.wait(2.5)
        b9_l3 = Tex("One batter 91, ten share 19: the").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        b9_l3b = Tex(r"average hides them — Gini 0{,}63").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l3))
        self.play(Write(b9_l3b))
        self.play(Create(SurroundingRectangle(b9_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the report card and the staircase
        self.next_band(10)
        b10_title = Tex("The report card with three subjects").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Health, education, income — average to").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l1b = Tex(r"one HDI mark: SA $\approx 0{,}71$, health drags").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.wait(2.5)
        b10_l2 = Tex("Sharpest test: infant mortality —").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        b10_l2b = Tex("falling to the mid-20s is real progress").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l2))
        self.play(Write(b10_l2b))
        self.wait(2.5)
        b10_l3 = Tex("Drop the two boxes: a staircase,").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        b10_l3b = Tex("SA mid-staircase, one foot high, one low").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l3b))
        self.play(Create(SurroundingRectangle(b10_l3b, color=GREEN)))
        self.wait(4)
