# Part 1 — Expert

This session covers sensors: the light-dependent resistor whose resistance decreases with light, thermistors of negative and positive temperature coefficient types, and touch or moisture detectors. The anchor is a bench in Upington with a multimeter on ohms clipped to an LDR, the reading dropping from 800 kilohms under a cupped hand down to 300 ohms in the window light, then clipped to a thermistor that falls from 10 kilohms on the bench to 3 kilohms between warm fingers. The governing idea is that these sensors are resistors whose value depends on light, temperature or the presence of a conducting bridge, that their changes are too weak to drive a load directly but are ideal for the base of a transistor, and that the right sensor for a device is chosen by what must be detected and how large and clean the change is. Describing the behaviour of each sensor, testing it with a meter and selecting one for a purpose are examinable.

## Subtopic: The Light-Dependent Resistor: Resistance Falls as Light Rises

The light-dependent resistor is a disc of a semiconducting material, usually cadmium sulphide, with a zigzag track on its face and two legs. In darkness its resistance is high, hundreds of kilohms to a megohm; as light falls on the track, the material releases more charge carriers and the resistance drops, to a few kilohms in room light and a few hundred ohms in direct sun. The relationship is smooth and inverse: more light, less resistance. The LDR has no polarity and can be connected either way round. Its symbol is a resistor rectangle with two arrows pointing in at it, representing light arriving, sometimes inside a circle.

Testing an LDR with a multimeter on ohms shows the behaviour directly: cover it with a hand and the reading climbs; uncover it and the reading falls; shine a torch on it and it falls further. Recording three readings, dark, room, bright, gives a sense of the range and is a good investigation page for the PAT. The LDR responds in a fraction of a second, fast enough for a night light but not for anything like a light beam counting fast objects.

Uses: automatic street lights that come on at dusk, the night light of the PAT scenarios, cameras setting their exposure, a light meter, and a simple alarm that triggers when a beam of light to the LDR is broken. In a transistor circuit the LDR is placed in series with a fixed resistor across the supply to make a voltage divider, and the base is taken from the junction between them; the fixed resistor's value is chosen so that the base voltage crosses the 0.6 volt turn-on point at the light level wanted, and a variable resistor in its place lets the user set that level.

The questions for this section are with you now: how the LDR's resistance changes with light, testing it with a meter, and its uses and placement in a transistor circuit.

## Subtopic: Thermistors: Negative and Positive Temperature Types

A thermistor is a resistor whose value changes strongly with temperature. The common type is the negative temperature coefficient thermistor, NTC: its resistance falls as it warms, from perhaps 10 kilohms at room temperature to 3 kilohms when held between warm fingers and a few hundred ohms in hot water. The positive temperature coefficient type, PTC, does the opposite: its resistance rises as it warms, often sharply above a certain temperature, which makes it useful as a self-resetting fuse that limits current when a circuit gets hot. The thermistor's symbol is a resistor rectangle with a diagonal line through it and the Greek letter theta or the letter t beside it; a minus or plus sign shows the type.

Testing a thermistor is the same as the LDR: multimeter on ohms, read at room temperature, then warm it between fingers or near a lamp and watch the reading fall for an NTC or rise for a PTC. Do not put it in a flame; it is a small bead or disc and burns. Record a table of temperature and resistance using a thermometer and warm water for a proper investigation. The response is slower than the LDR, a few seconds, because the bead itself must warm.

Uses: fire and overheating alarms, a thermostat for an incubator or a geyser, a temperature display, the fan control in a computer, and the engine temperature sensor in a car. In a transistor circuit the NTC thermistor takes the place of the LDR in the voltage divider; put it in the upper position and the transistor turns on as the thermistor warms, the fire alarm; put it in the lower position and the transistor turns on as it cools, the frost warning for a seedling tray. The variable resistor beside it sets the temperature at which the switch happens, which is the circuit built in a later session.

The questions for this section are with you now: NTC and PTC thermistors and their symbol, testing and investigating a thermistor, and its uses and placement.

## Subtopic: Touch and Moisture Detectors and Choosing a Sensor for the PAT

Touch and moisture detectors are the simplest sensors of all: two metal contacts close together with a gap between them that does not conduct. Bridge the gap with something that conducts a little, a fingertip or damp soil, and a small current can pass, far too small to light an LED but enough for a transistor base. A touch switch is two bare pads or a pair of screw heads on the box; touching both at once completes the base circuit and the transistor turns the load on. A moisture detector is two probes, nails or strips of copper, pushed into soil or placed at the bottom of a tank, and the water or damp soil between them forms the bridge.

