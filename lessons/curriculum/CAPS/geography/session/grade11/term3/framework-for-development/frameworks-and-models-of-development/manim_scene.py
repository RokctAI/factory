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

# Band-layout whiteboard scene for the CAPS Grade 11 Geography session duo
# "Frameworks and Models of Development". One band per teaching beat; the
# camera moves down, nothing is removed. Diagrams (core-periphery rings,
# Rostow staircase) hand-built from Line/Arrow/Dot/Circle/Rectangle/Tex only.
# Subtopic shares follow subtopics.json: 220/235/235/225/190/195/205 of 1505 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DevelopmentFrameworksSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): aspects — economic, social
        title = Tex("Frameworks and Models of Development").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("Five aspects every full answer touches").scale(1.05).shift(UP * 1.1)
        self.play(Write(s0_l1))
        self.wait(2)
        s0_l2 = Tex("1 ECONOMIC: production, jobs, income —").scale(1.0).shift(UP * 0.2)
        s0_l2b = Tex("the engine room that funds the rest").scale(1.0).shift(DOWN * 0.6)
        self.play(Write(s0_l2))
        self.play(Write(s0_l2b))
        self.wait(2.5)
        s0_l3 = Tex("2 SOCIAL: money becoming education,").scale(1.0).shift(DOWN * 1.5)
        s0_l3b = Tex("health, housing, women's inclusion").scale(1.0).shift(DOWN * 2.3)
        self.play(Write(s0_l3))
        self.play(Write(s0_l3b))
        self.wait(3)

        # --- Band 1 (subtopic_1): sustainable, appropriate, spatial
        self.next_band(1)
        b1_title = Tex("Sustainable, appropriate, spatial").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("3 SUSTAINABLE (Brundtland): meet present").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l1b = Tex("needs WITHOUT compromising future").scale(0.95).shift(band_shift(1) + UP * 0.4)
        b1_l1c = Tex("generations' ability to meet theirs").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l1b))
        self.play(Write(b1_l1c))
        self.play(Create(SurroundingRectangle(VGroup(b1_l1b, b1_l1c), color=GREEN)))
        self.wait(3)
        b1_l2 = Tex("4 APPROPRIATE SCALE: solar and borehole").scale(0.95).shift(band_shift(1) + DOWN * 1.4)
        b1_l2b = Tex("for the Karoo village, not a power station").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l2))
        self.play(Write(b1_l2b))
        self.wait(2.5)
        b1_l3 = Tex("5 SPATIAL: WHERE — cores vs peripheries").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l3))
        self.wait(3)

        # --- Band 2 (subtopic_2): core-periphery drawn
        self.next_band(2)
        b2_title = Tex("The core-periphery model").scale(1.15).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_title))
        self.wait(1.5)
        core = Circle(radius=0.9, color=YELLOW).shift(band_shift(2) + LEFT * 2.6 + DOWN * 0.4)
        core_lab = Tex("CORE").scale(0.9).shift(band_shift(2) + LEFT * 2.6 + DOWN * 0.4)
        peri = Circle(radius=2.3, color=BLUE).shift(band_shift(2) + LEFT * 2.6 + DOWN * 0.4)
        peri_lab = Tex("PERIPHERY").scale(0.85).shift(band_shift(2) + LEFT * 2.6 + UP * 1.6)
        self.play(Create(peri), Write(peri_lab))
        self.play(Create(core), Write(core_lab))
        self.wait(2)
        back1 = Arrow(LEFT * 4.7 + DOWN * 0.4, LEFT * 3.6 + DOWN * 0.4, color=RED, buff=0).shift(band_shift(2))
        back2 = Arrow(LEFT * 2.6 + DOWN * 2.5, LEFT * 2.6 + DOWN * 1.4, color=RED, buff=0).shift(band_shift(2))
        back_lab = Tex("BACKWASH: skills, capital in").scale(0.85).shift(band_shift(2) + RIGHT * 2.9 + UP * 0.6)
        self.play(Create(back1), Create(back2), Write(back_lab))
        self.wait(2)
        spread = Arrow(LEFT * 1.6 + UP * 0.3, LEFT * 0.4 + UP * 1.0, color=GREEN, buff=0).shift(band_shift(2))
        spread_lab = Tex("SPREAD: remittances out").scale(0.85).shift(band_shift(2) + RIGHT * 2.9 + DOWN * 0.3)
        self.play(Create(spread), Write(spread_lab))
        self.wait(2)
        b2_l1 = Tex("Cumulative causation: success").scale(0.9).shift(band_shift(2) + RIGHT * 3.0 + DOWN * 1.3)
        b2_l1b = Tex("attracts success").scale(0.9).shift(band_shift(2) + RIGHT * 3.0 + DOWN * 2.0)
        self.play(Write(b2_l1))
        self.play(Write(b2_l1b))
        self.wait(2)
        b2_l2 = Tex("Planning: widen spread, narrow backwash").scale(0.9).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l2))
        self.wait(3)

        # --- Band 3 (subtopic_2): three scales
        self.next_band(3)
        b3_title = Tex("Run it at three scales").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Global: industrial North core; Africa,").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l1b = Tex("Asia, Latin America supplying periphery").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l1b))
        self.wait(2.5)
        b3_l2 = Tex(r"National: Gauteng $\approx \tfrac{1}{3}$ of GDP on the").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        b3_l2b = Tex("smallest footprint; Eastern Cape, Limpopo").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        b3_l2c = Tex("former homelands export their workers").scale(0.95).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l2))
        self.play(Write(b3_l2b))
        self.play(Write(b3_l2c))
        self.wait(2.5)
        b3_l3 = Tex("Local: office-tower core, township edge").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): Rostow's staircase drawn
        self.next_band(4)
        b4_title = Tex("Rostow's five stages").scale(1.15).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        # staircase: five steps rising left to right
        steps = VGroup(
            Line(LEFT * 6.0 + DOWN * 2.4, LEFT * 3.8 + DOWN * 2.4, color=WHITE),
            Line(LEFT * 3.8 + DOWN * 2.4, LEFT * 3.8 + DOWN * 1.5, color=WHITE),
            Line(LEFT * 3.8 + DOWN * 1.5, LEFT * 1.6 + DOWN * 1.5, color=WHITE),
            Line(LEFT * 1.6 + DOWN * 1.5, LEFT * 1.6 + DOWN * 0.6, color=WHITE),
            Line(LEFT * 1.6 + DOWN * 0.6, RIGHT * 0.6 + DOWN * 0.6, color=WHITE),
            Line(RIGHT * 0.6 + DOWN * 0.6, RIGHT * 0.6 + UP * 0.3, color=WHITE),
            Line(RIGHT * 0.6 + UP * 0.3, RIGHT * 2.8 + UP * 0.3, color=WHITE),
            Line(RIGHT * 2.8 + UP * 0.3, RIGHT * 2.8 + UP * 1.2, color=WHITE),
            Line(RIGHT * 2.8 + UP * 1.2, RIGHT * 5.4 + UP * 1.2, color=WHITE),
        ).shift(band_shift(4))
        for seg in steps:
            self.play(Create(seg), run_time=0.35)
        l1 = Tex("1 traditional").scale(0.7).shift(band_shift(4) + LEFT * 4.9 + DOWN * 2.9)
        l2 = Tex("2 preconditions").scale(0.7).shift(band_shift(4) + LEFT * 2.7 + DOWN * 2.0)
        l3 = Tex("3 TAKE-OFF").scale(0.7).shift(band_shift(4) + LEFT * 0.5 + DOWN * 1.1)
        l4 = Tex("4 maturity").scale(0.7).shift(band_shift(4) + RIGHT * 1.7 + DOWN * 0.2)
        l5 = Tex("5 mass consumption").scale(0.7).shift(band_shift(4) + RIGHT * 4.2 + UP * 0.7)
        self.play(Write(l1), Write(l2))
        self.play(Write(l3), Write(l4), Write(l5))
        self.wait(2.5)
        b4_l1 = Tex(r"Take-off: investment $>10\%$ of income,").scale(0.95).shift(band_shift(4) + UP * 1.9 + LEFT * 1.6)
        b4_l1b = Tex("growth becomes self-sustaining").scale(0.95).shift(band_shift(4) + DOWN * 3.1 + RIGHT * 1.0)
        self.play(Write(b4_l1))
        self.play(Write(b4_l1b))
        self.wait(3)

        # --- Band 5 (subtopic_3): the criticisms
        self.next_band(5)
        b5_title = Tex("Criticising Rostow — for marks").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Assumes one Western path for all").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("Ignores colonialism: the ladder was").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l2b = Tex("pulled up behind the climbers").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.play(Write(b5_l2b))
        self.wait(2.5)
        b5_l3 = Tex("Ignores the core-periphery trap: raw").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        b5_l3b = Tex("exporters never accumulate the capital").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l3))
        self.play(Write(b5_l3b))
        self.wait(2.5)
        b5_l4 = Tex("No stage for sustainability at the top").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): South Africa through Rostow
        self.next_band(6)
        b6_title = Tex("South Africa on the staircase").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Preconditions: mineral revolution —").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l1b = Tex("railways and ports after 1870").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l1b))
        self.wait(2.5)
        b6_l2 = Tex("Take-off: manufacturing, 1930s--1960s;").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6_l2b = Tex("today: maturity features, dominant services").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l2))
        self.play(Write(b6_l2b))
        self.wait(2.5)
        b6_l3 = Tex("One country refuses one step: apartheid").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        b6_l3b = Tex("held millions off the staircase entirely").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l3))
        self.play(Write(b6_l3b))
        self.wait(3)

        # --- Band 7 (subtopic_4): apartheid geography and the synthesis
        self.next_band(7)
        b7_title = Tex("The map Rostow cannot draw").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Apartheid: core-periphery by law —").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l1b = Tex("homelands as labour reservoirs feeding").scale(0.95).shift(band_shift(7) + UP * 0.4)
        b7_l1c = Tex("backwash to the mining core").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l1b))
        self.play(Write(b7_l1c))
        self.wait(2.5)
        b7_l2 = Tex("Post-1994: SDIs, Coega and Richards Bay").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        b7_l2b = Tex("zones, Maputo corridor — new magnets").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l2))
        self.play(Write(b7_l2b))
        self.wait(2.5)
        b7_l3 = Tex("Rostow: the TIMELINE; core-periphery: the MAP").scale(0.9).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): five inspectors
        self.next_band(8)
        b8_title = Tex("Five boxes every plan must tick").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Wallet: is the economy producing?").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("People: is money becoming clinics, taps?").scale(0.95).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("Tomorrow: no burning the roof beams —").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        b8_l3b = Tex("Brundtland's sentence, word for word").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.play(Write(b8_l3b))
        self.wait(2.5)
        b8_l4 = Tex("Fit: solar the village can repair, not").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        b8_l4b = Tex("a monument; Map: everywhere, not one corner").scale(0.9).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l4))
        self.play(Write(b8_l4b))
        self.wait(3)

        # --- Band 9 (subtopic_6): the magnet and the empty edges
        self.next_band(9)
        b9_title = Tex("The magnet and the empty edges").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Magnet $=$ core; filings slide inward —").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l1b = Tex("January buses from the Eastern Cape").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l1b))
        self.wait(2.5)
        b9_l2 = Tex("Backwash in; spread trickles home;").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        b9_l2b = Tex("planning is plumbing — Coega bolts a").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        b9_l2c = Tex("new magnet onto the periphery").scale(1.0).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l2))
        self.play(Write(b9_l2b))
        self.play(Write(b9_l2c))
        self.wait(2.5)
        b9_l3 = Tex("Three zoom levels, one model, nine marks").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the aeroplane on the runway
        self.next_band(10)
        b10_title = Tex("The aeroplane on the runway").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Parked, ground crew, TAKE-OFF ($>10\\%$").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l1b = Tex("invested), climb-out, cruising altitude").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.wait(2.5)
        b10_l2 = Tex("Criticisms: one runway for all; fuel").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10_l2b = Tex("siphoned from colonies; some held at the").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        b10_l2c = Tex("gate; destination is a shopping mall").scale(0.95).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(b10_l2))
        self.play(Write(b10_l2b))
        self.play(Write(b10_l2c))
        self.wait(2.5)
        b10_l3 = Tex("No stage for apartheid — say it, score it").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(4)
