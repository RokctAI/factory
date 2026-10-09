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

# Band-layout whiteboard scene for artists-impression-of-a-cam-and-a-crank (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/180/160/120/110/90 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ArtistsImpressionCamCrankSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What an Artist's Impression Is For
        self.write_rows(0, "What an Artist's Impression Is For", [
            "Working drawing: to scale, mm, for the maker",
            "Impression: colour, 3D, for everyone else",
            "Early sketch to judge; late picture to present",
            "PAT shows both",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Colour, Shading and Texture
        self.next_band(1)
        self.write_rows(1, "Colour, Shading and Texture", [
            "Colour: separate parts, hint at material",
            "Shading: one light, top left, pale to dark",
            "Texture: grain, highlight stripe, stipple",
            "Outline, colour, shade, texture, outline",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Drawing the Cam and the Crank
        self.next_band(2)
        self.write_rows(2, "Drawing the Cam and the Crank", [
            "Cam: disc, shaft, follower, arrows",
            "Crank: axle, arm, handle, dashed circle",
            "Highlight stripe on every cylinder",
            "Would a stranger understand it?",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Dimensions belong on the impression''",
            "``Light can change direction halfway''",
            "``Every part a different bright colour''",
            "``Press hard for the first outline''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Picture That Sells the Idea
        self.next_band(4)
        self.write_rows(4, "A Picture That Sells the Idea", [
            "Toy box picture versus instruction sheet",
            "Picture: colour, no sizes",
            "Sheet: sizes, no colour",
            "Show both at the presentation",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Making Flat Shapes Look Solid
        self.next_band(5)
        self.write_rows(5, "Making Flat Shapes Look Solid", [
            "Colour tells parts apart",
            "Light top left, keep it there",
            "Shadow underneath",
            "Wavy lines wood, bright stripe metal",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Your Own Cam and Crank Drawing
        self.next_band(6)
        self.write_rows(6, "Your Own Cam and Crank Drawing", [
            "Cam: colour, shade, shadow, arrows",
            "Crank: grey cylinders, dashed circle",
            "No measurements",
            "Stranger test",
        ], scale=0.9, box=2)

        last = Tex("Colour separates, shading gives form, texture shows material: an artist's impression lets anyone see the design before it is built.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