The behaviour is useful and limited. Dry soil or air between the probes is nearly an open circuit; wet soil or water is a resistance of a few kilohms to a few tens of kilohms, depending on how pure the water is and how far apart the probes are. Tap water with its minerals conducts; distilled water barely does, which is why a probe sensor in a rainwater tank must be tested with the actual water. Probes corrode, especially the positive one, so stainless steel or carbon rods last longer than iron nails, and a design that only passes current when checking, not continuously, slows the corrosion. The investigation records the resistance between the probes dry, damp and wet.

Choosing a sensor for the PAT follows the need. Detecting darkness: LDR. Detecting heat or cold: NTC thermistor. Detecting a hand or a person: touch plates, or a pressure mat as a switch. Detecting water level or wet soil: probes, or a float switch or reed switch if a clean on-off is wanted without corrosion. Each sensor's change is recorded from the meter test, and the one with the largest, cleanest change at the condition to be detected is chosen; a sensor whose resistance barely moves gives a transistor that hovers half on, which the previous session showed is wasteful and unreliable. The error museum, four exhibits. One: expecting an LDR or thermistor to light an LED directly. Two: a thermistor in a flame. Three: probes tested in tap water for a device that will sit in rainwater. Four: an LDR placed where the LED's own light falls on it, so the circuit flickers.

The questions for this section are with you now: touch and moisture detectors as bridged contacts, their behaviour and corrosion, and choosing a sensor for the PAT.

# Part 2 — Simplifier

Now the same lesson again with the multimeter clipped to the LDR and then the thermistor on the bench in Upington — plain words, same facts.

## Subtopic: A Resistor That Reacts to Light

An LDR is a resistor that changes with light. Dark: hundreds of kilohms. Room light: a few kilohms. Sun: a few hundred ohms. More light, less resistance. Either way round. Symbol: a rectangle with two arrows coming in.

Test it: meter on ohms, cover it with a hand and the reading climbs; uncover it and it falls; torch on, it falls more. Write the three readings.

Street lights, night lights, cameras. In a circuit: LDR and a fixed resistor in series across the battery, base taken from the middle. The fixed resistor sets when it switches; make it variable and the user can set it.

Keep a resistor that reacts to light in mind and try the questions for this part: the LDR.

## Subtopic: A Resistor That Reacts to Heat

A thermistor is a resistor that changes with heat. NTC, the common one: warmer means lower resistance, 10 kilohms on the bench, 3 kilohms in warm fingers. PTC: warmer means higher, used as a self-resetting fuse. Symbol: a rectangle with a slash and a t.

Test it the same way: meter on ohms, warm it in your fingers, watch it fall for NTC. Never in a flame. Table of temperature and resistance for a proper investigation.

Fire alarms, thermostats, computer fans, car engines. In a circuit it replaces the LDR in the divider. Upper position: on when hot. Lower position: on when cold.

Hold a resistor that reacts to heat in mind and try this part's questions: thermistors.

## Subtopic: Two Contacts and Something That Conducts

Touch and moisture: two contacts with a gap. Bridge the gap with a fingertip or damp soil and a trickle flows, enough for a transistor base. Touch pads on the box; probes in the soil or tank.

Dry: open. Wet: a few kilohms to tens of kilohms. Tap water conducts, rainwater barely, so test with the real water. Probes corrode; use stainless or carbon and only pass current when checking.

Choose by the need: dark, LDR; hot or cold, NTC; a hand, touch pads; water or wet soil, probes, or a float or reed switch for a clean click. Pick the sensor with the biggest, cleanest change.

Pocket summary of the lesson. Sensors are resistors that respond to the world. The LDR's resistance falls as light rises; the NTC thermistor's falls as it warms and the PTC's rises; touch and moisture detectors are two contacts bridged by skin or water. Each is tested with a multimeter on ohms and recorded dark, room and bright or cold, room and warm or dry, damp and wet. None can drive a load directly; each feeds a transistor base through a divider, and the sensor with the largest clean change at the condition to be detected is chosen.

Hold two contacts and something that conducts, and take the final questions of the lesson: touch, moisture and choosing.
