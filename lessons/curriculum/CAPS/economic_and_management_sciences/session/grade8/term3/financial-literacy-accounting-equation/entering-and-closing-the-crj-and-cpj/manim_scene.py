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

# Band-layout whiteboard scene for entering-and-closing-the-crj-and-cpj (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (290/190/170/200/160/130/130 of 1270 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class EnteringAndClosingTheCrjAndCpjSession(MovingCameraScene):
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
        self.write_rows(0, "Sort every document", [
            "Money in: CRJ",
            "Money out: CPJ",
            "Bank statement feeds both",
            "Enter each pile in date order",
        ], box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "June receipts", [
            "Capital R15 000: sundry",
            "Combined deposit R2 050",
            "Loan R10 000: sundry",
            "EFT for services: current income",
        ], box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "June payments", [
            "Equipment R6 800: sundry",
            "Wages and fuel: own columns",
            "Drawings and loan repaid: sundry",
            "Bank charges R95: B/S",
        ], box=2)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Closing off both journals", [
            "CRJ: 6 000 + 25 040 = 31 040",
            "CPJ: 3 600 + 1 350 + 9 845 = 14 795",
            "Bank: 31 040 - 14 795 = 16 245",
            "Single line above, double below",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "June in the equation", [
            "Assets +R23 045",
            "OE +R14 045, L +R9 000",
            "Profit R6 040 - R5 495 = R545",
            "Financing is not income",
        ], box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Two notebooks, one bank", [
            "In pile and out pile",
            "Bank lane plus one other lane",
            "Sundry needs a name tag",
            "Loan appears in both",
        ], box=3)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Does June balance?", [
            "Lanes agree in each notebook",
            "Bank left R16 245",
            "R14 045 + R9 000 = R23 045",
            "Profit only R545",
        ], box=2)

        self.wait(4)
