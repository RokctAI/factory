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

# Band-layout whiteboard scene for government-expenditure (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (260/170/180/160/150/170/180 of 1270 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class GovernmentExpenditureSession(MovingCameraScene):
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
        self.write_rows(0, "How spending is divided", [
            "Current: used up this year (salaries)",
            "Capital: lasts many years (schools, roads)",
            "Transfers: grants, nothing in return",
            "Division of Revenue Act: national, provinces, local",
        ], box=3)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Education and health", [
            "Teachers, no-fee schools, school meals",
            "Universities, TVET, NSFAS",
            "Clinics, hospitals, medicines, HIV treatment",
            "Human capital raises productivity",
        ], box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Housing and social grants", [
            "Subsidised houses, informal settlement upgrades",
            "SASSA grants: child support R560",
            "Older person's, disability, SRD R370",
            "More than 25 million recipients",
        ], box=1)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Transport and security", [
            "Roads, commuter rail, bus subsidies",
            "Police, courts, prisons, defence",
            "Both lower the cost of doing business",
            "Auditor-General checks spending",
        ], box=3)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Choices and calculations", [
            "Opportunity cost: the next best use given up",
            "300 / 1 000 x 100 = 30\\%",
            "R50 billion / 2 million = R25 000 per learner",
            "Interest now rivals health",
        ], box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Follow one rand", [
            "School, clinic, grant",
            "House, road, police",
            "Seventh stop: interest",
            "More for one means less for another",
        ], box=3)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Sharing out the pot", [
            "Education R300 of R1 000: 30\\%",
            "Health R300 of R1 100: about 27\\%",
            "Per learner: R25 000 a year",
            "Minister, Parliament, Auditor-General",
        ], box=1)

        self.wait(4)
