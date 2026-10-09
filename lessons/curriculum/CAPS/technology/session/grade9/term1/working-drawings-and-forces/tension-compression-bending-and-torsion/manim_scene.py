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

# Band-layout whiteboard scene for tension-compression-bending-and-torsion (Part 1 Expert
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


class TensionCompressionBendingAndTorsionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Tension and Compression: Pulling and Pushing Members
        self.write_rows(0, "Tension and Compression: Pulling and Pushing Members", [
            "Tension pulls longer: steel, rope",
            "Compression pushes shorter: concrete, brick",
            "Concrete weak in tension; glass, brick too",
            "Long thin compression members buckle",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Bending in Beams: Both at Once
        self.next_band(1)
        self.write_rows(1, "Bending in Beams: Both at Once", [
            "Beam sags: top compressed, bottom stretched",
            "Neutral axis in the middle",
            "Steel near the tension face: mesh low",
            "Cantilever: tension on top; deeper = stiffer",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Torsion and Cross-Bracing
        self.next_band(2)
        self.write_rows(2, "Torsion and Cross-Bracing", [
            "Torsion: twist about the axis",
            "Tube beats bar for its weight",
            "Rectangle racks; triangle cannot",
            "Knee brace on the rail; posts deep",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Steel in the middle of the slab''",
            "``Concrete is simply strong''",
            "``Solid bar where a tube is better''",
            "``Rectangle with no diagonal''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Stretched or Squashed
        self.next_band(4)
        self.write_rows(4, "Stretched or Squashed", [
            "Pull: steel yes, concrete cracks",
            "Push: concrete yes, thin steel buckles",
            "Paper and chalk test",
            "Each material where it is strong",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): The Top Squashes, the Bottom Stretches
        self.next_band(5)
        self.write_rows(5, "The Top Squashes, the Bottom Stretches", [
            "Plank on bricks sags",
            "Top squashed, bottom stretched",
            "Steel on the stretched side",
            "On edge beats flat",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Twist, and the Diagonal That Stops It
        self.next_band(6)
        self.write_rows(6, "Twist, and the Diagonal That Stops It", [
            "Wring a cloth: torsion",
            "Rails are tubes",
            "One diagonal = two triangles",
            "Brace the rail ends",
        ], scale=0.9, box=2)

        last = Tex("Tension and compression, bending as both at once with steel on the stretched face, and torsion resisted by tubes and triangles: why the slab, steps and rails are detailed as they are.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
