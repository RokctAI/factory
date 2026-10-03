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

# Band-layout whiteboard scene for government-and-businesses (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (240/170/160/170/210/160/160 of 1270 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class GovernmentAndBusinessesSession(MovingCameraScene):
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
        self.write_rows(0, "Businesses and government", [
            "Goods and services: businesses to government",
            "Payment and subsidies: government to businesses",
            "Infrastructure and services: government to businesses",
            "Taxes: businesses to government",
        ], box=1)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Government as consumer", [
            "Public procurement: buying from businesses",
            "Section 217: fair, equitable, transparent",
            "competitive, cost-effective",
            "Tender: advertise, bid, evaluate, award",
        ], box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Government as producer", [
            "Infrastructure: roads, ports, rail, power",
            "National: CIPC, SARS customs, courts, Reserve Bank",
            "Provincial: roads, educated healthy workers",
            "Local: water, electricity, refuse, zoning",
        ], box=0)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Regulator and tax collector", [
            "Competition, consumer and labour laws",
            "Company tax: 27\\% of taxable income",
            "VAT 15\\%: output tax minus input tax",
            "R3 000 - R1 500 = R1 500 to SARS",
        ], box=3)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Supporting small businesses", [
            "Preference points in tenders, price still first",
            "B-BBEE levels broaden ownership",
            "Finance, mentoring, trading stalls",
            "Pay suppliers within 30 days",
        ], box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "The builder who won the tender", [
            "Province buys classrooms: customer",
            "Road, water, power, courts: producer",
            "Pays company tax, VAT and PAYE",
            "One job, every role",
        ], box=0)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Customer, producer, marshal", [
            "Marshal: fair rules for everyone",
            "Minimum wage, consumer protection",
            "VAT line: R1 million sales a year",
            "Government buys, builds and referees",
        ], box=0)

        self.wait(4)
