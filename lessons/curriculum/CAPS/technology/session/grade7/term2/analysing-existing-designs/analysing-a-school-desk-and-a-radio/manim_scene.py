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

# Band-layout whiteboard scene for analysing-a-school-desk-and-a-radio (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/190/150/110/110/110 of 940 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AnalysingASchoolDeskAndARadioSession(MovingCameraScene):
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
        self.wait(46)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Examining the school desk
        self.write_rows(0, "Examining the school desk", [
            "List features first: tube, slope, laminate, shelf",
            "Why each: cheap, ergonomic, cleanable, stable",
            "Who: learner 11-14; who pays: department",
            "Weaknesses count; then write the brief",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Radio and phone
        self.next_band(1)
        self.write_rows(1, "Radio and phone", [
            "Radio: aerial, dial, batteries, grille, strap",
            "Phone: screen, keypad, camera, SIM, torch",
            "Users without mains power, little money",
            "Simple, cheap, battery life; brief follows",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Why analyse existing designs
        self.next_band(2)
        self.write_rows(2, "Why analyse existing designs", [
            "Part of the investigate step",
            "List, explain, evaluate, reconstruct the brief",
            "Shows the compromises made",
            "Builds the habit of noticing",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Describe looks instead of features and purposes''",
            "``Praise without a weakness''",
            "``Brief that describes the product, not the need''",
            "``Forget who pays''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Taking the desk apart
        self.next_band(4)
        self.write_rows(4, "Taking the desk apart", [
            "Tubes, slope, laminate, shelf, fixed seat",
            "Cheap, easy writing, wipes clean, no theft",
            "Tall learner squashed, frame rusts",
            "Brief: tough, cheap, safe, ten years",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): A radio and a phone
        self.next_band(5)
        self.write_rows(5, "A radio and a phone", [
            "Aerial out for signal, in to carry",
            "Batteries where there is no power",
            "Torch for homes without lights",
            "Basic phone: fewer features, lower price",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Why bother
        self.next_band(6)
        self.write_rows(6, "Why bother", [
            "Study the old before designing the new",
            "Four moves every time",
            "Bottle waist, kettle handle, taxi door",
            "Noticing is where design begins",
        ], scale=0.9, box=1)

        last = Tex("Every product answers a brief; list, explain, evaluate, and reconstruct the question it answered.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
