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

# Band-layout whiteboard scene for advertising-poster-for-the-device (Part 1 Expert
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


class PosterDesignSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Poster Must Do: Audience, Message and the Ten-Second Test
        self.write_rows(0, "What a Poster Must Do: Audience, Message and the Ten-Second Test", [
            "Audience: elderly, families, in sun, three metres",
            "One message; one action",
            "Ten-second test with strangers",
            "Pretty is not enough",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Designing the Poster: Headline, Image, Benefits, Layout
        self.next_band(1)
        self.write_rows(1, "Designing the Poster: Headline, Image, Benefits, Layout", [
            "Thumbnails, rough, A3",
            "Headline 50 mm; one picture; benefits; action box",
            "Features become benefits",
            "Hierarchy, alignment, contrast, space, consistency",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Honesty, Accessibility and Evaluating the Finished Poster
        self.next_band(2)
        self.write_rows(2, "Honesty, Accessibility and Evaluating the Finished Poster", [
            "Claims true and tested; no fear",
            "'Loud enough', not 'keeps you safe'",
            "Big type; two languages; contrast",
            "Checklist, record, evaluate",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Paragraph instead of headline and benefits''",
            "``Claim the device cannot meet''",
            "``Fear imagery aimed at the elderly''",
            "``Tiny pale English-only type''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Who Is It For, and What Must It Say?
        self.next_band(4)
        self.write_rows(4, "Who Is It For, and What Must It Say?", [
            "Second-language readers",
            "Top-left and centre first",
            "Tear-off or photographable contact",
            "Five messages are none",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Putting It on the Page
        self.next_band(5)
        self.write_rows(5, "Putting It on the Page", [
            "Eye order by size and place",
            "Three-by-four grid",
            "One or two typefaces; three colours",
            "Name once big, once small",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Truthful, Readable, Judged
        self.next_band(6)
        self.write_rows(6, "Truthful, Readable, Judged", [
            "Spec and test record as evidence",
            "Three metres, two metres",
            "Stand out with space, not volume",
            "Brief, diagram, table, poster, evaluation",
        ], scale=0.9, box=3)

        last = Tex("One audience, one message, one action, tested in ten seconds; honest claims from tested specs, large bilingual type, and an evaluated poster that completes the project.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
