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

# Band-layout whiteboard scene for government-and-households (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (270/150/170/130/200/180/150 of 1250 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class GovernmentAndHouseholdsSession(MovingCameraScene):
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
        self.write_rows(0, "Households and government", [
            "Labour: households to government (real)",
            "Wages and grants: government to households (money)",
            "Services: government to households (real)",
            "Taxes and rates: households to government (money)",
        ], box=1)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Government as consumer", [
            "Buys household labour: employs people",
            "National: police, soldiers, Home Affairs",
            "Provincial: teachers, nurses, doctors",
            "Local: refuse, traffic, water technicians",
        ], box=0)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Government as producer", [
            "National: policing, IDs, grants via SASSA",
            "Provincial: no-fee schools, clinics, housing",
            "Local: water, sanitation, refuse, lights",
            "Free basic water: 6 000 litres a month",
        ], box=2)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "What households owe", [
            "PAYE income tax and 15\\% VAT",
            "Basic foods zero-rated",
            "Pay municipal rates and accounts",
            "Save water, protect property, vote",
        ], box=0)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "The social wage", [
            "Free and subsidised services + grants",
            "Raises living standards of poor households",
            "Grants are means-tested",
            "Paid for by taxes: needs a growing economy",
        ], box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "One household, one month", [
            "Mama's salary: government buys labour",
            "Gogo's grant: a transfer",
            "School, clinic, police, water: services",
            "PAYE and VAT go back to SARS",
        ], box=1)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Two hats and a transfer", [
            "Customer hat: employs and pays salaries",
            "Shop hat: produces services",
            "Transfer: grant, nothing in exchange",
            "Free at the counter, paid by taxes",
        ], box=3)

        self.wait(4)
