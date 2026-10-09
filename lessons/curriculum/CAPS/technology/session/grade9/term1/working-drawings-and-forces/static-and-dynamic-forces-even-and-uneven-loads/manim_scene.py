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

# Band-layout whiteboard scene for static-and-dynamic-forces-even-and-uneven-loads (Part 1 Expert
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


class StaticAndDynamicForcesEvenAndUnevenLoadsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Static Loads: Weight That Stays Put
        self.write_rows(0, "Static Loads: Weight That Stays Put", [
            "Static: does not change with time",
            "Dead load: slab ~3 100 kg",
            "Live but steady: parked chair, trolley",
            "Predictable; check the ground",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Dynamic Loads: Forces That Move and Change
        self.next_band(1)
        self.write_rows(1, "Dynamic Loads: Forces That Move and Change", [
            "Dynamic: moves, sudden, repeats",
            "Impact: jump = 3 to 4 x weight",
            "Fatigue: thousands of footsteps",
            "Thick treads, deep posts, nosings",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Even and Uneven Loads on Stairs, Ramps and Landings
        self.next_band(2)
        self.write_rows(2, "Even and Uneven Loads on Stairs, Ramps and Landings", [
            "Even: spread, everyone shares",
            "Uneven: wheels, kerb hit, bunched crowd",
            "Hollow + wheel = cracked slab",
            "Turning: tip a landing, lever a post",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Dead load only''",
            "``Running crowd = standing crowd''",
            "``Wheels treated as spread load''",
            "``Rail built for weight, not push''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Standing Still Versus Moving
        self.next_band(4)
        self.write_rows(4, "Standing Still Versus Moving", [
            "Still weight",
            "Slab: 3 tonnes always",
            "Parked chair, stacked chairs",
            "Easy to add up",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Why a Crowd on the Stairs Is Different
        self.next_band(5)
        self.write_rows(5, "Why a Crowd on the Stairs Is Different", [
            "Running crowd, jump, lean, wind",
            "Moving hits harder",
            "Repeats crack slowly",
            "Mesh, deep posts, strong rails",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Spread Out or Bunched Up
        self.next_band(6)
        self.write_rows(6, "Spread Out or Bunched Up", [
            "Spread: slab on fill, full landing",
            "Bunched: four wheels, one spot",
            "Washed-out hollow is the danger",
            "One side loaded tips",
        ], scale=0.9, box=2)

        last = Tex("Static loads stay, dynamic loads hit and repeat, even loads share and uneven loads concentrate: the slab, mesh, posts and rails are designed for all four.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
