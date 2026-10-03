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

# Band-layout whiteboard scene for causes-and-effects-of-slave-resistance (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (140/150/180/160/90/90/90 of 900 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CausesAndEffectsOfSlaveResistanceSession(MovingCameraScene):
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
        # --- Band 0: Causes of Resistance
        self.write_rows(0, "Causes of Resistance", [
            "Loss of freedom; forced unpaid work",
            "Cruel punishment and broken families",
            "No rights; memories of home",
            "Ideas of freedom: France, Haiti, abolition",
        ], scale=0.86, box=1)
        # --- Band 1: Everyday Resistance
        self.next_band(1)
        self.write_rows(1, "Everyday Resistance", [
            "Working slowly, breaking tools",
            "Keeping language, faith and culture",
            "Complaints to the courts",
            "Running away: drosters",
        ], scale=0.86, box=4)
        # --- Band 2: Hangklip and the 1808 Rebellion
        self.next_band(2)
        self.write_rows(2, "Hangklip and the 1808 Rebellion", [
            "Hangklip: maroon community in caves",
            "1808: Louis of Mauritius leads rebellion",
            "Over 300 marched from the Swartland",
            "Stopped at Salt River; leaders hanged",
        ], scale=0.86, box=3)
        # --- Band 3: Effects of Resistance
        self.next_band(3)
        self.write_rows(3, "Effects of Resistance", [
            "Rebels punished: whipped, branded, hanged",
            "Stricter controls and patrols",
            "Pressure for reform and abolition",
            "1820s reforms; slavery ended 1834",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Why Resist?
        self.next_band(4)
        self.write_rows(4, "Why Resist?", [
            "Lost freedom",
            "Cruelty and broken families",
            "Hope from news of freedom",
        ], scale=0.86, box=0)
        # --- Band 5: How They Resisted
        self.next_band(5)
        self.write_rows(5, "How They Resisted", [
            "Quiet resistance",
            "Running away; Hangklip caves",
            "1808: Louis of Mauritius",
        ], scale=0.86, box=0)
        # --- Band 6: What Happened?
        self.next_band(6)
        self.write_rows(6, "What Happened?", [
            "Harsh punishments",
            "Stricter rules",
            "Pressure to end slavery, 1834",
        ], scale=0.86, box=0)
        self.wait(4)
