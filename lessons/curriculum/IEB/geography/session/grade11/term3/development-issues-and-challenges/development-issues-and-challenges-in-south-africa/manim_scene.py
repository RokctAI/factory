# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
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
# "Development Issues and Challenges in South Africa". One band per teaching
# beat; the camera moves down, nothing is removed. Text-led with primitive
# accents. Subtopic shares follow subtopics.json:
# 235/230/235/225/190/195/200 of 1510 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DevelopmentChallengesSAIEBSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the factors, first links
        title = Tex("Development Issues and Challenges").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("Factors: resources, energy, history,").scale(1.0).shift(UP * 1.1)
        s0_l1b = Tex("trade, population, education, environment").scale(1.0).shift(UP * 0.3)
        self.play(Write(s0_l1))
        self.play(Write(s0_l1b))
        self.wait(2.5)
        s0_l2 = Tex("Resource curse: Angola's oil, poverty;").scale(0.95).shift(DOWN * 0.7)
        s0_l2b = Tex("Botswana's diamonds, schools").scale(0.95).shift(DOWN * 1.5)
        self.play(Write(s0_l2))
        self.play(Write(s0_l2b))
        self.wait(2.5)
        s0_l3 = Tex("Never the rocks — what is DONE with them").scale(1.0).shift(DOWN * 2.5)
        self.play(Write(s0_l3))
        self.play(Create(SurroundingRectangle(s0_l3, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the chain — INTERRELATED
        self.next_band(1)
        b1_title = Tex("The chain: INTERRELATED").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        c1 = Tex("drought").scale(0.9).shift(band_shift(1) + LEFT * 4.5 + UP * 1.0)
        c2 = Tex("child leaves school").scale(0.9).shift(band_shift(1) + LEFT * 0.8 + UP * 1.0)
        c3 = Tex("skills fall").scale(0.9).shift(band_shift(1) + RIGHT * 3.2 + UP * 1.0)
        a1 = Line(c1.get_right(), c2.get_left(), color=YELLOW)
        a2 = Line(c2.get_right(), c3.get_left(), color=YELLOW)
        self.play(Write(c1))
        self.play(Create(a1), Write(c2))
        self.play(Create(a2), Write(c3))
        self.wait(2)
        c4 = Tex("investment leaves").scale(0.9).shift(band_shift(1) + LEFT * 3.2 + DOWN * 0.4)
        c5 = Tex("land overworked").scale(0.9).shift(band_shift(1) + RIGHT * 0.6 + DOWN * 0.4)
        c6 = Tex("next drought worse").scale(0.9).shift(band_shift(1) + RIGHT * 4.2 + DOWN * 0.4)
        self.play(Write(c4))
        self.play(Write(c5))
        self.play(Write(c6))
        self.wait(2)
        b1_l1 = Tex("One factor alone $=$ half the story;").scale(0.95).shift(band_shift(1) + DOWN * 1.6)
        b1_l1b = Tex("trace the chain for full marks").scale(0.95).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l1b))
        self.play(Create(SurroundingRectangle(b1_l1b, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): SA's numbers
        self.next_band(2)
        b2_title = Tex("South Africa's particular burdens").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Spatial legacy: settled far from work,").scale(0.95).shift(band_shift(2) + UP * 1.2)
        b2_l1b = Tex("poorest land — the map outlives the laws").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l1b))
        self.wait(2.5)
        b2_l2 = Tex(r"Gini $\approx 0{,}63$; unemployment $>30\%$,").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        b2_l2b = Tex(r"youth $>40\%$ — the core challenge").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l2))
        self.play(Write(b2_l2b))
        self.play(Create(SurroundingRectangle(b2_l2b, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("Skills pipeline leaks: vacancies beside").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        b2_l3b = Tex("joblessness — the mismatch bottleneck").scale(0.95).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l3))
        self.play(Write(b2_l3b))
        self.wait(3)

        # --- Band 3 (subtopic_2): the strained machinery + balance
        self.next_band(3)
        b3_title = Tex("Strain and balance").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Services: millions connected since 1994 —").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l1b = Tex("yet backlogs, breakdowns, protests").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l1b))
        self.wait(2.5)
        b3_l2 = Tex("Health: ARV programme bent the curve;").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        b3_l2b = Tex("TB and lifestyle disease still load it").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l2))
        self.play(Write(b3_l2b))
        self.wait(2.5)
        b3_l3 = Tex("Balanced essay: gains AND strain,").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        b3_l3b = Tex("both halves true at once").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l3))
        self.play(Write(b3_l3b))
        self.play(Create(SurroundingRectangle(b3_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): community principles + rural cases
        self.next_band(4)
        b4_title = Tex("Community-based development").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Principles: participation, local knowledge,").scale(0.9).shift(band_shift(4) + UP * 1.2)
        b4_l1b = Tex("fit technology, skills transfer, OWNERSHIP").scale(0.9).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l1b))
        self.wait(2.5)
        b4_l2 = Tex("Working for Wetlands: gullies plugged,").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        b4_l2b = Tex("water held, wages and skills earned").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l2))
        self.play(Write(b4_l2b))
        self.wait(2.5)
        b4_l3 = Tex("Wupperthal rooibos co-ops: pooled tea,").scale(0.95).shift(band_shift(4) + DOWN * 2.2)
        b4_l3b = Tex("profits stay in the valley").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l3))
        self.play(Write(b4_l3b))
        self.play(Create(SurroundingRectangle(b4_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): urban cases + the honest limit
        self.next_band(5)
        b5_title = Tex("Urban cases and the honest limit").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Warwick Junction: planned WITH traders —").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l1b = Tex("a feared interchange became a market").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l1b))
        self.wait(2.5)
        b5_l2 = Tex("Enkanini: community-run solar;").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l2b = Tex("upgrade IN PLACE, keep the networks").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l2))
        self.play(Write(b5_l2b))
        self.wait(2.5)
        b5_l3 = Tex("Limit: small against national need —").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        b5_l3b = Tex("complements the state, never replaces it").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l3))
        self.play(Write(b5_l3b))
        self.play(Create(SurroundingRectangle(b5_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the damage list
        self.next_band(6)
        b6_title = Tex("Development's environmental bill").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Mining: Olifants River acidic, metal-laden").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("Energy: eMalahleni's air over maize soils").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Overgrazing: topsoil silts Eastern Cape dams").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("Urban sprawl over wetlands; sewage in rivers").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Coal: among the heaviest carbon").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        b6_l5b = Tex("emitters per person").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l5))
        self.play(Write(b6_l5b))
        self.wait(3)

        # --- Band 7 (subtopic_4): the two truths and the tools
        self.next_band(7)
        b7_title = Tex("Two truths, one solution").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Damage $=$ a loan against development,").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l1b = Tex("repaid with interest — by the poor first").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l1b))
        self.wait(2.5)
        b7_l2 = Tex("Poverty also degrades: firewood stripped,").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l2b = Tex("fragile veld overstocked").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l2))
        self.play(Write(b7_l2b))
        self.wait(2.5)
        b7_l3 = Tex("Sustainable development: EIAs, mine rehab,").scale(0.9).shift(band_shift(7) + DOWN * 2.2)
        b7_l3b = Tex("parks earning tourism, sun and wind").scale(0.9).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l3))
        self.play(Write(b7_l3b))
        self.play(Create(SurroundingRectangle(b7_l3b, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the knot in the earphones
        self.next_band(8)
        b8_title = Tex("The knot in the earphones").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Fish stocks thin (resources); daughter").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l1b = Tex("leaves school (education); raw fish sold").scale(0.95).shift(band_shift(8) + UP * 0.4)
        b8_l1c = Tex("cheap, tinned bought dear (trade)").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l1b))
        self.play(Write(b8_l1c))
        self.wait(2.5)
        b8_l2 = Tex("No power, no ice (energy); moved off the").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        b8_l2b = Tex("fishing grounds by decree (history)").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l2))
        self.play(Write(b8_l2b))
        self.wait(2.5)
        b8_l3 = Tex("Write the chain — INTERRELATED").scale(1.0).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the meeting on the stoep
        self.next_band(9)
        b9_title = Tex("The meeting on the stoep").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Golden rule: people maintain").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l1b = Tex("what is THEIRS").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l1b))
        self.play(Create(SurroundingRectangle(b9_l1b, color=GREEN)))
        self.wait(2.5)
        b9_l2 = Tex("Wetlands healed for wages; Wupperthal").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        b9_l2b = Tex("tea pooled; Warwick planned with traders").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l2))
        self.play(Write(b9_l2b))
        self.wait(2.5)
        b9_l3 = Tex("Honest limit: stoep projects are small —").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        b9_l3b = Tex("community hands AND state muscle").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l3))
        self.play(Write(b9_l3b))
        self.wait(3)

        # --- Band 10 (subtopic_7): borrowing from tomorrow's roof
        self.next_band(10)
        b10_title = Tex("Borrowing from tomorrow's roof").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Burn the beams: warm tonight,").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l1b = Tex("drenched when the rains come").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.wait(2.5)
        b10_l2 = Tex("The bill lands on the poor first —").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10_l2b = Tex("the shack beside the dump, the brown river").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l2))
        self.play(Write(b10_l2b))
        self.wait(2.5)
        b10_l3 = Tex("Build without burning the beams:").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        b10_l3b = Tex("EIAs, rehab, parks, sun and wind").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l3b))
        self.play(Create(SurroundingRectangle(b10_l3b, color=GREEN)))
        self.wait(4)
