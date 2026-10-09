### subtopic_1 — The Diode: A One-Way Valve for Current
**Assistant:** If the LED only drops 2 volts, why does it not just take 2 volts from the battery and leave the rest alone?

**Tutor:** Because voltage is not something a component takes a portion of; it is the push the battery applies across whatever is connected to it, and the whole 4.5 volts is applied across the LED when nothing else is in the loop. The LED's nature is to hold about 2 volts across itself and let the current rise steeply if anything tries to push the voltage higher. So the battery pushes, the LED cannot hold the extra 2.5 volts back, and the current rises until the only thing limiting it is the battery's own internal resistance and the thin wires, which allow far more than the 20 milliamperes the LED can survive. The junction inside overheats and fails. A resistor in series changes the picture: now the 4.5 volts is shared, the LED keeps its 2 volts and the resistor takes the remaining 2.5, and the resistor's value sets the current, because a resistor is a component that does take a definite voltage for a definite current. That is why the resistor, not the LED, is in charge of how much flows.

***

### subtopic_2 — The LED: A Diode That Lights, and Why It Needs a Resistor
**Assistant:** Why do chargers need diodes if a battery only takes current one way anyway?

**Tutor:** Because the mains supply is alternating current, which reverses direction fifty times a second, and a battery charged by that would be charged for a hundredth of a second and then discharged for the next hundredth, netting nothing and heating up. The charger must first turn the alternating current into current that flows one way, and that is what diodes do: arranged as a rectifier, they pass the half-cycles in one direction and block the half-cycles in the other, or, in a bridge of four diodes, flip the backward half-cycles so that all the current arrives the same way round. A capacitor then smooths the bumps, a component met later in the term. So the diode is not there because the battery is fussy; it is there because the supply keeps changing its mind and the battery needs a decision made for it.

***

### subtopic_3 — Using LEDs as Indicators in the PAT Device
**Assistant:** Can I use two LEDs in series on one resistor to get more light?

**Tutor:** Yes, if the battery voltage is high enough, and it is a good way to make the PAT indicator brighter without doubling the current. Two red LEDs in series drop about 2 volts each, 4 volts in total, leaving only 0.5 volts for the resistor on a 4.5 volt battery, which works but is marginal; as the battery runs down below about 4.2 volts the LEDs will dim and go out early. On a 6 volt battery, four cells, two LEDs in series drop 4 volts and leave 2 volts for the resistor, which at 10 milliamperes is 200 ohms, a comfortable arrangement that gives two LEDs' worth of light for one LED's current. What you must not do is put two LEDs in parallel on one resistor: tiny differences between the LEDs mean one takes most of the current and glows while the other barely lights, and the bright one may be overdriven. Series with one resistor is fine; parallel needs a resistor each.
