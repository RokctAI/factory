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

# Band-layout whiteboard scene for the Probability: Games, Lotteries and Risk
# session duo. Part 1 — Expert: subtopics 1-4 (language of chance, theory vs
# relative frequency, the lottery, compound events). Part 2 — Simplifier:
# subtopics 5-7 retell the ruler of chance, the lotto arithmetic and the
# two-step tree. Durations 215/215/225/230/195/195/195 of 1470 s.
# Exporter-safe mobjects only; add-only lifecycle; camera moves down one
# band per teaching beat.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ProbabilityGamesLotteriesRiskSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the language of chance ---
        title = Tex("Probability: Games, Lotteries and Risk").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Sample space: spinner sectors 1 to 8").scale(1.0).shift(UP * 1.1)
        b0_l2 = MathTex(r"P(8) = \tfrac{1}{8} \approx 0,13").scale(1.0).shift(UP * 0.2)
        b0_l3 = MathTex(r"P(\text{even}) = \tfrac{4}{8} = 0,5").scale(1.0).shift(DOWN * 0.7)
        b0_l4 = MathTex(r"P(\text{not } 8) = 1 - \tfrac{1}{8} = \tfrac{7}{8}").scale(1.0).shift(DOWN * 1.7)
        b0_l5 = Tex("Counting needs EQUALLY LIKELY outcomes").scale(0.95).shift(DOWN * 2.6)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2)); self.wait(2)
        self.play(Write(b0_l3)); self.wait(2)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b0_l5)); self.wait(3)

        # --- Band 1 (subtopic_2): theory vs relative frequency ---
        self.next_band(1)
        b1_title = Tex("Two honest ways to measure chance").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Theory: fair coin } P(H) = 0,5").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"\text{Observed: } \tfrac{108}{200} = 0,54").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("More trials: frequency drifts to theory").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = MathTex(r"\text{Deliveries: } \tfrac{21}{60} = 0,35 \text{ late}").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        b1_l5 = Tex("No symmetry? Only observation can price it").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b1_l4)); self.wait(2)
        self.play(Write(b1_l5)); self.wait(3)

        # --- Band 2 (subtopic_3): the lottery ---
        self.next_band(2)
        b2_title = Tex("The lottery and other long shots").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"P(\text{jackpot}) = \tfrac{1}{20\;358\;520}").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("One board a week: a win in 400 000 years").scale(0.95).shift(band_shift(2) + UP * 0.2)
        b2_l3 = Tex("Someone wins because millions play").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = Tex("Price, prize, probability: operator profits").scale(0.95).shift(band_shift(2) + DOWN * 1.7)
        b2_l5 = Tex("Insurance: same maths, roles reversed").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2)
        self.play(Write(b2_l2)); self.wait(2)
        self.play(Write(b2_l3)); self.wait(2)
        self.play(Write(b2_l4)); self.wait(2)
        self.play(Write(b2_l5)); self.wait(3)

        # --- Band 3 (subtopic_4): compound events ---
        self.next_band(3)
        b3_title = Tex("Trees and two-way tables").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        # small tree: two forks drawn with lines
        root = band_shift(3) + LEFT * 4.2 + UP * 0.6
        f1a = root + RIGHT * 1.8 + UP * 0.8
        f1b = root + RIGHT * 1.8 + DOWN * 0.8
        self.play(Create(Line(root, f1a)), Create(Line(root, f1b)))
        t_off = MathTex(r"\text{off } 0,4").scale(0.7).shift(f1a + UP * 0.3)
        t_on = MathTex(r"\text{on } 0,6").scale(0.7).shift(f1b + DOWN * 0.3)
        self.play(Write(t_off), Write(t_on))
        self.wait(2)
        b3_l1 = MathTex(r"P(\text{off AND late}) = 0,4 \times 0,5 = 0,20").scale(0.95).shift(band_shift(3) + RIGHT * 1.4 + UP * 0.9)
        b3_l2 = MathTex(r"P(\text{late}) = 0,20 + 0,06 = 0,26").scale(0.95).shift(band_shift(3) + RIGHT * 1.4 + UP * 0.0)
        b3_l3 = MathTex(r"\text{Endpoints: } 0,20 + 0,20 + 0,06 + 0,54 = 1").scale(0.9).shift(band_shift(3) + DOWN * 1.0)
        b3_l4 = MathTex(r"\text{Of the walkers: } \tfrac{18}{45} = 0,4").scale(0.95).shift(band_shift(3) + DOWN * 1.9)
        b3_l5 = Tex("The words choose the denominator").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        self.play(Write(b3_l3)); self.wait(2)
        self.play(Write(b3_l4)); self.wait(2)
        self.play(Write(b3_l5)); self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 4 (subtopic_5): the ruler of chance ---
        self.next_band(4)
        b4_title = Tex("A scale from impossible to certain").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2.5)
        ruler = Line(band_shift(4) + LEFT * 4.0 + UP * 0.6, band_shift(4) + RIGHT * 4.0 + UP * 0.6)
        z = MathTex(r"0").scale(0.8).shift(band_shift(4) + LEFT * 4.0 + UP * 1.1)
        h = MathTex(r"0,5").scale(0.8).shift(band_shift(4) + UP * 1.1)
        o = MathTex(r"1").scale(0.8).shift(band_shift(4) + RIGHT * 4.0 + UP * 1.1)
        self.play(Create(ruler), Write(z), Write(h), Write(o))
        self.wait(2)
        d1 = Dot(band_shift(4) + LEFT * 3.0 + UP * 0.6, color=YELLOW)
        d1_lab = MathTex(r"\tfrac{1}{8}").scale(0.7).shift(band_shift(4) + LEFT * 3.0 + UP * 0.1)
        self.play(Create(d1), Write(d1_lab)); self.wait(2)
        b4_l1 = Tex("Count the ways, count them all, divide").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        b4_l2 = MathTex(r"\text{NOT trick: } P(\text{no 8}) = 1 - \tfrac{1}{8} = \tfrac{7}{8}").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        b4_l3 = Tex("Rain 0,4 means dry 0,6 — done").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l1)); self.wait(3)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(3)
        self.play(Write(b4_l3)); self.wait(3)

        # --- Band 5 (subtopic_6): why the lotto is not a plan ---
        self.next_band(5)
        b5_title = Tex("Why the lotto is not a retirement plan").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2.5)
        b5_l1 = MathTex(r"\tfrac{1}{20\;358\;520}").scale(1.1).shift(band_shift(5) + UP * 1.0)
        b5_l2 = Tex("A ticket for everyone in two provinces; one wins").scale(0.9).shift(band_shift(5) + UP * 0.1)
        b5_l3 = Tex("Winners on TV = millions of losing tickets").scale(0.95).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = Tex("Average ticket returns under half its price").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        b5_l5 = Tex("Insurance: the same machine, protecting you").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(3)
        self.play(Write(b5_l2)); self.wait(3)
        self.play(Write(b5_l3)); self.wait(3)
        self.play(Write(b5_l4)); self.wait(3)
        self.play(Write(b5_l5)); self.wait(3)

        # --- Band 6 (subtopic_7): two steps of chance ---
        self.next_band(6)
        b6_title = Tex("Two steps of chance").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2.5)
        b6_l1 = MathTex(r"\text{AND: multiply along } \; 0,4 \times 0,5 = 0,20").scale(0.95).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\text{OR: add across } \; 0,20 + 0,06 = 0,26").scale(0.95).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"\text{Endpoints sum to 1: } 0,20+0,20+0,06+0,54").scale(0.9).shift(band_shift(6) + DOWN * 0.8)
        b6_l4 = MathTex(r"\text{Of the walkers: } \tfrac{18}{45}, \text{ not } \tfrac{18}{120}").scale(0.95).shift(band_shift(6) + DOWN * 1.8)
        b6_l5 = Tex("Ask: out of WHOM? — then write the fraction").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l1)); self.wait(3)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(3)
        self.play(Write(b6_l3)); self.wait(3)
        self.play(Write(b6_l4)); self.wait(3)
        self.play(Write(b6_l5)); self.wait(4)
