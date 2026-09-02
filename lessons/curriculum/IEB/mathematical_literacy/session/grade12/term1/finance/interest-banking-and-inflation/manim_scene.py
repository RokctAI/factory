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

# Band-layout whiteboard scene for the Interest, Banking and Inflation session
# duo. Part 1 — Expert: subtopics 1-4 (simple interest, compound interest,
# bank statement, inflation). Part 2 — Simplifier: subtopics 5-7 retell the
# two workers, the kitchen-table statement and the milk-bottle time machine.
# Durations 215/215/225/230/195/195/195 of 1470 s. Exporter-safe mobjects
# only; add-only lifecycle; camera moves down one band per teaching beat.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class InterestBankingInflationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): simple interest ---
        title = Tex("Interest, Banking and Inflation").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"\text{One year: } 12\;000 \times 0,065 = \text{R780}").scale(1.0).shift(UP * 1.1)
        b0_l2 = Tex("Same R780 every year — original principal only").scale(0.95).shift(UP * 0.2)
        b0_l3 = MathTex(r"\text{3 years: } 12\;000 + 3 \times 780 = 14\;340").scale(1.0).shift(DOWN * 0.7)
        b0_l4 = MathTex(r"12\;000 \times (1 + 0,065 \times 3) = 14\;340").scale(1.0).shift(DOWN * 1.7)
        b0_l5 = Tex("A straight, tilted line on the graph").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2)); self.wait(2)
        self.play(Write(b0_l3)); self.wait(2)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b0_l5)); self.wait(3)

        # --- Band 1 (subtopic_2): compound interest ---
        self.next_band(1)
        b1_title = Tex("Compound: interest earns interest").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"12\;000 \times 1,065 = 12\;780").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"12\;780 \times 1,065 = 13\;610,70").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"13\;610,70 \times 1,065 = 14\;495,40").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = MathTex(r"\text{vs simple } 14\;340: \text{ ahead by } 155,40").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        b1_l5 = MathTex(r"\text{5 years: } 16\;441,04 \text{ vs } 15\;900").scale(1.0).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b1_l4)); self.wait(2)
        self.play(Write(b1_l5)); self.wait(3)

        # --- Band 2 (subtopic_3): the bank statement ---
        self.next_band(2)
        b2_title = Tex("One month, line by line").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Open } 860,40 \;\; +4\;200,00 \to 5\;060,40").scale(0.95).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{Debit order } -329,00 \to 4\;731,40").scale(0.95).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"\text{Cash } -600,00 \;\; \text{fee } -10,50").scale(0.95).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"\text{Admin fee } -5,90 \to \text{close } 4\;115,00").scale(0.95).shift(band_shift(2) + DOWN * 1.6)
        b2_l5 = MathTex(r"\text{Fees: } 10,50 + 5,90 = 16,40").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2)); self.wait(2)
        self.play(Write(b2_l3)); self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b2_l5)); self.wait(3)

        # --- Band 3 (subtopic_4): inflation ---
        self.next_band(3)
        b3_title = Tex("Inflation: the same machine, against you").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"32,00 \times 1,05 = 33,60").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"33,60 \times 1,05 = 35,28").scale(1.05).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex("R200: six bottles today, five in two years").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = MathTex(r"\text{Ten years: } \times 1,63 \;\; \text{R200} \to \text{R122,78}").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = MathTex(r"3\% \text{ raise under } 5\% \text{ inflation: R150 short}").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2)); self.wait(2)
        self.play(Write(b3_l3)); self.wait(2)
        self.play(Write(b3_l4)); self.wait(2)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 4 (subtopic_5): the two ways money grows ---
        self.next_band(4)
        b4_title = Tex("The two ways money grows").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2.5)
        b4_l1 = Tex("Worker one grows only the original pot").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"780, \; 780, \; 780 \to 14\;340").scale(1.05).shift(band_shift(4) + UP * 0.2)
        b4_l3 = Tex("Worker two grows whatever is in the pot").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"780, \; 830,70, \; 884,70 \to 14\;495,40").scale(1.05).shift(band_shift(4) + DOWN * 1.6)
        b4_l5 = Tex("Straight line vs snowball — the gap widens").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l1)); self.wait(3)
        self.play(Write(b4_l2)); self.wait(3)
        self.play(Write(b4_l3)); self.wait(3)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)
        self.play(Write(b4_l5)); self.wait(3)

        # --- Band 5 (subtopic_6): the statement on the kitchen table ---
        self.next_band(5)
        b5_title = Tex("The statement on the kitchen table").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2.5)
        b5_l1 = Tex("Wages in, debit order out, cash out").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("Quiet lines: R10,50 ATM, R5,90 admin").scale(1.0).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"\text{Fees } 16,40 \text{ a month} = 196,80 \text{ a year}").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = MathTex(r"860,40 + 4\;200 - 329 - 600 - 16,40 = 4\;115").scale(0.9).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l1)); self.wait(3)
        self.play(Write(b5_l2)); self.wait(3)
        self.play(Write(b5_l3)); self.wait(3)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3.5)

        # --- Band 6 (subtopic_7): the bottle of milk time machine ---
        self.next_band(6)
        b6_title = Tex("The bottle of milk time machine").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2.5)
        b6_l1 = MathTex(r"32,00 \to 33,60 \to 35,28").scale(1.1).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("The note stands still; its power shrinks").scale(1.0).shift(band_shift(6) + UP * 0.2)
        b6_l3 = Tex("Mattress money melts at 5\\% a year").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = MathTex(r"6,5\% \text{ growth beats } 5\% \text{ inflation}").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        b6_l5 = Tex("An increase below inflation is a pay cut").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l1)); self.wait(3)
        self.play(Write(b6_l2)); self.wait(3)
        self.play(Write(b6_l3)); self.wait(3)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)
        self.play(Write(b6_l5)); self.wait(4)
