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

# Band-layout whiteboard scene for balloons-airships-and-modern-air-transport (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/130/180/110/110/110 of 800 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BalloonsAirshipsAndModernAirTransportSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Balloons
        self.write_rows(0, "Balloons", [
            "Hot air is lighter, so it rises",
            "1783: the Montgolfier brothers",
            "Sheep, duck and rooster first",
            "Balloons cannot be steered",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Airships
        self.next_band(1)
        self.write_rows(1, "Airships", [
            "Airship: balloon with engines",
            "1900: Zeppelin's first airship",
            "1937: the Hindenburg fire",
            "Blimps today use helium",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Modern Air Transport
        self.next_band(2)
        self.write_rows(2, "Modern Air Transport", [
            "1934: South African Airways",
            "1952: first jet airliner service",
            "Helicopters hover and rescue",
            "Planes burn a lot of fuel",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Balloons can be steered''",
            "``The first balloon passengers were people''",
            "``Airships replaced aeroplanes''",
            "``Aeroplanes cause no pollution''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Up, Up and Away
        self.next_band(4)
        self.write_rows(4, "Up, Up and Away", [
            "Hot air",
            "Rises",
            "1783",
            "Wind",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Balloons With Engines
        self.next_band(5)
        self.write_rows(5, "Balloons With Engines", [
            "Airship",
            "Engines",
            "Steered",
            "Hindenburg",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Jets and Helicopters
        self.next_band(6)
        self.write_rows(6, "Jets and Helicopters", [
            "Jets",
            "Helicopters",
            "Air ambulances",
            "Airports",
        ], scale=0.9, box=0)

        last = Tex("From balloons to airships to jets, air transport now carries people and goods across the world in hours.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
