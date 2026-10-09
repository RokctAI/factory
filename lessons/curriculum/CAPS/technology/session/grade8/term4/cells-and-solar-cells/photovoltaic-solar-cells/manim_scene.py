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

# Band-layout whiteboard scene for photovoltaic-solar-cells (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/160/120/110/90 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SolarCellsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.15).shift(band_shift(k) + UP * 2.4)
        self.play(Write(t))
        self.wait(1.5)
        made = []
        for i, r in enumerate(rows):
            m = Tex(r).scale(scale).shift(band_shift(k) + UP * (1.3 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.3)
            made.append(m)
        if box is not None:
            self.play(Create(SurroundingRectangle(made[box], color=box_color)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(42)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): How a Photovoltaic Cell Turns Sunlight Into Electricity
        self.write_rows(0, "How a Photovoltaic Cell Turns Sunlight Into Electricity", [
            "Light frees electrons; junction push",
            "Half a volt a cell; series into panels",
            "400 watts; four to six times a day",
            "Shade, dust, heat, angle cut output",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Panels, Batteries and Inverters: Solar in Use
        self.next_band(1)
        self.write_rows(1, "Panels, Batteries and Inverters: Solar in Use", [
            "Panel, controller, battery, inverter",
            "Controller protects the battery",
            "Cloud: battery covers; night: battery carries",
            "Rainy run: fridge off, then lights",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Advantages and Disadvantages of Solar Cells
        self.next_band(2)
        self.write_rows(2, "Advantages and Disadvantages of Solar Cells", [
            "For: free, clean, durable, anywhere, cheap",
            "Against: night, winter, storage cost",
            "Against: up-front, materials, land",
            "Verdict: cheapest and cleanest, never alone",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``'Solar is free'''",
            "``Load shedding blamed on the panel''",
            "``No environmental cost claimed''",
            "``Only advantages given''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Light In, Current Out
        self.next_band(4)
        self.write_rows(4, "Light In, Current Out", [
            "Twenty percent efficiency",
            "Hot panel: slightly less",
            "Nothing consumed; stops harmlessly",
            "Weakest cell rules the string",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): From Cell to Rooftop
        self.next_band(5)
        self.write_rows(5, "From Cell to Rooftop", [
            "Size the parts together",
            "Farm: grid absorbs by day",
            "Batteries added for evening peak",
            "Rooftop surged with load shedding",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): The Case For and Against
        self.next_band(6)
        self.write_rows(6, "The Case For and Against", [
            "Energy debt repaid in one to two years",
            "Lithium, cobalt: mining and labour",
            "Evening peak is the gap",
            "Solar is not free",
        ], scale=0.9, box=2)

        last = Tex("Sunlight frees electrons in silicon; panels, batteries and inverters make it useful; and solar is our cheapest, cleanest new power, with storage, cost and materials as its honest limits.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
