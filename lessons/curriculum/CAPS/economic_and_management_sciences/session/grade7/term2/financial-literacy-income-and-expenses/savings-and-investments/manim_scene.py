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

# Band-layout whiteboard scene for savings-and-investments (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-5). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (180/200/240/110/110 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SavingsAndInvestmentsSession(MovingCameraScene):
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
        self.write_rows(0, "Saving and investing", [
            "Saving: setting money aside for later",
            "Investing: putting money to work to grow",
            "Short-term goals: save",
            "Long-term goals: invest",
        ], box=1)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Interest and compound growth", [
            "Interest: payment for the use of money",
            "Simple: interest on the original amount",
            "Compound: interest on interest too",
            "Start early, let it grow",
        ], box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Options, risk and return", [
            "Savings account, fixed deposit",
            "Stokvels and burial societies",
            "Unit trusts, shares, property",
            "Higher return, higher risk",
        ], box=3)


        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Early versus late", [
            "Lebo saves R200 a month from age 20",
            "Sam saves R200 a month from age 40",
            "Lebo ends with much more",
            "Interest on interest needs time",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Safe jar and growth jar", [
            "Safe jar: savings account, emergencies",
            "Growth jar: unit trusts, shares, property",
            "Stokvel: save together, build trust",
            "Too good to be true? Walk away",
        ], box=3)

        self.wait(4)
