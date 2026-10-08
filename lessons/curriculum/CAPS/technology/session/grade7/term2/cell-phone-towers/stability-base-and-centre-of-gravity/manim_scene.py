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

# Band-layout whiteboard scene for stability-base-and-centre-of-gravity (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/150/160/110/110/110 of 880 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class StabilityBaseAndCentreOfGravitySession(MovingCameraScene):
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
        self.wait(44)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Centre of gravity and the base
        self.write_rows(0, "Centre of gravity and the base", [
            "Centre of gravity: where the weight acts",
            "Stands while its line falls inside the base",
            "Wider base, lower centre, anchoring",
            "Tower: wide feet, steel kept low, bolted down",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Reinforcing the frame
        self.next_band(1)
        self.write_rows(1, "Reinforcing the frame", [
            "Gusset: plate across a joint",
            "Web: plate filling between members",
            "Cross-bracing: X on faces and inside",
            "Reinforce where forces concentrate",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Visual pollution
        self.next_band(2)
        self.write_rows(2, "Visual pollution", [
            "A structure that spoils the view",
            "Siting, slim pole, disguise, sharing, colour",
            "Every answer has a trade-off",
            "Refused tower connects nobody",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Heavy means stable''",
            "``Reinforce everywhere''",
            "``Looks are not a technical problem''",
            "``Disguise is free''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Why things topple
        self.next_band(4)
        self.write_rows(4, "Why things topple", [
            "Balance point: ruler on a finger",
            "Line inside the base: stands",
            "Cone rocks back; broom on its handle falls",
            "Wider, lower, or bolted down",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Strengthening the weak spots
        self.next_band(5)
        self.write_rows(5, "Strengthening the weak spots", [
            "Corners and lowest panels",
            "Gusset at the corner",
            "Web between the bars",
            "X inside so it cannot twist",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Nobody wants to look at it
        self.next_band(6)
        self.write_rows(6, "Nobody wants to look at it", [
            "Neighbours object to the lattice",
            "Hide it, slim it, disguise it, share it",
            "Tree disguise costs and catches wind",
            "Explain the trades honestly",
        ], scale=0.9, box=1)

        last = Tex("Keep the centre of gravity low over a wide anchored base, reinforce the joints, and respect the view.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
