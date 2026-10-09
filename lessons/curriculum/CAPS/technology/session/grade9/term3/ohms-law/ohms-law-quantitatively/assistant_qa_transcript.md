### subtopic_1 — Voltage, Current and Resistance as Measured Quantities
**Assistant:** If Ohm's law does not work for an LED, how can we use it to choose the LED's resistor?

**Tutor:** Because we apply it to the resistor, not to the LED, and we treat the LED as what it is, a component that takes a fixed voltage. The LED's rule is simple: when it is lit it has about 2 volts across it, almost regardless of the current. The resistor's rule is Ohm's law: its current is its voltage divided by its resistance. In a series circuit they share the battery's 4.5 volts, so if the LED takes 2, the resistor has 2.5 across it; and in a series circuit they carry the same current, so whatever current Ohm's law gives for the resistor is also the LED's current. Choose the resistor so that 2.5 volts over its resistance gives the current you want for the LED. Two components, two different rules, one shared current, and the resistor is the one that obeys Ohm, so it is the one you calculate.

***

### subtopic_2 — Ohm's Law: Current Rises in Step With Voltage at Fixed Resistance
**Assistant:** Why does the temperature matter? The resistor on the bench did not feel hot.

**Tutor:** At the currents used on the bench it was not hot, which is exactly why the readings sat on a straight line and the law held. Resistance in a metal comes from electrons bumping into the vibrating atoms of the metal, and the hotter the metal, the more the atoms vibrate and the more the electrons are hindered, so resistance rises with temperature. A resistor carrying a few milliamperes warms by a fraction of a degree and its resistance changes by a fraction of a percent, invisible on a school meter. A lamp filament runs at over two thousand degrees and its resistance when hot is about ten times its resistance when cold, so a graph of current against voltage for a lamp curves over as it heats, and Ohm's law in its simple form does not describe it. Stating the condition constant temperature in the exam shows you know when the straight line can be trusted and when it cannot.

***

### subtopic_3 — The Three Forms of the Law and Simple Worked Examples
**Assistant:** Why does the formula need amperes when every current in the PAT is in milliamperes?

**Tutor:** Because the ohm is defined so that one volt across one ohm gives one ampere, and the equation V equals I R is only true with those three units together. Put milliamperes in and the answer is a thousand times wrong: 5 milliamperes times 470 ohms would appear to give 2350 volts, which is absurd for a 4.5 volt battery, whereas 0.005 amperes times 470 gives 2.35 volts, which is sensible. There is a shortcut that electronics people use: if you keep the current in milliamperes, the resistance must be in kilohms, because a thousandth times a thousand cancels; so 5 milliamperes times 0.47 kilohms is also 2.35 volts. Either way the units must match. The safest habit for the examination is to convert to amperes, write the units beside every number, and do the sense check at the end: a few volts across a resistor in a battery circuit is right, thousands of volts is a conversion slip.
