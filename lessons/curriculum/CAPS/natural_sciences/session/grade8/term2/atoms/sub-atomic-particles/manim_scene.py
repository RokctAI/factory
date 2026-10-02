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

# Band-layout whiteboard scene for sub-atomic-particles (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (230/230/240/220/180/190/180 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SubAtomicParticlesSession(MovingCameraScene):
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
        self.write_rows(0, 'Discovering the inside of the atom', [
            '1897 Thomson: electron; plum pudding model',
            '1909 gold foil: most pass, 1 in 8 000 bounce back',
            '1911 Rutherford: tiny dense positive nucleus',
            '1932 Chadwick: the neutron',
        ], scale=0.8, box=2)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, 'Three sub-atomic particles', [
            'Proton: +1, mass 1, nucleus',
            'Neutron: 0, mass 1, nucleus',
            'Electron: $-1$, mass 1/1836, outside the nucleus',
            'Atom 100 m across: nucleus about 1 mm',
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, 'Atoms are neutral', [
            'Electrons = protons = atomic number',
            'Neutrons = mass number $-$ atomic number',
            'Na: 11 p, 12 n, 11 e. \\ Al: 13 p, 14 n, 13 e',
            'Lose an electron: ion, charge +1',
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, 'Drawing the atom', [
            'Dalton ball, Thomson pudding, Rutherford nucleus, Bohr shells',
            'Shells hold 2, then 8, then 8',
            'C: 2, 4. \\ Na: 2, 8, 1. \\ Ar: 2, 8, 8',
            'Not to scale',
        ], scale=0.8, box=2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        errs = [
            "``Electrons are in the nucleus''",
            "``Neutrons are negative''",
            "``Protons equal neutrons, so the atom is neutral''",
            "``Neutrons = mass number + atomic number''",
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
        self.write_rows(5, 'A stadium with a grain of sand', [
            'Gold foil: almost all pass through',
            'Nucleus: grain of sand on the centre spot',
            'Your electrons push its electrons',
        ], scale=0.85, box=1)

        # --- Band 6 (subtopic_6)
        self.next_band(6)
        self.write_rows(6, 'Three particles, three charges', [
            'Protons positive, in the nucleus',
            'Neutrons neutral, in the nucleus',
            'Electrons negative, outside, very light',
        ], scale=0.85, box=None)

        # --- Band 7 (subtopic_7)
        self.next_band(7)
        self.write_rows(7, 'A perfect balance', [
            'Protons = electrons: no overall charge',
            'Neutrons = mass number take away atomic number',
            'Rings: 2, then 8, then 8',
        ], scale=0.85, box=0)

        last = Tex('Protons positive, neutrons neutral, electrons outside.').scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
