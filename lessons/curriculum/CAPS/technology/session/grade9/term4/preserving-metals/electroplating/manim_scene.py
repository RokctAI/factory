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

# Band-layout whiteboard scene for electroplating (Part 1 Expert
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


class ElectroplatingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What Electroplating Is and Where It Is Used
        self.write_rows(0, "What Electroplating Is and Where It Is Used", [
            "Thin metal coat by electric current",
            "Chrome, nickel, gold, zinc, tin, silver",
            "Reasons: preserve, appearance, properties",
            "Small bright objects; thin coat scratches through",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): The Electroplating Cell: Anode, Cathode, Electrolyte and Current
        self.next_band(1)
        self.write_rows(1, "The Electroplating Cell: Anode, Cathode, Electrolyte and Current", [
            "Electrolyte: salt of coating metal",
            "Anode: coating metal on +; cathode: object on -",
            "Ions to cathode, deposit; anode dissolves",
            "Rules: clean, low steady current, face the anode",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): The Practical Investigation: Copper Plating a Key
        self.next_band(2)
        self.write_rows(2, "The Practical Investigation: Copper Plating a Key", [
            "Kit: jar, copper sulphate, copper strip, key, 3-4.5 V",
            "Safety: gloves, glasses, wash, keep solution",
            "Sand, wash, do not touch; wire; pink in minutes",
            "Record; reverse leads: no plating; damp test",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Cleaned key handled with fingers''",
            "``Leads reversed so the key loses metal''",
            "``Too many cells giving a dark powdery coat''",
            "``Key and copper strip touching, shorting the cell''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Metal Coat Put On by Electricity
        self.next_band(4)
        self.write_rows(4, "A Metal Coat Put On by Electricity", [
            "Metal coat by electricity",
            "Taps, coins, jewellery, screws, cans",
            "Seal, look good, hard surface",
            "Not for gates and roofs",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Metal Leaves One Side and Lands on the Other
        self.next_band(5)
        self.write_rows(5, "Metal Leaves One Side and Lands on the Other", [
            "Minus gets the metal",
            "Strip shrinks, key gains",
            "More current or time, thicker",
            "Spotless, low, facing",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Clean It, Wire It, Wait
        self.next_band(6)
        self.write_rows(6, "Clean It, Wire It, Wait", [
            "Clean it, wire it, wait",
            "Ten minutes to pink",
            "Swap leads: nothing",
            "Gloves on, hands washed",
        ], scale=0.9, box=0)

        last = Tex("Electroplating moves metal ions from an anode through a salt solution onto a clean object made the cathode, growing a thin protective, decorative coat.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
