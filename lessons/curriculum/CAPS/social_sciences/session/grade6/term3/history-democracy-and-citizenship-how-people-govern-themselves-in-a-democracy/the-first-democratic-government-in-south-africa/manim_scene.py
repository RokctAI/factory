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

# Band-layout whiteboard scene for the-first-democratic-government-in-south-africa (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (220/130/180/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TheFirstDemocraticGovernmentInSouthAfricaSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Mandela Becomes President
        self.write_rows(0, "Mandela Becomes President", [
            "ANC won about 62 percent",
            "9 May: elected by parliament",
            "10 May: sworn in",
            "Union Buildings, Pretoria",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): The Government of National Unity
        self.next_band(1)
        self.write_rows(1, "The Government of National Unity", [
            "Government of National Unity",
            "ANC, National Party, IFP",
            "Mbeki and de Klerk: deputies",
            "Nine new provinces",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Healing and Rebuilding
        self.next_band(2)
        self.write_rows(2, "Healing and Rebuilding", [
            "RDP: houses, water, power",
            "TRC: truth and amnesty",
            "Rugby World Cup, 1995",
            "Mandela stepped down, 1999",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Mandela took power''",
            "``Only the ANC governed''",
            "``All problems were solved''",
            "``The TRC was a prison court''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A New President
        self.next_band(4)
        self.write_rows(4, "A New President", [
            "Election",
            "Mandela",
            "Oath",
            "Pretoria",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Sharing Power
        self.next_band(5)
        self.write_rows(5, "Sharing Power", [
            "ANC",
            "National Party",
            "IFP",
            "Provinces",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Building a New Nation
        self.next_band(6)
        self.write_rows(6, "Building a New Nation", [
            "RDP",
            "TRC",
            "Rugby",
            "1999",
        ], scale=0.9, box=1)

        last = Tex("South Africa's first democratic government brought former enemies together to govern for everyone and began the long work of healing and rebuilding.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
