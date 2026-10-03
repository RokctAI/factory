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

# Band-layout whiteboard scene for producing-profit-through-manufacturing (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-5). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (180/180/200/90/120 of 770 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ProducingProfitThroughManufacturingSession(MovingCameraScene):
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
        self.write_rows(0, "Manufacturing", [
            "Raw materials turned into products",
            "Value added by labour and skill",
            "Small scale: crafts, food, clothing",
            "Large scale: factories and plants",
        ], box=1)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Costs of production", [
            "Materials: used in each unit",
            "Labour: wages to make the product",
            "Overheads: rent, power, equipment use",
            "Cost per unit = total cost / units made",
        ], box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Pricing and profit", [
            "Selling price above cost per unit",
            "Profit per unit = price - cost",
            "Check customers and competitors",
            "Manufacturing versus trading",
        ], box=1)


        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Naledi's bracelet batch", [
            "Materials R160 + labour R100 + other R40",
            "Total R300 for 20 bracelets",
            "Cost per bracelet: R15",
            "Sells at R30: profit R15 each",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Make it or buy it?", [
            "Trading: buy sweets, resell",
            "Manufacturing: bake muffins, sell",
            "Trading: quicker, smaller mark-up",
            "Manufacturing: more skill, more value",
        ], box=3)

        self.wait(4)
