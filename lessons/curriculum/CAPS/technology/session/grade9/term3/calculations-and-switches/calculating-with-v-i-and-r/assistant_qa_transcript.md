### subtopic_1 — Setting Out an Ohm's Law Calculation
**Assistant:** Why does the larger resistor in a series pair get more of the voltage?

**Tutor:** Because they share one current and voltage is current times resistance. In series there is only one path, so exactly the same current flows through the 470 ohm resistor and the 330 ohm resistor. Apply Ohm's law to each one on its own: the voltage across the 470 is the current times 470, and across the 330 it is the same current times 330, so the 470 has more volts across it, in the ratio 470 to 330. The two voltages must add up to the battery's 4.5 volts because that is the total push available round the loop. This is the same reason the LED resistor works: the LED insists on its 2 volts, and the resistor, carrying the same current, takes whatever is left; choosing the resistor's value is choosing what current makes those leftover volts appear across it.

***

### subtopic_2 — Resistors in Series and the Shared Current
**Assistant:** How can the parallel pair have less resistance than either resistor when I have added a resistor?

**Tutor:** Because you have added a path, not a hindrance. Resistance is about how hard it is for current to get from one point to another. Put a second resistor across the first and the current now has two routes between the same two points; each route carries the current Ohm's law gives it for the full voltage, and the total current is the sum. More current for the same voltage means lower resistance, by definition. Two equal resistors give exactly twice the current and so half the resistance; adding a third equal one gives a third of the original. If the added resistor is very large, it adds only a trickle and barely lowers the combined resistance, which is why the combined value is always just below the smallest branch rather than wildly lower. The water picture helps: two pipes side by side carry more than one, however narrow the second pipe is.

***

### subtopic_3 — Resistors in Parallel and Calculations for the PAT Circuit
**Assistant:** The brief said six months of battery. Our LED runs the battery flat in two weeks. Have we failed?

**Tutor:** No, because the two weeks is the warning time, not the standby time, and the device spends almost all its life in standby. Battery life is capacity divided by the average current, and the average depends on how the device is used. With the reed switch open, which is whenever the tank is above the low mark, the circuit is broken and the current is zero; the battery is losing nothing except its own slow self-discharge, which for alkaline cells is a few percent a year. The LED only draws its 5.3 milliamperes while the tank is actually low, and the family will refill or wait for the municipal supply within a day or two, so the warning might run for a total of a few days a month. Add up a year of that and the battery is still mostly full. The specification is met because of the design choice to use a sensor that is an open switch in standby; a transistor circuit that drew a few milliamperes continuously would have failed it, and the calculation is what shows the difference.
