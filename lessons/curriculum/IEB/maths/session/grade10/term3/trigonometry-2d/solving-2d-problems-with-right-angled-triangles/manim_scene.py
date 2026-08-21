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

# Band-layout whiteboard scene. One band per teaching beat; the camera moves
# down to clean space and nothing is ever removed. Covers all seven subtopics
# of the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7), dwell times
# roughly proportional to subtopics.json (160/170/170/190/160/170/150 of 1170 s).

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a term, teacher-style."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Solving2DTrigProblemsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): elevation and depression, from the horizontal
        title = Tex("Angles of Elevation and Depression").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        eye = LEFT * 4.0 + UP * 0.4
        horiz = Line(eye, eye + RIGHT * 7.0)
        sight_up = Line(eye, eye + RIGHT * 5.5 + UP * 2.0)
        self.play(Create(horiz))
        self.wait(1.5)
        self.play(Create(sight_up))
        self.wait(1.5)
        b0_l1 = Tex(r"Elevation: horizontal first, then tilt UP").scale(0.9).shift(DOWN * 0.8)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex(r"Depression: horizontal first, then tilt DOWN").scale(0.9).shift(DOWN * 1.6)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex(r"NEVER from the vertical cliff face").scale(0.9).shift(DOWN * 2.5)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=RED)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the alternate-angle bridge
        self.next_band(1)
        b1_title = Tex("The alternate-angle bridge").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        topP = band_shift(1) + LEFT * 3.5 + UP * 1.0
        botP = band_shift(1) + RIGHT * 3.5 + DOWN * 1.4
        h_top = Line(topP, topP + RIGHT * 3.5)
        h_bot = Line(botP + LEFT * 7.0, botP)
        sight = Line(topP, botP)
        self.play(Create(h_top), Create(h_bot))
        self.wait(1.5)
        self.play(Create(sight))
        self.wait(2)
        b1_l1 = Tex(r"Two parallel horizontals, one line of sight across both").scale(0.85).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex(r"Depression from the top $=$ elevation from the ground").scale(0.9).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): mast sketch and labels
        self.next_band(2)
        b2_title = Tex(r"35 m from a mast, elevation $28^\circ$").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        base = band_shift(2) + RIGHT * 2.5 + DOWN * 1.6
        obs = band_shift(2) + LEFT * 3.5 + DOWN * 1.6
        mast = Line(base, base + UP * 3.0)
        ground = Line(obs, base)
        sight2 = Line(obs, base + UP * 3.0)
        sq = Square(side_length=0.3).move_to(base + UP * 0.15 + LEFT * 0.15)
        self.play(Create(mast), Create(ground))
        self.play(Create(sight2), Create(sq))
        self.wait(2)
        lab_h = MathTex("h").scale(0.9).next_to(mast, RIGHT, buff=0.2)
        lab_35 = MathTex(r"35 \text{ m}").scale(0.8).next_to(ground, DOWN, buff=0.2)
        lab_a = MathTex(r"28^\circ").scale(0.7).move_to(obs + RIGHT * 1.1 + UP * 0.28)
        self.play(Write(lab_h), Write(lab_35), Write(lab_a))
        self.wait(2)
        b2_l1 = Tex(r"From the angle: opposite $h$, adjacent 35, hypotenuse unused").scale(0.8).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l1))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): solve for the height
        self.next_band(3)
        b3_title = Tex("Have adjacent, want opposite: tangent").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\tan 28^\circ = \frac{h}{35}").scale(1.1).shift(band_shift(3) + UP * 1.0)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"h = 35 \times \tan 28^\circ = 35 \times 0{,}5317").scale(1.0).shift(band_shift(3) + DOWN * 0.1)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex(r"$h = 18{,}6$ m (one decimal, unit stated)").scale(1.05).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex(r"Degree mode — check the little D first").scale(0.9).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): finding an angle — the ladder
        self.next_band(4)
        b4_title = Tex("Finding an angle: the ladder").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"6 m ladder, foot 1,8 m from the wall").scale(0.95).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\cos\theta = \frac{1{,}8}{6} = 0{,}3 \;\text{(adjacent, hypotenuse)}").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"\theta = \cos^{-1}(0{,}3) = 72{,}5^\circ").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex(r"Ratio back to angle: the INVERSE function, never division").scale(0.85).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): finding a distance — cliff and car
        self.next_band(5)
        b5_title = Tex("Finding a distance: cliff and car").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Cliff 45 m; depression to the car $32^\circ$").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"Alternate angles: elevation at the car is also $32^\circ$").scale(0.9).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\tan 32^\circ = \frac{45}{d} \;\Rightarrow\; d = \frac{45}{\tan 32^\circ}").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"d = \frac{45}{0{,}6249} = 72{,}0 \text{ m}").scale(1.05).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex(r"Unknown in the bottom: DIVIDE by the tan").scale(0.9).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): two triangles, one height — setup
        self.next_band(6)
        b6_title = Tex("Two triangles, one height").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        baseT = band_shift(6) + RIGHT * 3.2 + DOWN * 1.6
        topT = baseT + UP * 2.8
        pQ = baseT + LEFT * 2.0
        pP = baseT + LEFT * 4.5
        tower = Line(baseT, topT)
        groundT = Line(pP + LEFT * 0.5, baseT)
        sQ = Line(pQ, topT)
        sP = Line(pP, topT)
        self.play(Create(tower), Create(groundT))
        self.play(Create(sQ), Create(sP))
        self.wait(2)
        lab_P = MathTex(r"P: 35^\circ").scale(0.6).next_to(pP, DOWN, buff=0.2)
        lab_Q = MathTex(r"Q: 55^\circ").scale(0.6).next_to(pQ, DOWN, buff=0.2)
        lab_25 = MathTex(r"25 \text{ m}").scale(0.6).move_to((pP + pQ) / 2 + DOWN * 0.7)
        lab_d = MathTex(r"d").scale(0.7).move_to((pQ + baseT) / 2 + DOWN * 0.3)
        self.play(Write(lab_P), Write(lab_Q), Write(lab_25), Write(lab_d))
        self.wait(2.5)
        b6_l1 = MathTex(r"h = d\tan 55^\circ \qquad h = (d + 25)\tan 35^\circ").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): equate the two heights and solve
        self.next_band(7)
        b7_title = Tex("Equate, factor, divide, verify").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"d\tan 55^\circ = (d + 25)\tan 35^\circ").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"d(\tan 55^\circ - \tan 35^\circ) = 25\tan 35^\circ").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"d = \frac{25 \times 0{,}7002}{1{,}4281 - 0{,}7002} = \frac{17{,}505}{0{,}7279} = 24{,}05").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"h = 24{,}05 \times \tan 55^\circ = 34{,}3 \text{ m}").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex(r"Verify: $(24{,}05 + 25)\tan 35^\circ = 34{,}3$ \;\checkmark").scale(0.9).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): everything starts level
        self.next_band(8)
        b8_title = Tex("Everything starts level").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Elevation: how far UP from level (the drone)").scale(0.95).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex(r"Depression: how far DOWN from level (the friend below)").scale(0.9).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"You look down at your friend at the SAME angle").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = Tex(r"your friend looks up at you — one line, two parallel levels").scale(0.85).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the mast, one triangle at a time
        self.next_band(9)
        b9_title = Tex("The mast, one triangle at a time").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Three lines: upright mast, flat ground, slanted sight").scale(0.9).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"Stand inside $28^\circ$: opposite $=$ mast, adjacent $=$ 35 m").scale(0.9).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex(r"SOH CAH TOA: opposite with adjacent lives only in TOA").scale(0.9).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"h = 35\tan 28^\circ \approx 18{,}6 \text{ m — about four storeys}").scale(0.95).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 10 (subtopic_6): the zipline — sine for balance
        self.next_band(10)
        b10_title = Tex("The zipline: sine for balance").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"40 m cable at $25^\circ$: the cable is the hypotenuse").scale(0.9).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex(r"Height is opposite — opposite with hypotenuse: SOH").scale(0.9).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"h = 40\sin 25^\circ = 40 \times 0{,}4226 \approx 16{,}9 \text{ m}").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex(r"The two sides in the story pick the ratio for you").scale(0.9).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l4))
        self.wait(2.5)

        # --- Band 11 (subtopic_7): reading the story into a sketch
        self.next_band(11)
        b11_title = Tex("Reading the story into a sketch").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex(r"1. Vertical thing $+$ horizontal thing $=$ free right angle").scale(0.85).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = Tex(r"2. The angle sits with the OBSERVER — level line for depression").scale(0.8).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = Tex(r"3. ``How far'' $=$ horizontal; ``how high'' $=$ vertical; cable $=$ hypotenuse").scale(0.75).shift(band_shift(11) + DOWN * 0.6)
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = Tex(r"4. Read the answer back: 18,6 m mast sensible; 1 860 m — mode!").scale(0.8).shift(band_shift(11) + DOWN * 1.5)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        self.wait(4)
