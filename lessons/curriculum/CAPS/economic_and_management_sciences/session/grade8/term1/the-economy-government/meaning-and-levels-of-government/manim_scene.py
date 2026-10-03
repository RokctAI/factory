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

# Band-layout whiteboard scene for meaning-and-levels-of-government (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-6). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (300/190/170/200/190/220 of 1270 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class MeaningAndLevelsOfGovernmentSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.78, box=None):
        t = Tex(title).scale(1.1).shift(band_shift(k) + UP * 2.4)
        self.play(Write(t))
        self.wait(1.5)
        made = []
        for i, r in enumerate(rows):
            m = Tex(r).scale(scale).shift(band_shift(k) + UP * (1.3 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.3)
            made.append(m)
        if box is not None:
            self.play(Create(SurroundingRectangle(made[box], color=YELLOW)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1)
        self.write_rows(0, "What government is", [
            "Authority to make, carry out and judge laws",
            "Collects taxes; provides public goods",
            "Public good: non-payers cannot be kept out",
            "Constitution of 1996 is the highest law",
        ], box=1)

        # --- Band 1 (subtopic_1)
        self.next_band(1)
        self.write_rows(1, "Three arms of government", [
            "Legislature makes laws: Parliament",
            "Executive carries them out: President and Cabinet",
            "Judiciary judges: the courts",
            "Separation of powers prevents abuse",
        ], box=3)

        # --- Band 2 (subtopic_2)
        self.next_band(2)
        self.write_rows(2, "Three spheres of government", [
            "National: President and Cabinet",
            "Provincial: 9 provinces, Premier and MECs",
            "Local: municipalities, mayor and councillors",
            "8 metro + 44 district + 205 local = 257",
        ], box=3)

        # --- Band 3 (subtopic_3)
        self.next_band(3)
        self.write_rows(3, "Who does what", [
            "National: SANDF, SAPS, Home Affairs, SASSA, SARS",
            "Provincial: schools, hospitals, provincial roads",
            "Local: water, refuse, streets, lights, rates",
            "Concurrent: shared, e.g. health, housing",
        ], box=3)

        # --- Band 4 (subtopic_4)
        self.next_band(4)
        self.write_rows(4, "Government in the circular flow", [
            "Consumer: buys goods and services (procurement)",
            "Employer: teachers, nurses, police",
            "Producer: education, health, water, roads",
            "Redistributor: taxes in, grants out",
        ], box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5)
        self.next_band(5)
        self.write_rows(5, "One street, three governments", [
            "Police van: national",
            "Clinic and school: provincial",
            "Tap, street light, refuse truck: municipality",
            "You vote for all three",
        ], box=2)

        # --- Band 6 (subtopic_6)
        self.next_band(6)
        self.write_rows(6, "Make, do and judge", [
            "Make: Parliament",
            "Do: President, ministers, departments",
            "Judge: the courts",
            "No player may also be the referee",
        ], box=3)

        self.wait(4)
