### subtopic_1 — What a Capacitor Is and How It Stores Charge
**Assistant:** Why does the charging slow down? The battery is pushing just as hard the whole time.

**Tutor:** The battery is, but it is pushing against something that pushes back more and more. At the start the capacitor is empty, so it has no voltage of its own and the battery's whole voltage is across the resistor, driving the largest current. As charge arrives on the plates the capacitor develops a voltage between them, opposing the battery, and the voltage left to drive current through the resistor is the battery voltage minus the capacitor voltage. Less voltage across the resistor means less current, by Ohm's law, so the charge arrives more slowly, which raises the capacitor voltage more slowly, and so on. The curve flattens out and only ever approaches the battery voltage. Discharging mirrors it: a full capacitor drives a big current through the LED, loses charge, has less voltage, drives less current, and fades gently rather than cutting off. That gentle curve is what the eye sees as the LED dimming over a second.

***

### subtopic_2 — Charging, Discharging and the Time It Takes
**Assistant:** Why are electrolytic capacitors polarised when ceramic ones are not?

**Tutor:** Because of how the insulating layer is made. In a ceramic or film capacitor the dielectric is a slab of ceramic or plastic, the same material whichever way the voltage is applied, so it does not care about direction. In an electrolytic, the insulator is an extraordinarily thin film of aluminium oxide grown on one of the foils by passing current through a liquid electrolyte in a particular direction during manufacture; that thin film is why electrolytics pack so much capacitance into a small can. The film only stays intact while the voltage is applied the way it was formed, positive on the oxide-coated foil. Reverse it and the oxide breaks down, current flows through the electrolyte, the liquid heats and makes gas, and the can swells and bursts. So the stripe is not a convention; it marks the only direction in which the insulator actually insulates.

***

### subtopic_3 — Capacitor Types, Polarity and Uses in Simple Circuits
**Assistant:** Could a capacitor replace the battery in the PAT indicator?

**Tutor:** No, and working out why is a good exercise in sizes. The indicator LED draws about 5 milliamperes while warning. A 1000 microfarad capacitor charged to 4.5 volts holds a charge of 4.5 millicoulombs, which at 5 milliamperes lasts under a second, and in practice the LED fades well before the capacitor is empty because its voltage drops below the LED's 2 volts. To hold the LED on for a day you would need a capacitor hundreds of thousands of times larger, far bigger than the tank. A battery, by contrast, keeps making charge chemically for thousands of hours at a steady voltage. What a capacitor can do in the PAT is small and useful: smooth a flicker, hold the LED on for a second or two after a momentary sensor contact so a brief dip in the water does not blink the warning, or help a transistor pair oscillate to flash the LED. Storage for a moment, not supply for a day.
