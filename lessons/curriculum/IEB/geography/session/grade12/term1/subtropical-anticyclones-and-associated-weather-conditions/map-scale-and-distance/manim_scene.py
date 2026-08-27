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

# Band-layout whiteboard scene for "Map Scale and Distance" (grade 12,
# term 1). All seven subtopics: Part 1 Expert (1-4), Part 2 Simplifier (5-7).
# Band time apportioned to subtopics.json (230/220/210/260/200/180/190 of
# 1490 s). Exporter-safe primitives only; the ruler, the ladder and the
# worked lines are hand-built from Line/Dot/Tex, element by element.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MapScaleDistanceSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): what 1:50 000 means
        title = Tex("Map Scale and Distance").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"1:50 000 — one unit of paper $=$").scale(1.0).shift(UP * 1.3)
        b0_l2 = Tex(r"fifty thousand of the SAME units of ground").scale(0.95).shift(UP * 0.6)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"The ratio is unit-free: cm in, cm out").scale(0.95).shift(DOWN * 0.3)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex(r"Feel it: 50 000 cm $=$ 500 m $=$ half a km").scale(0.95).shift(DOWN * 1.2)
        b0_l5 = Tex(r"1 cm $=$ 0,5 km; \quad 2 cm $=$ 1 km").scale(1.0).shift(DOWN * 2.0)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(2.5)
        b0_l6 = Tex(r"A 30 cm ruler spans 15 km of country").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): three costumes, large vs small scale
        self.next_band(1)
        b1_title = Tex("Three costumes, one scale").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Words: ``1 cm represents half a km''").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"Ratio: 1:50 000 (the one we calculate with)").scale(0.95).shift(band_shift(1) + UP * 0.5)
        b1_l3 = Tex(r"Linear bar: step distances off, no arithmetic").scale(0.95).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2.5)
        # Linear scale bar sketch.
        bar = Line(band_shift(1) + DOWN * 1.2 + LEFT * 3.0, band_shift(1) + DOWN * 1.2 + RIGHT * 3.0)
        t0 = Line(band_shift(1) + DOWN * 1.05 + LEFT * 3.0, band_shift(1) + DOWN * 1.35 + LEFT * 3.0)
        t1 = Line(band_shift(1) + DOWN * 1.05 + LEFT * 1.0, band_shift(1) + DOWN * 1.35 + LEFT * 1.0)
        t2 = Line(band_shift(1) + DOWN * 1.05 + RIGHT * 1.0, band_shift(1) + DOWN * 1.35 + RIGHT * 1.0)
        t3 = Line(band_shift(1) + DOWN * 1.05 + RIGHT * 3.0, band_shift(1) + DOWN * 1.35 + RIGHT * 3.0)
        bar_lab = Tex(r"0 \quad 1 \quad 2 \quad 3 km").scale(0.8).shift(band_shift(1) + DOWN * 1.8)
        self.play(Create(bar), Create(t0), Create(t1), Create(t2), Create(t3), Write(bar_lab))
        self.wait(2.5)
        b1_l4 = Tex(r"1:10 000 is the LARGER scale —").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        b1_l5 = Tex(r"bigger fraction, smaller area, more detail").scale(0.95).shift(band_shift(1) + DOWN * 3.4)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the straight-line calculation, in full
        self.next_band(2)
        b2_title = Tex("The worked calculation").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Measured: 7,4 cm point-centre to point-centre").scale(0.9).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"Real distance $=$ map distance $\times$ 50 000").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"$7{,}4 \times 50\,000 = 370\,000$ cm").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex(r"($7 \times 50\,000 = 350\,000$; $0{,}4 \times 50\,000 = 20\,000$)").scale(0.8).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = Tex(r"$\div$ 100 $\to$ 3 700 m; \quad $\div$ 1 000 $\to$ 3,7 km").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l5))
        self.wait(2)
        b2_l6 = Tex(r"Answer: 3,7 kilometres — unit stated").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the shortcut and measuring care
        self.next_band(3)
        b3_title = Tex("Shortcut and precision").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"On 1:50 000 only: halve the centimetres —").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"half of 7,4 is 3,7. Use it to CHECK").scale(0.95).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex(r"Write the full ladder in your working:").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = Tex(r"the steps carry the marks").scale(0.95).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex(r"Measure to the nearest millimetre:").scale(0.95).shift(band_shift(3) + DOWN * 2.0)
        b3_l6 = Tex(r"1 mm of slack $=$ 50 m of ground error").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): curved routes and other scales
        self.next_band(4)
        b4_title = Tex("Curves, other sheets, reverse").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"String technique: press along the bends,").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"straighten, read: 11,8 cm $\to$ 5,9 km").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Orthophoto 1:10 000: $7{,}4 \times 10\,000$").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex(r"$= 74\,000$ cm $=$ 740 m $=$ 0,74 km").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex(r"Reverse: 3,7 km $= 370\,000$ cm;").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        b4_l6 = Tex(r"$\div\ 50\,000 = 7{,}4$ cm on the sheet").scale(0.95).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(2)
        b4_l7 = Tex(r"Map $\to$ ground: multiply; ground $\to$ map: divide").scale(0.9).shift(band_shift(4) + DOWN * 3.5)
        self.play(Write(b4_l7))
        self.play(Create(SurroundingRectangle(b4_l7, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): the sense check
        self.next_band(5)
        b5_title = Tex("The hand-span sense check").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"A hand-span $\approx$ 10 cm $\approx$ 5 km —").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"about an hour's walk").scale(0.95).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"7,4 cm $\to$ 3,7 km: under a span,").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex(r"under an hour — it fits").scale(0.95).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)
        bad = Tex(r"37 km from under one hand-span").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(bad))
        self.play(Create(strike(bad)))
        self.wait(2)
        b5_l5 = Tex(r"Convert, then ask: could I walk this").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        b5_l6 = Tex(r"in an afternoon?").scale(0.95).shift(band_shift(5) + DOWN * 3.7)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): the traps and where the skill feeds
        self.next_band(6)
        b6_title = Tex("Traps, named").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        t1 = Tex(r"$\div$ 1 000 on the cm $\to$ m rung").scale(0.9).shift(band_shift(6) + UP * 1.2)
        self.play(Write(t1))
        self.play(Create(strike(t1)))
        self.wait(2)
        t2 = Tex(r"wrong factor — sheet quietly changed").scale(0.9).shift(band_shift(6) + UP * 0.3)
        self.play(Write(t2))
        self.play(Create(strike(t2)))
        self.wait(2)
        t3 = Tex(r"rounding 7,4 up before multiplying").scale(0.9).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(t3))
        self.play(Create(strike(t3)))
        self.wait(2)
        t4 = Tex(r"metres offered where km were asked").scale(0.9).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(t4))
        self.play(Create(strike(t4)))
        self.wait(2)
        b6_l1 = Tex(r"This skill feeds gradient, cross-sections,").scale(0.9).shift(band_shift(6) + DOWN * 2.5)
        b6_l2 = Tex(r"area, and every ``how far'' question").scale(0.9).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the shrunk district
        self.next_band(7)
        b7_title = Tex("The district, shrunk 50 000 times").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"A map is a scale model pressed flat —").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"know only HOW HARD it was shrunk").scale(0.95).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Marinade rule: 1 part to 5 parts works in").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex(r"spoons or jugs — ratios compare, not count").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex(r"Bottom-margin bar: the pre-calculated").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        b7_l6 = Tex(r"till slip — read km with no arithmetic").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(2.5)
        b7_l7 = Tex(r"Pinch-zoom: 1:10 000 is the zoomed-in sheet").scale(0.9).shift(band_shift(7) + DOWN * 3.5)
        self.play(Write(b7_l7))
        self.play(Create(SurroundingRectangle(b7_l7, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): multiply once, step down twice
        self.next_band(8)
        b8_title = Tex("Multiply once, step down twice").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Un-shrink: $7{,}4 \times 50\,000 = 370\,000$ cm").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex(r"True — and useless: nobody quotes").scale(0.95).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex(r"a trip in centimetres").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex(r"Step down like cents to rand:").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex(r"$370\,000$ cm $\to$ 3 700 m $\to$ 3,7 km").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2.5)
        b8_l6 = Tex(r"Say the unit: ``kilometres'' is the").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        b8_l7 = Tex(r"cheapest mark you will ever write").scale(0.95).shift(band_shift(8) + DOWN * 3.6)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_7): shoelaces and zoomed sheets
        self.next_band(9)
        b9_title = Tex("Shoelaces and zoomed-in sheets").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Bendy road: shoelace along the curves,").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex(r"then straighten: 11,8 cm $\to$ 5,9 km").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex(r"Orthophoto: same 7,4 cm $\to$ only 740 m —").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex(r"a fifth of the ground, zoomed in").scale(0.95).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex(r"Backwards: 3,7 km $\div$ 50 000 $= 7{,}4$ cm —").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        b9_l6 = Tex(r"reverse your own answer to check it").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): the closing checklist
        self.next_band(10)
        b10_title = Tex("The closing checklist").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Measure to the millimetre").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"Never round before multiplying").scale(0.95).shift(band_shift(10) + UP * 0.5)
        b10_l3 = Tex(r"Use the scale printed on THIS sheet").scale(0.95).shift(band_shift(10) + DOWN * 0.2)
        b10_l4 = Tex(r"Finish in the unit that was asked").scale(0.95).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex(r"Give every answer the hand-span test").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(2.5)
        b10_l6 = Tex(r"Gradient, cross-section and area all").scale(0.95).shift(band_shift(10) + DOWN * 2.8)
        b10_l7 = Tex(r"stand on this one conversion").scale(0.95).shift(band_shift(10) + DOWN * 3.5)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.wait(4)
