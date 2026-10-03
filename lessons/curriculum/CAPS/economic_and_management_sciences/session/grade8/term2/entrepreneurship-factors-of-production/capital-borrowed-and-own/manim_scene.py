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

# Band-layout whiteboard scene for capital-borrowed-and-own (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (270/160/170/190/150/150/190 of 1280 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CapitalBorrowedAndOwnSession(MovingCameraScene):
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
        self.write_rows(0, "Factors of production", [
            "Natural resources: rent",
            "Labour: wages and salaries",
            "Capital: interest",
            "Entrepreneurship: profit (not guaranteed)",
        ], box=3)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "What capital means", [
            "Physical capital: man-made, used to produce",
            "Fixed: trailer, machine; working: stock, wages",
            "Financial capital: money to acquire them",
            "Capital multiplies labour's productivity",
        ], box=1)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Own capital", [
            "Savings, family contributions, retained profit",
            "No repayment, no interest, full control",
            "Limited; savings at risk",
            "Opportunity cost: interest given up",
        ], box=3)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Borrowed capital", [
            "Loans, overdrafts, finance, trade credit",
            "Interest and instalments regardless of profit",
            "Collateral may be lost",
            "R60 000 x 12\\% = R7 200 a year",
        ], box=3)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Choosing the mix", [
            "Gearing: borrowed vs own",
            "R60 000 of R100 000 = 60\\% debt",
            "Higher gearing: more reward, more risk",
            "Borrow only what income can repay",
        ], box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "The coffee trailer", [
            "Spot and beans: natural resources",
            "Barista: labour",
            "Trailer and money: capital",
            "Owner: entrepreneurship",
        ], box=3)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "My money or borrowed money", [
            "Own: R30 000 savings + R10 000 gift",
            "Borrowed: R60 000 at 12\\%",
            "Supplier: 30 days trade credit",
            "Compare the total cost",
        ], box=3)

        self.wait(4)
