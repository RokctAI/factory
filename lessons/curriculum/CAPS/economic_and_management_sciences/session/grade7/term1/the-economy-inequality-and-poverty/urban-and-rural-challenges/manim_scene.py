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

# Band-layout whiteboard scene for urban-and-rural-challenges (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-5). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (170/160/180/150/100 of 760 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class UrbanAndRuralChallengesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.78, box=None):
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
            self.play(Create(SurroundingRectangle(made[box], color=YELLOW)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1)
        self.write_rows(0, "Urban and rural areas", [
            "Urban: towns and cities, dense",
            "Rural: farms, villages, sparse",
            "Urban: services and secondary work",
            "Rural: farming, mining, some tourism",
        ], box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Rural challenges", [
            "Few jobs; many depend on grants",
            "Poor roads, water, electricity, internet",
            "Clinics and schools far away",
            "Young people leave for cities",
        ], box=0)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Urban challenges", [
            "Rapid urbanisation",
            "Informal settlements and housing backlog",
            "Unemployment, crime and traffic",
            "Pressure on water, power and refuse",
        ], box=1)


        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Village and city", [
            "Village: long walk to clinic, few jobs",
            "City: jobs nearby but expensive",
            "Village: space, community, farming",
            "City: crowding, traffic, shacks",
        ], box=0)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Push, pull and fix", [
            "Push: no jobs, no services",
            "Pull: jobs, schools, clinics",
            "Fix village: roads, farms, tourism",
            "Fix city: houses near jobs, transport",
        ], box=0)

        self.wait(4)
