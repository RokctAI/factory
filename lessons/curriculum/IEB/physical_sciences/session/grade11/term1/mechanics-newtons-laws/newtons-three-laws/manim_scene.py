# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene for the Newton's Three Laws duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (220/230/240/225/180/180/190
# of 1465 s). Exporter-safe mobjects only; add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ThreeLawsOfMotionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): first law and inertia ---
        title = Tex("Newton's Three Laws").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("First law: rest or uniform velocity persists").scale(0.95).shift(UP * 1.2)
        b0_l2 = Tex("unless a NET force acts").scale(0.95).shift(UP * 0.5)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(VGroup(b0_l1, b0_l2), color=BLUE)))
        self.wait(2.5)
        b0_l3 = Tex("Inertia: resistance to change of motion").scale(0.95).shift(DOWN * 0.7)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Mass measures inertia").scale(0.95).shift(DOWN * 1.5)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the braking taxi ---
        self.next_band(1)
        b1_title = Tex("The braking taxi").scale(1.1).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        taxi = Rectangle(width=3.2, height=1.2, color=YELLOW).shift(band_shift(1) + LEFT * 2.0 + DOWN * 0.4)
        self.play(Create(taxi))
        aBrake = Arrow(LEFT * 0.2 + DOWN * 0.4, LEFT * 1.6 + DOWN * 0.4, buff=0, color=RED).shift(band_shift(1) + RIGHT * 1.8)
        lBrake = Tex("braking force on TAXI").scale(0.8).shift(band_shift(1) + RIGHT * 2.6 + UP * 0.3)
        self.play(Create(aBrake), Write(lBrake))
        self.wait(2)
        b1_l1 = Tex("No backward force on the passenger").scale(0.9).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Body continues at original velocity").scale(0.9).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Seatbelt supplies the missing backward force").scale(0.9).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l3))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): second law statement ---
        self.next_band(2)
        b2_title = Tex("Second law").scale(1.15).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"F_{net} = ma").scale(1.4).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=BLUE)))
        self.wait(2.5)
        b2_l2 = Tex(r"1 N = 1 kg$\cdot$m$\cdot$s$^{-2}$").scale(1.0).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("Method: diagram, positive direction,").scale(0.95).shift(band_shift(2) + DOWN * 0.9)
        b2_l4 = Tex("equation, substitute, answer with unit").scale(0.95).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): the crate ---
        self.next_band(3)
        b3_title = Tex("25 kg crate: 120 N pull, 45 N friction").scale(1.0).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"F_{net} = 120 - 45 = 75\ \text{N}").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"a = \frac{75}{25} = 3\ \text{m}\cdot\text{s}^{-2}").scale(1.05).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Constant velocity? Then $F_{net} = 0$:").scale(0.95).shift(band_shift(3) + DOWN * 1.2)
        b3_l4 = Tex("pull = friction = 45 N").scale(0.95).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Vertical forces stay out of horizontal sums").scale(0.9).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the lift, four cases ---
        self.next_band(4)
        b4_title = Tex("60 kg on a scale in a lift: $w = 588$ N").scale(1.0).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{at rest: } N = 588\ \text{N}").scale(0.95).shift(band_shift(4) + UP * 1.3)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\text{up at } 1{,}5: N = 588 + 90 = 678\ \text{N}").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\text{down at } 1{,}5: N = 588 - 90 = 498\ \text{N}").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"\text{free fall: } N = 0\ \text{N}").scale(0.95).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex("True weight: 588 N in every case").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the rocket ---
        self.next_band(5)
        b5_title = Tex("Rocket: 8 000 kg, thrust 100 000 N").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"w = 8\ 000 \times 9{,}8 = 78\ 400\ \text{N}").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"F_{net} = 100\ 000 - 78\ 400 = 21\ 600\ \text{N}").scale(1.0).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"a = \frac{21\ 600}{8\ 000} = 2{,}7\ \text{m}\cdot\text{s}^{-2}\ \text{up}").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex("Weight is the entry fee before any climb").scale(0.9).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): third law ---
        self.next_band(6)
        b6_title = Tex("Third law: A on B, B on A").scale(1.1).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Equal magnitude, opposite direction,").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("DIFFERENT objects, same type of force").scale(0.95).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(VGroup(b6_l1, b6_l2), color=BLUE)))
        self.wait(2.5)
        b6_l3 = Tex("Rower pushes water back; water pushes boat forward").scale(0.85).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("You push the ground back; the ground pushes you forward").scale(0.85).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l4))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): the book-on-desk trap ---
        self.next_band(7)
        b7_title = Tex("The dictionary trap").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Weight down and normal force up:").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("equal, opposite — but BOTH on the dictionary").scale(0.95).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("NOT an action-reaction pair").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=RED)))
        self.wait(2)
        b7_l4 = Tex("True pairs: Earth-dictionary (gravity),").scale(0.9).shift(band_shift(7) + DOWN * 1.6)
        b7_l5 = Tex("desk-dictionary (contact)").scale(0.9).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(2.5)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the taxi again, felt ---
        self.next_band(8)
        b8_title = Tex("Why you jerk forward when the taxi brakes").scale(1.0).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Nothing pushed you — you simply carried on").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.play(Create(SurroundingRectangle(b8_l1, color=GREEN)))
        self.wait(2.5)
        b8_l2 = Tex("Full bucket vs empty bucket: mass is stubbornness").scale(0.9).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Seatbelt: slows your body WITH the taxi").scale(0.9).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Forces change motion; they do not maintain it").scale(0.9).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): leftover push ---
        self.next_band(9)
        b9_title = Tex("Harder push, heavier load").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Only the LEFTOVER push counts").scale(0.95).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"120 - 45 = 75\ \text{N leftover}").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"75 \div 25 = 3\ \text{m}\cdot\text{s}^{-2}").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("\"Constant velocity\" means leftover = 0").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): lift floor ---
        self.next_band(10)
        b10_title = Tex("The lift floor").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("The scale measures its own push, not you").scale(0.95).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{up: } 678\ \text{N}\quad \text{still: } 588\ \text{N}\quad \text{down: } 498\ \text{N}").scale(0.9).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Cable snaps: scale reads 0 — support gone,").scale(0.9).shift(band_shift(10) + DOWN * 0.7)
        b10_l4 = Tex("gravity still on duty").scale(0.9).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(3)

        # --- Band 11 (subtopic_7): the wall that pushes back ---
        self.next_band(11)
        b11_title = Tex("The wall that pushes back").scale(1.15).shift(band_shift(11) + UP * 2.3)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex("Every push is answered — on the OTHER object").scale(0.95).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11_l1))
        self.play(Create(SurroundingRectangle(b11_l1, color=GREEN)))
        self.wait(2.5)
        b11_l2 = Tex("Donkey pulls cart; cart pulls donkey —").scale(0.9).shift(band_shift(11) + UP * 0.2)
        b11_l3 = Tex("different ledgers, so no cancelling").scale(0.9).shift(band_shift(11) + DOWN * 0.5)
        self.play(Write(b11_l2))
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = Tex("Carry on; leftover over mass; push returned").scale(0.9).shift(band_shift(11) + DOWN * 1.6)
        self.play(Write(b11_l4))
        self.wait(4)
