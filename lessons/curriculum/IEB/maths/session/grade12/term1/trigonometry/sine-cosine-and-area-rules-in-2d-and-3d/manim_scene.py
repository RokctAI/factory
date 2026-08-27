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

# Band-layout whiteboard scene. One band per teaching beat, camera moves down,
# nothing is ever removed. Covers all seven subtopics of the session duo:
# Part 1 — Expert (subtopics 1-4), Part 2 — Simplifier (subtopics 5-7),
# band time apportioned to subtopics.json (220/230/250/260/190/200/220 of 1570 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SineCosineAndAreaRulesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): labels and the three rules
        title = Tex("Sine, Cosine and Area Rules").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Little $a$ faces capital $A$ — always").scale(1.05).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = MathTex(r"\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}").scale(1.05).shift(DOWN * 0.1)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"a^2 = b^2 + c^2 - 2bc\cos A").scale(1.05).shift(DOWN * 1.1)
        self.play(Write(d3))
        self.wait(2)
        d4 = MathTex(r"\text{Area} = \tfrac{1}{2}ab\sin C").scale(1.05).shift(DOWN * 2.1)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the stocktake
        self.next_band(1)
        b1_title = Tex("The stocktake chooses the rule").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Complete pair $+$ one more piece: SINE rule").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Two sides + included angle, or three sides: COSINE rule").scale(0.95).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Two sides + wedge, area wanted: AREA rule").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("All proofs start: drop a perpendicular height").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the sine rule at work
        self.next_band(2)
        b2_title = Tex(r"$A = 35^\circ$, $B = 75^\circ$, $a = 12$").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"b = \frac{12\sin 75^\circ}{\sin 35^\circ} = 20{,}21").scale(1.05).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = Tex("Bigger angle faces longer side: $20{,}21 > 12$ \\; sensible").scale(0.95).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"C = 180^\circ - 35^\circ - 75^\circ = 70^\circ \;\text{(free)}").scale(1.0).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("Angle hunts: check the obtuse alternative too").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): the cosine rule at work
        self.next_band(3)
        b3_title = Tex("Sides 6 and 11 around $50^\\circ$").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"a^2 = 36 + 121 - 132\cos 50^\circ = 72{,}15").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"a = \sqrt{72{,}15} \approx 8{,}49").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = Tex("Pythagoras plus a hinge correction").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"\text{Sides } 4, 7, 9: \; \cos A = \tfrac{114}{126} = \tfrac{19}{21}, \; A \approx 25{,}21^\circ").scale(0.9).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = MathTex(r"\text{Area} = \tfrac{1}{2}(6)(11)\sin 50^\circ \approx 25{,}28").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_4): the two-triangle strategy
        self.next_band(4)
        b4_title = Tex("Mast at P, observers at Q and R").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\hat{Q} = 65^\circ, \; \hat{R} = 40^\circ, \; QR = 80 \Rightarrow \hat{P} = 75^\circ").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\text{Bridge } PQ = \frac{80\sin 40^\circ}{\sin 75^\circ} = 53{,}24 \text{ m}").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{Standing page: height} = PQ\tan 32^\circ").scale(1.0).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"= 53{,}24 \times 0{,}6249 = 33{,}27 \text{ m}").scale(1.05).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex("Solve the data-rich triangle first, then cross").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): which tool comes out of the box
        self.next_band(5)
        b5_title = Tex("Which tool comes out of the box").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Sine rule: the matching-pairs tool").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex("Cosine rule: the hinge tool").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Area rule: the carpet quote — no ladder needed").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex("Side over the WRONG angle's sine $=$ the classic zero").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l4))
        self.play(Create(strike(b5_l4)))
        self.wait(3)

        # --- Band 6 (subtopic_6): the field you cannot walk across
        self.next_band(6)
        b6_title = Tex("Fences 6 and 11, hinge at $50^\\circ$").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"36 + 121 = 157, \quad 132\cos 50^\circ \approx 84{,}85").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\sqrt{157 - 84{,}85} \approx 8{,}49 \text{ units of fence}").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = MathTex(r"\text{At } 90^\circ: \sqrt{157} \approx 12{,}53 \;\text{(pure Pythagoras)}").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"\text{Marsh area: } \tfrac{1}{2}(6)(11)\sin 50^\circ \approx 25{,}28").scale(0.95).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_7): the flagpole and its two triangles
        self.next_band(7)
        b7_title = Tex("Two pages and a spine").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Lying page: ground triangle with the data").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("Standing page: right-angled, holds the height").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"\text{Spine } PQ = \frac{80\sin 40^\circ}{\sin 75^\circ} \approx 53{,}24").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"\text{Height} = 53{,}24\tan 32^\circ \approx 33{,}27 \text{ m}").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("Data-rich page first; only the spine travels").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.wait(4)
