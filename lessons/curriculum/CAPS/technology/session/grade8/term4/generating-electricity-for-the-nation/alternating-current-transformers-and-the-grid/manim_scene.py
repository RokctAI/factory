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

# Band-layout whiteboard scene for alternating-current-transformers-and-the-grid (Part 1 Expert
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


class GridTransformersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Alternating Current: Why the Grid Uses AC, Not DC
        self.write_rows(0, "Alternating Current: Why the Grid Uses AC, Not DC", [
            "DC one way; AC swings at 50 hertz",
            "Generator: field grows, flips, grows",
            "Losses rise with current squared",
            "High volts, low amps, low loss",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Step-Up and Step-Down Transformers
        self.next_band(1)
        self.write_rows(1, "Step-Up and Step-Down Transformers", [
            "Two coils, one iron core",
            "Turns ratio = volts ratio",
            "Step-up at station; step-down to 230",
            "Volts up, amps down; AC only",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): The National Grid: From Power Station to Plug
        self.next_band(2)
        self.write_rows(2, "The National Grid: From Power Station to Plug", [
            "20 kV to 275/400 kV; 765 kV highest",
            "Pylons: three phases plus shield wire",
            "132, 88, 11, 22 kV, then 230 or 400",
            "50 hertz balance; load shedding protects it",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``High voltage called 'stronger'''",
            "``Transformer making more power''",
            "``Transformer drawn on a battery''",
            "``Load shedding as an empty tank''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Current That Swings
        self.next_band(4)
        self.write_rows(4, "Current That Swings", [
            "Peak 325, equivalent 230",
            "3000 rpm gives 50 hertz",
            "Flicker 100 times a second",
            "Early systems ran DC",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Volts Up, Volts Down
        self.next_band(5)
        self.write_rows(5, "Volts Up, Volts Down", [
            "Oil and fins for cooling",
            "Symbol: two coils, core lines",
            "Charger: 230 to 5 volts",
            "Energy conserved, few percent lost",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): The Wires Across the Country
        self.next_band(6)
        self.write_rows(6, "The Wires Across the Country", [
            "Houses single-phase; factories three-phase",
            "National Transmission Company",
            "Blackout takes days",
            "Not 'stronger': less loss",
        ], scale=0.9, box=3)

        last = Tex("AC swings so transformers can lift it for the journey and drop it for the house; the national grid carries it across the country, balanced at 50 hertz.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
