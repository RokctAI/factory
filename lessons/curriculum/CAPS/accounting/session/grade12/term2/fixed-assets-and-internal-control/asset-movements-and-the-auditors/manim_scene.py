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

# Band-layout whiteboard scene for the CAPS grade 12 accounting session duo
# "Asset Movements and the Auditors". One band per teaching beat; the camera
# moves down to fresh space and earlier work stays on the canvas. Only
# exporter-safe mobjects (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/
# SurroundingRectangle/VGroup) and write-only reveals — no Transform, no
# FadeOut, no sub-part indexing on MathTex.
#
# Subtopic time shares (subtopics.json, total 1540 s):
# 235/235/240/220 expert, 195/205/210 simplifier.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AssetMovementsAndAuditorsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the fixed asset note as a reconciliation ---
        title = Tex("Asset Movements and the Auditors").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_head = Tex("Fixed asset note — Bathini Deliveries: vehicles").scale(1.1).shift(UP * 1.4)
        self.play(Write(b0_head))
        self.wait(2)
        b0_l1 = Tex(r"Opening carrying value: \quad R840\,000").scale(1.1).shift(UP * 0.5)
        b0_l2 = Tex(r"(cost R1\,400\,000 $-$ acc.\ depr.\ R560\,000)").scale(1.0).shift(DOWN * 0.3)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex(r"$+$ Additions at COST: \quad R400\,000").scale(1.1).shift(DOWN * 1.2)
        b0_l4 = Tex(r"$-$ Disposal at CARRYING VALUE: \quad R60\,000").scale(1.1).shift(DOWN * 2.0)
        b0_l5 = Tex(r"$-$ Depreciation for the year: \quad R230\,000").scale(1.1).shift(DOWN * 2.8)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): closing value + two-column verification ---
        self.next_band(1)
        b1_title = Tex("Close the note, then verify it").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"840\,000 + 400\,000 - 60\,000 - 230\,000").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex(r"Closing carrying value $=$ R950\,000").scale(1.15).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex(r"Cost: $1\,400\,000 + 400\,000 - 200\,000 = $ R1\,600\,000").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = Tex(r"Acc.\ depr.: $560\,000 + 230\,000 - 140\,000 = $ R650\,000").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        b1_l5 = Tex(r"Check: $1\,600\,000 - 650\,000 = $ R950\,000").scale(1.05).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.wait(2.5)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_1): cost vs carrying value discipline + loss ---
        self.next_band(2)
        b2_title = Tex("The discipline point").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_wrong = Tex(r"Disposal recorded at cost R200\,000 in the note").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l1 = Tex("Additions enter at COST").scale(1.1).shift(band_shift(2) + UP * 0.1)
        b2_l2 = Tex("Disposals leave at CARRYING VALUE").scale(1.1).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"Sold for R48\,000, carrying value R60\,000:").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        b2_l4 = Tex(r"Loss on disposal R12\,000 $\rightarrow$ income statement").scale(1.05).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): age and remaining lifespan ---
        self.next_band(3)
        b3_title = Tex("How old are the assets?").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Equipment: cost R900\,000, 10\% straight line").scale(1.05).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"Annual depreciation $=$ R90\,000 (10-year life)").scale(1.05).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"\text{Age} = \frac{\text{acc. depreciation}}{\text{annual charge}}").scale(0.96).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = MathTex(r"\frac{630\,000}{90\,000} = 7 \text{ years used}").scale(1.1).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = Tex(r"$10 - 7 = 3$ years remain $\rightarrow$ plan replacement NOW").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l3))
        self.wait(2.5)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_2): replacing fast enough + limits ---
        self.next_band(4)
        b4_title = Tex("Replacing fast enough?").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Additions R400\,000 vs depreciation R230\,000").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"Additions $>$ depreciation $\Rightarrow$ fleet renewed").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex(r"Depreciation outrunning additions $=$").scale(1.05).shift(band_shift(4) + DOWN * 0.8)
        b4_l4 = Tex("a business eating its own capacity").scale(1.05).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex("Limits: class averages; fully depreciated assets").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): audit evidence ---
        self.next_band(5)
        b5_title = Tex("Internal audit: the evidence").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Physical inspection — find the vehicle in the yard").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("Documentation — invoices, licences, logbooks").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("Observation — watch the process actually run").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("Enquiry and confirmation; recalculation").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_weak = Tex("Weakest evidence: a manager's verbal assurance").scale(1.0).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_weak))
        self.play(Create(strike(b5_weak)))
        self.wait(3)

        # --- Band 6 (subtopic_3): sampling + the audit report ---
        self.next_band(6)
        b6_title = Tex("Sampling, then the report").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Random — every item an equal chance").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("Systematic — every tenth item from the register").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Stratified — weight the sample toward risk").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex(r"Report: scope $\rightarrow$ finding $\rightarrow$ risk $\rightarrow$ recommendation").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        b6_l5 = Tex(r"Fuel without logbooks $\rightarrow$ fuel cards, monthly check").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): internal vs external auditor ---
        self.next_band(7)
        b7_title = Tex("Internal vs external auditor").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        mid7 = Line(band_shift(7) + UP * 1.6, band_shift(7) + DOWN * 1.6, stroke_width=3)
        self.play(Create(mid7))
        b7_ih = Tex("INTERNAL").scale(1.05).shift(band_shift(7) + UP * 1.3 + LEFT * 3.2)
        b7_eh = Tex("EXTERNAL").scale(1.05).shift(band_shift(7) + UP * 1.3 + RIGHT * 3.2)
        self.play(Write(b7_ih), Write(b7_eh))
        self.wait(1.5)
        b7_i1 = Tex("Employee").scale(0.95).shift(band_shift(7) + UP * 0.6 + LEFT * 3.2)
        b7_e1 = Tex("Independent").scale(0.95).shift(band_shift(7) + UP * 0.6 + RIGHT * 3.2)
        self.play(Write(b7_i1), Write(b7_e1))
        self.wait(2)
        b7_i2 = Tex("Reports to management").scale(0.9).shift(band_shift(7) + LEFT * 3.2)
        b7_e2 = Tex("Reports to shareholders").scale(0.9).shift(band_shift(7) + RIGHT * 3.2)
        self.play(Write(b7_i2), Write(b7_e2))
        self.wait(2)
        b7_i3 = Tex("All year, all controls").scale(0.9).shift(band_shift(7) + DOWN * 0.6 + LEFT * 3.2)
        b7_e3 = Tex("Year-end, the AFS").scale(0.9).shift(band_shift(7) + DOWN * 0.6 + RIGHT * 3.2)
        self.play(Write(b7_i3), Write(b7_e3))
        self.wait(2)
        b7_i4 = Tex("Improve controls").scale(0.9).shift(band_shift(7) + DOWN * 1.2 + LEFT * 3.2)
        b7_e4 = Tex("Audit opinion").scale(0.9).shift(band_shift(7) + DOWN * 1.2 + RIGHT * 3.2)
        self.play(Write(b7_i4), Write(b7_e4))
        self.wait(2)
        b7_l5 = Tex("Three layers: controls, internal audit, external audit").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the taxi owner's five beats ---
        self.next_band(8)
        b8_title = Tex("The taxi owner's note: five beats").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Begin: books carry R840\,000").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"Buy: $+$R400\,000 (at what they COST)").scale(1.05).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex(r"Sell: $-$R60\,000 (at what the books CARRIED)").scale(1.05).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex(r"Wear: $-$R230\,000 depreciation").scale(1.05).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex(r"End: $840 + 400 - 60 - 230 = $ R950\,000").scale(1.05).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        b8_l6 = Tex("Hidden beat? Rebuild it from the other four").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): how old is the fleet, really? ---
        self.next_band(9)
        b9_title = Tex("How old is the fleet, really?").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Equipment R900\,000, wears R90\,000 a year").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"\frac{630\,000 \text{ worn}}{90\,000 \text{ a year}} = 7 \text{ years old}").scale(0.86).shift(band_shift(9) + UP * 0.0)
        b9_l3 = Tex("Ten-year life, seven used: 3-year countdown").scale(1.05).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex(r"Health check: added R400\,000 $>$ wore R230\,000").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        b9_l5 = Tex("The fleet is getting younger — but check averages").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the inside checker and the outside referee ---
        self.next_band(10)
        b10_title = Tex("The inside checker, the outside referee").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Lindiwe samples: hat draws, every fifth taxi,").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("and always the expensive ones — risk first").scale(1.0).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Evidence ranked: look, read, watch, ask, recalc").scale(1.0).shift(band_shift(10) + DOWN * 0.3)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"Report in three moves: gap $\rightarrow$ rands $\rightarrow$ fix").scale(1.0).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex("She reports; the owner acts — management answers").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        b10_l6 = Tex("Referee: chosen by the money, rules once a year").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l5))
        self.wait(2)
        self.play(Write(b10_l6))
        self.wait(4)
