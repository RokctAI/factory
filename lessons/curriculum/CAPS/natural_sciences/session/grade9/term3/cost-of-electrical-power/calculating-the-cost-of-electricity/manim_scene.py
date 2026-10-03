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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ElectricityCostSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Kilowatt-hour
        title = Tex("The kilowatt-hour").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("We pay for energy, not power").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("1 kWh = 1 kW for 1 hour").scale(0.9).shift(UP * 0.35)
        b0_l3 = MathTex(r"1 \ \mathrm{kWh} = 3\,600\,000 \ \mathrm{J}").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = MathTex(r"E = P \times t = 2 \times 3 = 6 \ \mathrm{kWh}").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Calculating the Cost
        self.next_band(1)
        b1_title = Tex("The three steps").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("1. Power in kW, time in hours").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("2. Energy = kW times hours").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("3. Cost = kWh times price").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = MathTex(r"270 \times R2{,}50 = R675").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Meters, Units and Tariffs
        self.next_band(2)
        b2_title = Tex("Meters and tariffs").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("One unit = 1 kWh").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Prepaid tokens add units").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Tariffs approved by NERSA").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = MathTex(r"200 \div 2{,}50 = 80 \ \mathrm{kWh}").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Comparing Costs and the Error Museum
        self.next_band(3)
        b3_title = Tex("Comparing costs").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("60 W bulb, 180 h: 10,8 kWh, R27").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("9 W LED, 180 h: 1,62 kWh, R4,05").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Saving: R22,95 a month").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Geyser 1 h less a day: R225 a month").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Comparing Costs and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``We pay for watts''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``A kWh is a unit of power''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``100 W for 2 h is 200 kWh''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``30 minutes is 0,3 hours''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Counting Units
        self.next_band(5)
        b5_title = Tex("Counting units").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("We buy energy").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("One unit = 1 kWh").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Units = kilowatts times hours").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("kW is how fast, kWh is how much").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Three-step Cost
        self.next_band(6)
        b6_title = Tex("The three-step cost").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Kettle: 2 kW times 0,5 h = 1 unit").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Geyser: 3 kW times 3 h = 9 units").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Watts to kW: divide by 1 000").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Minutes to hours: divide by 60").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Saving Money at Home
        self.next_band(7)
        b7_title = Tex("Saving money").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Swap to LED bulbs").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Geyser on a timer").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Boil only what you need").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Heating appliances: biggest savings").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l2, color=YELLOW)))
        self.wait(4)
