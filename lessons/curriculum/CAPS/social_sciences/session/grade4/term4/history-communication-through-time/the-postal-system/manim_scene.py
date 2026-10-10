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

# Band-layout whiteboard scene for the-postal-system (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/170/140/110/110/110 of 810 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ThePostalSystemSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): How the Post Began
        self.write_rows(0, "How the Post Began", [
            "1500: a letter in a shoe",
            "Post office stones at the Cape",
            "1792: first post office",
            "1911: first airmail",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Stamps, Addresses and Sorting
        self.next_band(1)
        self.write_rows(1, "Stamps, Addresses and Sorting", [
            "1840: Penny Black stamp",
            "1853: Cape triangle stamps",
            "Name, address, postal code",
            "Sorting and delivery",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): The Post Today
        self.next_band(2)
        self.write_rows(2, "The Post Today", [
            "Fewer letters, more email",
            "Parcels and documents",
            "Courier companies",
            "Letters are history sources",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The post always used stamps''",
            "``Letters always went by aeroplane''",
            "``A postal code is a phone number''",
            "``Nobody uses the post today''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Shoes and Stones
        self.next_band(4)
        self.write_rows(4, "Shoes and Stones", [
            "Shoe in a tree",
            "Post office stones",
            "1792",
            "Runners",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Stamp It
        self.next_band(5)
        self.write_rows(5, "Stamp It", [
            "Stamp",
            "Address",
            "Postal code",
            "Sorting",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Post Now
        self.next_band(6)
        self.write_rows(6, "Post Now", [
            "Email",
            "Parcels",
            "Couriers",
            "Cards",
        ], scale=0.9, box=0)

        last = Tex("The postal system grew from a letter in a shoe to a network that carries letters and parcels around the world.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
