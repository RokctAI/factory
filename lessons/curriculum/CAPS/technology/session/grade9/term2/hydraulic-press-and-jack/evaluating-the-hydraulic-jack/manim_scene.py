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

# Band-layout whiteboard scene for evaluating-the-hydraulic-jack (Part 1 Expert
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


class EvaluatingTheHydraulicJackSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): How a Hydraulic Jack Works: Pump, Valves and Ram
        self.write_rows(0, "How a Hydraulic Jack Works: Pump, Valves and Ram", [
            "Ram, pump cylinder, reservoir, two valves",
            "Up-stroke: oil in; down-stroke: oil to ram",
            "Hold: valves closed, oil trapped",
            "Release valve: oil back; overload valve",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Judging the Jack: Fitness for Purpose, Cost and Safety
        self.next_band(1)
        self.write_rows(1, "Judging the Jack: Fitness for Purpose, Cost and Safety", [
            "Fitness: rated load, lift height, test; hard level ground",
            "Cost: between scissor and trolley; lasts decades",
            "Safety: tip, slip, sink, handle; stands, chocks",
            "Wide base, gripping saddle score higher",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Judging the Jack: Aesthetics and Ergonomics
        self.next_band(2)
        self.write_rows(2, "Judging the Jack: Aesthetics and Ergonomics", [
            "Aesthetics: finish and stamped rating signal quality",
            "Ergonomics: long handle, light force, gentle release, light",
            "Table: criterion, observation, judgement, evidence",
            "Verdict + two improvements",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Evaluated by liking, no evidence''",
            "``Safety scored without stands''",
            "``Aesthetics dismissed for a tool''",
            "``Ergonomics confused with aesthetics''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Pump, Hold, Release
        self.next_band(4)
        self.write_rows(4, "Pump, Hold, Release", [
            "Fat ram, thin pump, oil store, doors",
            "Pump, pump, pump",
            "Shuts and holds",
            "Open the valve, down slowly",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Does It Do the Job, Safely, for the Money?
        self.next_band(5)
        self.write_rows(5, "Does It Do the Job, Safely, for the Money?", [
            "Does it lift the car? Check the stamp",
            "Worth it for a workshop",
            "Stand under the car, always",
            "Hazards listed, not hidden",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Looks and Handling
        self.next_band(6)
        self.write_rows(6, "Looks and Handling", [
            "Looks strong and well made",
            "Comfortable to pump and carry",
            "Evidence in every row",
            "Two things to improve",
        ], scale=0.9, box=2)

        last = Tex("A jack pumps oil through one-way valves to a large ram and holds it with the valves closed; evaluate it for purpose, cost, safety, looks and handling with evidence.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
