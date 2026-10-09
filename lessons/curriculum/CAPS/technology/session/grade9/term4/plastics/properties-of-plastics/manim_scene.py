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

# Band-layout whiteboard scene for properties-of-plastics (Part 1 Expert
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


class PropertiesOfPlasticsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Thermoplastics and Thermosets: Two Families
        self.write_rows(0, "Thermoplastics and Thermosets: Two Families", [
            "Polymer: long chain molecules",
            "Thermoplastic: chains slide, remelts, recyclable",
            "Thermoset: cross-linked net, chars, no remelt",
            "Examples: PET, PP, PVC vs Bakelite, melamine",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Properties: Strength, Flexibility, Insulation, Resistance
        self.next_band(1)
        self.write_rows(1, "Properties: Strength, Flexibility, Insulation, Resistance", [
            "Light; strong for mass; tough; flexible",
            "Insulate electricity and heat",
            "Resist water and chemicals; easy to mould",
            "Weak: heat 80 to 200 deg, UV, fire",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Matching Property to Use
        self.next_band(2)
        self.write_rows(2, "Matching Property to Use", [
            "PET bottle: clear, light, holds pressure",
            "LDPE bag flexible; PP chair tough + UV stabiliser",
            "PVC pipe rigid, chemical proof; thermoset plug",
            "Design: need -> properties -> plastic",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``All plastics treated as one material''",
            "``Thermoset expected to melt and remould''",
            "``Plastic called simply weaker than metal''",
            "``Sunlight ignored for an outdoor item''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Softens Again or Sets for Good
        self.next_band(4)
        self.write_rows(4, "Softens Again or Sets for Good", [
            "Chains side by side: softens",
            "Chains in a net: chars",
            "Codes = thermoplastics",
            "Warm a scrap to test",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): What Plastics Are Good At
        self.next_band(5)
        self.write_rows(5, "What Plastics Are Good At", [
            "Float, bend, take a knock",
            "No shock, no heat through",
            "No rust, any shape",
            "Sun and heat weaken",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): The Right Plastic for the Job
        self.next_band(6)
        self.write_rows(6, "The Right Plastic for the Job", [
            "Bottle, bag, chair, pipe",
            "Plug stays hard when hot",
            "Nylon gears, foam boxes",
            "Need first, then plastic",
        ], scale=0.9, box=3)

        last = Tex("Thermoplastics soften and remelt while thermosets set for good, and each plastic is chosen for the job whose demands match its property profile.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
