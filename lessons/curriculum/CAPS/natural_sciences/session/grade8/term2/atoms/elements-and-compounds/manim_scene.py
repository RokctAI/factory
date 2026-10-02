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

# Band-layout whiteboard scene for elements-and-compounds (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (220/230/240/230/180/180/190 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ElementsAndCompoundsSession(MovingCameraScene):
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1)
        self.write_rows(0, 'Matter: pure substances and mixtures', [
            'Pure: one kind of particle, fixed composition',
            'Mixture: substances not joined, any proportion',
            'Pure: sharp melting point; mixture: a range',
            'Pure substances: elements and compounds',
        ], scale=0.8, box=3)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, 'Elements: one kind of atom', [
            'Monatomic: He, Ne, Ar. \\ Lattice: metals, diamond',
            'Diatomic: H$_2$, N$_2$, O$_2$, F$_2$, Cl$_2$, Br$_2$, I$_2$',
            'Larger: O$_3$, S$_8$, P$_4$ (allotropes)',
            'O$_2$ is still an element',
        ], scale=0.8, box=1)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, 'Compounds: fixed ratio', [
            'H$_2$O, CO$_2$, NH$_3$, CH$_4$, C$_6$H$_{12}$O$_6$, NaCl',
            'Na + Cl$_2$: salt you can eat',
            'CO poison; CO$_2$ breathed out',
            'Names: sodium chloride, magnesium oxide; mono, di, tri',
        ], scale=0.78, box=1)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, 'Formulas and particle diagrams', [
            'Subscript counts atoms; coefficient counts molecules',
            'C$_6$H$_{12}$O$_6$: 24 atoms. \\ 2H$_2$O: 6 atoms',
            'One kind of particle: pure. More: mixture',
            'One kind of atom per particle: element. More: compound',
        ], scale=0.78, box=2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        errs = [
            "``O$_2$ is a compound''",
            "``Air is a compound''",
            "``A compound keeps its elements' properties''",
            "``2H$_2$O is the same as H$_2$O$_2$''",
        ]
        for i, e in enumerate(errs):
            m = Tex(e).scale(0.85).shift(band_shift(4) + UP * (1.3 - 1.0 * i))
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5)
        self.next_band(5)
        self.write_rows(5, 'Pure or mixed?', [
            'Fruit salad: a mixture',
            'Pure: one substance only',
            'Elements and compounds are both pure',
        ], scale=0.85, box=1)

        # --- Band 6 (subtopic_6)
        self.next_band(6)
        self.write_rows(6, 'Couples that never split up', [
            'Helium alone; oxygen in pairs, O$_2$',
            'Seven elements are couples',
            'Same atoms joined: still an element',
        ], scale=0.85, box=2)

        # --- Band 7 (subtopic_7)
        self.next_band(7)
        self.write_rows(7, 'New substance, new personality', [
            'Wild metal + poison gas = table salt',
            'H$_2$O puts fires out',
            'Small number counts atoms',
        ], scale=0.85, box=0)

        last = Tex('Joined in a fixed ratio: a brand-new substance.').scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
