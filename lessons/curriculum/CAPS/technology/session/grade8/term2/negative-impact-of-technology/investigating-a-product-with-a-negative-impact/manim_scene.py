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

# Band-layout whiteboard scene for investigating-a-product-with-a-negative-impact (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/160/120/110/90 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class NegativeImpactInvestigationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.15).shift(band_shift(k) + UP * 2.4)
        self.play(Write(t))
        self.wait(1.5)
        made = []
        for i, r in enumerate(rows):
            m = Tex(r).scale(scale).shift(band_shift(k) + UP * (1.3 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.3)
            made.append(m)
        if box is not None:
            self.play(Create(SurroundingRectangle(made[box], color=box_color)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(42)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Technology Has Costs as Well as Benefits
        self.write_rows(0, "Technology Has Costs as Well as Benefits", [
            "Costs the designers did not weigh",
            "Environment, society, individual",
            "Phone connects and pollutes; nappy saves and persists",
            "Where, to whom, how much?",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Investigating One Product in Depth
        self.next_band(1)
        self.write_rows(1, "Investigating One Product in Depth", [
            "Describe, trace, ask, gather, judge, record",
            "Raw materials, manufacture, transport, use, disposal",
            "Bottle: oil, energy, trucks, sugar, drains and dumps",
            "Evidence with source and date",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Discussing Solutions That Counteract the Harm
        self.next_band(2)
        self.write_rows(2, "Discussing Solutions That Counteract the Harm", [
            "Material, design, use, end of life, rules, behaviour",
            "Less harm, same benefit, practical here",
            "Deposit scheme yes; ban no",
            "Choose the product and the harm to design against",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Only the disposal stage matters''",
            "``Condemn without weighing benefits''",
            "``One solution is enough''",
            "``Practicality can wait''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Every Gain Has a Price
        self.next_band(4)
        self.write_rows(4, "Every Gain Has a Price", [
            "Solved a problem, made a new one",
            "Earth, people, me",
            "Good and bad held together",
            "Not 'is it bad' but 'where'",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Picking Apart One Product
        self.next_band(5)
        self.write_rows(5, "Picking Apart One Product", [
            "One product, five stages, three questions",
            "Count, photograph, read the label, ask",
            "Say where each fact came from",
            "Sugar inside, litter outside",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): What Could Be Done About It
        self.next_band(6)
        self.write_rows(6, "What Could Be Done About It", [
            "Six kinds of fix",
            "Less harm? Same benefit? Works here?",
            "Deposit works; ban does not",
            "Pick your product",
        ], scale=0.9, box=1)

        last = Tex("Every product has costs to the earth, people and users; trace them through its life, find the worst, and aim a practical fix that keeps the benefit.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
