### subtopic_1 — Drawing the LED Circuit: 470 Ohm Resistor, Switch and 4.5 Volt Battery
**Assistant:** Why does the LDR circuit need a transistor but the LED circuit does not?

**Tutor:** Because of what each sensor or switch can carry. In the LED circuit the switch is a metal contact that can pass the LED's 5 milliamperes without any loss, so battery, switch, resistor and LED in one loop is enough. In the LDR circuit the sensor is a resistor whose value slides between a few hundred ohms and a megohm; even at its lowest it would pass only a weak current, and it never switches cleanly off, so a buzzer wired straight through it would either hum faintly all the time or never sound properly. The transistor solves both problems: the LDR only has to move the base voltage past 0.6 volts, which takes a tiny current, and the transistor then passes the buzzer's full current from the battery and does it with a clean on and off. Any sensor that is a changing resistance rather than a true switch, an LDR, a thermistor, a pair of probes, needs this arrangement; a float switch or reed switch does not.

***

### subtopic_2 — Drawing the LDR and Buzzer Circuit on a 3 Volt Battery
**Assistant:** The buzzer in the LDR circuit hums softly even in bright light. What is wrong?

**Tutor:** Nothing is broken; the transistor is sitting just at the edge of turning on, which means the divider is set wrong for the light in the room. In bright light the LDR should pull the junction close to negative so the base is well below 0.6 volts. If the room is not bright enough, or the fixed resistor is too small, the junction sits near 0.5 or 0.6 volts and the transistor is partly on, letting a trickle through the buzzer, which hums. Three fixes, in order of ease: turn the variable resistor, if there is one, until the hum just stops; replace a 10 kilohm fixed resistor with a larger one, 22 or 47 kilohms, so the junction sits lower for the same LDR; or move the LDR to where the light it is meant to sense actually falls on it, away from shadow. This is also why the lesson said sensors with a large, clean change make better switches: the LDR's swing between this room and darkness must be big enough to take the base well past the threshold in both directions.

***

### subtopic_3 — Building Both on a Breadboard and Testing Against the Diagram
**Assistant:** Why check the build against the diagram before connecting the battery? Would testing not find the fault anyway?

**Tutor:** Testing finds that there is a fault; checking finds where it is before it can do damage, and some faults do damage. An LED put in backwards does no harm, it just stays dark. A transistor with its legs reversed can be destroyed the moment power is applied, an electrolytic capacitor backwards can burst, and a wire that bridges the positive rail to the negative rail shorts the battery, heats it and can start to melt the breadboard. A one-minute check, finger on each component on the diagram and eye on the matching part on the board, catches these before power touches them. It also separates two kinds of fault that feel the same when the circuit is dead: a wiring slip, which the check catches, and a design error, which only shows up in testing after the wiring is confirmed right. Builders who skip the check spend their fault-finding time doubting a good design because of a miscounted row.
