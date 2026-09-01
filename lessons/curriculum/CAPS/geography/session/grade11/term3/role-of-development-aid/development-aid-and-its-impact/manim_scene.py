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

# Band-layout whiteboard scene for the CAPS Grade 11 Geography session duo
# "Development Aid and Its Impact". One band per teaching beat; the camera
# moves down, nothing is removed. Text-led topic with primitive accents only.
# Subtopic shares follow subtopics.json: 225/240/225/230/190/195/200 of 1505 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DevelopmentAidSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): definition and channels
        title = Tex("Development Aid and Its Impact").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("Aid (ODA): resources transferred on terms").scale(1.0).shift(UP * 1.1)
        s0_l1b = Tex("softer than the market's — grants,").scale(1.0).shift(UP * 0.3)
        s0_l1c = Tex("concessional loans").scale(1.0).shift(DOWN * 0.5)
        self.play(Write(s0_l1))
        self.play(Write(s0_l1b))
        self.play(Write(s0_l1c))
        self.wait(2.5)
        s0_l2 = Tex("Bilateral: government to government").scale(0.95).shift(DOWN * 1.4)
        s0_l3 = Tex("Multilateral: World Bank, UN, AfDB").scale(0.95).shift(DOWN * 2.2)
        s0_l4 = Tex("NGO: Gift of the Givers, MSF — private").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(s0_l2))
        self.wait(1.5)
        self.play(Write(s0_l3))
        self.wait(1.5)
        self.play(Write(s0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): co-operation and motives
        self.next_band(1)
        b1_title = Tex("From aid to co-operation").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Aid language: donor and passive recipient").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("Co-operation: partnership — recipients").scale(0.95).shift(band_shift(1) + UP * 0.4)
        b1_l2b = Tex("set priorities, donors align with them").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Write(b1_l2b))
        self.play(Create(SurroundingRectangle(b1_l2b, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("SA sits on both sides: health recipient,").scale(0.95).shift(band_shift(1) + DOWN * 1.4)
        b1_l3b = Tex("African Renaissance Fund donor").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l3))
        self.play(Write(b1_l3b))
        self.wait(2)
        b1_l4 = Tex("Motives are mixed: influence, trade, security").scale(0.9).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three types
        self.next_band(2)
        b2_title = Tex("Technical, conditional, humanitarian").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("TECHNICAL: skills, not cash — a skill").scale(0.95).shift(band_shift(2) + UP * 1.2)
        b2_l1b = Tex("keeps working after the money is spent").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l1b))
        self.wait(2.5)
        b2_l2 = Tex("CONDITIONAL (tied): procurement tying —").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        b2_l2b = Tex("buy the donor's goods; policy strings —").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        b2_l2c = Tex("structural adjustment gutted clinics").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l2))
        self.play(Write(b2_l2b))
        self.play(Write(b2_l2c))
        self.wait(2.5)
        b2_l3 = Tex("HUMANITARIAN: fast relief — Idai, KZN floods").scale(0.9).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l3))
        self.wait(3)

        # --- Band 3 (subtopic_2): short-term vs long-term
        self.next_band(3)
        b3_title = Tex("Stop the bleeding vs build the hospital").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Short-term relief treats symptoms —").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l1b = Tex("by design; it saves lives fast").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l1b))
        self.wait(2.5)
        b3_l2 = Tex("Long-term development aid builds the").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        b3_l2b = Tex("systems whose absence made it deadly").scale(1.0).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l2))
        self.play(Write(b3_l2b))
        self.wait(2.5)
        b3_l3 = Tex("Category error: judging food aid for").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        b3_l3b = Tex("failing to industrialise a country").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l3))
        self.play(Write(b3_l3b))
        self.play(Create(SurroundingRectangle(b3_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the positive case — health
        self.next_band(4)
        b4_title = Tex("When aid works: the health record").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Smallpox ERADICATED by aid-funded").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l1b = Tex("vaccination; polio near extinction").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l1b))
        self.wait(2.5)
        b4_l2 = Tex("PEPFAR and Global Fund: SA's ARV").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        b4_l2b = Tex("programme — life expectancy climbed").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        b4_l2c = Tex("from the low 50s back above 60").scale(0.95).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l2))
        self.play(Write(b4_l2b))
        self.play(Write(b4_l2c))
        self.play(Create(SurroundingRectangle(b4_l2c, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex("Malaria deaths cut by nets and treatment").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l3))
        self.wait(3)

        # --- Band 5 (subtopic_3): relief, infrastructure, catalysis
        self.next_band(5)
        b5_title = Tex("Relief, roads and the catalyst effect").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Gift of the Givers in KZN within days;").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l1b = Tex("Ebola contained in West Africa, 2014").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l1b))
        self.wait(2.5)
        b5_l2 = Tex("Concessional finance builds what private").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l2b = Tex("capital will not risk; Green Revolution").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l2))
        self.play(Write(b5_l2b))
        self.wait(2.5)
        b5_l3 = Tex("Works best: targeted, aligned with the").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        b5_l3b = Tex("recipient's plan, sustained to the finish").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l3))
        self.play(Write(b5_l3b))
        self.play(Create(SurroundingRectangle(b5_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): dependency, distortion, debt
        self.next_band(6)
        b6_title = Tex("When aid fails: the three D's").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("DEPENDENCY: accountable to donors, not").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l1b = Tex("voters — the bridge becomes a crutch").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l1b))
        self.wait(2.5)
        b6_l2 = Tex("DISTORTION: dumped food undercuts").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6_l2b = Tex("farmers; projects poach the best staff").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l2))
        self.play(Write(b6_l2b))
        self.wait(2.5)
        b6_l3 = Tex("DEBT: 1980s--90s service exceeded health").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        b6_l3b = Tex("plus education spending — aid in reverse").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l3))
        self.play(Write(b6_l3b))
        self.wait(3)

        # --- Band 7 (subtopic_4): the verdict
        self.next_band(7)
        b7_title = Tex("The scaffolding verdict").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Add corruption skimming, and").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l1b = Tex("fragmentation drowning small ministries").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l1b))
        self.wait(2.5)
        b7_l2 = Tex("Aid is a tool, not a verdict: strong on").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l2b = Tex("solvable problems, dangerous as a").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        b7_l2c = Tex("permanent economic strategy").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l2))
        self.play(Write(b7_l2b))
        self.play(Write(b7_l2c))
        self.wait(2.5)
        b7_l3 = Tex("Scaffolding: essential, then removed").scale(1.0).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): fish, fishing lessons, the flood
        self.next_band(8)
        b8_title = Tex("Fish, fishing lessons and the flood").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("The FISH: relief — boats, blankets,").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l1b = Tex("medicine, fast; it feeds today only").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l1b))
        self.wait(2.5)
        b8_l2 = Tex("The LESSON: technical aid — a skill").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l2b = Tex("works for thirty years; useless mid-flood").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l2))
        self.play(Write(b8_l2b))
        self.wait(2.5)
        b8_l3 = Tex("Free fish forever: fishermen beach their").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        b8_l3b = Tex("boats — DEPENDENCY, bridge turned crutch").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l3))
        self.play(Write(b8_l3b))
        self.play(Create(SurroundingRectangle(b8_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the gift with strings
        self.next_band(9)
        b9_title = Tex("The gift with strings").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("String one — buy from MY shop:").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l1b = Tex("procurement tying, inflated invoices").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l1b))
        self.wait(2.5)
        b9_l2 = Tex("String two — run your house MY way:").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        b9_l2b = Tex("structural adjustment cut the clinics").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l2))
        self.play(Write(b9_l2b))
        self.wait(2.5)
        b9_l3 = Tex("Upgrade: co-operation — their plan, both").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        b9_l3b = Tex("sides accountable; SA sits on both sides").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l3))
        self.play(Write(b9_l3b))
        self.play(Create(SurroundingRectangle(b9_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the examiner's scale
        self.next_band(10)
        b10_title = Tex("Weighing aid like an examiner").scale(1.15).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        # balance scale: beam + pans
        beam = Line(LEFT * 3.2 + UP * 1.6, RIGHT * 3.2 + UP * 1.6, color=WHITE).shift(band_shift(10))
        post = Line(UP * 1.6, UP * 0.8, color=WHITE).shift(band_shift(10))
        pan_l = Line(LEFT * 3.2 + UP * 1.6, LEFT * 3.2 + UP * 0.9, color=WHITE).shift(band_shift(10))
        pan_r = Line(RIGHT * 3.2 + UP * 1.6, RIGHT * 3.2 + UP * 0.9, color=WHITE).shift(band_shift(10))
        self.play(Create(beam), Create(post), Create(pan_l), Create(pan_r))
        win_lab = Tex("smallpox gone, ARVs,").scale(0.8).shift(band_shift(10) + LEFT * 3.2 + UP * 0.3)
        win_lab2 = Tex("malaria nets, KZN relief").scale(0.8).shift(band_shift(10) + LEFT * 3.2 + DOWN * 0.4)
        fail_lab = Tex("beached farmers, debt,").scale(0.8).shift(band_shift(10) + RIGHT * 3.2 + UP * 0.3)
        fail_lab2 = Tex("strings, dependency").scale(0.8).shift(band_shift(10) + RIGHT * 3.2 + DOWN * 0.4)
        self.play(Write(win_lab), Write(win_lab2))
        self.wait(2)
        self.play(Write(fail_lab), Write(fail_lab2))
        self.wait(2.5)
        b10_l1 = Tex("Aid is scaffolding: essential during").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        b10_l1b = Tex("construction, never called the house,").scale(1.0).shift(band_shift(10) + DOWN * 2.3)
        b10_l1c = Tex("designed to become unnecessary").scale(1.0).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.play(Write(b10_l1c))
        self.play(Create(SurroundingRectangle(b10_l1c, color=GREEN)))
        self.wait(4)
