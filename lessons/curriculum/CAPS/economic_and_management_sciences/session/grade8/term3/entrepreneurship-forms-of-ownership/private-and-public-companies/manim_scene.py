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

# Band-layout whiteboard scene for private-and-public-companies (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (260/190/190/150/190/120/150 of 1250 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class PrivateAndPublicCompaniesSession(MovingCameraScene):
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
        self.write_rows(0, "What a company is", [
            "Incorporated with CIPC under the 2008 Act",
            "Separate legal person",
            "Limited liability and continuity",
            "Shareholders own, directors manage",
        ], box=1)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Private company", [
            "(Pty) Ltd, at least one director",
            "No shares offered to the public",
            "Transfer of shares restricted",
            "Company tax: 27\\%",
        ], box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Public company", [
            "Ltd, at least three directors",
            "Shares offered via a prospectus",
            "Often listed on the JSE",
            "Audited statements and an AGM",
        ], box=2)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Shares in numbers", [
            "R100 000 / 1 000 shares = R100 a share",
            "300 shares earn R30 000",
            "100 shares at R50: max loss R5 000",
            "Sold at R80: gain R3 000",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Other kinds of companies", [
            "Inc: directors share liability",
            "SOC Ltd: owned by the state",
            "NPC: surplus used for its purpose",
            "Co-operative: one member, one vote",
        ], box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "The bakery becomes a person", [
            "Soweto Bakes (Pty) Ltd",
            "Company owns and owes",
            "Owners risk only their investment",
            "Carries on if one retires",
        ], box=2)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Selling slices to the public", [
            "Ltd: shares sold to anyone",
            "Raise huge amounts of capital",
            "Stricter rules, public results",
            "Dividends and share growth",
        ], box=1)

        self.wait(4)
