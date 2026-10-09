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

# Band-layout whiteboard scene for plastics-in-modern-motor-cars (Part 1 Expert
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


class PlasticsInModernMotorCarsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Case Study: Why a Car Is a Fifth Plastic
        self.write_rows(0, "Case Study: Why a Car Is a Fifth Plastic", [
            "Car: ~10\\% plastic by mass, ~20\\% by volume",
            "100 to 150 kg, 200+ parts; 1950s almost none",
            "Light, formable, tough, insulating, rust-free",
            "Steel stays: body, chassis, engine, suspension",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Where the Plastics Are: Bumper, Dash, Tank, Lights
        self.next_band(1)
        self.write_rows(1, "Where the Plastics Are: Bumper, Dash, Tank, Lights", [
            "Outside: PP bumpers, ABS trim, PC lenses",
            "Inside: PP/ABS dash skeleton, skin over PU foam",
            "Under: blow-moulded HDPE tank, nylon intake",
            "Wiring PVC, nylon connectors, PP battery case",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Safety, Fuel and Recycling at End of Life
        self.next_band(2)
        self.write_rows(2, "Safety, Fuel and Recycling at End of Life", [
            "Safety: padding, no shards, shorter stops",
            "10\\% less mass = 5 to 7\\% less fuel",
            "End of life: mixed, painted, glued; landfill",
            "Fix: codes, clips, fewer polymers, recycled",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Car body called plastic because of bumpers''",
            "``Fuel tank assumed to be steel''",
            "``All scrapped car plastic assumed recycled''",
            "``Fuel saving from lightness forgotten''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Car Full of Plastic
        self.next_band(4)
        self.write_rows(4, "A Car Full of Plastic", [
            "A tenth by weight",
            "Why: light, moulded, no rust",
            "Loads stay steel",
            "Fuel saved",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Part by Part
        self.next_band(5)
        self.write_rows(5, "Part by Part", [
            "Bumpers and lenses",
            "Dash over foam",
            "Plastic fuel tank",
            "Nylon takes the heat",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Lighter, Safer, and Then What
        self.next_band(6)
        self.write_rows(6, "Lighter, Safer, and Then What", [
            "Safer inside",
            "Less fuel",
            "Hard to sort at the end",
            "Label and clip",
        ], scale=0.9, box=2)

        last = Tex("Plastics make up a tenth of a modern car by mass, chosen part by part for lightness, formability and toughness, and their mixed end-of-life recycling is the problem designers now solve with codes and clips.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
