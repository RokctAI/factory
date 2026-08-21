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

# Band-layout whiteboard scene for the IEB Grade 11 Geography session duo
# "Development Aid and Its Impact". One band per teaching beat; the camera
# moves down, nothing is removed. Text-led with primitive accents.
# Subtopic shares follow subtopics.json: 225/240/225/230/190/195/200 of 1505 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DevelopmentAidIEBSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): definition and channels
        title = Tex("Development Aid and Its Impact").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("Aid (ODA): resources on gentler terms —").scale(0.95).shift(UP * 1.1)
        s0_l1b = Tex("grants, or concessional loans").scale(0.95).shift(UP * 0.3)
        self.play(Write(s0_l1))
        self.play(Write(s0_l1b))
        self.wait(2.5)
        s0_l2 = Tex("Bilateral: state to state").scale(0.95).shift(DOWN * 0.6)
        s0_l3 = Tex("Multilateral: World Bank, UN, AfDB").scale(0.95).shift(DOWN * 1.4)
        s0_l4 = Tex("NGO: fast and close to the ground").scale(0.95).shift(DOWN * 2.2)
        self.play(Write(s0_l2))
        self.wait(1.5)
        self.play(Write(s0_l3))
        self.wait(1.5)
        self.play(Write(s0_l4))
        self.play(Create(SurroundingRectangle(s0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): co-operation and motives
        self.next_band(1)
        b1_title = Tex("From charity to co-operation").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Partnership, duties both ways: recipient").scale(0.9).shift(band_shift(1) + UP * 1.2)
        b1_l1b = Tex("sets priorities, donor funds THAT plan").scale(0.9).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l1b))
        self.wait(2.5)
        b1_l2 = Tex("SA: both chairs — receives health").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        b1_l2b = Tex("funding, assists via Renaissance Fund").scale(0.95).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(b1_l2))
        self.play(Write(b1_l2b))
        self.wait(2.5)
        b1_l3 = Tex("Motives are mixed: solidarity plus").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        b1_l3b = Tex("influence, trade, security — say so").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l3))
        self.play(Write(b1_l3b))
        self.play(Create(SurroundingRectangle(b1_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three types
        self.next_band(2)
        b2_title = Tex("Three types, exact definitions").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("TECHNICAL: skills, not cash —").scale(0.95).shift(band_shift(2) + UP * 1.2)
        b2_l1b = Tex("spent once, works for decades").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l1b))
        self.wait(2.5)
        b2_l2 = Tex("CONDITIONAL: strings — buy from my").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        b2_l2b = Tex("shop; run your house my way").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l2))
        self.play(Write(b2_l2b))
        self.wait(2.5)
        b2_l3 = Tex("HUMANITARIAN: fast relief — Freddy,").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        b2_l3b = Tex("Horn drought, KZN floods").scale(0.95).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l3))
        self.play(Write(b2_l3b))
        self.play(Create(SurroundingRectangle(b2_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): short-term vs long-term
        self.next_band(3)
        b3_title = Tex("Short-term against long-term").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Relief STOPS THE BLEEDING;").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("development BUILDS THE HOSPITAL").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Structural adjustment, 1980s--90s:").scale(0.95).shift(band_shift(3) + DOWN * 0.6)
        b3_l3b = Tex("cuts, privatisation, open markets —").scale(0.95).shift(band_shift(3) + DOWN * 1.4)
        b3_l3c = Tex("clinics and classrooms paid the bill").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l3))
        self.play(Write(b3_l3b))
        self.play(Write(b3_l3c))
        self.wait(3)

        # --- Band 4 (subtopic_3): the positive case — health
        self.next_band(4)
        b4_title = Tex("When aid works: the evidence").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Smallpox: ERADICATED by aid-funded").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l1b = Tex("vaccination; polio at the brink").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l1b))
        self.wait(2.5)
        b4_l2 = Tex("Global Fund + PEPFAR: world's largest").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        b4_l2b = Tex("ARV programme — life expectancy back").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        b4_l2c = Tex("from low 50s to above 60").scale(0.95).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l2))
        self.play(Write(b4_l2b))
        self.play(Write(b4_l2c))
        self.play(Create(SurroundingRectangle(b4_l2c, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex("Malaria deaths cut by nets and medicine").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l3))
        self.wait(3)

        # --- Band 5 (subtopic_3): relief, infrastructure, catalysis
        self.next_band(5)
        b5_title = Tex("Relief, roads and the catalyst").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Fast relief: KZN floods in days;").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l1b = Tex("earthquake rubble within the week").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l1b))
        self.wait(2.5)
        b5_l2 = Tex("Concessional finance: the roads and").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l2b = Tex("power lines private capital avoids").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l2))
        self.play(Write(b5_l2b))
        self.wait(2.5)
        b5_l3 = Tex("Works best: specific, measurable,").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        b5_l3b = Tex("recipient-aligned, finished properly").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l3))
        self.play(Write(b5_l3b))
        self.play(Create(SurroundingRectangle(b5_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): dependency, distortion, debt
        self.next_band(6)
        b6_title = Tex("When aid fails: three Ds").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("DEPENDENCY: answering to donors,").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l1b = Tex("not voters; tax base unbuilt").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l1b))
        self.wait(2.5)
        b6_l2 = Tex("DISTORTION: free food beaches farmers;").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        b6_l2b = Tex("donor salaries hollow the ministries").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l2))
        self.play(Write(b6_l2b))
        self.wait(2.5)
        b6_l3 = Tex("DEBT: service exceeded health plus").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        b6_l3b = Tex("education spending — aid in reverse").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l3))
        self.play(Write(b6_l3b))
        self.play(Create(SurroundingRectangle(b6_l3b, color=RED)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the verdict
        self.next_band(7)
        b7_title = Tex("The balanced verdict").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Plus corruption and fragmentation:").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l1b = Tex("a hundred projects, a hundred logos").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l1b))
        self.wait(2.5)
        b7_l2 = Tex("Aid is a TOOL, not a verdict —").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l2b = Tex("strong on solvable problems, risky").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        b7_l2c = Tex("as a permanent strategy").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l2))
        self.play(Write(b7_l2b))
        self.play(Write(b7_l2c))
        self.wait(2)
        b7_l3 = Tex("Scaffolding: up while building, then down").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): fish, fishing lessons, the flood
        self.next_band(8)
        b8_title = Tex("Fish, fishing lessons and the flood").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("FISH $=$ humanitarian: feeds today,").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l1b = Tex("cannot lay the drainage").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l1b))
        self.wait(2.5)
        b8_l2 = Tex("LESSON $=$ technical: spent once,").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        b8_l2b = Tex("works thirty years — except mid-flood").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l2))
        self.play(Write(b8_l2b))
        self.wait(2.5)
        b8_l3 = Tex("Free fish forever: boats beached —").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        b8_l3b = Tex("DEPENDENCY, the bridge become crutch").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l3))
        self.play(Write(b8_l3b))
        self.play(Create(SurroundingRectangle(b8_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the gift with strings
        self.next_band(9)
        b9_title = Tex("The gift with strings").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("String one: buy the pump from MY shop —").scale(0.9).shift(band_shift(9) + UP * 1.2)
        b9_l1b = Tex("procurement tying, costs inflate").scale(0.9).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l1b))
        self.wait(2.5)
        b9_l2 = Tex("String two: run your house MY way —").scale(0.9).shift(band_shift(9) + DOWN * 0.5)
        b9_l2b = Tex("policy conditionality, adjustment era").scale(0.9).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l2))
        self.play(Write(b9_l2b))
        self.wait(2.5)
        b9_l3 = Tex("Upgrade: co-operation — their plan,").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        b9_l3b = Tex("your contribution, duties both ways").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l3))
        self.play(Write(b9_l3b))
        self.play(Create(SurroundingRectangle(b9_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the geographer's scale
        self.next_band(10)
        b10_title = Tex("Weighing aid like a geographer").scale(1.1).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(2)
        beam = Line(LEFT * 4.0 + UP * 1.2, RIGHT * 4.0 + UP * 1.2, color=WHITE).shift(band_shift(10))
        pivot = Dot(UP * 1.2, color=YELLOW).shift(band_shift(10))
        self.play(Create(beam), Create(pivot))
        left_lab = Tex("triumphs: smallpox, ARVs,").scale(0.75).shift(band_shift(10) + LEFT * 3.4 + UP * 0.4)
        left_lab2 = Tex("malaria, fast relief").scale(0.75).shift(band_shift(10) + LEFT * 3.4 + DOWN * 0.3)
        right_lab = Tex("failures: dependency, debt,").scale(0.75).shift(band_shift(10) + RIGHT * 3.4 + UP * 0.4)
        right_lab2 = Tex("distortion, strings").scale(0.75).shift(band_shift(10) + RIGHT * 3.4 + DOWN * 0.3)
        self.play(Write(left_lab), Write(left_lab2))
        self.wait(1.5)
        self.play(Write(right_lab), Write(right_lab2))
        self.wait(2)
        b10_l1 = Tex("Aid is SCAFFOLDING: essential while").scale(0.95).shift(band_shift(10) + DOWN * 1.4)
        b10_l1b = Tex("building, never the house, designed").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        b10_l1c = Tex("from day one to come down").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.play(Write(b10_l1c))
        self.play(Create(SurroundingRectangle(b10_l1c, color=GREEN)))
        self.wait(4)
