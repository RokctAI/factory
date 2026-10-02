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

# Band-layout whiteboard scene for sole-traders-and-partnerships (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-6). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (270/200/230/270/100/200 of 1270 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SoleTradersAndPartnershipsSession(MovingCameraScene):
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
        self.write_rows(0, "Key ideas", [
            "Legal personality: a separate person in law",
            "Unlimited vs limited liability",
            "Continuity when owners leave",
            "Companies register with CIPC",
        ], box=1)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Sole trader", [
            "One owner, all decisions, all profit",
            "Easy and cheap to start",
            "Unlimited liability, no legal personality",
            "No continuity, limited capital",
        ], box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Partnership", [
            "Two or more partners",
            "Written partnership agreement",
            "Jointly and severally liable",
            "Ends when a partner leaves or dies",
        ], box=2)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Choosing and sharing", [
            "More capital and skills: partnership",
            "Independence: sole trader",
            "R160 000 at 3:5 = R60 000 and R100 000",
            "Equal: R80 000 each",
        ], box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "One baker, one kitchen", [
            "Owns it alone: sole trader",
            "Keeps every rand of profit",
            "Supplier can claim her savings",
            "She stops, it stops",
        ], box=2)

        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Two bakers, one shop", [
            "More money, skills and hands",
            "Profit shared by agreement",
            "Risk shared: either can be claimed",
            "Write it down first",
        ], box=3)

        self.wait(4)
