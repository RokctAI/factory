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


class WeimarRepublicAndTheTreatyOfVersaillesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Germany in Defeat and the Birth of the Weimar Republic
        title = Tex('The Weimar Republic').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('9 November 1918: the Kaiser abdicates').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Votes for all men and women over 20').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Proportional representation: many parties, coalitions').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Article 48: rule by decree in an emergency').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Treaty of Versailles: Land, Army, Money and Blame
        self.next_band(1)
        b1_title = Tex('The Treaty of Versailles: LAMB').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Land: 13 percent of European land; all colonies').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Army: 100 000 men, no tanks, aircraft or submarines').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Money: reparations of 132 billion gold marks').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Blame: Article 231, the War Guilt Clause').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): German Reactions and the Weaknesses of the Republic
        self.next_band(2)
        b2_title = Tex('German reactions').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Excluded from the talks: a Diktat').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('Stab-in-the-back myth; the November Criminals').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Generals had admitted defeat in September 1918').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('A republic blamed for a defeat it did not cause').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): The Crisis of 1923, Recovery and the Error Museum
        self.next_band(3)
        b3_title = Tex('Crisis and recovery').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('1923: the Ruhr occupied; money printed').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Hyperinflation: bread at 200 billion marks').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Stresemann: new currency and the Dawes Plan').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('1924 to 1929: recovery on American loans').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): The Crisis of 1923, Recovery and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Weimar was named after a president''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Germany negotiated the treaty''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The army was stabbed in the back''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``The treaty abolished the army''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Losing Team Gets a New Captain
        self.next_band(5)
        b5_title = Tex("The losing team's new captain").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('The Kaiser runs away; a democracy begins').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Everyone over 20 votes').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Many small parties, shaky governments').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Article 48: remember this emergency rule').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Four Letters: L A M B
        self.next_band(6)
        b6_title = Tex('Four letters: L A M B').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Land: lost land and every colony').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Army: 100 000 men, no tanks or planes').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Money: 132 billion gold marks').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('Blame: Article 231. And the stab-in-the-back lie.').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): A Wheelbarrow Full of Money
        self.next_band(7)
        b7_title = Tex('A wheelbarrow full of money').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('1923: the Ruhr taken; money printed').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('A loaf of bread: 200 billion marks').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Savings wiped out').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Recovery on American loans until 1929').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
