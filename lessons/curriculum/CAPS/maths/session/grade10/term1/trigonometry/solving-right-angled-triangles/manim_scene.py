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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing removed.
# Write-only reveals on single-string Tex/MathTex keep the export clean; the
# triangles are hand-built from Lines + Tex labels (exporter-supported shapes
# only). Bands cover all seven subtopics (Part 1 — Expert: 1-4; Part 2 —
# Simplifier: 5-7), dwell time proportional to subtopics.json
# (230/200/230/270/190/185/195 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def right_triangle(origin, base=3.2, height=2.0):
    """Right angle at origin's right end: base along, vertical up at the far
    end, hypotenuse back to origin. Built from Lines only."""
    a = origin
    b = origin + RIGHT * base
    c = origin + RIGHT * base + UP * height
    return VGroup(Line(a, b), Line(b, c), Line(c, a),
                  Line(b + LEFT * 0.25, b + LEFT * 0.25 + UP * 0.25),
                  Line(b + LEFT * 0.25 + UP * 0.25, b + UP * 0.25))


class SolvingRightAngledTrianglesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(12)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): labelling and the choosing routine
        title = Tex("Solving Right-Angled Triangles").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = Tex(r"Label from your chosen angle:").scale(1.05).shift(UP * 0.9)
        self.play(Write(l1))
        self.wait(1.5)
        l2 = Tex(r"hypotenuse faces the right angle — it never moves;").scale(1.0).shift(UP * 0.1)
        l3 = Tex(r"opposite faces YOUR angle; adjacent runs beside it").scale(1.0).shift(DOWN * 0.7)
        self.play(Write(l2))
        self.play(Write(l3))
        self.wait(2.5)
        l4 = MathTex(r"\frac{O}{H}: \sin \quad \frac{A}{H}: \cos \quad \frac{O}{A}: \tan").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(l4))
        self.play(Create(SurroundingRectangle(l4, color=YELLOW)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the ladder — unknown on top
        self.next_band(1)
        b1_title = Tex(r"Ladder: 20 m at $35^\circ$ — how high up the wall?").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        tri1 = right_triangle(band_shift(1) + LEFT * 3.6 + DOWN * 0.2)
        self.play(Create(tri1))
        b1_ang = MathTex(r"35^\circ").scale(0.8).shift(band_shift(1) + LEFT * 2.6 + UP * 0.05)
        b1_hyp = MathTex(r"20").scale(0.9).shift(band_shift(1) + LEFT * 2.4 + UP * 1.3)
        b1_opp = MathTex(r"h").scale(0.9).shift(band_shift(1) + RIGHT * 0.05 + UP * 0.8)
        self.play(Write(b1_ang), Write(b1_hyp), Write(b1_opp))
        self.wait(2)
        b1_l1 = MathTex(r"\sin 35^\circ = \frac{h}{20}").scale(1.05).shift(band_shift(1) + RIGHT * 2.6 + UP * 1.0)
        b1_l2 = MathTex(r"h = 20 \sin 35^\circ").scale(1.05).shift(band_shift(1) + RIGHT * 2.6 + UP * 0.0)
        b1_l3 = MathTex(r"h = 11{,}47 \text{ m}").scale(1.1).shift(band_shift(1) + RIGHT * 2.6 + DOWN * 1.0)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        b1_l4 = Tex(r"Sense check: opposite is always shorter than hypotenuse").scale(0.95).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the cable — unknown underneath
        self.next_band(2)
        b2_title = Tex(r"Cable at $40^\circ$, anchor 15 m out — cable length?").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\cos 40^\circ = \frac{15}{c}").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"Unknown underneath: divide the known by the ratio").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"c = \frac{15}{\cos 40^\circ} = 19{,}58 \text{ m}").scale(1.1).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_wrong = MathTex(r"15 \times \cos 40^\circ = 11{,}49 \;\text{ — shorter than } 15!").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        b2_rule = Tex("The hypotenuse must be the longest side").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_rule))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): the ramp — finding the angle, whole triangle
        self.next_band(3)
        b3_title = Tex(r"Ramp: rises 0,8 m over 5 m — find the angle").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\tan\theta = \frac{0{,}8}{5} = 0{,}16").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\theta = \tan^{-1}(0{,}16) = 9{,}09^\circ").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = MathTex(r"\text{Third angle: } 90^\circ - 9{,}09^\circ = 80{,}91^\circ").scale(1.0).shift(band_shift(3) + DOWN * 0.9)
        b3_l4 = MathTex(r"\text{Pythagoras: } \sqrt{0{,}64 + 25} = 5{,}06 \text{ m}").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex(r"Round only the final answer, never mid-working").scale(0.95).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_4): elevation — the mast
        self.next_band(4)
        b4_title = Tex(r"Elevation $62^\circ$, 24 m away, eyes at 1,6 m").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l0 = Tex(r"Both angles measured from the HORIZONTAL").scale(0.95).shift(band_shift(4) + UP * 1.3)
        self.play(Write(b4_l0))
        self.wait(2)
        b4_l1 = MathTex(r"\tan 62^\circ = \frac{\text{rise}}{24}").scale(1.05).shift(band_shift(4) + UP * 0.3)
        b4_l2 = MathTex(r"\text{rise} = 24 \tan 62^\circ = 45{,}14 \text{ m}").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\text{Mast} = 45{,}14 + 1{,}6 = 46{,}74 \text{ m}").scale(1.05).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        b4_l4 = Tex(r"The triangle started at her eyes — add the 1,6 m").scale(0.95).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): depression — the cliff
        self.next_band(5)
        b5_title = Tex(r"Cliff 40 m, depression $25^\circ$ — distance to boat?").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"Alternate angles: elevation at the boat $= 25^\circ$").scale(1.0).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\tan 25^\circ = \frac{40}{d}").scale(1.05).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"d = \frac{40}{\tan 25^\circ} = 85{,}78 \text{ m}").scale(1.05).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex(r"Traps: radian mode; depression placed inside the").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        b5_l5 = Tex(r"triangle; eye height dropped; rounding mid-way").scale(0.95).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): naming sides from where you stand
        self.next_band(6)
        b6_title = Tex("Naming the sides from where you stand").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Stand at your angle: opposite faces you,").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"adjacent runs beside you, hypotenuse never moves").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"Only two sides matter: the known and the wanted").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"\text{Ladder: } h = 20 \sin 35^\circ = 11{,}47 \text{ m}").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        b6_l5 = Tex(r"Lazier lean than $45^\circ$, so under 14 m — sensible").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.wait(2.5)

        # --- Band 7 (subtopic_6): upstairs multiply, downstairs divide
        self.next_band(7)
        b7_title = Tex("Upstairs you multiply, downstairs you divide").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"12 loaves cost R216: one loaf is a DIVIDE;").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"R18 each, want 12: that is a MULTIPLY").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"\sin 35^\circ = \frac{h}{20}: \;\; h = 20\sin 35^\circ").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = MathTex(r"c = \frac{15}{\cos 40^\circ} = 19{,}58 \text{ m}").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l3))
        self.wait(2.5)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        b7_l5 = Tex(r"Safety net: the hypotenuse must beat every side").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # --- Band 8 (subtopic_7): looking up and looking down
        self.next_band(8)
        b8_title = Tex("Looking up and looking down").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Your down-angle equals their up-angle — parallel lines").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"\text{Mast: } 24\tan 62^\circ + 1{,}6 = 46{,}74 \text{ m}").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{Boat: } d = \frac{40}{\tan 25^\circ} = 85{,}78 \text{ m}").scale(1.0).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex(r"Ask every time: did my triangle start at the ground,").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        b8_l5 = Tex(r"or on top of a learner?").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(4)
