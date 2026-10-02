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
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class OverloadProtectionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Overloads and Short Circuits
        title = Tex("Too much current").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Large currents overheat cables: fire").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Overload: too many appliances").scale(0.9).shift(UP * 0.35)
        b0_l3 = MathTex(r"8{,}7 + 8{,}7 + 4 = 21{,}4 \ \mathrm{A}").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Short circuit: live touches neutral").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Fuses and Circuit Breakers
        self.next_band(1)
        b1_title = Tex("Fuses and breakers").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("In series, in the live wire").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Fuse: thin wire melts; replace same rating").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Breaker: automatic switch; reset").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("10 A lights; 16 or 20 A plugs").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The Earth Leakage Unit
        self.next_band(2)
        b2_title = Tex("Earth leakage unit").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("About 50 mA through the chest can kill").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Compares live and neutral currents").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Trips at about 30 mA leakage").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Test button every few months").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): What to Do When Power Trips and the Error Museum
        self.next_band(3)
        b3_title = Tex("When power trips").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Unplug, reset, reconnect one by one").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Trips with one appliance: it is faulty").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Trips with nothing on: call an electrician").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Never bypass protection").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): What to Do When Power Trips and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Fuses protect people''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Use a thicker fuse''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``A tripping breaker is faulty''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Fuses go in the neutral''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Too Much Current
        self.next_band(5)
        b5_title = Tex("Too much current").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Hot wires start fires").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Overload: currents add up").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Short circuit: sparks and a bang").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Warm plugs are a warning").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Melting Link and the Clicking Switch
        self.next_band(6)
        b6_title = Tex("Melting link, clicking switch").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Fuse melts on purpose").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Same rating; never foil").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Breaker clicks off").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Push it back on after fixing").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The People Protector
        self.next_band(7)
        b7_title = Tex("The people protector").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Out must equal back").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("30 thousandths missing: off").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Press the test button").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Never bypass it").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l1, color=YELLOW)))
        self.wait(4)
