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
# removed. Write-only reveals on single-string Tex keep the export to the
# allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (210/220/220/230/190/190/180 of
# 1440 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EconomicSystemsOriginsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Basic Economic Problem and the Three Questions
        b0_title = Tex("Scarcity and the three questions").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Wants unlimited, resources scarce").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("What to produce?").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("How to produce?").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("For whom to produce?").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Planned Economy and Its Origins
        self.next_band(1)
        b1_title = Tex("The planned economy").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("State owns the factors of production").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Central plan decides; state sets prices").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Marx and Engels, 1848").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Soviet Union from 1917; today North Korea").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The Market Economy and Its Origins
        self.next_band(2)
        b2_title = Tex("The market economy").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Private ownership of resources").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Consumers and businesses decide").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Prices: demand and supply").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Adam Smith, 1776: the invisible hand").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): The Mixed Economy and South Africa's System
        self.next_band(3)
        b3_title = Tex("The mixed economy").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Private sector plus the state").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Grew after the 1930s depression").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("SA: Eskom, Transnet, schools, grants").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Rules: minimum wage, Competition Commission").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): The Mixed Economy and South Africa's System
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Mixed means fifty-fifty''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Market economies have no government''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The Soviet Union invented the idea''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Rich countries have no scarcity''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Who Decides? The School Tuck Shop Test
        self.next_band(5)
        b5_title = Tex("Who decides at the tuck shop?").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Principal decides: planned").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Learners' money decides: market").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Both decide: mixed").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("R10 on chips: the juice is the cost").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Three Ways to Run a Village
        self.next_band(6)
        b6_title = Tex("Three villages").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Council owns and shares: planned").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Families sell at market: market").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Market plus tax for clinic: mixed").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Most countries today are mixed").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Where South Africa Sits on the Line
        self.next_band(7)
        b7_title = Tex("South Africa on the line").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Planned ---------- Market").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("North Korea left, United States right").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("South Africa in the middle").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Ask: who owns it, who sets the price?").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(4)
