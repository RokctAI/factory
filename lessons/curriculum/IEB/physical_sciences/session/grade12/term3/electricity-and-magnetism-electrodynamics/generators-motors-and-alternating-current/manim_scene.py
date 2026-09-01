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

# Band-layout whiteboard scene for "Generators, Motors and Alternating Current"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only; the generator is hand-built from Rectangles
# (coil, magnets), Circles (rings), Lines (wires, axes) and Tex labels.
# Band dwell time follows subtopics.json (235/240/240/235/190/195/195 of 1530).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class GeneratorsMotorsACSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # --- Band 0 (subtopic_1): induction and the generator principle
        title = Tex("Generators, Motors and AC").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Generator: mechanical $\\rightarrow$ electrical").scale(1.0).shift(UP * 1.1)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("Induction: changing flux through a coil").scale(1.0).shift(UP * 0.2)
        b0_l3 = Tex("induces an emf").scale(1.0).shift(DOWN * 0.6)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = Tex("Rotation is the payment: work against").scale(0.95).shift(DOWN * 1.6)
        b0_l5 = Tex("magnetic forces becomes electrical energy").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): build the AC generator; rings decide AC or DC
        self.next_band(1)
        b1_title = Tex("Build the AC generator").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        c1 = band_shift(1) + DOWN * 0.2
        pole_n = Rectangle(width=0.7, height=2.4).move_to(c1 + LEFT * 2.9)
        pole_s = Rectangle(width=0.7, height=2.4).move_to(c1 + RIGHT * 2.9)
        lab_n = Tex("N").scale(0.8).move_to(c1 + LEFT * 2.9)
        lab_s = Tex("S").scale(0.8).move_to(c1 + RIGHT * 2.9)
        self.play(Create(pole_n), Create(pole_s), Write(lab_n), Write(lab_s))
        coil = Rectangle(width=3.2, height=1.6).move_to(c1)
        lab_coil = Tex("armature coil").scale(0.7).shift(c1 + UP * 1.3)
        self.play(Create(coil), Write(lab_coil))
        ring1 = Circle(radius=0.22).move_to(c1 + DOWN * 1.6 + LEFT * 0.5)
        ring2 = Circle(radius=0.22).move_to(c1 + DOWN * 1.6 + RIGHT * 0.5)
        lab_rings = Tex("slip rings").scale(0.7).shift(c1 + DOWN * 2.1)
        self.play(Create(ring1), Create(ring2), Write(lab_rings))
        brush1 = Rectangle(width=0.18, height=0.35).move_to(c1 + DOWN * 2.6 + LEFT * 0.5)
        brush2 = Rectangle(width=0.18, height=0.35).move_to(c1 + DOWN * 2.6 + RIGHT * 0.5)
        lab_brush = Tex("brushes").scale(0.7).shift(c1 + DOWN * 3.1)
        self.play(Create(brush1), Create(brush2), Write(lab_brush))
        self.wait(2)
        b1_l1 = Tex("Slip rings: AC. Split-ring commutator: DC.").scale(0.9).shift(band_shift(1) + DOWN * 3.5 + UP * 0.0)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the motor effect, forces on the coil
        self.next_band(2)
        b2_title = Tex("The motor effect").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Current-carrying conductor in a field").scale(0.95).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("experiences a force").scale(0.95).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        c2 = band_shift(2) + DOWN * 1.3
        coil2 = Rectangle(width=3.0, height=1.2).move_to(c2)
        arr_up = Line(c2 + LEFT * 1.5 + UP * 0.0, c2 + LEFT * 1.5 + UP * 1.1)
        arr_dn = Line(c2 + RIGHT * 1.5 + UP * 0.0, c2 + RIGHT * 1.5 + DOWN * 1.1)
        lab_up = Tex("force up").scale(0.7).shift(c2 + LEFT * 1.5 + UP * 1.45)
        lab_dn = Tex("force down").scale(0.7).shift(c2 + RIGHT * 1.5 + DOWN * 1.45)
        self.play(Create(coil2))
        self.play(Create(arr_up), Write(lab_up))
        self.play(Create(arr_dn), Write(lab_dn))
        self.wait(2.5)
        b2_l3 = Tex("Opposite currents, opposite forces: a turning couple").scale(0.85).shift(band_shift(2) + DOWN * 3.2)
        self.play(Write(b2_l3))
        self.wait(3)

        # --- Band 3 (subtopic_2): one device, two energy directions
        self.next_band(3)
        b3_title = Tex("One device, two directions").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Commutator flips the current every half turn,").scale(0.9).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("timed at the vertical: the lurch becomes a spin").scale(0.9).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Turn the shaft $\\rightarrow$ electricity out: GENERATOR").scale(0.9).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex("Feed electricity in $\\rightarrow$ shaft turns: MOTOR").scale(0.9).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)
        b3_l5 = Tex("Same parts list: coil, magnets, brushes, ring").scale(0.85).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): why the grid chose AC
        self.next_band(4)
        b4_title = Tex("Why the grid chose AC").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Transformers change AC voltage easily").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"P_{loss} = I^2R").scale(1.1).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex("High voltage $\\Rightarrow$ small current").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        b4_l4 = Tex("$\\Rightarrow$ tiny squared loss").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex("Step up for the journey, down to 220 V at the wall").scale(0.85).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the AC wave against the DC line
        self.next_band(5)
        b5_title = Tex("The AC wave, sketched for marks").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        c5 = band_shift(5) + DOWN * 0.5
        ax_v = Line(c5 + LEFT * 3.4 + DOWN * 1.6, c5 + LEFT * 3.4 + UP * 1.8)
        ax_t = Line(c5 + LEFT * 3.4, c5 + RIGHT * 3.4)
        self.play(Create(ax_v), Create(ax_t))
        # Sine wave approximated by joined line segments.
        pts = [c5 + LEFT * 3.4]
        import math
        for i in range(1, 25):
            x = -3.4 + i * (6.8 / 24)
            y = 1.3 * math.sin(i * (2 * math.pi / 12))
            pts.append(c5 + RIGHT * x + UP * y)
        wave = VGroup(*[Line(pts[i], pts[i + 1]) for i in range(len(pts) - 1)])
        self.play(Create(wave), run_time=2)
        lab_vmax = Tex("$V_{max}$").scale(0.7).shift(c5 + LEFT * 2.0 + UP * 1.7)
        self.play(Write(lab_vmax))
        self.wait(2)
        b5_l1 = Tex("50 cycles per second; below zero $=$ reversed flow").scale(0.8).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex("Resistor: current peaks WITH the voltage").scale(0.85).shift(band_shift(5) + DOWN * 3.3)
        self.play(Write(b5_l2))
        self.wait(3)

        # --- Band 6 (subtopic_4): rms — the DC-equivalent value
        self.next_band(6)
        b6_title = Tex("RMS: the honest average").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Plain average of the wave: zero. Useless.").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("Heating follows current SQUARED: positive both ways").scale(0.85).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"V_{rms} = \frac{V_{max}}{\sqrt{2}} \qquad I_{rms} = \frac{I_{max}}{\sqrt{2}}").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = MathTex(r"V_{max} = 220\sqrt{2} = 311,13\ \text{V}").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Insulation survives the peak; bills run on the rms").scale(0.8).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): worked example — 55 ohm element on the mains
        self.next_band(7)
        b7_title = Tex("Worked: 55 $\\Omega$ element, 220 V mains").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"I_{rms} = \frac{220}{55} = 4\ \text{A}").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"P_{avg} = V_{rms} I_{rms} = 220 \times 4 = 880\ \text{W}").scale(0.95).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = MathTex(r"I_{max} = 4\sqrt{2} = 5,66\ \text{A}").scale(0.95).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = MathTex(r"P_{peak} = V_{max} I_{max} = 1760\ \text{W} = 2 \times P_{avg}").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Average power $=$ half of $V_{max} I_{max}$").scale(0.9).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_5): the dynamo on the bicycle wheel
        self.next_band(8)
        b8_title = Tex("The dynamo on the bicycle wheel").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Magnet $+$ coil $+$ your legs $=$ a power station").scale(0.9).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Still magnet: nothing. Moving magnet: volts.").scale(0.95).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Engage the dynamo: pedalling stiffens —").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = Tex("the lamplight is bought from your muscles").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Power station: same physics, bigger rider —").scale(0.9).shift(band_shift(8) + DOWN * 2.5)
        b8_l6 = Tex("steam, water or wind spins the coil").scale(0.9).shift(band_shift(8) + DOWN * 3.3)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): one machine, two personalities
        self.next_band(9)
        b9_title = Tex("One machine, two personalities").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Plug the fan in: current $\\rightarrow$ spin (motor)").scale(0.9).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("Flick the blades: spin $\\rightarrow$ current (generator)").scale(0.9).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("Split ring swaps current every half turn,").scale(0.9).shift(band_shift(9) + DOWN * 0.7)
        b9_l4 = Tex("on cue at the vertical: spin forever").scale(0.9).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Electric vehicle: motor when driving,").scale(0.9).shift(band_shift(9) + DOWN * 2.4)
        b9_l6 = Tex("generator when braking — same copper").scale(0.9).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_7): what 220 volts actually means
        self.next_band(10)
        b10_title = Tex("What 220 volts actually means").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("The socket swings $+311$ to $-311$, fifty times a second").scale(0.85).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Plain average: zero. But heat $\\propto I^2$ —").scale(0.9).shift(band_shift(10) + UP * 0.3)
        b10_l3 = Tex("both strokes of the slosh heat the element").scale(0.9).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = MathTex(r"\frac{311}{\sqrt{2}} = 220\ \text{V (rms)}").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex("1100 W heater: 5 A on the books,").scale(0.9).shift(band_shift(10) + DOWN * 2.5)
        b10_l6 = Tex("peaks near 7 A — wiring rated for the peaks").scale(0.9).shift(band_shift(10) + DOWN * 3.3)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(4)
