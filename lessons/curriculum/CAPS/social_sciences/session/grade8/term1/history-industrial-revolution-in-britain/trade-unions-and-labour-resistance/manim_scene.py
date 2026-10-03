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

# Band-layout whiteboard scene for trade-unions-and-labour-resistance (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (300/300/290/270/150/150/150 of 1610 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TradeUnionsAndLabourResistanceSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.1).shift(band_shift(k) + UP * 2.4)
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0: Early resistance
        self.write_rows(0, "Early resistance", [
            "Luddites 1811 to 1816: smashed wage-cutting machines",
            "1812: machine-breaking made a capital crime",
            "Peterloo, 16 August 1819: about 60 000 people",
            "About 18 killed; the Six Acts followed",
        ], scale=0.8, box=0)
        # --- Band 1: Building unions
        self.next_band(1)
        self.write_rows(1, "Building unions", [
            "1799 and 1800: Combination Acts ban unions",
            "1824: Combination Acts repealed",
            "1834: Tolpuddle Martyrs transported",
            "1836: pardoned after a petition of about 800 000",
        ], scale=0.86, box=2)
        # --- Band 2: Chartism
        self.next_band(2)
        self.write_rows(2, "Chartism", [
            "1838: the People's Charter, six points",
            "Votes for men over 21; secret ballot",
            "Petitions 1839, 1842, 1848 rejected",
            "Five of six points later became law",
        ], scale=0.86, box=3)
        # --- Band 3: New unions and legacy
        self.next_band(3)
        self.write_rows(3, "New unions and legacy", [
            "1851 engineers; 1868 TUC; 1871 Trade Union Act",
            "1888 matchgirls; 1889 dockers' tanner",
            "South Africa: ICU 1919; COSATU 1985",
            "Constitution section 23: right to join a union",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Machine breakers and a massacre
        self.next_band(4)
        self.write_rows(4, "Machine breakers and a massacre", [
            "Hammers against wage-cutting machines",
            "A peaceful crowd in Manchester",
            "Horsemen charge: Peterloo",
        ], scale=0.86, box=2)
        # --- Band 5: The fight for unions
        self.next_band(5)
        self.write_rows(5, "The fight for unions", [
            "Together workers are strong: the strike",
            "Banned until 1824",
            "Tolpuddle: six men sent away, then pardoned",
        ], scale=0.86, box=2)
        # --- Band 6: Chartists and great strikes
        self.next_band(6)
        self.write_rows(6, "Chartists and great strikes", [
            "Six demands for the vote",
            "Matchgirls and dockers win",
            "South Africa: the right to organise",
        ], scale=0.86, box=0)
        self.wait(4)
