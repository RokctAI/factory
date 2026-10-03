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

# Band-layout whiteboard scene for slave-life-and-legacy-islam-and-afrikaans (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/180/200/190/90/90/90 of 1020 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SlaveLifeAndLegacyIslamAndAfrikaansSession(MovingCameraScene):
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
        # --- Band 0: Work and Daily Life
        self.write_rows(0, "Work and Daily Life", [
            "Farms: wheat, vines, wine, livestock",
            "Town: domestic work and skilled trades",
            "Long hours, basic food, no shoes",
            "Women worked in fields and houses",
        ], scale=0.86, box=1)
        # --- Band 1: Control, Punishment and Family
        self.next_band(1)
        self.write_rows(1, "Control, Punishment and Family", [
            "Passes; no legal marriage; families sold apart",
            "Whipping and public punishments",
            "Families and communities still formed",
            "Manumission: freed by owner or self-purchase",
        ], scale=0.8, box=3)
        # --- Band 2: Legacy: Islam at the Cape
        self.next_band(2)
        self.write_rows(2, "Legacy: Islam at the Cape", [
            "Exiles and slaves from Indonesia and India",
            "1694: Sheikh Yusuf exiled to the Cape",
            "Tuan Guru: first madrasah 1793",
            "1794: Auwal Mosque, Bo-Kaap",
        ], scale=0.86, box=2)
        # --- Band 3: Legacy: Afrikaans and Culture
        self.next_band(3)
        self.write_rows(3, "Legacy: Afrikaans and Culture", [
            "Afrikaans grew from Dutch through many speakers",
            "Malay, Portuguese creole, Khoe words",
            "Arabic-Afrikaans: early written Afrikaans",
            "Cuisine, architecture, Kaapse Klopse",
        ], scale=0.8, box=4)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Daily Life
        self.next_band(4)
        self.write_rows(4, "Daily Life", [
            "Farms and houses",
            "No shoes, no legal marriage",
            "Families and communities still formed",
        ], scale=0.86, box=0)
        # --- Band 5: Islam
        self.next_band(5)
        self.write_rows(5, "Islam", [
            "Sheikh Yusuf, 1694",
            "Tuan Guru and the first mosque",
            "Community, dignity, learning",
        ], scale=0.86, box=0)
        # --- Band 6: Afrikaans
        self.next_band(6)
        self.write_rows(6, "Afrikaans", [
            "Afrikaans: many contributors",
            "Words from Malay and Khoe",
            "Food and music",
        ], scale=0.86, box=0)
        self.wait(4)
