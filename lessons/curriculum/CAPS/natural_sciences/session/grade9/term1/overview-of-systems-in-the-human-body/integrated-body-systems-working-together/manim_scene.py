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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IntegratedSystemsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Seven Systems and Their Jobs
        title = Tex("The seven systems").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Digestive: food to glucose, absorbed into blood").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Respiratory: oxygen in, carbon dioxide out").scale(0.9).shift(UP * 0.50)
        b0_l3 = Tex("Circulatory: transports everything (about 5 litres per minute)").scale(0.9).shift(DOWN * 0.30)
        b0_l4 = Tex("Excretory: filters blood, removes urea as urine").scale(0.9).shift(DOWN * 1.10)
        b0_l5 = Tex("Nervous controls; musculoskeletal supports and moves; reproductive").scale(0.9).shift(DOWN * 1.90)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4, b0_l5):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Supplying a Cell: Glucose and Oxygen In, Waste Out
        self.next_band(1)
        b1_title = Tex("Supplying one muscle cell").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Bread: digestive system makes glucose, into blood").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Air: respiratory system loads oxygen, into blood").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Circulatory system carries both to the cell; mitochondria respire").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Carbon dioxide to lungs; urea to kidneys; always via the blood").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Sprinting for a Taxi: Systems in Action
        self.next_band(2)
        b2_title = Tex("Sprinting for a taxi").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Nervous system decides; muscles pull on bones").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Heart rate: about 70 to about 150 beats per minute").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Breathing: about 15 to about 40 breaths per minute").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Sweat and flushed skin keep the body near 37 degrees").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Keeping Conditions Steady and the Error Museum
        self.next_band(3)
        b3_title = Tex("Steady conditions; failure spreads").scale(1.0).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Systems cooperate to hold temperature, glucose and water steady").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Asthma: less oxygen in blood, so muscles tire").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Kidney failure: urea builds up; dialysis filters the blood").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Explain A affects B: name what A supplies to B").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Keeping Conditions Steady and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``The lungs give oxygen straight to the muscles''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Digestion happens only in the stomach''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The heart makes blood''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``The excretory system removes faeces''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Body Is a Taxi Rank
        self.next_band(5)
        b5_title = Tex("The body is a taxi rank").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Food stall = digestive; petrol pump = respiratory").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Taxis = circulatory; cleaners = excretory").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Marshal = nervous; frames and drivers = musculoskeletal").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Nobody at the rank works alone: integrated").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Follow One Vetkoek and One Breath
        self.next_band(6)
        b6_title = Tex("One vetkoek and one breath").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Mouth, stomach, small intestine: glucose into blood").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Lungs: oxygen into blood").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Blood to leg: glucose + oxygen gives carbon dioxide + water + energy").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Carbon dioxide back to lungs; urea to kidneys. Never skip the blood.").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): When One Department Goes on Strike
        self.next_band(7)
        b7_title = Tex("When one department strikes").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Asthma: less oxygen, blood carries less, muscles tire").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Kidneys fail: urea builds up in every cell").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Sprint: heart 70 to 150, breathing 15 to 40, sweat at 37").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Linking answer = the chain: system, supply, cell").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
