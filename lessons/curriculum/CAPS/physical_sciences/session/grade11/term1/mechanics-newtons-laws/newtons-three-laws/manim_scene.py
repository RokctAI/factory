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

# Band-layout whiteboard scene for the Newton's Three Laws session duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (220/230/240/225/180/180/190
# of 1465 s). Exporter-safe mobjects only; add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class NewtonsThreeLawsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the first law and inertia ---
        title = Tex("Newton's Three Laws").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("First law: rest or uniform velocity continues").scale(1.0).shift(UP * 1.3)
        b0_l2 = Tex("unless a NET force acts").scale(1.0).shift(UP * 0.6)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Inertia: resistance to change of motion").scale(1.0).shift(DOWN * 0.4)
        b0_l4 = Tex("Mass measures inertia").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_trap = Tex("a force keeps an object moving").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(b0_trap))
        self.play(Create(strike(b0_trap)))
        self.wait(1.5)
        b0_l5 = Tex("A force CHANGES motion").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the seatbelt argument ---
        self.next_band(1)
        b1_title = Tex("The taxi brakes at 60 km/h").scale(1.15).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        taxi = Rectangle(width=3.0, height=1.1).shift(band_shift(1) + LEFT * 1.5 + UP * 1.0)
        ltaxi = Tex("taxi").scale(0.85).shift(band_shift(1) + LEFT * 1.5 + UP * 1.0)
        brake = Arrow(LEFT * 3.2 + UP * 1.0, LEFT * 4.6 + UP * 1.0, buff=0, color=RED).shift(band_shift(1))
        lbrake = Tex("brake force").scale(0.8).shift(band_shift(1) + LEFT * 3.9 + UP * 1.7)
        pas = Dot(band_shift(1) + LEFT * 1.0 + UP * 1.0, color=YELLOW)
        aP = Arrow(LEFT * 1.0 + UP * 0.3, RIGHT * 1.0 + UP * 0.3, buff=0, color=YELLOW).shift(band_shift(1))
        lP = Tex("passenger keeps going").scale(0.8).shift(band_shift(1) + RIGHT * 3.2 + UP * 0.3)
        self.play(Create(taxi), Write(ltaxi))
        self.play(Create(brake), Write(lbrake))
        self.wait(1.5)
        self.play(FadeIn(pas), Create(aP), Write(lP))
        self.wait(2.5)
        b1_l1 = Tex("No backward force on the passenger").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("The seatbelt SUPPLIES the missing force").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = Tex("Headrest: same job in reverse — whiplash").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l3))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the second law and the method ---
        self.next_band(2)
        b2_title = Tex("Second law").scale(1.2).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"F_{net} = ma").scale(1.4).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=BLUE)))
        self.wait(2.5)
        b2_l2 = MathTex(r"1\ \text{N} = 1\ \text{kg m/s}^2").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("1. Free-body diagram").scale(0.95).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = Tex("2. State the positive direction").scale(0.95).shift(band_shift(2) + DOWN * 1.4)
        b2_l5 = Tex("3. Write $F_{net} = ma$ along it").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        b2_l6 = Tex("4. Substitute; answer with unit and direction").scale(0.95).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l3))
        self.wait(1.5)
        self.play(Write(b2_l4))
        self.wait(1.5)
        self.play(Write(b2_l5))
        self.wait(1.5)
        self.play(Write(b2_l6))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): the crate, worked ---
        self.next_band(3)
        b3_title = Tex("20 kg crate: 100 N pull, 40 N friction").scale(1.05).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"F_{net} = 100 - 40 = 60\ \text{N forward}").scale(1.05).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"a = \frac{60}{20} = 3\ \text{m/s}^2").scale(1.1).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex(r"Constant velocity: $F_{net} = 0$, so $F = 40$ N").scale(1.0).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_trap = Tex("weight in the horizontal equation").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_trap))
        self.play(Create(strike(b3_trap)))
        self.wait(1.5)
        b3_l4 = Tex("Vertical and horizontal stay separate").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the lift, cases one and two ---
        self.next_band(4)
        b4_title = Tex("70 kg learner on a scale in a lift").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        d = Dot(band_shift(4) + LEFT * 3.0 + UP * 0.8)
        aN = Arrow(LEFT * 3.0 + UP * 0.8, LEFT * 3.0 + UP * 2.0, buff=0, color=YELLOW).shift(band_shift(4))
        lN = MathTex(r"N").scale(0.9).shift(band_shift(4) + LEFT * 2.4 + UP * 1.9)
        aW = Arrow(LEFT * 3.0 + UP * 0.8, LEFT * 3.0 + DOWN * 0.6, buff=0, color=YELLOW).shift(band_shift(4))
        lw = MathTex(r"686\ \text{N}").scale(0.85).shift(band_shift(4) + LEFT * 1.9 + DOWN * 0.5)
        self.play(FadeIn(d))
        self.play(Create(aN), Write(lN))
        self.play(Create(aW), Write(lw))
        self.wait(2)
        b4_l1 = MathTex(r"\text{Rest: } N = 686\ \text{N}").scale(1.0).shift(band_shift(4) + RIGHT * 1.8 + UP * 1.4)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex(r"Up at 2 m/s$^2$:").scale(1.0).shift(band_shift(4) + DOWN * 1.3)
        b4_l3 = MathTex(r"N - 686 = 70 \times 2 \Rightarrow N = 826\ \text{N}").scale(1.0).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = Tex("Feels heavier; true weight unchanged").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): down, free fall ---
        self.next_band(5)
        b5_l1 = Tex(r"Down at 2 m/s$^2$ (up positive, $a = -2$):").scale(1.0).shift(band_shift(5) + UP * 2.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"N - 686 = 70 \times (-2) \Rightarrow N = 546\ \text{N}").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = MathTex(r"\text{Free fall: } N = 686 - 686 = 0\ \text{N}").scale(1.0).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("Apparent weightlessness: no support,").scale(0.95).shift(band_shift(5) + DOWN * 1.0)
        b5_l5 = Tex("not no gravity").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(2.5)
        b5_l6 = Tex("Mass 70 kg; weight 686 N — never swap them").scale(0.95).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l6))
        self.wait(2.5)

        # --- Band 6 (subtopic_3): the rocket ---
        self.next_band(6)
        b6_title = Tex("Rocket: 5 000 kg, thrust 70 000 N").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"w = 5\ 000 \times 9{,}8 = 49\ 000\ \text{N}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"F_{net} = 70\ 000 - 49\ 000 = 21\ 000\ \text{N}").scale(1.0).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"a = \frac{21\ 000}{5\ 000} = 4{,}2\ \text{m/s}^2 \text{ up}").scale(1.05).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the third law ---
        self.next_band(7)
        b7_title = Tex("Third law: action-reaction pairs").scale(1.15).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("A on B equals B on A, opposite direction").scale(1.0).shift(band_shift(7) + UP * 1.3)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("Equal magnitude").scale(0.95).shift(band_shift(7) + UP * 0.4)
        b7_l3 = Tex("Opposite direction").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        b7_l4 = Tex("On DIFFERENT objects").scale(0.95).shift(band_shift(7) + DOWN * 1.0)
        b7_l5 = Tex("Same type of force").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l2))
        self.wait(1.5)
        self.play(Write(b7_l3))
        self.wait(1.5)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=BLUE)))
        self.wait(1.5)
        self.play(Write(b7_l5))
        self.wait(2)
        b7_l6 = Tex("Swimmer pushes water back; water pushes her on").scale(0.9).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l6))
        self.wait(2.5)

        # --- Band 8 (subtopic_4): the book on the table ---
        self.next_band(8)
        b8_title = Tex("Book on a table: 20 N down, 20 N up").scale(1.05).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_trap = Tex("weight and normal force are a pair").scale(1.0).shift(band_shift(8) + UP * 1.3)
        self.play(Write(b8_trap))
        self.play(Create(strike(b8_trap)))
        self.wait(2)
        b8_l1 = Tex("Both act on the BOOK — same object").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Earth pulls book $\\leftrightarrow$ book pulls Earth").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Table pushes book $\\leftrightarrow$ book pushes table").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Horse and cart: the pulls land on different").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        b8_l5 = Tex("objects, so they never cancel").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): the taxi brakes ---
        self.next_band(9)
        b9_title = Tex("Why you jerk forward when the taxi brakes").scale(1.05).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Your body did not fly — it just kept going").scale(0.95).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("The TAXI changed; nothing shoved you").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Inertia: stubbornness; mass: how much of it").scale(0.95).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("The seatbelt shoves you WITH the taxi").scale(0.95).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("Force changes motion; it does not maintain it").scale(0.95).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_6): harder push, heavier load ---
        self.next_band(10)
        b10_title = Tex("Harder push, heavier load").scale(1.2).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Only the LEFTOVER push counts").scale(1.0).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"100 - 40 = 60\ \text{N leftover}").scale(1.05).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"\frac{60}{20} = 3\ \text{m/s}^2").scale(1.1).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex("Steady speed or at rest: leftover is ZERO").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("Half the topic's questions solved by that line").scale(0.9).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_7): the lift floor and the wall ---
        self.next_band(11)
        b11_title = Tex("The lift floor and the wall that pushes back").scale(1.05).shift(band_shift(11) + UP * 2.3)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex("Scale reads the floor's push, not you").scale(0.95).shift(band_shift(11) + UP * 1.3)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"686 \to 826 \to 546 \to 0\ \text{N}").scale(1.05).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11_l2))
        self.wait(2)
        b11_l3 = Tex("Your real weight never changed once").scale(0.95).shift(band_shift(11) + DOWN * 0.6)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2.5)
        b11_l4 = Tex("Push the wall — it pushes back equally").scale(0.95).shift(band_shift(11) + DOWN * 1.6)
        self.play(Write(b11_l4))
        self.wait(2)
        b11_l5 = Tex("Equal pushes land on DIFFERENT things,").scale(0.95).shift(band_shift(11) + DOWN * 2.5)
        b11_l6 = Tex("so walking works and carts still roll").scale(0.95).shift(band_shift(11) + DOWN * 3.2)
        self.play(Write(b11_l5))
        self.play(Write(b11_l6))
        self.wait(4)
