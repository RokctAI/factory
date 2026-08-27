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
# "Frameworks and Models of Development". One band per teaching beat; the
# camera moves down, nothing is removed. Text-led with primitive accents.
# Subtopic shares follow subtopics.json: 220/235/235/225/190/195/205 of 1505 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DevelopmentFrameworksIEBSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): aspects — economic, social
        title = Tex("Frameworks and Models of Development").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("ECONOMIC: the engine room —").scale(1.0).shift(UP * 1.1)
        s0_l1b = Tex("production, jobs, income, investment").scale(1.0).shift(UP * 0.3)
        self.play(Write(s0_l1))
        self.play(Write(s0_l1b))
        self.wait(2.5)
        s0_l2 = Tex("SOCIAL: the conversion step —").scale(1.0).shift(DOWN * 0.7)
        s0_l2b = Tex("schools, clinics, water, women included").scale(1.0).shift(DOWN * 1.5)
        self.play(Write(s0_l2))
        self.play(Write(s0_l2b))
        self.wait(2.5)
        s0_l3 = Tex("Necessary engine, insufficient alone").scale(1.0).shift(DOWN * 2.5)
        self.play(Write(s0_l3))
        self.play(Create(SurroundingRectangle(s0_l3, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): sustainable, appropriate, spatial
        self.next_band(1)
        b1_title = Tex("Three more aspects").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("SUSTAINABLE (Brundtland): meet today's").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l1b = Tex("needs without compromising tomorrow's").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l1b))
        self.play(Create(SurroundingRectangle(b1_l1b, color=GREEN)))
        self.wait(2.5)
        b1_l2 = Tex("APPROPRIATE SCALE: village solar and").scale(0.95).shift(band_shift(1) + DOWN * 0.6)
        b1_l2b = Tex("rain tanks, not an unrepairable plant").scale(0.95).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_l2))
        self.play(Write(b1_l2b))
        self.wait(2.5)
        b1_l3 = Tex("SPATIAL: WHERE? — cores boom,").scale(0.95).shift(band_shift(1) + DOWN * 2.3)
        b1_l3b = Tex("peripheries wait").scale(0.95).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l3))
        self.play(Write(b1_l3b))
        self.wait(3)

        # --- Band 2 (subtopic_2): core-periphery drawn
        self.next_band(2)
        b2_title = Tex("The core-periphery model").scale(1.15).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_title))
        self.wait(1.5)
        core = Circle(radius=0.9, color=YELLOW).shift(band_shift(2) + UP * 0.6)
        core_lab = Tex("CORE").scale(0.8).shift(band_shift(2) + UP * 0.6)
        ring = Circle(radius=2.6, color=BLUE).shift(band_shift(2) + UP * 0.6)
        per_lab = Tex("PERIPHERY").scale(0.8).shift(band_shift(2) + UP * 0.6 + RIGHT * 3.6)
        self.play(Create(core), Write(core_lab))
        self.play(Create(ring), Write(per_lab))
        self.wait(2)
        arr_in = Line(LEFT * 2.4 + UP * 0.6, LEFT * 1.0 + UP * 0.6, color=RED).shift(band_shift(2))
        bw_lab = Tex("backwash: people, savings").scale(0.75).shift(band_shift(2) + LEFT * 3.4 + DOWN * 0.4)
        self.play(Create(arr_in), Write(bw_lab))
        self.wait(2)
        arr_out = Line(RIGHT * 1.0 + DOWN * 0.6, RIGHT * 2.4 + DOWN * 0.6, color=GREEN).shift(band_shift(2))
        sp_lab = Tex("spread: remittances, investment").scale(0.75).shift(band_shift(2) + RIGHT * 3.2 + DOWN * 1.4)
        self.play(Create(arr_out), Write(sp_lab))
        self.wait(2)
        b2_l1 = Tex("Cumulative causation: success recruits").scale(0.9).shift(band_shift(2) + DOWN * 2.3)
        b2_l1b = Tex("success — the magnet strengthens").scale(0.9).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_l1))
        self.play(Write(b2_l1b))
        self.wait(3)

        # --- Band 3 (subtopic_2): three scales
        self.next_band(3)
        b3_title = Tex("One model, three scales").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Global: industrial North core;").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l1b = Tex("minerals and crops flow inward").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l1b))
        self.wait(2.5)
        b3_l2 = Tex(r"National: Gauteng $\approx \frac{1}{3}$ of GDP,").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        b3_l2b = Tex("smallest province; homeland edges").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l2))
        self.play(Write(b3_l2b))
        self.play(Create(SurroundingRectangle(b3_l2b, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Local: office-tower core, township rim,").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        b3_l3b = Tex("the long taxi ride between").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l3))
        self.play(Write(b3_l3b))
        self.wait(3)

        # --- Band 4 (subtopic_3): Rostow's staircase drawn
        self.next_band(4)
        b4_title = Tex("Rostow's staircase").scale(1.15).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        steps = [
            ("1 Traditional", LEFT * 5.0 + DOWN * 2.0),
            ("2 Preconditions", LEFT * 2.6 + DOWN * 1.2),
            ("3 Take-off", LEFT * 0.2 + DOWN * 0.4),
            ("4 Maturity", RIGHT * 2.2 + UP * 0.4),
            ("5 Consumption", RIGHT * 4.6 + UP * 1.2),
        ]
        prev = None
        for label, pos in steps:
            t = Tex(label).scale(0.8).shift(band_shift(4) + pos)
            self.play(Write(t), run_time=0.7)
            if prev is not None:
                self.play(Create(Line(prev + RIGHT * 0.9, pos + LEFT * 1.1,
                                      color=YELLOW).shift(band_shift(4))), run_time=0.4)
            prev = pos
            self.wait(0.8)
        b4_l1 = Tex(r"Take-off: investment $>10\%$ of income,").scale(0.9).shift(band_shift(4) + DOWN * 2.9)
        b4_l1b = Tex("growth feeds itself").scale(0.9).shift(band_shift(4) + DOWN * 3.6)
        self.play(Write(b4_l1))
        self.play(Write(b4_l1b))
        self.play(Create(SurroundingRectangle(b4_l1b, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the criticisms
        self.next_band(5)
        b5_title = Tex("Criticising Rostow").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("One Western path assumed for all").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("Colonialism ignored: ladders pulled up").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Periphery trap: raw exporters never").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l3b = Tex("bank the take-off fuel").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l3))
        self.play(Write(b5_l3b))
        self.wait(2)
        b5_l4 = Tex("Summit is a shopping mall —").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        b5_l4b = Tex("no stage for sustainability").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l4))
        self.play(Write(b5_l4b))
        self.play(Create(SurroundingRectangle(b5_l4b, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): South Africa through Rostow
        self.next_band(6)
        b6_title = Tex("South Africa on the staircase").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Preconditions: rails and harbours after").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l1b = Tex("1870, serving diamonds and gold").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l1b))
        self.wait(2.5)
        b6_l2 = Tex("Take-off 1930s--1960s behind tariffs;").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6_l2b = Tex("today: maturity features, split consumption").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l2))
        self.play(Write(b6_l2b))
        self.wait(2.5)
        b6_l3 = Tex("One country, several steps at once —").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        b6_l3b = Tex("no stage model has a stage for apartheid").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l3))
        self.play(Write(b6_l3b))
        self.play(Create(SurroundingRectangle(b6_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): apartheid geography and the synthesis
        self.next_band(7)
        b7_title = Tex("The map Rostow cannot draw").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Apartheid: core-periphery by law —").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l1b = Tex("homelands as labour reservoirs").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l1b))
        self.wait(2.5)
        b7_l2 = Tex("Answer since 1994: new magnets —").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l2b = Tex("Saldanha, Richards Bay, Lubombo corridor").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l2))
        self.play(Write(b7_l2b))
        self.wait(2.5)
        b7_l3 = Tex("Rostow: the TIMELINE; core-periphery:").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        b7_l3b = Tex("the MAP — use each, criticise both").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l3))
        self.play(Write(b7_l3b))
        self.play(Create(SurroundingRectangle(b7_l3b, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): five stamps
        self.next_band(8)
        b8_title = Tex("Five boxes every plan must tick").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Wallet — is the economy producing?").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("People — money becoming clinics, taps?").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.wait(1.5)
        self.play(Write(b8_l2))
        self.wait(1.5)
        b8_l3 = Tex("Tomorrow — Brundtland, word for word").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("Fit — right size: solar and rain tanks,").scale(0.95).shift(band_shift(8) + DOWN * 1.4)
        b8_l4b = Tex("not a monument nobody can repair").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        b8_l5 = Tex("Map — everywhere, or one rich corner?").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l4))
        self.play(Write(b8_l4b))
        self.wait(1.5)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the magnet and the empty edges
        self.next_band(9)
        b9_title = Tex("The magnet and the empty edges").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        mag = Circle(radius=0.7, color=YELLOW).shift(band_shift(9) + UP * 0.8)
        mag_lab = Tex("core").scale(0.7).shift(band_shift(9) + UP * 0.8)
        self.play(Create(mag), Write(mag_lab))
        d1 = Dot(LEFT * 4.0 + UP * 0.8, color=BLUE).shift(band_shift(9))
        d2 = Dot(RIGHT * 4.0 + UP * 1.4, color=BLUE).shift(band_shift(9))
        d3 = Dot(RIGHT * 3.4 + DOWN * 0.2, color=BLUE).shift(band_shift(9))
        a1 = Line(LEFT * 4.0 + UP * 0.8, LEFT * 0.9 + UP * 0.8, color=RED).shift(band_shift(9))
        self.play(Create(d1), Create(d2), Create(d3))
        self.play(Create(a1))
        self.wait(2)
        b9_l1 = Tex("Filings crawl inward: BACKWASH —").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        b9_l1b = Tex("buses from the villages every January").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l1))
        self.play(Write(b9_l1b))
        self.wait(2)
        b9_l2 = Tex("Spread flows back: remittances, branch").scale(0.9).shift(band_shift(9) + DOWN * 2.8)
        b9_l2b = Tex("plants — planning is plumbing").scale(0.9).shift(band_shift(9) + DOWN * 3.6)
        self.play(Write(b9_l2))
        self.play(Write(b9_l2b))
        self.play(Create(SurroundingRectangle(b9_l2b, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the aeroplane on the runway
        self.next_band(10)
        b10_title = Tex("The aeroplane on the runway").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Parked: traditional. Ground crew:").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l1b = Tex("preconditions — rails, harbours, banks").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.wait(2.5)
        b10_l2 = Tex(r"TAKE-OFF: investment $>10\%$, lift feeds").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10_l2b = Tex("lift; climb to maturity; cruise: consumption").scale(0.9).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l2))
        self.play(Write(b10_l2b))
        self.wait(2.5)
        b10_l3 = Tex("Criticise: one runway, siphoned tanks,").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        b10_l3b = Tex("gates held shut, mall as destination").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l3b))
        self.play(Create(SurroundingRectangle(b10_l3b, color=GREEN)))
        self.wait(4)
