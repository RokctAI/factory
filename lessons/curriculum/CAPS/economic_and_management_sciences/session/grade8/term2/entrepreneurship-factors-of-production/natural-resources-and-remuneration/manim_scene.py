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

# Band-layout whiteboard scene for natural-resources-and-remuneration (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-6). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (290/170/190/170/140/330 of 1290 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class NaturalResourcesAndRemunerationSession(MovingCameraScene):
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
        self.write_rows(0, "Natural resources", [
            "Gifts of nature: land, soil, water, minerals",
            "Renewable: sun, wind, forests, fish",
            "Non-renewable: coal, gold, oil",
            "SA: rich minerals, scarce water",
        ], box=3)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Using resources sustainably", [
            "Farms: contour ploughing, crop rotation",
            "Mines: rehabilitate land, treat water",
            "Fishing quotas; renewable energy",
            "State custodian: rights and licences",
        ], box=0)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Remuneration of the factors", [
            "Natural resources: rent",
            "Labour: wages and salaries",
            "Capital: interest",
            "Entrepreneurship: profit = 500 000 - 310 000 = 190 000",
        ], box=3)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Remuneration in the circular flow", [
            "Households own the factors",
            "Businesses pay factor income",
            "Households spend in goods markets",
            "Unequal ownership: unequal income",
        ], box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "What nature gives the farm", [
            "Soil, sun, rain, borehole water",
            "Renewable if used carefully",
            "Non-renewable: coal and gold",
            "Sustainable: use today, save tomorrow",
        ], box=3)

        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Splitting the harvest cheque", [
            "Rent R60 000; wages R220 000",
            "Interest R30 000",
            "Profit R190 000 is what is left",
            "Drought: R280 000 - R310 000 = loss R30 000",
        ], box=3)

        self.wait(4)
