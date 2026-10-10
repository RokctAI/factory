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

# Band-layout whiteboard scene for natural-and-human-made-animal-shelters (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/160/170/110/110/110 of 820 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class NaturalAndHumanMadeAnimalSheltersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Shelters Animals Make
        self.write_rows(0, "Shelters Animals Make", [
            "Natural shelters: made by animals",
            "Weaver nests of grass",
            "Snail and tortoise shells",
            "Wasps: paper from chewed wood",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Shelters People Make for Animals
        self.next_band(1)
        self.write_rows(1, "Shelters People Make for Animals", [
            "Human-made: built by people",
            "Kennel for a dog",
            "Kraal for cattle, goats, sheep",
            "Stable for horses, cage for birds",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): What a Good Shelter Does
        self.next_band(2)
        self.write_rows(2, "What a Good Shelter Does", [
            "Protect from weather",
            "Safe from predators and thieves",
            "Place to rest and raise young",
            "Right size for the animal",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``People built the tortoise's shell''",
            "``A kraal has a roof''",
            "``Wasps make nests from leaves''",
            "``Any size shelter will do''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Nests and Shells
        self.next_band(4)
        self.write_rows(4, "Nests and Shells", [
            "Nests and shells",
            "Grass nests",
            "Mud nests",
            "Shells and hollow trees",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Kennels and Kraals
        self.next_band(5)
        self.write_rows(5, "Kennels and Kraals", [
            "Kennels and kraals",
            "Kennel: dog",
            "Kraal: cattle",
            "Stable: horses",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Safe, Dry and Warm
        self.next_band(6)
        self.write_rows(6, "Safe, Dry and Warm", [
            "Safe, dry and warm",
            "Keeps off weather",
            "Keeps out danger",
            "Fits the animal",
        ], scale=0.9, box=0)

        last = Tex("Animals make natural shelters, people make human-made shelters, and both keep animals safe and dry.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
