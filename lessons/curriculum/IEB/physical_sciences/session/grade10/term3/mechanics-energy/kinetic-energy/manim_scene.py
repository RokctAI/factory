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

# Band-layout whiteboard scene for kinetic-energy (Part 1 Expert subtopics
# 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe mobjects, add-only
# lifecycle, one band per teaching beat.
# Time apportioned to subtopics.json (225/235/240/245/180/175/175 of 1475 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class KineticEnergySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): energy carried by motion ---
        title = Tex("Kinetic Energy").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Energy carried by MOTION").scale(1.1).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = MathTex(r"E_k = \tfrac{1}{2} m v^2").scale(1.4).shift(UP * 0.0)
        self.play(Write(d2))
        self.play(Create(SurroundingRectangle(d2, color=GREEN)))
        self.wait(2.5)
        d3 = Tex("Mass dial: plain. Speed dial: SQUARED.").scale(1.0).shift(DOWN * 1.3)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex("Scalar, never negative — rest is the floor").scale(1.0).shift(DOWN * 2.3)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_2): a bakkie at fifteen ---
        self.next_band(1)
        b1t = Tex("Pricing the motion: 800 kg at 15 m/s").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"15 \text{ m/s} = 54 \text{ km/h}").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1a))
        self.wait(2)
        b1b = MathTex(r"v^2 = 15^2 = 225").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1b))
        self.wait(2)
        b1c = MathTex(r"E_k = \tfrac{1}{2} \times 800 \times 225 = 90\,000 \text{ J}").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1c))
        self.play(Create(SurroundingRectangle(b1c, color=GREEN)))
        self.wait(2.5)
        b1d = Tex("The 4 kg tin, two kilometres up — same joules").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1d))
        self.wait(3)

        # --- Band 2 (subtopic_2): the forgotten square ---
        self.next_band(2)
        b2t = Tex("The forgotten square").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = MathTex(r"\tfrac{1}{2} \times 800 \times 15 = 6\,000 \text{ J}").scale(1.05).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2a))
        self.play(Create(strike(b2a)))
        self.wait(2.5)
        b2b = Tex("Fifteen times too small").scale(1.05).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2b))
        self.wait(2)
        b2c = Tex("Defence: write $v^2 = 225$ as its own line first").scale(1.0).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2c))
        self.play(Create(SurroundingRectangle(b2c, color=GREEN)))
        self.wait(2.5)
        b2d = Tex("km/h $\\div$ 3,6 BEFORE squaring").scale(1.0).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_3): doubling the speed ---
        self.next_band(3)
        b3t = Tex("The driver doubles the speed").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = MathTex(r"30 \text{ m/s} = 108 \text{ km/h}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3a))
        self.wait(2)
        b3b = MathTex(r"E_k = \tfrac{1}{2} \times 800 \times 900 = 360\,000 \text{ J}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3b))
        self.play(Create(SurroundingRectangle(b3b, color=GREEN)))
        self.wait(2.5)
        b3c = MathTex(r"\frac{360\,000}{90\,000} = 4 \quad (2^2 = 4)").scale(1.05).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3c))
        self.wait(2.5)
        b3d = Tex("Double the speed, FOUR times the energy").scale(1.05).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3d))
        self.wait(3)

        # --- Band 4 (subtopic_3): the road consequences ---
        self.next_band(4)
        b4t = Tex("What the square does on the road").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("Four times the energy: four times the braking distance").scale(0.9).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4a))
        self.wait(2.5)
        b4b = Tex("A crash at 80 $=$ four crashes at 40, at once").scale(0.95).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4b))
        self.wait(2.5)
        b4c = Tex("100 $\\to$ 120 km/h adds more than 0 $\\to$ 60").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4c))
        self.wait(2.5)
        b4d = Tex("Speed limits are quadratic arithmetic").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4d))
        self.play(Create(SurroundingRectangle(b4d, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): the four-step method ---
        self.next_band(5)
        b5t = Tex("The method, four steps").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("1. List $m$ and $v$; convert units as you list").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5b = Tex("2. Square the velocity on its own line").scale(0.95).shift(band_shift(5) + UP * 0.2)
        b5c = Tex("3. Assemble $\\tfrac{1}{2} m v^2$, carrying units").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        b5d = Tex("4. Sense-check: positive, no direction, right scale").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        for m in (b5a, b5b, b5c, b5d):
            self.play(Write(m))
            self.wait(2)
        self.wait(2)

        # --- Band 6 (subtopic_4): the remaining traps ---
        self.next_band(6)
        b6t = Tex("The traps").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("Squaring km/h: wrong by a factor of $\\sim$13").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.play(Create(strike(b6a)))
        self.wait(2)
        b6b = Tex("Dropping the half: every answer doubled").scale(0.95).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6b))
        self.wait(2)
        b6c = Tex("`90 000 J north'").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6c))
        self.play(Create(strike(b6c)))
        self.wait(2)
        b6d = Tex("Comparing speeds linearly — square first").scale(0.95).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6d))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the moving wallet ---
        self.next_band(7)
        b7t = Tex("The moving wallet").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("Moving $=$ carrying cash").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.wait(2)
        b7b = Tex("Stopping $=$ spending every cent").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7b))
        self.play(Create(SurroundingRectangle(b7b, color=GREEN)))
        self.wait(2.5)
        b7c = Tex("Mass dial: honest. Speed dial: multiplies by itself.").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("No direction, never negative, rest is empty").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7d))
        self.wait(3)

        # --- Band 8 (subtopic_6): counting the bakkie's cash ---
        self.next_band(8)
        b8t = Tex("Counting the bakkie's cash").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = MathTex(r"15 \times 15 = 225").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2)
        b8b = MathTex(r"\tfrac{1}{2} \times 800 = 400").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8b))
        self.wait(2)
        b8c = MathTex(r"400 \times 225 = 90\,000 \text{ J}").scale(1.1).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8c))
        self.play(Create(SurroundingRectangle(b8c, color=GREEN)))
        self.wait(2.5)
        b8d = Tex("Brakes: the furnace that swallows it all").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8d))
        self.wait(3)

        # --- Band 9 (subtopic_7): the quadratic surcharge ---
        self.next_band(9)
        b9t = Tex("The quadratic surcharge").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = MathTex(r"30^2 = 900; \; 400 \times 900 = 360\,000 \text{ J}").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = Tex("Double the speed, FOUR times the cash").scale(1.05).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9b))
        self.play(Create(SurroundingRectangle(b9b, color=GREEN)))
        self.wait(2.5)
        b9c = Tex("Four times the stopping distance, four times the wreckage").scale(0.9).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9c))
        self.wait(2)
        b9d = Tex("Compare speeds by their SQUARES").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9d))
        self.wait(4)
