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

# Band-layout whiteboard scene for contraception-and-preventing-hiv (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/200/160/120/120/120 of 870 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ContraceptionAndPreventingHivSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Contraception
        self.write_rows(0, "Contraception", [
            "Contraception: prevents pregnancy",
            "Abstinence: the only 100\\% method",
            "Condoms: block sperm AND infections; every time, correctly",
            "Pill, injection, implant: no STI protection",
        ], scale=0.76, box=2)

        # --- Band 1 (subtopic_2): HIV, AIDS and other STIs
        self.next_band(1)
        self.write_rows(1, "HIV, AIDS and other STIs", [
            "STIs: often no symptoms; clinics treat free",
            "HIV: virus attacking CD4 cells; AIDS: late stage",
            "Spread: sex, blood, mother to baby; NOT hugs or cups",
            "Test to know; ART keeps people healthy",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Consequences and choices
        self.next_band(2)
        self.write_rows(2, "Consequences and choices", [
            "Risks: pregnancy, STIs, HIV, complications",
            "Emotional and school consequences",
            "Age of consent 16; abuse is never the child's fault",
            "Decide in advance; say no clearly; Childline 116",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``You cannot get pregnant the first time''",
            "``The pill protects against HIV''",
            "``HIV spreads by hugging or sharing cups''",
            "``HIV and AIDS are the same thing''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Preventing pregnancy
        self.next_band(4)
        self.write_rows(4, "Preventing pregnancy", [
            "Abstinence: the only 100\\% way",
            "Condom: blocks sperm and infections",
            "Use it every time, from the start",
            "Pill and injections: no infection protection",
        ], scale=0.88, box=0)

        # --- Band 5 (subtopic_5): The body's security guards
        self.next_band(5)
        self.write_rows(5, "The body's security guards", [
            "HIV knocks out the body's guards",
            "AIDS: the late stage without treatment",
            "Not spread by hugs, cups or mosquitoes",
            "Test to know; ART keeps people healthy",
        ], scale=0.88, box=2)

        # --- Band 6 (subtopic_6): Worth waiting for
        self.next_band(6)
        self.write_rows(6, "Worth waiting for", [
            "Risks: pregnancy, infections, leaving school",
            "Age of consent: 16; abuse is never your fault",
            "Childline: 116, free",
            "Decide in advance; say no clearly",
        ], scale=0.82, box=3)

        last = Tex("Knowledge, delay, condoms and testing protect your future.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
