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

# Band-layout whiteboard scene for what-the-industrial-revolution-was-and-social-change (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (210/200/230/250/150/150/150 of 1340 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class WhatTheIndustrialRevolutionWasAndSocialChangeSession(MovingCameraScene):
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
        # --- Band 0: Machines, power and factories
        self.write_rows(0, "Machines, power and factories", [
            "Jenny, water frame 1769, mule 1779, power loom 1785",
            "Water wheels first; Watt and Boulton steam engines",
            "Cromford mill 1771: the factory system",
            "Manchester: Cottonopolis",
        ], scale=0.8, box=2)
        # --- Band 1: Coal, iron, canals, railways
        self.next_band(1)
        self.write_rows(1, "Coal, iron, canals, railways", [
            "Coal: about 5 to 50 million tonnes a year, 1750 to 1850",
            "Darby's coke 1709; Cort's puddling 1784",
            "Bridgewater Canal 1761 halves coal prices",
            "Railways 1825 and 1830; about 10 000 km by 1850",
        ], scale=0.8, box=3)
        # --- Band 2: Population, towns, classes
        self.next_band(2)
        self.write_rows(2, "Population, towns, classes", [
            "England and Wales: 6 million 1750, 18 million 1851",
            "1851: more people in towns than countryside",
            "Industrial middle class and working class",
            "Votes: 1832 middle class; 1867, 1884 working men",
        ], scale=0.8, box=1)
        # --- Band 3: Time, work and family
        self.next_band(3)
        self.write_rows(3, "Time, work and family", [
            "The bell at six; 12 to 14 hour days",
            "Family members work apart",
            "Optimists: cheap goods, wages up after 1850",
            "Pessimists: early costs in health and hours",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: From muscles to steam
        self.next_band(4)
        self.write_rows(4, "From muscles to steam", [
            "A T-shirt that took days, a factory that pours out cloth",
            "Machines, power, factories, transport",
            "Coal feeds; iron builds",
        ], scale=0.8)
        # --- Band 5: The great move to town
        self.next_band(5)
        self.write_rows(5, "The great move to town", [
            "Families walk to the towns",
            "1851: most people in towns",
            "Middle class and working class",
        ], scale=0.86, box=1)
        # --- Band 6: The factory clock
        self.next_band(6)
        self.write_rows(6, "The factory clock", [
            "Bell at six; the machine sets the pace",
            "Family works apart",
            "Better life came slowly",
        ], scale=0.86, box=2)
        self.wait(4)
