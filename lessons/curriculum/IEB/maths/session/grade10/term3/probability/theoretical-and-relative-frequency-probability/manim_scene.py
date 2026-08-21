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
# roughly proportional to subtopics.json (160/170/180/170/160/170/160 of
# 1170 s).

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a term, teacher-style."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ProbabilityTwoEnginesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the vocabulary
        title = Tex("The Language of Probability").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Experiment: an action with an uncertain result").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex(r"Outcome: one possible result — spinner lands on 5").scale(1.0).shift(UP * 0.3)
        b0_l3 = MathTex(r"S = \{1, 2, 3, 4, 5, 6, 7, 8\}, \quad n(S) = 8").scale(1.05).shift(DOWN * 0.6)
        b0_l4 = MathTex(r"E = \{3, 6\} \;\text{(multiple of 3)}, \quad n(E) = 2").scale(1.05).shift(DOWN * 1.5)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2.5)
        self.play(Write(b0_l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the 0-to-1 scale
        self.next_band(1)
        b1_title = Tex("Every probability lives between 0 and 1").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"0 $=$ impossible: spinning a 9").scale(1.05).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"1 $=$ certain: spinning a number below nine").scale(1.05).shift(band_shift(1) + UP * 0.3)
        b1_l3 = Tex(r"0,5 $=$ as likely as not").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"\tfrac{1}{4} = 0{,}25 = 25\% \;\;\text{— the same statement}").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = MathTex(r"P = 1{,}3 \;\text{ or }\; P < 0").scale(1.05).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l5))
        self.play(Create(strike(b1_l5)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): theoretical probability on the spinner
        self.next_band(2)
        b2_title = Tex("Theoretical probability: count what COULD happen").scale(0.95).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"P(E) = \frac{n(E)}{n(S)} \;\text{(equally likely)}").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = MathTex(r"P(\text{multiple of } 3) = \frac{2}{8} = \frac{1}{4} = 0{,}25").scale(1.05).shift(band_shift(2) + DOWN * 0.2)
        b2_l3 = MathTex(r"P(\text{greater than } 5) = \frac{3}{8}").scale(1.1).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l2))
        self.wait(2.5)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex(r"Keep fractions exact: $\tfrac{5}{12}$ is exact, $0{,}42$ is not").scale(1.0).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): the bag of marbles
        self.next_band(3)
        b3_title = Tex("The bag: 4 yellow, 5 purple, 3 orange").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"n(S) = 12 \;\text{ marbles — not } 3 \text{ colours!}").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"P(\text{purple}) = \frac{5}{12}").scale(1.1).shift(band_shift(3) + UP * 0.1)
        b3_l3 = MathTex(r"P(\text{yellow}) = \frac{4}{12} = \frac{1}{3}").scale(1.1).shift(band_shift(3) + DOWN * 1.0)
        b3_l4 = MathTex(r"P(\text{yellow or orange}) = \frac{4 + 3}{12} = \frac{7}{12}").scale(1.05).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)
        b3_l5 = Tex(r"Count marbles, never colours").scale(1.05).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): relative frequency
        self.next_band(4)
        b4_title = Tex("Relative frequency — count what DID happen").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"A drawing pin is lopsided — theory is silent").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\text{Rel freq} = \frac{\text{occurrences}}{\text{trials}}").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"250 \text{ tosses, } 90 \text{ point-up}: \;\; \frac{90}{250} = 0{,}36").scale(1.05).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex(r"The data's estimate of the truth").scale(1.05).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the settling, and which engine when
        self.next_band(5)
        b5_title = Tex("More trials, steadier estimate").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"10 \text{ tosses}: 0{,}6 \quad 250: 0{,}36 \quad 2\,500: 0{,}38").scale(1.0).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex(r"33 heads in 60 tosses $= 0{,}55$: normal wobble").scale(1.0).shift(band_shift(5) + UP * 0.3)
        b5_l3 = Tex(r"$70\%$ heads in $3\,000$ tosses: a weighted coin, caught").scale(0.95).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l2))
        self.wait(2.5)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex(r"Spinners, coins, marbles: theoretical").scale(1.0).shift(band_shift(5) + DOWN * 1.5)
        b5_l5 = Tex(r"Drawing pins, weather, buses: relative frequency").scale(1.0).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): complementary events
        self.next_band(6)
        b6_title = Tex("Complementary events — the best shortcut").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"P(\text{not } A) = 1 - P(A)").scale(1.2).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = MathTex(r"P(\text{not an } 8) = 1 - \tfrac{1}{8} = \tfrac{7}{8}").scale(1.05).shift(band_shift(6) + UP * 0.1)
        b6_l3 = MathTex(r"P(\text{dry day}) = 1 - 0{,}25 = 0{,}75").scale(1.05).shift(band_shift(6) + DOWN * 0.8)
        b6_l4 = MathTex(r"P(\text{not orange}) = 1 - \tfrac{3}{12} = \tfrac{3}{4}").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex(r"Mutually exclusive $+$ exhaustive $\Rightarrow$ they sum to 1").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the volume slider
        self.next_band(7)
        b7_title = Tex("A volume slider from impossible to certain").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        lineL = band_shift(7) + LEFT * 5.0 + UP * 0.8
        lineR = band_shift(7) + RIGHT * 5.0 + UP * 0.8
        slider = Line(lineL, lineR)
        lab0 = MathTex("0").scale(0.9).next_to(lineL, DOWN, buff=0.15)
        lab1 = MathTex("1").scale(0.9).next_to(lineR, DOWN, buff=0.15)
        labI = Tex("mute / impossible").scale(0.7).next_to(lineL, UP, buff=0.15)
        labC = Tex("full / certain").scale(0.7).next_to(lineR, UP, buff=0.15)
        self.play(Create(slider), Write(lab0), Write(lab1), Write(labI), Write(labC))
        self.wait(2)
        d_mid = Dot(band_shift(7) + UP * 0.8, color=YELLOW)
        labM = MathTex(r"0{,}5").scale(0.8).next_to(d_mid, DOWN, buff=0.15)
        d9 = Dot(lineL, color=RED)
        dsun = Dot(lineR, color=GREEN)
        self.play(Create(d9), Create(dsun))
        self.wait(1.5)
        self.play(Create(d_mid), Write(labM))
        self.wait(2)
        b7_l1 = Tex(r"Spinner shows 9: slider at 0. \; Sunrise tomorrow: at 1").scale(0.95).shift(band_shift(7) + DOWN * 0.6)
        b7_l2 = Tex(r"Heads on a coin, even sector: dead centre, 0,5").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        b7_l3 = Tex(r"Nothing sits left of 0 or right of 1 — error alarm").scale(1.0).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): counting your way — the fruit gums
        self.next_band(8)
        b8_title = Tex("Twelve fruit gums: 4 yellow, 5 purple, 3 orange").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"How many COULD you grab? 12").scale(1.05).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"How many make you smile (purple)? 5").scale(1.05).shift(band_shift(8) + UP * 0.3)
        b8_l3 = MathTex(r"\frac{\text{smiles}}{\text{candidates}} = \frac{5}{12}").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex(r"Count THINGS, not TYPES: 3 colours but 12 gums").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        b8_l5 = Tex(r"Purple holds 5 tickets in the draw; orange only 3").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l4))
        self.wait(2.5)
        self.play(Write(b8_l5))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): try it a hundred times
        self.next_band(9)
        b9_title = Tex("Try it a hundred times").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Lopsided object: experience must count instead").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = MathTex(r"\frac{90 \text{ point-ups}}{250 \text{ tosses}} = 0{,}36").scale(1.1).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex(r"5 tosses: a rumour. \; 250: a report. \; 2\,500: an audit").scale(0.95).shift(band_shift(9) + DOWN * 1.0)
        b9_l4 = Tex(r"Fair and symmetrical: count. Lopsided or alive: tally").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l3))
        self.wait(2.5)
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex(r"When both work, the answers settle to the same place").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5))
        self.wait(4)
