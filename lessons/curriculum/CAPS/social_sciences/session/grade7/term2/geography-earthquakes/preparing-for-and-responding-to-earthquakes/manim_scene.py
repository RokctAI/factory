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

# Band-layout whiteboard scene for preparing-for-and-responding-to-earthquakes (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/170/210/190/90/90/90 of 1030 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class PreparingForAndRespondingToEarthquakesSession(MovingCameraScene):
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
        # --- Band 0: Hazard, Risk and Vulnerability
        self.write_rows(0, "Hazard, Risk and Vulnerability", [
            "Hazard: an event that could cause harm",
            "Disaster: a hazard that does serious harm",
            "Vulnerability: how easily people are harmed",
            "Prepare, respond, recover, prepare again",
        ], scale=0.86, box=1)
        # --- Band 1: Building and Planning for Earthquakes
        self.next_band(1)
        self.write_rows(1, "Building and Planning for Earthquakes", [
            "Steel reinforcement and cross-bracing",
            "Base isolators let the ground move beneath",
            "Building codes must be enforced",
            "Plan land use away from faults and soft soils",
        ], scale=0.8, box=1)
        # --- Band 2: Warnings, Education and Drills
        self.next_band(2)
        self.write_rows(2, "Warnings, Education and Drills", [
            "Prediction: not yet possible",
            "Early warning: seconds to a minute",
            "Drop, cover and hold on",
            "Drills and an emergency kit",
        ], scale=0.86, box=2)
        # --- Band 3: Responding and Recovering
        self.next_band(3)
        self.write_rows(3, "Responding and Recovering", [
            "The first 72 hours matter most",
            "Rescue, medical care, shelter, clean water",
            "Rescue South Africa, Gift of the Givers",
            "Recover: build back better",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Why Some Places Suffer More
        self.next_band(4)
        self.write_rows(4, "Why Some Places Suffer More", [
            "Hazard: could hurt",
            "Disaster: did hurt",
            "Weak houses mean more harm",
        ], scale=0.86, box=0)
        # --- Band 5: Strong Buildings and Drills
        self.next_band(5)
        self.write_rows(5, "Strong Buildings and Drills", [
            "Steel, braces and rubber pads",
            "Drop, cover, hold on",
            "Coast: go to high ground",
        ], scale=0.86, box=0)
        # --- Band 6: Helping Afterwards
        self.next_band(6)
        self.write_rows(6, "Helping Afterwards", [
            "Rescue fast: first three days",
            "Tents, doctors, clean water",
            "Build back better",
        ], scale=0.86, box=0)
        self.wait(4)
