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

# Band-layout whiteboard scene for building-the-working-model-safely (Part 1 Expert
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


class BuildingTheWorkingModelSafelySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Planning the Build: Parts, Tools, Order and Safety Rules
        self.write_rows(0, "Planning the Build: Parts, Tools, Order and Safety Rules", [
            "Lay out parts by balloon number; tick the list",
            "Pin up circuit, exploded view, orthographic",
            "Order: empty box, board tested, fit, close, label",
            "Safety: glasses, iron in stand, cut away, clamp, hair back",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Soldering and Assembling the Circuit Neatly
        self.next_band(1)
        self.write_rows(1, "Soldering and Assembling the Circuit Neatly", [
            "Tin tip; lead and pad together 2 s; solder to joint",
            "Good: bright, smooth volcano; dry: dull, lumpy, ball",
            "Polarity first: LED, capacitor, transistor, buzzer",
            "Cut strip board tracks; test board before boxing",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Fitting the Enclosure, Testing to Scale and Finishing
        self.next_band(2)
        self.write_rows(2, "Fitting the Enclosure, Testing to Scale and Finishing", [
            "Mark from drawing; start small; drill to size; grommet",
            "Holder fixed; board on spacers; lid wires with slack",
            "To scale: measure against the drawing",
            "Test each spec outdoors as specified; record; clean up",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Box drilled with the circuit inside''",
            "``Dry joint that passes the eye''",
            "``Strip board track left uncut''",
            "``Box closed without testing or recording''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Lay It All Out First
        self.next_band(4)
        self.write_rows(4, "Lay It All Out First", [
            "Tick every part",
            "Drawings on the wall",
            "Box, board, fit, close",
            "Anyone can call stop",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Hot Iron, Steady Hands, Clean Joints
        self.next_band(5)
        self.write_rows(5, "Hot Iron, Steady Hands, Clean Joints", [
            "Two seconds, feed the joint",
            "Shiny is good",
            "Long leg, stripe, flat face, plus",
            "Uncut track is fault number one",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Does It Match the Drawing and Do the Job?
        self.next_band(6)
        self.write_rows(6, "Does It Match the Drawing and Do the Job?", [
            "Small bit first",
            "No rattles, some slack",
            "Ruler against the drawing",
            "Pass or fail by number",
        ], scale=0.9, box=3)

        last = Tex("Build in order to the drawings, solder bright joints with polarity checked, keep every safety rule, and test the finished model against each specification.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
