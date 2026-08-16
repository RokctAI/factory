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

# Band-layout whiteboard scene for the CAPS Grade 11 Geography session duo
# "Development Issues and Challenges in South Africa". One band per teaching
# beat; the camera moves down, nothing is removed. Text-led topic: boards
# built from Tex/MathTex with Arrow/Line/Rectangle accents only.
# Subtopic shares follow subtopics.json: 235/230/235/225/190/195/200 of 1510 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DevelopmentChallengesSASession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the factors, first links
        title = Tex("Development Issues and Challenges").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("Resources are not destiny:").scale(1.05).shift(UP * 1.1)
        s0_l2 = Tex("DRC rich and poor; Singapore bare, rich").scale(1.05).shift(UP * 0.3)
        self.play(Write(s0_l1))
        self.play(Write(s0_l2))
        self.wait(2.5)
        s0_l3 = Tex("Captured by a few: the RESOURCE CURSE").scale(1.05).shift(DOWN * 0.6)
        self.play(Write(s0_l3))
        self.play(Create(SurroundingRectangle(s0_l3, color=GREEN)))
        self.wait(2)
        s0_l4 = Tex("Energy: no power, no factories, pumps,").scale(1.0).shift(DOWN * 1.5)
        s0_l4b = Tex("cold chains or evening study").scale(1.0).shift(DOWN * 2.3)
        self.play(Write(s0_l4))
        self.play(Write(s0_l4b))
        self.wait(2)
        s0_l5 = Tex("History: colonial borders, mine-to-port rail").scale(0.95).shift(DOWN * 3.1)
        self.play(Write(s0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the chain — INTERRELATED
        self.next_band(1)
        b1_title = Tex("The factors pull each other").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Trade imbalances drain capital;").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("population growth divides each gain;").scale(1.0).shift(band_shift(1) + UP * 0.4)
        b1_l3 = Tex("education is the master key").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex(r"Drought $\rightarrow$ child leaves school $\rightarrow$").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        b1_l4b = Tex(r"skills fall $\rightarrow$ no investment $\rightarrow$").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        b1_l4c = Tex(r"land overworked $\rightarrow$ next drought worse").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l4))
        self.play(Write(b1_l4b))
        self.play(Write(b1_l4c))
        self.play(Create(SurroundingRectangle(b1_l4c, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): SA's numbers
        self.next_band(2)
        b2_title = Tex("South Africa's particular challenges").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Apartheid spatial legacy: people placed").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l1b = Tex("far from jobs, on the worst land").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l1b))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{Gini} \approx 0{,}63").scale(1.15).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = Tex(r"Unemployment $>30\%$; youth $>40\%$").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex("Growth without absorbing labour").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): the strained machinery + balance
        self.next_band(3)
        b3_title = Tex("Strained machinery — and real gains").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Education: strong enrolment, weak").scale(0.95).shift(band_shift(3) + UP * 1.4)
        b3_l1b = Tex("outcomes — vacancies beside joblessness").scale(0.95).shift(band_shift(3) + UP * 0.7)
        self.play(Write(b3_l1))
        self.play(Write(b3_l1b))
        self.wait(2.5)
        b3_l2 = Tex("Services: millions connected since 1994,").scale(0.95).shift(band_shift(3) + UP * 0.0)
        b3_l2b = Tex("yet backlogs and protests persist").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l2))
        self.play(Write(b3_l2b))
        self.wait(2.5)
        b3_l3 = Tex("HIV curve turned by the ARV programme;").scale(0.95).shift(band_shift(3) + DOWN * 1.4)
        b3_l3b = Tex("load-shedding: a development issue").scale(0.95).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l3))
        self.play(Write(b3_l3b))
        self.wait(2)
        b3_l4 = Tex("Both halves true — half-view, half marks").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): community principles + rural cases
        self.next_band(4)
        b4_title = Tex("Community-based development: rural").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Principles: participation, local knowledge,").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l1b = Tex("skills transfer, OWNERSHIP").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l1b))
        self.wait(2.5)
        b4_l2 = Tex("Working for Water: clear alien wattle").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        b4_l2b = Tex("and gum — streams return, wages earned").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l2))
        self.play(Write(b4_l2b))
        self.wait(2.5)
        b4_l3 = Tex("Food gardens, stokvel savings groups;").scale(0.95).shift(band_shift(4) + DOWN * 2.2)
        b4_l3b = Tex("Eastern Cape wool co-ops lifted prices").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l3))
        self.play(Write(b4_l3b))
        self.wait(3)

        # --- Band 5 (subtopic_3): urban cases + the honest limit
        self.next_band(5)
        b5_title = Tex("Community-based development: urban").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Khayelitsha: residents co-designed lit").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l1b = Tex("walkways on routes they walk — crime fell").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l1b))
        self.wait(2.5)
        b5_l2 = Tex("Upgrade IN PLACE: tenure, water, power").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l2b = Tex("where people built — not relocation").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l2))
        self.play(Write(b5_l2b))
        self.wait(2.5)
        b5_l3 = Tex("Limit: small vs national need, elite").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        b5_l3b = Tex("capture — complements the state, not replaces").scale(0.9).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l3))
        self.play(Write(b5_l3b))
        self.play(Create(SurroundingRectangle(b5_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the damage list
        self.next_band(6)
        b6_title = Tex("Development and the environment").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Acid mine drainage: Witwatersrand water").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("Coal power: Mpumalanga's polluted airshed").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Overgrazing: eroded soil silts the dams").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("Settlement over wetlands; Vaal sewage").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Top per-capita carbon emitter — coal").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the two truths and the tools
        self.next_band(7)
        b7_title = Tex("Two truths, one solution").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Damage is a LOAN against development,").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l1b = Tex("repaid with interest by the poor").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l1b))
        self.wait(2.5)
        b7_l2 = Tex("Poverty degrades too: fuelwood stripped,").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l2b = Tex("fragile range overstocked").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l2))
        self.play(Write(b7_l2b))
        self.wait(2.5)
        b7_l3 = Tex("SUSTAINABLE DEVELOPMENT: EIAs, mine").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        b7_l3b = Tex("rehabilitation, parks, renewables").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
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
        b8_l1 = Tex("Causes come pre-tangled: pull one wire,").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l1b = Tex("the knot tightens somewhere else").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l1b))
        self.wait(2.5)
        b8_l2 = Tex(r"Drought $\rightarrow$ herding, not school $\rightarrow$").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        b8_l2b = Tex(r"no matric $\rightarrow$ no job $\rightarrow$ raw wool sold").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        b8_l2c = Tex("cheap — the history wire under it all").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l2))
        self.play(Write(b8_l2b))
        self.play(Write(b8_l2c))
        self.wait(2.5)
        b8_l3 = Tex("Write the chain: INTERRELATED").scale(1.0).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the meeting on the stoep
        self.next_band(9)
        b9_title = Tex("The meeting on the stoep").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Far-off officials build; the pump rusts.").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("Chairs on a stoep: residents plan, build,").scale(0.95).shift(band_shift(9) + UP * 0.4)
        b9_l2b = Tex("own — people maintain what is THEIRS").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.play(Write(b9_l2b))
        self.play(Create(SurroundingRectangle(b9_l2b, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("Working for Water; wool pooled and").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        b9_l3b = Tex("graded; Khayelitsha's lit walkways").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l3))
        self.play(Write(b9_l3b))
        self.wait(2.5)
        b9_l4 = Tex("Community hands AND state muscle").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): borrowing from tomorrow's roof
        self.next_band(10)
        b10_title = Tex("Borrowing from tomorrow's roof").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Burn the roof beams to stay warm:").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l1b = Tex("warm tonight, soaked next summer").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.wait(2.5)
        b10_l2 = Tex("Acid mine water creeping to rivers;").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10_l2b = Tex("the bill lands on the poor first").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l2))
        self.play(Write(b10_l2b))
        self.wait(2.5)
        b10_l3 = Tex("Poverty strips the last woodland — the").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        b10_l3b = Tex("knot again; build without burning beams").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l3b))
        self.play(Create(SurroundingRectangle(b10_l3b, color=GREEN)))
        self.wait(4)
