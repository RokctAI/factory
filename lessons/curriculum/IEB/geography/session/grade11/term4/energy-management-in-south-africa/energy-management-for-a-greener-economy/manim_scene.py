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

# Band-layout whiteboard scene for the IEB session "Energy Management for a
# Greener Economy" (grade 11, term 4). Seven subtopics of the duo: Part 1
# Expert (subtopics 1-4), Part 2 Simplifier (subtopics 5-7). Band time
# apportioned to subtopics.json (225/235/230/230/190/200/205 of 1515 s).
# Exporter-safe primitives only; diagrams (leaking bucket, spanner table,
# stadium wave dots) hand-built from Line/Arrow/Dot/Rectangle/Tex.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class EnergyManagementGreenerEconomySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the three pressures
        title = Tex("Energy Management for a Greener Economy").scale(1.05).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Energy-hungry economy; 8 units in 10 from coal").scale(0.95).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex(r"1. Supply: demand can outrun the system").scale(0.95).shift(UP * 0.4)
        b0_l3 = Tex(r"2. Climate + trade: carbon border taxes loom").scale(0.95).shift(DOWN * 0.4)
        b0_l4 = Tex(r"3. Equity: wasted energy is development lost").scale(0.95).shift(DOWN * 1.2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex(r"Fastest fix: manage demand, not new stations").scale(0.95).shift(DOWN * 2.2)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the concept pair and the master idea
        self.next_band(1)
        b1_title = Tex("The concept pair").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Greener economy: growth up, emissions down").scale(0.95).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"Sustainable lifestyle: habits all could copy").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex(r"Master idea: EFFICIENCY —").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex(r"same service from fewer units").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex(r"The invisible power station:").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        b1_l6 = Tex(r"the unit never used is cheapest and cleanest").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): government — planning, pricing
        self.next_band(2)
        b2_title = Tex("Government: planning and pricing").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"IRP: the electricity roadmap — what retires,").scale(0.95).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex(r"what gets built, by which year").scale(0.95).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex(r"Auctions procure wind and solar plants").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex(r"Unbundling: independent grid, fair competition").scale(0.9).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex(r"Carbon tax: pay per tonne of CO$_2$ —").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        b2_l6 = Tex(r"pollution finally carries a price").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): rules, delivery, example
        self.next_band(3)
        b3_title = Tex("Government: rules, delivery, example").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Building rules: efficient from birth").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"Appliance labels: the fridge's appetite shown").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex(r"Millions of subsidised solar water heaters").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex(r"Just transition: billions for grid, retraining,").scale(0.95).shift(band_shift(3) + DOWN * 1.4)
        b3_l5 = Tex(r"green industry — coal towns caught, not dropped").scale(0.9).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(2.5)
        b3_l6 = Tex(r"Biggest landlord: state retrofits move markets").scale(0.9).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): business — audits and self-generation
        self.next_band(4)
        b4_title = Tex("Business: audits and rooftops").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Energy audit: meter where the joules go —").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"air leaks, tired motors, bare hot pipes").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Fixes ranked by payback: double-digit savings").scale(0.9).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex(r"Self-generation: PV on malls, farms, mines;").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        b4_l5 = Tex(r"private wind farms of hundreds of MW").scale(0.95).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2.5)
        b4_l6 = Tex(r"Wheeling: generate there, consume here").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): market access and greenwashing
        self.next_band(5)
        b5_title = Tex("Market access and honesty").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Carbon footprint: emissions baked into a product").scale(0.9).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex(r"Border rules tax it; banks screen for it;").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex(r"clean energy $=$ passport to markets").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex(r"Sustainability: from ethics to strategy").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex(r"No greenwashing: baseline, target,").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        b5_l6 = Tex(r"audit, published result — or nothing").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): individuals — the geyser ladder and the wins
        self.next_band(6)
        b6_title = Tex("Individuals: the geyser ladder").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Geyser $\approx$ 40\% of the bill:").scale(0.95).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(1.5)
        b6_l2 = Tex(r"60 $^\circ$C $\to$ blanket $\to$ timer $\to$ solar/heat pump").scale(0.9).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex(r"LED: same light, a tenth of the power").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex(r"Lids on pots; microwave small jobs; full loads").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        b6_l5 = Tex(r"Winter: seal draughts, warm the person").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex(r"Standby off at the wall; share the lift, walk").scale(0.9).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): the citizen layer and the honest close
        self.next_band(7)
        b7_title = Tex("The citizen above the consumer").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Shift chores off the 6 pm peak: helps the grid").scale(0.9).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex(r"Rooftop PV: the home as micro power station").scale(0.9).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"Voice: support the lines, plants and plans —").scale(0.9).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex(r"infrastructure follows public acceptance").scale(0.9).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex(r"Honest close: one home cannot decarbonise").scale(0.9).shift(band_shift(7) + DOWN * 2.2)
        b7_l6 = Tex(r"a grid — but the peak IS the sum of homes").scale(0.9).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the leaking bucket
        self.next_band(8)
        b8_title = Tex("The leaking bucket").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        # Bucket drawn from lines, with leak arrows.
        bl = Line(band_shift(8) + UP * 1.0 + LEFT * 1.5, band_shift(8) + DOWN * 1.0 + LEFT * 1.1)
        br = Line(band_shift(8) + UP * 1.0 + RIGHT * 1.5, band_shift(8) + DOWN * 1.0 + RIGHT * 1.1)
        bb = Line(band_shift(8) + DOWN * 1.0 + LEFT * 1.1, band_shift(8) + DOWN * 1.0 + RIGHT * 1.1)
        self.play(Create(bl), Create(br), Create(bb))
        self.wait(1.5)
        pour = Arrow(band_shift(8) + UP * 2.0, band_shift(8) + UP * 1.1, color=BLUE)
        self.play(Create(pour))
        leak1 = Arrow(band_shift(8) + DOWN * 0.2 + LEFT * 1.3, band_shift(8) + DOWN * 0.6 + LEFT * 2.4, color=YELLOW)
        leak2 = Arrow(band_shift(8) + DOWN * 0.5 + RIGHT * 1.3, band_shift(8) + DOWN * 0.9 + RIGHT * 2.4, color=YELLOW)
        self.play(Create(leak1), Create(leak2))
        self.wait(2)
        b8_l1 = Tex(r"Holes: draughts, old bulbs, naked geysers,").scale(0.9).shift(band_shift(8) + DOWN * 1.7)
        b8_l2 = Tex(r"tired motors, offices lit for nobody").scale(0.9).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Plugging holes beats building dams:").scale(0.95).shift(band_shift(8) + DOWN * 3.2)
        b8_l4 = Tex(r"the unit never used is cheapest and cleanest").scale(0.9).shift(band_shift(8) + DOWN * 3.9)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the toolbox with three spanners
        self.next_band(9)
        b9_title = Tex("The toolbox with three spanners").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"GOVERNMENT: rules of the game —").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex(r"IRP, auctions, carbon tax, labels, transition").scale(0.9).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex(r"BUSINESS: audit the waste, fill the roofs,").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex(r"answer the smoke question at the border").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex(r"INDIVIDUALS: smallest spanner,").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        b9_l6 = Tex(r"sixty million copies in circulation").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the stadium wave
        self.next_band(10)
        b10_title = Tex("The stadium wave").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        # A row of dots lifting like a wave.
        dots = [Dot(band_shift(10) + UP * 1.2 + LEFT * 3.0 + RIGHT * 0.75 * i) for i in range(9)]
        for d in dots:
            self.play(Create(d), run_time=0.2)
        self.wait(1.5)
        b10_l1 = Tex(r"The 6 pm peak $=$ millions of private choices").scale(0.9).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex(r"Plays by size: geyser first — 40\% of the bill;").scale(0.9).shift(band_shift(10) + DOWN * 0.4)
        b10_l3 = Tex(r"then LEDs, kitchen, winter seals, standby, wheels").scale(0.85).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"Beyond the meter: off-peak shifts, rooftop PV,").scale(0.9).shift(band_shift(10) + DOWN * 2.1)
        b10_l5 = Tex(r"a citizen's voice for the transition").scale(0.9).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex(r"Rules $+$ big bolts $+$ the wave $=$ greener economy").scale(0.9).shift(band_shift(10) + DOWN * 3.7)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
