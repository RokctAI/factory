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

# Band-layout whiteboard scene for physical-causes-of-illness-and-spiritual-healing (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/160/130/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PhysicalCausesOfIllnessAndSpiritualHealingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Physical and Spiritual Causes of Illness
        self.write_rows(0, "Physical and Spiritual Causes of Illness", [
            "Physical causes: injury, food",
            "Dirty water and infections",
            "Spiritual causes: ancestors",
            "The whole person in balance",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Kinds of Healers and Spiritual Healing
        self.next_band(1)
        self.write_rows(1, "Kinds of Healers and Spiritual Healing", [
            "Herbalist: inyanga, ixhwele",
            "Diviner: isangoma, igqirha",
            "Bones, dreams, ceremonies",
            "San trance dances",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Indigenous Healing Today
        self.next_band(2)
        self.write_rows(2, "Indigenous Healing Today", [
            "Many use both kinds",
            "Recognised by law, 2007",
            "Healers refer to clinics",
            "Care with remedies",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Only spirits''",
            "``All healers are the same''",
            "``Traditional healing is illegal''",
            "``Choose only one kind''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Body and Spirit
        self.next_band(4)
        self.write_rows(4, "Body and Spirit", [
            "Body",
            "Mind",
            "Family",
            "Ancestors",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Herbalists and Diviners
        self.next_band(5)
        self.write_rows(5, "Herbalists and Diviners", [
            "Herbs",
            "Bones",
            "Dreams",
            "Dance",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Side by Side
        self.next_band(6)
        self.write_rows(6, "Side by Side", [
            "Law",
            "Clinic",
            "Both",
            "Respect",
        ], scale=0.9, box=2)

        last = Tex("Indigenous healing cares for the whole person, body and spirit, and today it works side by side with clinics and hospitals.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
