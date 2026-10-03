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


def box(origin, l=1.0, h=0.5, d=0.35, color=WHITE):
    """Rectangular prism wireframe: front face l by h, depth drawn at 45 degrees."""
    off = np.array([d, d, 0])
    f = [origin, origin + RIGHT * l, origin + RIGHT * l + UP * h, origin + UP * h]
    b = [p + off for p in f]
    g = VGroup()
    for i in range(4):
        g.add(Line(f[i], f[(i + 1) % 4], color=color))
        g.add(Line(b[i], b[(i + 1) % 4], color=color))
        g.add(Line(f[i], b[i], color=color))
    return g


def cylinder(base_centre, r=0.5, h=1.0, tilt=0.35, color=WHITE):
    top = base_centre + UP * h
    return VGroup(
        Ellipse(width=2 * r, height=2 * r * tilt, color=color).move_to(top),
        Ellipse(width=2 * r, height=2 * r * tilt, color=color).move_to(base_centre),
        Line(base_centre + LEFT * r, top + LEFT * r, color=color),
        Line(base_centre + RIGHT * r, top + RIGHT * r, color=color),
    )


def results_table(origin, rows, col_w=2.2, row_h=0.5, scale=0.5):
    g = VGroup()
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            g.add(Tex(cell).scale(scale).move_to(origin + RIGHT * col_w * (j + 0.5) + DOWN * row_h * (i + 0.5)))
        g.add(Line(origin + DOWN * row_h * (i + 1), origin + RIGHT * col_w * len(row) + DOWN * row_h * (i + 1),
                   color=GREY, stroke_width=1))
    return g


class DoublingVolumeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): one dimension doubled
        title = Tex("Doubling one dimension").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0 = box(np.array([-6.3, 0.6, 0]), l=1.2, h=0.6)
        b1 = box(np.array([-6.3, -1.2, 0]), l=1.2, h=0.6)
        b2 = box(np.array([-5.1, -1.2, 0]), l=1.2, h=0.6, color=BLUE)
        self.play(Create(b0))
        self.play(Create(b1), Create(b2), run_time=1.5)
        two = Tex("Two old boxes end to end").scale(0.55).move_to(np.array([-5.0, -1.7, 0]))
        self.play(Write(two))
        rows = [["Dimensions", "Volume", "Multiplier"],
                ["4 by 3 by 2", "24", "1"],
                ["8 by 3 by 2", "48", "2"],
                ["4 by 6 by 2", "48", "2"],
                ["4 by 3 by 4", "48", "2"],
                ["Prism, length 20", "120", "2"],
                ["Cylinder r 2, h 10", "40$\\pi$", "2"]]
        t = results_table(np.array([-2.2, 2.3, 0]), rows)
        self.play(Create(t), run_time=3)
        self.wait(3)
        rule = Tex("One dimension doubled: volume times 2").scale(0.8).shift(DOWN * 2.6 + RIGHT * 1.2)
        self.play(Write(rule))
        self.play(Create(SurroundingRectangle(rule, color=YELLOW)))
        self.wait(3)

        # --- Band 1 (subtopic_2): two dimensions and the radius
        self.next_band(1)
        b1_title = Tex("Two dimensions, and the radius").scale(1.15).shift(band_shift(1) + UP * 3.0)
        self.play(Write(b1_title))
        self.wait(1.5)
        c_small = cylinder(band_shift(1) + LEFT * 6.0 + DOWN * 1.5, r=0.4, h=1.2)
        c_tall = cylinder(band_shift(1) + LEFT * 4.6 + DOWN * 1.5, r=0.4, h=2.4, color=GREEN)
        c_wide = cylinder(band_shift(1) + LEFT * 2.6 + DOWN * 1.5, r=0.8, h=1.2, color=BLUE)
        self.play(Create(c_small), Create(c_tall), Create(c_wide), run_time=2)
        cl = Tex("$20\\pi$ \\quad $40\\pi$ \\quad $80\\pi$").scale(0.6).move_to(band_shift(1) + LEFT * 4.3 + DOWN * 2.2)
        self.play(Write(cl))
        lines = [
            r"8 \times 6 \times 2 = 96 = 4 \times 24",
            r"\text{Triangle legs } 6, 8: \tfrac{1}{2} \times 6 \times 8 = 24;\ 24 \times 10 = 240",
            r"\pi \times 4^2 \times 5 = 80\pi \approx 251.33 = 4 \times 20\pi",
            r"\text{Tank: taller } \approx 4247 \ell \qquad \text{wider } \approx 8495 \ell",
        ]
        for i, r in enumerate(lines):
            m = MathTex(r).scale(0.62).shift(band_shift(1) + RIGHT * 2.6 + UP * (1.6 - 0.9 * i))
            self.play(Write(m))
            self.wait(2.4)
        rr = Tex("Radius is squared: doubling it gives times 4").scale(0.75).shift(band_shift(1) + RIGHT * 2.6 + DOWN * 2.3)
        self.play(Write(rr))
        self.play(Create(SurroundingRectangle(rr, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): every dimension
        self.next_band(2)
        b2_title = Tex("Every dimension doubled: times 8").scale(1.15).shift(band_shift(2) + UP * 3.0)
        self.play(Write(b2_title))
        self.wait(1.5)
        o = band_shift(2) + LEFT * 6.2 + DOWN * 1.8
        cubes = VGroup()
        for dx, dy in ((0, 0), (1, 0), (0, 1), (1, 1)):
            cubes.add(box(o + RIGHT * 0.9 * dx + UP * 0.9 * dy, l=0.9, h=0.9, d=0.4, color=BLUE))
        for dx, dy in ((0, 0), (1, 0), (0, 1), (1, 1)):
            cubes.add(box(o + RIGHT * 0.9 * dx + UP * 0.9 * dy + np.array([0.4, 0.4, 0]), l=0.9, h=0.9, d=0.4, color=GREY))
        self.play(Create(cubes), run_time=2.5)
        cl2 = Tex("Eight small cubes fill the big one").scale(0.55).move_to(o + RIGHT * 1.3 + DOWN * 0.5)
        self.play(Write(cl2))
        ev = [
            r"8 \times 6 \times 4 = 192 = 8 \times 24",
            r"\text{Cube: } 125 \to 1000 \qquad \pi \times 16 \times 10 = 160\pi",
            r"\text{Surface: } 52 \to 208 \ (\times 4) \qquad 150 \to 600",
            r"\text{Length } \times 2,\ \text{area } \times 4,\ \text{volume } \times 8",
        ]
        for i, r in enumerate(ev):
            m = MathTex(r).scale(0.68).shift(band_shift(2) + RIGHT * 2.4 + UP * (1.6 - 0.9 * i))
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(m, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): scale factor k
        self.next_band(3)
        b3_title = Tex("Scale factor k").scale(1.2).shift(band_shift(3) + UP * 3.0)
        self.play(Write(b3_title))
        self.wait(1.5)
        kk = [
            r"\text{Lengths } \times k \qquad \text{areas } \times k^2 \qquad \text{volumes } \times k^3",
            r"k = 3: \ 60 \times 27 = 1620 \qquad k = \tfrac{1}{2}: \ \times \tfrac{1}{8} \qquad k = 1.5: \ \times 3.375",
            r"\text{Backwards: } k = \sqrt[3]{\text{volume factor}} \qquad \sqrt[3]{8} = 2,\ \sqrt[3]{2} \approx 1.26",
            r"\text{Cube side 1: } 6 : 1 \qquad \text{side 2: } 24 : 8 = 3 : 1",
        ]
        for i, r in enumerate(kk):
            m = MathTex(r).scale(0.7).shift(band_shift(3) + UP * (1.7 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.6)
        ap = Tex("Big pot: 8 times the stew, 4 times the metal").scale(0.8).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(ap))
        self.play(Create(SurroundingRectangle(ap, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        e1 = Tex("Every dimension doubled: volume doubled").scale(0.8).shift(band_shift(4) + UP * 1.5)
        e2 = Tex("Radius doubled: volume doubled").scale(0.8).shift(band_shift(4) + UP * 0.6)
        e3 = Tex("Tripled every way: volume times 9").scale(0.8).shift(band_shift(4) + DOWN * 0.3)
        e4 = Tex("8 times the volume, so lengths times 8").scale(0.8).shift(band_shift(4) + DOWN * 1.2)
        e5 = Tex("Doubled box needs 8 times the cardboard").scale(0.8).shift(band_shift(4) + DOWN * 2.1)
        for m in (e1, e2, e3, e4, e5):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.6)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): stretch one way then two
        self.next_band(5)
        b5_title = Tex("Stretch one way, then two").scale(1.2).shift(band_shift(5) + UP * 2.8)
        self.play(Write(b5_title))
        self.wait(2)
        s1 = Tex("24 little cubes; one way stretched: 48, two old boxes").scale(0.8).shift(band_shift(5) + UP * 1.4)
        s2 = Tex("Two ways stretched: 96, four old boxes").scale(0.8).shift(band_shift(5) + UP * 0.5)
        s3 = Tex("Tent prism: 60, then 120, then 240").scale(0.8).shift(band_shift(5) + DOWN * 0.4)
        s4 = Tex("Each doubled direction: another times 2").scale(0.85).shift(band_shift(5) + DOWN * 1.3)
        for m in (s1, s2, s3, s4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(s4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): the radius counts twice
        self.next_band(6)
        b6_title = Tex("The radius counts twice").scale(1.2).shift(band_shift(6) + UP * 2.8)
        self.play(Write(b6_title))
        self.wait(2)
        t_small = cylinder(band_shift(6) + LEFT * 5.8 + DOWN * 1.4, r=0.45, h=1.3)
        t_tall = cylinder(band_shift(6) + LEFT * 4.3 + DOWN * 1.4, r=0.45, h=2.6, color=GREEN)
        t_wide = cylinder(band_shift(6) + LEFT * 2.2 + DOWN * 1.4, r=0.9, h=1.3, color=BLUE)
        self.play(Create(t_small), Create(t_tall), Create(t_wide), run_time=2)
        r1 = Tex("Taller: times 2").scale(0.8).shift(band_shift(6) + RIGHT * 3.0 + UP * 1.3)
        r2 = Tex("Wider: times 4").scale(0.8).shift(band_shift(6) + RIGHT * 3.0 + UP * 0.4)
        r3 = Tex("Both: times 8").scale(0.8).shift(band_shift(6) + RIGHT * 3.0 + DOWN * 0.5)
        r4 = Tex("Buy the wider tank").scale(0.8).shift(band_shift(6) + RIGHT * 3.0 + DOWN * 1.4)
        for m in (r1, r2, r3, r4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(r2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): times k cubed
        self.next_band(7)
        b7_title = Tex("Times k cubed").scale(1.2).shift(band_shift(7) + UP * 2.8)
        self.play(Write(b7_title))
        self.wait(2)
        k1 = Tex("Cube side 5 holds 125; side 10 holds 1 000").scale(0.8).shift(band_shift(7) + UP * 1.5)
        k2 = Tex("Paper times 4, space inside times 8").scale(0.8).shift(band_shift(7) + UP * 0.6)
        k3 = Tex("Triple: times 27. Halve: times one eighth.").scale(0.8).shift(band_shift(7) + DOWN * 0.3)
        k4 = Tex("Backwards: cube root. Twice the tin: about 1.26 times.").scale(0.8).shift(band_shift(7) + DOWN * 1.2)
        for m in (k1, k2, k3, k4):
            self.play(Write(m))
            self.wait(2.2)
        k5 = Tex("Count directions. Radius twice. k cubed.").scale(0.9).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(k5))
        self.play(Create(SurroundingRectangle(k5, color=YELLOW)))
        self.wait(4)
