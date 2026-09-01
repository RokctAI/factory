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

# Band-layout whiteboard scene for the session duo "Cost and Revenue
# Analysis" (Grade 11, Term 2). One band per teaching step; the camera moves
# down to fresh space and nothing is removed. Exporter-safe mobjects only;
# the MC/MR graph is hand-built from Arrows, chained Lines and Dots. Band
# time apportioned to subtopics.json (230/200/230/260/180/160/190 of 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CostRevenueAnalysisSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the cost table and fixed cost ---
        title = Tex("Cost and Revenue Analysis").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        c1 = Tex(r"Output: 0, 1, 2, 3, 4, 5, 6 units").scale(1.1).shift(UP * 1.2)
        c2 = Tex(r"Total cost: 24, 44, 58, 70, 88, 120, 166").scale(1.1).shift(UP * 0.3)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2.5)
        c3 = Tex(r"At zero output cost is R24 $=$ FIXED cost").scale(1.05).shift(DOWN * 0.7)
        self.play(Write(c3))
        self.play(Create(SurroundingRectangle(c3, color=GREEN)))
        self.wait(2)
        c4 = Tex("The part that grows with output: VARIABLE cost").scale(1.0).shift(DOWN * 1.7)
        self.play(Write(c4))
        self.wait(3)

        # --- Band 1 (subtopic_1): average cost — divide ---
        self.next_band(1)
        b1_title = Tex(r"Average cost $=$ total cost $\div$ output").scale(1.15).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        a1 = MathTex(r"44 \div 1 = 44, \quad 58 \div 2 = 29, \quad 70 \div 3 \approx 23{,}33").scale(0.95).shift(band_shift(1) + UP * 1.2)
        a2 = MathTex(r"88 \div 4 = 22, \quad 120 \div 5 = 24").scale(1.0).shift(band_shift(1) + UP * 0.3)
        a3 = MathTex(r"166 \div 6 \approx 27{,}67").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(a1))
        self.wait(2.5)
        self.play(Write(a2))
        self.wait(2)
        self.play(Write(a3))
        self.wait(2)
        a4 = Tex("Slides down, bottoms at 4 units, then rises: the U-shape").scale(0.95).shift(band_shift(1) + DOWN * 1.6)
        a5 = Tex("Fixed R24 shared thinner, then capacity strains").scale(1.0).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(a4))
        self.wait(2)
        self.play(Write(a5))
        self.wait(3)

        # --- Band 2 (subtopic_1): marginal cost — subtract neighbours ---
        self.next_band(2)
        b2_title = Tex("Marginal cost: the extra cost of ONE more unit").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        m1 = MathTex(r"44 - 24 = 20, \quad 58 - 44 = 14, \quad 70 - 58 = 12").scale(1.0).shift(band_shift(2) + UP * 1.2)
        m2 = MathTex(r"88 - 70 = 18, \quad 120 - 88 = 32, \quad 166 - 120 = 46").scale(0.95).shift(band_shift(2) + UP * 0.3)
        self.play(Write(m1))
        self.wait(2.5)
        self.play(Write(m2))
        self.wait(2.5)
        m3 = Tex("MC sags, then climbs hard").scale(1.05).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Marginal cost $=$ total cost $\div$ output").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(m4))
        self.play(Create(strike(m4)))
        self.wait(1.5)
        m5 = Tex(r"Average: DIVIDE. \; Marginal: SUBTRACT neighbours.").scale(1.0).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(m5))
        self.play(Create(SurroundingRectangle(m5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the revenue side at R40 ---
        self.next_band(3)
        b3_title = Tex("Revenue at a market price of R40: price taker").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        r1 = Tex(r"Total revenue: 0, 40, 80, 120, 160, 200, 240").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(r1))
        self.wait(2.5)
        r2 = MathTex(r"\text{AR: } 40 \div 1 = 80 \div 2 = 120 \div 3 = \text{R}40").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex(r"Average revenue IS the price").scale(1.05).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(r3))
        self.wait(2)
        r4 = MathTex(r"\text{MR: } 80 - 40 = 120 - 80 = \text{R}40 \text{ every step}").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(r4))
        self.wait(2)
        r5 = Tex("Flat line at R40: fingerprint of perfect competition").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(r5))
        self.play(Create(SurroundingRectangle(r5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): brute-force profit column ---
        self.next_band(4)
        b4_title = Tex(r"Profit $=$ total revenue $-$ total cost").scale(1.15).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        p1 = MathTex(r"0 - 24 = -24, \quad 40 - 44 = -4, \quad 80 - 58 = 22").scale(0.95).shift(band_shift(4) + UP * 1.2)
        p2 = MathTex(r"120 - 70 = 50, \quad 160 - 88 = 72").scale(1.0).shift(band_shift(4) + UP * 0.3)
        p3 = MathTex(r"200 - 120 = 80, \quad 240 - 166 = 74").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(p1))
        self.wait(2.5)
        self.play(Write(p2))
        self.wait(2)
        self.play(Write(p3))
        self.wait(2)
        p4 = Tex(r"Profit crests at FIVE units with R80").scale(1.1).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(p4))
        self.play(Create(SurroundingRectangle(p4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the marginal march, MR = MC ---
        self.next_band(5)
        b5_title = Tex("The economist's method: think at the margin").scale(1.1).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        w1 = MathTex(r"\text{Unit 1: } 40>20\checkmark \; \text{Unit 2: } 40>14\checkmark").scale(0.86).shift(band_shift(5) + UP * 1.2)
        w2 = MathTex(r"\text{Unit 3: } 40>12\checkmark \; \text{Unit 4: } 40>18\checkmark").scale(0.86).shift(band_shift(5) + UP * 0.3)
        w3 = MathTex(r"\text{Unit 5: } 40 \text{ vs } 32 \;\checkmark \text{ (R8 ahead)}").scale(0.95).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(w1))
        self.wait(2.5)
        self.play(Write(w2))
        self.wait(2)
        self.play(Write(w3))
        self.wait(2)
        w4 = MathTex(r"\text{Unit 6: } 40 \text{ vs } 46 \text{ wipes out R6 — refuse}").scale(0.95).shift(band_shift(5) + DOWN * 1.5)
        self.play(Write(w4))
        self.play(Create(strike(w4)))
        self.wait(2)
        w5 = Tex(r"Produce until MR $=$ MC: halt at five").scale(1.1).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(w5))
        self.play(Create(SurroundingRectangle(w5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): verify both directions + the R74 trap ---
        self.next_band(6)
        b6_title = Tex("Verify from both directions").scale(1.15).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        v1 = Tex(r"Unit 5: MC R32 $<$ MR R40 — worth it ($+$R8)").scale(1.0).shift(band_shift(6) + UP * 1.2)
        v2 = Tex(r"Unit 6: MC R46 $>$ MR R40 — burns R6 of profit").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(v1))
        self.wait(2)
        self.play(Write(v2))
        self.wait(2)
        v3 = MathTex(r"200 - 120 = \text{R}80 \text{ — both methods agree}").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(v3))
        self.wait(2)
        v4 = Tex(r"Six units still gives R74, so six is fine").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(v4))
        self.play(Create(strike(v4)))
        self.wait(1.5)
        v5 = Tex(r"The test is: does the NEXT unit pay?").scale(1.05).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(v5))
        self.play(Create(SurroundingRectangle(v5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the graph — MC hook against flat MR ---
        self.next_band(7)
        b7_title = Tex("The graph the exam asks for").scale(1.15).shift(band_shift(7) + UP * 2.6)
        self.play(Write(b7_title))
        self.wait(1.5)
        org = band_shift(7) + LEFT * 4.6 + DOWN * 2.6
        # x: 1 unit of output = 1.3 world units; y: R10 = 0.8 world units.
        ax_y = Arrow(org, org + UP * 4.4, buff=0)
        ax_x = Arrow(org, org + RIGHT * 8.6, buff=0)
        ylab = Tex("Rand").scale(0.8).move_to(org + UP * 4.4 + RIGHT * 0.8)
        xlab = Tex("Output").scale(0.8).move_to(org + RIGHT * 8.6 + UP * 0.4)
        self.play(Create(ax_y), Create(ax_x), Write(ylab), Write(xlab))
        self.wait(1.5)
        # MC points: (1,20)(2,14)(3,12)(4,18)(5,32)(6,46)
        pts = [(1, 20), (2, 14), (3, 12), (4, 18), (5, 32), (6, 46)]
        world = [org + RIGHT * 1.3 * q + UP * 0.08 * r for q, r in pts]
        mc_lines = VGroup(*[Line(world[i], world[i + 1], stroke_width=5)
                            for i in range(len(world) - 1)])
        mc_lab = Tex("MC").scale(0.85).move_to(world[-1] + UP * 0.4)
        self.play(Create(mc_lines), Write(mc_lab))
        self.wait(2)
        mr_line = Line(org + UP * 3.2 + RIGHT * 0.2, org + UP * 3.2 + RIGHT * 8.2,
                       stroke_width=5, color=BLUE)
        mr_lab = Tex(r"MR $=$ AR $=$ R40").scale(0.8).move_to(org + UP * 3.6 + RIGHT * 7.0)
        self.play(Create(mr_line), Write(mr_lab))
        self.wait(2)
        cross = Dot(org + RIGHT * 1.3 * 5.57 + UP * 3.2, color=RED)
        cross_lab = Tex("MC breaks above MR").scale(0.75).move_to(org + RIGHT * 5.2 + UP * 3.8)
        self.play(Create(cross), Write(cross_lab))
        self.wait(2)
        ans = Tex("Last whole unit before the break: FIVE").scale(0.95).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(ans))
        self.play(Create(SurroundingRectangle(ans, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): costs that sleep, costs that work ---
        self.next_band(8)
        b8_title = Tex("The boerewors-roll stand: sleeping and working costs").scale(1.0).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        s1 = Tex("Stall fee, gazebo, gas bottle: owed before one roll").scale(0.95).shift(band_shift(8) + UP * 1.3)
        s2 = Tex(r"That is the R24 at zero output — FIXED").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.wait(2)
        s3 = Tex("Rolls, wors, onions, the helper: VARIABLE").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(s3))
        self.wait(2)
        s4 = MathTex(r"\text{Average: } 70 \div 3 \approx 23{,}33 \quad \text{(divide)}").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        s5 = MathTex(r"\text{Marginal: } 88 - 70 = 18 \quad \text{(subtract)}").scale(1.0).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(s4))
        self.wait(2)
        self.play(Write(s5))
        self.play(Create(SurroundingRectangle(VGroup(s4, s5), color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): forty rand a roll ---
        self.next_band(9)
        b9_title = Tex("R40 a roll, every single roll").scale(1.15).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        q1 = Tex("One stand in a row of stands: a price taker").scale(1.0).shift(band_shift(9) + UP * 1.3)
        self.play(Write(q1))
        self.wait(2)
        q2 = Tex(r"Takings: 40, 80, 120, 160, 200, 240 — equal steps").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(q2))
        self.wait(2)
        q3 = MathTex(r"120 \div 3 = 40, \quad 120 - 80 = 40").scale(1.05).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(q3))
        self.wait(2)
        q4 = Tex(r"AR $=$ MR $=$ price: one flat line at R40").scale(1.05).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(q4))
        self.play(Create(SurroundingRectangle(q4, color=GREEN)))
        self.wait(2)
        q5 = Tex("Next year's monopoly line will tilt downhill").scale(0.95).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(q5))
        self.wait(3)

        # --- Band 10 (subtopic_7): is the next one worth making? ---
        self.next_band(10)
        b10_title = Tex("Is the next one worth making?").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        n1 = Tex(r"Profits: $-24$, $-4$, 22, 50, 72, 80, 74").scale(1.05).shift(band_shift(10) + UP * 1.3)
        self.play(Write(n1))
        self.wait(2.5)
        n2 = Tex(r"Roll 5: brings R40, costs R32 — make it").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(n2))
        self.wait(2)
        n3 = Tex(r"Roll 6: brings R40, costs R46 — refuse it").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(n3))
        self.play(Create(strike(n3)))
        self.wait(2)
        n4 = Tex(r"``Am I making money?'' is the wrong question").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(n4))
        self.wait(2)
        n5 = Tex(r"Halt at five: keep going while the next one pays").scale(1.0).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(n5))
        self.play(Create(SurroundingRectangle(n5, color=GREEN)))
        self.wait(4)
