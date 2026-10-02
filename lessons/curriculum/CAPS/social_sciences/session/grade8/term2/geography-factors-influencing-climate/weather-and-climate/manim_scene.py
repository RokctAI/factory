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

# Band-layout whiteboard scene for weather-and-climate (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (300/250/280/240/150/150/150 of 1520 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class WeatherAndClimateSession(MovingCameraScene):
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
        # --- Band 0: Weather and climate
        self.write_rows(0, "Weather and climate", [
            "Weather: now, hours and days",
            "Climate: average over about 30 years",
            "Climate is what you expect",
            "Weather is what you get",
        ], scale=0.86, box=1)
        # --- Band 1: Temperature and humidity
        self.next_band(1)
        self.write_rows(1, "Temperature and humidity", [
            "Stevenson screen: shade, airflow, height",
            "Mean = (max + min) $\\div$ 2",
            "(28 + 12) $\\div$ 2 = 20",
            "Relative humidity: percent of saturation",
        ], scale=0.86, box=2)
        # --- Band 2: Wind and precipitation
        self.next_band(2)
        self.write_rows(2, "Wind and precipitation", [
            "Direction: where it comes from",
            "Vane for direction; anemometer for speed",
            "Rain, drizzle, snow, sleet, hail",
            "1 mm on 1 m² = 1 litre",
        ], scale=0.86, box=1)
        # --- Band 3: Records and forecasts
        self.next_band(3)
        self.write_rows(3, "Records and forecasts", [
            "Weather service: stations, radar, satellites",
            "Synoptic charts and isobars",
            "40 $\\div$ 5 = 8 mm a day",
            "Thirty years of records make a climate",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: What you get, what you expect
        self.next_band(4)
        self.write_rows(4, "What you get, what you expect", [
            "Weather changes in an hour",
            "Climate from thirty years",
        ], scale=0.86, box=1)
        # --- Band 5: How hot and how damp
        self.next_band(5)
        self.write_rows(5, "How hot and how damp", [
            "Thermometer in the shade",
            "Humid air feels sticky",
        ], scale=0.86, box=0)
        # --- Band 6: Wind and rain
        self.next_band(6)
        self.write_rows(6, "Wind and rain", [
            "Vane, cups and gauge",
            "Rain measured in millimetres",
        ], scale=0.86, box=1)
        self.wait(4)
