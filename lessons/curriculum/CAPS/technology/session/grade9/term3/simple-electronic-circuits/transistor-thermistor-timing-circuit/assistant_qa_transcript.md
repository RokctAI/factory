### subtopic_1 — The Circuit: Thermistor, Variable Resistor, Transistor, LED, Capacitor and Switch
**Assistant:** How do I work out the junction voltage without just guessing?

**Tutor:** Use the voltage divider rule, which is Ohm's law applied to two resistors in series. The thermistor and the variable resistor carry the same current because they are in series, and they share the supply voltage in proportion to their resistances. The voltage across the lower resistor, which is the junction voltage because the lower resistor goes to negative, is the supply times the lower resistance divided by the total resistance. With the thermistor at 10 kilohms on top and the variable resistor at 2 kilohms below, the junction is 4.5 times 2 over 12, which is 0.75 volts. Cool the thermistor to 20 kilohms and it is 4.5 times 2 over 22, about 0.41 volts. The rule works for any divider: supply times bottom over the sum. Then compare the result with 0.6 volts: above, the transistor is on; below, it is off. Two lines of arithmetic tell you the LED's state at any temperature, and that is what the examiner wants to see rather than a guess.

***

### subtopic_2 — How It Works: Sensing Temperature and Setting the Threshold
**Assistant:** Why put the capacitor on the base instead of across the LED?

**Tutor:** Because the flicker starts at the base, and the base is where a small capacitor can make a large difference. The problem is that near the threshold temperature the junction voltage wobbles a little above and below 0.6 volts, and the transistor amplifies that wobble into the LED switching fully on and off. A capacitor from base to negative has to charge and discharge through the divider and base resistors before the base voltage can change, so a brief wobble is absorbed before it reaches the base and the transistor only responds to a sustained change. The currents at the base are tiny, so a 100 microfarad capacitor gives about a second of smoothing. A capacitor across the LED would have to smooth the LED's own 5 milliampere current, which would need a far larger capacitor to achieve the same effect, and it would do nothing to stop the transistor itself switching. Smooth the control signal, not the output; it is cheaper and it works.

***

### subtopic_3 — The Capacitor's Role, Building the Circuit and Adapting It
**Assistant:** The brief for our team's device is a frost warning for seedlings. Which arrangement, and does the delay help or hurt?

**Tutor:** Sensor below, which is the inverted arrangement, and the delay helps. For a frost warning the LED must come on when the thermistor is cold. The NTC thermistor's resistance rises as it cools, so to make the junction rise with cold the thermistor must be the lower resistor, from the junction to negative, with the variable resistor on top from positive to the junction; then as the thermistor's resistance climbs, it takes a larger share of the supply and the junction rises past 0.6 volts, switching the LED on. The variable resistor is set in a bowl of iced water so the LED just comes on near 2 or 3 degrees, before actual frost. The delay from the capacitor is useful here: a gust of cold air across the tray for a second should not trigger the warning, and the second or two of smoothing ignores it, while a real drop in temperature over minutes brings the LED on steadily. For a fire alarm the same delay would be a drawback, and a smaller capacitor would be chosen.
