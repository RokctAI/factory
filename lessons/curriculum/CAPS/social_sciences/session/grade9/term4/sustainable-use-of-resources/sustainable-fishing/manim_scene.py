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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex keep the export to the
# allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SustainableFishingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): What Sustainable Fishing Means
        title = Tex('Sustainable fishing').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Use no faster than it renews').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Healthy stocks, healthy ecosystem').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Maximum sustainable yield').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Leave a safety margin').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Managing Fisheries: Science, Rules and Enforcement
        self.next_band(1)
        b1_title = Tex('Managing fisheries').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Scientists assess the stocks').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Total allowable catch and quotas').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Closed seasons and size limits').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Hake recovers, certified 2004').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Protected Areas, Better Methods and Fish Farming
        self.next_band(2)
        b2_title = Tex('Protection and better methods').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Marine protected areas').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('Spillover to nearby waters').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Turtle excluders, bird-scaring lines').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Fish farming: help with risks').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Consumers, Communities and SASSI, and the Error Museum
        self.next_band(3)
        b3_title = Tex('Consumers and communities').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('SASSI: green, orange, red').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Ecolabels on certified fish').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Small-scale fishers' rights, 2012").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('High Seas Treaty, 2023').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Consumers, Communities and SASSI, and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Sustainable means no fishing''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Fish farms always help''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Protected areas are useless''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``My choice makes no difference''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Referee at a Match
        self.next_band(5)
        b5_title = Tex('A referee at a match').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Count the fish first').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Set a limit for the year').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Let small fish grow up').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Inspectors check the catch').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Nursery in the Sea
        self.next_band(6)
        b6_title = Tex('A nursery in the sea').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Fish grow big and breed').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Some swim out to be caught').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Smarter fishing gear').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('Careful fish farms').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): A Traffic Light in the Fish Shop
        self.next_band(7)
        b7_title = Tex('A traffic light in the fish shop').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Green: go').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Orange: think twice').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Red: stop, it's illegal").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Fair rights for fishing communities').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l1, color=YELLOW)))
        self.wait(4)
