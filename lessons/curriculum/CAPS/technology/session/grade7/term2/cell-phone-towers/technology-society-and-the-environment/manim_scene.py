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

# Band-layout whiteboard scene for technology-society-and-the-environment (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/180/180/110/110/110 of 930 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TechnologySocietyAndTheEnvironmentSession(MovingCameraScene):
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
        self.wait(47)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Finding out what society needs
        self.write_rows(0, "Finding out what society needs", [
            "Ask the people who have the need",
            "Surveys, meetings, data, local leaders",
            "Phones beat landlines; prepaid airtime",
            "Suburb and village need different towers",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Impact on society
        self.next_band(1)
        self.write_rows(1, "Impact on society", [
            "Good: ambulance, school, money, cards, warnings",
            "Bad: view, fears, screens, scams, theft",
            "Uneven: over the hill, the digital divide",
            "Design shrinks the bad: solar, disguise, share",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Impact on the environment
        self.next_band(2)
        self.write_rows(2, "Impact on the environment", [
            "Before: steel, concrete, roads",
            "During: electricity, diesel, lights, guy wires",
            "After: batteries and e-waste",
            "Share, solar, shield, mark, recycle",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Technology itself is neutral''",
            "``List only the benefits''",
            "``Fears are just ignorance''",
            "``The environment is someone else's problem''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Asking people what they need
        self.next_band(4)
        self.write_rows(4, "Asking people what they need", [
            "Where, what for, what can you pay",
            "Towers cheaper than wires",
            "Needs become the brief",
            "City short and hidden; village tall and solar",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Who wins and who loses
        self.next_band(5)
        self.write_rows(5, "Who wins and who loses", [
            "Clinic, school, shop, farmer",
            "View, worry, screens, theft",
            "Over the hill: no signal",
            "Shrink the bad by design",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): What nature pays
        self.next_band(6)
        self.write_rows(6, "What nature pays", [
            "Mine, smelt, pour, truck",
            "Power, diesel, lights, wires",
            "Batteries and old phones",
            "List both sides, improve the balance",
        ], scale=0.9, box=3)

        last = Tex("Find the need by asking, list the good and the bad for everyone affected, and design for a better balance.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
